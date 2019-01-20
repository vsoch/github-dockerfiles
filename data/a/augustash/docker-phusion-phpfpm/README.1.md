![https://www.augustash.com](http://augustash.s3.amazonaws.com/logos/ash-inline-color-500.png)

# PHP-FPM Image

**This `php-fpm` container is not currently aimed at public consumption. It exists as an internal tool for August Ash development and is built upon [Phusion](http://phusion.github.io/baseimage-docker/).**

## Usage

To build the Docker image, clone this repository and from the project directory run:

```bash
docker-compose build
```

Now start a new container from the image, expose the proper ports, and mount a volume for persistence:

```bash
docker-compose up -d
```

You can also start a container outside of Docker Compose:

```bash
docker run -d -P augustash/phpfpm:7.0.13
```

## Extensions

The following extra PHP extensions are enabled:

* `bcmath`
* `curl`
* `gd`
* `iconv`
* `imagick`
* `intl`
* `json`
* `mcrypt`
* `mhash`
* `opcache`
* `pdo_mysql`
* `redis`
* `soap`
* `xml`
* `xsl`
* `zip`

## Running One-off Commands

The image used for this container provides a facility to run single, one-off commands. Run a single command in the following manner:

```bash
docker run --rm -e SKIP_UPDATE=true YOUR_IMAGE /sbin/my_init -- <COMMAND ARGUMENTS>
```

The example syntax will:

* Run all system startup files, such as `/etc/my_init.d/*` and `/etc/rc.local`.
* Start all `runit` services.
* Run the specified command.
* When the specified command exits, stops all `runit` services.

The default invocation is too noisy for one-off commands. You may also not want to run the startup files. You can customize all this by passing arguments to `my_init`. For more information pass the help flag like `/sbin/my_init --help`.

As a practical example, run the following to get the PHP version:

```bash
docker run --rm -it -e SKIP_UPDATE=true augustash/phpfpm /sbin/my_init  --skip-startup-files --quiet -- php -v
```

## Volumes

One mount point for connecting data volumes from the host or other containers are available.

* `/src` - Application root

## Exposed Ports

* Port `9000`

## Available Environment Variables

* `SKIP_UPDATE`
* `PHPFPM_LISTEN_PORT`
* `PHPFPM_CACHE_HOST`
* `PHPFPM_CACHE_PORT`
* `PHPFPM_CACHE_PASSWORD`
* `PHPFPM_PM_MODE`
* `PHPFPM_PM_MAX_CHILDREN`
* `PHPFPM_PM_START_SERVERS`
* `PHPFPM_PM_MIN_SPARE_SERVERS`
* `PHPFPM_PM_MAX_SPARE_SERVERS`
* `PHPFPM_PM_MAX_REQUESTS`
* `PHPFPM_OUTPUT_BUFFERING`
* `PHPFPM_REALPATH_CACHE_SIZE`
* `PHPFPM_REALPATH_CACHE_TTL`
* `PHPFPM_MAX_EXECUTION_TIME`
* `PHPFPM_MAX_INPUT_TIME`
* `PHPFPM_MAX_INPUT_VARS`
* `PHPFPM_MEMORY_LIMIT`
* `PHPFPM_DISPLAY_ERRORS`
* `PHPFPM_LOG_ERRORS`
* `PHPFPM_UPLOAD_MAX_FILESIZE`
* `PHPFPM_POST_MAX_SIZE`
* `PHPFPM_DATE_TIMEZONE`
* `PHPFPM_OPCACHE_ENABLE`
* `PHPFPM_OPCACHE_ENABLE_CLI`
* `PHPFPM_OPCACHE_MEMORY_CONSUMPTION`
* `PHPFPM_OPCACHE_VALIDATE_TIMESTAMPS`
* `PHPFPM_FAST_SHUTDOWN`
