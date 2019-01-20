# Use phusion/baseimage as base image. To make your builds reproducible, make
# sure you lock down to a specific version, not to `latest`!
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for
# a list of version numbers.
FROM phusion/baseimage:0.9.20
MAINTAINER Travis Rowland <travis.rowland@gmail.com>

CMD ["/sbin/my_init"]

# Environment Variables
# ENV DEBIAN_FRONTEND noninteractive
ENV TIMEZONE            UTC
ENV PHP_MEMORY_LIMIT    512M
ENV MAX_UPLOAD          50M
ENV PHP_MAX_FILE_UPLOAD 200
ENV PHP_MAX_POST        100M

# Update packages
RUN apt-get clean && \
    apt-get autoremove

# Install required packages
RUN apt-get update && \
    apt-get -y install \
    netcat \
    unzip \
    php \
    php-sqlite3 \
    php-pear \
    php-ldap \
    php-pgsql \
    php-mcrypt \
    php-mbstring \
    php-gmp \
    php-json \
    php-mysql \
    php-gd \
    php-odbc \
    php-xmlrpc \
    php-memcache \
    php-curl \
    php-imagick \
    php-intl \
    php-fpm \
    php-bcmath \
    git \
    curl \
    wget \
    libxrender1 \
    nginx \
    ansible \
    nano

# Create php-fpm pid
RUN service php7.0-fpm start

# Set environment variables
RUN sed -i '/daemonize /c daemonize = no' /etc/php/7.0/fpm/php-fpm.conf && \
    echo "clear_env = no" >> /etc/php/7.0/fpm/php-fpm.conf && \
  	sed -i '/^listen /c listen = 0.0.0.0:9000' /etc/php/7.0/fpm/pool.d/www.conf && \
  	sed -i 's/^listen.allowed_clients/;listen.allowed_clients/' /etc/php/7.0/fpm/pool.d/www.conf && \
  	sed -i "s|;*listen\s*=\s*/||g" /etc/php/7.0/fpm/pool.d/www.conf && \
  	sed -i "s|;*date.timezone =.*|date.timezone = ${TIMEZONE}|i" /etc/php/7.0/fpm/php.ini && \
  	sed -i "s|;*memory_limit =.*|memory_limit = ${PHP_MEMORY_LIMIT}|i" /etc/php/7.0/fpm/php.ini && \
    sed -i "s|;*upload_max_filesize =.*|upload_max_filesize = ${MAX_UPLOAD}|i" /etc/php/7.0/fpm/php.ini && \
    sed -i "s|;*max_file_uploads =.*|max_file_uploads = ${PHP_MAX_FILE_UPLOAD}|i" /etc/php/7.0/fpm/php.ini && \
    sed -i "s|;*post_max_size =.*|post_max_size = ${PHP_MAX_POST}|i" /etc/php/7.0/fpm/php.ini && \
    sed -i "s|;*cgi.fix_pathinfo=.*|cgi.fix_pathinfo= 0|i" /etc/php/7.0/fpm/php.ini && \

    # Install composer
    curl -sS https://getcomposer.org/installer | php && \
        mv composer.phar /usr/local/bin/composer && \
        echo "PATH=$PATH:/usr/local/bin" >> ~/.bash_profile && \
        echo "export PATH" >> ~/.bash_profile && \
        . ~/.bash_profile

# Set Workdir
WORKDIR /www

# Expose volumes
VOLUME ["/www"]

# Expose ports
EXPOSE 9000
EXPOSE 80
EXPOSE 443

# Setup app configuration
ADD config/app.php /

# Setup nginx-proxy
# https://github.com/jwilder/docker-gen
# https://github.com/jwilder/nginx-proxy
ADD config/nginx.tmpl /

# Setup Ansible
ADD ansible/. /ansible

# Setup init scripts
ADD my_init/init-ansible.sh /etc/my_init.d/10-init-ansible.sh
ADD my_init/init-nginx.sh /etc/my_init.d/20-init-nginx.sh
ADD my_init/init.sh /etc/my_init.d/30-init.sh

# Setup private key
ADD config/id_rsa /
RUN mv /id_rsa /root/.ssh/id_rsa
RUN chmod 600 ~/.ssh/id_rsa
RUN echo "    IdentityFile ~/.ssh/id_rsa" >> /etc/ssh/ssh_config

ENV COMPOSER_HOME=/www

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
