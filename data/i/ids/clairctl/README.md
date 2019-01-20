# clairctl

> Tracking container vulnerabilities with Clair Control

---
This was forked because I was unable to scan local images, I kept getting 404 errors in Clair.  Having never cut a line of Go code, it only seemed logical to try to debug it.  It is a really cool tool. How hard could it be?

Seems when you pass it a local image to scan, __clairCtl__ will copy the image layers to a temp location, and then fire up a temporary HTTP server to host them up for Clair.

__clairCtl__ then sends requests to Clair to scan each layer, which is an url back to itself.

The issue I was having was that the url clairCtl was sending to Clair didn't match the actual path it was serving via HTTP, because it was derriving the temp path in two places using two different sources for image name information, and they often didn't match.

I've altered that logic a bit to allow the names to match by letting the user supplied name pass through. Still a work in progress.

In any case, all the images I couldn't scan remotely, I can now scan locally, including the ones affected by the change in Docker's manifest format on DockerHub that causes clairCtl to kick up an __Unsupported Schema__ error: https://github.com/jgsqware/clairctl/issues/93

Local scanning seems like all you would need in a CI job, as Clair is likely to be hosted as a shared service in the pre-production environment. All you really need is the ability to scan the local image after it has been built in the CI runner.

I've made a few mods to support this:

* It now defaults to local scan
* Added a line `viper.SetEnvKeyReplacer(strings.NewReplacer(".", "_"))` in the config.go so that nested config.yml settings could be passed as env variables, which is handy in CI. See the [clairctlenv](clairctlenv) file for examples.
* Added a routine to start the local server for a report, which seemed missing.
* Added a freeport routine to get an available port dynamically (deprecating the setting in yaml and env).  This is needed when running multuple concurrent scans on a ci runner.

> I've been able to use clairctl to scan the resulting clairctl docker image, which is very meta, and also provides a working example of using clairctl in a Gitlab CI pipeline.

The __Gitlab CI__ jobs do the following on commit:

### for all branches:
- compile

### for master:
- increments the product version
- cross-compiles and publishes binaries to Github on a new release version
- builds a new docker image 
- scans the image with clairctl (an artifact from the cross-compile job previously)
- pushes the new version and tag to docker hub
- updates the “latest” tag and pushes

### for develop:
- cross-compiles and publishes binaries to Github on a standing pre-release “develop" version
- builds new docker image “develop” version
- scans the image with clairctl (an artifact from the cross-compile job)
- pushes the new develop image to docker hub

---

Clairctl is a lightweight command-line tool doing the bridge between Registries as Docker Hub, Docker Registry or Quay.io, and the CoreOS vulnerability tracker, Clair.
Clairctl will play as reverse proxy for authentication.

Clairctl version is align with the [CoreOS Clair](https://github.com/coreos/clair) supported version.

# Installation

## Released version:

Go to [Release](https://github.com/ids/clairctl/releases) and download the client version for your platform

## Master branch version

```bash
curl -L https://raw.githubusercontent.com/ids/clairctl/master/install.sh | sh
``` 

# Docker-compose

```bash
$ git clone git@github.com:ids/clairctl.git $GOPATH/src/github.com/ids/clairctl
$ cd $GOPATH/src/github.com/ids/clairctl
$ docker-compose up -d postgres
Creating network "clairctl_default" with the default driver
Creating clairctl_postgres_1 ...
Creating clairctl_clair_1 ...
Creating clairctl_clairctl_1 ...
```

The above commands will check out the `clairctl` repo and start the complete postgres/clair/clairctl stack.

```bash
$ docker-compose exec clairctl clairctl health

Clair: ✔
```

The above command will make sure clairctl can reach clair.

If you wish to serve local images to clair, the user inside the clairctl container will need read access to `/var/run/docker.sock`.

Give the user access by:
  - Running the container as root (`--user root` with `docker run` or `user: root` with `docker-compose`)
  - Add the container user to the docker group (`----group-add group_id` with `docker run` or `group_add: group_id` with `docker-compose`)

To get the group name or id, simply execute :

```bash
$ docker-compose exec clairctl ls -alh /var/run/docker.sock
srw-rw----    1 root     50             0 Jul 18 09:48 /var/run/docker.sock
```

In the example above, 50 is the required group.

# Usage

[![asciicast](https://asciinema.org/a/41461.png)](https://asciinema.org/a/41461)

# Reporting

**clairctl** get vulnerabilities report from Clair and generate HTML report

clairctl can be used for Docker Hub and self-hosted Registry

# Commands

```
Analyze your docker image with Clair, directly from your registry.

Usage:
  clairctl [command]

Available Commands:
  analyze     Analyze Docker image
  health      Get Health of clairctl and underlying services
  pull        Pull Docker image information (This will not pull the image !)
  push        Push Docker image to Clair
  report      Generate Docker Image vulnerabilities report
  version     Get Versions of clairctl and underlying services

Flags:
      --config string      config file (default is ./.clairctl.yml)
      --log-level string   log level [Panic,Fatal,Error,Warn,Info,Debug]

Use "clairctl [command] --help" for more information about a command.
```

# Optional Configuration

```yaml
clair:
  port: 6060
  healthPort: 6061
  uri: http://clair
  report:
    path: ./reports
    format: html
```

## Optional whitelist yaml file

This is an example yaml file. You can have an empty file or a mix with only `generalwhitelist` or `images`.

```yaml
generalwhitelist: #Approve CVE for any image
  CVE-2016-2148: BusyBox
  CVE-2014-8625: Why is it whitelisted
images:
  ubuntu: #Approve CVE only for ubuntu image, regardless of the version
    CVE-2014-2667: Python
    CVE-2017-5230: Something
  alpine:
    CVE-2016-7068: Something
```

# Building the latest binaries

**clairctl** requires Go 1.8+.

Install Glide:
```
curl https://glide.sh/get | sh
```

Clone and build:
```
git clone git@github.com:ids/clairctl.git $GOPATH/src/github.com/ids/clairctl
cd $GOPATH/src/github.com/ids/clairctl
glide install -v
go get -u github.com/jteeuwen/go-bindata/...
go generate ./clair
go build
```

This will result in a `clairctl` executable in the `$GOPATH/src/github.com/ids/clairctl` folder.

# FAQ

## I get 400 errors !

If you get 400 errors, check out clair's logs. The usual reasons are :
  
  - You are serving a local image, and clair cannot connect to clairctl.
  - You are trying to analyze an official image from docker hub and you have not done a docker login first.
  
Please try these two things before opening an Issue.

## I get access denied on /var/run/docker.sock

If you are running the stack with the provided `docker-compose.yml`, don't forget to grant the user from the clairctl container access to `/var/run/docker.sock`. 

All steps are detailed in the Docker-compose section above.

# Contribution and Test

Go to /contrib folder
