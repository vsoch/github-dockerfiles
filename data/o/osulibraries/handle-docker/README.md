Handle System Docker Image
==========================

A simple Docker image to run the [Handle System software][1]. Note that this
image is intended for development environments and is not suitable for
production use.

See the [Hub page][2] for the available images and the [Github repo][3] to
review the Dockerfiles.

Usage
-----

Pull and run the docker image:

    $ docker pull osul/handle
    $ docker run -p 8000:8000 -p 2641:2641 osul/handle

This image will expose the Handle Server HTTP interface on port 8000 and the
UDP and TCP Handle protocol on port 2641. The handle server is homed to the
`1234.TEST` and `1234.DEV` prefixes and configured for standalone operation.

The server admin handle is `1234.TEST/ADMIN` and responds to either the secret
key `password` on index 301, or a public key on index 300. You can find the
private key `admpriv.bin` in the [github repository][3].

### Client configuration

Handle clients will need to be configured to use this server to resolve
requests because it is not part of the global registry. For the reference
client:

  1. Create a copy of `siteinfo.json` from the [github repository][3] in
     `~/.handle` named `resolver_site`
  2. Change the value of the "address" key in that file to the IP or hostname
     of the Docker container (i.e. localhost)
  3. Run `echo "*" > ~/.handle/local_nas` to also direct admin operations to the
     container


[1]: https://www.handle.net
[2]: https://hub.docker.com/r/osul/handle
[3]: https://github.com/osulibraries/handle-docker
