# DEPRECATED

Do not use this repository. Use https://github.com/ixc/letsencrypt-docker
instead, which works with the official `dockercloud-haproxy` image and fixes
a few problems and limitations with this `letsencrypt` image.

# Overview

The `haproxy` image will:

  * Create a self signed default certificate, so HAproxy can start before we
    have any real certificates.

  * Watch the `/etc/letsencrypt/live` directory and when changes are detected,
  	install combined certificates and reload HAproxy.

The `letsencrypt` image will:

  * Automatically create or renew certificates on startup and daily thereafter.

# Usage

In your stack file:

  * Link to the `letsencrypt` service from the `haproxy` service.

  * Use `volumes_from: letsencrypt` in the `haproxy` service.

  * Define a `DOMAINS` environment variable in the `letsencrypt` service.
    Certificates are separated by semi-colon (;) and domains are separated by
    comma (,).

  * Define an `EMAIL` environment variable in the `letsencrypt` service. It
    will be used for all certificates.

  * Define an `OPTIONS` environment variable in the `letsencrypt` service, if
    you want to pass additional arguments to `certbot` (e.g. `--staging`).

Several environment variables are hard coded, and don't need to be defined in
your stack file:

  * The `DEFAULT_SSL_CERT` environment variable is set to the value of the
  	default/first Let's Encrypt certificate (if not already explicitly set),
  	to ensure SSL termination is enabled.

  * The `VIRTUAL_HOST` and `VIRTUAL_HOST_WEIGHT` environment variables are hard
    coded in the `letsencrypt` image, to ensure challenge requests for all
    domains are proxied to the `letsencrypt` service.

A sample stack file is provided.
