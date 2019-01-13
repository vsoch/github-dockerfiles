This project aim at building a set of docker images for navitia.
The end result will be three images for jormungandr, kraken and tyr

We use a temporary docker image to build the other images because we want to reduce the time to build and the size of the images.

First step, build the builder:
```
    docker build -t navitia-builder .
```

Then use to build the images, you need to mount your docker's socket into the builder.
It will compile navitia from scratch and create the images
```
    docker run -v /var/run/docker.sock:/var/run/docker.sock navitia-builder
```

This should take a while.

those images should be available on dockerhub and are used in the docker compose


If you want to use them without the docker compose, you will need some configuration files and to mount them
in the different containers. You will find example for each file in the docker compose

There is a few external dependancies that are require for navitia to work:
    - rabbitmq
    - postgresql
    - redis

So first we will start our dependencies, we need one postgres database for jormungandr/tyr and one postgis for our instance
```
docker run --name postgres_jormungandr -e POSTGRES_PASSWORD=navitia -e POSTGRES_USER=jormungandr -d postgres
docker run --name postgres_default -e POSTGRES_PASSWORD=navitia -e POSTGRES_USER=default -d mdillon/postgis
docker run --name rabbitmq rabbitmq:management
```
# nav2_docker_compose
docker compose with micro containers, one for each navitia's service

# how to use
You'll need docker and docker-compose (tested with docker v1.12.1 and docker-compose v1.8.1)

Build the images:

`docker-compose build`

run them all

`docker-compose up`

you can then add some data in the `default` coverage:

The input dir in in `tyr_beat` in `/srv/ed/input/<name_of_the_coverage>`.

The easiest way is to copy the data via docker:

`docker cp data/dumb_ntfs.zip nav2dockercompose_tyr_beat_1:/srv/ed/input/default/`

(or you can change the docker-compose and make a shared volume).

Then you can query jormungandr:

`http :9090/v1/coverage/default/lines`

**Note:**

For the moment the navitia' images are not yet pushed into dockerhub, so you need to build the images in builder/
cf the builder's readme

# TODO
- push container on docker hub
- add the possibility for some containers to use the local code (first jormungandr)
- make it easy to add more kraken instances
- move the tyr and kraken images to alpine :wink:
