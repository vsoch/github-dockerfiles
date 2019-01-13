## Ansible Dockerfile


This repository contains **Dockerfile** of [Ansible](http://www.ansible.com/) for [Docker](https://www.docker.com/)'s [automated build](https://registry.hub.docker.com/u/dockerfile/ansible/) published to the public [Docker Hub Registry](https://registry.hub.docker.com/).


### Base Docker Image

* [dockerfile/python](http://dockerfile.github.io/#/python)


### Installation

1. Install [Docker](https://www.docker.com/).

2. Download [automated build](https://registry.hub.docker.com/u/dockerfile/ansible/) from public [Docker Hub Registry](https://registry.hub.docker.com/): `docker pull dockerfile/ansible`

   (alternatively, you can build an image from Dockerfile: `docker build -t="dockerfile/ansible" github.com/dockerfile/ansible`)


### Usage

    docker run -it --rm dockerfile/ansible

Ansible Examples
----------------

This repository contains examples and best practices for building Ansible Playbooks.

LAMP Stack + HAProxy: Example Playbooks
-----------------------------------------------------------------------------

- Requires Ansible 1.2
- Expects CentOS/RHEL 6 hosts

This example is an extension of the simple LAMP deployment. Here we'll install
and configure a web server with an HAProxy load balancer in front, and deploy
an application to the web servers. This set of playbooks also have the
capability to dynamically add and remove web server nodes from the deployment.
It also includes examples to do a rolling update of a stack without affecting
the service.

(To use this demonstration with Amazon Web Services, please use the "aws" sub-directory.)

You can also optionally configure a Nagios monitoring node.

### Initial Site Setup

First we configure the entire stack by listing our hosts in the 'hosts'
inventory file, grouped by their purpose:

		[webservers]
		webserver1
		webserver2
		
		[dbservers]
		dbserver
		
		[lbservers]
		lbserver
		
		[monitoring]
		nagios

After which we execute the following command to deploy the site:

		ansible-playbook -i hosts site.yml

The deployment can be verified by accessing the IP address of your load
balancer host in a web browser: http://<ip-of-lb>:8888. Reloading the page
should have you hit different webservers.

The Nagios web interface can be reached at http://<ip-of-nagios>/nagios/

The default username and password are "nagiosadmin" / "nagiosadmin".

### Removing and Adding a Node

Removal and addition of nodes to the cluster is as simple as editing the
hosts inventory and re-running:

        ansible-playbook -i hosts site.yml

### Rolling Update

Rolling updates are the preferred way to update the web server software or
deployed application, since the load balancer can be dynamically configured
to take the hosts to be updated out of the pool. This will keep the service
running on other servers so that the users are not interrupted.

In this example the hosts are updated in serial fashion, which means that
only one server will be updated at one time. If you have a lot of web server
hosts, this behaviour can be changed by setting the 'serial' keyword in
webservers.yml file.

Once the code has been updated in the source repository for your application
which can be defined in the group_vars/all file, execute the following
command:

	 ansible-playbook -i hosts rolling_update.yml

You can optionally pass: -e webapp_version=xxx to the rolling_update
playbook to specify a specific version of the example webapp to deploy.
LAMP Stack + HAProxy: Example Playbooks for Amazon Web Services
-----------------------------------------------------------------------------

- Requires Ansible 1.2
- Expects CentOS/RHEL 6 hosts

This example is an extension of the simple LAMP deployment. Here we'll install
and configure a web server with an HAProxy load balancer in front, and deploy
an application to the web servers. This set of playbooks also have the
capability to dynamically add and remove web server nodes from the deployment.
It also includes examples to do a rolling update of a stack without affecting
the service.

You can also optionally configure a Nagios monitoring node.

### Initial Site Setup

First, we provision the hosts neccessary for this demonstration using the included playbook, "demo-aws-launch.yml". This will provision the following instances, with the group structure specified below. The hosts are tagged via AWS EC2 tagging and the Ansible inventory sync script (or Tower) will create the appropriate groups from these tags.

		[tag_ansible_group_webservers]
		webserver1
		webserver2
		
		[tag_ansible_group_dbservers]
		dbserver
		
		[tag_ansible_group_lbservers]
		lbserver
		
		[tag_ansible_group_monitoring]
		nagios

After which we execute the following command to deploy the site:

		ansible-playbook -i ec2.py site.yml

The deployment can be verified by accessing the IP address of your load
balancer host in a web browser: http://<ip-of-lb>:8888. Reloading the page
should have you hit different webservers.

The Nagios web interface can be reached at http://<ip-of-nagios>/nagios/

The default username and password are "nagiosadmin" / "nagiosadmin".

### Removing and Adding a Node

Removal and addition of nodes to the cluster is as simple as creating new instances, syncing the
Ansible inventory and re-running:

        ansible-playbook -i ec2.py site.yml

### Rolling Update

Rolling updates are the preferred way to update the web server software or
deployed application, since the load balancer can be dynamically configured
to take the hosts to be updated out of the pool. This will keep the service
running on other servers so that the users are not interrupted.

In this example the hosts are updated in serial fashion, which means that
only one server will be updated at one time. If you have a lot of web server
hosts, this behaviour can be changed by setting the 'serial' keyword in
webservers.yml file.

Once the code has been updated in the source repository for your application
which can be defined in the group_vars/all file, execute the following
command:

	 ansible-playbook -i ec2.py rolling_update.yml

You can optionally pass: -e webapp_version=xxx to the rolling_update
playbook to specify a specific version of the example webapp to deploy.
## WordPress+Nginx+PHP-FPM+MariaDB Deployment

- Requires Ansible 1.2 or newer
- Expects CentOS/RHEL 7.x host/s

RHEL7 version reflects changes in Red Hat Enterprise Linux and CentOS 7:
1. Network device naming scheme has changed
2. iptables is replaced with firewalld
3. MySQL is replaced with MariaDB

These playbooks deploy a simple all-in-one configuration of the popular
WordPress blogging platform and CMS, frontend by the Nginx web server and the
PHP-FPM process manager. To use, copy the `hosts.example` file to `hosts` and 
edit the `hosts` inventory file to include the names or URLs of the servers
you want to deploy.

Then run the playbook, like this:

	ansible-playbook -i hosts site.yml

The playbooks will configure MariaDB, WordPress, Nginx, and PHP-FPM. When the run
is complete, you can hit access server to begin the WordPress configuration.

### Ideas for Improvement

Here are some ideas for ways that these playbooks could be extended:

- Parameterize the WordPress deployment to handle multi-site configurations.
- Separate the components (PHP-FPM, MySQL, Nginx) onto separate hosts and 
handle the configuration appropriately.
- Handle WordPress upgrades automatically.

We would love to see contributions and improvements, so please fork this
repository on GitHub and send us your changes via pull requests.Building a simple LAMP stack and deploying Application using Ansible Playbooks.
-------------------------------------------

These playbooks require Ansible 1.2.

These playbooks are meant to be a reference and starter's guide to building
Ansible Playbooks. These playbooks were tested on CentOS 6.x so we recommend
that you use CentOS or RHEL to test these modules.

This LAMP stack can be on a single node or multiple nodes. The inventory file
'hosts' defines the nodes in which the stacks should be configured.

        [webservers]
        localhost

        [dbservers]
        bensible

Here the webserver would be configured on the local host and the dbserver on a
server called "bensible". The stack can be deployed using the following
command:

        ansible-playbook -i hosts site.yml

Once done, you can check the results by browsing to http://localhost/index.php.
You should see a simple test page and a list of databases retrieved from the
database server.
##Deploying a sharded, production-ready MongoDB cluster with Ansible
------------------------------------------------------------------------------

- Requires Ansible 1.2
- Expects CentOS/RHEL 6 hosts

### A Primer
---------------------------------------------

![Alt text](images/nosql_primer.png "Primer NoSQL")

The above diagram shows how MongoDB differs from the traditional relational
database model. In an RDBMS, the data associated with 'user' is stored in a
table, and the records of users are stored in rows and columns. In MongoDB, the
'table' is replaced by a 'collection' and the individual 'records' are called
'documents'.  One thing to notice is that the data is stored as key/value pairs
in BJSON format.

Another thing to notice is that NoSQL-style databases have a looser consistency
model. As an example, the second document in the users collection has an
additonal field of 'last name'.
 
### Data Replication
------------------------------------

![Alt text](images/replica_set.png "Replica Set")

Data backup is achieved in MongoDB via _replica sets_. As the figure above shows,
a single replication set consists of a replication master (active) and several
other replications slaves (passive). All the database operations like
add/delete/update happen on the replication master and the master replicates
the data to the slave nodes. _mongod_ is the process which is resposible for all
the database activities as well as replication processes. The minimum
recommended number of slave servers are 3.

### Sharding (Horizontal Scaling) .
------------------------------------------------

![Alt text](images/sharding.png "Sharding")

Sharding works by partitioning the data into seperate chunks and allocating
diffent ranges of chunks to diffrent shard servers. The figure above shows a
collection which has 90 documents which have been sharded across the three
servers: the first shard getting ranges from 1-29, and so on. When a client wants
to access a certain document, it contacts the query router (mongos process),
which in turn contacts the 'configuration node', a lightweight mongod
process) that keeps a record of which ranges of chunks are distributed across
which shards. 

Please do note that every shard server should be backed by a replica set, so
that when data is written/queried copies of the data are available. So in a
three-shard deployment we would require 3 replica sets and primaries of each
would act as the sharding server.

Here are the basic steps of how sharding works:

1) A new database is created, and collections are added.

2) New documents get updated when clients update, and all the new documents
goes into a single shard.

3) When the size of collection in a shard exceeds the 'chunk_size' the
collection is split and balanced across shards.


