Kazoo Docker Meta
=================

A container to build and run Kazoo Docker Fleet.

How to run
==========

```sh
docker build -t jamhed/kazoo/meta .
docker run -v /var/run/docker.sock:/var/run/docker.sock --entrypoint ./build.sh -ti kazoo/meta
docker run -v /var/run/docker.sock:/var/run/docker.sock --entrypoint ./run.sh -ti kazoo/meta
```

How it works
============

The goal is to simplify build process for non-linux environments. The container needs to have access
to the host Docker and will build and run images on the host.

# Kazoo CI

Continious integration server. Accepts Github webhooks and trigger commit-dependent build and test process.
Reports test results back to Github, and provides test run files.

# Build and test commit manually

```sh
docker exec -ti kazoo-ci ./build.sh 73fde591d5
```
# Kazoo container

## Default build

By default the latest version of Kazoo is checked out on build. It is possible to override this by
specifying commit number and repository to build.sh command:
```sh
./build.sh [COMMIT] [REPO]
```

## Development build

If you already have Kazoo sources and just want to run one or more Kazoo instances exactly this version
then you need to specify SKIP\_BUILD environment variable before build:
```sh
SKIP_BUILD=1 ./build.sh
```

In this case no Kazoo source will be checked out, instead the container will try to build and run
the source code on container startup, and you will be required to provide Kazoo source tree as Docker volume:
```sh
KAZOO_SOURCE=/home/user/kazoo-source ./run.sh
```

## UID/GID matching

In order Kazoo container to write files to provided volume owner of the mounted folder must be the same numerical
value as in container, therefore we're trying to guess and match it on build process.
