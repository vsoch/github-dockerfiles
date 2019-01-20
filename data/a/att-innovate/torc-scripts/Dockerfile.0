FROM ubuntu:14.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -qq

COPY ./provision/statesync /statesync

ENV RUST_BACKTRACE=1

ENTRYPOINT ["/statesync"]
CMD ["--help"]
