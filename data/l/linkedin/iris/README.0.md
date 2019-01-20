Iris sample terraform config for AWS
====================================

Overview
--------

This sample terraform spins up a cluster consists of the following services:

* 1 NAT server
* 1 app server (iris, iris-sender, nginx) in public subnset
* 1 RDS cluster in private subnet
* 2 elastic IPs


Usage
-----

Set the following variables in `terraform.tfvars` file:

```
aws_access_key = "AAAAAAAAAAAAAAAAAAAA"
aws_secret_key = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
aws_key_name  = "aws-ssh"
aws_key_file = "/Users/foo/.ssh/aws-ssh.pem"
```

Verify intended state:

```bash
terraform plan
```

Deploy:

```bash
terraform apply
```

Find out public DNS via terraform output, look for key `iris_public_dns`:

```bash
terraform output
```

Iris can be accessed at `${iris_public_dns}:16649`.

Access to NAT server as bastion host:

```bash
# make sure your AWS ssh key is loaded through ssh-add
ssh -A -i YOUR_AWS_SSH_KEY ec2-user@NAT_SERVER
```

Access to Iris app node from NAT server:

```bash
ssh ubuntu@APP_SERVER_INTERNAL_IP
```
Build steps
-----------

Generate JSON for packer:

```bash
mkdir output
python gen_packer_cfg.py ./iris.yaml | tail -n +2 > ./output/iris.json
```

Build and publish AWS AMI:

```bash
packer build -only=amazon-ebs \
    -var "aws_ssh_keypair_name=YOUR_KEY_NAME_IN_AWS" \
    -var "aws_ssh_private_key_file=$HOME/.ssh/AWS_KEY.pem" \
    -var "aws_access_key=AAAAAAAAAAAAAAAAAAAA" \
    -var "aws_secret_key=BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB" \
    ./output/iris.json
```

Build Docker image:

```bash
packer build -only=docker ./output/iris.json
```


Usage
-----

### Docker

Spin up an Iris instance and connect to existing MySQL DB:

```bash
docker run -d -e DOCKER_DB_BOOTSTRAP=1 \
	-e IRIS_CFG_DB_USER=root -e IRIS_CFG_DB_PASSWORD=admin -e IRIS_CFG_DB_HOST=IP_ADDRESS \
	--name iris -p 16649:16649 \
	quay.io/iris/iris:latest
```


Inspect docker image with docker run:

```bash
docker run --rm=true -i -t quay.io/iris/iris:latest /bin/bash
```
Iris chart
==========

Usage
-----

```
helm dependency build
helm install --name FOO .
```
Iris-API (and iris-sender) under Docker
======================================

**NOTE: Not mainatined anymore, please build latest docker image from provided packer setup.
See: ../packer/README.md**

### Get started

Build container. This installs all dependencies as well as copies all iris source code.

    docker build -t iris .

Edit iris's config file as needed (MySQL and vendor settings and so on):

    vim docker/config/config.yaml

Run it, with bind mounts to give access to iris api config file

    docker run -p 16649:16649 -v `pwd`/docker/config:/home/iris/config -t iris

You can optionally bind mount log directories for uwsgi/nginx:

    mkdir -p docker/logs/{uwsgi,nginx}
    docker run -p 16649:16649 -v `pwd`/docker/config:/home/iris/config \
    -v `pwd`/docker/logs/nginx:/home/iris/var/log/nginx  \
    -v `pwd`/docker/logs/uwsgi:/home/iris/var/log/uwsgi  -t iris

You can then hit `http://localhost:16649 ` to access iris running within the docker.

### Quick commands

Check what containers are running:

    docker ps

Kill and remove a container:

    docker rm -f $ID

Execute a bash shell inside container while it's running:

    docker exec -i -t $ID /bin/bash
Iris documentation
==================

Dependencies
------------

```
pip install Sphinx sphinxcontrib-httpdomain sphinx_rtd_theme
```

Build
-----

```bash
make html
```
