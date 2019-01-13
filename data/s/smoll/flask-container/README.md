# flask-container [![Circle CI](https://circleci.com/gh/smoll/flask-container.svg?style=svg)](https://circleci.com/gh/smoll/flask-container)

Following along with [this](https://realpython.com/blog/python/docker-in-action-fitter-happier-more-productive/) RealPython article...

## Usage

Start flask app and redis db with

```
$ docker-compose up
```

View the site at [http://localhost:5000/](http://localhost:5000/) for docker native / [http://192.168.59.103:5000/](http://192.168.59.103:5000/) for boot2docker

## Rebuilding containers

This is only necessary if you make changes to the [Dockerfile](web/Dockerfile) or [dev Dockerfile](./Dockerfile) (or update [requirements.txt](web/requirements.txt)/[dev-requirements.txt](web/dev-requirements.txt))

```
$ docker-compose build web
$ docker-compose build tests # test container
```

## Tests

Run tests on your dev env with

```
$ docker-compose run tests
```

## Debugging

In order for a `import pdb; pdb.set_trace()` breakpoint to work, start the web container with

```
docker-compose run --service-ports web
```

If you want to set a pdb breakpoint with nosetests (acceptance tests), you can either

0. Start nosetests with [a flag so it does not capture stdout](http://stackoverflow.com/a/4950690/3456726), i.e.

  ```
  $ nosetests tests/acceptance -s # in run_tests.sh
  ```

0. Use the `set_trace` [variant that comes with Nose](http://stackoverflow.com/a/7493906/3456726), i.e.

  ```
  from nose.tools import set_trace; set_trace()
  ```
