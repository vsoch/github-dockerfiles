FROM ubuntu:trusty
MAINTAINER Zenoss, Inc <dev@zenoss.com>

RUN echo 'deb http://archive.ubuntu.com/ubuntu trusty main universe' > /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y -q wget git-core make mercurial bzr
RUN apt-get install -y -q redis-server
RUN wget -qO- http://go.googlecode.com/files/go1.2.linux-amd64.tar.gz | tar -C / -xz
ENV GOROOT /go
ENV GOPATH /gosrc
ENV PATH $PATH:/go/bin

WORKDIR /gosrc/src/github.com/zenoss/metricshipper
