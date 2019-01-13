Example Image with a  WLS Domain
================================
This Dockerfile extends the Oracle WebLogic image by creating a sample WLS 12.2.1.3 domain and cluster.

Utility scripts are copied into the image, enabling users to plug Node Manager automatically into the Administration Server running on another container.

### Admin Password

On the first startup of the container, a random password will be generated for the administration of the domain. You can find this password in the output line:

`Oracle WebLogic Server auto generated Admin password:`

If you need to find the password at a later time, grep for `password` in the Docker logs generated during the startup of the container. To look at the Docker container logs, run:

    $ docker logs --details <Container-id>

**NOTE:** The administration password can be passed in at runtime by using the `-e` option, and override the generated password.  If using the auto-generated password, please make sure to pass the password into the Managed Server container at runtime.

### How to Build and Run

**NOTE:** First make sure you have built `oracle/weblogic:12.2.1.3-developer`.

You can define the following environment variables at Docker runtime using the `-e` option  on the command line or in the `domain.properties` file. These environmental variables need to be set for the Administration Server as well as for the Managed Servers.

* Admin Password:  `ADMIN_PASSWORD`  Auto Generated
* Admin Username:  `ADMIN_USERNAME`  `weblogic`      
* Admin Name:      `ADMIN_NAME`       `AdminServer`  
* Domain Name:     `DOMAIN_NAME`      `base_domain`  
* Admin Port:      `ADMIN_PORT`       `7001`          
* Admin Host:      `ADMIN_HOST`       `wlsadmin`    
* Cluster Name:    `CLUSTER_NAME`   `DockerCluster`
* Debug Flag:       `DEBUG_FLAG`      `false`         
* Production Mode:  `PRODUCTION_MODE` `dev`            
* Managed Server Name:  `MS_NAME`      Generated    
* Managed Server Port: `MS_PORT`       `8001`          
* Node Manager Name:  `NM_NAME`        Generated      


To build this sample, run:

        $ docker build -t 12213-domain .

**Important**: The domain directory needs to be externalized by using data volumes (`-v` option). The Administration Server as well as the Managed Servers need to read/write to the same `DOMAIN_HOME`.

To start the containerized Administration Server, run:

	$ docker run -d --name wlsadmin --hostname wlsadmin -p 7001:7001 --env-file ./container-scripts/domain.properties -e ADMIN_PASSWORD=<admin_password> -v <host directory>:/u01/oracle/user_projects 12213-domain

To start a containerized Managed Server (MS1) to self-register with the Administration Server above, run:

 	$ docker run -d --name MS1 --link wlsadmin:wlsadmin -p 8001:8001 --env-file ./container-scripts/domain.properties -e ADMIN_PASSWORD=<admin_password> -e MS_NAME=MS1 --volumes-from wlsadmin 12213-domain createServer.sh

To start a second Managed Server (MS2), run:

 	$ docker run -d --name MS2 --link wlsadmin:wlsadmin -p 8002:8001 --env-file ./container-scripts/domain.properties -e ADMIN_PASSWORD=<admin_password> -e MS_NAME=MS2 --volumes-from wlsadmin 12213-domain createServer.sh

The above scenario from this sample will give you a WebLogic domain with a cluster set up on a single host environment.

You may create more containerized Managed Servers by calling the `docker` command above for `createServer.sh` as long you link properly with the Administration Server. For an example of a multihost environment, see the sample `1221-multihost`.

# Copyright
Copyright (c) 2014-2018 Oracle and/or its affiliates. All rights reserved.
Example Image with a WLS Domain
===============================
This Dockerfile extends the Oracle WebLogic Server image by creating a sample WLS 12.2.1.3 domain and cluster. Utility scripts are copied into the image, enabling users to plug Node Manager automatically into the Administration Server running on another container.

The Oracle WebLogic Deploy Tooling (WDT) automates domain creation and application deployment.  The tool creates the domain using a declarative, metadata model describing the domain and applications (with their dependent resources). 

The Dockerfile uses the `createDomain` script from the WebLogic Deploy Tooling to create the domain from a text-based model file. More information about WDT is available in the README file for the WDT project in GitHub:

`https://github.com/oracle/weblogic-deploy-tooling`

### WDT Model File and Archive

This sample includes a basic WDT model, `simple-topology.yaml`, that describes the intended configuration of the domain within the Docker image. WDT models can be created and modified using a text editor, following the format and rule described in the README file for the WDT project in GitHub.

Another option is to use the WDT `discoverDomain` tool to create a model. This process is also described in the WDT project's README file. A user can use the tool to analyze an existing domain, and create a model based on its configuration. The user may choose to customize the model before using it to create a new Docker image.

