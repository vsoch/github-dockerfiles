Description
===========

Installs FI-ware Cloud Portal.

Requirements
============

Ubuntu 14.04
Chef must be installed.

Attributes
==========

node[cloud_portal]['app_dir'] contains the path to install

Usage
=====

With chef-solo:

    sudo chef-solo -c solo.rb -j node.json

You can find a solo.rb and node.json samples at the root of the recipe.

For the system to work the internal config.js must be properly filled.# How to use this Dockerfile

To run a Cloud Portal Docker container you have two options: 

- You can build your own image using the Dockerfile we provide and then run the container from it or
- you can run the container directly from the image we provide in Docker Hub.

Both options require that you have [docker](https://docs.docker.com/installation/) installed on your machine.

## Build your own image and run the container from it

You have to download the [Cloud Portal's code](https://github.com/ging/fiware-cloud-portal) from GitHub and navigate to `extras/docker` directory. There, to compile your own image just run:

	sudo docker build -t cloud-portal-image .


> **Note**
> If you do not want to have to use `sudo` in this or in the next section follow [these instructions](https://docs.docker.com/installation/ubuntulinux/#create-a-docker-group).

This builds a new Docker image following the steps in `Dockerfile` and saves it in your local Docker repository with the name `cloud-portal-image`. You can check the available images in your local repository using: 

	sudo docker images


> **Note**
> If you want to know more about images and the building process you can find it in [Docker's documentation](https://docs.docker.com/userguide/dockerimages/).

Now you can run a new container from the image you have just created with:

	sudo docker run -d --name cloud-portal-container -v [host_config_file]:/opt/fiware-cloud-portal/config.js -p [host_port]:[container_port] cloud-portal-image


Where the different params mean: 

* -d indicates that the container runs as a daemon
* --name is the name of the new container (you can use the name you want)
* -v stablishes a relation between a local folder (in your host computer) and a container's folder. In this case it is used to pass to the container the configuration file that Cloud Portal needs to work. `host_config_file` has to be the location of a local file with that configuration following the [config template](https://github.com/ging/fiware-cloud-portal/blob/master/config.js.template).
* -p stablishes a relation between a local port and a container's port. You can use the port you want in `host_port` but `container_port` has to be the same that you have set in `config.app_port` in your config file. If you have set `config.https` to `true` you have to use here the https port.
* the last param is the name of the image

Here is an example of this command:

	sudo docker run -d --name cloud-portal -v /home/root/workspace/fiware-cloud-portal/config.js:/opt/fiware-cloud-portal/config.js -p 80:80 cloud-portal-image


Once the container is running you can view the console logs using: 

	sudo docker logs -f cloud-portal


To stop the container:

	sudo docker stop cloud-portal



## Run the container from the last release in Docker Hub

You can also run the container from the [image we provide](https://hub.docker.com/r/ging/cloud-portal/) in Docker Hub. In this case you have only to execute the run command. But now the image name is ging/cloud-portal:*version* where `version` is the release you want to use:

	sudo docker run -d --name cloud-portal-container -v [host_config_file]:/opt/fiware-cloud-portal/config.js -p [host_port]:[container_port] ging/cloud-portal

> **Note**
> If you do not specify a version you are pulling from `latest` by default.