Use `ENABLE_XDEBUG` to force image to use `xdebug.remote_connectback` to the IP performing the call.

Use `ENABLE_XDEBUG_FORCEHOST` with `PHP_IDE_CONFIG: "serverName=..."` to force all processes to connect to your host, handy for debugging Behat contexts etc.

```
version: '2'
services:

  php:
    environment:
#       ENABLE_XDEBUG_FORCEHOST: "172.19.0.1"
#       PHP_IDE_CONFIG: "serverName=taenk-php"
#       ENABLE_XDEBUG_PROFILE: "TRUE"
#       ENABLE_XDEBG: "TRUE"
```

