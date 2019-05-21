# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
from __future__ import absolute_import

import argparse
import os
import subprocess

PY2_CPU_BINARY = 'https://files.pythonhosted.org/packages/71/64/49c5125befd5e0f0e17f115d55cb78080adacbead9d19f253afd0157656a/mxnet-1.3.0.post0-py2.py3-none-manylinux1_x86_64.whl'  # noqa
PY3_CPU_BINARY = 'https://files.pythonhosted.org/packages/71/64/49c5125befd5e0f0e17f115d55cb78080adacbead9d19f253afd0157656a/mxnet-1.3.0.post0-py2.py3-none-manylinux1_x86_64.whl'  # noqa
PY2_GPU_BINARY = 'https://files.pythonhosted.org/packages/52/8b/3f9cfe199e592b0723617e5d1919b83022f05cc359bd1885f7d1e9ce4758/mxnet_cu90mkl-1.3.0.post0-py2.py3-none-manylinux1_x86_64.whl'  # noqa
PY3_GPU_BINARY = 'https://files.pythonhosted.org/packages/52/8b/3f9cfe199e592b0723617e5d1919b83022f05cc359bd1885f7d1e9ce4758/mxnet_cu90mkl-1.3.0.post0-py2.py3-none-manylinux1_x86_64.whl'  # noqa
DEFAULT_REGION = 'us-west-2'


def _parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--account')
    parser.add_argument('--version')
    parser.add_argument('--repo')
    parser.add_argument('--region', default=DEFAULT_REGION)
    parser.add_argument('--py2-cpu-binary', type=str, default=PY2_CPU_BINARY)
    parser.add_argument('--py3-cpu-binary', type=str, default=PY3_CPU_BINARY)
    parser.add_argument('--py2-gpu-binary', type=str, default=PY2_GPU_BINARY)
    parser.add_argument('--py3-gpu-binary', type=str, default=PY3_GPU_BINARY)

    return parser.parse_args()


args = _parse_args()
binaries = {
    'py2-cpu': args.py2_cpu_binary,
    'py3-cpu': args.py3_cpu_binary,
    'py2-gpu': args.py2_gpu_binary,
    'py3-gpu': args.py3_gpu_binary
}

build_dir = os.path.join('docker', args.version, 'final')
prev_dir = os.getcwd()
os.chdir(build_dir)

# Run docker-login so we can pull the cached image
login_cmd = subprocess.check_output(
    'aws ecr get-login --no-include-email --registry-id {}'.format(args.account).split())
print('Executing docker login command: '.format(login_cmd))
subprocess.check_call(login_cmd.split())

for arch in ['cpu', 'gpu']:
    for py_version in ['2', '3']:
        binary_url = binaries['py{}-{}'.format(py_version, arch)]
        binary_file = os.path.basename(binary_url)
        cmd = 'wget -O {} {}'.format(binary_file, binary_url)
        print('Downloading binary file: {}'.format(cmd))
        subprocess.check_call(cmd.split())

        tag = '{}-{}-py{}'.format(args.version, arch, py_version)
        dest = '{}:{}'.format(args.repo, tag)
        prev_image_uri = '{}.dkr.ecr.{}.amazonaws.com/{}'.format(args.account, args.region, dest)
        dockerfile = os.path.join(build_dir, 'Dockerfile.{}'.format(arch))

        tar_file = subprocess.check_output('ls sagemaker_mxnet_container*.tar.gz',
                                           shell=True).strip().decode('ascii')
        print('framework_support_installable: {}'.format(os.path.basename(tar_file)))

        build_cmd = [
            'docker', 'build',
            '-f', dockerfile,
            '--cache-from', prev_image_uri,
            '--build-arg', 'py_version={}'.format(py_version),
            '--build-arg', 'framework_support_installable={}'.format(tar_file),
            '--build-arg', 'framework_installable={}'.format(binary_file),
            '-t', dest,
            '.',
        ]
        print('Building docker image: {}'.format(' '.join(build_cmd)))
        subprocess.check_call(build_cmd)

        print('Deleting binary file {}'.format(binary_file))
        subprocess.check_call('rm {}'.format(binary_file).split())

os.chdir(prev_dir)
