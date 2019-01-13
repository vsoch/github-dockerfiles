# OpenStack on CoreOS Cluster 


CoreOS provide ease of cluster managing such as fault tolerance and scaleability features.
OpenStack operation need to high availability features in real world. So I am trying to make docker container according to CoreOS for OpenStack Operation Environments.
* Controller / Network / Compute Service Start Automation
* When a server failure using shared disk (such as NFS on gluster filesystem), minimize the data lose after restart the service. (MySQL Data, Glance Images, Nova Instances etc.)
* CoreOS etcd and fleet service provide by a rapid recovery, and easy scalability server node.

And also OpenStack is obtaining using Docker/CoreOS the following advatages :
* Easy to Deploy
* Easy to Test
* Easy to Scale-out
* Fault Tolerance

## Cluster Configuration 
The sample cluster consists 4 group.
* controller : 3-node cluster (role of controller)
* network : 2-node cluster (role of neutron)
* compute : 2-node cluster (role of compute)
* nova-docker : 2-node cluster (role of nova-docker)

## Test Environments
#####Install dependencies

* [VirtualBox][virtualbox] 4.3.10 or greater.
* [Vagrant][vagrant] 1.6 or greater.

This is a muti-node cluster proof-of-concept that includes setting up the external connectivity to VMs using Virtualbox environment. We have to setup for Virtualbox network option is as follows:

1) Open Virtualbox

2) Navigate to the Network Preferences

3) Create a new NAT Network and name it “NatNetwork”, Edit Network CIDR "10.0.5.0/24" and Unselect “supports DHCP”

#####Usage of Network Interface:

| Device | Role  | IP Range |
|--------|--------|---------|
| eth0 |  NAT (Default Route)      | 10.0.2.XX |
| eth1 | External Network (The above special setting of NAT) | 10.0.5.XX |
| eth2 | Tunneling | 172.16.0.XX |
| eth3 | Data Management | 192.168.10.XX |

## Docker Container
##### Controller Image
* Image Name : 
continuse/openstack-controller:juno
continuse/openstack-controller:kilo
* provide service : MySQL, RabbitMQ, Keystone, Glance, Nova, Neutron

##### Network Image
* Image Name : 
continuse/openstack-network:juno
continuse/openstack-network:kilo
* provide service : Distributed Virtual Router / L3 HA with VxLAN

##### Compute Image
* Images Name : 
continuse/openstack-compute:juno
continuse/openstack-compute:kilo
* provide service : Libvirt, Nova, Netron

##### Nova-docker Image
* Images Name : 
continuse/openstack-nova-docker:juno
continuse/openstack-nova-docker:kilo
* provide service : Nova, Netron, Docker Driver

**Currently, these images support Operating System is only  CoreOS, but I plan to develop for any Linux that supports Docker Service.In addition, I will update for the other services of OpenStack, such as swift, cinder service etc.**

## CoreOS Installation
My development environment is as VirtualBox and Vagrant on Mac OSX (dual core i5 and 16G memory). Please refer to the website https://coreos.com about CoreOS installation.

The below installation procedure is an example of my development environment.

1) Update "discovery URL" in cluster/controller/user-data file

* getting the discovery URL
```
$ curl -w "\n" 'https://discovery.etcd.io/new?size=3'
https://discovery.etcd.io/6a28e078895c5ec737174db2419bb2f3
```
* Be sure to replace ``<token>`` with your discovery URL
```
coreos:
  etcd:
    # generate a new token for each unique cluster from https://discovery.etcd.io/new
    # WARNING: replace each time you 'vagrant destroy'
    discovery: <token>
```

2) Update your Timezone in 
* ``cluster/controller/user-data``
* ``cluster/network/user-data``
* ``cluster/compute/user-data``
* ``cluster/nova-docker/user-data``

You will need to modify the set-timezeone field in your timezone. The default value is ``Asia/Seoul``.

3) config.rb

**There is no need to change the general configuration.**

