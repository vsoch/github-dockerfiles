#
# Dockerfile lighttpd-mariadb5.5-php5
# ref https://github.com/rossriley/dockerbase
#
FROM ubuntu:14.04
MAINTAINER  Y12STUDIO "y12studio@gmail.com"
# Update OS.
RUN sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list
RUN apt-get update && apt-get -y upgrade

# Ensure UTF-8
RUN locale-gen en_US.UTF-8
ENV LANG       en_US.UTF-8
ENV LC_ALL     en_US.UTF-8

# Install basic packages.
RUN apt-get install -y software-properties-common curl git unzip nano wget

# Install MariaDB from repository.
RUN echo "deb http://ftp.osuosl.org/pub/mariadb/repo/5.5/ubuntu trusty main" > /etc/apt/sources.list.d/mariadb.list && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes mariadb-server mariadb-server-5.5

# Configure MariaDB to listen on any address.
RUN sed -i -e 's/^bind-address/#bind-address/' /etc/mysql/my.cnf

# Change the innodb-buffer-pool-size to 128M (default is 256M).
# This should make it friendlier to run on low memory servers.
RUN sed -i -e 's/^innodb_buffer_pool_size\s*=.*/innodb_buffer_pool_size = 128M/' /etc/mysql/my.cnf

# install lighttpd
RUN apt-get -y install lighttpd php5-fpm php5 php5-mysql php-apc php5-mcrypt php5-curl php5-gd php5-json php5-cli
RUN sed -i -e "s/short_open_tag = Off/short_open_tag = On/g" /etc/php5/fpm/php.ini
RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer

# Configure for PHP websites
RUN echo "cgi.fix_pathinfo = 1;" >> /etc/php5/fpm/php.ini
RUN echo "max_input_vars = 10000;" >> /etc/php5/fpm/php.ini
RUN echo "date.timezone = Asia/Taipei;" >> etc/php5/fpm/php.ini

# configure lighttpd
RUN cd /etc/lighttpd/conf-available/ && cp 15-fastcgi-php.conf 15-fastcgi-php.conf.bak
ADD fastcgi-php.conf /etc/lighttpd/conf-available/15-fastcgi-php.conf
RUN lighttpd-enable-mod fastcgi && lighttpd-enable-mod fastcgi-php

RUN echo '<?php phpinfo(); ?>' > /var/www/info.php

RUN chown -R www-data:www-data /var/www

# Install sshd
RUN apt-get update &&  apt-get install -y sudo openssh-server
RUN mkdir /var/run/sshd
#
# add user
#
RUN useradd -m -s /bin/bash docker &&\
   echo "docker:docker123" | chpasswd &&\
   mkdir -p /home/docker/.ssh; chmod 700 /home/docker/.ssh &&\
   chown -R docker:docker /home/docker &&\
   echo "docker ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
#
# http://stackoverflow.com/questions/18173889/cannot-access-centos-sshd-on-docker
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config &&\
    sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config

# phpmyadmin
RUN apt-get install -y dbconfig-common javascript-common libjs-jquery libjs-jquery-ui php-gettext

ADD install_phpmyadmin.sh /install_phpmyadmin.sh
RUN chmod 755 /install_phpmyadmin.sh
ADD start.sh /start.sh
RUN chmod 755 /start.sh

EXPOSE 22
EXPOSE 80
CMD ["/bin/bash", "/start.sh"]

