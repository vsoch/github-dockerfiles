
# Outrigger MariaDB

> MariaDB docker container with easy configuration via environment variables.

## Supported tags and respective `Dockerfile` links

-	[`5.5` (*5.5/Dockerfile*)](https://github.com/phase2/docker-mariadb/blob/master/5.5/Dockerfile) [![](https://images.microbadger.com/badges/version/outrigger/mariadb:5.5.svg)](https://microbadger.com/images/outrigger/mariadb:5.5 "Get your own version badge on microbadger.com")
-	[`10.0` (*10.0/Dockerfile*)](https://github.com/phase2/docker-mariadb/blob/master/10.0/Dockerfile) [![](https://images.microbadger.com/badges/version/outrigger/mariadb:10.0.svg)](https://microbadger.com/images/outrigger/mariadb:10.0 "Get your own version badge on microbadger.com")
-	[`10.1` (*10.1/Dockerfile*)](https://github.com/phase2/docker-mariadb/blob/master/10.1/Dockerfile) [![](https://images.microbadger.com/badges/version/outrigger/mariadb:10.1.svg)](https://microbadger.com/images/outrigger/mariadb:10.1 "Get your own version badge on microbadger.com")
-	[`10.2` (*10.2/Dockerfile*)](https://github.com/phase2/docker-mariadb/blob/master/10.2/Dockerfile) [![](https://images.microbadger.com/badges/version/outrigger/mariadb:10.2.svg)](https://microbadger.com/images/outrigger/mariadb:10.2 "Get your own version badge on microbadger.com")

This mariadb image is a MySQL compliant database image with configuration through
a collection of environment variables detailed below.

For more documentation on how Outrigger images are constructed and how to work
with them, please [see the documentation](http://docs.outrigger.sh/).

## How to use this image

Starting a MariaDB instance:

```bash
docker run --name some-mariadb -e MYSQL_PASS=my-secret-pw -d phase2/mariadb
```

... where some-mariadb is the name you want to assign to your container and
my-secret-pw is the password to be set for the MySQL root user

### Customizing Database Behavior

The MariaDB startup configuration is specified in the file `/etc/mysql/my.cnf`,
and that file in turn includes any files found in the `/etc/mysql/my.cnf.d`
directory that end with `.cnf`. Settings in files in this directory will augment
and/or override settings in /etc/mysql/my.cnf.

If you want to use a customized MySQL configuration, you can create your
alternative configuration file in a directory on the host machine and then mount
that directory location as `/etc/mysql/my.cnf.d` inside the mariadb container.

If `/my/custom/config-file.cnf` is the path and name of your custom
configuration file, you can start your mariadb container like this note that
only the directory path of the custom config file is used in this command):

```bash
docker run --name some-mariadb -v /my/custom:/etc/mysql/my.cnf.d -e MYSQL_PASS=my-secret-pw -d outrigger/mariadb
```

This will start a new container some-mariadb where the MariaDB instance uses the
combined startup settings from /etc/mysql/my.cnf and
/etc/mysql/conf.d/config-file.cnf, with settings from the latter taking
precedence.

> **If you add custom configuration in this way, you may invalidate the
environment variables as source of database configuration.**

## Environment Variables

Outrigger images use Environment Variables and [confd](https://github.com/kelseyhightower/confd)
to "templatize" a number of Docker environment configurations. These templates are
processed on startup with environment variables passed in via the docker run
command-line or via your docker-compose manifest file. Here are the "tunable"
configurations offered by this image.

* `MYSQL_PASS`: [`admin`] This will be the password that is set for the user
  named **admin**.  The root user does not have a password and allow local connections only.
* `MYSQL_DATABASE`: [e.g., `app_db`] If set, a database with this name will be
created when the database first starts up. *This is not set by default.*
* `MYSQL_EXPIRE_LOGS_DAYS`: [`10`]
* `MYSQL_MAX_ALLOWED_PACKET`: [`16M`]
* `MYSQL_MAX_CONNECTIONS`: [`10`]
* `MYSQL_QUERY_CACHE_LIMIT`: [`1M`]
* `MYSQL_QUERY_CACHE_SIZE`: [`16M`]
* `MYSQL_SLOW_QUERY_LOG`: [`0`] By default the slow query log is disabled.
* `MYSQL_LONG_QUERY_TIME`: [`10`] Long query threshold time in seconds.
* `MYSQL_LOG_QUERY_NO_INDEX`: [`0`] By default do not log queries that do not use an index.

## Security Reports

Please email outrigger@phase2technology with security concerns.

## Maintainers

[![Phase2 Logo](https://s3.amazonaws.com/phase2.public/logos/phase2-logo.png)](https://www.phase2technology.com)
