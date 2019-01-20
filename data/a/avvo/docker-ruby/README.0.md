# Rails image for production

Built for production, uses Alpine

```
docker build -f Dockerfile -t avvo/ruby-rails:latest .
docker push avvo/ruby-rails:latest
```

Versions:
 * v1.1: Set bundler to 1.15
# Ruby Ubuntu images

Built for CI

```
docker build -f Dockerfile.ubuntu-base -t avvo/ubuntu-base:latest .
docker push avvo/ubuntu-base:latest
docker build -f Dockerfile.2.2.6 -t avvo/ruby-ubuntu:2.2.6 .
docker push avvo/ruby-ubuntu:2.2.6
docker build -f Dockerfile.2.2.7 -t avvo/ruby-ubuntu:2.2.7 -t avvo/ruby-ubuntu:2.2 .
docker push avvo/ruby-ubuntu:2.2.7
docker push avvo/ruby-ubuntu:2.2
docker build -f Dockerfile.2.3.4 -t avvo/ruby-ubuntu:2.3.4 -t avvo/ruby-ubuntu:2.3 .
docker push avvo/ruby-ubuntu:2.3.4
docker push avvo/ruby-ubuntu:2.3
docker build -f Dockerfile.2.4.1 -t avvo/ruby-ubuntu:2.4.1 -t avvo/ruby-ubuntu:2.4 -t avvo/ruby-ubuntu:2 -t avvo/ruby-ubuntu:latest .
docker push avvo/ruby-ubuntu:2.4.1
docker push avvo/ruby-ubuntu:2.4
docker push avvo/ruby-ubuntu:2
docker push avvo/ruby-ubuntu:latest
```

Tags:

* `avvo/ubuntu-base:1.1` adds unzip package
# alpine-phantomjs-builder

This is meant to build a phantomjs package that can be used in alpine docker images.  It's **NOT** meant to be a usable docker image after the build is complete, and simply outputs the phantomjs tarball.

Please don't push the built image up to any docker image repos.  It's not suitable for running services, containers, etc.

This should be broken out into a repo of its own, but since it doesn't work yet... that step was skipped.

Current status as of May 22nd, 2017: Need to figure out why the phantomjs binary built by this image hangs in alpine.  A couple of patches were introduced to integrate this phantomjs more closely with alpine, (build-deps, and build-nonstatic) but neither one fixed the hanging problem.
