# inspire-docker
[![Build Status](https://travis-ci.org/inspirehep/inspire-docker.svg?branch=master "Build Status")](https://travis-ci.org/inspirehep/inspire-docker/branches?branch=master)

## Usage

Install Docker: https://docs.docker.com/engine/installation/

To grab a Python image having (almost) all the dependencies cached for `pip-accel`
In which you can install the overlay:

```shell
docker pull inspirehep/python-base:latest
```

If you want a specific Python version you can do:
```shell
docker pull inspirehep/python-base:python2.7
```

Python 3.5 is still not compatible.

To grab an Elasticsearch image having all the plugins needed for running
the Overlay do:

```shell
docker pull inspirehep/elasticsearch:latest
```


## Testing changes to this repo

In order to test any changes you do to the Dockerfiles in this repo, you can
build and test them locally before sending a pull request:

### Build the new images

Building the images is as easy as running the docker build with the appropiate
tag, for example:

```shell
docker build -f python_base/Dockerfile -t inspirehep/python-base .
```

Or alternatively run the build script, setting up any required env vars (see
the .travis.yml for the latest possible values):

```shell
export TRAVIS_BRANCH=master
export DOCKER_PROJECT=inspirehep/python-base
export DOCKER_IMAGE_TAG=latest
export DOCKERFILE=python_base/Dockerfile
export ARGS='--build-arg=INSPIRE_PYTHON_VERSION=2.7'
./build.sh --help
./build.sh
```

That will locally build and tag the image, to verify just list the local
images:

```shell
docker images
```


### run the tests

To run the tests locally you will have to set some environment variables that
the scripts expect to be there (set by travis, see the .travis.yml file for
more example values). The script will complain if any of the env vars is not
set when running so you can just run it to check the latest need. An exampe
that works at the time of writing this:

```shell
export TRAVIS_BRANCH=master
export DOCKER_COMPOSE_VERSION=1.6.2
export DOCKER_PROJECT=inspirehep/python-base
export DOCKER_IMAGE_TAG=latest
./test.sh --help
./test.sh --no-install-compose
```
