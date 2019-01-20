FROM ubuntu:trusty
MAINTAINER Uken Ops "ops@uken.com"

ENV DEBIAN_FRONTEND noninteractive

ADD ./sources.list /etc/apt/sources.list

RUN rm -Rfv /var/lib/apt/lists/*

ADD ./packages.txt /tmp/packages.txt
RUN apt-get -y update && xargs apt-get install --force-yes -y < /tmp/packages.txt
RUN rm -f /tmp/packages.txt

RUN adduser --disabled-password --home=/app --gecos 'SheepIt' app

# forego with https://github.com/ddollar/forego/pull/55
ADD https://s3.amazonaws.com/uken-ubuntu-packages/forego/forego /usr/bin/forego
RUN chmod 655 /usr/bin/forego

RUN chmod 600 /etc/crontab

ENTRYPOINT ["/bin/bash", "-l", "-c"]
