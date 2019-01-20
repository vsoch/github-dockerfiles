# ci-images

Base docker images for Circle CI

This repository is hosted at https://github.com/sspinc/ci-images.

The following images are built automatically from this repository:

|Name|Image|More|
|----|-----|----|
|golang|[sspinc/ci-golang](https://hub.docker.com/r/sspinc/ci-golang/)|[README](golang/README.md)|
|jdk|[sspinc/ci-jdk](https://hub.docker.com/r/sspinc/ci-jdk/)|[README](jdk/README.md)|
|python|[sspinc/ci-python](https://hub.docker.com/r/sspinc/ci-python/)|[README](python/README.md)|

## Getting started

### Install dependencies

For macOS install brew and run `script/bootstrap`.

For Linux install the following:

* docker

### Build locally

Run `script/build <path>`.

Examples:

    $ script/build golang/1.9
    # => this will build the image sspinc/ci-golang:1.9