The number of servers in the cluster.
```
# Size of the CoreOS cluster created by Vagrant
$num_instances=3
```
choose for CoreOS (stable, beta or alpha)
```
# Official CoreOS channel from which updates should be downloaded
$update_channel='stable'
```
Set Up for VirtualBox VMs

For testing, vm_memory is over 2048, and vb_cpus is over 2.
```
#$vb_gui = false
$vb_memory = 2048
$vb_cpus = 2
```

4) Update Vagrant Vagrantfile

Do NOT EDIT "Vagrantfile" except for NFS mount path for test.
* ``cluster/controller/Vagrantfile``
* ``cluster/network/Vagrantfile``
* ``cluster/compute/Vagrantfile``
* ``cluster/nova-docker/Vagrantfile``


**NFS Mount**

```
config.vm.synced_folder "~/test/cluster/continuse", "/continuse", id: "root", :nfs => true, :mount_options =>  ["nolock,vers=3,udp"], :map_uid => 0, :map_gid => 0
```
5) Start the machine(s)

```
$ cd $HOME/test/controller
$ vagrant up
.......
$ cd ../network
$ vagrant up
.......
$ cd ../compute
$ vagrant up
.......
$ cd ../nova-docker
$ vagrant up
```
During procedures for ``vagrant up`` need to your admin password for NFS mount.

