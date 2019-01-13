FROM unit9/base:latest

MAINTAINER Artiom Vasiliev <artiom@unit9.com>

COPY "sources.list" "/etc/apt/sources.list"
COPY "collectd.run" "/etc/service/collectd/run"

RUN apt-get update \
    && apt-get install -y \
        --no-install-recommends \
        build-essential \
        libgcrypt20-dev \
        librrd-dev \
        snmp \
        libsnmp-dev \
        snmp-mibs-downloader \
    && rm -rf /var/cache/apt /var/lib/apt/lists/* \
    && cd /tmp \
    # install collectd
    && curl -LO https://storage.googleapis.com/collectd-tarballs/collectd-5.7.1.tar.bz2 \
    && tar xjf collectd-5.7.1.tar.bz2 \
    && rm collectd-5.7.1.tar.bz2 \
    && cd collectd-5.7.1 \
    && ./configure --with-librrd --enable-librrd --with-snmp --enable-snmp \
    && make \
    && make install \
    && cd /tmp \
    && rm -r collectd-5.7.1 \
    # cleanup
    && apt-get remove --purge -y build-essential \
    && apt-get autoremove -y
