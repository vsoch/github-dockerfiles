FROM ubuntu:precise
MAINTAINER Uken Ops "ops@uken.com"

ENV DEBIAN_FRONTEND noninteractive

ADD ./sources.list /etc/apt/sources.list

RUN rm -Rfv /var/lib/apt/lists/*

ADD ./packages.txt /tmp/packages.txt
RUN apt-get -y update && xargs apt-get install --force-yes -y < /tmp/packages.txt
RUN rm -f /tmp/packages.txt

RUN adduser --disabled-password --home=/app --gecos 'SheepIt' app

RUN mkdir /build /cache
ADD ./sheepit_init /sheepit_init

ENTRYPOINT ["/sheepit_init"]
WORKDIR /app
