# Hadoop docker image
This is a hadoop docker build project on Debian Linux distro.

## Version
2.7.1


## Building the image
- ``docker build -t anoopnair/hadoop_debian:2.7.1 .``

## Running
- ``docker run --name hadoop -p 49707:49707 -p 50010:50010 -p 50020:50020 -p 50030:50030 -p 50070:50070 -p 50075:50075 -p 50090:50090 -p 8030:8030 -p 8031:8031 -p 8032:8032 -p 8033:8033 -p 8040:8040 -p 8042:8042 -p 8088:8088 -it anoopnair/hadoop_debian:2.7.1``

## UI
- http://localhost:8088/

# Pig docker image
This is a hadoop pig docker build project on Debian Linux distro.

## Version
- hadoop: 2.7.1
- pig: 0.15.0


## Building the image
- ``docker build -t anoopnair/pig_hadoop_debian:0.15.0 .``

## Running
- ``docker run --name pig -it anoopnair/pig_hadoop_debian:0.15.0 bash``
- and then start running pig scripts

