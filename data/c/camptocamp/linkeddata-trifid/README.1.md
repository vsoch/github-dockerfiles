# Content replacing proxy for geoadmin-trifid

This provides a docker image providing an HTTP proxy rewriting request and 
content to allow acessing the geoadmin-trifid instance from a host other than 
`https://ld.geo.admin.ch/`.

## Building

    docker build --no-cache -t geoadmin-trifid-proxy .

## Running

The following launches the proxy and exposes its port as `8888` on the host:

    docker run --rm -ti -p 8888:3000 geoadmin-trifid-proxy

With the default configuration this assumes geoadmin-trifid is accessible
to the proxy at `http://geotrifid:8080/`, i.e `geotrifid`should be the name
of the trifid-container in the docker-compose or Rancher Stack.