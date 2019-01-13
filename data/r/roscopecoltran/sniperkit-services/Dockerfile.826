FROM alpine:3.6
MAINTAINER smizy

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION

LABEL \
    org.label-schema.build-date=$BUILD_DATE \
    org.label-schema.docker.dockerfile="/Dockerfile" \
    org.label-schema.license="MIT License" \
    org.label-schema.name="smizy/postgres" \
    org.label-schema.url="https://github.com/smizy" \
    org.label-schema.vcs-ref=$VCS_REF \
    org.label-schema.vcs-type="Git" \
    org.label-schema.vcs-url="https://github.com/smizy/docker-postgres"

ENV PGDATA /var/lib/postgresql/data

RUN set -x \
    && apk update \
    && apk add \
        bash \
        postgresql \
        su-exec \
    && mkdir -p \
        /var/run/postgresql \
        ${PGDATA} \
        /docker-entrypoint-initdb.d \
    && chown -R postgres /var/run/postgresql ${PGDATA} \
    && sed -ri "s!^#?(listen_addresses)\s*=\s*\S+.*!\1 = '*'!" /usr/share/postgresql/postgresql.conf.sample
    
COPY entrypoint.sh /usr/local/bin/

VOLUME ["${PGDATA}"]

EXPOSE 5432

ENTRYPOINT ["entrypoint.sh"]
CMD ["postgres"]
