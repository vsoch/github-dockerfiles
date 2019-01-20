infoboard
=========

A rotaterscript for our infoboards shown on the big screen tv on the
wall

## File permissions

In order for the admin script to save the configuration, the web
server user needs write permission to the `config.yml` file.

## Docker container

To persist the configuration across container restarts, mount in the
config.yml file:

``` shell
docker run -v $PWD/config.yml:/srv/config.yml infoboard:latest
```
