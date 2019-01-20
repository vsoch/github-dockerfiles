atlas-deer
==========

This contains all the projects relating to the 4.0 API release of Atlas, a.k.a `deer`. It replaces the deer branches on the other existing atlasapi/* repositories.

The repository is divided in 5 projects:

* atlas-api: the Atlas API 4.0 web-app containing HTTP controllers, query executors and model serializers.
* atlas-processing: the back-end web-app for running scheduled tasks.
* atlas-core: defines the model and interfaces on which atlas-api and atlas-processing rely and their common and base implementations.
* atlas-cassandra: Cassandra-based implementations of the core persistence interfaces.
* atlas-elasticsearch: elasticsearch-based implementations of the core index interfaces.

Development installation
------------------------

You will need:
  * Maven 3
  * Google’s protocol buffer compiler, protoc, on your path (see bug below if you have trouble compiling protoc).
  * ElasticSearch (Check the atlas-elasticsearch POM and find the current client version used, you need the same version - both major and minor must match).
  * The current version of the 2.0.x release of Cassandra (http://planetcassandra.org/cassandra/) and latest cqlsh
  * The latest version of MongoDB (http://www.mongodb.org/)

* Make sure the protobuf library version specified in the atlas-cassandra/pom.xml matches the output of protoc —version
* Start Cassandra locally on the standard port
* Start ElasticSearch (check the cluster name in dev.properties and change your elasticsearch.yml in /config/ to match)
* Run mvn package in the project directory

At this stage you hopefully have successfully obtained war files.

* Run cqlsh:
  * create keyspace atlas_deer_dev with replication = { 'class': 'SimpleStrategy', 'replication_factor': 1 };
* cqlsh -k atlas_deer_dev -f atlas-cassandra/src/main/resources/atlas.schema

Finally:
* java -jar atlas-api/target/atlas-api.war

Development
--------------------------
## Tests
The integration tests are run via the `failsafe` plugin, which hooks into the `verify` Maven phase.
This means that to run **all** the tests, you need to run `mvn test verify` instead of `mvn test`.

## Netty
The netty transport is set to use `epoll`, which may not work if you want to run it in a non-Linux
environment. If you see issues around the Cassandra driver or Netty's transport, try removing the
relevant lines from the POMs and rebuilding.

Security
--------------------------

Be advised that we are in the process of removing OAuth authentication from Atlas and externalising 
those responsibilities to other internal systems. Towards that goal we have added new admin
endpoints under `/4/admin` that duplicate functionality in our existing OAuth enabled admin
endpoints, but without any user authentication in them.

If you are running your own deployment of Atlas you need to put your own security in front of
those endpoints otherwise you will be introducing a security vulnerability that will allow anyone
with access to the endpoints to read and modify api keys.

Problems
--------
* Error when using make to compile protoc
        https://code.google.com/p/protobuf/issues/detail?id=570
