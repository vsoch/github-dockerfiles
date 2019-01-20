## Supported tags and respective `Dockerfile` links
-	[`8.6`, `latest` (*Dockerfile*)](https://github.com/INsReady/docker-drupal-dev/blob/master/8.6/Dockerfile)
-	[`8.5` (*Dockerfile*)](https://github.com/INsReady/docker-drupal-dev/blob/master/8.5/Dockerfile)
-   [`contentacms` (*Dockerfile*)](https://github.com/INsReady/docker-drupal-dev/blob/master/contentacms/Dockerfile)
-   [`lightning` (*Dockerfile*)](https://github.com/INsReady/docker-drupal-dev/blob/master/lightning/Dockerfile)
-   [`reservoir` (*Dockerfile*)](https://github.com/INsReady/docker-drupal-dev/blob/master/reservoir/Dockerfile)
-   [`thunder` (*Dockerfile*)](https://github.com/INsReady/docker-drupal-dev/blob/master/thunder/Dockerfile)
-   [`varbase` (*Dockerfile*)](https://github.com/INsReady/docker-drupal-dev/blob/master/varbase/Dockerfile)
-	[`7` (*Dockerfile*)](https://github.com/INsReady/docker-drupal-dev/blob/7/Dockerfile)

This image is updated via pull requests to [the `INsReady/docker-drupal-dev` GitHub repo](https://github.com/INsReady/docker-drupal-dev).

## Why do we need this image?

The official Drupal Docker library is optimized for production. Therefore, it doesn't have any developers tools built-in. This image is directly dependent on the official library, and adds a list of tools that necessary for Drupal development. Developers shall use this image for development, and use the official library for production. There should be zero difference in how Drupal works between these two images.

> [Offical Drupal Docker Library](https://hub.docker.com/_/drupal/)

## What tools are included in the developer environment?

- Git
- MariaDB Client
- wget
- nano
- Composer
- Drush
- Drupal Console
- Xdebug (Remote debugging enabled as default)
- Drupal Devel module
- phpredis

## Distribution supported

See the supported tags above. Please use the respective Docker tags to download the Drupal distribution below:

- [Contenta CMS](https://www.drupal.org/project/contentacms)
- [Lightning](https://www.drupal.org/project/lightning)
- [Reservoir](https://github.com/acquia/reservoir)
- [Thunder](https://www.drupal.org/project/thunder)
- [Varbase](https://www.drupal.org/project/varbase)
- **Drupal Commerce** has its own dedicated [docker image](https://hub.docker.com/r/insready/drupal-commerce/).

## Contributing
You are invited to contribute new features, fixes, or updates, large or small; we are always thrilled to receive pull requests, and do our best to process them as fast as we can.

Before you start to code, we recommend discussing your plans through a [GitHub issue](https://github.com/INsReady/docker-drupal-dev/issues), especially for more ambitious contributions. This gives other contributors a chance to point you in the right direction, give you feedback on your design, and help you find out if someone else is working on the same thing.