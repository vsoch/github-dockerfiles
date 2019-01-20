<!--
  Licensed to the Apache Software Foundation (ASF) under one or more
  contributor license agreements.  See the NOTICE file distributed with
  this work for additional information regarding copyright ownership.
  The ASF licenses this file to You under the Apache License, Version 2.0
  (the "License"); you may not use this file except in compliance with
  the License.  You may obtain a copy of the License at
      http://www.apache.org/licenses/LICENSE-2.0
  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->
# NiFi Registry Ranger extension

This extension provides `org.apache.nifi.registry.ranger.RangerAuthorizer` class for NiFi Registry to authorize user requests by access policies defined at [Apache Ranger](https://ranger.apache.org/).

## Prerequisites

* Apache Ranger 1.2.0 or later is needed.

## How to install

### Enable Ranger extension at NiFi Registry build

In order to enable Ranger extension when you build NiFi Registry, specify `include-ranger` profile with a maven install command:

```
cd nifi-registry
mvn clean install -Pinclude-ranger
```

Then the extension will be installed at `${NIFI_REG_HOME}/ext/ranger` directory.

### Add Ranger extension to existing NiFi Registry

Alternatively, you can add Ranger extension to an existing NiFi Registry.
To do so, build the extension with the following command:

```
cd nifi-registry
mvn clean install -f nifi-registry-extensions/nifi-registry-ranger
```

The extension zip will be created as `nifi-registry-extensions/nifi-registry-ranger-extension/target/nifi-registry-ranger-extension-xxx-bin.zip`.

Unzip the file into arbitrary directory so that NiFi Registry can use, such as `${NIFI_REG_HOME}/ext/ranger`.
For example:

```
mkdir -p ${NIFI_REG_HOME}/ext/ranger
unzip -d ${NIFI_REG_HOME}/ext/ranger nifi-registry-extensions/nifi-registry-ranger-extension/target/nifi-registry-ranger-extension-xxx-bin.zip
```

## NiFi Registry Configuration

In order to use this extension, following NiFi Registry files need to be configured.

### nifi-registry.properties

```
# Specify Ranger extension dir
nifi.registry.extension.dir.ranger=./ext/ranger/lib
# Specify Ranger authorizer identifier, which is defined at authorizers.xml
nifi.registry.security.authorizer=ranger-authorizer
```

### authorizers.xml

Add following `authorizer` element:
```
    <authorizer>
        <identifier>ranger-authorizer</identifier>
        <class>org.apache.nifi.registry.ranger.RangerAuthorizer</class>
        <property name="Ranger Service Type">nifi-registry</property>

        <property name="User Group Provider">file-user-group-provider</property>

        <!-- Specify Ranger service name to use -->
        <property name="Ranger Application Id">nifi-registry-service-name</property>

        <!--
            Specify configuration file paths for Ranger plugin.
            See the XML files bundled with this extension for further details.
         -->
        <property name="Ranger Security Config Path">./ext/ranger/conf/ranger-nifi-registry-security.xml</property>
        <property name="Ranger Audit Config Path">./ext/ranger/conf/ranger-nifi-registry-audit.xml</property>

        <!--
            Specify user identity that is used by Ranger to access NiFi Registry.
            This property is used by NiFi Registry for Ranger to get available NiFi Registry policy resource identifiers.
            The configured user can access NiFi Registry /policies/resources REST endpoint regardless of configured access policies.
            Ranger uses available policies for user input suggestion at Ranger policy editor UI.
        -->
        <property name="Ranger Admin Identity">ranger@NIFI</property>

        <!--
            Specify if target Ranger is Kerberized.
            If set to true, NiFi Registry will use the principal and keytab defined at nifi-registry.properties:
            - nifi.registry.kerberos.service.principal
            - nifi.registry.kerberos.service.keytab.location

            The specified credential is used to access Ranger API, and to write audit logs into HDFS (if enabled).

            At Ranger side, the configured user needs to be added to 'policy.download.auth.users' property, see Ranger configuration section below.

            Also, ranger-nifi-registry-security.xml needs additional "xasecure.add-hadoop-authorization = true" configuration.
        -->
        <property name="Ranger Kerberos Enabled">false</property>

    </authorizer>
```

## Ranger Configuration

At Ranger side, add a NiFi Registry service. NiFi Registry service has following configuration properties:

- NiFi Registry URL: Specify corresponding NiFi Registry URL that will be managed by this Ranger service. E.g. `https://nifi-registry.example.com:18443/nifi-registry-api/policies/resources`
- Authentication Type: Should be `SSL`. Ranger authenticates itself to NiFi Registry by X.509 client certificate in the configured Keystore.
- Keystore: Specify a Keystore filepath to use for X.509 client certificate.
- Keystore Type: Specify the type of Keystore. E.g. `JKS`
- Keystore Password: Specify the password of Keystore.
- Truststore: Specify a Truststore filepath to verify NiFi Registry server certificate.
- Truststore Type: Specify the type of Truststore. E.g. `JKS`
- Truststore Password: Specify the password of Truststore.
- Add New Configurations:
  - policy.download.auth.users: Required if Ranger is Kerberized.
    Specify the NiFi Registry user to download policies,
    which is configured by 'nifi.registry.kerberos.service.principal' at nifi-registry.properties,
    when NiFi Registry Ranger authorizer is configured as 'Ranger Kerberos Enabled' to true.
<!--
  Licensed to the Apache Software Foundation (ASF) under one or more
  contributor license agreements.  See the NOTICE file distributed with
  this work for additional information regarding copyright ownership.
  The ASF licenses this file to You under the Apache License, Version 2.0
  (the "License"); you may not use this file except in compliance with
  the License.  You may obtain a copy of the License at
      http://www.apache.org/licenses/LICENSE-2.0
  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->
# Test Keys

The automated security tests require keys and certificates for TLS connections. 
The keys in this directory can be used for that purpose.

***

**NOTICE**: This directory contains keys and certificates for *development and testing* purposes only.

**Never use these keystores and truststores in a real-world scenario where actual security is needed.** 

The CA and private keys (including their protection passwords) have been published on the Internet, so they should never be trusted.

***  

## Directory Contents

### Certificate Authority (CA)

| Hostname / DN | File | Description | Format | Password |
| --- | --- | --- | --- | --- |
| - | ca-cert.pem | CA public cert | PEM (unencrypted) | N/A |
| - | ca-key.pem | CA private (signing) key | PEM | password |
| - | ca-ts.jks | CA cert truststore (shared by clients and servers) | JKS | password |
| - | ca-ts.p12 | CA cert truststore (shared by clients and servers) | PKCS12 | password |
| registry, localhost | registry-cert.pem | NiFi Registry server public cert | PEM (unencrypted) | N/A |
| registry, localhost | registry-key.pem | NiFi Registry server private key | PEM | password |
| registry, localhost | registry-ks.jks | NiFi Registry server key/cert keystore | JKS | password |
| registry, localhost | registry-ks.p12 | NiFi Registry server key/cert keystore | PKCS12 | password |
| CN=user1, OU=nifi | user1-cert.pem | client (user="user1") public cert | PEM (unencrypted) | N/A |
| CN=user1, OU=nifi | user1-key.pem | client (user="user1") private key | PEM | password |
| CN=user1, OU=nifi | user1-ks.jks | client (user="user1") key/cert keystore | JKS | password |
| CN=user1, OU=nifi | user1-ks.p12 | client (user="user1") key/cert keystore | PKCS12 | password |

## Generating Additional Test Keys/Certs

If we need to add a service or user to our test environment that requires a cert signed by the same CA, here are the steps for generating additional keys for this directory that are signed by the same CA key.

Requirements:

- docker
- keytool (included with Java)
- openssl (included/available on most platforms)

If you do not have docker, you can substitute the nifi-toolkit binary, which is available for download from https://nifi.apache.org and should run on any platform with Java 1.8. 

### New Service Keys

The steps for generating a new service key/cert pair are (using `proxy` as the example service):

```
# make working directory
WD="/tmp/test-keys-$(date +"%Y%m%d-%H%M%S")"
mkdir "$WD"
cd "$WD"

# copy existing CA key/cert pair to working directory, rename to default tls-toolkit names
cp /path/to/nifi-registry/nifi-registry-core/nifi-registry-web-api/src/test/resources/keys/ca-key.pem ./nifi-key.key
cp /path/to/nifi-registry/nifi-registry-core/nifi-registry-web-api/src/test/resources/keys/ca-cert.pem ./nifi-cert.pem

# use NiFi Toolkit Docker image to generate new keys/certs
docker run -v "$WD":/tmp -w /tmp apache/nifi-toolkit:latest tls-toolkit standalone \
      --hostnames proxy \
      --subjectAlternativeNames localhost \
      --nifiDnSuffix ", OU=nifi" \
      --keyStorePassword password \
      --trustStorePassword password \
      --days 9999 \
      -O

# switch to output directory, create final output directory
cd "$WD"
mkdir keys

# copy new service key/cert to final output dir in all formats
keytool -importkeystore \
      -srckeystore proxy/keystore.jks -srcstoretype jks -srcstorepass password -srcalias nifi-key \
      -destkeystore keys/proxy-ks.jks -deststoretype jks -deststorepass password -destalias proxy-key
keytool -importkeystore \
      -srckeystore keys/proxy-ks.jks -srcstoretype jks -srcstorepass password \
      -destkeystore keys/proxy-ks.p12 -deststoretype pkcs12 -deststorepass password
openssl pkcs12 -in keys/proxy-ks.p12 -passin pass:password -out keys/proxy-key.pem -passout pass:password
openssl pkcs12 -in keys/proxy-ks.p12 -passin pass:password -out keys/proxy-cert.pem -nokeys

echo
echo "New keys written to ${WD}/keys"
echo "Copy to NiFi Registry test keys dir by running: "
echo "    cp \"$WD/keys/*\" /path/to/nifi-registry/nifi-registry-core/nifi-registry-web-api/src/test/resources/keys/"
```

You can verify the contents of the new keystore (and that the signature is done by the correct CA) using the following command:

    keytool -list -v -keystore "$WD/keys/proxy-ks.jks" -storepass password

If you are satisfied with the results, you can copy the files from `/tmp/test-keys-YYYYMMDD-HHMMSS/keys` to this directory:
 
    cp "$WD/keys/*" /path/to/nifi-registry/nifi-registry-core/nifi-registry-web-api/src/test/resources/keys/

### New Client or User Keys

The steps for generating a new user key/cert pair are (using `user2` as the example user):

```
# make working directory
WD="/tmp/test-keys-$(date +"%Y%m%d-%H%M%S")"
mkdir "$WD"
cd "$WD"

# copy existing CA key/cert pair to working directory, rename to default tls-toolkit names
cp /path/to/nifi-registry/nifi-registry-core/nifi-registry-web-api/src/test/resources/keys/ca-key.pem ./nifi-key.key
cp /path/to/nifi-registry/nifi-registry-core/nifi-registry-web-api/src/test/resources/keys/ca-cert.pem ./nifi-cert.pem

# use NiFi Toolkit Docker image to generate new keys/certs
docker run -v "$WD":/tmp -w /tmp apache/nifi-toolkit:latest tls-toolkit standalone \
      --clientCertDn "CN=user2, OU=nifi" \
      --clientCertPassword password \
      --days 9999 \
      -O

# switch to output directory, create final output directory
cd "$WD"
mkdir keys

# transform tls-toolkit output to final output
keytool -importkeystore \
      -srckeystore CN=user2_OU=nifi.p12 -srcstoretype PKCS12 -srcstorepass password -srcalias nifi-key \
      -destkeystore keys/user2-ks.jks -deststoretype JKS -deststorepass password -destalias user2-key
keytool -importkeystore \
      -srckeystore keys/user2-ks.jks -srcstoretype jks -srcstorepass password \
      -destkeystore keys/user2-ks.p12 -deststoretype pkcs12 -deststorepass password
openssl pkcs12 -in keys/user2-ks.p12 -passin pass:password -out keys/user2-key.pem -passout pass:password
openssl pkcs12 -in keys/user2-ks.p12 -passin pass:password -out keys/user2-cert.pem -nokeys

echo
echo "New keys written to ${WD}/keys"
echo "Copy to NiFi Registry test keys dir by running: "
echo "    cp \"$WD/keys/*\" /path/to/nifi-registry/nifi-registry-core/nifi-registry-web-api/src/test/resources/keys/"
```

You can verify the contents of the new keystore (and that the signature is done by the correct CA) using the following command:

    keytool -list -v -keystore "$WD/keys/user2-ks.jks" -storepass password

If you are satisfied with the results, you can copy the files from `/tmp/test-keys-YYYYMMDD-HHMMSS/keys` to this directory:
 
    cp "$WD/keys/*" /path/to/nifi-registry/nifi-registry-core/nifi-registry-web-api/src/test/resources/keys/


## Regenerating All Test Keys/Certs

In case you need to regenerate this entire directory, here are the steps that were used to first create it. 
Follow these steps in order to recreate it.

Requirements:

- docker
- keytool (included with Java)
- openssl (included/available on most platforms)

If you do not have docker, you can substitute the nifi-toolkit binary, which is available for download from https://nifi.apache.org and should run on any platform with Java 1.8. 

The steps for regenerating these test keys are:

```
# make working directory
WD="/tmp/test-keys-$(date +"%Y%m%d-%H%M%S")"
mkdir "$WD"
cd "$WD"

# use NiFi Toolkit Docker image to generate new keys/certs
docker run -v "$WD":/tmp -w /tmp apache/nifi-toolkit:latest tls-toolkit standalone \
      --certificateAuthorityHostname "Test CA (Do Not Trust)" \
      --hostnames registry \
      --subjectAlternativeNames localhost \
      --nifiDnSuffix ", OU=nifi" \
      --keyStorePassword password \
      --trustStorePassword password \
      --clientCertDn "CN=user1, OU=nifi" \
      --clientCertPassword password \
      --days 9999 \
      -O

# switch to output directory, create final output directory
cd "$WD"
mkdir keys

# copy CA key/cert to final output dir in all formats
cp nifi-key.key keys/ca-key.pem
cp nifi-cert.pem keys/ca-cert.pem
keytool -importkeystore \
      -srckeystore registry/truststore.jks -srcstoretype jks -srcstorepass password -srcalias nifi-cert \
      -destkeystore keys/ca-ts.jks -deststoretype jks -deststorepass password -destalias ca-cert
keytool -importkeystore \
      -srckeystore keys/ca-ts.jks -srcstoretype jks -srcstorepass password \
      -destkeystore keys/ca-ts.p12 -deststoretype pkcs12 -deststorepass password

# copy registry service key/cert to final output dir in all formats
keytool -importkeystore \
      -srckeystore registry/keystore.jks -srcstoretype jks -srcstorepass password -srcalias nifi-key \
      -destkeystore keys/registry-ks.jks -deststoretype jks -deststorepass password -destalias registry-key
keytool -importkeystore \
      -srckeystore keys/registry-ks.jks -srcstoretype jks -srcstorepass password \
      -destkeystore keys/registry-ks.p12 -deststoretype pkcs12 -deststorepass password
openssl pkcs12 -in keys/registry-ks.p12 -passin pass:password -out keys/registry-key.pem -passout pass:password
openssl pkcs12 -in keys/registry-ks.p12 -passin pass:password -out keys/registry-cert.pem -nokeys

# copy user1 client key/cert to final output dir in all formats
keytool -importkeystore \
      -srckeystore CN=user1_OU=nifi.p12 -srcstoretype PKCS12 -srcstorepass password -srcalias nifi-key \
      -destkeystore keys/user1-ks.jks -deststoretype JKS -deststorepass password -destkeypass password -destalias user1-key
keytool -importkeystore \
      -srckeystore keys/user1-ks.jks -srcstoretype jks -srcstorepass password \
      -destkeystore keys/user1-ks.p12 -deststoretype pkcs12 -deststorepass password
openssl pkcs12 -in keys/user1-ks.p12 -passin pass:password -out keys/user1-key.pem -passout pass:password
openssl pkcs12 -in keys/user1-ks.p12 -passin pass:password -out keys/user1-cert.pem -nokeys

echo
echo "New keys written to ${WD}/keys"
echo "Copy to NiFi Registry test keys dir by running: "
echo "    cp -f \"$WD/keys/*\" /path/to/nifi-registry/nifi-registry-core/nifi-registry-web-api/src/test/resources/keys/"
```

You should now have a `/tmp/test-keys-YYYYMMDD-HHMMSS/keys` directory with all the necessary keys for testing with various tools.

You can verify the contents of a keystore using the following command:

    keytool -list -v -keystore "$WD/keys/registry-ks.jks" -storepass password

If you are satisfied with the results, you can copy the files from `/tmp/test-keys-YYYYMMDD-HHMMSS/keys` to this directory:

    cp -f "$WD/keys/*" /path/to/nifi-registry/nifi-registry-core/nifi-registry-web-api/src/test/resources/keys/
<!--
  Licensed to the Apache Software Foundation (ASF) under one or more
  contributor license agreements.  See the NOTICE file distributed with
  this work for additional information regarding copyright ownership.
  The ASF licenses this file to You under the Apache License, Version 2.0
  (the "License"); you may not use this file except in compliance with
  the License.  You may obtain a copy of the License at
      http://www.apache.org/licenses/LICENSE-2.0
  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->

# Docker Image Quickstart

## Capabilities
This image currently supports running in standalone mode either unsecured or with user authentication provided through:
   * [Two-Way SSL with Client Certificates](https://nifi.apache.org/docs/nifi-registry-docs/html/administration-guide.html#security-configuration)
   * [Lightweight Directory Access Protocol (LDAP)](https://nifi.apache.org/docs/nifi-registry-docs/html/administration-guide.html#ldap_identity_provider)
   
## Building
The Docker image can be built using the following command:

    # user @ puter in ~/path/to/apache/nifi-registry/nifi-registry-docker/dockerhub    
    $ docker build -t apache/nifi-registry:latest .

This will result in an image tagged apache/nifi:latest

    $ docker images
    > REPOSITORY               TAG           IMAGE ID            CREATED                  SIZE
    > apache/nifi-registry     latest        751428cbf631        A long, long time ago    342MB
    
**Note**: The default version of NiFi Registry specified by the Dockerfile is typically that of one that is unreleased if working from source.
To build an image for a prior released version, one can override the `NIFI_REGISTRY_VERSION` build-arg with the following command:
    
    $ docker build --build-arg NIFI_REGISTRY_VERSION={Desired NiFi Registry Version} -t apache/nifi-registry:latest .

There is, however, no guarantee that older versions will work as properties have changed and evolved with subsequent releases.
The configuration scripts are suitable for at least 0.1.0+.

## Running a container

### Standalone Instance, Unsecured
The minimum to run a NiFi Registry instance is as follows:

    docker run --name nifi-registry \
      -p 18080:18080 \
      -d \
      apache/nifi-registry:latest
      
This will provide a running instance, exposing the instance UI to the host system on at port 18080,
viewable at `http://localhost:18080/nifi-registry`.

You can also pass in environment variables to change the NiFi Registry communication ports and hostname using the Docker '-e' switch as follows:

    docker run --name nifi-registry \
      -p 19090:19090 \
      -d \
      -e NIFI_REGISTRY_WEB_HTTP_PORT='19090'
      apache/nifi-registry:latest

For a list of the environment variables recognised in this build, look into the .sh/secure.sh and .sh/start.sh scripts
        
### Standalone Instance, Two-Way SSL
In this configuration, the user will need to provide certificates and the associated configuration information.
Of particular note, is the `AUTH` environment variable which is set to `tls`.  Additionally, the user must provide an
the DN as provided by an accessing client certificate in the `INITIAL_ADMIN_IDENTITY` environment variable.
This value will be used to seed the instance with an initial user with administrative privileges.
Finally, this command makes use of a volume to provide certificates on the host system to the container instance.

    docker run --name nifi-registry \
      -v /path/to/tls/certs/localhost:/opt/certs \
      -p 18443:18443 \
      -e AUTH=tls \
      -e KEYSTORE_PATH=/opt/certs/keystore.jks \
      -e KEYSTORE_TYPE=JKS \
      -e KEYSTORE_PASSWORD=QKZv1hSWAFQYZ+WU1jjF5ank+l4igeOfQRp+OSbkkrs \
      -e TRUSTSTORE_PATH=/opt/certs/truststore.jks \
      -e TRUSTSTORE_PASSWORD=rHkWR1gDNW3R9hgbeRsT3OM3Ue0zwGtQqcFKJD2EXWE \
      -e TRUSTSTORE_TYPE=JKS \
      -e INITIAL_ADMIN_IDENTITY='CN=AdminUser, OU=nifi' \
      -d \
      apache/nifi-registry:latest

### Standalone Instance, LDAP
In this configuration, the user will need to provide certificates and the associated configuration information.  Optionally,
if the LDAP provider of interest is operating in LDAPS or START_TLS modes, certificates will additionally be needed.
Of particular note, is the `AUTH` environment variable which is set to `ldap`.  Additionally, the user must provide a
DN as provided by the configured LDAP server in the `INITIAL_ADMIN_IDENTITY` environment variable. This value will be 
used to seed the instance with an initial user with administrative privileges.  Finally, this command makes use of a 
volume to provide certificates on the host system to the container instance.

#### For a minimal, connection to an LDAP server using SIMPLE authentication:

    docker run --name nifi-registry \
      -v /path/to/tls/certs/localhost:/opt/certs \
      -p 18443:18443 \
      -e AUTH=ldap \
      -e KEYSTORE_PATH=/opt/certs/keystore.jks \
      -e KEYSTORE_TYPE=JKS \
      -e KEYSTORE_PASSWORD=QKZv1hSWAFQYZ+WU1jjF5ank+l4igeOfQRp+OSbkkrs \
      -e TRUSTSTORE_PATH=/opt/certs/truststore.jks \
      -e TRUSTSTORE_PASSWORD=rHkWR1gDNW3R9hgbeRsT3OM3Ue0zwGtQqcFKJD2EXWE \
      -e TRUSTSTORE_TYPE=JKS \
      -e INITIAL_ADMIN_IDENTITY='cn=nifi-admin,dc=example,dc=org' \
      -e LDAP_AUTHENTICATION_STRATEGY='SIMPLE' \
      -e LDAP_MANAGER_DN='cn=ldap-admin,dc=example,dc=org' \
      -e LDAP_MANAGER_PASSWORD='password' \
      -e LDAP_USER_SEARCH_BASE='dc=example,dc=org' \
      -e LDAP_USER_SEARCH_FILTER='cn={0}' \
      -e LDAP_IDENTITY_STRATEGY='USE_DN' \
      -e LDAP_URL='ldap://ldap:389' \
      -d \
      apache/nifi-registry:latest

#### The following, optional environment variables may be added to the above command when connecting to a secure  LDAP server configured with START_TLS or LDAPS

    -e LDAP_TLS_KEYSTORE: ''
    -e LDAP_TLS_KEYSTORE_PASSWORD: ''
    -e LDAP_TLS_KEYSTORE_TYPE: ''
    -e LDAP_TLS_TRUSTSTORE: ''
    -e LDAP_TLS_TRUSTSTORE_PASSWORD: ''
    -e LDAP_TLS_TRUSTSTORE_TYPE: ''

### The following, optional environment variables can be used to configure the database

| nifi-registry.properties entry         | Variable                   |
|----------------------------------------|----------------------------|
| nifi.registry.db.url                   | NIFI_REGISTRY_DB_URL       |
| nifi.registry.db.driver.class          | NIFI_REGISTRY_DB_CLASS     |
| nifi.registry.db.driver.directory      | NIFI_REGISTRY_DB_DIR       |
| nifi.registry.db.driver.username       | NIFI_REGISTRY_DB_USER      |
| nifi.registry.db.driver.password       | NIFI_REGISTRY_DB_PASS      |
| nifi.registry.db.driver.maxConnections | NIFI_REGISTRY_DB_MAX_CONNS |
| nifi.registry.db.sql.debug             | NIFI_REGISTRY_DB_DEBUG_SQL |

#### The following, optional environment variables may be added to configure flow persistence provider.

| Environment Variable           | Configuration Property               |
|--------------------------------|--------------------------------------|
| NIFI_REGISTRY_FLOW_STORAGE_DIR | Flow Storage Directory               |
| NIFI_REGISTRY_FLOW_PROVIDER    | (Class tag); valid values: git, file |
| NIFI_REGISTRY_GIT_REMOTE       | Remote to Push                       |
| NIFI_REGISTRY_GIT_USER         | Remote Access User                   |
| NIFI_REGISTRY_GIT_PASSWORD     | Remote Access Password               |

<!--
  Licensed to the Apache Software Foundation (ASF) under one or more
  contributor license agreements.  See the NOTICE file distributed with
  this work for additional information regarding copyright ownership.
  The ASF licenses this file to You under the Apache License, Version 2.0
  (the "License"); you may not use this file except in compliance with
  the License.  You may obtain a copy of the License at
      http://www.apache.org/licenses/LICENSE-2.0
  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->
# Apache NiFi Registry

Registry—a subproject of Apache NiFi—is a complementary application that provides a central location for storage and management of shared resources across one or more instances of NiFi and/or MiNiFi.

## Table of Contents

- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [Getting Help](#getting-help)
- [License](#license)

## Requirements

* Java 1.8 (above 1.8.0_45)

## Getting Started

To start NiFi Registry:
- [linux/osx] execute bin/nifi-registry.sh start
- [windows] execute bin/run-nifi-registry.bat
- Direct your browser to http://localhost:18080/nifi-registry/

## Getting Help
If you have questions, you can reach out to our mailing list: dev@nifi.apache.org
([archive](http://mail-archives.apache.org/mod_mbox/nifi-dev)).
We're also often available in IRC: #nifi on
[irc.freenode.net](http://webchat.freenode.net/?channels=#nifi) 
and in #NiFi on [ASF HipChat](https://www.hipchat.com/gzh2m5YML).

## License

Except as otherwise noted this software is licensed under the
[Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0.html)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

