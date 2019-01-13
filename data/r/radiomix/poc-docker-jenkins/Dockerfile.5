#
# Take from https://github.com/shipyard/docker-private-registry.git
#
FROM shipyard/docker-registry

MAINTAINER Shipyard Project "http://shipyard-project.com"

##
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y apache2-utils supervisor python-setuptools make g++ libpcre3-dev wget libssl-dev libreadline-dev perl redis-server

#nginx
RUN wget http://openresty.org/download/ngx_openresty-1.4.3.6.tar.gz -O /tmp/nginx.tar.gz
RUN (cd /tmp && tar zxf nginx.tar.gz && cd ngx_* && ./configure --with-luajit && make && make install)
RUN echo "uwsgi_param   UWSGI_SCHEME     \$scheme;" >> /usr/local/openresty/nginx/uwsgi_params
RUN mkdir /var/log/nginx
# path of the ssl cert and key files
ADD ssl/ /opt/ssl/

RUN easy_install pip
RUN pip install uwsgi
ADD run.sh /usr/local/bin/run

ADD . /app
#ADD ./config.yml /docker-registry/config/config.yml
#VOLUME /registry-data


RUN pip install -r /app/requirements.txt

ENV CACHE_REDIS_HOST 127.0.0.1
ENV CACHE_REDIS_PORT 6379
ENV CACHE_LRU_REDIS_HOST 127.0.0.1
ENV CACHE_LRU_REDIS_PORT 6379

EXPOSE 80
EXPOSE 443
CMD ["/usr/local/bin/run"]
ADD ssl/registry.im7.de.key /opt/ssl/registry.im7.de.key
ADD ssl/registry.im7.de.cert /opt/ssl/registry.im7.de.cert
ENV SSL_CERT_PATH /opt/ssl/registry.im7.de.key
ENV SSL_CERT_KEY_PATH  /opt/ssl/registry.im7.de.cert
ENV REGISTRY_NAME registry.im7.de