List the status the running machines of each directory (controller, network, compute, nova-docker:
```
$ vagrant status
Current machine states:

controller-01                   running (virtualbox)
controller-02                   running (virtualbox)
controller-03                   running (virtualbox)

```

You can connect to one of the machines the following vagrant ssh command:
```
$ vagrant ssh controller-01 -- -A
```

## Pulling the docker container images 
I could not use attached storage for docker. (refer to https://coreos.com/docs/cluster-management/setup/mounting-storage/#use-attached-storage-for-docker). Because my test environment does not support btrfs file system device.

### controller image
Download for All nodes (controller-01, controller-02, controller-03)
```
On Mac
$ cd $HOME/test/controller
$ vagrant ssh controller-03 -- -A

On CoreOS
$ sudo docker pull continuse/openstack-controller:juno (or kilo)
```

### network image
Download for All nodes (network-01, network-02)
```
On Mac
$ cd $HOME/test/network
$ vagrant ssh network-01 -- -A

On CoreOS
$ sudo docker pull continuse/openstack-network:juno (or kilo)
```

### compute image
Download for All nodes (compute-01, compute-02)
```
On Mac
$ cd $HOME/test/compute
$ vagrant ssh compute-01 -- -A

On CoreOS
$ sudo docker pull continuse/openstack-compute:juno (or kilo)
```

### nova-docker image
Download for All nodes (nova-docker-01, nova-docker-02)
```
On Mac
$ cd $HOME/test/nova-docker
$ vagrant ssh nova-docker-01 -- -A

On CoreOS
$ sudo docker pull continuse/openstack-nova-docker:juno (or kilo)
```

**If you do not the pulling images, it takes a lot of time at the beginning of services.**

## Service File Modification

First, connect to one of the machines
```
$ vagrant ssh controller-01 -- -A
```

Neutron Service provide Distributed Virtual Router and L3 HA options. This docker images can configured to select one. 

**If you want to configure Distributed Virtual Router, to modify ""--env HA_MODE=DVR" option in three files.** 

**If you want to configure L3 HA, to modify ""--env HA_MODE=L3_HA" option in 4 files.** 

* /continuse/service/controller.service
* /continuse/service/network.service
* /continuse/service/compute.service
* /continuse/service/nova-docker.service

**NOTE: MUST BE THE SAME for the same environment variable at the three service files.**

example) If you want to configure ``HA_MODE=DVR``, ALL service files (controller.service, network.service, compute.service, nova-docker.service) set to ``HA_MODE=DVR`` as the same.

## Data Initialization

YOU MUST BE DATA INITIALIZATION, AFTER THE CHAGE ``HA_MODE`` VALUE.
* Glance Image Data Remove

        $ rm -rf /continuse/shared/glance/*

* MySQL Data Remove
        $ rm -rf /continuse/shared/mysql/*

* Nova Instance Data Remove
        $ rm -rf /continuse/shared/nova/*

## Usage

Nova-docker driver is provided separately as Nova-compute service with libvirt/KVM-qemu.

Please refer to [Nova-Docker Driver Usage](README-nova-docker.md)

### Service Start / Stop / Destroy

connect to one of the machines:

**controller service start**
```
On Mac
$ cd $HOME/abc/coreos
$ vagrant ssh controller-01 -- -A

On CoreOS
Last login: Fri Apr  3 12:11:03 2015 from 10.0.2.2
CoreOS stable (607.0.0)
$ cd /continuse/service
$ fleetctl start controller.service
```
**network service start (2 node service start for HA)**
```
$ fleetctl start network.service
```

**compute service start**
```
$ fleetctl start compute.service
```

The unit should have been scheduled to a machine in your cluster.
You can know which machine run the service.
```
$ fleetctl list-units
UNIT			       MACHINE         	        ACTIVE	SUB
compute.service	   68b75b56.../192.168.10.31	active	running
controller.service	01df5f39.../192.168.10.13	active	running
network.service	   154fea9e.../192.168.10.21	active	running
network.service	   0d348a8e.../192.168.10.22	active	running
```

**service stop**

If you want to stop the service. The stop means that stop the service, but service information remains the cluster.
```
$ fleetctl stop controller.service
$ fleetctl stop network.service
$ fleetctl stop compute.service
```
**service destroy**

This command effective that the service information removed from the cluster.
```
$ fleetctl destroy controller.service
$ fleetctl destroy network@.service
```

###Log Monitoring
You can view a log of each service in a realtime.
```
$ fleetctl journal -f controller.service
$ journalctl -u network.service -f
$ journalctl -u compute.service -f
```

###Login to controller / Network / Compute Node
You can get the IP Address through the ``fleetctl list-unins`` command for the controller host.

```
$ fleetctl list-units
UNIT			    MACHINE				        ACTIVE	SUB
compute.service	    68b75b56.../192.168.10.31	active	running 
controller.service 	01df5f39.../192.168.10.13	active	running  
network.service	    154fea9e.../192.168.10.21	active	running  
network.service	    0d348a8e.../192.168.10.22	active	running  
```

**login to controller running host**

```
$ vagrant ssh controller-03 -- -A
on CoreOS
$ connect
```
Network / Compute Node connection method
```
=== Network Node ===
login to network-01 or network-03
$ connect

=== Compute Node ===
login to compute-01 or compute-02 
$ connect
```

### Image Upload & Create Network etc. on Controller

```
Login to controller-01
$ connect

# 
```
Source the admin credentials to gain access to admin-only CLI commands on controller
```
$ export OS_TENANT_NAME=admin
$ export OS_USERNAME=admin
$ export OS_PASSWORD=adminpass
$ export OS_AUTH_URL=http://controller:5000/v2.0/
$ export OS_NO_CACHE=1
```
Glance Image Upload
```
$ cd /continuse/script
$ glance image-create \
     --name "cirros-0.3.3-x86_64" \
     --file cirros-0.3.3-x86_64-disk.img \
     --disk-format qcow2 --container-format bare \
     --is-public True \
     --progress
```

Nova security group add
```
$ nova secgroup-add-rule default tcp 22 22 0.0.0.0/0
$ nova secgroup-add-rule default icmp -1 -1 0.0.0.0/0 
```

External Network and Subnet Creation
```
neutron net-create public --router:external True \
    --provider:network_type flat \
    --provider:physical_network external

neutron subnet-create --name public-subnet \
    --gateway 10.0.5.1 \
    --allocation-pool start=10.0.5.100,end=10.0.5.200 \
    --disable-dhcp public 10.0.5.0/24
```

Private Network Creation
```
neutron net-create private
neutron subnet-create --name private-subnet private \
    10.10.0.0/24 --dns-nameserver 10.0.5.1
```

Router Creation (HA_MODE=L3_HA)
```
neutron router-create router  --ha True
neutron router-interface-add router private-subnet
neutron router-gateway-set router public
```

Router Creation (HA_MODE=DVR)
```
neutron router-create router  --ha False
neutron router-interface-add router private-subnet
neutron router-gateway-set router public
```

Keypair Generation
```
nova keypair-add myKey > myKey.pem
chmod 0600 myKey.pem
```

###Using Dashboard
You can get the IP Address through the ``fleetctl list-unins`` command for the controller host. Access the dashboard using a web browser: http://controller-ip-addr/horizon/. For instance http://192.168.10.13/horizon/ (ID : admin, Password : adminpass)

In my case to change RAM size 512M to 64M in m1.tiny in flavor. And Launch Instance to select network "private".

Floating IP Create on the controller
```
controller:/continuse/script# neutron floatingip-create public
Created a new floatingip:
+---------------------+--------------------------------------+
| Field               | Value                                |
+---------------------+--------------------------------------+
| fixed_ip_address    |                                      |
| floating_ip_address | 10.0.5.101                           |
| floating_network_id | dd3e01a0-26ad-49eb-b003-0cf2770a6388 |
| id                  | ca880356-9c38-4587-b10f-ce27d2f58436 |
| port_id             |                                      |
| router_id           |                                      |
| status              | DOWN                                 |
| tenant_id           | ade4c04bb5fb4185bc3e52365ea547dc     |
+---------------------+--------------------------------------+
```

Floating IP associate
```
nova floating-ip-associate demo01 10.0.5.101
```

Connect to VM
```
controller:/continuse/script# ssh cirros@10.0.5.101 -i myKey.pem
The authenticity of host '10.0.5.101 (10.0.5.101)' can't be established.
RSA key fingerprint is 3d:cd:c1:40:f3:58:01:2f:a0:1a:13:a2:87:8d:16:ae.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '10.0.5.101' (RSA) to the list of known hosts.
$
$
$
$ ping openstack.org
PING openstack.org (162.242.140.107): 56 data bytes
64 bytes from 162.242.140.107: seq=0 ttl=45 time=682.501 ms
64 bytes from 162.242.140.107: seq=1 ttl=45 time=493.169 ms
64 bytes from 162.242.140.107: seq=2 ttl=45 time=314.223 ms
^C
--- openstack.org ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 314.223/496.631/682.501 ms
$
```


## Fault Tolerance Test
You can get IP address for running controller service using ``fleetctl list-units`` command.

**Controller node fail test**
```
On Mac
$ vagrant halt controller-03
==> controller-03: Attempting graceful shutdown of VM...
$ vagrant up controller-03
Bringing machine 'core-04' up with 'virtualbox' provider...
==> controller-03: Checking if box 'coreos-stable' is up to date...
==> controller-03: Clearing any previously set forwarded ports...
.
.
.
.

$ vagrant ssh controller-02
Last login: Wed Apr 29 14:31:02 2015 from 10.0.2.2
CoreOS alpha (681.0.0)
core@core-01 ~ $ fleetctl list-units
UNIT			    MACHINE				        ACTIVE	SUB
compute.service	    68b75b56.../192.168.10.31	active	running
controller.service	 8f6fcefb.../192.168.10.12	active	running
network.service	    154fea9e.../192.168.10.31	active	running
network.service	    0d348a8e.../192.168.10.32	active	running
$
```
You will found controller.service running on controller-02 from controller-03. For verification, to connect dashboard "http://192/168.10.12/horizon/" and YOU CAN ANY ACTION IS NO PROBLEM.

**Network Node / Compute Node Fail Test is the same as the above controller node fail test.**
In Case Of HA_MODE=L3_HA, there is no problem in network node fail test, but HA_MODE=DVR does not support failover. Because currently "snat" namespace could not move to the another host.

## VM Migration

If you want to compute node fail test, YOU NEED TO VM MIGRATION.
If one VM ran on compute-01 and your new service of compute.service run on compute-02, you will need the following the action on controller node.
```
On controller
$ nova evacuate demo01 compute-02 –-on-shared-storage
```
Confirm to access the dashboard for migration VM.



[virtualbox]: https://www.virtualbox.org/
[vagrant]: https://www.vagrantup.com/downloads.html
[using-coreos]: http://coreos.com/docs/using-coreos/
# Block Storage Service
This docker image has been testing using NFS Server. I'm planning to support Gluster File System Cluster or Ceph Cluster with Cinder Service ASAP.

## cinder cluster start (Now only one node for test)
```
On Mac
$ cd cinder
$ vagrant up
......
.....
$ vagrant ssh cinder-01
On CoreOS
$ sudo docker pull continuse/openstack-cinder:kilo 
```

## cinder service start using fleetctl command
On the controller node
```
$ cd /continuse/service
$ fleetctl start cinder.service
```

## Block Storage Attaching Test Procedure

On the Controller Node
```
$ export OS_PROJECT_DOMAIN_ID=default
$ export OS_USER_DOMAIN_ID=default
$ export OS_PROJECT_NAME=admin
$ export OS_TENANT_NAME=admin
$ export OS_USERNAME=admin
$ export OS_PASSWORD=$ADMIN_PASS
$ export OS_AUTH_URL=http://controller:35357/v3
$ export OS_IMAGE_API_VERSION=2
$ export OS_VOLUME_API_VERSION=2

$ cinder service-list
+------------------+---------------+------+---------+-------+----------------------------+-----------------+
|      Binary      |      Host     | Zone |  Status | State |         Updated_at         | Disabled Reason |
+------------------+---------------+------+---------+-------+----------------------------+-----------------+
| cinder-scheduler |   controller  | nova | enabled |   up  | 2015-07-09T06:05:13.000000 |       None      |
|  cinder-volume   | cinder-01@nfs | nova | enabled |   up  | 2015-07-09T06:05:14.000000 |       None      |
+------------------+---------------+------+---------+-------+----------------------------+-----------------+

$ cinder create --display_name disk01 1
+---------------------------------------+--------------------------------------+
|                Property               |                Value                 |
+---------------------------------------+--------------------------------------+
|              attachments              |                  []                  |
|           availability_zone           |                 nova                 |
|                bootable               |                false                 |
|          consistencygroup_id          |                 None                 |
|               created_at              |      2015-07-09T06:06:53.000000      |
|              description              |                 None                 |
|               encrypted               |                False                 |
|                   id                  | 47629300-da8d-4633-9680-9090b5e2c450 |
|                metadata               |                  {}                  |
|              multiattach              |                False                 |
|                  name                 |                disk01                |
|         os-vol-host-attr:host         |                 None                 |
|     os-vol-mig-status-attr:migstat    |                 None                 |
|     os-vol-mig-status-attr:name_id    |                 None                 |
|      os-vol-tenant-attr:tenant_id     |   30037a509d4c425a9012d6af386bd0eb   |
|   os-volume-replication:driver_data   |                 None                 |
| os-volume-replication:extended_status |                 None                 |
|           replication_status          |               disabled               |
|                  size                 |                  1                   |
|              snapshot_id              |                 None                 |
|              source_volid             |                 None                 |
|                 status                |               creating               |
|                user_id                |   b3d4f6bf75a74aba8baa6bcfe68a183e   |
|              volume_type              |                 None                 |
+---------------------------------------+--------------------------------------+

$ nova list
+--------------------------------------+--------+--------+------------+-------------+-------------------------------+
| ID                                   | Name   | Status | Task State | Power State | Networks                      |
+--------------------------------------+--------+--------+------------+-------------+-------------------------------+
| d0e3ee9b-220d-47ae-8616-e7ccd55ec885 | demo01 | ACTIVE | -          | Running     | private=10.10.0.3, 10.0.5.101 |
+--------------------------------------+--------+--------+------------+-------------+-------------------------------+

$ cinder list
+--------------------------------------+-----------+--------+------+-------------+----------+--------------------------------------+
|                  ID                  |   Status  |  Name  | Size | Volume Type | Bootable |             Attached to              |
+--------------------------------------+-----------+--------+------+-------------+----------+--------------------------------------+
| 47629300-da8d-4633-9680-9090b5e2c450 | available | disk01 |  1   |     None    |  false   |                                      |
| a95632b5-15cf-4ff1-b568-dda0f52190d3 |   in-use  | disk01 |  1   |     None    |  false   | d0e3ee9b-220d-47ae-8616-e7ccd55ec885 |
+--------------------------------------+-----------+--------+------+-------------+----------+--------------------------------------+

$ nova volume-attach demo01 47629300-da8d-4633-9680-9090b5e2c450 auto
+----------+--------------------------------------+
| Property | Value                                |
+----------+--------------------------------------+
| device   | /dev/vdc                             |
| id       | 47629300-da8d-4633-9680-9090b5e2c450 |
| serverId | d0e3ee9b-220d-47ae-8616-e7ccd55ec885 |
| volumeId | 47629300-da8d-4633-9680-9090b5e2c450 |
+----------+--------------------------------------+

$ ssh cirros@10.0.5.101 -i myKey.pem
$ sudo fdisk /dev/vdc
Device contains neither a valid DOS partition table, nor Sun, SGI or OSF disklabel
Building a new DOS disklabel with disk identifier 0x1c3dc9fa.
Changes will remain in memory only, until you decide to write them.
After that, of course, the previous content won't be recoverable.

Warning: invalid flag 0x0000 of partition table 4 will be corrected by w(rite)

Command (m for help): n
Partition type:
   p   primary (0 primary, 0 extended, 4 free)
   e   extended
Select (default p): p
Partition number (1-4, default 1): 1
First sector (2048-2097151, default 2048):
Using default value 2048
Last sector, +sectors or +size{K,M,G} (2048-2097151, default 2097151):
Using default value 2097151

Command (m for help): w
The partition table has been altered!

Calling ioctl() to re-read partition table.
Syncing disks.
```

## Issues
The cinder node reboot when fleetctl service restart. If not....could not NFS mount.

# Heat Usage
Heat is the OpenStack orchestration program. This document is included hands-on explore OpenStack orchestration using Heat.

## Create Heat Domain (each user)
This procedure is only one excution each user, after MySQL Database Initial.

Source the admin credentials to gain access to admin-only CLI commands on controller
```
LOGIN TO CONTROLLER

$ export OS_TENANT_NAME=admin
$ export OS_USERNAME=admin
$ export OS_PASSWORD=adminpass
$ export OS_AUTH_URL=http://controller:5000/v2.0/
$ export OS_NO_CACHE=1

$ heat-keystone-setup-domain --stack-user-domain-name heat_user_domain \
$ --stack-domain-admin heat_domain_admin \
$ --stack-domain-admin-password $HEAT_DOMAIN_PASS
```

## Single Compute Instacne
To show how Heat works, below you can see a very simple HOT template.

#### login to controller

```
On Mac
$ vagrant ssh controller-03

On CoreOS (controller)
$ connect
$
```

#### excute admin_openrc.sh

```
export OS_PROJECT_DOMAIN_ID=default
export OS_USER_DOMAIN_ID=default
export OS_PROJECT_NAME=admin
export OS_TENANT_NAME=admin
export OS_USERNAME=admin
export OS_PASSWORD=$ADMIN_PASS
export OS_AUTH_URL=http://controller:35357/v3
export OS_IMAGE_API_VERSION=2
```

#### make a template file (create file as test1.yaml)

```
heat_template_version: 2014-10-16

description: Simple template to deploy a single compute instance

resources:
  my_instance:
    type: OS::Nova::Server
    properties:
      image: cirros-0.3.3-x86_64
      flavor: m1.tiny
      key_name: myKey
      networks:
        - network: private
```

#### create instance

```
$ heat stack-create stack1 -f test1.yaml
+--------------------------------------+------------+--------------------+----------------------+
| id                                   | stack_name | stack_status       | creation_time        |
+--------------------------------------+------------+--------------------+----------------------+
| 957cc4f3-3baa-4a0d-acce-740693c017cc | stack1     | CREATE_IN_PROGRESS | 2015-06-24T06:55:14Z |
+--------------------------------------+------------+--------------------+----------------------+
```

#### show status

```
$ heat stack-show stack1
```

#### delete instacne

```
$ heat stack-delete stack1
```

## Single Compute Instance with parameters

#### make a template file (create file as test2.yaml)

```
heat_template_version: 2014-10-16

description: Simple template to deploy a single compute instance

parameters:
  image:
    type: string
    label: Image name or ID
    description: Image to be used for compute instance
    default: cirros-0.3.3-x86_64
  flavor:
    type: string
    label: Flavor
    description: Type of instance (flavor) to be used
    default: m1.tiny
  key:
    type: string
    label: Key name
    description: Name of key-pair to be used for compute instance
    default: myKey
  private_network:
    type: string
    label: Private network name or ID
    description: Network to attach instance to.
    default: private

resources:
  my_instance:
    type: OS::Nova::Server
    properties:
      image: { get_param: image }
      flavor: { get_param: flavor }
      key_name: { get_param: key }
      networks:
        - network: { get_param: private_network }

outputs:
  instance_ip:
    description: IP address of the instance
    value: { get_attr: [my_instance, first_address] }

```

#### Create Instance
```
$ heat stack-create stack2 -f test2.yaml -P key=myKey;image=cirros-0.3.3-x86_64"
```

# Nova-docker driver
The Docker driver is a hypervisor driver, it is support to Openstack Nova Compute. The driver lives out-of-tree for juno, but I am trying to make docker container just like Nova Compute Container. Now I'm testing this driver, and I think that needed to orchestrating docker tool.

## nova-docker service start
Any Host Login to One of the Controller Cluster Nodes. And Nova-docker service starting. 
```
# vagrant ssh controller-01

on coreos
$ cd /continuse/service
$ fleetctl start nova-docker.service
```

## Docker Image Upload to Glance
```
$ vagrant ssh nova-docker-01
.....
....
$ connect

# export OS_TENANT_NAME=admin
# export OS_USERNAME=admin
# export OS_PASSWORD=adminpass
# export OS_AUTH_URL=http://controller:5000/v2.0/
# export OS_NO_CACHE=1

== cirros & redis image pulling. ==
# docker pull cirros
# docker pull redis

== image upload to Glance
# docker save cirros | glance image-create --is-public=True --container-format=docker --disk-format=raw --name redis
```
**The docker driver is getting information the only container name from Glance Image Service, so the image is registered in the Glance Image Service using the small size of cirros image as named redis. To launch instance, using the image stored in the node which running nova-dokcer driver, and DOES NOT USE Glance Image Service.MUST BE PULLING docker image on nova-docker host. If you do not PULLING THE IMAGES, fail to launch instance.**

## Launch Instance
You can make instance using Project->Instance menu on Horizon (Dashboard), and allocate a floating public IP.

## Docker Container Running Check & Test
Login to CoreOS host which does not running neutron service. (You can use controller nodes)
YOU HAVE TO ADD RULE "REDIS TCP PORT" in Security Group Rules.
```
# vagrant ssh controller-01

$ sudo docker run --rm -it redis redis-cli -h 10.0.5.101

```
## Issues
The Live Migration feature does not support on Nova-docker driver, so sophisticated tool is required for normal use.


