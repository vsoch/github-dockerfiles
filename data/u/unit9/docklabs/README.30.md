# Base image with Python, uWSGI, Node, Ruby, & frontend tools

See [the readme for `unit9/webstack`](/webstack).

The difference in this image is that Node 7.x is used.
# Base image with Python, uWSGI, Node, Ruby, & frontend tools

See the following base images for a full introduction:

- [`unit9/base`](https://github.com/unit9/docklabs/tree/master/base)
- [`unit9/python-uwsgi`](https://github.com/unit9/docklabs/tree/master/python-uwsgi)

This image adds standard frontend build tools.

## Features

- Latest stable releases of Node 4.x, Ruby 2.1
- Frontend development tools: Compass, Gulp, Bower
- Ready to build your frontend apps!

## Using with your `Dockerfile`

Pull `unit9/webstack:latest` and customise this example:

```
FROM unit9/webstack:latest
MAINTAINER You <you@example.com>

# Install backend app requirements
ADD requirements.txt /app
RUN pip install -r ./requirements.txt

# Service definition for runit
ADD run_my_app /etc/service/my_app/run
ENV PORT=5000
EXPOSE 5000

# Install frontend build dependencies via NPM
ADD package.json /app
RUN npm install

# Slurp application code
ADD . /app

# Install frontend build dependencies via bower
RUN bower install --allow-root -q

# Build frontend
RUN gulp

```

Notice that neither `cmd` or `exec` are defined; refer to the
documentation for `unit9/base` for an explanation why.

Inside the file `run_my_app`, there should be a shell script that
reads the environment and sets up the uWSGI service; refer to the
documentation for `unit9/python-uwsgi` for details.

## License

See the file [`LICENSE`](/LICENSE).
# Base image with Python, uWSGI, Node, Ruby, & frontend tools

See [the readme for `unit9/webstack`](/webstack).

The difference in this image is that Node 6.x is used.
