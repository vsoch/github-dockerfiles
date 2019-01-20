# Local Testing Setup

This directory contains a Docker configuration to run a NodePool integration environment.  In its current configuration,
it is most useful for development testing of the Jenkins plugin.

## Prerequisite

1. Docker (18.x or better)
1. Docker Compose (v1.20.1 or better)
1. OpenStack Cloud Account
1. OpenStack Command Line Tools (if manually creating a base OpenStack virtual machine image)
   * Install Python >2.7 or Python >3.6
   * Optionally install/leverage a python virtual environment (virtualenv)
   * To install, run: `pip install python-openstackclient`
1. A base OpenStack virtual machine image that matches the `nodepool.yaml` setup.  See instructions below.

## Setup

Steps to do plugin development work:

1. Change to the docker folder: `cd docker`.
1. Set the following environment variables.  These are used by the various configuration files.
   1. `KEYPAIR_NAME` environment variable to the name of your keypair used with the region of Rackspace public cloud. (e.g. `export KEYSPAIR_NAME=mykeypair`)
   1. `NODEPOOL_CLOUD_NAME` - the openstack cloud configuration definition from the `~/.config/openstack/clouds.yaml` file
   1. `NODEPOOL_REGION_NAME` - specifies the OpenStack region - typically one of `["DFW", "IAD", "ORD", "LON"]`
   1. `NODEPOOL_KEYPAIR_NAME` - specifies a previously registered KeyPair to use for the Jenkins slaves
   1. If testing with an IDE, don't forget to set these variables in the debugger profile.
1. Review the `nodepool.yaml` configuration file. This file will be used to start a single cloud server instance of
   Debian Stretch or Ubuntu Xenial (as indicated in the `labels` and `providers` section).
1. docker-compose build - builds the docker image in the current folder
1. docker-compose up - brings up the collection of docker images in the foreground (use `-d` to run in the background)
   Optional: run `docker-compose -f docker-compose-jenkins.yml up` to run Jenkins within a container (review the version
   defined within the YML file to match your desired Jenkins release).  If using this option, you'll need to manually 
   install the nodepood plugin by running `mvn hpi:hpi` from the project root folder to generate the 
   `target/nodepool-agents.hpi` file, log into the Jenkins instance, and upload the plugin.  Configuration is the same
   as below, except use `zookeeper` instead of the loopback address.

Once everything starts, there should be 4-5 containers running:

1. `docker_nodepool_launcher` - container responsible for launching for managing a pool of cloud server nodes.
1. `docker_nodepool_builder` - TODO/optional container responsible for automatically creating a base VM image to use as the Jenkins slave
1. `elkozmon/zoonavigator-web` - a ZooKeeper GUI interface for CRUD operations
1. `elkozmon/zoonavigator-api` - the accompanying ZooKeeper API server for the GUI
1. `zookeeper` - one or more zookeeper instance(s) which NodePool depends on

There is also a `sh` script in this directory for convenience access to the containers' shells.

## Start Jenkins with NodePool

How to configure and run jobs via the NodePool plugin:

1. First complete the above steps.  Ensure the local containers are up and running without any errors.
1. Run `mvn hpi:run` from the project root directory. Use `-Djetty.port=8080` to specify the port explicitly.  Use 
   `mvn hpi:run -Dhpi.prefix=/jenkins` to specify the prefix path. `MAVEN_OPTS` can be used to specify all sorts of 
   other JVM parameters, like `-Xmx`.
