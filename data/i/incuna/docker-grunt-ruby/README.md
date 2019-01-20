# docker-grunt

A basic dockerfile to create a node and ruby environment for running grunt and compass (e.g. with https://github.com/gruntjs/grunt-contrib-compass)

This is available via the docker hub registry as `incuna/grunt-ruby`

# Contributing changes
This repo provides two Dockerfiles:
* Standard build with just the node and ruby environment
* An "onbuild" version, which will automatically copy and install packages from `Gemfile` and `package.json` files in the project directory. For more information on `ONBUILD`, see the [Docker documentation](https://docs.docker.com/reference/builder/#onbuild)

The onbuild version lives in the `/onbuild` directory (as per docker hub conventions) and should always be a direct copy of the main Dockerfile with the `ONBUILD` instructions added at the end.

**Any changes should be made to both Dockerfiles**

# Releasing
* Update changelog
* Make sure both Dockerfiles have been updated
* Tag this github repository with a new version tag
* Go to the docker hub, and add the same tags to the automated image build. Add a tag for the normal and the onbuild versions
