[![dockeri.co](http://dockeri.co/image/bandsintown/fluentd)](https://hub.docker.com/r/bandsintown/fluentd/)

[![Build status](https://badge.buildkite.com/f78e045c0b561ba33f80f3c996ccfe89b49ade24b832f92bfd.svg)](https://buildkite.com/bandsintown/docker-fluentd)
[![GitHub issues](https://img.shields.io/github/issues/bandsintown/docker-fluentd.svg "GitHub issues")](https://github.com/bandsintown/docker-fluentd)
[![GitHub stars](https://img.shields.io/github/stars/bandsintown/docker-fluentd.svg "GitHub stars")](https://github.com/bandsintown/docker-fluentd)
[![Docker layers](https://images.microbadger.com/badges/image/bandsintown/fluentd.svg)](http://microbadger.com/images/bandsintown/fluentd)
	
# What is Fluentd?

Fluentd is an open source data collector, which lets you unify the data
collection and consumption for a better use and understanding of data.

> [www.fluentd.org](http://www.fluentd.org/)

![Fluentd Logo](http://www.fluentd.org/assets/img/miscellany/fluentd-logo.png)


# How to use this image

To create endpoint that collects logs on your host just run:

```bash
docker run -d -p 24224:24224 -v /data:/var/log/fluentd bandsintown/fluentd
```

Default configurations are to:

- listen port `24224` for Fluentd forward protocol
- store logs with tag `docker.**` into `/var/log/fluentd/docker.*.log`
  (and symlink `docker.log`)
- store all other logs into `/var/log/fluentd/log/data.*.log` (and symlink `data.log`)



## Environment Variables

Environment variable below are configurable to control how to execute fluentd process:


### `FLUENTD_CONF`

This variable allows you to specify configuration file name that will be used
in `-c` Fluentd command line option.

If you want to use your own configuration file (without any optional plugins),
you can do it with this environment variable and Docker volumes (`-v` option
of `docker run`).

1. Write configuration file with filename `yours.conf`.
2. Execute `docker run` with `-v /path/to/dir:/fluentd/etc`
   to share `/path/to/dir/yours.conf` in container,
   and `-e FLUENTD_CONF=yours.conf` to read it.


### `FLUENTD_OPT`

Use this variable to specify other Fluentd command line options,
like `-v` or `-q`.

# Build

This project is configured as an [automated build in Dockerhub](https://hub.docker.com/r/bandsintown/fluentd/).

# License

All the code contained in this repository, unless explicitly stated, is
licensed under ISC license.

A copy of the license can be found inside the [LICENSE](LICENSE) file.