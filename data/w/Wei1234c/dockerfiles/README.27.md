# Hadoop pseudo-distributed dockerfile for armv7


by: [Wei Lin](mailto://wei1234c@gmail.com) / date: 2015/9/6


## To build image: ##

    cd /path/of/the/Dockerfile
    
    docker build -t hadoop_pseudo-distributed .



##  To start a container: ##

    docker run -d -P --name=hadoop_pseudo hadoop_pseudo-distributed



----------


- Ref 1: [Oracle-Java8 dockerfile](https://github.com/dockerfile/java/tree/master/oracle-java8 "Oracle-Java8 dockerfile")
- Ref 2: [SSHD dockerfile](https://docs.docker.com/examples/running_ssh_service/ "SSHD dockerfile")
- Ref 3: [Hadoop dockerfile](https://github.com/sequenceiq/hadoop-docker "Hadoop dockerfile")

