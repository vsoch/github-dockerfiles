FROM ubuntu:14.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -qq
RUN apt-get install -y curl
RUN apt-get install -y build-essential
RUN apt-get install -y libssl-dev openssh-client git

RUN curl -sSf https://static.rust-lang.org/rustup.sh | sh -s -- --revision=1.12.0 --yes --disable-sudo

VOLUME /project
WORKDIR /project
ENV CARGO_HOME=/project/target/

ENTRYPOINT ["cargo"]
CMD ["--help"]
