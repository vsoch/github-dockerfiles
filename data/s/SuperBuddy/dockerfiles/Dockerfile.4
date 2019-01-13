# docker build -f Dockerfile -t superbuddy/testnodejs .

FROM node

MAINTAINER svlentink <sander@superbuddy.nl>
LABEL Description="node based tester"

# https://github.com/phusion/baseimage-docker/issues/58
# http://serverfault.com/questions/618994/when-building-from-dockerfile-debian-ubuntu-package-install-debconf-noninteract
ENV DEBIAN_FRONTEND noninteractive

RUN npm install -g \
  standard

COPY defaultTests /usr/lib/defaultTests
COPY runtests.sh /usr/bin/runtests

CMD ["/usr/bin/runtests"]
