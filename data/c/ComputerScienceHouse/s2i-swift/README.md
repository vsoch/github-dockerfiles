# Swift 3.0 S2I Docker Image

This repository contains the source for building Swift applications as reproducible Docker images using source-to-image. The resulting image can be run using Docker.

## Source Repository Expectations

This image expects that you have a `run.sh` file in the root directory of your repository that handles all tasks necessary for setting up and running your compiled app.

## Installation

This image is available on DockerHub. To pull it, run:

```
docker pull computersciencehouse/swift-ubuntu16.04
```

To build the image from scratch, run:

```
git clone https://github.com/ComputerScienceHouse/s2i-swift.git
cd s2i-swift
make build
```

## Standalone Usage

To build a Swift application using standalone S2I and then run the resulting image with Docker, execute:

```
s2i build [path to your app/git clone url] computersciencehouse/swift-ubuntu16.04 my-swift-app
docker run -p 8080:8080 my-swift-app
```

## OpenShift Usage

To use this image within your OpenShift cluster, use the included `openshift-swift.json` to create the ImageStream within your project. For cluster administrators, you can make this image available to all users by running the following command on a master or logged in as a user with administrative privileges on the `openshift` namespace:

```
oc create -f openshift-swift.json -n openshift
```

## Test

This repository includes the S2I test framework, which launches tests to check the functionality of a simple Swift application built on top of this image.

```
cd s2i-swift
make test
```
