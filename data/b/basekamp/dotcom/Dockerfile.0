FROM php:5-apache 

ENV GOTPL_VER 0.1.5
ENV GOTPL_URL https://github.com/wodby/gotpl/releases/download/${GOTPL_VER}/gotpl-linux-amd64-${GOTPL_VER}.tar.gz

RUN docker-php-ext-install mysql mysqli pdo pdo_mysql
RUN apt-get update && apt-get install -y \
        # Recommended by Drupal.
        wget \
        # Needed to install drush at runtime without git.
        zip \
        # Needed for drush to perform sql operations.
        mysql-client \
        # Other for Drupal.
        php5-json \
        php5-xmlrpc \
        php5-xsl && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# GD toolkit needs more love.
# See: https://github.com/docker-library/php/issues/322#issuecomment-299255477
RUN apt-get update && apt-get install -y \
		libfreetype6-dev \
		libjpeg62-turbo-dev \
		libmcrypt-dev \
		libpng12-dev \
	&& docker-php-ext-install -j$(nproc) iconv mcrypt \
	&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
	&& docker-php-ext-install -j$(nproc) gd

# Apache mods.
RUN a2enmod rewrite

# PHP config.
RUN echo 'memory_limit = 512M' >> /usr/local/etc/php/conf.d/local.ini && \
    echo 'upload_max_filesize = 100M' >> /usr/local/etc/php/conf.d/local.ini && \
    echo 'post_max_size = 100M' >> /usr/local/etc/php/conf.d/local.ini && \
    # Disable errors on production.
    echo 'error_reporting = E_ALL & ~E_NOTICE & ~E_WARNING' >> /usr/local/etc/php/conf.d/local.ini && \
    echo 'error_Reporting = off'  >> /usr/local/etc/php/conf.d/local.ini

# Composer.
RUN curl --silent --output /tmp/composer-setup.php https://getcomposer.org/installer && \
    php /tmp/composer-setup.php --install-dir=/usr/local/bin --filename=composer && \
    rm /tmp/composer-setup.php

# Drush.
RUN composer global require drush/drush:8.1.13 && \
    ln -s /root/.composer/vendor/bin/drush /usr/local/bin/drush

# Go TPL for Drupal settings file.
RUN wget -qO- ${GOTPL_URL} | tar xz -C /usr/local/bin
ENV MARIADB_HOST ${MARIADB_HOST:-}
ENV MARIADB_DATABASE ${MARIADB_DATABASE:-}
ENV MARIADB_USER ${MARIADB_USER:-}
ENV MARIADB_PASSWORD ${MARIADB_PASSWORD:-}
COPY templates /etc/gotpl/

WORKDIR /var/www/html

# Helm stable/drupal with persistence overwrites the volume mount to {}, so we
# perform file operations in this temporary directory, then move /html back to
# WORKDIR at runtime via docker-php-entrypoint.
COPY html /html
RUN mkdir /html/sites/default/files && chmod a+w /html/sites/default/files && \
    chown -R www-data:www-data /html
COPY docker-drupal-entrypoint /usr/local/bin/

EXPOSE 80 443
CMD ["docker-drupal-entrypoint"]
