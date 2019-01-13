FROM unit9/base:latest
MAINTAINER UNIT9 ops team <root@unit9.com>

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive \
    apt-get install --no-install-recommends --yes \
        haproxy \
    && rm -rf /var/cache/apt /var/lib/apt/lists

ADD rc.local /etc/rc.local
ADD haproxy.run /etc/service/haproxy/run
ADD defaults.cfg /etc/haproxy/defaults.cfg
VOLUME /etc/secrets /etc/haproxy/conf.d
EXPOSE 80 443 1080
