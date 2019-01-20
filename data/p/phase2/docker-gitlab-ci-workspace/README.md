# Outrigger GitLab CI Workspace

> A GitLab CI workbench ready to support a container-based pipeline.

[![Docker Stars](https://img.shields.io/docker/stars/outrigger/gitlab-ci-workspace.svg)](https://hub.docker.com/r/outrigger/gitlab-ci-workspace) [![Docker Pulls](https://img.shields.io/docker/pulls/outrigger/gitlab-ci-workspace.svg)](https://hub.docker.com/r/outrigger/gitlab-ci-workspace) [![](https://images.microbadger.com/badges/image/outrigger/gitlab-ci-workspace:18.svg)](https://microbadger.com/images/outrigger/gitlab-ci-workspace:18 "Get your own image badge on microbadger.com")

GitLab CI allows specification of a Docker image which will be pulled and started
as the first step of each job in every pipeline. For pipelines which will build
and deploy Docker images, a container based on the official Docker image is best.

We have extended that with additional tools:

* BASH, curl, OpenSSL to facilitate common build operations and expectations.
* Python for docker-compose and potentially future addition of aws-cli and gcloud.
* Kubernetes environment ready: built with kubectl and helm for k8s-ing.

Why are all these things built into this one image? We might pull some of these tools out in the future,
but the goal of this image is not to be a lean, single-purpose Docker image, but to provide an immutable
and quick-to-load CI environment.

## Usage Example

### Running Locally

This is how you might start up the Container locally to explore environment assumptions:

```
docker run --rm -it -v /var/run/docker.sock:/var/run/docker.sock outrigger/gitlab-ci-workspace bash
```

The volume mount allows the container to start and manage Docker containers for the host system.

### Using in .gitlab-ci.yml

```
# Configuration for the GitLab CI pipeline.
# https://docs.gitlab.com/ce/ci/yaml/
image: outrigger/gitlab-ci-workbench:18

services:
  - docker:18-dind

# <...>
```

## Security Reports

Please email outrigger@phase2technology.com with security concerns.

## Maintainers

[![Phase2 Logo](https://s3.amazonaws.com/phase2.public/logos/phase2-logo.png)](https://www.phase2technology.com)
