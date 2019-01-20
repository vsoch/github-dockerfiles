# Outrigger Apache/PHP

> PHP application server for Apache w/ PHP-FPM

## Supported tags and respective `Dockerfile` links

-	[`php55` (*php55/Dockerfile*)](https://github.com/phase2/docker-apache-php/blob/master/php55/Dockerfile)
[![](https://images.microbadger.com/badges/image/outrigger/apache-php:php55.svg)](https://microbadger.com/images/outrigger/apache-php:php55 "Get your own image badge on microbadger.com")
-	[`php56` (*php56/Dockerfile*)](https://github.com/phase2/docker-apache-php/blob/master/php56/Dockerfile)
[![](https://images.microbadger.com/badges/image/outrigger/apache-php:php56.svg)](https://microbadger.com/images/outrigger/apache-php:php56 "Get your own image badge on microbadger.com")
-	[`php70` (*php70/Dockerfile*)](https://github.com/phase2/docker-apache-php/blob/master/php70/Dockerfile)
[![](https://images.microbadger.com/badges/image/outrigger/apache-php:php70.svg)](https://microbadger.com/images/outrigger/apache-php:php70 "Get your own image badge on microbadger.com")
-	[`php71` (*php71/Dockerfile*)](https://github.com/phase2/docker-apache-php/blob/master/php71/Dockerfile)
[![](https://images.microbadger.com/badges/image/outrigger/apache-php:php71.svg)](https://microbadger.com/images/outrigger/apache-php:php71 "Get your own image badge on microbadger.com")
-	[`php72` (*php72/Dockerfile*)](https://github.com/phase2/docker-apache-php/blob/master/php72/Dockerfile)
[![](https://images.microbadger.com/badges/image/outrigger/apache-php:php72.svg)](https://microbadger.com/images/outrigger/apache-php:php72 "Get your own image badge on microbadger.com")

An image for running Apache with PHP-FPM based on outrigger/apache-php-base.
This includes a default VirtualHost.

For more documentation on how Outrigger images are constructed and how to work
with them, please [see the documentation](http://docs.outrigger.sh/).

## Features

See [Apache PHP Base](https://github.com/phase2/docker-apache-php-base) for all Features and Configuration

## Environment Variables

Outrigger images use Environment Variables and [confd](https://github.com/kelseyhightower/confd)
to "templatize" a number of Docker environment configurations. These templates are
processed on startup with environment variables passed in via the docker run
command-line or via your docker-compose manifest file. Here are the "tunable"
configurations offered by this image.

## Security Reports

Please email outrigger@phase2technology.com with security concerns.

## Maintainers

[![Phase2 Logo](https://s3.amazonaws.com/phase2.public/logos/phase2-logo.png)](https://www.phase2technology.com)
