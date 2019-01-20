FROM andthensome/docker-php-5.3-fpm

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

RUN mkdir -p /usr/include/freetype2/freetype && ln -s /usr/include/freetype2/freetype.h /usr/include/freetype2/freetype/freetype.h


RUN docker-php-ext-install mbstring \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install  gd \
    && docker-php-ext-install  zip \
    && docker-php-ext-install  mcrypt


#RUN curl -L https://pecl.php.net/get/redis-2.2.7.tgz > /tmp/redis.tgz \
#    && mkdir -p /usr/src/php/ext \
#    && tar -xvf /tmp/redis.tgz -C /usr/src/php/ext \
#    && rm /tmp/redis.tgz \
#    && docker-php-ext-install redis-2.2.7

RUN pecl install memcache && docker-php-ext-enable memcache

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
