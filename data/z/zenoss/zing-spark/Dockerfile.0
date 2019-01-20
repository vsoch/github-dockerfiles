ARG SPARK_VERSION=2.2.0
ARG HADOOP_VERSION=hadoop2.7


FROM alpine:3.6 as build
RUN apk add curl jq --update

ARG SPARK_VERSION
ARG HADOOP_VERSION

ADD spark-mirror.sh /tmp/spark-mirror.sh

ENV SPARK_VERSION ${SPARK_VERSION}
ENV HADOOP_VERSION ${HADOOP_VERSION}

RUN curl -s `/tmp/spark-mirror.sh` | tar xzf - -C /tmp

FROM openjdk:8u131-jre
MAINTAINER Zenoss

ENV SPARK_HOME /opt/spark
ENV PATH $PATH:$SPARK_HOME/bin

ARG SPARK_VERSION
ARG HADOOP_VERSION
ARG SPARK_FILENAME=spark-${SPARK_VERSION}-bin-${HADOOP_VERSION}

COPY --from=build /tmp/$SPARK_FILENAME /opt/spark
