FROM ubuntu:14.04
MAINTAINER Larry Shaffer <lshaffer@boundlessgeo.com>
# Culled from https://github.com/kartoza/docker-postgis/tree/9.3-2.1 on Feb 19, 2016

ARG APT_CATCHER_IP=localhost

# Set up OS
ADD setup.sh /tmp/
RUN chmod 0700 /tmp/setup.sh && sh /tmp/setup.sh

# Set up Postgres
ADD setup-postgres.sh /tmp/
RUN chmod 0700 /tmp/setup-postgres.sh && sh /tmp/setup-postgres.sh

EXPOSE 5432

# Set up DBs, PostGIS extensions and run Postgres/PostGIS
ADD start-postgis.sh /start-postgis.sh
RUN chmod 0755 /start-postgis.sh
CMD /start-postgis.sh
