
```bash
docker build -t dajobe/hbase .
```

# mount a host directory to data volumn
```bash
# create data store folder
mkdir data
id=$(docker run --name=hbase-docker -h hbase-docker -d -v $PWD/data:/data dajobe/hbase)
# create other container for hbase shell
docker run --rm -it --link $id:hbase-docker dajobe/hbase hbase shell
# if you don't want to create other container
docker exec -it hbase-docker bash
# run in docker container
hbase shell
```
```bash
# HBase Test
hbase(main):001:0> create 'member','member_id','address','info'
hbase(main):002:0> list
hbase(main):003:0> describe 'member'
hbase(main):004:0> exit
```
```bash
# clean up
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
# delete temp hbase data
# rm -rf data
```


# No Volumn
```bash
# build image
docker build -t dajobe/hbase .
# start container
id=$(docker run --name=hbase-docker -h hbase-docker -d dajobe/hbase)
docker exec -it hbase-docker bash
# create other container for hbase shell
# docker run --rm -it --link $id:hbase-docker dajobe/hbase hbase shell
```

```bash
# HBase Simple Test
hbase(main):001:0> create 'member','member_id','address','info'
hbase(main):002:0> list
hbase(main):003:0> describe 'member'
hbase(main):004:0> exit
```

```bash
# clean up
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
```



