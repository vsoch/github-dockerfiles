# docker-sdr

A docker-compose project for launching the DLSS SDR ecosystem.

## Running

```
$ docker-compose build
# initialize databases, solr collections, etc
$ ./setup.sh
# launching the whole ecosystem:
$ docker-compose up
# or launching only some components
# $ docker-compose up stacks
```

## Viewing applications

By default, we use the `localtest.me` to generate local hostnames (set as `VIRTUAL_HOST_BASE` in `.env`). Applications are exposed as subdomains of the host, e.g.:

- http://stacks.localtest.me
- http://argo.localtest.me
- http://suri.localtest.me
- etc
