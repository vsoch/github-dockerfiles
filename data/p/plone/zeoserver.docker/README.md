# zeoserver.docker

ZEO Server [Docker](http://docker.com) image based on [plone.recipe.zeoserver](https://pypi.python.org/pypi/plone.recipe.zeoserver)

## Supported tags and respective Dockerfile links

- `2.13.23, 2.13, 2, latest` [(2.13/debian/Dockerfile)](https://github.com/plone/zeoserver.docker/blob/master/2.13.23/debian/Dockerfile)
- `2.13.23-alpine, 2.13-alpine, 2-alpine` [(2.13/alpine/Dockerfile)](https://github.com/plone/zeoserver.docker/blob/master/2.13.23/alpine/Dockerfile)

## Base docker image

 - [hub.docker.com](https://registry.hub.docker.com/u/plone/zeoserver)

## Source code

  - [github.com](http://github.com/plone/plone.zeoserver)

### Supported Environment Variables

* `HEALTH_CHECK_TIMEOUT` - Time in seconds to wait until health check starts. Defaults to `1` second.
* `HEALTH_CHECK_INTERVAL` - Interval in seconds to check that the ZEO application is still healthy. Defaults to `1` second.

## Documentation

You can find all the documentation in the [docs](https://github.com/plone/zeoserver.docker/blob/master/docs)


## Contribute

- [Issue Tracker](https://github.com/plone/zeoserver.docker/issues)
- [Source Code](https://github.com/plone/zeoserver.docker/)
- [Documentation](https://github.com/plone/zeoserver.docker/tree/master/docs)

Please **DO NOT** commit to master directly. Even for the smallest and most trivial fix.
**ALWAYS** open a pull request and ask somebody else to merge your code. **NEVER** merge it yourself.


## License

The project is licensed under the GPLv2.
