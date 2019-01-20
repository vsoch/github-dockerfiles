# subgraph_pound

This purpose of this project is to automatically create Subgraph OS ISOs using 
Debian `live-build`. 

## Disclaimer

`subgraph_pound` may be of use or interest to others, however, this is not 
intended to be a `build-yr-own-iso` project. We don't officially support
third-party ISO building. The simple reason for this is that we automate our
internal processes to save us time and effort. Providing support costs us time
and effort. 

This project works OOTB for us but it may not work for others. It may reasonably
(and often temporarily) fail to build an ISO due to external circumstances that
are outside of our control. Differences in build environment or attempts to
customize the build configuration may also cause build failures. This software
comes with no warranty. If it works for you, great. If it doesn't, you're on
your own.

## Setting up the build environment

The project relies on `docker` and `docker-compose` to instrument the
`live-build` software with a backing `apt-cacher-ng` instance to speed up
subsequent builds. 

Installing `docker` and `docker-compose` is a task left up to the user based on 
their host environment. It is best to use recent versions of these tools. 

Further information on installing docker can be found [here](https://docs.docker.com/engine/installation/).

*NOTE*: We recommend against trying to build within Subgraph OS. Firstly, the 
build dependencies need some help to install cleanly. Secondly, building over 
Tor will be slow and may possible time out or fail. Lastly, dpkg will eventually
die during the build when PaX kills postinst commands, causing the build to fail. 
For the last issue, there is no easy workaround.

## Creating an ISO

To create an ISO, run the following commands:
```
$ make
$ make run
```

At the end of a successful build, the ISO file will be located in the following
location:
```
/var/builds/iso/<USER>/<BUILD_START_DATE>/live-image-amd64.hybrid.iso
```

## Staging

`live-build` provides a number of ways to change run-time configuration. For our
purposes, we sometimes use these capabilities to stage things. The most common
case is to stage new packages for testing in an ISO. The other case is that
sometimes we want to modify some behavior in `live-build` through run-time
hooks.

### Staging packages

It is possible to stage new packages simply by dropping `.debs` into the
following directory of this repository:
```
livebuilder/staging_packages/
```

To ensure that these packages are included in the next ISO build, run `make` and 
`make run` as described above. The build script will copy the staging packages
into the `live-build` configuration. When the ISO is created, the staging
packages will take precedence over the versions that are available in the APT
repositories for Subgraph OS.

### Staging hooks

`live-build` run-time hooks can be staged by dropping `*.hooks.*` files in the
following directory of this repository:
```
livebuilder/staging_hooks/
```

To ensure that the hooks are included in the next ISO build, run `make` and
`make run` as described above. The build script will copy the staging hooks into
the `live-build` configuration. During the next ISO build, these hooks will be
run at their appropriate phase.

## Docker base image

To more reliably build Subgraph OS, we have created a base image (based on
Debian testing) that is known to work. It is hosted on Docker Hub and will be
pulled automatically when the build process runs. We update the base image
occasionally to bring in new versions of the base operating system and the build
dependencies.

### Base image creation

We have created our base image using the following commands:
```
# debootstrap --include=git,live-build,live-config,ca-certificates,cpio,apt-utils --variant=minbase testing livebuilder_testing
# tar -C livebuilder_testing -c . | docker import - livebuilder_testing
```


