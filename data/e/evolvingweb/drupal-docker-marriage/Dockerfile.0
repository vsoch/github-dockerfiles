FROM ubuntu:14.04

# Detect a deb package cache
ADD deploy/detect_squid_deb_proxy /var/build/scripts/detect_squid_deb_proxy
RUN /var/build/scripts/detect_squid_deb_proxy


##### Install packages

# LAMP
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN apt-get -y install git mysql-client \
  mysql-server apache2 libapache2-mod-php5 php5-mysql php-apc php5-gd \
  php5-memcache php5-json memcached python-setuptools php5-curl

# Utilities
RUN apt-get install -y curl git vim openssh-server pwgen

# supervisord init replacement
RUN easy_install supervisor
ADD ./deploy/supervisord.conf /etc/supervisord.conf
RUN mkdir -p /var/run/sshd; mkdir -p /var/log/supervisor

# composer and drush
RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer
RUN composer global require drush/drush:6.*
RUN ln -sf /$HOME/.composer/vendor/drush/drush/drush /usr/bin/drush

# postfix for emails
RUN echo "postfix postfix/mailname string example.com" | debconf-set-selections
RUN echo "postfix postfix/main_mailer_type string 'Internet Site'" | \
  debconf-set-selections
RUN apt-get install -y postfix


##### Setup system

# Add SSH key
ADD ./deploy/id_rsa.pub /root/.ssh/id_rsa.pub
RUN cat /root/.ssh/id_rsa.pub >> /root/.ssh/authorized_keys
RUN chmod 700 /root/.ssh; chmod 600 /root/.ssh/authorized_keys

# Apache vhost configuration
ADD deploy/apache_vhost /etc/apache2/sites-available/000-default.conf
RUN a2enmod rewrite vhost_alias

# MySQL setup
RUN pwgen -c -n -1 12 > /tmp/password_db_root
RUN pwgen -c -n -1 12 > /tmp/password_db_drupal
ADD deploy/mysql_wait /usr/local/bin/
RUN chmod a+x /usr/local/bin/mysql_wait
RUN supervisord -c /etc/supervisord.conf && mysql_wait && \
  mysqladmin -u root password $(cat /tmp/password_db_root) && \
  echo "CREATE DATABASE drupal; \
        GRANT ALL PRIVILEGES ON drupal.* TO 'drupal'@'localhost' \
        IDENTIFIED BY '$(cat /tmp/password_db_drupal)'; \
	      FLUSH PRIVILEGES;" | mysql -uroot -p$(cat /tmp/password_db_root) && \
  supervisorctl stop all
RUN rm /tmp/password_db_root


##### Setup Drupal site

# Cache behat requirements
RUN mkdir -p /var/shared/sites/wedding/site
ADD site/tests /var/shared/sites/wedding/site/tests
RUN composer -q -d=/var/shared/sites/wedding/site/tests install

# Import database
ADD ./db/ivan_wedding.sql /tmp/drupal.sql
RUN supervisord -c /etc/supervisord.conf && mysql_wait && \
  mysql -udrupal -p$(cat /tmp/password_db_drupal) drupal < /tmp/drupal.sql && \
  supervisorctl stop all

# Setup code, fix permissions
RUN rm -rf /var/www && ln -s /var/shared/sites/wedding/site /var/www
ADD . /tmp/repo
RUN cp -TR /tmp/repo /var/shared/sites/wedding && \
  mkdir /var/www/sites/default/files && \
  chown -R www-data /var/www/ && \
  chmod -R o-rwx /var/www/ && \
  chmod -R ug+rX /var/www/ && \
  chmod -R ug+w /var/www/sites/default/files

# Create settings.php
ADD deploy/settings.db /tmp/settings.db
RUN (cat /var/www/sites/default/default.settings.php /tmp/settings.db) | \
  sed -e "s/%%PASSWORD%%/$(cat /tmp/password_db_drupal)/" \
  > /tmp/settings.php
RUN cp /tmp/settings.php /var/www/sites/default/settings.php && \
    chown www-data:www-data /var/www/sites/default/settings.php && \
    chmod a-w /var/www/sites/default/settings.php

# Run updb
RUN supervisord -c /etc/supervisord.conf && mysql_wait && \
  cd /var/www/ && drush -y updb && supervisorctl stop all

# Set up behat
ADD deploy/behat /usr/local/bin/
ADD deploy/docker_host_ip /tmp/docker_host_ip
ADD deploy/selenium_ip /tmp/selenium_ip
RUN sed -i "s/DOCKER_HOST_IP/$(cat /tmp/docker_host_ip)/; \
 s/SELENIUM_IP/$(cat /tmp/selenium_ip)/" /var/www/tests/behat.yml
RUN composer -q -d=/var/www/tests install

EXPOSE 80
EXPOSE 22
CMD ["supervisord", "-n"]
