FROM orgsync/base:1.0.0
MAINTAINER Joshua Griffith <joshua@orgsync.com>

RUN apt-get update \
    && apt-get install -y \
        git \
        autoconf \
        build-essential \
        libbz2-dev \
        libcurl4-openssl-dev \
        libevent-dev \
        libsasl2-dev \
        libmemcached-dev \
        libmemcached-dbg \
        libffi-dev \
        libglib2.0-dev \
        libncurses5-dev \
        libreadline-dev \
        libssl-dev \
        libxml2-dev \
        libxslt1-dev \
        libyaml-dev \
        zlib1g-dev \
        libmysqlclient-dev \
        libpq-dev \
        libsqlite3-dev \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean
