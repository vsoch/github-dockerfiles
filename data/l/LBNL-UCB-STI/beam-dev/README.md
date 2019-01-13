# beam-dev

[![Docker Build Statu](https://img.shields.io/docker/build/beamframework/beam-dev.svg)](https://hub.docker.com/r/beamframework/beam-dev/)
[![Docker Automated buil](https://img.shields.io/docker/automated/beamframework/beam-dev.svg)](https://hub.docker.com/r/beamframework/beam-dev/)

Development environment for the BEAM modeling framework.

## How to use this image

### Building a Gradle project

Run this from the directory of the Beam project you want to build.

`docker run --rm -v "$PWD":/beam -v "$HOME"/.gradle:/.gradle --name beam-dev beamframework/beam-dev gradle <gradle-task>`
