Custom WAR Packager. Jenkinsfile Builder demo
===

This demo demonstrates building of Jenkinsfile Runner Docker images
with Custom WAR Packager.

To build the, run `make clean build`

You can experiment with other `Jenkinsfile`s if needed.
Once the Docker image is built, the demo Jenkinsfile Runner can be started simply as..

    docker run --rm -v $PWD/demo/Jenkinsfile:/workspace/Jenkinsfile jenkins-experimental/cwp-jenkinsfile-runner-demo


or in Kubernetes

    kubectl create configmap jenkinsfile --from-file=demo/Jenkinsfile
    kubectl create -f demo/kubernetes.yaml

Jenkins WAR Packager Demo. Stapler
===

This demo builds a Jenkins WAR which includes...

* `master` version of stapler


### Usage

To build the demo just run the `sh build.sh` command.
It will produce a `tmp/output/target/jenkins-stapler-1.0-SNAPSHOT.war` file.
You can run this file as a common Jenkins WAR file.
Jenkins WAR Packager Demo. All-latest core (with Maven)
===

This demo builds a Jenkins WAR which includes...

* Master branch of the Jenkins core
* Latest versions of Stapler, Remoting and XStream
* Latest versions of some modules (full list - TODO)
  * Some agent installer modules have obsolete tooling, they need to be updated before inclusion
* Latest version of Lib Task Reactor

The demo is similar to [All-latest core](../all-latest-core) demo, but it runs in Maven.

Limitations:

* Only component JARs are updated, the builder does not update dependencies
* WAR Packager is able to replace/add libs to WEB-INF/lib only, components
like Extras Executable War cannot be updated right now


### Usage

To build the demo just run the `mvn clean package` command.
It will produce a `target/custom-war-packager-maven-plugin/output/target/jenkins-all-latest-1.1-SNAPSHOT.war` file.
You can run this file as a common Jenkins WAR file.
Custom WAR Packager. Configuration-as-Code demo
===

This demo demonstrates usage of Configuration-as-Code plugin together 
with Jenkins Custom WAR Packager.

Use the provided Makefile in order to build (`make clean build`) 
and run (`make run`) the demo.
The root Custom WAR Packager project should be built first before running.


External Task Logging to Elasticsearch Demo
===

This demo packages Jenkins WAR for External Task Logging to Elasticsearch with help of Logstash plugin.

This demo includes [Logstash Plugin PR#18](https://github.com/jenkinsci/logstash-plugin/pull/18) and
all its upstream dependencies. 
It also bundles auto-configuration System Groovy scripts, so that the WAR file starts
up with pre-configured Logstash plugin settings and some other configs.

Features of the demo:

* Pipeline jobs logging goes to Elasticsearch
* When tasks are executed on agents, the logs get posted to Elasticsearch directly
  without passing though the master and causing scalability issues
* Pipeline jobs override standard Log actions in the Jenkins core, so the
  underlying implementation is transparent to users
* Secrets are escaped in stored/displayed logs when running on master and agents.
* Console annotations work as they work for common Jenkins instances
* Log blocks are collapsible in the _Console_ screen
* Origin container ID of every message is visible in Kibana (if you have set that up) via sender field

The demo can be run in Docker Compose,
ELK stack is provided by the [sebp/elk](https://hub.docker.com/r/sebp/elk/)  image in this case.

## Prerequisites

* Docker and Docker Compose are installed

## Building demo

To build the demo...

1. Go to the repository root, run `mvn clean package` to build Jenkins Custom WAR Packager
2. Change directory to the demo root
3. Run `make build`

First build may take a while, because the packager will need to checkout and build 
many repositories.

## Running demo

1. Run `make run`. It will spin up the demo with predefined environment.
   Jenkins will be available on the port 8080, credentials: `admin/admin`
2. If you want to run demo jobs on the agent, 
also run `docker-compose up agent` in a separate terminal window
3. In order to access the instance, use the "admin/admin" credentials.
4. Run one of the demo jobs.   
5. Browse logs
  * Classic Log action queries data from Elasticsearch
  * There is a _Log (Kibana)_ action in runs, which shows Kibana. 
  * In order to see Kibana logs, you will need to configure the default index in the 
    embedded page once Jenkins starts up. Use `logstash/` as a default index and 
    `@timestamp` as data source

## Manual run

This guideline allows to run the demo locally.
Only Logstash will be preconfigured.

1. Run `docker run -p 5601:5601 -p 9200:9200 -p 5044:5044 -it --name elk sebp/elk:es241_l240_k461` 
to start the Docker container to to expose ports
2. Run Jenkins using `JENKINS_HOME=$(pwd)/work java -jar tmp/output/target/external-task-logging-elk-2.107.3-elk-SNAPSHOT.war --httpPort=8080 --prefix=/jenkins` 
(or just `run run.sh`).
  * If needed, the demo can be configured by setting system properties
  * `elasticsearch.host` - host, defaults to `http://elk`
  * `elasticsearch.port` - Elasticsearch port, defaults to `9200`
  * `logstash.key` - Path to the root index/key for logging, defaults to `/logstash/logs`
  * `elasticsearch.username` and `elasticsearch.password` - 
3. Pass through the installation Wizard
4. Create a Pipeline job with some logging (e.g. `echo` commands), run it
5. Browse logs (see above)
Demo with POM input
===================

Jenkins WAR Packager Demo. All-latest core
===

This demo builds a Jenkins WAR which includes...

* Master branch of the Jenkins core
* Latest versions of Stapler, Remoting and XStream
* Latest versions of some modules (full list - TODO)
  * Some agent installer modules have obsolete tooling, they need to be updated before inclusion
* Latest version of Lib Task Reactor
* Docker Packaging for the build

Limitations:

* Only component JARs are updated, the builder does not update dependencies
* WAR Packager is able to replace/add libs to WEB-INF/lib only, components
like Extras Executable War cannot be updated right now


### Usage

To build the demo just run the `sh build.sh` command.
It will produce a `tmp/output/target/jenkins-all-latest-1.0-SNAPSHOT.war` file.
You can run this file as a common Jenkins WAR file.
Docker Package for Custom WAR Packager Environment
===

This image packages all tools needed by Custom WAR Packager to operate correctly.
It **DOES NOT** include the Custom WAR Packager itself, the tool should be retrieved from a Maven plugin.

### Usage

The image can be used within Jenkins Pipeline definitions.
In the [Custom WAR Packager CI Demo](https://github.com/oleg-nenashev/jenkins-custom-war-packager-ci-demo) uses this image from the 'docker' label
(the agent is provisioned by a Cloud plugin like Kubernetes or Docker plugin).

### Building Image

```sh
docker build -t onenashev/custom-war-packager-builder .
```
