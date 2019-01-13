FROM unit9/base:latest
MAINTAINER Kamil Cholewiński <kamil.cholewinski@unit9.com>

ADD cron.run /etc/cron.run

RUN set -eux; \
    rm -f /etc/cron.daily/apt; \
    rm -f /etc/cron.daily/dpkg; \
    rm -f /etc/cron.daily/passwd; \
    for schedule in hourly daily; \
    do \
       mkdir -p /etc/cron.${schedule}; \
       mkdir -p /etc/service/cron@${schedule}; \
       ln -s /etc/cron.run /etc/service/cron@${schedule}/run; \
    done
