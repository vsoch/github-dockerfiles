FROM ubuntu:quantal

RUN echo "deb http://ja.archive.ubuntu.com/ubuntu/ quantal universe" >> /etc/apt/sources.list
RUN echo "deb http://ja.archive.ubuntu.com/ubuntu/ quantal-updates universe" >> /etc/apt/sources.list
RUN apt-get -y update

RUN apt-get -y install build-essential curl git
RUN apt-get -y install python3 python3-pip python3-dev
RUN apt-get -y install libxml2-dev libxslt-dev

RUN pip-3.2 install virtualenv
