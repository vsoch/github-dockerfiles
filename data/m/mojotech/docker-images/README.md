# docker-images

This repo contains scripts to build some useful docker base images. The are available for use at [quay.io](http://quay.io).

## Images

### [debian](http://quay.io/mojotech/debian)
A debian wheezy base image with the mojotech apt repository key.

### [node](http://quay.io/mojotech/node)
The debian base image plus node.js, npm, and the build tools necessary to install most npm packages (even those requiring native extensions).

### [clojure](http://quay.io/mojotech/clojure)
The debian base image plus java and leiningen.

### [groovy](http://quay.io/mojotech/groovy)
The debian base image plus java and gradle.

### [python](http://quay.io/mojotech/python)
The debian base image plus python, pip, and virtualenv.

### [riemann](http://quay.io/mojotech/riemann)
The clojure image with the riemann service installed.

### [datomic](http://quay.io/mojotech/datomic)
The clojure image with the datomic service installed.

## Building

Use `make <name>` to build an image. For example, to build the clojure image:

    make clojure

Dependencies are expressed in the Makefile, so running the above command would also build the debian image.

It is also possible to specify the `TAG` and `REGISTRY` of the resulting image:

    make REGISTRY=quay.io/mojotech TAG=$(git rev-parse --short HEAD) clojure

This would override the default `REGISTRY` (mojotech) and `TAG` (latest).

## Pushing

To push all the images once built, use `make push`. To push just a single image, use `make push-<name>`. The `REGISTRY` and `TAG` values can also be overridden:

    make REGISTRY=quay.io/mojotech TAG=$(git rev-parse --short HEAD) push-clojure