1. Open Jenkins in a browser window at http://localhost:8080/jenkins
1. Create a "Nodepool Cloud" configuration entry
    * Click "Manage Jenkins" => "Configure System"
    * Near the top, change the "Labels" value to a value different than the default "master". Example: "master-2". This
      will allow Items/Jobs to set a Restriction on where the project can run without using additional plugins.
    * Near the bottom of the page, find the "Nodepool Cloud" configuration options.
    * Connection string should be `127.0.0.1:2181`.  Fill this in and test it.  It should connect to your local ZK 
      instance without error.
    * Fill out the Instance Credentials section. If necessary, fill out a new Jenkins Credentials Provider. The form 
      assumes that you've previously established an SSH KeyPair with OpenStack.  You will need to provide the 
      private key associated with the KeyPair.
    * Under Label Prefix, select a unique/arbitrary label to describe the cloud pool (e.g. `nodepool-yourname-`)
    * Save the changes
1. Update Plugins (Optional)
    * Click "Manage Jenkins" => "Manage Plugins"
    * Update all the plugins
    * Restart the server by going to "Manage Jenkins" => "Prepare for Shutdown", then http://localhost:8080/jenkins/restart
1. Create a Jenkins job to test the NodePool plugin
    * Select "New Item" from the main menu, enter a item name/job name (such as "Test"), select "Freestyle project" to
      keep it simple and press "OK".
    * From the "General" tab, click the "Restrict where this project can be run" and for "Label Expression" add a value
      such as `nodepool-yourname-debian` to match the Label Prefix specified in the Jenkins "Configure System" page and
      the name of the cloud server instance defined in the `nodepool.yaml` configuration file.
    * Under the "Build" section, configure a simple shell script to run. Provide a simple shell command such as
      `echo "Hello, world"` by selecting "Add build step" and choosing "Execute shell".
    * Click "Save" to complete the setup.
1. Run the Job
    * Select the Job that was just created (e.g. Test) - then select "Build Now"
    * If Jenkins can't find the label it will be in pending state.  Double check your settings and configuration.
    * Optionally check the NodePool View: http://localhost:8080/jenkins/nodepool-view/ for a summary of the NodePool
      slave instances.

## Create Base Image

The goal of a base image is to start with an image that includes all the tools needed to support builds as a Jenkins
slave.  For many of our jobs, Java 8 needs to be installed.  Each project/team may have additional requirements such as 
build tools, source code control tools, and even docker/container libraries.

There are two ways to establish a base image to use as the Jenkins Nodepool slave virtual machine:

1. Create an image manually
1. Leverage the Docker NodePool Builder

This section describes how to manually create a base image using the OpenStack command line tools.

### Determine Base Image

Review your `~/.config/openstack/clouds.yaml` configuration file to determine the `--os-cloud` property value.

Query OpenStack for list of available base images.  In this example, we'll leverage Debian 9 - note the ID value.

```bash
openstack --os-cloud daviddeal image list
```

Typical results may include:

```code
+--------------------------------------+--------------------------------------------------------------+--------+
| ID                                   | Name                                                         | Status |
+--------------------------------------+--------------------------------------------------------------+--------+
| 8b87aed3-1e19-4c7d-89fa-daeb734058d6 | ASC-prototype_PyPI + users                                   | active |
| 9dd4042f-8892-4128-96db-dc915665cabc | CentOS 6 (PVHVM)                                             | active |
| 996b367c-3be0-49b2-a92d-89260d11eb3f | CentOS 7 (PVHVM)                                             | active |
| 72af39fe-0521-446a-a6de-19e81416fc6a | CentOS 7 (PVHVM) (Orchestration)                             | active |
| 5d954038-4f3a-4d5a-8026-47ce408f23e4 | CoreOS (Alpha)                                               | active |
| b2da5e7e-8c0f-43c5-9e53-99560e4be8d2 | CoreOS (Beta)                                                | active |
| 4304f242-c66c-4e6e-ad29-59c4a5605a12 | CoreOS (Stable)                                              | active |
| 22cd4526-66c5-4653-8c45-5ebb4007d1d1 | Debian 7 (Wheezy) (PVHVM)                                    | active |
| 7f18f6ba-4cca-4ef4-adb7-081a15883c0a | Debian 8 (Jessie) (PVHVM)                                    | active |
| 50d38165-06f8-4415-9b69-6dc08c1eb664 | Debian 9 (Stretch) (PVHVM)                                   | active |
| dc096800-4ed2-4934-8ac4-88cc7befcf3b | Fedora 26 (PVHVM)                                            | active |
| d88a4c90-3a1d-4458-b174-4290962a14a9 | Fedora 27 (PVHVM)                                            | active |
...more...
| f648f153-270e-41a9-a679-834a77c9659d | ubuntu-trusty                                                | active |
| b56a03c3-3664-4724-9bdc-54c6ffca4d7a | wserverbak                                                   | active |
+--------------------------------------+--------------------------------------------------------------+--------+
```

