## Build Nginx with HTTP/2 support

This repository contains a Dockerfile that compiles an Nginx installation with support for HTTP/2 enabled. We also provide a sample nginx.conf.
The build we do in this Dockerfile will work for a single static website. You may need to change some ```configure``` options according to your needs.

To make the Docker build, you may clone this repository and run the Docker commands as follows.

```
$ git clone git@github.com:bluesoft/dockerfiles.git
$ cd nginx-h2
$ docker build -t nginx-h2 .
$ docker run -d -p 8443:443 -v /path/to/my/website/:/usr/local/nginx/html/ nginx-h2
```

Or you may just pull the image from Dockerhub.

```
$ docker pull bluesoftbr/nginx-h2
$ docker run -d -p 8443:443 -v /path/to/my/website/:/usr/local/nginx/html/ nginx-h2
```

Change ```/path/to/my/website/``` to the absolute path to your website.

Access ```https://localhost:8443/``` through your browser and have fun!

## Important

For more information on the options to configure HTTP/2 in Nginx, [please visit their documentation].
Nginx 1.9.5 was released 2015-09-22 as a stable release. [Take a look at the Announcement].

[//]: #
[please visit their documentation]: <http://nginx.org/en/docs/http/ngx_http_v2_module.html>
[Take a look at the Announcement]: <https://www.nginx.com/blog/nginx-1-9-5/>

