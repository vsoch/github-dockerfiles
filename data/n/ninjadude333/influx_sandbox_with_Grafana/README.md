# influx_sandbox_with_Grafana
the official influxDB sandbox with Grafana added

# Pre-Requirements:
1. docker-ce or docker-ee installed and running on the machine.
2. docker-compose tool installed on the machine.
3. Kapacitor image will be generated with all the atomiQ prerequirements, so all of the files stated in the DockerFile at ./images/kapacitor/latest/ should be there.

*if using docekr-ee the use of arguments in the docker file will be disabled. (Dockerfile ARG before FROM known issue/bug)

# How to run ?
In order to run the InfluxdB Sandbox with grafana do the following:
1.	Clone to this repo: (using amdocs domain user and password)
2.  Rename directory to the convention of SANDBOX-{UserName}-{Starting Port Number} for example : SANDBOX-DavidG-3000
3.	Edit the .env file and put the wanted port mapping for the modules starting with the port number in the folder name.(for default ports don’t change anything.)
4.	Run ./sandbox up
5.	Have fun.

In order to run multiple sandboxes on the same machine: 
1.	Copy the cloned folder to a new folder.
2.  Rename directory to the convention of SANDBOX-{UserName}-{Starting Port Number} for example : SANDBOX-DavidG-3000
3.	Change the port mappings on the .env file to new ports that will not overlap previous sandboxes already running. starting with the port number in the folder name.
4.	Run ./sandbox up

# TICK Sandbox

This repo is a quick way to get the entire TICK Stack spun up and working together. It uses [Docker](https://www.docker.com/) to spin up the full TICK stack in a connected fashion. This is heavily tested on Mac and should mostly work on linux and Windows.

To get started you need a running docker installation. If you don't have one, you can download Docker for [Mac](https://www.docker.com/docker-mac) or [Windows](https://www.docker.com/docker-windows), or follow the installation instructions for Docker CE for your [Linux distribution](https://docs.docker.com/engine/installation/#server).

### Running 

To run the `sandbox`, simply use the convenient cli:

```bash
$ ./sandbox
sandbox commands:
  up           -> spin up the sandbox environment (add -nightly to grab the latest nightly builds of InfluxDB and Chronograf)
  down         -> tear down the sandbox environment
  restart      -> restart the sandbox
  influxdb     -> attach to the influx cli
  
  enter (influxdb||kapacitor||chronograf||telegraf||grafana) -> enter the specified container
  logs  (influxdb||kapacitor||chronograf||telegraf||grafana) -> stream logs for the specified container
  
  delete-data  -> delete all data created by the TICK Stack
  docker-clean -> stop and remove all running docker containers
  rebuild-docs -> rebuild the documentation container to see updates
```

To get started just run `./sandbox up`. You browser will open two tabs:

- `localhost:xxxx` - Chronograf's address. You will use this as a management UI for the full stack
- `localhost:xxxx` - Documentation server. This contains a simple markdown server for tutorials and documentation.

.env the container ports can be configured in the .env file,
also it is possible to run many instances of this on the same server as long as you run it from a different directory and make sure the ports are not overlapping.

