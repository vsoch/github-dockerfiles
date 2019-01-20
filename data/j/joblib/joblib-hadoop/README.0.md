## Hadoop Docker

The Hadoop cluster runs the docker containers from
[this github project](https://github.com/big-data-europe/docker-hadoop).

### Description

To start the HDFS cluster, run:
```
  docker-compose up
```

### Build the nodemanager using docker:

```
  docker build nodemanager/ --tag joblib/joblib-hadoop-nodemanager:latest
```