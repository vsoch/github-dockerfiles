# dkdde/phantomjs-binaries

## Docker Data Volume Container phantomjs-binaries

This Docker image `dkdde/phantomjs-binaries` consists of

* static compiled [phantomjs](https://github.com/ariya/phantomjs) binaries (v1.9.2, v1.9.7 and v2.1.1)

to be run as [Docker Data Volume Container](https://docs.docker.com/engine/tutorials/dockervolumes/).

### Installation/Setup

Download latest Docker image:

    $ docker pull dkdde/phantomjs-binaries

### Usage

Create data volume container, name it `phantomjs` and expose `/home/jenkins/.phantomjs`:

    $ docker create -v /home/jenkins/.phantomjs --name phantomjs dkdde/phantomjs-binaries:latest

### Development

[Clone project](https://github.com/dkd/docker-dkdde-phantomjs-binaries) and copy extracted [phantomjs binary build archives](http://phantomjs.org/build.html) into the given phantomjs directory. Mind appropriate version numbers of subdirectories.

    $ git clone https://github.com/dkd/docker-dkdde-phantomjs-binaries.git
    $ cd docker-dkdde-phantomjs-binaries

Build image, tag appropriately and push to Docker Hub:

    $ docker build . --tag dkdde/phantomjs-binaries
    $ docker push dkdde/phantomjs-binaries
