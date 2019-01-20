FROM augustash/baseimage:0.9.19-1
MAINTAINER Pete McWilliams <pmcwilliams@augustash.com>

# environment
ENV GPG_KEYS 1A4E8B7277C42E53DBA9C7B9BCAA30EA9C0D5763
ENV PHP_DIR /etc/php
ENV PHP_PREFIX /usr/local
ENV PHP_EXTRA_CONFIGURE_ARGS --with-fpm-user=ash --with-fpm-group=ash
ENV PHP_REDIS_VERSION 3.0.0
ENV PHP_VERSION 7.0.13
ENV PHP_FILENAME php-7.0.13.tar.xz
ENV PHP_SHA256 357ba7f93975d7d836abed0852dc3ed96a988af539e87750613294cbee82f1bf

ENV APTLIST \
        bzip2 \
        imagemagick \
        libc-client2007e \
        libcurl3 \
        libedit2 \
        libmcrypt4 \
        libmhash2 \
        libsqlite3-0 \
        libxml2 \
        libxslt1.1 \
        mysql-client \
        xfonts-base \
        xfonts-75dpi

ENV BUILD_DEPS \
        autoconf \
        file \
        g++ \
        gcc \
        libc-dev \
        libc-client2007e-dev \
        libcurl4-openssl-dev \
        libedit-dev \
        libicu-dev \
        libjpeg-dev \
        libkrb5-dev \
        libldap2-dev \
        libmagickwand-dev \
        libmcrypt-dev \
        libmhash-dev \
        libpng12-dev \
        libpq-dev \
        libsqlite3-dev \
        libssl-dev \
        libxml2-dev \
        libxslt1-dev \
        make \
        pkg-config \
        re2c

# download source
RUN \
    cd /usr/src && \
    curl -fsSL -o php.tar.xz "https://secure.php.net/get/$PHP_FILENAME/from/this/mirror" && \
    echo "$PHP_SHA256 *php.tar.xz" | sha256sum -c - && \
    curl -fsSL -o php.tar.xz.asc "https://secure.php.net/get/$PHP_FILENAME.asc/from/this/mirror" && \
    export GNUPGHOME="$(mktemp -d)" && \
    for key in $GPG_KEYS; do \
        gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
    done && \
    gpg --batch --verify php.tar.xz.asc php.tar.xz && \
    rm -r "$GNUPGHOME" && \
    mkdir -p $PHP_DIR/conf.d

# install helper scripts
COPY scripts/ /usr/local/bin/

# install packages
RUN \
    apt-get -yqq update && \
    apt-get -yqq install --no-install-recommends --no-install-suggests $APTLIST $BUILD_DEPS && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# build php
RUN \
    docker-php-source extract && \
    cd /usr/src/php && \
    ./configure \
        --prefix="$PHP_PREFIX" \
        --with-config-file-path="$PHP_DIR" \
        --with-config-file-scan-dir="$PHP_DIR/conf.d" \
        --disable-cgi \
        --enable-fpm \
        --enable-ftp \
        --enable-intl \
        --enable-mbstring \
        --enable-mysqlnd \
        --enable-opcache \
        --enable-soap \
        --with-curl \
        --with-gd \
        --with-libedit \
        --with-mcrypt \
        --with-mhash \
        --with-openssl \
        --with-xsl \
        --with-zlib \
        $PHP_EXTRA_CONFIGURE_ARGS && \
    make -j"$(nproc)" && \
    make install && \
    { find /usr/local/bin /usr/local/sbin -type f -executable -exec strip --strip-all '{}' + || true; } && \
    make clean && \
    cp php.ini-production $PHP_DIR/php.ini.default && \
    docker-php-source delete

# build exentions
RUN \
    pecl install imagick && \
    pecl install "redis-$PHP_REDIS_VERSION"

RUN \
    docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr && \
    docker-php-ext-enable imagick && \
    docker-php-ext-enable redis && \
    docker-php-ext-install \
        bcmath \
        iconv \
        json \
        opcache \
        pdo_mysql \
        soap \
        xml \
        zip

# install tools
RUN curl -sS https://getcomposer.org/installer | php -- \
    --install-dir=/usr/local/bin --filename=composer

# clean up
RUN \
    apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $BUILD_DEPS && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# add scripts
COPY confd/ /etc/confd/
COPY init/ /etc/my_init.d/
COPY services/ /etc/service/
RUN  chmod +x /etc/service/*/run /etc/my_init.d/*.sh

# exports
EXPOSE 9000
CMD ["/sbin/my_init"]
