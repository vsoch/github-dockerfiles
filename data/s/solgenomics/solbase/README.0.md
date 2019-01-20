# SGN Development Vagrant

## Intro

This git repository serves TWO purposes:

#### Purpose 1) Do you need a virtual machine for immediate use?<br/>
#### Purpose 2) Do you want to generate a brand new virtual machine?<br/>
<br/>

For Logging In:
```
username: vagrant
password: vagrant
```
<br/>

## Purpose 1 Tutorial

Make sure you have VirtualBox AND the VirtualBox Extension Pack installed
https://www.virtualbox.org/wiki/Downloads

Step 1: Download the VirtualBox virtual machine from here: <br/>
* For 10GB Machine: ftp://solgenomics.net/virtualbox/SGNDev10.ova 
* For 120GB Machine: ftp://solgenomics.net/virtualbox/SGNDev120.ova 

Step 2: Open VirtualBox and click File->Import Appliance. Select the downloaded OVA file.<br/>
Step 3: Start the virtual machine.<br/>

## Purpose 2 Tutorial

Install Vagrant from https://www.vagrantup.com/downloads.html 

Make sure you have VirtualBox AND the VirtualBox Extension Pack installed
https://www.virtualbox.org/wiki/Downloads

Step 1: Clone this repo on your computer.<br/>
Step 2:<br/>

Tell vagrant to configure the VM
```
vagrant up
```
This may take around an hour or two

Step 3: Open VirtualBox. The newly generated virtual machine will show up.<br/>
Step 4: Start the virtual machine.<br/>
Step 5: Follow the welcome.txt instructions to fully customize the virtual machine to your needs.<br/>

To remove any trace of the VM
```
vagrant destroy
```
# Docker

* work in progress

## Docker Cloud Repository

Built docker containers for solbase are available here https://hub.docker.com/r/muellerlab/

## Running a Single Container

Container version numbers can be found in the docker repository above.

```
docker run -p 3000:3000 muellerlab/solbase:1.05
```

Now you should see solbase running on your browser on localhost; however,
our docker deployment is a distribution of three containers: solbase, postgres, and nginx.
To bundle these three together, you can run a stack described below.

## Running a Stack of Containers

Clone this repository on your machine and go to docker directory, then execute:

```
docker swarm init
docker stack deploy -c docker-compose.yml solbase
```

Now you should see solbase running on your browser on localhost.