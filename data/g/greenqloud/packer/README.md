Packer Templates
================

*note:*

*GreenQloud provides no official support for this community repository*

GreenQloud's Packer Templates is a project that encapsulates [Packer](http://packer.io) templates for building virtual machine images for QStack. 

#Installation with docker

* Install docker (1.9.1+)
* docker pull qstack/packer
* Container prebuilt on dockerhub https://hub.docker.com/r/qstack/packer/

# Installation when installing on OS from scratch

You need

* qemu for building .qcow2 KVM images
* vmware (Fusion/Player) for building vmware .ova images
* packer


### rough install on Debian

	apt-get install git curl qemu unzip tofrodos

	curl -o /tmp/packer.zip https://releases.hashicorp.com/packer/0.10.1/packer_0.10.1_linux_amd64.zip

	unzip /tmp/packer.zip -d /opt/packer

	ln -s /opt/packer/packer /usr/bin/packer

	git clone https://github.com/greenqloud/packer.git
	cd packer/stable
	make


We have tested only on Debian 7, but you should get the same results anywhere if using latest stables of qemu and packer


# Stable templates (stable/)

go the the `stable` directory and issue `make`.  You will get a list of templates available and you can build them by issuing `make <templatename>-version_minorversion`

The finished template will be placed in a new directory called `output-<templatename>-version_minorversion`

Current stable templates:

* Debian 8.1
* Windows 2012 Standard R2
* Ubuntu 14.04
* Ubuntu 15.04

### disk size

You can control the disk size of the produced template by setting the `disk_size` parameter, for example: `make debian-8_1 disk_size=61440` (this would produce a 60GB template)

# Not fully tested templates (testing/)

These templates work the same way as the ones in the *stable* directory, although they have not been polished.  Go to the `testing` directory and you can `make` the templates.

Current "testing" templates:

* CoreOS stable
* Centos 7.0
* Debian 7.8


# Unstable templates (unstable/)

These are templates that are works in progress and may not be working at all. They should absolutely not be used in production, pull requests are welcome.


# "attic" directory

This has old deprecated stuff and is only here for historical (hysterical?) reasons.  This might be deleted at any moment.

# Quick testing of template

To see if the template boots and does most of what you want to do, you can run it on your packer server to do a quick glance through VNC, before registering and testing in QStack

	qemu-system-x86_64 -device virtio-net -drive file=debian-8.1-10240.qcow2,if=virtio,cache=writeback,discard=ignore -boot once=d -name test -machine type=pc,accel=kvm -m 4096M -vnc 0.0.0.0:1


# Registering templates in QStack

You can register them via the admin panel as described in the documentation, or via cloudmonkey

	# find ostypes
	cloudmonkey list ostypes
	cloudmonkey register template name="Debian 8.1 10GB" displaytext="Debian 8.1 10GB" zoneid=be25c4af-5c73-437c-9506-4cccc9aa5d52 hypervisor="kvm" format="qcow2" ostypeid=49759e4c-2a2c-11e5-b8ff-0242ac110007 bits=64 url="http://server.with.images/debian-8.1-10240.qcow2" ispublic=true isfeatured=true

# License & Authors

- Author: Jon Thor Kristinsson (<jon@greenqloud.com>)
- Author: Jordi Amorós (<jordi@greenqloud.com>)
- Author: Kristinn Soffanías Rúnarsson (<soffi@greenqloud.com>)


```text
Copyright 2015, Greenqloud (<support@greenqloud.com>)
```
