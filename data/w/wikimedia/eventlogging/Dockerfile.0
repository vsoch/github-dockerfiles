FROM debian:jessie
MAINTAINER Andrew Otto <otto@wikimedia.org>

COPY debian-backports.list /etc/apt/sources.list.d/debian-backports.list
COPY wikimedia.list /etc/apt/sources.list.d/wikimedia.list
COPY wikimedia.key /tmp/wikimedia.key

RUN set -x; \
  apt-key add /tmp/wikimedia.key \
  && apt-get update

RUN set -x; \
  apt-get install  -y --no-install-recommends \
  git                   \
  ca-certificates       \
  python-dateutil       \
  python-jsonschema     \
  python-mysqldb        \
  python-sqlalchemy     \
  python-kafka          \
  python-zmq            \
  python-six            \
  python-statsd         \
  python-tornado        \
  python-sprockets-mixins-statsd \
  python-yaml           \
  python-psutil         \
  python-ua-parser

RUN set -x; \
  mkdir -p /usr/src \
  && git clone https://gerrit.wikimedia.org/r/p/eventlogging \
    /usr/src/eventlogging \
  && cd /usr/src/eventlogging \
  && git submodule update --init

ENV PYTHONPATH="/usr/src/eventlogging"
ENV PATH="$PATH:/usr/src/eventlogging/bin"

# Default to InnoDB in case MySQL writer is used.
ENV EVENTLOGGING_MYSQL_ENGINE=InnoDB

ENTRYPOINT ["/bin/bash"]