### Determine OS Size/Flavor

Next, list the available flavors of the virtual machine.  Choose a size - the virtual machine that we use is only for
making a snapshot.  Therefore, a small virtual machine is adequate.

```bash
openstack --os-cloud daviddeal flavor list
```

Typical results may include:

```code
+-------------------------+-----------------------------------+--------+------+-----------+-------+-----------+
| ID                      | Name                              |    RAM | Disk | Ephemeral | VCPUs | Is Public |
+-------------------------+-----------------------------------+--------+------+-----------+-------+-----------+
| 2                       | 512MB Standard Instance           |    512 |   20 |         0 |     1 | N/A       |
| 3                       | 1GB Standard Instance             |   1024 |   40 |         0 |     1 | N/A       |
| 4                       | 2GB Standard Instance             |   2048 |   80 |         0 |     2 | N/A       |
| 5                       | 4GB Standard Instance             |   4096 |  160 |         0 |     2 | N/A       |
| 6                       | 8GB Standard Instance             |   8192 |  320 |         0 |     4 | N/A       |
| 7                       | 15GB Standard Instance            |  15360 |  620 |         0 |     6 | N/A       |
| 8                       | 30GB Standard Instance            |  30720 | 1200 |         0 |     8 | N/A       |
| compute1-15             | 15 GB Compute v1                  |  15360 |    0 |         0 |     8 | N/A       |
| compute1-30             | 30 GB Compute v1                  |  30720 |    0 |         0 |    16 | N/A       |
| compute1-4              | 3.75 GB Compute v1                |   3840 |    0 |         0 |     2 | N/A       |
| compute1-60             | 60 GB Compute v1                  |  61440 |    0 |         0 |    32 | N/A       |
| compute1-8              | 7.5 GB Compute v1                 |   7680 |    0 |         0 |     4 | N/A       |
| general1-1              | 1 GB General Purpose v1           |   1024 |   20 |         0 |     1 | N/A       |
| general1-2              | 2 GB General Purpose v1           |   2048 |   40 |         0 |     2 | N/A       |
| general1-4              | 4 GB General Purpose v1           |   4096 |   80 |         0 |     4 | N/A       |
| general1-8              | 8 GB General Purpose v1           |   8192 |  160 |         0 |     8 | N/A       |
| io1-120                 | 120 GB I/O v1                     | 122880 |   40 |      1200 |    32 | N/A       |
| io1-15                  | 15 GB I/O v1                      |  15360 |   40 |       150 |     4 | N/A       |
...more...
| performance1-1          | 1 GB Performance                  |   1024 |   20 |         0 |     1 | N/A       |
| performance1-2          | 2 GB Performance                  |   2048 |   40 |        20 |     2 | N/A       |
| performance1-4          | 4 GB Performance                  |   4096 |   40 |        40 |     4 | N/A       |
| performance1-8          | 8 GB Performance                  |   8192 |   40 |        80 |     8 | N/A       |
| performance2-120        | 120 GB Performance                | 122880 |   40 |      1200 |    32 | N/A       |
| performance2-15         | 15 GB Performance                 |  15360 |   40 |       150 |     4 | N/A       |
| performance2-30         | 30 GB Performance                 |  30720 |   40 |       300 |     8 | N/A       |
| performance2-60         | 60 GB Performance                 |  61440 |   40 |       600 |    16 | N/A       |
| performance2-90         | 90 GB Performance                 |  92160 |   40 |       900 |    24 | N/A       |
+-------------------------+-----------------------------------+--------+------+-----------+-------+-----------+
```