### Deploying MongoDB Ansible
--------------------------------------------

#### Deploy the Cluster
----------------------------

![Alt text](images/site.png "Site")
  
The diagram above illustrates the deployment model for a MongoDB cluster deployed by
Ansible. This deployment model focuses on deploying three shard servers,
each having a replica set, with the backup replica servers serving as the other two shard
primaries. The configuration servers are co-located with the shards. The _mongos_
servers are best deployed on seperate servers. This is the minimum recomended
configuration for a production-grade MongoDB deployment. Please note that the
playbooks are capable of deploying N node clusters, not limited to three. Also,
all the processes are secured using keyfiles.

#### Prerequisite

Edit the group_vars/all file to reflect the below variables.

1) iface: 'eth1'     # the interface to be used for all communication.
		
2) Set a unique mongod_port variable in the inventory file for each MongoDB
server.

3) The default directory for storing data is /data, please do change it if
required. Make sure it has sufficient space: 10G is recommended.

### Deployment Example

The inventory file looks as follows:

		#The site wide list of mongodb servers
		[mongo_servers]
		mongo1 mongod_port=2700
		mongo2 mongod_port=2701
		mongo3 mongod_port=2702

		#The list of servers where replication should happen, including the master server.
		[replication_servers]
		mongo3
		mongo1
		mongo2

		#The list of mongodb configuration servers, make sure it is 1 or 3
		[mongoc_servers]
		mongo1
		mongo2
		mongo3

		#The list of servers where mongos servers would run. 
		[mongos_servers]
		mongos1
		mongos2

