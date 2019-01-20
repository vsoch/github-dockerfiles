Solr Docker Image
=================

A docker image to run [Apache Solr][1], based on the [official Solr image][2].
This image attempts to solve the problem of running a Solr image as a service in
[Gitlab CI][3].

See the [Hub page][2] for the available images and the [Github repo][3] to
review the Dockerfiles.

Basic Usage
-----------

Pull and run the docker image:

    $ docker pull osul/solr
    $ docker run -p 8983:8983 osul/solr

Solr will now be available at [http://localhost:8983/solr/](http://localhost:8983/solr/).
See the [official Solr image][2] documentation for more details.

Gitlab CI Integration
---------------------

To use this image as a service in a Gitlab CI build, include the Solr
schema/configuration files in your project's source code. Add `osul/solr` to the
`services` key in your `.gitlab-ci.yml`

    services:
      - osul/solr

Next, add the Solr configuration directory (within your project) and the Solr
core name to the `variables` key:

    variables:
      SOLR_CORE_NAME: "mycore"
      SOLR_CONFIG_DIR: "solr/config"

When the Solr image starts, it will clone a copy of the project under test,
check out the current commit, and create a new Solr core using the
configuration files in the `SOLR_CONFIG_DIR`. The Solr core will be available
to the application at: `http://osul__solr:8983/solr/mycore`


[1]: http://lucene.apache.org/solr/
[2]: https://hub.docker.com/_/solr/
[3]: https://about.gitlab.com/gitlab-ci/
[4]: https://hub.docker.com/r/osul/solr
[5]: https://github.com/osulibraries/solr-docker
