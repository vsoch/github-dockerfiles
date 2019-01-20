FROM php:5.6-apache
MAINTAINER Karim Ratib <karim@meedan.com>

RUN set -xe \
    && apt-get update \
    && apt-get install -y libpng-dev libjpeg-dev libpq-dev libxml2-dev \
    && docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \
    && docker-php-ext-install mysqli pdo_mysql gd soap \
    && rm -rf /var/lib/apt/lists/*

RUN set -xe \
    && ln -sf /usr/share/zoneinfo/America/Vancouver /etc/localtime \
    && touch /usr/local/etc/php/conf.d/mantis.ini \
    && echo 'date.timezone = "America/Vancouver"' >> /usr/local/etc/php/conf.d/mantis.ini \
    && echo 'log_errors = 1' >> /usr/local/etc/php/conf.d/mantis.ini

COPY ./ /var/www/html
