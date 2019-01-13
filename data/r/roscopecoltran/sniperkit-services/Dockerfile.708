FROM alpine:3.3

RUN apk --update --no-progress add build-base php-dev autoconf \
    php-fpm php-mcrypt php-curl php-gd php-json php-openssl \
    php-pdo_mysql php-pdo_sqlite php-phar php-iconv php-ctype \
    php-opcache php-mysqli php-zip zlib git bash openssl-dev php-pgsql \
    && curl -s -o phpredis-2.2.7.tar.gz -b a -L https://github.com/phpredis/phpredis/archive/2.2.7.tar.gz \
    && curl -s -o xdebug-2.3.3.tgz -b a -L https://xdebug.org/files/xdebug-2.3.3.tgz \
    && curl -s -o xhprof-0.9.4.tgz -b a -L http://pecl.php.net/get/xhprof-0.9.4.tgz \
    && curl -s -o mongo-1.6.14.tgz -b a -L http://pecl.php.net/get/mongo-1.6.14.tgz \
    && cd / && tar zxvf phpredis-2.2.7.tar.gz && cd /phpredis-2.2.7 && phpize \
    &&./configure && make && make install && rm -rf /phpredis-2.2.7 /phpredis-2.2.7.tar.gz \
    && cd / && tar zxvf xdebug-2.3.3.tgz && cd /xdebug-2.3.3 && phpize \
    && ./configure && make && make install && rm -rf /xdebug-2.3.3 /xdebug-2.3.3.tgz \
    && cd / && tar zxvf xhprof-0.9.4.tgz && cd /xhprof-0.9.4/extension && phpize \
    && ./configure && make && make install && rm -rf /xhprof-0.9.4 /xhprof-0.9.4.tgz \
    && cd / && tar zxvf mongo-1.6.14.tgz && cd /mongo-1.6.14 && phpize \
    && ./configure && make && make install && rm -rf /mongo-1.6.14 /mongo-1.6.14.tgz \
    && apk del build-base autoconf openssl-dev \
    && rm -rf /var/cache/apk/* \

RUN echo "export TERM=xterm" >> /root/.bashrc \
    && rm -rf /etc/php/php-fpm.conf /etc/php/php.ini \
    && mkdir /php \
    && ln -s /php/php.ini /etc/php/php.ini \
    && ln -s /php/php-fpm.conf /etc/php/php-fpm.conf

WORKDIR /www

CMD php-fpm

#RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/
#RUN docker-php-ext-install mbstring

# start setup phptrace
#COPY phptrace-0.3.0.tar.gz /
#RUN cd / && tar zxvf phptrace-0.3.0.tar.gz
#RUN cd /phptrace-0.3.0/extension && phpize && ./configure && make && make install && cd ../cmdtool && make && mv phptrace /usr/bin && mv trace-php /usr/bin/
#RUN rm -rf /phptrace-0.3.0 /php-redis-2.2.7.tar.gz
# end setup phptrace

