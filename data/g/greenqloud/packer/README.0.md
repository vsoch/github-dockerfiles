# qstack-templates-centos7# Ubuntu packer templates

## Create image

```bash
read -p 'Enter password: ' -s password
packer build -var 'user=ubuntu' -var "password=$password" ubuntu-14.04-server-amd64.json
```

## Software pre-installed

Look in scripts/packages.sh


# Installation when installing on OS from scratch

You need

* qemu for building .qcow2 KVM images
* vmware (Fusion/Player) for building vmware .ova images
* packer

# Creating templates

Issue `make`.  You will get a list of templates available and you can build them by issuing `make <templatename>-version_minorversion`

The finished template will be placed in a new directory called `output-<templatename>-version_minorversion`

### Disk size

You can control the disk size of the produced template by setting the `disk_size_gb` parameter, for example: `make centos-7-vmware disk_size_gb=60` (this would produce a 60GB template)

# Stable templates :

* Centos 6.8
* Centos 7


# Ubuntu packer templates

## Create image

```bash
read -p 'Enter password: ' -s password
packer build -var 'user=ubuntu' -var "password=$password" ubuntu-14.04-server-amd64.json
```

## Software pre-installed

Look in scripts/packages.sh



ovftool --compress=9 output-windows-2012-standard.r2/windows-2012-standard.r2-0-vmware.vmx soffi2.ova
## Time on medium specced server

time to build with packer: ~25mins
time to upload to s3 on 1gbit: ~7mins
download template to QS and register: ~5mins
boot first instance and test: ~5mins

## Windows Packer Templates

* Virtio drivers are loaded on startup
* Configured as 2 CPU and 4 GB memory by default
* No updates or services packs applied
* Firewall is disabled
* RDP enabled
* Powershell is installed with Remote Execution policy is set to unrestricted

The OS can be evaluated for 180-days. http://technet.microsoft.com/en-US/evalcenter/dn205286.aspx

### Quick Start

```bash
$ packer build windows-2012-R2-standard-amd64.json
```

### Windows 2012 R2 Standard

* User Administrator
* Default password Administr@tor

Alter the admin password and the disk size:

```
$ read -p 'Enter password: ' -s password
$ packer build -var "disk_size=61440" -var "password=$password" windows-2012-R2-standard-amd64.json
```

## Time on medium specced server

time to build with packer: ~25mins
time to upload to s3 on 1gbit: ~7mins
download template to QS and register: ~5mins
boot first instance and test: ~5mins

## Windows Packer Templates

* Virtio drivers are loaded on startup
* Configured as 2 CPU and 4 GB memory by default
* No updates or services packs applied
* Firewall is disabled
* RDP enabled
* Powershell is installed with Remote Execution policy is set to unrestricted

The OS can be evaluated for 180-days. http://technet.microsoft.com/en-US/evalcenter/dn205286.aspx

### Quick Start

```bash
$ packer build windows-2012-R2-standard-amd64.json
```

### Windows 2012 R2 Standard

* User Administrator
* Default password Administr@tor

Alter the admin password and the disk size:

```
$ read -p 'Enter password: ' -s password
$ packer build -var "disk_size=61440" -var "password=$password" windows-2012-R2-standard-amd64.json
```

# Ubuntu packer templates

## Create image

```bash
read -p 'Enter password: ' -s password
packer build -var 'user=ubuntu' -var "password=$password" ubuntu-14.04-server-amd64.json
```

## Software pre-installed

Look in scripts/packages.sh


# Ubuntu packer templates

## Create image

```bash
read -p 'Enter password: ' -s password
packer build -var 'user=ubuntu' -var "password=$password" ubuntu-14.04-server-amd64.json
```

## Software pre-installed

Look in scripts/packages.sh


This directory, and in particular it's makefile, can create a
virtual machine that runs on VMware Fusion (for the mac) with
Centos[1] in that VM.  It uses packer[2] to that.

Prior to running the makefile you'll need to have:
- installed packer
- installed VMware Fusion
- and downloaded the CentOS-6.5-x86_64-bin-DVD1.iso for Centos[3]

Put CentOS-6.5-x86_64-bin-DVD1.iso into iso/CentOS-6.5-x86_64-bin-DVD1.iso.

You may wish to tinker with
- pack.json+ -- which tells packer what to do.
- http_directory/anaconda-ks.cfg which tells CentOS's kickstarter[4] how to
  setup the machine.
- change the centos mirror used in both those

At that point just do
$ make
and cross your fingers.

[1] http://http://www.centos.org/
[2] http://packer.io/ 
[3] http://isoredirect.centos.org/centos/6/isos/x86_64/
[4] http://www.centos.org/docs/5/html/Installation_Guide-en-US/s1-kickstart2-howuse.html
## Windows Packer Templates

* Virtio drivers are loaded on startup
* Configured as 2 CPU and 4 GB memory by default
* No updates or services packs applied
* Firewall is disabled
* RDP enabled
* Powershell is installed with Remote Execution policy is set to unrestricted

The OS can be evaluated for 180-days. http://technet.microsoft.com/en-US/evalcenter/dn205286.aspx

## Packer Powershell Dependency

You need to install the Powershell provisioner for packer:

https://github.com/packer-community/packer-windows-plugins

### Quick Start

```bash
$ packer build windows-2012-R2-standard-amd64.json
```

### Windows 2012 R2 Standard

* User Administrator
* Default password Password123
* This template has the Cloud Instance Manager, but it does not work
  without a reboot (yet).

Alter the admin password and the disk size:

```
$ read -p 'Enter password: ' -s password
$ packer build -var "disk_size=61440" -var "password=$password" windows-2012-R2-standard-amd64.json
```

You also need to update the Autounattend.xml file with the new
password.

*NOTE*: Password strength requirements are pretty harsh
http://technet.microsoft.com/en-us/library/cc786468%28v=ws.10%29.aspx
# ISO Files

## Windows

Windows ISO files are available on [TechNet](http://technet.microsoft.com/en-us/evalcenter/dn407368.aspx)

### Windows iso's direct dl links
[Windows 2008 r2](http://care.dlservice.microsoft.com/dl/download/7/5/E/75EC4E54-5B02-42D6-8879-D8D3A25FBEF7/7601.17514.101119-1850_x64fre_server_eval_en-us-GRMSXEVAL_EN_DVD.iso), md5: 4263be2cf3c59177c45085c0a7bc6ca5

## Other