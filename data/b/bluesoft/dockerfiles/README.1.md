## Build Apache2 with HTTP/2 support

This repository contains a Dockerfile that compiles the Apache 2.4.17 stable release with support for HTTP/2 enabled. We also provide samples for httpd.conf and httpd-vhost.conf.
The build we do in this Dockerfile will work for a single static website. You may need to change some ```configure``` options according to your needs.

To make the Docker build, you may clone this repository and run the Docker commands as follows.

```
$ git clone git@github.com:bluesoft/dockerfiles.git
$ cd httpd-h2
$ docker build -t httpd-h2 .
$ docker run -d -p 8443:443 -v /path/to/my/website/:/usr/local/httpd/htdocs/ httpd-h2
```

Or you may just pull the image from Dockerhub.

```
$ docker pull bluesoftbr/httpd-h2
$ docker run -d -p 8443:443 -v /path/to/my/website/:/usr/local/httpd/htdocs/ httpd-h2
```

Change ```/path/to/my/website/``` to the absolute path to your website.

Access ```https://localhost:8443/``` through your browser and have fun!

## Important

For more information on the options to configure HTTP/2 in Apache, [please visit their documentation].
Apache 2.4.17 was released 2015-10-13 as a stable release. [Take a look at the Announcement].

[//]: #
[please visit their documentation]: <http://httpd.apache.org/docs/2.4/mod/mod_http2.html>
[Take a look at the Announcement]: <http://www.apache.org/dist/httpd/Announcement2.4.html>

