= CASL Ansible

CASL Ansible provides a common experience for provisioning infrastructure for OpenShift across a number of infrastructure providers using link:http://www.ansible.com/[Ansible].

This includes automation of OpenShift Cluster provisioning as well as other automation tasks post-provisioning.

.What Can I Do with CASL Tools?
* Automated provisioning of an OpenShift cluster with existing automation infrastructure.
* Automated provisioning of an OpenShift cluster on a non-automated static (BYO) infrastructure.

== Provisioning An OpenShift Cluster with Existing Automation Infrastructure
The CASL Ansible tools provide everything needed to automatically provision an OpenShift cluster from scratch.

=== Prerequisites
* A basic understanding of the link:./docs/PROVISIONING_ARCH.md[CASL Architecture Overview], which outlines the end to end approach for automated provisioning OpenShift clusters.
* Access to one of the following compatible infrastructures for deploying an OpenShift cluster:
** An OpenStack environment.
** An AWS environment.
** A GCP environment.

=== Provisioning Procedures
* link:./docs/PROVISIONING_OPENSTACK.md[Provisioning an OpenShift Cluster on OpenStack]
* link:./docs/PROVISIONING_AWS.md[Provisioning an OpenShift Cluster on AWS]
* link:./docs/PROVISIONING_GCP.md[Provisioning an OpenShift Cluster on GCP]

== Provisioning An OpenShift Cluster with BYO Infrastructure
The CASL Ansible tools also enable you to provision an OpenShift cluster on static infrastructure where provisioning is not fully automated. More details are available in the link:./docs/BYO_INFRASTRUCTURE.adoc[Bring Your Own Infrastructure guide]. 

== Additional Resources

=== External Dependencies
For some tasks, CASL Ansible has dependencies on external repositories:

link:https://github.com/redhat-cop/infra-ansible[Infra Ansible]::
  A repository of Ansible automation for generic infrastructure components.
link:https://github.com/openshift/openshift-ansible[OpenShift Ansible]::
  The core OpenShift Installation Playbooks including the supporting roles.
link:https://github.com/openshift/openshift-ansible-contrib[OpenShift Ansible Contrib]::
  A repository of extra, unsupported, and upstream Ansible roles and playbooks for OpenShift.

NOTE: The dependencies are managed using `ansible-galaxy` and the specific instructions will call this out when there is a need to use galaxy to pull in the correct dependencies.

=== Automation of OpenShift Cluster Content
The link:https://github.com/redhat-cop/openshift-applier[openshift-applier] is used to automate the seeding of OpenShift cluster content based on OpenShift templates and parameters files.
OpenStack Docker Client
==================

Produces a container capable of acting as a client for OpenStack

## Setup

The following steps are required to run the docker client.

