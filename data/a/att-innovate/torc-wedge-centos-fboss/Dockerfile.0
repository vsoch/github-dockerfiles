FROM ubuntu:14.04

RUN apt-get update -qq

COPY ./provision/bin/wedge_agent /
COPY ./provision/bin/containerbackdoor /
COPY ./provision/lib /usr/lib/
COPY ./provision/config/torc.json /
COPY ./provision/scripts/start-fboss.sh /

ENTRYPOINT ["/containerbackdoor"]
