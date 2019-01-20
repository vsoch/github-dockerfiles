# Docker Container for CKAN 2.5.3

This is a first attempt to build [CKAN 2.5.3](https://ckan.org/) within a docker container.

## Used docker images

The following images are used:
- [ckan_app:2.5.3](https://hub.docker.com/r/dkdde/ckan_app/) this is the main container
- [postgres:9.5-alpine](https://hub.docker.com/_/postgres/)
- [ckan_solr:2.5.3-alpine](https://hub.docker.com/r/dkdde/ckan_solr/) modified Solr 4.8
- [redis:3.2](https://hub.docker.com/_/redis/) this is not mandatory

## Starting the container

Simply clone this repo and use [Docker Compose](https://docs.docker.com/compose/) to fire up the container with `docker-compose up`.

## Fix me

- in order to use both `nginx` and `apache` for CKAN, [supervisord](http://supervisord.org/) is used to start both services
- initial CKAN configuration is executed once via a [supervisor script](./2_5_3/app/scripts/configure_ckan) which uses a delay of 5 sec to be executed (this might break on slow systems and should be changed)

## TODO

-
- write a more sophisticated README :)
