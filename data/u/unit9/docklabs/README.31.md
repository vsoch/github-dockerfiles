# Base image with runit-based service supervision

The image builds upon the latest
[Debian Jessie](https://hub.docker.com/_/debian/), and adds a thin
init + service supervision layer.

The purpose is mostly for internal use at
[UNIT9](http://www.unit9.com/), but there's nothing bundled that makes
it UNIT9-specific.

PID 1 duties (spawn [runit][], reap zombies) are handled with
[a simple Go program](https://github.com/peterbourgon/runsvinit)
written by Peter Bourgon and hosted on Github,
[license MIT](https://github.com/peterbourgon/runsvinit/blob/master/LICENSE).

Service supervision is handled with [runit][].

Programs that insist on logging to [syslog][] are handled with
[socklog][].

Source on Github: <https://github.com/unit9/docklabs>

[runit]: http://smarden.org/runit/
[socklog]: http://smarden.org/socklog/
[syslog]: https://en.wikipedia.org/wiki/syslog

## Features and non-features

- Lean, for small and fast downloads! Includes only what's absolutely
  essential on top of `debian:jessie`;
- `Makefile` for easy builds and uploads:
    - `make build` to build
    - `make push` to push to Docker Hub
    - `make shell` gives you a shell in the (ephemeral) container
- Support for `/etc/rc.local` to initialise & self-check the container

## Using with your `Dockerfile`

Pull `unit9/base:latest` and customise this example:

```
FROM unit9/base:latest
MAINTAINER You <you@example.com>

RUN apt-get update && \
    apt-get install --yes my-favourite-stuff && \
    rm -rf /var/cache/apt /var/lib/apt/lists

ADD run_my_stuff /etc/service/run_my_stuff/run
ADD rc.local /etc/rc.local

VOLUME /data/run_my_stuff
EXPOSE 1234
```

Notice that neither `cmd` or `exec` are defined; this is the role that
`runit` takes.

Inside the file `run_my_stuff`, there should be a shell script that
reads the environment and sets up the service. For example:

```
#!/bin/sh
set -eu

echo $UPSTREAM_PORT | sed -E 's#tcp://(.+):(.+)#\1 \2#' | {
    read host port
    echo >&2 host=$host port=$port

    cat > /etc/my_stuff.conf <<EOF
name my_stuff
host $host
port $port
EOF
    }

echo >&2 "Starting my stuff"
exec /usr/bin/my-stuff --config /etc/my_stuff.conf
```

Inside of `rc.local`, is another simple shell script, which can
perform any one-off initialisation tasks or self-checks:

```
#!/bin/sh
set -eux
test -f /var/www/html/index.html
lighttpd -t -f /etc/lighttpd/lighttpd.conf
exit 0
```

Make sure the script returns a non-zero code on an error. Your
container will exit upon failure - this is useful to e.g. stop a bad
deployment before the rolling update brings everything down.

## License

See the file [`LICENSE`](/LICENSE).