Build the site with the following command:

		ansible-playbook -i hosts site.yml


#### Verifying the Deployment 
---------------------------------------------

Once configuration and deployment has completed we can check replication set
availability by connecting to individual primary replication set nodes, `mongo
--host 192.168.1.1 --port 2700` and issue the command to query the status of
replication set, we should get a similar output.

		
		web2:PRIMARY> rs.status()
		{
			"set" : "web2",
			"date" : ISODate("2013-03-19T10:26:35Z"),
			"myState" : 1,
			"members" : [
			{
				"_id" : 0,
				"name" : "web2:2013",
				"health" : 1,
				"state" : 1,
				"stateStr" : "PRIMARY",
				"uptime" : 102,
				"optime" : Timestamp(1363688755000, 1),
				"optimeDate" : ISODate("2013-03-19T10:25:55Z"),
				"self" : true
			},
			{
				"_id" : 1,
				"name" : "web3:2013",
				"health" : 1,
				"state" : 2,
				"stateStr" : "SECONDARY",
				"uptime" : 40,
				"optime" : Timestamp(1363688755000, 1),
				"optimeDate" : ISODate("2013-03-19T10:25:55Z"),
				"lastHeartbeat" : ISODate("2013-03-19T10:26:33Z"),
				"pingMs" : 1
			}
			],
			"ok" : 1
		}


We can check the status of the shards as follows: connect to the mongos service
'mongo localhost:8888/admin -u admin -p 123456' and issue the following command to get
the status of the Shards:


		 
		mongos> sh.status()
		--- Sharding Status --- 
		  sharding version: { "_id" : 1, "version" : 3 }
		  shards:
			{  "_id" : "web2",  "host" : "web2/web2:2013,web3:2013" }
			{  "_id" : "web3",  "host" : "web3/web2:2014,web3:2014" }
  		databases:
			{  "_id" : "admin",  "partitioned" : false,  "primary" : "config" }


We can also make sure the sharding works by creating a database, a collection,
and populate it with documents and check if the chunks of the collection are
balanced equally across nodes. The below diagram illustrates the verification
step.

