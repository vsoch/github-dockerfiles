# Version: 1
# Name: maven
FROM yan047/jdk7v2

MAINTAINER "boyan.au@gmail.com"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -qq update && \
    apt-get -qq -y install maven && \
    apt-get -qq -y autoremove && \
    apt-get -qq -y autoclean


