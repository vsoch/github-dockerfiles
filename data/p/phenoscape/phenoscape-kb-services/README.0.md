# Swagger JSON
This is a swagger JSON built by the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project.# Docker container for phenoscape-kb-services

[![Docker Hub Repository](https://img.shields.io/docker/automated/phenoscape/phenoscape-kb-services.svg)](https://hub.docker.com/r/phenoscape/phenoscape-kb-services/) [![Docker Hub Pulls](https://img.shields.io/docker/pulls/phenoscape/phenoscape-kb-services.svg)](https://hub.docker.com/r/phenoscape/phenoscape-kb-services/)

This Docker container will automatically run the phenoscape-kb-services application, exposed on port 8082. (You will need to map this to a port suitable for you on the host.)

## Available image tags
The following tags are currently available from Docker Hub:
* `latest`: The [latest release]. Note that because this tag is currently not rebuilt automatically whenever a new release is made, it may in actuality be behind the latest release.
* `edge`: The `master` branch. Note the image available from Docker Hub is the last build from `master` that _succeeded_. (You can see the current [build status on Docker Hub] for each tag.)
* Release tag name: The corresponding release tag.

## Runtime customization

### application.conf
By defaut, the service will expect the `application.conf` file at `/srv/conf/application.conf`. Map the directory where you have your conf file to this path, or alternatively override the location on the `docker run` command line (append `-Dconfig.file=</path/to/application.conf>` after the image name; this must be a path _within_ the container).

You can find an example `application.conf` file in [`src/main/resources/application.conf.example`](../src/main/resources/application.conf.example) (relative to the project root).

Note that the `kb-services.port` and `kb-services.host` settings in your `application.conf` are irrelevant, because they are overridden in the entrypoint definition for the container.

### Java memory and other options
The application will typically benefit from a fair amount of memory. By default, Java is allowed up to 8GB of memory in the container.

You can change the memory available to Java, and other options, by setting the `JAVA_OPTS` environment on the `docker run` command line, by using the `--env` option. Note that this will override the default setting, and hence if you set the environemnt, you must include the increased memory as well.

## Build configuration

Currently the following build arguments (`--build-arg` command line option to `docker build`) are supported:

* `APP_USER` and `APP_GROUP`: designated user and group for running
  the application process within the container (default: `phenoscape`)
* `TARGET`: the target to build, as the branch, tag, or release. By default,
  the _latest release_ is built (this may not be the latest _tag_). To build
  a specific branch or tag, set `TARGET` to the corresponding value (e.g.,
  `--build-arg TARGET=master` to build from the master branch).

[latest release]: https://github.com/phenoscape/phenoscape-kb-services/releases/latest
[build status on Docker Hub]: https://hub.docker.com/r/phenoscape/phenoscape-kb-services/builds/
