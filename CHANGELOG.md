# Changelog

## v0.1.1 (2019-05-22)

### Bug fixes and other changes

 * remove parallelism
 * add more tests

## v0.1.0 (2019-05-21)

### Bug fixes and other changes

 * pass env vars
 * fix tox command
 * remove need for binaries
 * fix build script
 * fix build script
 * fix build script
 * add debugging
 * add debugging
 * add debugging
 * fix build script
 * fix script names and permissions
 * pick empirical number for coverage threshold
 * pick empirical number for coverage threshold
 * add py36 coverage file
 * ignore coverage in integ tests
 * bump to py36
 * fix flake8 errors with EI test
 * fix
 * fix test commands
 * fix
 * Add release buildspec
 * Fix mock_open usage
 * prevent hidden errors in buildspec
 * Update buildspec with PR number
 * Add buildspec for pr build
 * Set 'channels first' for Keras
 * add elastic inference sagemaker integ test
 * Don't use mx.eia() when allocating memory for an NDArray
 * Remove MXNET_ENGINE_TYPE default
 * Fix instance type fixture setup
 * Read framework version from Python SDK for integ test default
 * Set logging level before importing user module
 * Add EI documentation within README
 * Freeze pip version to <=18.1
 * Add env variable to make sure default encoding is utf-8
 * Add numpy array support in default serving methods
 * Add python-dev and build-essential to Dockerfiles
 * remove requests from test dependencies
 * fix response content_type handling
 * modify default model fn for eia
 * Unfreeze requests version
 * Merge pull request #53 from aws/sagemaker-containers-migration
 * Merge branch 'master' into sagemaker-containers-migration
 * Remove incompatible Dockerfiles and update README
 * Add port label to Dockerfile
 * Add integration test for importing and exporting ONNX models
 * Change parameter server hyperparameter name
 * Add integration test for inference with CSV
 * Fix unit test for csv deserialization
 * Fix inference for CSV and limit valid content types
 * Set number of model workers for inference server
 * Update testing section of the README
 * Make container set up parameter server for distributed training
 * Add default save method and update linear regression test
 * Clean up integration (local and SageMaker) tests
 * Fix serving, update integ tests, and allow user-supplied transform_fn
 * Migrate serving support
 * pin requests version
 * Switch to using MXNet 1.3 for migration and add Keras integ test
 * Add support for distributed training
 * Add tox.ini and configure coverage/flake8
 * Add single-machine training using SageMaker Containers
 * Add warning about upcoming training script format change to training log
 * fix line length
 * Install onnx in 1.2.1 containers
 * Add Dockerfiles for 1.2.1
 * Remove __all__
 * Allow the user script to be mounted locally.
 * Fix quotes so that Python 3 container can be built
 * Remove reference to dns
 * Move 1.1.0 docker files into a final folder
 * Add test and build instructions
 * Fix year in license headers
 * Add container support to install_requires
 * Add headers for Apache license
 * Remove pip installs of dependencies from Dockerfiles (redundant with
 * Add dockerfiles for building images for 1.1.0
 * Apply patch - Fix optimizer serialization for python3
 * Use instance type parameter when deploying to endpoint in functional test
 * Fix gunicorn python version for 1.0.0 gpu
 * Fix GPU image build for mxnet 0.12
 * Fix base 0.12.1 dockerfile to check out cub submodule correctly
 * Add functional test - MXNet distributed training + hosting + inference on SageMaker
 * Use nvidia-docker instead of docker when testing GPU images
 * Fix dockerfile entrypoints to use the correct python version
 * Added integ tests from internal repo + reorganized test directory structure to fit our convention
 * Add MKL patch for 1.0.0
 * Add steps for installing sagemaker_mxnet_container and sagemaker_container_support
 * Add dockerfiles for MXNet 0.12.1 and 1.0.0
 * Merge pull request #1 from jesterhazy/master
 * add mxnet container code
 * Updating initial README.md from template
 * Creating initial file from template
 * Creating initial file from template
 * Creating initial file from template
 * Creating initial file from template
 * Creating initial file from template
 * Initial commit