-------------------------------------------------------------------------------------------------------------------------------------------------------------

![Alt text](images/check.png "check")

The above mentioned steps can be tested with an automated playbook.

Issue the following command to run the test. Pass one of the _mongos_ servers
in the _servername_ variable.
		
		ansible-playbook -i hosts playbooks/testsharding.yml -e servername=server1


Once the playbook completes, we check if the sharding has succeeded by logging
on to any mongos server and issuing the following command. The output displays
the number of chunks spread across the shards.

		mongos> sh.status()
			--- Sharding Status --- 
  			sharding version: { "_id" : 1, "version" : 3 }
  			shards:
			{  "_id" : "bensible",  "host" : "bensible/bensible:20103,web2:20103,web3:20103" }
			{  "_id" : "web2",  "host" : "web2/bensible:20105,web2:20105,web3:20105" }
			{  "_id" : "web3",  "host" : "web3/bensible:20102,web2:20102,web3:20102" }
  			databases:
			{  "_id" : "admin",  "partitioned" : false,  "primary" : "config" }
			{  "_id" : "test",  "partitioned" : true,  "primary" : "web3" }
			
				test.test_collection chunks:
				
				bensible	7
				web2	6
				web3	7
			
			

 
### Scaling the Cluster
---------------------------------------

![Alt text](images/scale.png "scale")

To add a new node to the existing MongoDB Cluster, modify the inventory file as follows:

		#The site wide list of mongodb servers
		[mongoservers]
		mongo1 mongod_port=2700
		mongo2 mongod_port=2701
		mongo3 mongod_port=2702
		mongo4 mongod_port=2703

		#The list of servers where replication should happen, make sure the new node is listed here.
		[replicationservers]
		mongo4
		mongo3
		mongo1
		mongo2

		#The list of mongodb configuration servers, make sure it is 1 or 3
		[mongoc_servers]
		mongo1
		mongo2
		mongo3

		#The list of servers where mongos servers would run. 
		[mongos_servers]
		mongos1
		mongos2

Make sure you have the new node added in the _replicationservers_ section and
execute the following command:

		ansible-playbook -i hosts site.yml

###Verification.
-----------------------------

The newly added node can be easily verified by checking the sharding status and
seeing the chunks being rebalanced to the newly added node.

			$/usr/bin/mongo localhost:8888/admin -u admin -p 123456
			mongos> sh.status()
				--- Sharding Status --- 
  				sharding version: { "_id" : 1, "version" : 3 }
  			shards:
			{  "_id" : "bensible",  "host" : "bensible/bensible:20103,web2:20103,web3:20103" }
			{  "_id" : "web2",  "host" : "web2/bensible:20105,web2:20105,web3:20105" }
			{  "_id" : "web3",  "host" : "web3/bensible:20102,web2:20102,web3:20102" }
			{  "_id" : "web4",  "host" : "web4/bensible:20101,web3:20101,web4:20101" }
  			databases:
			{  "_id" : "admin",  "partitioned" : false,  "primary" : "config" }
			{  "_id" : "test",  "partitioned" : true,  "primary" : "bensible" }
		
			test.test_collection chunks:
			
				web4	3
				web3	6
				web2	6
				bensible	5

    
## WordPress+Nginx+PHP-FPM Deployment

- Requires Ansible 1.2 or newer
- Expects CentOS/RHEL 6.x hosts

These playbooks deploy a simple all-in-one configuration of the popular
WordPress blogging platform and CMS, frontend by the Nginx web server and the
PHP-FPM process manager. To use, copy the `hosts.example` file to `hosts` and 
edit the `hosts` inventory file to include the names or URLs of the servers
you want to deploy.

Then run the playbook, like this:

	ansible-playbook -i hosts site.yml

The playbooks will configure MySQL, WordPress, Nginx, and PHP-FPM. When the run
is complete, you can hit access server to begin the WordPress configuration.

### Ideas for Improvement

Here are some ideas for ways that these playbooks could be extended:

- Parameterize the WordPress deployment to handle multi-site configurations.
- Separate the components (PHP-FPM, MySQL, Nginx) onto separate hosts and 
handle the configuration appropriately.
- Handle WordPress upgrades automatically.

We would love to see contributions and improvements, so please fork this
repository on GitHub and send us your changes via pull requests.
Building a simple LAMP stack and deploying Application using Ansible Playbooks.
-------------------------------------------

These playbooks require Ansible 1.2.

These playbooks are meant to be a reference and starter's guide to building
Ansible Playbooks. These playbooks were tested on CentOS 7.x so we recommend
that you use CentOS or RHEL to test these modules.

