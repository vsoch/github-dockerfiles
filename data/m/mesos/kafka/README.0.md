# Intro
A docker image could be built with `build-image.sh` script.

The image will have following pre-installed components:
- openjdk-jdk;
- mesos native libs;

`/opt/kafka-mesos` folder will contain following content:
- kafka*.tgz - kafka distro;
- kafka-mesos*.jar - kafka-mesos distro;
- kafka-mesos.sh - shell script to run kafka-mesos;

No default configuration file for kafka-mesos is provided. All configuration params should be
specified via cli options.

# Building image
Building image is done by `build-image.sh` script. Please refer to help via `./build-image.sh -h`.

Example:
```
# ./build-image.sh
```
Note: this would not push the image. Push should be done manually after testing.

## Using docker-machine
If you have docker-machine installed, with virtualbox, you can run the following commands:
```
$ docker-machine create --driver virtualbox dev
$ eval "$(docker-machine env dev)"
$ ./build-image.sh
```

# Running image
Running image using docker. Required networking params should be provided. Image has no entry point,
so ./kafka-mesos.sh should be specified explicitly.

Example:
```
# sudo docker run -it -p 7000:7000 --add-host=master:192.168.3.5 `whoami`/kafka-mesos ./kafka-mesos.sh scheduler \
--master=master:5050 --zk=master:2181 --api=http://<accessible-ip>:7000 --storage=zk:/kafka-mesos
```
Where accessible-ip - is the IP address of running host, accessible from mesos nodes.

Note: if you want to inspect image content you can skip specifying `./kafka-mesos.sh` entry point.
In that case you will get shell access.

# Running image in Marathon
To run image in Marathon it is better to pre-pull image on all required nodes using:
```
# sudo docker pull <image-name>
```

After that, scheduler process could be created via Marathon API via POST /v2/apps call.
Example:
```
{
    "container": {
        "type": "DOCKER",
        "docker": {
            "network": "HOST",
            "image": "$imageName"
        }
    },
    "id":"kafka-mesos-scheduler",
    "cpus": 0.5,
    "mem": 256,
    "ports": [7000],
    "cmd": "./kafka-mesos.sh scheduler --master=master:5050 --zk=master:2181 --api=http://master:7000 --storage=zk:/kafka-mesos",
    "instances": 1,
    "constraints": [["hostname", "LIKE", "master"]]
}
```

Then the cli should be able to connect to url http://master:7000 from your api client machine
(typically different than the mesos slaves). Example:
```
# ./kafka-mesos.sh broker list --api=http://master:7000
no brokers
```
Now you can configure and start brokers.
# Vagrant VMs for Mesos cluster
Vagrantfile creates mesos cluster with following nodes:
- master;
- slave0..slave(N-1) (N is specified in vagrantfile);

Master provides web ui listening on http://master:5050
Both master and slave nodes runs mesos slave daemons.

Every node has pre-installed docker. Master node has pre-installed
marathon scheduler.

Host's public key is copied to `authorized_hosts`,
so direct access like `ssh vagrant@master|slaveX` should work.

For general mesos overview please refer to
http://mesos.apache.org/documentation/latest/mesos-architecture/

## Node Names
During first run vagrantfile creates `hosts` file which
contains host names for cluster nodes. It is recommended
to append its content to `/etc/hosts` (or other OS-specific
location) of the running (hosting) OS to be able to refer
master and slaves by logical names.

## Startup
Mesos master and slaves daemons are started automatically.

Each slave node runs 'mesos-slave' daemon while master runs both
'mesos-master' and 'mesos-slave' daemons.

Daemons could be controlled by using:
`/etc/init.d/mesos-{master|slave} {start|stop|status|restart}`

## Configuration
Configuration is read from the following locations:
- `/etc/mesos`, `/etc/mesos-{master|slave}`
  for general or master|slave specific CLI options;
- `/etc/default/mesos`, `/etc/default/mesos-{master|slave}`
  for general or master|slave specific environment vars;

Please refer to CLI of 'mesos-master|slave' daemons and `/usr/bin/mesos-init-wrapper`
for details.

## Logs
Logs are written to `/var/log/mesos/mesos-{master|slave}.*`