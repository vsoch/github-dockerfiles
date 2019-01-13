Example of Image with WLS Domain
================================
This Dockerfile extends the Oracle WebLogic image by creating a sample empty domain.

Util scripts are copied into the image enabling users to plug NodeManager automatically into the AdminServer running on another container.

# How to build and run
First make sure you have built **oracle/weblogic:12.2.1-developer**. Now to build this sample, run:

        $ docker build -t 1221-domain --build-arg ADMIN_PASSWORD=welcome1 --build-arg ADMIN_NAME=WL_AdminServer .

To start the containerized Admin Server, run:

        $ docker run -d --name wlsadmin --hostname wlsadmin -p 7001:7001 1221-domain

To start a containerized Managed Server to self-register with the Admin Server above, run:

        $ docker run -d --link wlsadmin:wlsadmin -p 7002:7002 1221-domain createServer.sh

The above scenario from this sample will give you a WebLogic domain with a cluster setup, on a single host environment.

You may create more containerized Managed Servers by calling the `docker` command above for `createServer.sh` as long you link properly with the Admin Server. For an example of multihost enviornment, check the sample `1221-multihost`.

# Copyright
Copyright (c) 2014-2018 Oracle and/or its affiliates. All rights reserved.8
Example of Image with WLS Domain
================================
This Dockerfile extends the Oracle WebLogic image built under 1221-domain with tag name '1221-domain'

WLST Offline script are used during Docker image build phase to deploy the

- JDBC Data Source (Derby database information is picked up from the datasource.properties file)
- JMS artifacts (JMS Server, Queue etc).

# How to build and run
First make sure you have built sample image inside **1221-domain**. Now to build this sample, run:

        $ docker build -t 1221-domain-with-resources .

To start the Admin Server with the application automatically deployed, run:

        $ docker run -d -p 7001:7001 1221-domain-with-resources

You should now be able to see the Data Source and the JMS components

When configured to do JMS Persistance the persistent store should be mapped to a volume on the host. Map the data volume in the container to a volume on the host to preserve the store in case the container fails, this allows for a new JMS Server recover messages. To map the data volumes use this docker run sample:

        $ docker run -d -v host-volume:/u01/oracle/user_projects/domains/base_domain/PersistentStore-directory -p 7001:7001 1221-domain-with-resources


# Copyright
Copyright (c) 2018 Oracle and/or its affiliates. All rights reserved.