### Manually Provision Node

Now that we have enough details, we can create a virtual machine of the appropriate size and type.

```bash
openstack --os-cloud daviddeal server create \
  --image 50d38165-06f8-4415-9b69-6dc08c1eb664 \
  --flavor performance1-1 \
  --key-name openstack_dd \
  test-dd
```

Should get something similar to this:

```code
+------------------------+-------------------------------------------------------------------+
| Field                  | Value                                                             |
+------------------------+-------------------------------------------------------------------+
| OS-DCF:diskConfig      | MANUAL                                                            |
| OS-EXT-STS:power_state | NOSTATE                                                           |
| OS-EXT-STS:task_state  | scheduling                                                        |
| OS-EXT-STS:vm_state    | building                                                          |
| accessIPv4             |                                                                   |
| accessIPv6             |                                                                   |
| addresses              |                                                                   |
| adminPass              | someadminpasswordvalue                                            |
| created                | 2018-03-27T21:43:21Z                                              |
| flavor                 | 1 GB Performance (performance1-1)                                 |
| hostId                 |                                                                   |
| id                     | b7688888-cccc-cccc-bbbb-ccceeee2cc0e                              |
| image                  | Debian 9 (Stretch) (PVHVM) (50d38165-06f8-4415-9b69-6dc08c1eb664) |
| key_name               | openstack_dd                                                      |
| name                   | test-dd                                                           |
| progress               | 0                                                                 |
| project_id             | 123456                                                            |
| properties             |                                                                   |
| status                 | BUILD                                                             |
| updated                | 2018-03-27T21:43:21Z                                              |
| user_id                | 000000111111222222333333444                                       |
+------------------------+-------------------------------------------------------------------+
```

### Check Status

Once the virtual machine is booted, we need to wait until it's available.  Use `server show` to query for the status.

```bash
openstack --os-cloud daviddeal server show test-dd
```

We're expecting a status of `ACTIVE` once the virtual machine is up and ready.

```code
+--------------------------------------+--------------------------------------------------------------------------------------+
| Field                                | Value                                                                                |
+--------------------------------------+--------------------------------------------------------------------------------------+
| OS-DCF:diskConfig                    | MANUAL                                                                               |
| OS-EXT-STS:power_state               | Running                                                                              |
| OS-EXT-STS:task_state                | None                                                                                 |
| OS-EXT-STS:vm_state                  | active                                                                               |
| RAX-PUBLIC-IP-ZONE-ID:publicIPZoneId | a8353c2fce691111777888333334444                                                      |
| accessIPv4                           | 104.XXX.XXX.XXX                                                                      |
| accessIPv6                           | 2001:4800:7819:104:be76:4eff:fe04:a205                                               |
| addresses                            | public=104.XXX.XXX.XXX, 2000:0000:000:000:0000:0000:0000:0000; private=10.200.00.28  |
| created                              | 2018-03-27T21:43:21Z                                                                 |
| flavor                               | 1 GB Performance (performance1-1)                                                    |
| hostId                               | 30424a3da8fbcdbbf31e88888888888888888888888888                                       |
| id                                   | b7655237-3f1c-42fc-bae6-c60ee382030e                                                 |
| image                                | Debian 9 (Stretch) (PVHVM) (55555555-dddd-aaaa-bbbb-CCCCCCCCCCCC)                    |
| key_name                             | openstack_dd                                                                         |
| name                                 | test-dd                                                                              |
| progress                             | 100                                                                                  |
| project_id                           | 123456                                                                               |
| properties                           | rax_service_level_automation='Complete'                                              |
| status                               | ACTIVE                                                                               |
| updated                              | 2018-03-27T21:44:40Z                                                                 |
| user_id                              | 000000111111222222333333444                                                          |
+--------------------------------------+--------------------------------------------------------------------------------------+
```

