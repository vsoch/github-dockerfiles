FROM ubuntu:14.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -qq

COPY ./provision/torc_scheduler /torc_scheduler
COPY ./provision/config.yml /config.yml
COPY ./provision/config-minimal.yml /config-minimal.yml

ENV RUST_BACKTRACE=1

ENTRYPOINT ["/torc_scheduler"]
CMD ["--config=/config.yml", "--master=127.0.0.1"]
