FROM alpine:3.4
MAINTAINER Akiyoshi Sakaguchi <autumngoodluck@gmail.com>

ENV NGINX_CONFIG_OPT_ENV --with-http_stub_status_module \
                         --with-http_ssl_module \
                         --with-http_realip_module \
                         --with-http_addition_module \
                         --with-http_sub_module \
                         --with-http_gunzip_module \
                         --with-http_gzip_static_module \
                         --with-http_random_index_module \
                         --with-http_secure_link_module \
                         --with-ipv6 \
                         --with-file-aio \
                         --with-pcre-jit \
                         --with-http_dav_module \
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
                         --error-log-path=/var/log/nginx/error.log

RUN apk add --update ca-certificates openssl pcre zlib \
  && apk add --virtual build-packages build-base linux-headers openssl-dev pcre-dev zlib-dev ruby-dev ruby-rake tar wget bison perl git \
  && git clone https://github.com/matsumoto-r/ngx_mruby.git \
  && cd ngx_mruby \
  && sh build.sh \
  && make install \
  && mkdir -p /usr/share/nginx/tmp \
  && ln -sf /dev/stdout /var/log/nginx/access.log \
  && ln -sf /dev/stderr /var/log/nginx/error.log \
  && cd / \
  && apk del build-packages \
  && rm -rf \
       ngx_mruby \
       /var/cache/apk/*

EXPOSE 80 443

ONBUILD ADD ngx-mruby/hook /usr/share/nginx/hook
ONBUILD ADD ngx-mruby/conf /etc/nginx/conf

CMD ["nginx", "-g", "daemon off;"]
