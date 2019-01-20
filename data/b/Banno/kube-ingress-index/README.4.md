# Distribution

The Docker toolset to pack, ship, store, and deliver content.

This repository's main product is the Docker Registry 2.0 implementation
for storing and distributing Docker images. It supersedes the
[docker/docker-registry](https://github.com/docker/docker-registry)
project with a new API design, focused around security and performance.

<img src="https://www.docker.com/sites/default/files/oyster-registry-3.png" width=200px/>

[![Circle CI](https://circleci.com/gh/docker/distribution/tree/master.svg?style=svg)](https://circleci.com/gh/docker/distribution/tree/master)
[![GoDoc](https://godoc.org/github.com/docker/distribution?status.svg)](https://godoc.org/github.com/docker/distribution)

This repository contains the following components:

|**Component**       |Description                                                                                                                                                                                         |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **registry**       | An implementation of the [Docker Registry HTTP API V2](docs/spec/api.md) for use with docker 1.6+.                                                                                                  |
| **libraries**      | A rich set of libraries for interacting with distribution components. Please see [godoc](https://godoc.org/github.com/docker/distribution) for details. **Note**: These libraries are **unstable**. |
| **specifications** | _Distribution_ related specifications are available in [docs/spec](docs/spec)                                                                                                                        |
| **documentation**  | Docker's full documentation set is available at [docs.docker.com](https://docs.docker.com). This repository [contains the subset](docs/) related just to the registry.                                                                                                                                          |

### How does this integrate with Docker engine?

This project should provide an implementation to a V2 API for use in the [Docker
core project](https://github.com/docker/docker). The API should be embeddable
and simplify the process of securely pulling and pushing content from `docker`
daemons.

### What are the long term goals of the Distribution project?

The _Distribution_ project has the further long term goal of providing a
secure tool chain for distributing content. The specifications, APIs and tools
should be as useful with Docker as they are without.

Our goal is to design a professional grade and extensible content distribution
system that allow users to:

* Enjoy an efficient, secured and reliable way to store, manage, package and
  exchange content
* Hack/roll their own on top of healthy open-source components
* Implement their own home made solution through good specs, and solid
  extensions mechanism.

## More about Registry 2.0

The new registry implementation provides the following benefits:

- faster push and pull
- new, more efficient implementation
- simplified deployment
- pluggable storage backend
- webhook notifications

For information on upcoming functionality, please see [ROADMAP.md](ROADMAP.md).

### Who needs to deploy a registry?

By default, Docker users pull images from Docker's public registry instance.
[Installing Docker](https://docs.docker.com/engine/installation/) gives users this
ability. Users can also push images to a repository on Docker's public registry,
if they have a [Docker Hub](https://hub.docker.com/) account.

For some users and even companies, this default behavior is sufficient. For
others, it is not.

For example, users with their own software products may want to maintain a
registry for private, company images. Also, you may wish to deploy your own
image repository for images used to test or in continuous integration. For these
use cases and others, [deploying your own registry instance](https://github.com/docker/docker.github.io/blob/master/registry/deploying.md)
may be the better choice.

### Migration to Registry 2.0

For those who have previously deployed their own registry based on the Registry
1.0 implementation and wish to deploy a Registry 2.0 while retaining images,
data migration is required. A tool to assist with migration efforts has been
created. For more information see [docker/migrator]
(https://github.com/docker/migrator).

## Contribute

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute
issues, fixes, and patches to this project. If you are contributing code, see
the instructions for [building a development environment](BUILDING.md).

## Support

If any issues are encountered while using the _Distribution_ project, several
avenues are available for support:

<table>
<tr>
	<th align="left">
	IRC
	</th>
	<td>
	#docker-distribution on FreeNode
	</td>
</tr>
<tr>
	<th align="left">
	Issue Tracker
	</th>
	<td>
	github.com/docker/distribution/issues
	</td>
</tr>
<tr>
	<th align="left">
	Google Groups
	</th>
	<td>
	https://groups.google.com/a/dockerproject.org/forum/#!forum/distribution
	</td>
</tr>
<tr>
	<th align="left">
	Mailing List
	</th>
	<td>
	docker@dockerproject.org
	</td>
</tr>
</table>


## License

This project is distributed under [Apache License, Version 2.0](LICENSE).
# Docker Registry Integration Testing

These integration tests cover interactions between registry clients such as
the docker daemon and the registry server. All tests can be run using the
[golem integration test runner](https://github.com/docker/golem)

The integration tests configure components using docker compose
(see docker-compose.yaml) and the runner can be using the golem
configuration file (see golem.conf).

## Running integration tests

### Run using multiversion script

The integration tests in the `contrib/docker-integration` directory can be simply
run by executing the run script `./run_multiversion.sh`. If there is no running
daemon to connect to, run as `./run_multiversion.sh -d`.

This command will build the distribution image from the locally checked out
version and run against multiple versions of docker defined in the script. To
run a specific version of the registry or docker, Golem will need to be
executed manually.

### Run manually using Golem

Using the golem tool directly allows running against multiple versions of
the registry and docker. Running against multiple versions of the registry
can be useful for testing changes in the docker daemon which are not
covered by the default run script.

#### Installing Golem

Golem is distributed as an executable binary which can be installed from
the [release page](https://github.com/docker/golem/releases/tag/v0.1).

#### Running golem with docker

Additionally golem can be run as a docker image requiring no additonal
installation.

`docker run --privileged -v "$GOPATH/src/github.com/docker/distribution/contrib/docker-integration:/test" -w /test distribution/golem golem -rundaemon .`

#### Golem custom images

Golem tests version of software by defining the docker image to test.

Run with registry 2.2.1 and docker 1.10.3

`golem -i golem-dind:latest,docker:1.10.3-dind,1.10.3 -i golem-distribution:latest,registry:2.2.1 .`


#### Use golem caching for developing tests

Golem allows caching image configuration to reduce test start up time.
Using this cache will allow tests with the same set of images to start
up quickly. This can be useful when developing tests and needing the
test to run quickly. If there are changes which effect the image (such as
building a new registry image), then startup time will be slower.

Run this command multiple times and after the first time test runs
should start much quicker.
`golem -cache ~/.cache/docker/golem -i golem-dind:latest,docker:1.10.3-dind,1.10.3 -i golem-distribution:latest,registry:2.2.1 .`

# Docker Compose V1 + V2 registry

This compose configuration configures a `v1` and `v2` registry behind an `nginx`
proxy. By default, you can access the combined registry at `localhost:5000`.

The configuration does not support pushing images to `v2` and pulling from `v1`.
If a `docker` client has a version less than 1.6, Nginx will route its requests
to the 1.0 registry. Requests from newer clients will route to the 2.0 registry.

### Install Docker Compose

1. Open a new terminal on the host with your `distribution` source.

2. Get the `docker-compose` binary.

		$ sudo wget https://github.com/docker/compose/releases/download/1.1.0/docker-compose-`uname  -s`-`uname -m` -O /usr/local/bin/docker-compose

	This command installs the binary in the `/usr/local/bin` directory. 
	
3. Add executable permissions to the binary.

		$  sudo chmod +x /usr/local/bin/docker-compose
		
## Build and run with Compose
	
1. In your terminal, navigate to the `distribution/contrib/compose` directory

	This directory includes a single `docker-compose.yml` configuration.
	
		nginx:
			build: "nginx"
			ports:
				- "5000:5000"
			links:
				- registryv1:registryv1
				- registryv2:registryv2
		registryv1:
			image: registry
			ports:
				- "5000"
		registryv2:
			build: "../../"
			ports:
				- "5000"

	This configuration builds a new `nginx` image as specified by the
	`nginx/Dockerfile` file. The 1.0 registry comes from Docker's official
	public image. Finally, the registry 2.0 image is built from the
	`distribution/Dockerfile` you've used previously.
 		
2. Get a registry 1.0 image.

		$ docker pull registry:0.9.1 

	The Compose configuration looks for this image locally. If you don't do this
	step, later steps can fail.
	
3. Build `nginx`, the registry 2.0 image, and 

		$ docker-compose build
		registryv1 uses an image, skipping
		Building registryv2...
		Step 0 : FROM golang:1.4
		
		...
		
		Removing intermediate container 9f5f5068c3f3
		Step 4 : COPY docker-registry-v2.conf /etc/nginx/docker-registry-v2.conf
		 ---> 74acc70fa106
		Removing intermediate container edb84c2b40cb
		Successfully built 74acc70fa106
		
	The commmand outputs its progress until it completes.

4. Start your configuration with compose.

		$ docker-compose up
		Recreating compose_registryv1_1...
		Recreating compose_registryv2_1...
		Recreating compose_nginx_1...
		Attaching to compose_registryv1_1, compose_registryv2_1, compose_nginx_1
		...
	

5. In another terminal, display the running configuration.

		$ docker ps
		CONTAINER ID        IMAGE                       COMMAND                CREATED             STATUS              PORTS                                     NAMES
		a81ad2557702        compose_nginx:latest        "nginx -g 'daemon of   8 minutes ago       Up 8 minutes        80/tcp, 443/tcp, 0.0.0.0:5000->5000/tcp   compose_nginx_1        
		0618437450dd        compose_registryv2:latest   "registry cmd/regist   8 minutes ago       Up 8 minutes        0.0.0.0:32777->5000/tcp                   compose_registryv2_1   
		aa82b1ed8e61        registry:latest             "docker-registry"      8 minutes ago       Up 8 minutes        0.0.0.0:32776->5000/tcp                   compose_registryv1_1   
	
### Explore a bit

1. Check for TLS on your `nginx` server.

		$ curl -v https://localhost:5000
		* Rebuilt URL to: https://localhost:5000/
		* Hostname was NOT found in DNS cache
		*   Trying 127.0.0.1...
		* Connected to localhost (127.0.0.1) port 5000 (#0)
		* successfully set certificate verify locations:
		*   CAfile: none
			CApath: /etc/ssl/certs
		* SSLv3, TLS handshake, Client hello (1):
		* SSLv3, TLS handshake, Server hello (2):
		* SSLv3, TLS handshake, CERT (11):
		* SSLv3, TLS alert, Server hello (2):
		* SSL certificate problem: self signed certificate
		* Closing connection 0
		curl: (60) SSL certificate problem: self signed certificate
		More details here: http://curl.haxx.se/docs/sslcerts.html
		
2. Tag the `v1` registry image.

		 $ docker tag registry:latest localhost:5000/registry_one:latest

2. Push it to the localhost.

		 $ docker push localhost:5000/registry_one:latest
		
	If you are using the 1.6 Docker client, this pushes the image the `v2 `registry.

4. Use `curl` to list the image in the registry.

			$ curl -v -X GET http://localhost:32777/v2/registry1/tags/list
			* Hostname was NOT found in DNS cache
			*   Trying 127.0.0.1...
			* Connected to localhost (127.0.0.1) port 32777 (#0)
			> GET /v2/registry1/tags/list HTTP/1.1
			> User-Agent: curl/7.36.0
			> Host: localhost:32777
			> Accept: */*
			> 
			< HTTP/1.1 200 OK
			< Content-Type: application/json; charset=utf-8
			< Docker-Distribution-Api-Version: registry/2.0
			< Date: Tue, 14 Apr 2015 22:34:13 GMT
			< Content-Length: 39
			< 
			{"name":"registry1","tags":["latest"]}
			* Connection #0 to host localhost left intact
		
	This example refers to the specific port assigned to the 2.0 registry. You saw
	this port earlier, when you used `docker ps` to show your running containers.


# Apache HTTPd sample for Registry v1, v2 and mirror

3 containers involved 

* Docker Registry v1 (registry 0.9.1)
* Docker Registry v2 (registry 2.0.0)
* Docker Registry v1 in mirror mode

HTTP for mirror and HTTPS for v1 & v2

* http://registry.example.com proxify Docker Registry 1.0 in Mirror mode
* https://registry.example.com proxify Docker Registry 1.0 or 2.0 in Hosting mode

## 3 Docker containers should be started 

* Docker Registry 1.0 in Mirror mode : port 5001
* Docker Registry 1.0 in Hosting mode : port 5000
* Docker Registry 2.0 in Hosting mode : port 5002

### Registry v1

    docker run -d -e SETTINGS_FLAVOR=dev -v /var/lib/docker-registry/storage/hosting-v1:/tmp -p 5000:5000 registry:0.9.1"

### Mirror

    docker run -d -e SETTINGS_FLAVOR=dev -e STANDALONE=false -e MIRROR_SOURCE=https://registry-1.docker.io -e MIRROR_SOURCE_INDEX=https://index.docker.io \
                  -e MIRROR_TAGS_CACHE_TTL=172800 -v /var/lib/docker-registry/storage/mirror:/tmp -p 5001:5000 registry:0.9.1"

### Registry v2

    docker run -d -e SETTINGS_FLAVOR=dev -v /var/lib/axway/docker-registry/storage/hosting2-v2:/tmp -p 5002:5000 registry:2"

# For Hosting mode access

* users should have account (valid-user) to be able to fetch images
* only users using account docker-deployer will be allowed to push images
Git Hooks
=========

To enforce valid and properly-formatted code, there is CI in place which runs `gofmt`, `golint`, and `go vet` against code in the repository.

As an aid to prevent committing invalid code in the first place, a git pre-commit hook has been added to the repository, found in [pre-commit](./pre-commit). As it is impossible to automatically add linked hooks to a git repository, this hook should be linked into your `.git/hooks/pre-commit`, which can be done by running the `configure-hooks.sh` script in this directory. This script is the preferred method of configuring hooks, as it will be updated as more are added.# The docs have been moved!

The documentation for Registry has been merged into
[the general documentation repo](https://github.com/docker/docker.github.io).
Commit history has been preserved.

The docs for Registry are now here:
https://github.com/docker/docker.github.io/tree/master/registry

> Note: The definitive [./spec directory](spec/) directory and
[configuration.md](configuration.md) file will be maintained in this repository
and be refreshed periodically in
[the general documentation repo](https://github.com/docker/docker.github.io).

As always, the docs in the general repo remain open-source and we appreciate
your feedback and pull requests!
