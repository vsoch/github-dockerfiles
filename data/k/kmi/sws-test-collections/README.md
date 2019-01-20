# Semantic Web Services Test Collection

This project contains shared resources used for testing semantic web services technologies. These test resources are a collection of
pre-existing and derived test collections produced by a number of researchers. We do not claim ownership and include them herein
solely for the purposes of testing, research, and development.

These pre-existing resources have solely been modified in order to better support their use within automated
testing of software. In particular, to avoid requiring root privileges when running these tests we have modified
all references to service files and ontologies to a port higher than 1024 as opposed to the original port 80.
The rest has remained untouched.

## Test Collection Docker Container

The test collection has been wrapped as a [Docker](https://www.docker.com) container with all resources deployed.
This should allow you to easily launch a server with the test collections deployed for testing purposes.
 
In order to use it simply run:

```
docker run -d -p 8000:80 openuniversity/sws-test-collections
```

This will automatically fetch the container from the Docker hub and launch it.
Once launched, the entire test collection would be served at [http://127.0.0.1:8000](http://127.0.0.1:8000)
If you are in Mac, the test collection will be served at DOCKER_HOST:8000 instead so you will need to do an additional mapping of these ports to your local machine.

```
boot2docker ssh -L 8000:localhost:8000
```

See [this document](https://github.com/boot2docker/boot2docker/blob/master/doc/WORKAROUNDS.md#port-forwarding-on-steroids) for more details on port forwarding with boot2docker. 

If you have modified the resources or you want to build the container locally you may do so as follows:

```
docker build -t container-name .
```

and then you may launch the container as follows:

```
docker run -d -p 8000:80 container-name
```

## Using the Test Collection in Java

You may use these test resources within a Java project by adding the jar to the classpath. 
Below you have an example on how to do so with maven. Note, that the example below filters the resources to use (see the 'includes' clause)


```
<!-- Obtain shared test resources and unpack them -->
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-dependency-plugin</artifactId>
    <version>2.8</version>
    <executions>
        <execution>
            <id>resource-dependencies</id>
            <phase>process-test-resources</phase>
            <goals>
                <goal>unpack-dependencies</goal>
            </goals>
            <configuration>
                <includeGroupIds>uk.ac.open.kmi.test-collections</includeGroupIds>
                <includeArtifactIds>sws-test-collections</includeArtifactIds>
                <outputDirectory>${project.build.testOutputDirectory}</outputDirectory>
                <includes>services/OWLS-1.1/*.owls</includes>
            </configuration>
        </execution>
    </executions>
</plugin>

```

## Included Test Collections

### OWLS-TC3-MSM

 Test collection automatically derived from the OWL-S TC3 using the transformer provided by msm4j-owls-transformer.
 Should changes occur to this transformer, the collection should be updated accordingly to reflect them.
 At the moment only the Turtle version has been generated although other RDF serialisations could be generated.

### Jena Geography Dataset (JGD)

Taken from: http://fusion.cs.uni-jena.de/professur/jgd

A dataset of about 200 geography services that have been gathered from web sites like seekda.com, xmethods.com,
webservicelist.com, programmableweb.com, and geonames.org. The dataset has been built for the retrieval of
(semantic) web service technology.

These services have been annotated by ourselves for the purposes of testing the support for discovery.
Annotations are provided for WSDL files using SAWSDL, and for HTML files using hRESTS.

JGD Collection Authors:
Ulrich Küster
(Institut für Informatik Friedrich-Schiller-Universität Jena)

Annotation Authors:
Jacek Kopecky
Carlos Pedrinaci
(Knowledge Media Institute - The Open University)


Additionally this module is automatically enriched with 3rd parties' datasets automatically downloaded from the Internet.

### OWLS-TC3

 Taken from: http://projects.semwebcentral.org/projects/owls-tc/

 OWLS-TC is a OWL-S service retrieval test collection to support the evaluation of the performance of OWL-S
 semantic Web service matchmaking algorithms.

 Authors:
 Matthias Klusch
 Patrick Kapahnke
 Benedikt Fries
 Mahboob Alam Khalid
 Martin Vasileski

 (German Research Center for Artificial Intelligence)

### SAWSDL-TC3-WSDL11

 Taken from: http://projects.semwebcentral.org/projects/sawsdl-tc/

 Third release of the SAWSDL service retrieval test collection named SAWSDL-TC. The collection is intended to support
 the evaluation of the performance of SAWSDL service matchmaking algorithms. SAWSDL-TC has been semi-automatically
 derived from OWLS-TC 4

 Authors:
 Matthias Klusch
 Patrick Kapahnke
 Benedikt Fries
 Mahboob Alam Khalid
 Martin Vasileski

### Web Service Contest 2008
 
 This module obtains an adapted version of this dataset from: http://iserve.kmi.open.ac.uk/datasets/composit-wsc08.zip

 This version was modified by Pablo Rodriguez Mier (CITIUS - University of Santiago de Compostela). The modified version
 includes the dataset used for evaluating composition engines that exploit semantic descriptions, adapted such that the
 taxonomies provided are captured in OWL.

 Original datasets from the WSC'08
 http://cec2008.cs.georgetown.edu/wsc08/

# License
 
 The packaged test collection is based on the datasets listed above. The actual modifications to simplify its use
 within programs and automated software tests is Licensed under GPLv3.


 Semantic Web Services Test Collection Package
 Copyright (C) 2008-2014 Knowledge Media Institute

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.