RHEL7 version reflects changes in Red Hat Enterprise Linux and CentOS 7:
1. Network device naming scheme has changed
2. iptables is replaced with firewalld
3. MySQL is replaced with MariaDB

This LAMP stack can be on a single node or multiple nodes. The inventory file
'hosts' defines the nodes in which the stacks should be configured.

        [webservers]
        localhost

        [dbservers]
        bensible

Here the webserver would be configured on the local host and the dbserver on a
server called "bensible". The stack can be deployed using the following
command:

        ansible-playbook -i hosts site.yml

Once done, you can check the results by browsing to http://localhost/index.php.
You should see a simple test page and a list of databases retrieved from the
database server.
## Standalone Tomcat Deployment

- Requires Ansible 1.2 or newer
- Expects CentOS/RHEL 6.x hosts

These playbooks deploy a very basic implementation of Tomcat Application Server,
version 7. To use them, first edit the "hosts" inventory file to contain the
hostnames of the machines on which you want Tomcat deployed, and edit the 
group_vars/tomcat-servers file to set any Tomcat configuration parameters you need.

Then run the playbook, like this:

	ansible-playbook -i hosts site.yml

When the playbook run completes, you should be able to see the Tomcat
Application Server running on the ports you chose, on the target machines.

This is a very simple playbook and could serve as a starting point for more
complex Tomcat-based projects. 

### Ideas for Improvement

Here are some ideas for ways that these playbooks could be extended:

- Write a playbook to deploy an actual application into the server.
- Deploy Tomcat clustered with a load balancer in front.

We would love to see contributions and improvements, so please fork this
repository on GitHub and send us your changes via pull requests.
## Tomcat failover with Memcached + Memcached Session Manager + Nginx (load blancer)

- Tested on Ansible 1.9.3 for Debian
- Expects hosts: Centos 6.x

This playbook deploys a failover solution for clustered Tomcat using Nginx as load balancer and Memcached + MSM as session manager.

- Nginx: balances the requests by round robin.
- Memcached: stores `sessionid` of tomcat.
- MSM: manages tomcat session.

For more detail about session management, see https://github.com/magro/memcached-session-manager

This playbook also deploys a demo web app (https://github.com/magro/msm-sample-webapp) to test the session management.


## Initial setup of inventory file

```
[lb_servers]
lbserver

[backend_servers]
tomcat_server_1
tomcat_server_2

[memcached_servers]
cached_server1
cached_server2
```

Edit inventory file `hosts` to suit your requirements and run playbook:

```
    $ ansible-playbook -i host site.yml
```

When finished, open web browser and access to http://nginx_ip/ to start testing.

## Ideas and improvements

- Setup SSL for load balancer.
- HA load balancer.
- Hardening iptables rules.

Pull requests are welcome.

## License

This work is licensed under MIT license.
## Standalone JBoss Deployment

- Requires Ansible 1.2 or newer
- Expects CentOS/RHEL 6 or 7 hosts

These playbooks deploy a very basic implementation of JBoss Application Server,
version 7. To use them, first edit the "hosts" inventory file to contain the
hostnames of the machines on which you want JBoss deployed, and edit the 
group_vars/all file to set any JBoss configuration parameters you need.

Then run the playbook, like this:

	ansible-playbook -i hosts site.yml

When the playbook run completes, you should be able to see the JBoss
Application Server running on the ports you chose, on the target machines.

This is a very simple playbook and could serve as a starting point for more
complex JBoss-based projects. 

## Application deployment

The playbook deploy-application.yml may be used to deploy the HelloWorld and Ticket Monster demo applications to JBoss hosts that have been deployed using site.yml, as above.

Run the playbook using:

	ansible-playbook -i hosts deploy-application.yml
	
The HelloWorld application will be available at `http://<jboss server>:<http_port>/helloworld`

The Ticket Monster application will be available at `http://<jboss server>:<http_port>/ticket-monster`

## Provisioning for Amazon Web Services

A simple playbook is provided, as an example, to provision hosts in preparation for running this JBoss deployment example.

	ansible-playbook -i hosts demo-aws-launch.yml

### Ideas for Improvement

Here are some ideas for ways that these playbooks could be extended:

- Write a playbook or an Ansible module to configure JBoss users.
- Extend this configuration to multiple application servers fronted by a load
balancer or other web server frontend.

We would love to see contributions and improvements, so please fork this
repository on GitHub and send us your changes via pull requests.
