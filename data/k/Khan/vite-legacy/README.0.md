# build docker image

From the root directory of this repo, run:
- docker build -t vite -f docker/Dockerfile .

# run docker

From the root directory of the repo being tested, run:
- docker run -v `pwd`:/home/under_test vite

Note: `under_test` must be that exact string.

TODO: add a script to package.json to run the docker.
TODO: publish the docker image to docker hub.
