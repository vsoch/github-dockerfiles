# Base image with Python & uWSGI

See [`unit9/base`](https://github.com/unit9/docklabs/tree/master/base)
for an introduction.

## Features

- Latest, patched Python 2.7, as found in Debian Jessie
- uWSGI installed, to run your Python web app

## Using with your `Dockerfile`

Pull `unit9/python-uwsgi:latest` and customise this example:

```
from unit9/python-uwsgi:latest
maintainer You <you@example.com>

# Install backend app requirements
add requirements.txt /app
run pip install -r ./requirements.txt

# Service definition for runit
add run_my_app /etc/service/my_app/run
env PORT=5000
expose 5000

# Add the rest of app code
add . /app

```

Notice that neither `cmd` or `exec` are defined; the `unit9/base`
image has a simple init system that runs services, as defined in
`/etc/service/*/run`; see [runit][] for details.

[runit]: http://smarden.org/runit/

Inside the file `run_my_app`, there should be a shell script that
reads the environment and sets up the uWSGI service. For example:

```
#!/bin/sh
set -eu
export DEBUG=${DEBUG:-0}
cd /app
exec chpst -u app   \
     uwsgi_python27 \
     --master       \
     --http-socket :$PORT              \
     --processes ${UWSGI_PROCESSES:-2} \
     --threads ${UWSGI_THREADS:-32}    \
     --module backend \
     --callable app
```

Note that your uWSGI process should be running as the user `app`! This
is not a strict requirement, but it's good for security. The user
already exists in this image.

## License

See the file [`LICENSE`](/LICENSE).
