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
