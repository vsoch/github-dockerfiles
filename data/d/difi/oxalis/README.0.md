# Oxalis Legacy

This folder contains modules provided for convenience even though they are not actively maintained. # Oxalis Document Sniffer (Legacy)

This extension contains functionality provided to help users during introduction of SBDH in OpenPEPPOL.

As the introduction of SBDH is completed, and quite some time has passed, this extension will not receive further updates.
Users may expect this extension and its functionality to be removed from Oxalis as of version 4.2 or 5.0.# Example extension

This is an example extension providing a simple implementation of TransmissionVerifier to log each message (metadata only) to be verified.

This implementation consists of the following files:

* [LoggingTransmissionVerifier](src/main/java/no/difi/oxalis/ext/example/LoggingTransmissionVerifier.java) - The implementation.
* [ExampleModule](src/main/java/no/difi/oxalis/ext/example/ExampleModule.java) - Guice module to make the implementation known to Oxalis.
* [reference.conf](src/main/resources/reference.conf) - Configuration to register the Guice module during Oxalis startup.
* [pom.xml](pom.xml) - Maven configuration to build an extension using Maven.

Extensions are included in classpath as of Oxalis 4.0.0.
The best ways of deploying your Oxalis instance:

* WAR file - Build your own WAR file containing the Oxalis libraries and your extensions for deployment on your servers.
* Oxalis Server - Include extensions and additional libaries in the `ext` folder.
* Docker - Include extensions and additional libraries in `/oxalis/ext/`.

To enable the verifier implementation included in this extension must the following be included in the oxalis configuration file:

```properties
oxalis.transmission.verifier = logging
``` # Oxalis Distributions

Oxalis is provided in different distributions to allow users to easily adopt Oxalis into their environment.

The following distributions are available:

* **[Oxalis Distribution](/oxalis-dist/oxalis-distribution)** -
    The traditional distribution package of Oxalis.

* **[Oxalis Server](/oxalis-dist/oxalis-server)** - 
    Oxalis as an application needing only Java 8 to run. 
    This is the distribution used to create the Docker image. 

* **[Oxalis Standalone](/oxalis-dist/oxalis-standalone)** -
    Simple client for sending provided as a single java archive (jar).
    Suited for testing and small manual tasks.

* **[Oxalis WAR](/oxalis-dist/oxalis-war)** - 
    The traditional war distribution for application servers recreated to use Java Servlet 3.0 functionality.
    This is the distribution made available as `oxalis.war` in `oxalis-distribution`.# Oxalis Web Archive (Oxalis WAR)

The traditional war distribution for application servers recreated to use Java Servlet 3.0 functionality.
This is the distribution made available as `oxalis.war` in `oxalis-distribution`.

It is recommended to create your own web archive (war) if you need to change anything inside the one provided by this project.
The following is a Maven configuration file (`pom.xml`) for your own project where you may customize Oxalis to your needs without having to change any existing artifacts.
This allow for the convenient deployment of a single web archive including your own code.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <!-- Replace the following three values according to your preferences. -->
    <groupId>com.example.peppol</groupId>
    <artifactId>oxalis</artifactId>
    <version>1.0-SNAPSHOT</version>

    <!-- Create web archive. -->
    <packaging>war</packaging>

    <properties>
        <!-- Replace with 4.0.3 or newer. -->
        <oxalis.version>4.0.x</oxalis.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>no.difi.oxalis</groupId>
            <artifactId>oxalis-war</artifactId>
            <version>${oxalis.version}</version>
            <classifier>classes</classifier>
        </dependency>
        <!-- Any other extensions or libraries to be included. -->
    </dependencies>

    <build>
        <!-- Resulting file as oxalis.war. -->
        <finalName>oxalis</finalName>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-war-plugin</artifactId>
                <version>2.1.1</version>
                <configuration>
                    <!-- Allow building without web.xml. -->
                    <failOnMissingWebXml>false</failOnMissingWebXml>
                </configuration>
            </plugin>
        </plugins>
    </build>

</project>
```
# Hooks

* [Docker hub file](post_push)