Domain creation may require the deployment of applications and libraries. This is accomplished by creating a ZIP archive with a specific structure, then referencing those items in the model. This sample creates and deploys a simple ZIP archive containing a small application WAR. That archive is built in the sample directory prior to creating the Docker image.

When the WDT `discoverDomain` tool is used on an existing domain, a ZIP archive is created containing any necessary applications and libraries. The corresponding configuration for those applications and libraries is added to the model.

### How to Build and Run

**NOTE:** The image is based on a WebLogic Server image in the docker-images project: `oracle/weblogic:12.2.1.3-developer`. Build that image to your local repository before building this sample.  The WebLogic Deploy Tool installer is used to build this image.


This sample deploys a simple, one-page web application contained in a ZIP archive. This archive needs to be built (one time only) before building the Docker image.

    $ ./build-archive.sh

To build this sample, run:

    $ docker build \
          --build-arg WDT_MODEL=simple-topology.yaml \
          --build-arg WDT_ARCHIVE=archive.zip \
          --force-rm=true \
          -t 12213-domain-wdt .

This will use the model file and archive in the sample directory.

### How to Run 
In this sample each of the managed servers in the WebLogic domain have a Data Source deployed to them. We want to connect the Data Source to an Oracle Database running in a container. Pull the Oracle Database image from the Docker Store or the Oracle Container Registry.

    $ docker pull container-registry.oracle.com/database/enterprise:12.2.0.1

Follow the steps below:

Create the docker network for the WLS and Database containers to run

    $ docker network create -d bridge SampleNET

#### Run the Database container

To create a database container, use the environment file below to set the database name, domain and feature bundle.  The example environment file properties/env.txt is:

    DB_SID=InfraDB
    DB_PDB=InfraPDB1
    DB_DOMAIN=us.oracle.com
    DB_BUNDLE=basic

    $ docker run -d \
          --name InfraDB \ 
          --network=SampleNET \ 
          -p 1521:1521 \
          -p 5500:5500 \
          --env-file <sample-directory>/env.txt \
          -it \
          --shm-size="8g" \
          container-registry.oracle.com/database/enterprise:12.2.0.1


    Verify that the Database is running and healthy, the STATUS field shows (healthy) in the output of docker ps.

    The Database is created with the default password 'Oradoc_db1', to change the database password you must use sqlplus.  To run sqlplus pull the Oracle Instant Client from the Oracle Container Registry or the Docker Store, and run a sqlplus container with the following command:

    $ docker run -ti \
          --network=SampleNET \
          --rm container-registry.oracle.com/database/instantclient:12.2.0.1 \
          sqlplus sys/Oradoc_db1@InfraDB:1521/InfraDB.us.oracle.com AS SYSDBA

    SQL> alter user system identified by MYDBPasswd container=all;

Make sure you add the new Database password 'MYDBPassword' in the properties file properties/domain.properties DB_PASSWORD. Verify that you can connect to the Database:

    $ docker exec -ti InfraDB /u01/app/oracle/product/12.2.0/dbhome_1/bin/sqlplus system/MYDBPasswd@InfraDB:1521/InfraPDB1.us.oracle.com

    SQL> select * from Dual;

#### Run WebLogic Domain

To start the containerized Administration Server, run:

    $ docker run -d \
          --name wlsadmin \
          --hostname wlsadmin \
          --network=SampleNET \
          -p 7001:7001 \
          -v <sample-directory>/properties:/u01/oracle/properties 12213-domain-wdt

To start a containerized Managed Server (ms-1) to self-register with the Administration Server above, run:

    $ docker run -d \
          --name ms-1 \
          --link wlsadmin:wlsadmin \
          --network=SampleNET \
          -p 9001:9001 \
          -v <sample-directory>/properties:/u01/oracle/properties \
          -e MS_NAME=ms-1 12213-domain-wdt startManagedServer.sh

To start an additional Managed Server (in this example ms-2), run:

    $ docker run -d \
          --name ms-2 \
          --link wlsadmin:wlsadmin \
          --network=SampleNET \
          -p 9002:9001 \
          -v <sample-directory>/properties:/u01/oracle/properties \
          -e MS_NAME=ms-2 12213-domain-wdt startManagedServer.sh

The above scenario from this sample will give you a WebLogic domain with a dynamic cluster set up on a single host environment.

You may create more containerized Managed Servers by calling the `docker` command above for `startManagedServer.sh` as long you link properly with the Administration Server. For an example of a multihost environment, see the sample `1221-multihost`.

# Copyright
Copyright (c) 2018 Oracle and/or its affiliates. All rights reserved.
