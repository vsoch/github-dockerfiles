# dockerized-jenkins-accelerator
Accelerator for setting up a Dockerized Jenkins

## Prerequisites

* Create a set of passwordless RSA keys for use by jenkins master, and place them in a directory "keys" in the "master" directory. (id_rsa, id_rsa.pub)
* Create a set of passwordless RSA keys for use by jenkins deploy slaves, and place them in a directory "keys" in the "slaves/deploy_slave" directory. (id_rsa, id_rsa.pub)
* Create a certificate for use by nginx, and place it in a directory "certs" in the "nginx" directory. (server.crt, server.key)

### Building the master 

This requires the following arguments as shown in the compose file:

* jenkins_master_pass: "${JENKINS_MASTER_PASS:-123}"
* jenkins_slave_port: "${JENKINS_SLAVE_PORT:-50000}"
* jenkins_slave_pass: "${JENKINS_SLAVE_PASS:-123}"
* jenkins_config_repo_provider: "${JENKINS_CONFIG_REPO_PROVIDER:-git}"
* jenkins_config_repo_url: git@github.com:<user>/<repo>.git

If you are comfortable with the default values you only need to pass in the repo for configuration storage but proper passwords are recommended. Generally this setup is intended to be immutable upon startup so for instance you could generate strong unknown passwords for the master and slave on your build environment.

An alternative for this is in the works to move away from docker arguments, as they have security concerns.

### Building slaves

This requires the following arguments in addition to the ones for the master:

* cli_url: "${JENKINS_CLI_URL:-http://jenkins:8080}"
* jnlp_user: "${JENKINS_JNLP_USER:-jenkins-slave}"

cli_url is the location of your master(s) and the jnlp_user is the user to login with. The default user is configured in the default master.

An alternative for this is in the works to move away from docker arguments, as they have security concerns.

## Building

```
docker-compose build
```

## Running locally

```
docker-compose up -d
```

## Running on Docker swarm

```
docker stack deploy docker-stack.yml
```

## Scaling slaves

Increase scaling count or build slave according to needs, they will connect automatically. When they are shutdown, they are automatically removed from the master. So you can safely scale them based on hw needs.
