Requirements
============
To run these tests, first get the vagrant setup for the systemvm working,
see ../../tools/vagrant/systemvm.

Then, install dependencies

    pip install nose paramiko python-vagrant envassert cuisine fabric

Running tests
=============
Then run the tests using your favorite python unittest runner

    nosetests-2.7

If you have already started the systemvm with 'vagrant up', that VM will get
used for all the tests.

If you have not started the systemvm yet, it will be started and stopped for
every test case. That's nice for test isolation, but it's very slow, so it is
not recommended.

You can also run these tests out of the box with PyDev or PyCharm or whatever.

Adding tests
============
Simply create new test_xxx.py files with test cases that extend from
SystemVMTestCase.

Use [envassert](https://pypi.python.org/pypi/envassert) checks to define
your test assertions.

Use [cuisine](https://pypi.python.org/pypi/cuisine),
[fab](https://pypi.python.org/pypi/Fabric), or
[paramiko](https://pypi.python.org/pypi/paramiko) to otherwise interact with
the systemvm. When you do, please consider creating your own little wrappers
around fab run. I.e. the pattern is

```
from __future__ import with_statement
from fabric.api import run, hide

def something_to_do(argument):
    with hide("everything"):
        result = run("do something %s" % argument).wrangle()
        return "expected" in result
```

for a new kind of check and then in your test

```
class HelloSystemVMTestCase(SystemVMTestCase):
    @attr(tags=["systemvm"], required_hardware="true")
    def test_something(self):
        assert something_to_do('foo')
```

Edit, test, edit, test
======================
The SystemVM Vagrantfile sets up rsync from systemvm/patches. These rsyncs run
once, when you type 'vagrant up'. To do these rsyncs every time you change a
patch file, run 'vagrant rsync-auto'. With that, your development process can
be,

* once, start up vagrant with 'vagrant up'
* once, start up the rsync watcher with 'vagrant rsync-auto'
* iterate:
  * write a test, save the file
  * run 'nostests' to check that the test fails
  * change a systemvm script to help the test pass, save the file
  * vagrant rsyncs the changed file
  * run 'nosetests' to check that the test now passes

If you use PyDev or PyCharm you can set it up to watch your test files for
changes and auto-run any changed tests.
####################################################
 Note there is a new systemvm build script based on
 Veewee(Vagrant) under tools/appliance.
####################################################

1. The buildsystemvm.sh script builds a 32-bit system vm disk based on the Debian Squeeze distro. This system vm can boot on any hypervisor thanks to the pvops support in the kernel. It is fully automated
2. The files under config/ are the specific tweaks to the default Debian configuration that are required for CloudStack operation.
3. The variables at the top of the buildsystemvm.sh script can be customized:
	IMAGENAME=systemvm # dont touch this
	LOCATION=/var/lib/images/systemvm #
	MOUNTPOINT=/mnt/$IMAGENAME/ # this is where the image is mounted on your host while the vm image is built
	IMAGELOC=$LOCATION/$IMAGENAME.img
	PASSWORD=password # password for the vm
	APT_PROXY= #you can put in an APT cacher such as apt-cacher-ng
	HOSTNAME=systemvm # dont touch this
	SIZE=2000 # dont touch this for now
	DEBIAN_MIRROR=ftp.us.debian.org/debian 
	MINIMIZE=true # if this is true, a lot of docs, fonts, locales and apt cache is wiped out

4. The systemvm includes the (non-free) Sun JRE. You can put in the standard debian jre-headless package instead but it pulls in X and bloats the image. 
5. You need to be 'root' to run the buildsystemvm.sh script
6. The image is a raw image. You can run the convert.sh tool to produce images suitable for Citrix Xenserver, VMWare and KVM. 
   * Conversion to Citrix Xenserver VHD format requires the vhd-util tool. You can use the 
       -- checked in config/bin/vhd-util) OR
       -- build the vhd-util tool yourself as follows:
           a. The xen repository has a tool called vhd-util that compiles and runs on any linux system (http://xenbits.xensource.com/xen-4.0-testing.hg?file/8e8dd38374e9/tools/blktap2/vhd/ or full Xen source at http://www.xen.org/products/xen_source.html).
           b. Apply this patch: http://lists.xensource.com/archives/cgi-bin/mesg.cgi?a=xen-devel&i=006101cb22f6%242004dd40%24600e97c0%24%40zhuo%40cloudex.cn.
           c. Build the vhd-util tool
               cd tools/blktap2
               make
               sudo make install
   * Conversion to ova (VMWare) requires the ovf tool, available from 
       http://communities.vmware.com/community/vmtn/server/vsphere/automationtools/ovf
   * Conversion to QCOW2 requires qemu-img
Json file used to test the provisioning scripts on virtual appliances
These are the templates for the redundant router 
and redundant vpc_router
// Licensed to the Apache Software Foundation (ASF) under one
// or more contributor license agreements.  See the NOTICE file
// distributed with this work for additional information
// regarding copyright ownership.  The ASF licenses this file
// to you under the Apache License, Version 2.0 (the
// "License"); you may not use this file except in compliance
// with the License.  You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing,
// software distributed under the License is distributed on an
// "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
// KIND, either express or implied.  See the License for the
// specific language governing permissions and limitations
// under the License.
This project contains code for basic VNC, RDP, and HyperV (RDP) clients.

Usage: 
  java common.Client vnc|rdp|hyperv OPTIONS

Common options:
  --help|-h	Show this help text.
  --debug-link|-DL	Print debugging messages when packets are trasnferred via links.
  --debug-element|-DE	Print debugging messages when packets are received or sended by elements.
  --debug-pipeline|-DP	Print debugging messages in pipelines.
  --host|-n|--host-name VALUE	Name or IP address of host to connect to. Required.
  --width|-W VALUE	Width of canvas. Default value is "1024".
  --height|-H VALUE	Height of canvas. Default value is "768".

VNC options:
  --port|-p VALUE	Port of VNC display server to connect to. Calculate as 5900 + display number, e.g. 5900 for display #0, 5901 for display #1, and so on. Default value is "5901".
  --password|-P VALUE	Password to use. Required.

RDP options:
  --ssl-implementation|-j jre|apr|bco	Select SSL engine to use: JRE standard implementation, Apache Portable Runtime native library, BonuncyCastle.org implementation. Default value is "apr".
  --port|-p VALUE	Port of RDP server to connect to. Default value is "3389".
  --domain|-D VALUE	NTLM domain to login into. Default value is "Workgroup".
  --user|-U VALUE	User name to use. Default value is "Administrator".
  --password|-P VALUE	Password to use. If omitted, then login screen will be shown.

HyperV options:
  --ssl-implementation|-j jre|apr|bco	Select SSL engine to use: JRE standard implementation, Apache Portable Runtime native library, BonuncyCastle.org implementation. Default value is "apr".
  --port|-p VALUE	Port of HyperV server to connect to. Default value is "2179".
  --instance|-i VALUE	HyperV instance ID to use. Required.
  --domain|-D VALUE	NTLM domain to login into. Default value is "Workgroup".
  --user|-U VALUE	User name to use. Default value is "Administrator".
  --password|-P VALUE	Password to use. Required.


Limitations of VNC client:
  * only basic functionality work.

Limitations of RDP client:
  * it uses SSL/TLS;
  * NLA is not supported;
  * only basic functionality work.


To configure and start RDP service properly, run rdp-config.bat on server.
// Licensed to the Apache Software Foundation (ASF) under one
// or more contributor license agreements.  See the NOTICE file
// distributed with this work for additional information
// regarding copyright ownership.  The ASF licenses this file
// to you under the Apache License, Version 2.0 (the
// "License"); you may not use this file except in compliance
// with the License.  You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing,
// software distributed under the License is distributed on an
// "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
// KIND, either express or implied.  See the License for the
// specific language governing permissions and limitations
// under the License.

To debug RDP sessions with Network Monitor or Wireshark, you need to
configure RDP server with custom private key. For Network Monitor
Decrypt Expert, you also will need to downgrade RDP server TLS protocol
to version 1.0.

File dev-rdp-config.bat contains instructions to configure RDP to use custom
key, open firewall, disable NLA, downgrade TLS, and start RDP service.

File rdp.pfx contains custom private key (password: test) for use with
rdp-config.bat and Network Monitor Decrypt Expert. If you will generate
your own key, you will need to alter rpd-file.bat to use it
fingerprints.

File rdp-key.pem contains private key in PEM format for use with
Wireshark.

As alternative, mimikatz can be used to extract RDP private key.
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

sync-transifex-ui is a script to automate the synchronisation between
Apache CloudStack L10N resource files and Transifex CloudStack project.

Requirements to use this script:
* A GNU/Linux or Unix machine
* Transifex client installed
http://support.transifex.com/customer/portal/topics/440187-transifex-client/articles
On Debian/Ubuntu: apt-get install transifex-client

Commun usage is:

1/ Init and configure the transifex client CLI
(Already made on git CloudStack repo)

  ./sync-transifex-ui.sh init-transifex https://www.transifex.com/projects/p/CloudStack_UI/

2/ Upload to Transifex the last version of the source language (en)
which generally have the new keys/values to translate.

 ./sync-transifex-ui.sh upload-source-language CloudStack_UI.42xmessagesproperties

3/ Download the last L10N resource files from Transifex to resources
files directory in CloudStack tree to upade the L10N resource files
with the translatons from traductors.

 ./sync-transifex-ui.sh download-l10n-languages CloudStack_UI.42xmessagesproperties

=====
The sync-transifex-ui provide too the ability to :

* Download from Transifex the source language resource files. Be carrefully, 
with this,you can remove some transation on Transifex if some keys has 
been removed inside the source language resource files.

 ./sync-transifex-ui.sh download-source-language CloudStack_UI.42xmessagesproperties

* Upload the L10N resource files on Transifex. 

 ./sync-transifex-ui.sh upload-l10n-languages CloudStack_UI.42xmessagesproperties

=====
Note 1: 
Choose the good branch on git matching with the good resource on Transifex:
(no branch) <--> CloudStack_UI.2-2messagesproperties
(no branch) <--> CloudStack_UI.30xmessagesproperties
(4.1)       <--> CloudStack_UI.41xmessageproperties
(master)    <--> CloudStack_UI.42xmessagesproperties

Note 2:
If you want add a new L10N language, we need edit the sync-transifex-ui.sh script
to add his language code in LIST_LANG variable, before run the download-l10n-languages
command.


Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.

===========================================================

NOTE - This folder is a work in progress.  The project has not determined
how to best establish a nightly DevCloud build process, or how to distribute
the image.

===========================================================

# Setting up Tools and Environment

    - Install [RVM](https://rvm.io/rvm/install)
    - Setup paths:
          export PATH=~/.rvm/bin:$PATH
    - Install Ruby 1.9.3, if it installed some other version:
          rvm install 1.9.3

All the dependencies will be fetched automatically.

Vagrant: https://github.com/chipchilders/vagrant.git
Veewee:  https://github.com/jedi4ever/veewee.git

devcloudbase/Ubuntu: http://releases.ubuntu.com/12.04/ubuntu-12.04.1-server-i386.iso

To save some time if you've downloaded iso of your distro, put the isos in:
tools/devcloud/deps/boxes/basebox-build/iso/

Note, gem would require gcc-4.2, make sure link exists:

    sudo ln -s /usr/bin/gcc /usr/bin/gcc-4.2

# How to build DevCloud

DevCloud build scripts are in src/
Move to src/deps/ to start the build process:

    cd src/deps/

Clean up any old stuff:

    ./boxer.sh -c all

Build the dependent vms:

    ./boxer.sh -b all

Now, start DevCloud:

    # Go back to the devcloud homedir
    cd ../
    # Bring up the devcloud vm
    vagrant up

If you get a vagrant error, at that point, try:

    source .rvmrc
    vagrant up

# CloudStack Build Automation in DevCloud

If you want to compile cloudstack in the devcloud vm:

    vim puppet/modules/devcloud/manifests/params.pp

and set

    $build_cloudstack = true

alternately, if you do not want to build cloudstack in the devcloud vm, set:

    $build_cloudstack = false


It will now bring up the devcloud vm for this first time.  Note that it will
attempt to download the SSVM and CPVM templates so it will take a long time to
launch initially.  It will also git clone the cloudstack repository and attempt
to build an launch it.

You can optionally speed things up by packaging a successful devcloud instance
build.  This will make subsequent launches must faster since it won't have to
re-downoad the SSVM and CPVM.  Once it has successfully been built, you can run:

    #exports the devcloud vagrant instance and adds it as "devcloud" to vagrant boxlist
    ./boxit.sh
    #modifies the Vagrant file to use this newly added instance
    sed -i 's,devcloudbase-xen,devcloud,g' Vagrantfile
Moved to https://git-wip-us.apache.org/repos/asf?p=cloudstack-cloudmonkey.git
#Licensed to the Apache Software Foundation (ASF) under one
#or more contributor license agreements.  See the NOTICE file
#distributed with this work for additional information
#regarding copyright ownership.  The ASF licenses this file
#to you under the Apache License, Version 2.0 (the
#"License"); you may not use this file except in compliance
#with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing,
#software distributed under the License is distributed on an
#"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#KIND, either express or implied.  See the License for the
#specific language governing permissions and limitations
#under the License.


#Cloud AutoDeploy

Scripts here are used to refresh the builds of the management server with those
made out of our CI system. The CI system is internal at the moment.

###Dependencies
* Python
* [jenkinsapi](http://pypi.python.org/pypi/jenkinsapi)
* marvin

build.cfg - contains build information given to the CI system
        - branch, BUILDABLE_TARGET
        - distro of mgmt server tarball

You may leave the rest as they are defaults and should work fine.

environment.cfg - typically the VM where you intended to install above build of
mgmt server. SSH access to be available and credentials are in the config file.

deployment.cfg - the JSON network model configuration file generated by Marvin so
the mgmt server can be configured. See the Marvin tutorial on how to fetch these.

other options - skip-host - will skip IPMI/PXE refresh of the hosts
        - install-marvin - will pull the latest marvin tarball from the CI
          system and install it

Once you have the available configuration setup in the above .cfg files simply
run the following.

### 1a. reset the environment with the new build
`$ python configure.py -b build.cfg -e environment.cfg -d deployment.cfg [[--skip-host] --install-marvin]`

OR 

### b. reset the environment with specific build number
`$ python configure.py -n <build-number> -e environment.cfg -d deployment.cfg [[--skip-host] --install-marvin]`

### 2. restart mgmt server to have the integration port (8096) open
`$ python restartMgmt.py -e environment.cfg`

### 3. setup cloudstack with your deployment configuration
`$ nosetests -v --with-marvin --marvin-config=deployment.cfg --result-log=result.log -w /tmp`

### 4. restart again for global settings to be applied
`$ python restartMgmt.py -e environment.cfg`

### 5. wait for templates and system VMs to be ready
`$ nosetests -v --with-marvin --marvin-config=deployment.cfg --result-log=result.log testSetupSuccess.py`

#Licensed to the Apache Software Foundation (ASF) under one
#or more contributor license agreements.  See the NOTICE file
#distributed with this work for additional information
#regarding copyright ownership.  The ASF licenses this file
#to you under the Apache License, Version 2.0 (the
#"License"); you may not use this file except in compliance
#with the License.  You may obtain a copy of the License at
#http://www.apache.org/licenses/LICENSE-2.0
#Unless required by applicable law or agreed to in writing,
#software distributed under the License is distributed on an
#"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#KIND, either express or implied.  See the License for the
#specific language governing permissions and limitations
#under the License.

#UI for CloudStack using Angular.js
And a flask wrapper on top CloudStack API to make things easy on the client side.
Please put your systemVM into this location with the name: systemvmtemplate.vhd.bz2
Please put your tinyVHD image into this location with the name: ce5b212e-215a-3461-94fb-814a635b2215.vhd
Also put the template.properties file for the tinyVHD image into this location.
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.

===========================================================

Allows spinning up the systemvm appliance from ../../appliance inside
vagrant, and then running tests against it with nose.

To use, install vagrant, rvm, ruby, bundler, python and pip.
Then run ./test.sh.

To write tests, create files underneath ../../../test/systemvm
named test_xxx.py. These tests are standard python unit tests with
some logic to SSH into the SystemVM. See
../../../test/systemvm/README.md for more info.

Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.

===========================================================

This directory hosts configs for setting up the devcloud-kvm
environment.
# Devcloud 4

## Introduction

The follow project aims to simplify getting a full Apache CloudStack environment running on your machine. You can either take the easy ride and run `vagrant up` in either one of the 'binary installation' directories or compile CloudStack yourself. See for instructions in the 'basic' and 'advanced' directories.

The included VagrantFile will give you:

 - Management
     - NFS Server
     - MySQL Server
     - Router
     - * Cloudstack Management Server * (Only given in binary installation)

 - XenServer 6.2

## Getting started

1. Due to the large amount of data to be pulled from the Internet, it's probably not a good idea to do this over WiFi or Mobile data.

1. Given the amount of virtual machines this brings up it is recommended you have atleast 8gb of ram before attempting this.

1. Ensure your system has `git` installed.

1. When on Windows, make sure you've set the git option `autocrlf` to `false`:

      ```
      git config --global core.autocrlf false
      ```

1. Clone the repository:

	```
	git clone https://github.com/imduffy15/devcloud4.git
	```

1. Download and Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
   
   On Windows7, the Xenserver VM crashed immediately after booting with a General Protection Fault. 
   Installing VirtualBox version 4.3.6r91406 (https://www.virtualbox.org/wiki/Download_Old_Builds_4_3) fixed the problem, but only downgrade if the latest version does not work for you.
 
1. Download and install [Vagrant](https://www.vagrantup.com/downloads.html)

1. Ensure all Vagrant Plugins are installed:

	```bash
	vagrant plugin install vagrant-berkshelf vagrant-omnibus
	```

1. Download and install [ChefDK](https://downloads.chef.io/chef-dk/)

### Configure virtualbox

1. Open virtualbox and navigate to its preferences/settings window. 

1. Click onto the network tab and then onto the host only network tab. 

1. Configure your adapters as follows:

   - On Windows, the adapternames are different, and map as follows:
     - vboxnet0: VirtualBox Host-Only Ethernet Adapter
     - vboxnet1: VirtualBox Host-Only Ethernet Adapter 2
     - vboxnet2: VirtualBox Host-Only Ethernet Adapter 3
    
    #### For Basic Networking you only need:

    ##### vboxnet0
    - IPv4 IP address of 192.168.22.1
    - Subnet of 255.255.255.0
    - DHCP server disabled
    
    #### For Advanced Networking you will need:
    
    
    
    ##### vboxnet1
    - IPv4 IP address of 192.168.23.1
    - Subnet of 255.255.255.0
    - DHCP server disabled
    
    
    
    ##### vboxnet2
    - IPv4 IP address of 192.168.24.1
    - Subnet of 255.255.255.0
    - DHCP server disabled

## Defaults

### Management Server

 - IP: 192.168.22.5
 - Username: vagrant or root
 - Password: vagrant

### Hypervisor

 - IP: 192.168.22.10
 - Username: root
 - Password: password
    
### Configure virtualbox

1. Open virtualbox and navigate to its preferences/settings window. 

1. Click onto the network tab and then onto the host only network tab. 

1. Configure your adapters as follows:

    ##### vboxnet0
    - IPv4 IP address of 192.168.22.1
    - Subnet of 255.255.255.0
    - DHCP server disabled
    
    ##### vboxnet1
    - IPv4 IP address of 192.168.23.1
    - Subnet of 255.255.255.0
    - DHCP server disabled
    
    ##### vboxnet2
    - IPv4 IP address of 192.168.24.1
    - Subnet of 255.255.255.0
    - DHCP server disabled
    
   
### Start the vagrant boxes

```bash
vagrant up
```

*** Common issues: ***

- 'Cannot forward the specified ports on this VM': There could be MySQL or some other
  service running on the host OS causing vagrant to fail setting up local port forwarding.


### Start Cloudstack

1. Clone the Cloudstack Repository:

	```
	git clone https://github.com/apache/cloudstack.git
	```

	*** Note: ***
	
	Personally I prefer to use the 4.3 codebase rather than master. If you wish to do the same:	

	```
	git reset --hard 0810029
	```

1. Download vhd-util:

	```bash
	cd /path/to/cloudstack/repo
	wget http://download.cloud.com.s3.amazonaws.com/tools/vhd-util -P scripts/vm/hypervisor/xenserver/
	chmod +x scripts/vm/hypervisor/xenserver/vhd-util
	```

1. Compile Cloudstack:

	```bash
	cd /path/to/cloudstack/repo
	mvn -P developer,systemvm clean install -DskipTests=true
	```
	
1. Deploy Cloudstack Database:

	```bash
	cd /path/to/cloudstack/repo
	mvn -P developer -pl developer,tools/devcloud4 -Ddeploydb
	```

1. Start Cloudstack:

	```bash
	cd /path/to/cloudstack/repo
	mvn -pl :cloud-client-ui jetty:run
	```

1. Install Marvin:

	```
	cd /path/to/cloudstack/repo
	pip install tools/marvin/dist/Marvin-0.1.0.tar.gz
	```

1. Deploy:

    ```
    python -m marvin.deployDataCenter -i marvin.cfg 
    ```


### Configure virtualbox

1. Open virtualbox and navigate to its preferences/settings window. 

1. Click onto the network tab and then onto the host only network tab. 

1. Configure your adapters as follows:

    ##### vboxnet0
    - IPv4 IP address of 192.168.22.1
    - Subnet of 255.255.255.0
    - DHCP server disabled
    

### Start the vagrant boxes

```bash
vagrant up
```

*** Common issues: ***

- 'Cannot forward the specified ports on this VM': There could be MySQL or some other
  service running on the host OS causing vagrant to fail setting up local port forwarding.


### Start Cloudstack

1. Clone the Cloudstack Repository:

	```
	git clone https://github.com/apache/cloudstack.git
	```

	*** Note: ***
	
	Personally I prefer to use the 4.3 codebase rather than master. If you wish to do the same:	

	```
	git reset --hard 0810029
	```

1. Download vhd-util:

	```bash
	cd /path/to/cloudstack/repo
	wget http://download.cloud.com.s3.amazonaws.com/tools/vhd-util -P scripts/vm/hypervisor/xenserver/
	chmod +x scripts/vm/hypervisor/xenserver/vhd-util
	```

1. Compile Cloudstack:

	```bash
	cd /path/to/cloudstack/repo
	mvn -P developer,systemvm clean install -DskipTests=true
	```
	
1. Deploy Cloudstack Database:

	```bash
	cd /path/to/cloudstack/repo
	mvn -P developer -pl developer,tools/devcloud4 -Ddeploydb
	```

1. Start Cloudstack:

	```bash
	cd /path/to/cloudstack/repo
	mvn -pl :cloud-client-ui jetty:run
	```

1. Install Marvin:

	```
	cd /path/to/cloudstack/repo
	pip install tools/marvin/dist/Marvin-4.6.0-SNAPSHOT.tar.gz --allow-external mysql-connector-python
	```

1. Deploying:

    ```
    python -m marvin.deployDataCenter -i marvin.cfg 
    ```
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.

===========================================================

# Setting up Tools and Environment

    - Install latest VirtualBox (at least 4.2)
    - Install tools for exporting appliances: qemu-img, vboxmanage, vhd-util
    - Install [RVM](https://rvm.io/rvm/install)
    - Install shar
          yum install sharutils
    - Setup paths:
          export PATH=~/.rvm/bin:$PATH
    - Install Ruby 1.9.3, if it installed some other version:
          rvm install 1.9.3
    - Set rvm to use that 1.9.3
          rvm use ruby-1.9.3
    - Install bundler: (if you get any openssl issue see https://rvm.io/packages/openssl)
          gem install bundler

All the dependencies will be fetched automatically.

To save some time if you've downloaded iso of your distro, put the isos in:
tools/appliance/iso/

Note, gem may require gcc-4.2, make sure link exists:

    sudo ln -s /usr/bin/gcc /usr/bin/gcc-4.2

# Setting up jenkins (CI) builds

All the tools listed above are expected to be available. If you follow

    http://rvm.io/integration/jenkins

then you'll need to do a bit of logic to load RVM in jenkins. In the
build script you put into jenkins, start it with
```
#!/bin/bash -l
```

to ensure a login shell, then add something like
```
# inspired by https://github.com/CloudBees-community/rubyci-clickstart/blob/master/bin/run-ci
# also see https://rvm.io/integration/jenkins
# .rvmrc won't get trusted/auto-loaded by jenkins by default
export VAGRANT_HOME=$HOME/.vagrant.d-release-cloudstack
rvm use ruby-1.9.3@vagrant-release-cloudstack --create
# do not use --deployment since that requires Gemfile.lock...and we prefer an up-to-date veewee
bundle_args="--path vendor/bundle"
```


# How to build SystemVMs automatically

Just run build.sh, it will export archived appliances for KVM, XenServer,
VMWare and HyperV in `dist`:

    bash build.sh [systemvmtemplate|systemvmtemplate64]

# Building SystemVM template appliance manually

List available appliances one can build:

    veewee vbox list

Modify scripts in definitions/*appliance*/ as per needs.
Build systemvm template appliance:

    veewee vbox build 'systemvmtemplate'

Start the box:

    veewee vbox up 'systemvmtemplate'

Halt the box:

    veewee vbox halt 'systemvmtemplate'

Now VirtualBox can be used to export appliance.

To build the systemvm64template by hand using veewee, set VM_ARCH=amd64 and use
the systemvmtemplate:

    export VM_ARCH=amd64
    cp -r definitions/systemvmtemplate definitions/systemvm64template
    veewee vbox build 'systemvm64template'

Troubleshooting
===============
If you see following line in the screen, then veewee is failing 
extracting vboxmanage version.

    Downloading vbox guest additions iso v  - http://download.virtualbox.org/vi

You would be able to check it manually by typing:

    vboxmanage --version

If you're using Fedora for example, you'll need to install `kernel-devel`
package and run `/etc/init.d/vboxdrv setup` to get veewee working.

Testing
=======
The ./test.sh script tries out a few different default ways to invoke build.sh.

See ../vagrant/systemvm for a test setup that uses vagrant+serverspec to
provide actual integration tests that verify the built systemvm is up to spec.
What this tool is capable to do is

1.	Compare all the tables schema between upgraded setup and fresh install setup  and find if there is any schema difference between any tables
2.	Compare global configuration between upgraded and fresh install setup and find out if there is any difference between the two on following fields
	a.	Value
	b.	Scope
	c.	Description
	d.	Component
	e.	Category

3.	It will also find out if there is some global configuration present only in fresh setup and missing in upgraded environment and vice versa
4.	It will also find out global configuration value difference between before upgraded and after upgrade setup



The usage is as follows
1.	First run fresh_install_data_collection.sh file to generate data from fresh install setup .
	This will be used for comparing between fresh install and upgrade setup. 
	This is a onetime activity and need to be repeated only when there is some DB changes for that release .
	Output of this script will come in a base_data folder 

2.	Just before upgrade you need to run before_upgrade_data_collection.sh  file to collect required data needed to compare before upgrade and after upgrade setup data
	The output of this script will come in folder data_before_upgrade

3.	After upgrade  run cloud_schema_comparision.sh to compare cloud database all tables schema between fresh and upgraded setup. 
	NOTE: this script requires step 1 output in current working directory

4.	After upgrade  run usage_schema_comparision.sh to compare cloud usage all tables schema between fresh and upgraded setup
	NOTE: this script requires step 1 output in current working directory

5.      Run test_config_between_fresh_and_upgraded_setup.sh  to comapre table global configuration values between fresh and upgraded setup 
	NOTE: this script requires step 1 output in current working directory


6.      Run test_config_before_and_after_upgrade.sh  to comapre table global configuration values between before upgraded and after upgraded setup
	NOTE: this script requires step 2  output in current working directory


7.	In order to run any *.sh file  you need to provide 3 command line argument
	•	Database host ip/localhost
	•	Database user
	•	Database user password

8.	Result will be shown in the form of files . 

