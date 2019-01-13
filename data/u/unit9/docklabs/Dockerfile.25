FROM php:5.6-apache

RUN apt-get update \
    && apt-get install -y \
        rrdtool \
        git \
    && rm -rf /var/cache/apt /var/lib/apt/lists/*

RUN git clone https://github.com/pommi/CGP /var/www/html \
    && cd /var/www/html \
    && git reset --hard af2251eed3fc1e4969214de01b52d6badf714ccc \
    && rm -rf .git \
    && a2enmod rewrite
