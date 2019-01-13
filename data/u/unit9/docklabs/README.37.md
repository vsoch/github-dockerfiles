# HAProxy

This image packages [HAProxy](http://www.haproxy.org/), The Reliable,
High Performance TCP/HTTP Load Balancer. The included version is 1.5,
aka what is
[available in Debian Jessie](https://packages.debian.org/jessie/haproxy).

## Configuring

A file with some sane defaults is included in the image
(`/etc/haproxy/defaults.cfg`).

You should mount a volume with configuration snippets, in the form of
`*.cfg` files, per [HAProxy's config format][haproxy-config-manual],
at `/etc/haproxy/conf.d`. (Subdirectories will not be scanned.)

[haproxy-config-manual]: https://cbonte.github.io/haproxy-dconv/1.5/configuration.html

The files will be sorted by name and concatenated together, then
dumped into `/etc/haproxy/haproxy.cfg`.

By default, the container will expose ports 80 and 443, but HAProxy is
not configured to bind any listening sockets.

If you use `make run`, the contents of `conf.d` in this directory will
be mounted, exposing the stats interface on <http://localhost:8080>.
