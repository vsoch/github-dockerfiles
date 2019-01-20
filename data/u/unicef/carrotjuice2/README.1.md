This repository builds a base image with PhantomJS + other deps, such that
systems which don't cache un-tagged Docker images well are still reasonably
fast (for `make phantomjs-tests`).

Build it with

	docker build -t gatoatigrado/carrotjuice-test-base:v0.1 .

and push it to DockerHub with,

	docker push gatoatigrado/carrotjuice-test-base:v0.1

You may occasionally want to refresh package.json and bump the version number
and stuff, but the base docker image re-runs `npm install`, so hopefully you
don't have to do that often. Sorry we have so many packages.
