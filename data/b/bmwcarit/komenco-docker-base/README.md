komenco base containers
=======================

komenco is using docker containers to run everything from production
to development, even the tests are executed in a docker container. To
be ease the creation of application specific docker containers we
provide a couple of base containers that can be extended.

In standard setups the base container is extended to contain your
application and the other containers (test, simpleid, selenium) are
used as is.

Installation
------------

### Prerequisites ###

The following software is required on your system:

* [docker](https://www.docker.com/)
* [docker-compose](https://docs.docker.com/compose/)

Many of the major distributions provide packages for docker, but as they are not
necessarily providing the latest versions of docker we recommend that you follow
the installation instructions on the docker website.

docker-compose can be currently installed via pip. Please see the
docker-compose page for up-to-date installation instructions for your system.

### Building the containers ###

After checking out this repository build the base containers by
running the build script

    ./build.sh

License
-------

This project is licensed under the MIT license.
