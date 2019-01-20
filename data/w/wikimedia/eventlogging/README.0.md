# EventLogging Docker images

Each Dockerfile in this directory tree can be used to run an eventlogging
component.

The docker/run script is a helper wrapper around docker commands to make
running a simple EventLogging docker image easy.

```
$ docker/run --help
Usage: docker/run [<component>] ...

Builds and run an EventLogging docker container.

If <component> is not given, then a shell in the base container
with the codebase checkout out from upstream master at
/usr/src/eventlogging will be started.

If <component> is dev, then a shell in the dev container with the
local codebase mounted at /srv/eventlogging will be started.

Otherwise, one of the docker subdirectories will be started.

Anything after <component> will be passed as the arguments
to docker run, so you may use CMD overrides to pass
additional arguments to ENTRYPOINTS.  E.g.
docker/run service file:///tmp/out.log
```

```
$ docker/run dev
Building base EventLogging image...
docker build --tag wikimedia/eventlogging /Users/otto/Projects/wm/analytics/eventlogging/docker
Sending build context to Docker daemon 18.43 kB
Step 1 : FROM debian:jessie

...

Removing intermediate container da54f5652e68
Successfully built 83b6700005d5
docker build --tag wikimedia/eventlogging-dev /Users/otto/Projects/wm/analytics/eventlogging/docker/dev
Sending build context to Docker daemon 2.048 kB
Step 1 : FROM wikimedia/eventlogging
 ---> 83b6700005d5
Step 2 : ENV PYTHONPATH "/srv/eventlogging"
 ---> Running in b20677d9bd16
 ---> cfac280615fe
Removing intermediate container b20677d9bd16
Step 3 : ENV PATH "/srv/eventlogging/bin:$PATH"
 ---> Running in 116b722ac0e9
 ---> 50257e9379f6
Removing intermediate container 116b722ac0e9
Successfully built 50257e9379f6
docker run -i -t -v /Users/otto/Projects/wm/analytics/eventlogging:/srv/eventlogging wikimedia/eventlogging-dev
root@e5167bd2a4c3:/#

```
# Images

## wikimedia/eventlogging - docker/Dockerfile

This is the base EventLogging docker image.  Other specific component images are built from this.  You can use this image if you want to work with eventlogging code or run

```
$ docker build --tag wikimedia/eventlogging ./docker
...
$ docker run -i -t --name eventlogging-base wikimedia/eventlogging

root@a97ab96fae69:/# eventlogging-consumer -h
...
```

## wikimedia/eventlogging-dev - docker/dev/Dockerfile
This is the development version of the base EventLogging docker images.
Instead of cloning master from upstream, it expects you to mount
your working copy of the EventLogging codebase at /srv/eventlogging
when running this image.

```
$ docker build --tag wikimedia/eventlogging-dev ./docker/dev
...
$ docker run -i -t --name eventlogging-dev -v $(pwd):/srv/eventlogging wikimedia/eventlogging-dev

root@925aff049d11:/# which eventlogging-consumer
/srv/eventlogging/bin/eventlogging-consumer
root@925aff049d11:/# eventlogging-consumer -h
...
```

## wikimedia/eventlogging-service - docker/service/Dockerfile

```
$ docker build --tag wikimedia/eventlogging-service ./docker
...
$ docker run -p 8085:8085 --name eventlogging-service-stdout wikimedia/eventlogging-serivice
2015-12-30 18:26:44,052 (MainThread) Loading local schemas from /usr/src/eventlogging/config/schemas/jsonschema
2015-12-30 18:26:44,054 (MainThread) Loading schema from file:///usr/src/eventlogging/config/schemas/jsonschema/mediawiki/revision_visibility_set/1.yaml
2015-12-30 18:26:44,075 (MainThread) Loading schema from file:///usr/src/eventlogging/config/schemas/jsonschema/mediawiki/page_delete/1.yaml
2015-12-30 18:26:44,097 (MainThread) Loading schema from file:///usr/src/eventlogging/config/schemas/jsonschema/mediawiki/page_restore/1.yaml
2015-12-30 18:26:44,114 (MainThread) Loading schema from file:///usr/src/eventlogging/config/schemas/jsonschema/mediawiki/page_edit/1.yaml
2015-12-30 18:26:44,136 (MainThread) Loading schema from file:///usr/src/eventlogging/config/schemas/jsonschema/mediawiki/page_move/1.yaml
2015-12-30 18:26:44,157 (MainThread) Publishing valid JSON events to stdout://.

# In another shell:
$ curl -X POST -d @page_edit_record.json -H 'Content-Type: application/json' http://$(docker-machine ip default):8085/v1/events
```
