# Outrigger Build

> The Outrigger Build image provides a command-line toolkit for PHP & Node development with Drupal support.

## Supported tags and respective `Dockerfile` links

- [`php55` (*php55/Dockerfile*)](https://github.com/phase2/docker-build/blob/master/php55/Dockerfile) [![](https://images.microbadger.com/badges/image/outrigger/build:php55.svg)](https://microbadger.com/images/outrigger/build:php55 "Get your own image badge on microbadger.com")
- [`php56` (*php56/Dockerfile*)](https://github.com/phase2/docker-build/blob/master/php56/Dockerfile) [![](https://images.microbadger.com/badges/image/outrigger/build:php56.svg)](https://microbadger.com/images/outrigger/build:php56 "Get your own image badge on microbadger.com")
- [`php70` (*php70/Dockerfile*)](https://github.com/phase2/docker-build/blob/master/php70/Dockerfile) [![](https://images.microbadger.com/badges/image/outrigger/build:php70.svg)](https://microbadger.com/images/outrigger/build:php70 "Get your own image badge on microbadger.com")
- [`php71` (*php71/Dockerfile*)](https://github.com/phase2/docker-build/blob/master/php71/Dockerfile) [![](https://images.microbadger.com/badges/image/outrigger/build:php71.svg)](https://microbadger.com/images/outrigger/build:php71 "Get your own image badge on microbadger.com")
- [`php72` (*php71/Dockerfile*)](https://github.com/phase2/docker-build/blob/master/php72/Dockerfile) [![](https://images.microbadger.com/badges/image/outrigger/build:php72.svg)](https://microbadger.com/images/outrigger/build:php72 "Get your own image badge on microbadger.com")

This image provides the many development tools necessary to build applications
the Outrigger way, bundled with a wide array of tools useful for development and
troubleshooting via the command-line interface. While it is possible to directly
connect to the web containers, this is the preferred way to perform "server work".

For more documentation on how Outrigger images are constructed and how to work
with them, please [see the documentation](http://docs.outrigger.sh).

## Features

* Out of the box support for PHP (version based on tag), Ruby and multiple Node LTS versions (based on environment var, see below)
* Global availability of Composer, Drush, NPM, Bower, Grunt, Gulp, and Yeoman.

For more details of specific packages, libraries, and utilities, please see the
[Dockerfile](https://github.com/phase2/docker-build/blob/master/php71/Dockerfile).

### Drush (Drupal Shell) Integration

There is global configuration for Drush at `/etc/drush/drushrc.php`.

Default configuration in this file provides the following:

* Unlimited memory for PHP operations run via Drush.
* Unlimited execution time for PHP operations run via Drush.
* Drush commands will be looked up in `/etc/drush/commands`.
* Drush aliases will be looked up in `/etc/drush`.

### Additional Commands

* **Registry Rebuild**: `drush rr` is included by default.

### BASH History Persistence

If you would like your bash history preserved, provide a volume mount to a persistent
data location at /root/bash and initialization scripts will ensure your .bash\_history
file is written there. For example `/data/PROJECT/ENV/bash:/root/bash`

## Environment Variables

Outrigger images use Environment Variables and [confd](https://github.com/kelseyhightower/confd) to templatize a number
of Docker environment configurations. These templates are processed on startup with environment variables passed in
via the docker run command-line or via your `docker-compose.yml` manifest file. Here are the "tunable" configurations
offered by this image.

* `NODE_VERSION`: [`4`|`6`|`8`] Defaults to 4. Selects the major version of Node
  to make available to all tools via nvm. The latest minor release as of the image build will be used.
* `PHP_XDEBUG`: [`"true"`|`"false"`] Specify whether the PHP Xdebug extension should be enabled. Xdebug is configured to autostart on script execution and attempt to use a remote connection to 192.168.99.1 on port 9000.
* `PHP_YAML`: [`"false"`|`"true"`] A string literal to enable PHP YAML extension.
  Defaults to `"false"`.
* `XDEBUG_CONFIG`: This can be used to override many of the Xdebug remote settings. You can find documentation of this variable at [https://xdebug.org/docs/remote](https://xdebug.org/docs/remote). By default this variable is not set as all needed configuration is set within the .ini file. An example setting to override the remote host and port would be `"remote_host=172.17.0.1 remote_port=9999"`.

### Default Tools Configuration

A number of tools that are built into the Build image can be further configured by environment variables. These can be overridden
by your `docker run` command or your docker-compose configuration. For more details on these variables or other environment variable
options, check the configuration documentation for individual tools.

* **Composer**:
    * `COMPOSER_ALLOW_SUPERUSER`: [`1`] Run composer as the root user.
* **npm**:
    * `NPM_CONFIG_UNSAFE_PERM`: [`true`] Run npm commands with the --unsafe-perm flag. This makes behavior of running npm as root more consistent when using npm scripts that call other npm scripts.
* **bower**:
    * `BOWER_ALLOW_ROOT`: [`true`] Bower will refuse to execute when run as root without the --allow-root flag. This sets that as a persisting configuration.

Unless you are modifying a customized Build image to run as a user other than **root** you will not need to change these.

## Security Reports

Please email outrigger@phase2technology.com with security concerns.

## Maintainers

[![Phase2 Logo](https://s3.amazonaws.com/phase2.public/logos/phase2-logo.png)](https://www.phase2technology.com)
