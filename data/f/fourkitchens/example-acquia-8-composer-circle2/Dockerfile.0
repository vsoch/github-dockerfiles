# This was started from the docker file here:
# https://hub.docker.com/r/fauria/lamp/~/dockerfile/

# Set the base image.
FROM ubuntu:16.04

# Default environment variables.
ENV LOG_STDOUT **Boolean**
ENV LOG_STDERR **Boolean**
ENV LOG_LEVEL warn
ENV ALLOW_OVERRIDE All
ENV DATE_TIMEZONE UTC
ENV TERM dumb
ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION 8.0.0
ENV NPM_VERSION 5.5.1

# Replace shell with bash so we can source files.
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# Install packages needed to run a LAMP stack.
RUN apt-get update
RUN apt-get install -y software-properties-common python-software-properties
RUN LC_ALL=C.UTF-8 add-apt-repository -y ppa:ondrej/php
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y \
  php7.1 \
  php7.1-bz2 \
  php7.1-cgi \
  php7.1-cli \
  php7.1-common \
  php7.1-curl \
  php7.1-dev \
  php7.1-enchant \
  php7.1-fpm \
  php7.1-gd \
  php7.1-gmp \
  php7.1-imap \
  php7.1-interbase \
  php7.1-intl \
  php7.1-json \
  php7.1-ldap \
  php7.1-mcrypt \
  php7.1-mysql \
  php7.1-odbc \
  php7.1-opcache \
  php7.1-pgsql \
  php7.1-phpdbg \
  php7.1-pspell \
  php7.1-readline \
  php7.1-recode \
  php7.1-snmp \
  php7.1-sqlite3 \
  php7.1-sybase \
  php7.1-tidy \
  php7.1-xmlrpc \
  php7.1-xsl \
  php7.1-phar \
  php7.1-mbstring \
  php7.1-zip \
  unzip \
  wget \
  curl \
  sudo \
  snmp \
  vim \
  git \
  pv \
  iputils-ping

RUN apt-get install apache2 libapache2-mod-php7.1 -y
RUN apt-get install mariadb-common mariadb-server mariadb-client -y

# Install Composer.
RUN php -r "readfile('http://getcomposer.org/installer');" | php -- --install-dir=/usr/bin/ --filename=composer
ENV PATH="/root/.composer/vendor/bin:${PATH}"

# Install Drush.
RUN wget -O drush.phar https://github.com/drush-ops/drush-launcher/releases/download/0.6.0/drush.phar && chmod +x drush.phar && sudo mv drush.phar /usr/local/bin/drush

# Install node, npm, aquifer, and gulp.
RUN mkdir -p /tmp/node
WORKDIR /tmp/node
RUN curl -SLO "http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz" && \
  tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local --strip-components=1 && \
  rm "node-v$NODE_VERSION-linux-x64.tar.gz" && \
  npm install -g npm@"$NPM_VERSION" && \
  npm install -g aquifer gulp
WORKDIR /root

# Set up apache.
RUN sudo mkdir -p /root/project/docroot
COPY ./config/project.conf /etc/apache2/sites-available/project.conf
RUN echo "<html><head><title>LOADED!</title></head><body><h1>LOADED!</h1></body></html>" > /root/project/docroot/index.html
RUN chown -R www-data:www-data /root/project/docroot && \
  chmod -R g+rwX /root/project/docroot && \
  chmod +rx /root && \
  a2enmod rewrite && \
  a2ensite project && \
  rm -R /root/project

RUN echo '127.0.0.1       project.local' >> /etc/hosts

# Set up Mysql.
RUN sudo service mysql start && \
  mysql -e "CREATE DATABASE IF NOT EXISTS project" && \
  mysql -e "CREATE USER 'project'@'localhost' IDENTIFIED BY 'project'" && \
  mysql -e "GRANT ALL PRIVILEGES ON project.* TO 'project'@'localhost'"


COPY init.sh /usr/sbin
RUN chmod +x /usr/sbin/init.sh

VOLUME /root
VOLUME /var/log/httpd
VOLUME /var/lib/mysql
VOLUME /var/log/mysql
VOLUME /etc/apache2

EXPOSE 80
EXPOSE 3306

ENTRYPOINT /usr/sbin/init.sh
