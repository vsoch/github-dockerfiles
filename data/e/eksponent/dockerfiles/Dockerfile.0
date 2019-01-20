FROM php:5.6-fpm

# Install modules
RUN apt-get update && apt-get install -y  --no-install-recommends \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libpng12-dev \
    libpq-dev \
    apt-utils \
    mysql-client \
    zlib1g-dev \
    imagemagick \
    libxml2-dev \
    unzip \
    libmcrypt-dev

RUN docker-php-ext-install pdo_mysql mbstring opcache \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd \
    && docker-php-ext-install -j$(nproc) zip \
    && docker-php-ext-install -j$(nproc) mcrypt

# imagemagick as PHP extension
RUN apt-get install -y libmagickwand-6.q16-dev --no-install-recommends \
 && ln -s /usr/lib/x86_64-linux-gnu/ImageMagick-6.8.9/bin-Q16/MagickWand-config /usr/bin \
 && pecl install imagick \
 && echo "extension=imagick.so" > /usr/local/etc/php/conf.d/ext-imagick.ini

# LDAP (used by RUC)
RUN apt-get install libldap2-dev -y && \
    docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu && \
    docker-php-ext-install -j$(nproc) ldap 

RUN docker-php-ext-install -j$(nproc) soap
# BCMath is needed on Scleroseforeningen D8
RUN docker-php-ext-install -j$(nproc) bcmath && \
    docker-php-ext-enable bcmath


RUN curl -L https://pecl.php.net/get/redis-2.2.7.tgz > /tmp/redis.tgz \
    && mkdir -p /usr/src/php/ext \
    && tar -xvf /tmp/redis.tgz -C /usr/src/php/ext \
    && rm /tmp/redis.tgz \
    && docker-php-ext-install redis-2.2.7

RUN pecl install memcache && docker-php-ext-enable memcache

ADD local.ini /usr/local/etc/php/conf.d/local.ini
ADD fake-sendmail.sh /usr/local/bin/fake-sendmail.sh

ADD entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin/ --filename=composer

# Install Drush.
RUN composer global require drush/drush:7.*
ADD profile-extras.sh /etc/profile.d/profile-extras.sh

# Symlink in all the new stuff to the default path, to be even more sure it's discovered.
RUN ln -s /root/.composer/vendor/bin/* /usr/local/bin/

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
