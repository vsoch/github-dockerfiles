FROM ubuntu:trusty
MAINTAINER Zenoss, Inc <dev@zenoss.com>	

RUN	apt-get update -qq
RUN	apt-get install -qqy ca-certificates wget curl git

# Install Go
RUN	curl -s https://storage.googleapis.com/golang/go1.3.1.linux-amd64.tar.gz | tar -v -C /usr/local -xz
ENV	GOPATH  /go
ENV	PATH $PATH:/go/bin:/usr/local/go/bin

# build dependencies
RUN	apt-get install -y -q make ruby ruby-dev rpm
RUN	gem install fpm
RUN	apt-get install -qqy mercurial
RUN	go get github.com/tools/godep

