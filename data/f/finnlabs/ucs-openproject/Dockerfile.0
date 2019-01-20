FROM debian:7

RUN apt-get update -qq && apt-get install -y curl python-minimal tar
RUN apt-get install -y wget apt-transport-https
RUN apt-get install -y make
WORKDIR /workspace
ENTRYPOINT ["./bin/docker-entrypoint"]
