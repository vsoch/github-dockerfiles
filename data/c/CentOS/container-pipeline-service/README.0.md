# Continuous Integration

## Setup

- Install jenkins-job-builder: `sudo yum install python2-jenkins-job-builder -y`
- Configure `/etc/jenkins_jobs/jenkins_jobs.ini` Jenkins Job Builder as follows:
```
[jenkins]
user=<jenkins user>
password=<jenkins password>
url=<jenkins endpoint, e.g. https://ci.centos.org>
```

## Usage

```
jenkins-jobs update ci/job.yml
```

## CI jobs on ci.centos.org

- **[centos-container-pipeline-service-ci-master](https://ci.centos.org/view/Container/job/centos-container-pipeline-service-ci-master/)**: Runs on master branch of this repo at regular intervals.
- **[centos-container-pipeline-service-ci-pr](https://ci.centos.org/view/Container/job/centos-container-pipeline-service-ci-pr/)**: Runs on new pull requests created to this repo. It can also be triggered manually by commenting ``#dotests`` in the pull request by the project admins.
- **[centos-container-pipeline-service-ci-cleanup](https://ci.centos.org/view/Container/job/centos-container-pipeline-service-ci-cleanup/)**: Clean allocated resources on ci.centos.org on job success/failure
- **[centos-container-pipeline-service-container-index](https://ci.centos.org/view/Container/job/centos-container-pipeline-service-container-index/)**: Build centos container index from https://github.com/CentOS/container-index.git
## Tests

## Setup

Ensure that the container-pipeline-service project directory is in PYTHONPATH.

``export PYTHONPATH=/path/to/container-pipeline-service:$PYTHONPATH``

### Nomenclature

Add a test package or module for a feature with a name of the form
``test_(?P<index>\d\d)_(?P<feature>\w+)(?:.py)?``, for example,

- ``test_00_openshift`` is a test package
- ``test_10_scanner.py`` is a test module for scanner


where

- **index** is used to run tests in order
- **feature** is the name of a feature or project component


Any module/package name should start with the prefix ``test``.  You can
follow the same patten when adding test modules inside a test package.


### How to write tests

``` python
from ci.tests.base import BaseTestCase

# utitliy methods
from ci.lib import _print


class TestSomeFeature(BaseTestCase):

    # if you want to add something to test setup
    def setUp(self):
        super(TestSomeFeature, self).setUp()
        # your code goes here

    def test_00_first_test_case(self):
        # some code

        # utility method to run provisioning. If the system has been
        # provisioned already, it will just skip provisioning. However,
        # if you want to provision the system anyhow, pass
        # force=True as an keyword argument.
        self.provision()

        # utility method to run command on remote/local machines
        # if host arg is not provided, it defaults to running the command
        # on the local machine
        output = self.run_cmd('ls -la', user='root', host='192.168.10.20')

    def test_01_second_test_case(self):
        # some code

```

### Configuring hosts to test

By default, the hosts point to a multinode vagrant setup. You can customize it
by exporting a similar JSON to an env variable **CCCP_CI_HOSTS**:

``` json
{
  "jenkins_master": {
    "host": "192.168.100.100", 
    "remote_user": "vagrant", 
    "private_key": "~/.vagrant.d/insecure_private_key"
  }, 
  "controller": {
    "inventory_path": "provisions/hosts.vagrant", 
    "host": null, 
    "private_key": "~/.vagrant.d/insecure_private_key", 
    "user": "vagrant"
  }, 
  "openshift": {
    "host": "192.168.100.201", 
    "remote_user": "vagrant", 
    "private_key": "~/.vagrant.d/insecure_private_key"
  }, 
  "jenkins_slave": {
    "host": "192.168.100.200", 
    "remote_user": "vagrant", 
    "private_key": "~/.vagrant.d/insecure_private_key"
  }
}
```
Atomic Scanners
---------------

Atomic scanners to scan the container images and extracting metadata about containers.

There are following atomic scanners configured to run for pipeline service.

1. [Pipeline scanner](pipeline-scanner)

2. [RPM verify scanner](scanner-rpm-verify)
Atomic scanner: pipeline-scanner
--------------------------------

This is a container image scanner based on `atomic scan`. The goal of the
scanner is to scan CentOS based Docker images in the CentOS Community Container
Pipeline and generate relevant results.

Steps to use:

- Pull Docker image from **registry.centos.org**:

```
$ docker pull registry.centos.org/pipeline-images/pipeline-scanner
```

- Install it using `atomic`:

```
$ atomic install registry.centos.org/pipeline-images/pipeline-scanner
```

- Mount the image's rootfs because by default `atomic scan` would mount it in
  read-only mode but we need read-write capability:

```
$ atomic mount -o rw centos:centos7 /mnt
```

Make sure you have `centos:centos7` available locally before you try to mount

- Run the scanner on CentOS based images:

```
$ atomic scan --scanner pipeline-scanner --rootfs=/mnt centos:centos7
```
Atomic scanner: misc-package-updates
--------------------------------

This is a container image scanner based on `atomic scan`. The goal of the
scanner is to scan CentOS based container images in the CentOS Community Container
Pipeline and generate relevant results.

Steps to use:

- Pull container image from **registry.centos.org**:

```
$ docker pull registry.centos.org/pipeline-images/misc-package-updates
```

- Install it using `atomic`:

```
$ atomic install registry.centos.org/pipeline-images/misc-package-updates
```


- Run the scanner on CentOS based images:

```
$ IMAGE_NAME=registry.centos.org/centos/centos atomic scan --scanner misc-package-updates registry.centos.org/centos/centos
```

Scanner needs an environment variable `IMAGE_NAME` set on the host system to be
able to scan the image and report the results.
Atomic scanner: scanner-rpm-verify
--------------------------------

This is a container image scanner based on `atomic scan`. The goal of this
scanner is to scan container images by verifying and reporting the installed
RPM packages.

Steps to use:

- Pull Docker image from **registry.centos.org**:

```
$ docker pull registry.centos.org/pipeline-images/scanner-rpm-verify
```

- Install it using `atomic`:

```
$ atomic install registry.centos.org/pipeline-images/scanner-rpm-verify
```

- Mount the image's rootfs because by default `atomic scan` would mount it in
  read-only mode but we need read-write capability:

```
$ sudo atomic scan --scanner rpm-verify <image-to-scan>
```
Atomic scanner: container-capabilities-scanner
--------------------------------

###NOTE:

- This scanner requires you to:

    - mount Docker socket (`/var/run/docker.sock`) of host system to the atomic
      scan container.
    
    - share process namespace of host system with the atomic scan container

    - set label `RUN` in Dockerfile with appropriate `docker run` command

- This scanner hasn't been tested beyond simple `docker run` examples
  shared below

---


This is a container image scanner based on `atomic scan`. The goal of
the scanner is to scan CentOS based container images in the CentOS
Community Container Pipeline and generate relevant results.

This scanner scans container image for RUN label. A RUN label must
specify the `docker run` command for the image. The scanner checks for
various options like `--privileged`, `--security-opt`, `--net`,
etc. that provide a container with escalated privileges.

Steps to use:

- Pull container image from **registry.centos.org**:

    ```
    $ docker pull registry.centos.org/pipeline-images/container-capabilities-scanner
    ```

- Install it using `atomic`:

    ```
    $ atomic install registry.centos.org/pipeline-images/container-capabilities-scanner
    ```

- Consider below Dockerfile and resulting container image:


        $ cat Dockerfile
        FROM registry.centos.org/centos/centos

        LABEL RUN docker run -it --privileged --net=host --security-opt label=disable registry.centos.org/centos/centos bash

        $ docker build -t privileged-centos .

- Now run the scanner as below and check resulting output:
        
        $ IMAGE_NAME=privileged-centos atomic scan --scanner container-capabilities-scanner privileged-centos
        docker run -t --rm -v /etc/localtime:/etc/localtime -v /run/atomic/2017-04-06-05-55-32-547275:/scanin -v /var/lib/atomic/container-capabilities-scanner/2017-04-06-05-55-32-547275:/scanout:rw,Z -v /var/run/docker.sock:/var/run/docker.sock -e IMAGE_NAME=privileged-centos registry.centos.org/pipeline-images/container-capabilities-scanner python scanner.py
        
        Files associated with this scan are in /var/lib/atomic/container-capabilities-scanner/2017-04-06-05-55-32-547275.
        
        $ cat /var/lib/atomic/container-capabilities-scanner/2017-04-06-05-55-32-547275/1bbfb878505090d137863b1258709d9b28d7bd6a46bd5ebf627fbb6e0784ce4d/image_scan_results.json
        {
        "Scan Type": "check-capabilities",
        "CVE Feed Last Updated": "NA",
        "UUID": "1bbfb878505090d137863b1258709d9b28d7bd6a46bd5ebf627fbb6e0784ce4d",
        "Reference documentation": "http://www.projectatomic.io/blog/2016/01/how-to-run-a-more-secure-non-root-user-container/",
        "Scan Results": {
            "Container capabilities": "\nThis container uses privileged security switches:\n\n\u001b[1mINFO: --security-opt label=disable\u001b[0m \n      Disabling label separation turns off tools like SELinux and could allow processes from the container to break out onto your host system.\n\n\u001b[1mINFO: --net=host\u001b[0m \n      Processes in this container can listen to ports (and possibly rawip traffic) on the host's network.\n\n\u001b[1mINFO: --privileged\u001b[0m \n      This container runs without separation and should be considered the same as root on your system.\n\nFor more information on these switches and their security implications, consult the manpage for 'docker run'.\n\n"
        },
        "Successful": "true",
        "Finished Time": "2017-04-06-05-55-38-466022",
        "Start Time": "2017-04-06-05-55-38-160488",
        "Scanner": "Container Capabilities Scanner"
        }

Scanner needs an environment variable `IMAGE_NAME` set on the host
system to be able to scan the image and report the results.
# centos-cccp-ansible
Ansible scripts to setup CentOS Community Container Pipeline


## Useful playbook variables

- **cccp_index_repo**: Repository for container index, defaults to ``https://github.com/centos/container-index``. It can be pointed to a fork of or repo similar to the official CentOS container index repo.
- **oc_slave**: Hostname of Openshift Slave machine
- **jenkins_private_key_file**: Path to private key file for Jenkins master
- **jenkins_public_key_file**: Path to public key file for Jenkins slave
- **jenkins_admin_username**: Admin username for Jenkins
- **jenkins_admin_password**: Admin password for Jenkins
- **public_registry**: Endpoint for public container registry
- **nginx_conf_template**: Template name for nginx conf for container registry in ``nginx`` role
- **nginx_conf_file**: Filename for nginx conf for container registry in target node
- **ssl_cert_file**: SSL cert file path in nginx machine
- **ssl_key_file**: SSL key file path in nginx machine
- **copy_ssl_certs**: Copy insecure nginx SSL cert/key files for local setup, when true
- **beanstalk_server**: Hostname of beanstalk server machine
- **vagrant**: Set to ``true`` when provisioning using Vagrant

There are many more playbook variables defined. You can refer to the default
values in the ``defaults/main.yml`` file inside the respective role directories.
