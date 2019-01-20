Fedora Repository Docker Image
==============================

A simple Docker image to run the [Fedora Repository][1].

See the [Hub page][2] for the available images and the [Github repo][3] to
review the Dockerfiles.

Usage
-----

Pull and run the docker image:

    $ docker pull osul/fcrepo
    $ docker run -p 8080:8080 osul/fcrepo

Fedora will now be available at [http://localhost:8080/fcrepo](http://localhost:8080/fcrepo)

Notes
-----

  * The Tomcat 7 manager username and password are "fedora"
  * Fedora data is stored in a Docker volume at `/mnt/fcrepo4-data`
  * `/mnt/ingest` is also mounted as a Docker volume.


[1]: http://fedorarepository.org
[2]: https://hub.docker.com/r/osul/fcrepo
[3]: https://github.com/osulibraries/fcrepo-docker
