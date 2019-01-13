FROM frolvlad/alpine-oraclejdk8:8.131.11-cleaned
MAINTAINER David Rosenstark "drosenstark@gmail.com"

RUN apk add --update bash && rm -rf /var/cache/apk/*
RUN apk add --update libuuid && rm -rf /var/cache/apk/*
RUN apk add --update libidn && rm -rf /var/cache/apk/*
RUN apk add --update curl && rm -rf /var/cache/apk/*
RUN apk add --update ca-certificates
RUN wget http://www.scala-lang.org/files/archive/scala-2.10.1.tgz
RUN tar xf scala-2.10.1.tgz
RUN rm scala-2.10.1.tgz
RUN mv scala-2.10.1 /usr/lib
RUN ln -s /usr/lib/scala-2.10.1 /usr/lib/scala

RUN wget http://apache.mirror.anlx.net/spark/spark-2.1.1/spark-2.1.1-bin-hadoop2.7.tgz
RUN tar xf ./spark-2.1.1-bin-hadoop2.7.tgz
RUN rm ./spark-2.1.1-bin-hadoop2.7.tgz
RUN mkdir  /usr/local/spark
RUN cp -r spark-2.1.1-bin-hadoop2.7/* /usr/local/spark

ENV PATH=$PATH:/usr/lib/scala/:/usr/local/spark/bin/
