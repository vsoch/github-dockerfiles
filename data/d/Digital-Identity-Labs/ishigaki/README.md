# Ishigaki

[![Build Status](https://travis-ci.org/Digital-Identity-Labs/ishigaki.svg?branch=master)](https://travis-ci.org/Digital-Identity-Labs/ishigaki)
[![Docker Stars](https://img.shields.io/docker/stars/digitalidentity/ishigaki.svg)](https://hub.docker.com/r/digitalidentity/ishigaki/) 
[![Image Details](https://images.microbadger.com/badges/image/digitalidentity/ishigaki.svg)](https://microbadger.com/images/digitalidentity/ishigaki "Get your own image badge on microbadger.com")

## What is this?

[Shibboleth Identity Provider](https://www.shibboleth.net/products/identity-provider/) is a mature, SAML-based 
single sign on (SSO) web application widely deployed in academic organisations. It's used by millions of staff and 
students around the world.

Ishigaki is a minimalist, Debian-based, Shibboleth IdP Docker image. It is maintained by [Digital Identity Ltd.](http://digitalidentity.ltd.uk/) 
Ishigaki is intended to be a solid foundation for other images but can also be used directly by mounting volumes for configuration directories.

This image is *not* a stand-alone production-ready IdP - it's meant to be configured and then used in conjunction with
 other services to handle TLS, databases, LDAP, and so on. It's especially well suited to use with Docker Compose, Rancher or 
Kubernetes. 

## Why use this?

* **Modern**: uses the latest Shibboleth IdP, Jetty and Debian OS.
* **Small**: based on Minideb and built carefully, Ishigaki is only around 350MB and the download is under 180MB
* **Secure**: updated daily, nothing runs as root, and directory permissions are managed
* **Tested**: Ishigaki is built and tested automatically
* **Maintained**: we use this image ourselves


## Any reasons not to use this?

* It is *not* ready-to-use, and there is no UI or simplified configuration: you need to understand how to configure a 
Shibboleth IdP
* It's got no warranty or support (but see Ishigaki Academic Edition details below)
* It does not use the official Oracle JDK - it uses a high quality JDK from Zulu but Shibboleth community support may
 depend on using Oracle's software (again, see below for other options)
* It requires other supporting services to provide TLS and user information
* Docker should not be used in production unless you have a reliable process for regularly updating images and replacing containers
* It's relatively new - we expect to find more bugs 

## Configuring and running Ishigaki

### Getting the image

`docker pull digitalidentity/ishigaki`

### Configuring the IdP

Copy the current configuration from a running container:

`docker ps`  (then copy the container id)

`copy cp 1739d2ec6159:/opt ./optfs`  (use your container id!)

All the useful configuration for Ishigaki is in various /opt directories:

  *  `admin` - this contains some internal tools. 
  *  `jetty` - the global Jetty configuration.
  *  `jetty-shib` - extra Jetty configuration files for running Shibboleth
  *  `misc` - a few other files
  *  `shibboleth-idp` - the Shibboleth IDP configuration

Adjust these files to suit your use-case - see the
 [Shibboleth IdP documentation](https://wiki.shibboleth.net/confluence/display/IDP30/Home) for lots more information.

As you're probably copying these files over the top of existing files, you don't need to keep copies of files you aren't changing. 
You can usually not bother with the admin, jetty and misc directories. You will probably only need to change the jetty-shib directory
if you are adding TLS or backchannel ports directly to the IdP, rather than using a proxy.

If you copy over scripts in admin/ they will stop working until you use `chmod a+x /opt/admin/*.sh` to fix them. 

### Running Ishigaki with your configuration

Then you can either build an image that contains your configuration, like this:

```dockerfile
FROM digitalidentity/ishigaki:latest
# (Don't use latest in production)

LABEL description="An example IdP image based on Ishigaki" \
      version="0.0.1" \
      maintainer="example@example.com"

## The prepare_apps.sh script can use these - but they're not needed otherwise
ENV IDP_HOSTNAME=idp.example.com \
    IDP_SCOPE=example.com \
    IDP_ID=https://idp.example.com/idp/shibboleth

## Copy your configuration files over into the image
COPY optfs /opt

## This is an optional script to tidy up file permissions, etc.
RUN $ADMIN_HOME/prepare_apps.sh

```

or run the Ishigaki image with mounted directories

`docker run -v /home/bjensen/myshib/optfs/shibboleth-idp:/opt/shibboleth-idp digitalidentity/ishigaki`

### Using with Docker Compose

Running a relatively bare Ishigaki container on its own is only useful for some basic dev or testing work. It's far more useful when used with other Docker containers.

For example, a `docker-compose.yml` file like this can provide a basic IdP service, with TLS and LDAP:

```docker-compose
version: '3'
services:
  frontend:
    image: traefik:latest
    command: --web --docker --docker.domain=docker.localhost --logLevel=DEBUG
    ports:
      - "443:443"
      - "8080:8080"
      - "8433:8443"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - ./frontend/traefik.toml:/traefik.toml
      - ./frontend/certs:/certs

  ldap:
    image: digitalidentity/eduldap:latest
    labels:
      - "traefik.enable=false"

  idp:
    image: digitalidentity/ishigaki:latest
    volumes:
     - ./idp/shibboleth-idp:/opt/shibboleth-idp
    labels:
      - "traefik.backend=idp"
      - "traefik.frontend.passHostHeader=true"
      - "traefik.frontend.rule=Host:idp.localhost.demo.university"
      - "traefik.frontend.entryPoints=https"
      - "traefik.port=8080"
      - "traefik.protocol=http"

```

(This is not going to work on its own - you'll need to use your own data, Traefik configuration, LDAP data, etc)

### When building an image based on Ishigaki

Possibly useful things to know:

  * You can re-run the `prepare_apps.sh` script in /opt/admin/ to reset permissions after copying files (and replace it)
  * If you pass the "rebuild" option to `prepare_apps.sh` like this (`/opt/admin/prepare_apps.sh rebuild`) it will also
    repackage the IdP .war file, including any customised views or libraries you may have added to the edit-webapp directory
  * The Ishigaki repository uses the Inspec tests from the [ishigaki-spec](https://github.com/Digital-Identity-Labs/ishigaki-spec) profile on Github. 
  You can use this to test your own Docker image by including it as a dependency in your inSpec profile. Look at the code in the 
  Ishigaki repo to see how it's done.
   set of tests
  * If you copy new files over the admin scripts (such as prepare_apps.sh) they'll need their executable permissions
   setting again before they can be run: if you replace prepare_apps.sh it won't run directly until this is done. 
  

### Running without a reverse proxy

Unlike most IdP images Ishigaki assumes it is behind a reverse proxy such as Apache HTTPD or Traefik. 
The default configuration accepts and trusts some HTTP headers that it assumes carry information from the proxy.

If you add TLS, backchannel ports, etc and run Ishigaki directly, without a proxy, please remove the configuration options 
for these headers, or they may be a security risk for your service.


## Other Information


### What's Ishigaki Academic Edition?

Ishigaki Academic Edition is a commercial, supported version of Ishigaki produced and supported by [Mimoto Ltd](http://mimoto.co.uk). It can be used in exactly the same way, but has a few differences:

* Includes remote or on-site support from Mimoto
* Uses the official Oracle JDK
* Releases are manually checked, and given additional, more intensive tests
* Releases are signed, and available from a private repository

If you'd like more information about Ishigaki Academic Edition, please [contact Mimoto](http://mimoto.co.uk/contact/)

### Related Projects from Digital Identity

* eduLDAP - a quick and easy OpenLDAP image for HE use

### What does "ishigaki" mean?
Ishigaki are the impressive dry stone [foundation walls of Japanese castles](http://www.jcastle.info/resources/view/109-Stone-Walls).
(Ishigaki is also the name of a beautiful [island and city in Okinawa](https://en.wikipedia.org/wiki/Ishigaki_Island))

### Thanks
* Ian Young's script to test Java crypto features has been included with his kind permission
* We're just packaging huge amounts of work by [The Shibboleth Consortium](https://www.shibboleth.net/consortium/) and
 the wider Shibboleth community. If your organisation depends on Shibboleth please consider supporting them.

### Contributing
You can request new features by creating an [issue](https://github.com/Digital-Identity-Labs/ishigaki/issues), or submit a [pull request](https://github.com/Digital-Identity-Labs/ishigaki/pulls) with your contribution.

The Ishigaki repo contains tests that you can use in your own projects. We're extra grateful for any contributions that 
include tests.

If you have a support contract with Mimoto, please [contact Mimoto](http://mimoto.co.uk/contact/) for assistance, rather
 than use Github.

### License
Copyright (c) 2017 Digital Identity Ltd, UK

Licensed under the MIT License