1. Install docker
  1. on RHEL/Fedora: ```{yum/dnf} install docker```
  2. on Windows: [Install Docker for Windows](https://docs.docker.com/windows/step_one/)
  3. on OSX: [Max OS X](https://docs.docker.com/installation/mac/)
  4. on all other Operating Systems: [Supported Platforms](https://docs.docker.com/installation/)
2. Give your user access to run Docker containers (this is only required in Linux/Unix distros)
```
groupadd docker
usermod -a -G docker ${USER}
systemctl enable docker
systemctl restart docker
```

## Running

A typical run of the image would look like:

```
docker run -u `id -u` \
      -v $HOME/.ssh/id_rsa:/opt/app-root/src/.ssh/id_rsa \
      -v $HOME/src/:/tmp/src \
      -v $HOME/.config/openstack/:/opt/app-root/src/.config/openstack/ \
      -e INVENTORY_DIR=/tmp/src/casl-ansible/inventory/sample.osp.example.com.d/inventory/ \
      -e PLAYBOOK_FILE=/tmp/src/casl-ansible/playbooks/openshift/end-to-end.yml \
      -e OPTS="-e openstack_ssh_public_key=my-public-key" -t \
      redhatcop/installer-openstack
```

NOTE: The above commands expects the following inputs:
* Your ssh key to be mounted in the container at `/opt/app-root/src/.ssh/id_rsa`
* An link:https://docs.openstack.org/user-guide/common/cli-set-environment-variables-using-openstack-rc.html[OpenStack RC file] to be mounted at `/opt/app-root/src/.config/openstack/opensh.rc`.
* Your ansible inventories and playbooks repos to live within the same directory, mounted at `/tmp/src`

## Building the Image

This image is built and published to docker.io, so there's no reason to build it if you're just wanting to use the latest stable version. However, if you need to build it for development reasons, here's how:

```
cd ./casl-ansible
docker build -f images/installer-openstack/Dockerfile -t redhatcop/installer-openstack .
```

## Troubleshooting

Below are some of helpful hints for resolving issues experiencing while configuring and running the container

**Issue**

Getting "permission denied" when attempting to run the docker image, e.g. something similar to:

```
 :
time="2015-09-01T11:32:36-04:00" level=fatal msg="Get http:///var/run/docker.sock/v1.18/images/json: dial unix /var/run/docker.sock: permission denied. Are you trying to connect to a TLS-enabled daemon without TLS?"
 :
FATA[0000] Post http:///var/run/docker.sock/v1.18/containers/create: dial unix /var/run/docker.sock: permission denied. Are you trying to connect to a TLS-enabled daemon without TLS?
 :
```

**Resolution #2**

This error indicates the currently logged in user is unable to access the docker socket.

To resolve this issue, create a new *docker* group and add the user to the *docker* group

```
groupadd docker
usermod -a -G docker ${USER}
systemctl enable docker
systemctl restart docker
```

Reboot the machine or log out/log in to reload your environment and complete the configurations.
AWS Docker Client
==================

Produces a container capable of acting as a client for AWS

## Setup

The following steps are required to run the docker client.

1. Install docker
  1. on RHEL/Fedora: ```{yum/dnf} install docker```
  2. on Windows: [Install Docker for Windows](https://docs.docker.com/windows/step_one/)
  3. on OSX: [Max OS X](https://docs.docker.com/installation/mac/)
  4. on all other Operating Systems: [Supported Platforms](https://docs.docker.com/installation/)
2. Give your user access to run Docker containers (this is only required in Linux/Unix distros)
```
groupadd docker
usermod -a -G docker ${USER}
systemctl enable docker
systemctl restart docker
```

## Running

A typical run of the image would look like:

```
docker run -u `id -u` \
      -v $HOME/.ssh:/opt/app-root/src/.ssh \
      -v $HOME/aws-credentials.csv:/opt/app-root/src/aws-credentials.csv \
      -v $HOME/src/:/tmp/src \
      -e INVENTORY_DIR=/tmp/src/casl-ansible/inventory/sample.aws.example.com.d/inventory/ \
      -e PLAYBOOK_FILE=/tmp/src/casl-ansible/playbooks/openshift/end-to-end.yml \
      -e OPTS="-e aws_key_name=my-public-key" -t \
      redhatcop/installer-aws
```

The above commands expects the following inputs:
* Your ssh key (~/.ssh/id_rsa) to be mounted in the container at `/opt/app-root/src/.ssh/id_rsa`
* Your AWS credentials (in CSV format) is available in your home directory
* Your ansible inventories and playbooks repos to live within the same directory, mounted at `/tmp/src`

> **Note:** The AWS credentials file can be using the .csv as downloaded from AWS, or a .sh file can be used and will be sourced as-is (make sure the **AWS_SECRET_ACCESS_KEY** and **AWS_ACCESS_KEY_ID** environment variables are exported correctly).

## Building the Image

This image is built and published to docker.io, so there's no reason to build it if you're just wanting to use the latest stable version. However, if you need to build it for development reasons, here's how:

```
cd ./casl-ansible
docker build -f images/installer-aws/Dockerfile -t redhatcop/installer-aws .
```

## Troubleshooting

Below are some of helpful hints for resolving issues experiencing while configuring and running the container

TBD

OpenShift Applier Docker Client
===============================

This content has been moved to https://github.com/redhat-cop/openshift-applier
== The rhc-ose roles implementations

Below are the variables[Required and Optional] for each of the defined roles. They must be defined in the inventory files when running the related ansible playbook.

##Roles:

###dns

  - Required
    -
    -
    -
  - Optional
    -
    -
    -


###openshift-provision

  - Required
    -
    -
    -
  - Optional
    -
    -
    -

###openstack-create

  - Required
    -
    -
    -
  - Optional
    -
    -
    -

###registry

  - Required
    -
    -
    -
  - Optional
    -
    -
    -
# openshift-route-status


cfme-ocp-provider
=========

Role used to configure OpenShift as a Container Provider to Red Hat CloudForms.


Requirements
------------

None

Role Variables
--------------

The following role variables must be provided

```
cfme_host: <hostname of the CloudForms instance>
cfme_username: <Username to access CloudForms>
cfme_password: <Password to access CloudForms>
```

The following variables can also be provided in order to customize the configuration

```
ocp_master_host: <OpenShift API Host>
ocp_master_port: <OpenShift API Port>
hawkular_host: <Hawkular Hostname>
hawkular_port: <Hawkular Port>
ocp_token: <OAuth token to access OpenShift Rest API>
hawkular_token: <OAuth token to access Hawkular Metrics>
ocp_container_provier_name: <Name of the Container Provider in CloudForms to create for OpenShift>
default_token_sa_namespace: <Namespace of the Service Account containing the OAuth token if one is not provided for OpenShift or Hawkular>
default_token_sa_name: <Name of the Service Account containing the OAuth token if one is not provided for OpenShift or Hawkular>
```

Dependencies
------------
None


Example Playbook
----------------

The following is a sample playbook

```
# Example
- hosts: masters[0]
  roles:
    - role: cfme-ocp-provider
      cfme_host: cloudforms.example.com
```

License
-------

BSD

Author Information
------------------
Red Hat Community of Practice & staff of the Red Hat Open Innovation Labs.
# Instructions

1. Ensure the 'oc' client is part of your path 
2. Login as a cluster-admin on the OpenShift cluster
3. Execute with ansible, i.e.:

```
  > ansible-playbook -i inventory test.yml --connection=local
```
# make-applier-projects-unique

This content has been moved to https://github.com/redhat-cop/openshift-applier

manage-aws-infra
================

This role deploys and manages the underlying OCP required Infrastructure in AWS based in the variables defined in the inventory.

As this is a shared environment, specific tags not related to OCP are added as well to every ec2 and ebs created objects so they can be easily identified. These can be found and modified under 'instance_tags' option on every ec2 instance creation.

Requirements
------------

Ansible version >= 2.4

Role Variables
--------------

The majority of the variables required to use the role are defined under the **cloud_infrastructure** object. This object definition is the representation for the underlaying infrastructure and all the required components to deploy an OpenShift Cluster on top of it.

Many of these required variables have default values. These are the **mandatory** variables you need to specify in order the role to work.

Infrastructure skeleton variables
---------------------------------

```yaml
cloud_infrastructure: **mandatory**
   region: **mandatory**
   image_name: **mandatory**
   masters: **mandatory**
     count: **defaulted**
     flavor: **defaulted**
     zones:
     - **at least 1 zone specification is mandatory**
     name_prefix: **defaulted**
     root_volume_size: **defaulted**
     docker_volume_size: **defaulted**
   etcdnodes: **not mandatory when deploying embedded etcd**
     count: **defaulted**
     flavor: **defaulted**
     zones:
     - **at least 1 zone specification is mandatory when NOT deploying embedded etcd**
     name_prefix: **defaulted**
     root_volume_size: **defaulted**
     docker_volume_size:**defaulted**
   appnodes: **mandatory**
     count: **defaulted**
     flavor: **defaulted**
     zones:
     - **at least 1 zone specification is mandatory**
     name_prefix: **defaulted**
     root_volume_size: **defaulted**
     docker_volume_size: **defaulted**
   infranodes: **mandatory**
     count: **defaulted**
     flavor: **defaulted**
     zones:
     - **at least 1 zone specification is mandatory**
     name_prefix: **defaulted**
     root_volume_size: **defaulted**
     docker_volume_size: **defaulted**
   cnsnodes: **not mandatory when CNS is not required**
     count: **mandatory when using CNS and with a fixed value of 3. If not using CNS this is defaulted to 0**
     flavor: **defaulted**
     zones:
     - **at least 1 zone specification is mandatory when using CNS**
     name_prefix: **defaulted**
     root_volume_size: **defaulted**
     docker_volume_size: **defaulted**
     gluster_volume_size: **defaulted**
```

Other variables
---------------

| Variable        | Description                           |
|:---------------:|:-------------------------------------:|
|**aws_access_key**| aws access key from AWS_ACCESS_KEY_ID environment variable
|**aws_secret_key**| aws Secret access key from AWS_SECRET_ACCESS_KEY environment variable
|**aws_key_name**| aws Key pair name to be used with the instances
|**group_masters_tag**| tag to create ec2 groups for master nodes to be used in the inventory
|**group_masters_etcd_tag**| tag to create ec2 groups for etcd embedded nodes to be used in the inventory
|**group_etcd_nodes_tag**| tag to create ec2 groups for etcd nodes to be used in the inventory
|**group_infra_nodes_tag**| tag to create ec2 groups for infra nodes to be used in the inventory
|**group_app_nodes_tag**| tag to create ec2 groups for compute nodes to be used in the inventory
|**group_cns_nodes_tag**| tag to create ec2 groups for CNS nodes to be used in the inventory
|**labels_masters_tag**| tag to feed master node labels in OCP
|**labels_etcd_nodes_tag**| tag to feed etcd node labels in OCP
|**labels_infra_nodes_tag**| tag to feed infra node labels in OCP
|**labels_app_nodes_tag**| tag to feed compute node labels in OCP
|**labels_cns_nodes_tag**| tag to feed CNS node labels in OCP
|**env_id**| environment ID to use for the Cluster
|**public_dns_domain**| public DNS Zone where to register de Cluster
OpenShift Cluster Administration Role
=============================

This role performs methods to ensure the health and stability of the OpenShift Container Platform Environment

## Management Features

* Pruning Builds
* Pruning Deployments
* Pruning Images
* Pruning Projects

## Required Parameters

The following parameters are required for the execution of this role

`openshift_token` - OAuth Token associated with a user/service account with *cluster-admin* permissions

## Additional Parameters

Each management action has a set of parameters to tailor its' execution. Management actions contained within this role are disabled by default unless explicitly enabled. The following parameters can be configured with a value of `True` ``to enable each management action:

`openshift_prune_builds`  - Pruning builds
`openshift_prune_deployments`  - Pruning deployments
`openshift_prune_images`  - Pruning images in the Integrated Docker Registry
`openshift_prune_projects`  - Pruning OpenShift projects

## Running Playbooks with this Role

Prune builds, deployments and images

```
ansible-playbook -e "openshift_token=<token> openshift_prune_builds=True openshift_prune_deployments=True openshift_prune_images=True openshift_prune_projects=True"
```

## NOTES

### Minimum Ansible Version

* Requires Ansible **2.2.1.x** or greater

### Hosting Environment

* This role is meant for execution on Linux hosts / targets and may not work correctly on other hosting operating systems.

# openshift-labels


# The CASL Ansible playbooks

## openshift-cluster-seed.yml (openshift-applier)

This playbook (and supporting components) have been moved to a separate repo: https://github.com/redhat-cop/openshift-applier
# Nagios Example Run

The `nagios-target` and `nagios-server` roles can be used to setup a complete Nagios monitoring for any environment. The `nagios-target` role will prepare the targets with the correct monitoring configuratoin for use with the NRPE (Nagios Remote Plugin Executor). The target role will selectively enable the correct monitoring plugins (and correctly configured) per targets.

Below is an example inventory file for setting up the Nagios server and targets. Before executing, ensure that access to the target servers is enabled - i.e.: SSH key login for root. 

Example run of the playbook:
> ansible-playbook -i \<path_to_inventory\> setup_nagios.yml


```
[all:vars]
ansible_ssh_user=root

# Infrastructure Server
[infra]
dns.infra.example.com nagios_services=dns
nfs.infra.example.com nagios_services=nfs

[infra:vars]
hostgroup_name=infra-servers
hostgroup_alias=Infrastructure Servers

# OpenShift 3 environment
[openshift]
master.openshift.example.com nagios_services=docker,openshift-master,openshift-node
node1.openshift.example.com nagios_services=docker,openshift-node
node2.openshift.example.com nagios_services=docker,openshift-node
node3.openshift.example.com nagios_services=docker,openshift-node
dns.openshift.example.com nagios_services=dns
nfs.openshift.example.com nagios_services=nfs

[openshift:vars]
hostgroup_name=openshift-cluster
hostgroup_alias=OpenShift Cluster (Environment #2)


###############################################################################
# The 'nagios-targets' definition is required
[nagios-targets:children]
infra
openshift

# The 'nagios-servers' definition is required
[nagios-servers]
nagios.example.com
```


Alm-Openshift
===

Automates the deployment of alm to Openshift.


Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Running alm-openshift is easy! Here's a sample playbook:

    - hosts: localhost 
      gather_facts: no
      connection: local
      roles:
         - { role: alm-openshift }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).Crate-Openshift
===

Automates the deployment of crate to Openshift.


Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Running crate-openshift is easy! Here's a sample playbook:

    - hosts: localhost 
      gather_facts: no
      connection: local
      roles:
         - { role: crate-openshift }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).