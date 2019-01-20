FROM php:7.0-apache
MAINTAINER "Tiago"

RUN a2enmod rewrite

RUN apt-get update && apt-get install -y libpng12-dev libjpeg-dev libpq-dev mysql-client drush \
	&& rm -rf /var/lib/apt/lists/* \
	&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \
	&& docker-php-ext-install gd mbstring pdo pdo_mysql pdo_pgsql zip
