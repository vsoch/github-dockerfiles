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
