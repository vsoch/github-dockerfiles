# Garden Dockerfiles

Images CF Garden team consumes in testing environments.

* `garden-ci`: Used in the publish pipeline.
* `garden-ci-ubuntu`: Used in most nested tests.
* `golang-ci`: Used in non-nested tests.
* `large_layers`: An image with large layers.
* `ubuntu-bc`: Ubuntu image with `bc` program.
* `with-user-with-group`: Image with a user that has supplementary groups.
* `with-volume`: Image that uses defines a Docker volume.

## Building garden-ci-ubuntu

1) Use the provided makefile:

```
make garden-ci-ubuntu
```

2) Tag the image with the correct version:

```
docker tag cfgarden/garden-ci-ubuntu cfgarden/garden-ci-ubuntu:x.y.z
```

3) Login to Dockerhub

```
docker login
# It will prompt for the Dockerhub credentials that can be found in LastPass
```

4) Push

```
docker push cfgarden/garden-ci-ubuntu:x.y.z
docker push cfgarden/garden-ci-ubuntu:latest
```
