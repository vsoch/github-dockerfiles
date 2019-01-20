[![dockeri.co](http://dockeri.co/image/bandsintown/php)](https://hub.docker.com/r/bandsintown/php/)

[![Build status](https://badge.buildkite.com/aa01d972592c1c0ca35be92671f04142dd8a7294b0f7f78ad3.svg)](https://buildkite.com/bandsintown/docker-php)
[![GitHub issues](https://img.shields.io/github/issues/bandsintown/docker-php.svg "GitHub issues")](https://github.com/bandsintown/docker-php)
[![GitHub stars](https://img.shields.io/github/stars/bandsintown/docker-php.svg "GitHub stars")](https://github.com/bandsintown/docker-php)
[![Docker layers](https://images.microbadger.com/badges/image/bandsintown/docker-php.svg)](http://microbadger.com/images/bandsintown/docker-php)


# PHP

Docker image for php-fpm with Consul

This image is based on the [Bandsintown Alpine Linux image](https://github.com/bandsintown/docker-alpine) and the [PHP-FPM alpine](https://hub.docker.com/_/php/). Alpine Linux is much smaller than most distribution base images (~5MB), and thus leads to much slimmer images in general.

This variant is highly recommended when final image size being as small as possible is desired. The main caveat to note is that it does use musl libc instead of glibc and friends, so certain software might run into issues depending on the depth of their libc requirements. However, most software doesn't have an issue with this, so this variant is usually a very safe choice. See this Hacker News comment thread for more discussion of the issues that might arise and some pro/con comparisons of using Alpine-based images.

To minimize image size, it's uncommon for additional related tools (such as git or bash) to be included in Alpine-based images. Using this image as a base, add the things you need in your own Dockerfile (see the alpine image description for examples of how to install packages if you are unfamiliar).

## Motivation

We built this image to use Consul and Consul Template to be able to configure php dynamically.

In particular we want to be able to php.ini and php-fpm.conf files.

This image allows to define the `php.ini` and `php-fpm.conf` files as a Consul keys.

We also installed in the image some useful tool / extensions: 
  - [Memcached extension](http://php.net/manual/en/book.memcached.php)
  - [Composer](https://getcomposer.org/) 

## Configuration through Consul

To manage the php configuration through Consul you have to create a Consul key at `service/php/php.ini` or/and `service/php/php-fpm.conf` to register the configurations.

The default files are used in case the consul keys are not defined.


## Extensions installation

The image can be modifided to include more extensions offered by the PHP project or 3rd parties.

Some extensions are not provided with the PHP source, but are instead available through [PECL](https://pecl.php.net/). To install a PECL extension, use pecl install to download and compile it, then use docker-php-ext-enable to enable it:

```dockerfile
FROM php:7.1-fpm
   RUN pecl install redis-3.1.0 \
       && pecl install xdebug-2.5.0 \
       && docker-php-ext-enable redis xdebug
   FROM php:5.6-fpm
   RUN apt-get update && apt-get install -y libmemcached-dev zlib1g-dev \
       && pecl install memcached-2.2.0 \
       && docker-php-ext-enable memcached
```
## Other extenstions

Some extensions are not provided via either Core or PECL; these can be installed too, although the process is less automated:

```dockerfile
FROM php:5.6-apache
RUN curl -fsSL 'https://xcache.lighttpd.net/pub/Releases/3.2.0/xcache-3.2.0.tar.gz' -o xcache.tar.gz \
    && mkdir -p xcache \
    && tar -xf xcache.tar.gz -C xcache --strip-components=1 \
    && rm xcache.tar.gz \
    && ( \
        cd xcache \
        && phpize \
        && ./configure --enable-xcache \
        && make -j$(nproc) \
        && make install \
    ) \
    && rm -r xcache \
    && docker-php-ext-enable xcache
```

The ```docker-php-ext-*``` scripts can accept an arbitrary path, but it must be absolute (to disambiguate from built-in extension names), so the above example could also be written as the following:

```dockerfile
FROM php:5.6-apache
RUN curl -fsSL 'https://xcache.lighttpd.net/pub/Releases/3.2.0/xcache-3.2.0.tar.gz' -o xcache.tar.gz \
    && mkdir -p /tmp/xcache \
    && tar -xf xcache.tar.gz -C /tmp/xcache --strip-components=1 \
    && rm xcache.tar.gz \
    && docker-php-ext-configure /tmp/xcache --enable-xcache \
    && docker-php-ext-install /tmp/xcache \
    && rm -r /tmp/xcache
```
