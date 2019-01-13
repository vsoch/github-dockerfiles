# Navitia's dev image
Docker image used to build and run navitia's test

This image should be used only for dev purpose

# build

```
docker build -t navitia-local-builder .
```

Note: you can decide the number of thread you want the compilation to use with the env var NB_THREAD.

by default the compilation uses all it can

# run

the navitia dir needs to be given as a volume and mounted in build/navitia

We also need to give the docker socket to run docker tests inside the docker

```
docker run -v {you_path_to_navitia}:/work/navitia  -v /var/run/docker.sock:/var/run/docker.sock navitia-local-builder  
```   

If you plan to do it several times, you might want to cache the compilation

```
docker run -v {your_path_to_navitia}:/work/navitia -v ${pwd}/docker_build_dir:/work/build -v /var/run/docker.sock:/var/run/docker.sock navitia-local-builder  
```   

# misc

Note: don't forget to update the submodules in you local navitia sourcesThis project aims at building a set of docker images for navitia.
The end result will be three images for jormungandr, kraken and tyr

We use a temporary docker image to build the other images because we want to reduce the time to build and the size of the images.

First step, build the builder:
```
    docker build -t navitia-builder .
```

It's possible to compile navitia when building the image, it's mostly useful when testing,
it allow to not compile at each run so it's faster to run.
```
    docker build -t navitia-builder --build-arg BUILD=1 .
```

Then use to build the images, you need to mount your docker's socket into the builder.
It will compile navitia from scratch and create the images
```
    docker run --rm -v /var/run/docker.sock:/var/run/docker.sock navitia-builder
```

This should take a while.

If you want to build the docker on your own sources you can mount your navitia sources. 
You also need to add the `n` flag to the builder for the script not to update the sources

```
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v {your_path_to_navitia}:/build/navitia navitia-builder -n
```

those images are available on dockerhub and are used in the docker compose


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
Docker compose file for artemis

the instances are listed in artemis_instances_list.yml

the file docker-artemis-instance.yml has been generated using j2cli (cf. general readme)

`j2 docker-instances.jinja2 artemis/artemis_instances_list.yml > artemis/docker-artemis-instance.yml`


To start artemis:

`docker-compose -f docker-compose.yml -f artemis/docker-artemis-instance.yml up`

# TODO
for the moment we just have the artemis platform with this, we'll need to add an artemis container and change artemis:
 - to be able to launch the binarization from another container (either by using an http call to tyr or by running `docker exec tyr_container manage.py load_data`)
 - to find a way around the `service kraken_toto start|stop` (I think we can just change artemis to work if the kraken is already started)
 - to find a way around the `service apache2 start|stop` (likewise, I think we can make artemis work with the jormungandr already started)
# Running with local python sources

You can run jormungandr with your own sources

Note: if you changed any cpp or protobuff files, you will need to rebuild all the navitia's images (cf the readme in the builder directory)

```
NAVITIA_PATH={your_own_navitia_path} docker-compose -f docker-compose.yml -f docker-compose-local-jormun.yml up
```
# navitia_docker_compose

docker-compose with micro containers, one for each navitia's service

This repository is not actively maintained, and not ready for production use.
It's currently for testing only, as far as Kisio Digital (ex CanalTP) is concerned.

## How to use
You'll need docker and docker-compose (tested with docker v1.12.1 and docker-compose v1.8.1)

### Run them all

`docker-compose up`

### Provide data

The most common provided data formats are:
* OSM .pbf for street-network data
* NTFS for Public Transport data (most tested in Navitia)  
  You can as well provide GTFS directly to Navitia, but it will be deprecated.
  This will be replaced by using first gtfs2ntfs converter available in
  [navitia_model]((https://github.com/CanalTP/navitia_model)), then providing the
  NTFS output to navitia.


You can then add some data in the `default` coverage:

The input dir in in `tyr_beat` in `/srv/ed/input/<name_of_the_coverage>`.

The easiest way is to copy the data via docker:

`docker cp data/dumb_ntfs.zip navitiadockercompose_tyr_worker_1:/srv/ed/input/default/`

`navitiadockercompose_tyr_worker_1` is the name of the container, it can be different since it's dependant of the directory name.

(or you can change the docker-compose and make a shared volume).

### Query Navitia API

Then you can query jormungandr:

http://localhost:9191/v1/coverage/default/lines

## Additional instances
If you need additional instances, you can use the `docker-instances.jinja2` to generate another docker-compose file (if you want to do some shiny service discovery instead of this quick and dirty jinja template, we'll hapilly accept the contribution :wink: )

You'll need to install [j2cli](https://github.com/kolypto/j2cli)

`pip install "j2cli[yaml]"`

You need to provide the list of instances (the easiest way is to give it as a yaml file, check artemis/artemis_instances_list.yml for an example)

`j2 docker-instances.jinja2 my_instances_list.yml > additional_navitia_instances.yml`

Then you need to start the docker-compose with the additional instances

`docker-compose -f docker-compose.yml -f additional_navitia_instances.yml up`

To add data to a given instance, you'll need to do:

`docker cp data/dumb_ntfs.zip navitiadockercompose_tyr_worker_1:/srv/ed/input/<my_instance>`

## Tweak images
By default, the tag `:latest` will be used when images are pulled. If you want to use diferent tags, set the `TAG` envar. For instance, to run the `dev` images for development purposes, run:

`TAG=dev docker-compose -f docker-compose.yml -f additional_navitia_instances.yml up`

## TODO
- move the tyr and kraken images to alpine :wink:
# KIRIN

[The magical unicorn](https://github.com/CanalTP/kirin) is now available in the Navitia docker-compose.

### How to use

Prerequisites:
Two Docker images are needed to run the docker-compose-kirin:
- kirin: see the section [Docker](https://github.com/CanalTP/kirin#docker) in Kirin
- kirin_configurator: the image can be built using the following command line
	`docker build -f Dockerfile-kirin-configurator -t kirin_configurator .`

When running the Navitia *docker-compose*, add the *docker-compose_kirin* file in the command:
	`docker-compose -f docker-compose.yml -f kirin/docker-compose_kirin.yml up`

This will add the containers needed for Kirin to run and be linked to Navita:
- kirin: the Kirin web server
- kirin_database: the Kirin database, obviously
- kirin_background: a script to load the realtime updates already in the database
- kirin_configurator: a script to upgrade the database