### Log Into the Virtual Machine

To log into the newly created virtual machine, review the public IP address from the virtual machine status output above
and locate your private OpenStack SSH key (typically in the `~/.ssh` folder).  Here's an example session:

```bash
ssh -i ~/.ssh/openstack_dd_id_rsa root@104.XXX.XXX.XXX
```

### Install Additional Tools

This is an example of installing OpenJDK version 8 onto the Debian virtual machine.

```code
apt-get update && apt-get install openjdk-8-jdk -y
```

A more through example might look like:

```bash
# the location to fetch the public keys from
SSH_PUBLIC_KEYS_URL="https://raw.githubusercontent.com/rcbops/rpc-gating/master/keys/rcb.keys"

# fetch the public keys and put them inside the chroot
curl --connect-timeout 5 \
     --retry 3 \
     ${SSH_PUBLIC_KEYS_URL} > /tmp/ssh-public-keys

##
## Add jenkins user, group.
##
JENKINS_HOME="/var/lib/jenkins"
groupadd jenkins
useradd --gid jenkins \
        --shell /bin/bash \
        --home-dir ${JENKINS_HOME} \
        --create-home jenkins

mkdir -p ${JENKINS_HOME}/.ssh
chmod 700 ${JENKINS_HOME}/.ssh

cp /tmp/ssh-public-keys ${JENKINS_HOME}/.ssh/authorized_keys
chmod 644 ${JENKINS_HOME}/.ssh/authorized_keys

cat > /etc/sudoers.d/jenkins << EOF
jenkins ALL=(ALL) NOPASSWD:ALL
EOF
chmod 0440 /etc/sudoers.d/jenkins

# ensure everything has the right owner
chown -R jenkins:jenkins ${JENKINS_HOME}

# ensure the right version of openjdk is available
source /etc/lsb-release
if [[ "${DISTRIB_CODENAME}" == "trusty" ]]; then
  add-apt-repository -y ppa:openjdk-r/ppa
fi

# install the openjdk
pkgs_to_install=""
dpkg-query --list | grep openjdk-8-jre-headless &>/dev/null || pkgs_to_install+="openjdk-8-jre-headless"
if [ "${pkgs_to_install}" != "" ]; then
  apt-get update
  apt-get install -y ${pkgs_to_install}
fi
```

### List Services

Determine the desired virtual machine ID by useing `server list`.

```bash
openstack --os-cloud daviddeal server list
```

```code
...output truncated
| 55555555-dddd-aaaa-bbbb-CCCCCCCCCCCC | test-dd | ACTIVE | public=104.XXX.XXX.XXX, 2000:0000:000:000:0000:0000:0000:0000; private=10.200.00.28 | Debian 9 (Stretch) (PVHVM) | 1 GB Performance|
...
```

### Create the New Image

Using the virtual machine ID value, create the image by providing the region and an image name. 

```code
openstack --os-region-name DFW \
    server image create \
    --name nodepooljava-dd \
    55555555-dddd-aaaa-bbbb-CCCCCCCCCCCC
```



Optionally, add tags to the image:

```bash
openstack --os-region-name DFW \
  image set \
  --tag debian \
  --tag debian9 \
  --tag openjdk \
  --tag java \
  --tag nodepool \
  nodepool-dd-debian-java
```

### Check Image Progress

Creating an image takes some time.  Initially it will be in a `queued` status state.  To check status/progress, use the
`image list` command:

```bash
openstack --os-cloud daviddeal image list --long
```

### Delete Virtual Machine

Once the image has been created, clean up by deleting the virtual machine using the `delete server` command.

```bash
openstack --os-cloud daviddeal server delete test-dd
```

### Provision Node via Teraform

See the [OpenStack Provider Notes](https://www.terraform.io/docs/providers/openstack/index.html)
