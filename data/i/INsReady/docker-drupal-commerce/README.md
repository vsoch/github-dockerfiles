# Supported tags and respective `Dockerfile` links

-	[`8.6-2.x`, `latest` (*Dockerfile*)](https://github.com/INsReady/docker-drupal-commerce/blob/master/8.6/Dockerfile)
-	[`dev` (*Dockerfile*)](https://github.com/INsReady/docker-drupal-commerce/blob/master/dev/Dockerfile)

This image is updated via pull requests to [the `INsReady/docker-drupal-commerce` GitHub repo](https://github.com/INsReady/docker-drupal-commerce).


# What is Drupal Commerce?

Drupal Commerce is used to build eCommerce websites and applications of all sizes. At its core it is lean and mean, enforcing strict development standards and leveraging the greatest features of Drupal and major modules like Views and Rules for maximum flexibility.

> [Drupal Commerce Documentation](http://docs.drupalcommerce.org/)

# How to use this image

The basic pattern for starting a `drupal commerce` instance is:

```console
$ docker run --name some-drupal -d insready/drupal-commerce
```

If you'd like to be able to access the instance from the host without the container's IP, standard port mappings can be used:

```console
$ docker run --name some-drupal -p 8080:80 -d insready/drupal-commerce
```

Then, access it via `http://localhost:8080` or `http://host-ip:8080` in a browser.

There are multiple database types supported by this image, most easily used via standard container linking. In the default configuration, SQLite can be used to avoid a second container and write to flat-files. More detailed instructions for different (more production-ready) database types follow.

When first accessing the webserver provided by this image, it will go through a brief setup process. The details provided below are specifically for the "Set up database" step of that configuration process.

## MySQL

```console
$ docker run --name some-drupal --link some-mysql:mysql -d insready/drupal-commerce
```

-	Database type: `MySQL, MariaDB, or equivalent`
-	Database name/username/password: `<details for accessing your MySQL instance>` (`MYSQL_USER`, `MYSQL_PASSWORD`, `MYSQL_DATABASE`; see environment variables in the description for [`mysql`](https://registry.hub.docker.com/_/mysql/))
-	ADVANCED OPTIONS; Database host: `mysql` (for using the `/etc/hosts` entry added by `--link` to access the linked container's MySQL instance)

## PostgreSQL

```console
$ docker run --name some-drupal --link some-postgres:postgres -d insready/drupal-commerce
```

-	Database type: `PostgreSQL`
-	Database name/username/password: `<details for accessing your PostgreSQL instance>` (`POSTGRES_USER`, `POSTGRES_PASSWORD`; see environment variables in the description for [`postgres`](https://registry.hub.docker.com/_/postgres/))
-	ADVANCED OPTIONS; Database host: `postgres` (for using the `/etc/hosts` entry added by `--link` to access the linked container's PostgreSQL instance)

## Adding additional libraries / extensions

This image does not provide any additional PHP extensions or other libraries, even if they are required by popular plugins. There are an infinite number of possible plugins, and they potentially require any extension PHP supports. Including every PHP extension that exists would dramatically increase the image size.

If you need additional PHP extensions, you'll need to create your own image `FROM` this one. The [documentation of the `php` image](https://github.com/docker-library/docs/blob/master/php/README.md#how-to-install-more-php-extensions) explains how to compile additional extensions. Additionally, the [`drupal:7` Dockerfile](https://github.com/docker-library/drupal/blob/bee08efba505b740a14d68254d6e51af7ab2f3ea/7/Dockerfile#L6-9) has an example of doing this.

The following Docker Hub features can help with the task of keeping your dependent images up-to-date:

-	[Automated Builds](https://docs.docker.com/docker-hub/builds/) let Docker Hub automatically build your Dockerfile each time you push changes to it.
-	[Repository Links](https://docs.docker.com/docker-hub/builds/#repository-links) can ensure that your image is also rebuilt any time `drupal` is updated.


# License

View [license information](http://www.gnu.org/licenses/old-licenses/gpl-2.0.html) for the software contained in this image.

# Supported Docker versions

This image is officially supported on Docker version 1.12.5.

Support for older versions (down to 1.6) is provided on a best-effort basis.

Please see [the Docker installation documentation](https://docs.docker.com/installation/) for details on how to upgrade your Docker daemon.

# User Feedback

## Documentation

Documentation for this image is stored in the [`README.md`](https://github.com/INsReady/docker-drupal-commerce/blob/master/README.md) of the [`insready/docker-drupal-commerce` GitHub repo](https://github.com/INsReady/docker-drupal-commerce). Be sure to familiarize yourself with the [repository's `README.md` file](https://github.com/docker-library/docs/blob/master/README.md) before attempting a pull request.

## Issues

If you have any problems with or questions about this image, please contact us through a [GitHub issue](https://github.com/INsReady/docker-drupal-commerce/issues).

You can also reach many of the official image maintainers via the `#docker-library` IRC channel on [Freenode](https://freenode.net).

## Contributing

You are invited to contribute new features, fixes, or updates, large or small; we are always thrilled to receive pull requests, and do our best to process them as fast as we can.

Before you start to code, we recommend discussing your plans through a [GitHub issue](https://github.com/INsReady/docker-drupal-commerce/issues), especially for more ambitious contributions. This gives other contributors a chance to point you in the right direction, give you feedback on your design, and help you find out if someone else is working on the same thing.
