FROM smizy/hbase:1.2-alpine

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION

LABEL \
    org.label-schema.build-date=$BUILD_DATE \
    org.label-schema.docker.dockerfile="/Dockerfile" \
    org.label-schema.license="Apache License 2.0" \
    org.label-schema.name="smizy/hdocdb" \
    org.label-schema.url="https://github.com/smizy" \
    org.label-schema.vcs-ref=$VCS_REF \
    org.label-schema.vcs-type="Git" \
    org.label-schema.vcs-url="https://github.com/smizy/docker-hdocdb"

ENV HDOCDB_VERSION   $VERSION
ENV HDOCDB_HOME      /usr/local/hdocdb

## Add user-specified CLASSPATH
ENV HBASE_CLASSPATH  ${HDOCDB_HOME}/lib/*

RUN set -x \
    && apk update \
    && apk --no-cache add \
        openjdk8 \
        wget \
    && mkdir -p ${HDOCDB_HOME}/lib \
    && cd ${HDOCDB_HOME}/lib \
    && wget -q http://central.maven.org/maven2/io/hdocdb/hdocdb/${HDOCDB_VERSION}/hdocdb-${HDOCDB_VERSION}.jar \
    && apk del wget

COPY hdocdb.js  ${HDOCDB_HOME}/lib/

WORKDIR ${HDOCDB_HOME}