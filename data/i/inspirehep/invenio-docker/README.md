Invenio-Docker
=============

Docker images for Invenio

Images
------

### `inspirehep/invenio-base`

The base image for the Invenio project (master branch).
- It installs all the libraries required by Invenio.
- It does not configure Invenio.

### `inspirehep/invenio-drone`

The image used as a base for the Drone CI tests.
- It is based on `inspirehep/invenio-drone`.
- It configures the system for the Drone tests.
- It is specified in the `.drone.yml` file

### `test`

The image used to replicate the Drone CI tests.
- It is based on `inspirehep/invenio-drone`.
- It prepares the test environment with Drone-specific scripts.
- It is independent from the tested software (a part for the parent image).
- It is not intended to be pushed to Docker Hub.
- It is useful to replicate and debug the Drone tests execution.

Utilization
-----------

1. `make build`: builds images

2. `make test`: run tests, like Drone does

3. `make test-shell`: starts a shell in the Drone test container (then execute `drone` to run the tests)

4. `make push`: push images to Docker Hub

5. `make remove`: remove built images
