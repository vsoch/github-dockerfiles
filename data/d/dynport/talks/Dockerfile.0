FROM ubuntu

ENV DEBIAN_FRONTEND noninteractive

RUN apt-mark hold initscripts
RUN apt-get update
RUN apt-get upgrade -y

ENV RUBY_VERSION 2.1.1
RUN apt-get -y install curl build-essential libyaml-dev libxml2-dev libxslt1-dev libreadline-dev libssl-dev zlib1g-dev
RUN cd /tmp && curl -SsfLO http://ftp.ruby-lang.org/pub/ruby/$(echo $RUBY_VERSION | cut -d "." -f 1-2)/ruby-$RUBY_VERSION.tar.gz
RUN cd /tmp && tar xvfz ruby-$RUBY_VERSION.tar.gz
RUN cd /tmp/ruby-$RUBY_VERSION && ./configure --disable-install-doc && make && make install

ENV NGINX_VERSION 1.4.4
RUN apt-get install -y libpcre3 libpcre3-dev libpcrecpp0 libgd2-xpm-dev
RUN mkdir -p /src/
RUN cd /src && curl -Ssfl http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz | tar xfz -

ENV NGINX_SYSLOG_PATCH_VERSION 1.3.14
RUN mkdir -p /src/nginx_syslog_patch
RUN cd /src/nginx_syslog_patch && curl -SsfLO https://raw.github.com/yaoweibin/nginx_syslog_patch/master/config
RUN cd /src/nginx_syslog_patch && curl -SsfLO https://raw.github.com/yaoweibin/nginx_syslog_patch/master/syslog_$NGINX_SYSLOG_PATCH_VERSION.patch
RUN cd /src/nginx-$NGINX_VERSION && patch -p1 < /src/nginx_syslog_patch/syslog_$NGINX_SYSLOG_PATCH_VERSION.patch

ENV NGINX_HEADERS_MORE_VERSION 0.24
RUN cd /src && curl -SsfLO "https://github.com/agentzh/headers-more-nginx-module/archive/v$NGINX_HEADERS_MORE_VERSION.tar.gz"
RUN cd /src && tar xfz v$NGINX_HEADERS_MORE_VERSION.tar.gz

# compile nginx
RUN cd /src/nginx-$NGINX_VERSION && ./configure --with-http_ssl_module --with-http_gzip_static_module --with-http_stub_status_module --with-http_spdy_module --add-module=/src/nginx_syslog_patch --add-module=/src/headers-more-nginx-module-$NGINX_HEADERS_MORE_VERSION && make && make install

# syslog requirements
RUN apt-get install -y rsyslog

# bundler
ENV BUNDLER_VERSION 1.5.2
RUN unset http_proxy; gem install bundler --no-ri --no-rdoc -v=$BUNDLER_VERSION

# required packages
RUN apt-get install -y git-core libpq-dev libjpeg-dev imagemagick net-tools

# exif tool
ENV EXIF_TOOL_VERSION 9.33
RUN mkdir -p /src && cd /src && curl -SsfL "http://www.sno.phy.queensu.ca/~phil/exiftool/Image-ExifTool-$EXIF_TOOL_VERSION.tar.gz" | tar xfz -
RUN cd /src/Image-ExifTool-$EXIF_TOOL_VERSION && perl Makefile.PL && make install

# initial bundling
RUN mkdir -p /app/gems /app/current /app/shared /app/shared/config
ADD Gemfile /app/current/Gemfile
ADD Gemfile.lock /app/current/Gemfile.lock

RUN sed 's;https://rubygems.org;http://rubygems.org;' -i /app/current/Gemfile
RUN cd /app/current && bundle install --without development test

ADD . /app/current

ADD docker/syslog_relay.conf /etc/rsyslog.conf 
ADD docker/rsyslog.init /etc/init/rsyslog.conf

ADD docker/unicorn_config.rb /app/shared/config/unicorn_config.rb 
ADD docker/nginx.conf /usr/local/nginx/conf/nginx.conf
ADD docker/nginx.init /etc/init/nginx.conf
ADD docker/unicorn.init /etc/init/unicorn.conf
ADD docker/sidekiq.init /etc/init/sidekiq.conf

CMD ["/sbin/init"]
