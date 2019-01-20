# Camptocamp WSGI utilities

| branch  | CI  | requirements  | static analysis |
|---|---|---|---|
| master | [![Build master](https://ci.camptocamp.com/buildStatus/icon?job=geospatial/c2cwsgiutils/master)](https://ci.camptocamp.com/job/geospatial/job/c2cwsgiutils/job/master/) | [![Requirements master](https://requires.io/github/camptocamp/c2cwsgiutils/requirements.svg?branch=master)](https://requires.io/github/camptocamp/c2cwsgiutils/requirements/?branch=master) | [![Codacy Badge](https://api.codacy.com/project/badge/Grade/c47d09a059ca410cbc325f94d7993518)](https://www.codacy.com/app/camptocamp/c2cwsgiutils?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=camptocamp/c2cwsgiutils&amp;utm_campaign=Badge_Grade) |
| release_2 | [![Build release_1](https://ci.camptocamp.com/buildStatus/icon?job=geospatial/c2cwsgiutils/release_2)](https://ci.camptocamp.com/job/geospatial/job/c2cwsgiutils/job/release_2/) | [![Requirements release_2](https://requires.io/github/camptocamp/c2cwsgiutils/requirements.svg?branch=release_2)](https://requires.io/github/camptocamp/c2cwsgiutils/requirements/?branch=release_2) | |
| release_1 (deprecated) | [![Build release_1](https://ci.camptocamp.com/buildStatus/icon?job=geospatial/c2cwsgiutils/release_1)](https://ci.camptocamp.com/job/geospatial/job/c2cwsgiutils/job/release_1/) | [![Requirements release_1](https://requires.io/github/camptocamp/c2cwsgiutils/requirements.svg?branch=release_1)](https://requires.io/github/camptocamp/c2cwsgiutils/requirements/?branch=release_1) | |

This is a Python 3 library (>=3.5) providing common tools for Camptocamp WSGI
applications:

* Provide a small framework for gathering performance statistics about
  a web application (statsd protocol)
* Allow to use a master/slave PostgresQL configuration
* Logging handler for CEE/UDP logs
  * An optional view to change runtime the log levels
* SQL profiler to debug DB performance problems, disabled by default. Warning, it will slow down everything.
* A view to get the version information about the application and the installed packages
* A framework for implementing a health_check service
* Error handlers to send JSON messages to the client in case of error
* A cornice service drop in replacement for setting up CORS

Also provide tools for writing acceptance tests:

* A class that can be used from a py.test fixture to control a
  composition
* A class that can be used from a py.text fixture to test a REST API

As an example on how to use it in an application provided by a Docker image, you can look at the
test application in [acceptance_tests/app](acceptance_tests/app).
To see how to test such an application, look at [acceptance_tests/tests](acceptance_tests/tests).


## Install

The library is available in PYPI:
[https://pypi.python.org/pypi/c2cwsgiutils](https://pypi.python.org/pypi/c2cwsgiutils)

With pip:
```
pip install c2cwsgiutils
```

Or (preferred) as a base Docker image:
[camptocamp/c2cwsgiutils:2](https://hub.docker.com/r/camptocamp/c2cwsgiutils/)

If you need an image with a smaller foot print, use the tags prefixed with `-light`. Those are without
gdal and without the build tools.


## General config

In general, configuration can be done both with environment variables (taken first) or with entries in the
`production.ini` file.

You can configure the base URL for accessing the views provided by c2cwsgiutils with an environment variable
named `C2C_BASE_PATH` or in the `production.ini` file with a property named `c2c.base_path`.

A few REST APIs are added and can be seen with this URL (only enabled if C2C_BASE_PATH is not empty):
`{C2C_BASE_PATH}`.

Some APIs are protected by a secret. This secret is specified in the `C2C_SECRET` variable or `c2c.secret`
property. It is either passed as the `secret` query parameter or the `X-API-Key` header.


## Pyramid

A command line (`c2cwsgiutils_run`) is provided to start an HTTP server (gunicorn) with a WSGI application.
By default, it will load the application configured in `/app/production.ini`, but you can change that with
the `C2CWSGIUTILS_CONFIG` environment variable. All the environment variables are usable in the configuration
file using stuff like `%(ENV_NAME)s`.

To enable most of the features of c2cwsgiutils, you need to add this line to you WSGI main:

```python
import c2cwsgiutils.pyramid
config.include(c2cwsgiutils.pyramid.includeme)
```

Error catching views will be put in place to return errors as JSON.


## Logging

Two new logging backends are provided:

* `c2cwsgiutils.pyramid_logging.PyramidCeeSysLogHandler`: to send @cee formatted logs to syslog through UDP.
* `c2cwsgiutils.pyramid_logging.JsonLogHandler`: to output (on stdout or stderr) JSON formatted logs.

Look at the logging configuration part of
[acceptance_tests/app/production.ini](acceptance_tests/app/production.ini) for a usage example.

You can enable a view to configure the logging level on a live system using the `C2C_LOG_VIEW_ENABLED` environment
variable. Then, the current status of a logger can be queried with a GET on
`{C2C_BASE_PATH}/logging/level?secret={C2C_SECRET}&name={logger_name}` and can be changed with
`{C2C_BASE_PATH}/logging/level?secret={C2C_SECRET}&name={logger_name}&level={level}`. Overrides are stored in
Redis, if `C2C_REDIS_URL` (`c2c.redis_url`) is configured.


### Request tracking

In order to follow the logs generated by a request across all the services (think separate processes),
c2cwsgiutils tries to flag averything with a request ID. This field can come from the input as request headers
(`X-Request-ID`, `X-Correlation-ID`, `Request-ID` or `X-Varnish`) or will default to a UUID. You can add an
additional request header as source for that by defining the `C2C_REQUEST_ID_HEADER` environment variable
(`c2c.request_id_header`).

In JSON logging formats, a `request_id` field is automatically added.

You can enable (disabled by default since it can have a cost) the flagging of the SQL requests as well by
setting the C2C_SQL_REQUEST_ID environment variable (or c2c.sql_request_id in the .ini file). This will use
the application name to pass along the request id. If you do that, you must include the application name in
the PostgreSQL logs by setting `log_line_prefix` to something like `"%a "` (don't forget the space).

Then, in your application, it is recommended to transmit the request ID to the external REST APIs. Use
the `X-Request-ID` HTTP header, for example. The value of the request ID is accessible through an added
`c2c_request_id` attribute on the Pyramid Request objects. The `requests` module is patched to automatically
add this header.

The requests module is also patched to monitor requests done without timeout. In that case, you can
configure a default timeout with the `C2C_REQUESTS_DEFAULT_TIMEOUT` environment variable
(`c2c.requests_default_timeout`). If no timeout and no default is specified, a warning is issued.


## Metrics

To enable and configure the metrics framework, you can use:

* STATS_VIEW (c2c.stats_view): if defined, will enable the stats view `{C2C_BASE_PATH}/stats.json`
* STATSD_ADDRESS (c2c.statsd_address): if defined, send stats to the given statsd server
* STATSD_PREFIX (c2c.statsd_prefix): prefix to add to every metric names
* STATSD_USE_TAGS: If true, automatic metrics will use tags

If enabled, some metrics are automatically generated:

* {STATSD_PREFIX}.route.{verb}.{route_name}.{status}: The time to process a query (includes rendering)
* {STATSD_PREFIX}.render.{verb}.{route_name}.{status}: The time to render a query
* {STATSD_PREFIX}.sql.{query}: The time to execute the given SQL query (simplified and normalized)
* {STATSD_PREFIX}.requests.{scheme}.{hostname}.{port}.{verb}.{status}: The time to execute HTTP requests to
   outside services (only the time between the start of sending of the request and when the header is
   back with a chunk of the body)
* {STATSD_PREFIX}.redis.{command}: The time to execute the given Redis command

You can manually measure the time spent on something like that:

```python
from c2cwsgiutils import stats
with stats.timer_context(['toto', 'tutu']):
    do_something()
```

It will only add a timer event in case of success. If you want to measure both success and failures, do that:

```python
from c2cwsgiutils import stats
with stats.outcome_timer_context(['toto', 'tutu']):
    do_something()
```

Other functions exists to generate metrics. Look at the `c2cwsgiutils.stats` module.

Look at the `c2cwsgiutils_stats_db.py` utility if you want to generate statistics (gauges) about the
row counts.


## SQL profiler

The SQL profiler must be configured with the `C2C_SQL_PROFILER_ENABLED` environment variable. That enables a view
to query the status of the profiler (`{C2C_BASE_PATH}/sql_profiler?secret={C2C_SECRET}`) or to
enable/disable it (`{C2C_BASE_PATH}/sql_profiler?secret={C2C_SECRET}&enable={1|0}`).

If enabled, for each `SELECT` query sent by SQLAlchemy, another query it done with `EXPLAIN ANALYZE`
prepended to it. The results are sent to the `c2cwsgiutils.sql_profiler` logger.

Don't enable that on a busy production system. It will kill your performances.


## Profiler

If you set the `C2C_PROFILER_PATH` environment variable, you'll enable a profiler that will be available at
the given path. Due to limitations in the library used, the path must be at the root of the application (it
cannot contain slashes). You can also define the `C2C_PROFILER_MODULES`, a space separated list of Python
packages to have a pie chart of how much time is spent in the given packages.

The profiler, even if configured, is actually disabled when the application starts. To enable it you must
visit its page.

If you want to use this feature, you must have the `linesman` package installed.


## DB sessions

The `c2cwsgiutils.db.setup_session` allows you to setup a DB session that has two engines for accessing a
master/slave PostgresQL setup. The slave engine (read only) will be used automatically for `GET` and `OPTIONS`
requests and the master engine (read write) will be used for the other queries.

To use that, your production.ini must look like that:

```ini
sqlalchemy.url = %(SQLALCHEMY_URL)s
sqlalchemy.pool_recycle = 30
sqlalchemy.pool_size = 5
sqlalchemy.max_overflow = 25

sqlalchemy_slave.url = %(SQLALCHEMY_URL_SLAVE)s
sqlalchemy_slave.pool_recycle = 30
sqlalchemy_slave.pool_size = 5
sqlalchemy_slave.max_overflow = 25
```

And your code that initializes the DB connection must look like that:

```python
from c2cwsgiutils.db import setup_session
def init(config):
    global DBSession
    DBSession = setup_session(config, 'sqlalchemy', 'sqlalchemy_slave', force_slave=[
        "POST /api/hello"
    ])[0]
```

You can use the `force_slave` and `force_master` parameters to override the defaults and force a route to use
the master or the slave engine.


## Health checks

To enable health checks, you must add some setup in your WSGI main (usually after the DB connections are
setup). For example:

```python
from c2cwsgiutils.health_check import HealthCheck

def custom_check(request):
    global not_happy
    if not_happy:
        raise Exception("I'm not happy")
    return "happy"

health_check = HealthCheck(config)
health_check.add_db_session_check(models.DBSession, at_least_one_model=models.Hello)
health_check.add_url_check('http://localhost:8080/api/hello')
health_check.add_custom_check('custom', custom_check, 2)
health_check.add_alembic_check(models.DBSession, '/app/alembic.ini', 3)
```

Then, the URL `{C2C_BASE_PATH}/health_check?max_level=3` can be used to run the health checks and get a report
looking like that (in case of error):

```json
{
    "status": 500,
    "successes": {
        "db_engine_sqlalchemy": {"timing": 0.002},
        "db_engine_sqlalchemy_slave": {"timing": 0.003},
        "http://localhost/api/hello": {"timing": 0.010},
        "alembic_app_alembic.ini_alembic": {"timing": 0.005, "result": "4a8c1bb4e775"}
    },
    "failures": {
        "custom": {
            "message": "I'm not happy",
            "timing": 0.001
        }
    }
}
```

The levels are:

* 0: Don't add checks at this level. This max_level is used for doing a simple ping.
* 1: Checks for anything vital for the usefulness of the service (DB, redis, ...). This is the max_level set
     by default and used by load balancers to determine if the service is alive.
* \>=2: Use those at your convenience. Pingdom and CO are usually setup at max_level=100. So stay below.

When you instanciate the `HealthCheck` class, two checks may be automatically enabled:

* If redis is configured, check that redis is reachable.
* If redis is configured and the version information is available, check that the version matches
  accross all instances.

Look at the documentation of the `c2cwsgiutils.health_check.HealthCheck` class for more information.


## SQLAlchemy models graph

A command is provided that can generate Doxygen graphs of an SQLAlchemy ORM model.
See [acceptance_tests/app/models_graph.py](acceptance_tests/app/models_graph.py) how it's used.


## Version information

If the `/app/versions.json` exists, a view is added (`{C2C_BASE_PATH}/versions.json`) to query the current
version of a app. This file is generated by calling the `c2cwsgiutils_genversion.py [$GIT_TAG] $GIT_HASH`
command line. Usually done in the [Dockerfile](acceptance_tests/app/Dockerfile) of the WSGI application.


## Debugging

To enable the debugging interface, you must set the `C2C_DEBUG_VIEW_ENABLED` environment variable. Then you can
have dumps of a few things:

* every threads' stacktrace: `{C2C_BASE_PATH}/debug/stacks?secret={C2C_SECRET}`
* memory usage: `{C2C_BASE_PATH}/debug/memory?secret={C2C_SECRET}&limit=30`
* memory increase when calling another API: `{C2C_BASE_PATH}/debug/memory_diff?path={path_info}&secret={C2C_SECRET}&limit=30`
* sleep the given number of seconds (to test load balancer timeouts): `{C2C_BASE_PATH}/debug/sleep?secret={C2C_SECRET}&time=60.2`
* see the HTTP headers received by WSGI: `{C2C_BASE_PATH}/debug/headers?secret={C2C_SECRET}`
* return an HTTP error: `{C2C_BASE_PATH}/debug/error?secret={C2C_SECRET}&status=500`

It is possible to automatically reload gunicorn as soon as you change your local python code. For this you need
to have a specially tweaked `docker-compose.yml`:
```yml
services:
  api:
    environment:
      GUNICORN_PARAMS: '-b :80 --threads 10 --timeout 60 --reload'
  volumes:
    - ./api/somepath:/app/somepath:ro
```
The GUNICORN\_PARAMS has the `--reload` parameter and your local python code is
mounted (read only) into the container.


### Broadcast

Some c2cwsgiutils APIs effect or query the state of the WSGI server. Since only one process out of the 5
(by default) time the number of servers gets a query, only this one will be affected. To avoid that, you
can configure c2cwsgiutils to use Redis pub/sub to broadcast those requests and collect the answers.

The impacted APIs are:

* `{C2C_BASE_PATH}/debug/stacks`
* `{C2C_BASE_PATH}/debug/memory`
* `{C2C_BASE_PATH}/logging/level`
* `{C2C_BASE_PATH}/sql_profiler`

The configuration parameters are:

* `C2C_REDIS_URL` (`c2c.redis_url`): The URL to the Redis instance to use
* `C2C_BROADCAST_PREFIX` (`c2c.broadcast_prefix`): The prefix to add to the channels being used (must be
  different for 2 different services)

If not configured, only the process receiving the request is impacted.


## CORS

To have CORS compliant views, define your views like that:

```python
from c2cwsgiutils import services
hello_service = services.create("hello", "/hello", cors_credentials=True)

@hello_service.get()
def hello_get(request):
    return {'hello': True}
```


# Exception handling

By default, c2cwsgiutils will install exception handling views that will catch any exception raised by the
application views and will transform it into a JSON response with a HTTP status corresponding to the error.

You can disable this by setting `C2C_DISABLE_EXCEPTION_HANDLING` (`c2c.disable_exception_handling`) to "1".

In development mode (`DEVELOPMENT=1`), all the details (SQL statement, stacktrace, ...) are sent to the
client. In production mode, you can still get them by sending the secret defined in `C2C_SECRET` in the query.

If you want to use pyramid_debugtoolbar, you need to disable exception handling and configure it like that:
```
pyramid.includes =
    pyramid_debugtoolbar
debugtoolbar.enabled = true
debugtoolbar.hosts = 0.0.0.0/0
debugtoolbar.intercept_exc = debug
debugtoolbar.show_on_exc_only = true
c2c.disable_exception_handling = 1
```


# JSON pretty print

Two JSON renderers are available:

* `json`: the normal JSON renderer (default)
* `fast_json`: a faster JSON renderer
is tuned differently.

Both pretty prints the rendered JSON. While this adds significant amount of whitespace, the difference in
bytes transmitted on the network is negligible thanks to gzip compression.

The `fast_json` renderer is using ujson which is faster, but doesn't offer the ability to change the rendering
of some types (the `default` parameter of json.dumps). This will interact badly with `papyrus` and such.


## Sentry integration

The stacktraces can be sent to a sentry.io service for collection. To enable it, you must set the `SENTRY_URL`
(`c2c.sentry_url`) to point the the project's public DSN.

A few other environment variables can be used to tune the info sent with each report:

* `SENTRY_EXCLUDES` (`c2c.sentry.excludes`): list of loggers (colon separated, without spaces) to exclude for sentry
* `GIT_HASH` (`c2c.git_hash`): will be used for the release
* `SENTRY_CLIENT_RELEASE`: If not equal to "latest", will be taken for the release instead of the GIT_HASH
* `SENTRY_CLIENT_ENVIRONMENT`: the environment (dev, int, prod, ...)
* `SENTRY_CLIENT_IGNORE_EXCEPTIONS`: list (coma separated) of exceptions to ignore (defaults to SystemExit)
* `SENTRY_TAG_...`: to add other custom tags
* `SENTRY_LEVEL`: starting from what logging level to send events to Sentry (defaults to ERROR)


# Developer info

You will need `docker` (>=1.12.0), `docker-compose` (>=1.10.0) and
`make` installed on the machine to play with this project.
Check available versions of `docker-engine` with
`apt-get policy docker-engine` and eventually force install the
up-to-date version using a command similar to
`apt-get install docker-engine=1.12.3-0~xenial`.

To lint and test everything, run the following command:

```shell
make
```

Make sure you are strict with the version numbers:

* bug fix version change: Nothing added, removed or changed in the API and only bug fix
  version number changes in the dependencies
* minor version change: The API must remain backward compatible and only minor version
  number changes in the dependencies
* major version change: The API and the dependencies are not backward compatible

To make a release:

* Change the the version in [setup.py](setup.py).
* Commit and push to master.
* Tag the GIT commit.
* Rebase the `release_${MAJOR_VERSION}` branch to this commit and push the `release_${MAJOR_VERSION}` and
  the tag to github. Make sure to do that at the same time so that Jenkins can see the tag when it builds
  the branch.

We need the `release_${MAJOR_VERSION}` branch, so that Jenkins can build a new docker image for the major
versions every nights.
