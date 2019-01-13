# docker-opentsdb
[![](https://images.microbadger.com/badges/image/smizy/opentsdb:2.2.2-alpine.svg)](https://microbadger.com/images/smizy/opentsdb:2.2.2-alpine "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/version/smizy/opentsdb:2.2.2-alpine.svg)](https://microbadger.com/images/smizy/opentsdb:2.2.2-alpine "Get your own version badge on microbadger.com")
[![CircleCI](https://circleci.com/gh/smizy/docker-opentsdb.svg?style=svg&circle-token=03e3d264901a60ed454a2c296b3d243ad6f53305)](https://circleci.com/gh/smizy/docker-opentsdb)

OpenTSDB docker image based on alpine

## Run server

```
# load default env
eval $(docker-machine env default)

# network 
docker network create vnet

# make docker-compose.yml 
./make_docker_compose_yml.sh hdfs hbase tsdb > docker-compose.yml

# hadoop+hbase+tsdb startup (zookeeper, journalnode, namenode, datanode, hmaster, regionserver, tsdb)
docker-compose up -d

# tail logs for a while
docker-compose logs -f

# check ps
docker-compose ps

# check stats
docker ps --format {{.Names}} | xargs docker stats

# check web ui
open http://$(docker-machine ip default):4242
```

## Licenses
* Apache License 2.0

### mustache.sh License
* BSD License. See LICENSE.mustache.
* Source: https://github.com/rcrowley/mustache.sh
* Copyright 2011 Richard Crowley. All rights reserved.