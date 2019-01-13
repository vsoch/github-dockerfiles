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
