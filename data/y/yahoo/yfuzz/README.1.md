# yFuzz Server

![godoc](https://godoc.org/github.com/yahoo/yfuzz/services/yfuzz-server?status.svg)

The main API server for [yFuzz](https://github.com/yahoo/yfuzz).

## Table of Contents
- [yFuzz Server](#yfuzz-server)
  - [Table of Contents](#table-of-contents)
  - [Configuration](#configuration)
  - [Running](#running)
  - [Plugins](#plugins)
  - [Usage](#usage)
  - [Build](#build)
    - [Local Build](#local-build)
    - [Docker Build](#docker-build)

## Configuration
yFuzz will read configuration from a file called `config.yaml` (or any other format supported by [viper](https://github.com/spf13/viper)) located either in `$HOME/.yfuzz`, `/etc/yfuzz`, or the current directory.

Options can also be specified in environment variables with the `YFUZZ_` prefix.

See `config-sample.yaml` for sample configuration.

## Running
The simplest way to run the server is as a docker container:
```bash
$ docker run -v "$(pwd)"/config.yaml:/etc/yfuzz/config.yaml yfuzz/server
```

## Plugins
A number of plugins to the yFuzz API are supported:
* [Athenz](plugins/athenz): Authorize requests with [Athenz](http://www.athenz.io).
* [MTLS](plugins/mtls): Authenticate requests with mutual TLS and authorize based on a list of authorized keys. 

## Usage
API endpoints are documented with godoc. 

yFuzz is currently accessible through the use of the [yFuzz CLI](../../cmd/yfuzz-cli).

## Build 
To build the server, you will need [Go](https://golang.org/), [Glide](https://glide.sh/), and [Make](https://www.gnu.org/software/make/).

There are two ways to build the yFuzz server: on your system, and as a docker image.

### Local Build
```bash
$ git clone https://github.com/yahoo/yfuzz.git
$ cd yfuzz/services/yfuzz-server
$ make install
```

### Docker Build
```bash
$ git clone https://github.com/yahoo/yfuzz.git
$ cd yfuzz/services/yfuzz-server
$ make docker
```
# Athenz Plugin
The Athenz plugin uses [Athenz](http://www.athenz.io) to authorize requests to the [yFuzz API](../..).

Requests are authenticated with mutual TLS, so the `todo` setting must be enabled in the [CLI config](../../../cmd/yfuzz-cli#settings).

## Configuration
Plugins in yFuzz are configured in the `config.yaml` file. The following options are available for the `athenz` plugin:
* `url`: URL for your Athenz server.
* `cert-file`: Path to the x509 certificate associated with your Athenz service.
* `key-file`: Path to the private key associated with the certificate.
* `ca-issuer-name`: The name of the CA used by your Athenz instance.
* `action` and `resource`: Athenz principals must be authorized to perform `action` on `resource` to be able to access the yFuzz API.

```yaml
plugins:
  # Information for Athenz (see http://athenz.io/)
  - athenz:
      url: https://your-athenz-server.com/zms/v1
      cert-file: /path/to/athenz/cert
      key-file: /path/to/athenz/key
      ca-issuer-name: Athenz CA Name
      action: access
      resource: yfuzz:yfuzz
```

## See Also
* The mutual TLS option in the [yFuzz CLI](../../../cmd/yfuzz-cli#settings).
* The [list of yFuzz plugins](../../../docs/plugins.md).# MTLS Plugin
The mtls (mutual TLS) plugin uses mutual tls and self-signed certificates to authenticate requests to the [yFuzz API](../..).

Requests are authorized based on if the public key associated with the user's certificate is in a whitelist.

## Adding a New User
First, generate a user x509 certificate:
```bash
$ openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -nodes
$ openssl rsa -in key.pem -pubout
```

Then whitelist that certificate by adding the public key to the yFuzz configuration file.

## Configuration
Plugins in yFuzz are configured in the `config.yaml` file. The following options are available for the `mtls` plugin:

```yaml
plugins:
  - mtls:
      authorized-keys:
        - |
          -----BEGIN PUBLIC KEY-----
          Public key goes here.
          -----END PUBLIC KEY-----
        - |
          -----BEGIN PUBLIC KEY-----
          A second public key.
          -----END PUBLIC KEY-----
```

* `authorized-keys`: List of public keys corresponding to users authorized to access yFuzz.

## See Also
* Mutual TLS configuration in the [yFuzz CLI](../../../cmd/yfuzz-cli#settings).
* The [list of yFuzz plugins](../../../docs/plugins.md).