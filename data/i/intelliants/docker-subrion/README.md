# What is Subrion?

Subrion is a **free open source content management system**
that allows you to build websites for any purpose. Yes, from blog to corporate mega portal.

## How to use this image

Start up a MySQL container.

```console
$ docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=secretpass -d mysql
```

For more information on MySQL containers, please refer to [this](https://hub.docker.com/_/mysql/).
Then run:

```console
$ docker run --name some-subrion —-link some-mysql:mysql -d intelliants/subrion
```

The following environment variables are also honored for configuring your Subrion instance:

* `-e SUBRION_DB_HOST=…` (defaults to the IP and port of the linked `mysql` container)
* `-e SUBRION_DB_USER=…` (defaults to "root")
* `-e SUBRION_DB_PASSWORD=…` (defaults to the value of the `MYSQL_ROOT_PASSWORD` environment variable from the linked `mysql` container)
* `-e SUBRION_DB_NAME=…` (defaults to "subrion")

If the `SUBRION_DB_NAME` specified does not already exist on the given MySQL server, it will be created automatically upon startup of the `subrion`container, provided that the `SUBRION_DB_USER` specified has the necessary permissions to create it.

```console
$ docker run --name some-subrion --link some-mysql:mysql -p 8080:80 -d intelliants/subrion
```
The -p argument is used for port mapping. Inside the container, Apache runs on port 80. We tell Docker that we’ll use the port 8080 to communicate with the port 80 inside the container.   

If you'd like to use an external database instead of a linked `mysql`container, specify the hostname and port with `SUBRION_DB_HOST` along with the password in `SUBRION_DB_PASSWORD` and the username in `SUBRION_DB_USER` (if it is something other than `root`):

```console
$ docker run --name some-subrion -e SUBRION_DB_HOST=10.1.2.3:3306 \ 
    -e SUBRION_DB_USER=... -e SUBRION_DB_PASSWORD=... -d intelliants/subrion
```
The problem with this example is that we can't access the Subrion files easily, also each time we start the container, it will change its IP. But we can easily fix both of these issues.

```console
$ docker run -d --name some-subrion --link some-mysql:mysql -p 127.0.0.2:8080:80 -v "$PWD/":/var/www/html intelliants/subrion
```
We specified 127.0.0.2 as the IP for this container to avoid dynamic IP. -v "$PWD/":/var/www/html will map the two folders. By default, the container puts the Subrion files in the /var/www/html directory which is the filesystem inside the container (this is nothing to do with our local filesystem).
Check out your current directory and you'll see that some additional files are there. So we recommended to run the command above in a dedicated empty directory, let it be `subrion`.

If you're on Linux, you should change the permissions of the Subrion folder (the local folder) to writable. That's because the containers are created by the Docker daemon, a process that starts when the system boots (by the sudo user). To fix this execute:

```console
$ sudo chmod -R 777 subrion
```

You'll now have write access to these folders and you'll be good to go!

## … via docker-compose

Example `docker-compose.yml` for `subrion`:

```yaml
version: '2'

services:
  subrion:
    image: intelliants/subrion
    links: 
      - subriondb:mysql
    ports:
      - 8080:80
    environment:
      SUBRION_DB_PASSWORD: secretpass

  subriondb:
    image: mysql:5.6
    environment:
      MYSQL_ROOT_PASSWORD: secretpass
```

Run `docker-compose up`, wait for it to initialize completely, and visit `http://localhost:8080` or `http://host-ip:8080`.

## Adding additional libraries / extensions

This image does not provide any additional PHP extensions or other libraries, even if they are required by popular plugins. There are an infinite number of possible plugins, and they potentially require any extension PHP supports. Including every PHP extension that exists would dramatically increase the image size.

If you need additional PHP extensions, you'll need to create your own image `FROM` this one. The [documentation of the `php` image](https://github.com/docker-library/docs/blob/master/php/README.md#how-to-install-more-php-extensions) explains how to compile additional extensions.

The following Docker Hub features can help with the task of keeping your dependent images up-to-date:

- [Automated Builds](https://docs.docker.com/docker-hub/builds/) let Docker Hub automatically build your Dockerfile each time you push changes to it.
- [Repository Links](https://docs.docker.com/docker-hub/builds/#repository-links) can ensure that your image is also rebuilt any time `subrion` is updated.
