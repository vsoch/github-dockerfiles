FROM alpine:3.4
MAINTAINER Akiyoshi Sakaguchi <autumngoodluck@gmail.com>

ENV NGINX_VERSION 1.11.1

RUN apk --update add ca-certificates openssl pcre zlib \
  && apk add --virtual build-dependencies build-base linux-headers openssl-dev pcre-dev zlib-dev curl \
  && curl -SLO http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz \
  && tar xzvf nginx-${NGINX_VERSION}.tar.gz \
  && cd nginx-${NGINX_VERSION} \
  && ./configure \
       --with-ipv6 \
       --with-file-aio \
       --with-pcre-jit \
       --with-http_dav_module \
       --with-http_ssl_module \
       --with-http_stub_status_module \
       --with-http_gzip_static_module \
       --with-http_v2_module \
       --with-http_auth_request_module \
       --with-mail \
       --with-mail_ssl_module \
       --prefix=/usr/share/nginx \
       --sbin-path=/usr/local/sbin/nginx \
       --conf-path=/etc/nginx/conf/nginx.conf \
       --pid-path=/var/run/nginx.pid \
       --lock-path=/var/run/nginx.lock \
       --http-client-body-temp-path=/usr/share/nginx/tmp/client_body \
       --http-proxy-temp-path=/usr/share/nginx/tmp/proxy \
       --http-fastcgi-temp-path=/usr/share/nginx/tmp/fastcgi \
       --http-uwsgi-temp-path=/usr/share/nginx/tmp/uwsgi \
       --http-scgi-temp-path=/usr/share/nginx/tmp/scgi \
       --http-log-path=/var/log/nginx/access.log \
       --error-log-path=/var/log/nginx/error.log \
  && make \
  && make install \
  && ln -sf /dev/stdout /var/log/nginx/access.log \
  && ln -sf /dev/stderr /var/log/nginx/error.log \
  && cd / \
  && apk del build-dependencies \
  && rm -rf \
       nginx-${NGINX_VERSION} \
       nginx-${NGINX_VERSION}.tar.gz \
       /var/cache/apk/*

VOLUME ["/var/cache/nginx"]

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]