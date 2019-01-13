# AlpineLinux Python
FROM alpine:3.4
MAINTAINER Nicolas Seyvet <nicolas.seyvet@ericsson.com>

# Install needed packages. Notes:
#  - ca-certificates: for SSL verification during Pip and easy_install
#  - python: the binaries themselves
#  - python-dev: are used for gevent e.g.
#  - py-pip: Pip.
#  - ca-certificates: for SSL verification during Pip and easy_install

RUN apk update \
  && apk add --update python3 python3-dev ca-certificates \
  && pip3 install --upgrade pip \ 
  && rm -rf /var/cache/apk/*

