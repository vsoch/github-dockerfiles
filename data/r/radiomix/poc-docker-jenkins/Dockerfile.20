#
# We use ubuntu:14.04 as the jetty container as a base image for dockerfile/java 
# 
# FROM starts with trusted build from https://registry.hub.docker.com/u/dockerfile/java/
# alternatively, we can build an image from Dockerfile: docker build -t="dockerfile/java" github.com/dockerfile/java
# Exposes Port 8080
# Usage
# java:> 	docker run -it --rm dockerfile/java java
# javac:> 	docker run -it --rm dockerfile/java javac
# 

#based on ubuntu:14.04
FROM dockerfile/java  


MAINTAINER jglick@cloudbees.com
# cribbed from cjlyth/jetty
WORKDIR /opt
ENV VERSION 9.2.1.v20140609
RUN curl "http://mirrors.ibiblio.org/eclipse/jetty/stable-9/dist/jetty-distribution-$VERSION.tar.gz" | tar xvfz -
RUN ln -sv jetty-distribution-$VERSION jetty
ADD etc /opt/jetty/etc
CMD /opt/jetty/bin/jetty.sh -d supervise
EXPOSE 8080

