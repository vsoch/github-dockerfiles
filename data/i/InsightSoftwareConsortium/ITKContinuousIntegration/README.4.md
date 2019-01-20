General
=======

This project configures and starts a Jenkins instance for ITK. It uses the upstream Jenkins docker image to create
its own docker image (installing the plugins listed in the configuration file). The SSL connection is handled through
a nginx instance (reverse proxy). Nginx runs the nginx upstream docker image. Both containers are linked with the
docker run option `--link` (See `run.sh`).

Starting the server should normally done running `run.sh`. A folder named `itkjenkins` will be created and contain all
the Jenkins configuration files. This folder is automatically mounted in the Jenkins docker container. The private key
and private SSL certificates are mounted in the nginx container. The paths to these are given with environment variable
(see below `Starting an ITK Jenkins instance`).

Starting an ITK Jenkins instance
================================

* Create `SSL_CERT` environment variable to point to the location of the
  SSL certificate (`export SSL_CERT {my_location}`). This should be a
  location like
  etc/letsencrypt/archive/itkjenkins.eastus.cloudapp.azure.com/fullchain1.pem
* Create `SSL_KEY` environment variable to point to the location of the
  SSL private key (`export SSL_KEY ${my_location}).
  etc/letsencrypt/archive/itkjenkins.eastus.cloudapp.azure.com/privkey1.pem
* Create `LETSENCRYPT_EMAIL` environment variable that contains the email address
  that is contacted when the SSL certificate is about to expire.
* Set weekly cron job to renew SSL certificate (NOTE: it will actually only be
  renewed when it is about to expire). The cron job should run
  `renewSSLcertificate.script`
* run `build.sh` to create the Jenkins image
* run `run.sh` to start the nginx and Jenkins servers
* Get admin temporary password
  - Read the output of `run.sh`. The initial admin password is printed
  in the output
  - or run `docker exec itkjenkins more /var/jenkins_home/secrets/initialAdminPassword`
    (or `getSecret.sh` script)
* Open browser and connect to server. It should appear as a secure connection (SSL).
* Enter admin password (=secret). If needed, admin user name is `admin`.
* Click on "x" next to "Getting Started" to skip installation of plugins. The ones we need are already installed in the
docker image
* Click on "Start using Jenkins"
* Click on 	Manage Jenkins"->"Configure Global Security"
* Select "Github Authentication Plugin"
* Make sure that Github Authentification is configured on https://github.com/organizations/InsightSoftwareConsortium/settings/applications
  Follow the instructions available here: https://wiki.jenkins.io/display/JENKINS/GitHub+OAuth+Plugin . Potentially disregard warning message
  about URL being incorrect
* Under "Global GitHub OAuth Settings", enter
 - "Client ID"
 - "Client Secret"
* Save!
* Log out!
* Log back in
* Click on 	Manage Jenkins"->"Configure Global Security"
* Select "Role-Based Strategy"
* Save!
* In "Manage Jenkins"->"Manage and Assign Roles"
  - Manage Roles
  - Assign Roles:
    - group "authenticated" is for all authenticated users
    - Use Github user names to add users to role
* Configure hyper: https://github.com/jenkinsci/hyper-slaves-plugin
* Expose port TCP 50000 (or the fixed value at Jenkins Configure Global Security) for JNLP connections
* Configure GitHub Pull Request builder: https://wiki.jenkins.io/display/JENKINS/GitHub+pull+request+builder+plugin
* Configure Azure VM Agents: https://plugins.jenkins.io/azure-vm-agents ,
  https://docs.microsoft.com/en-us/azure/jenkins/jenkins-azure-vm-agents

Backup Jenkins data folder
==========================

* Run `createBackup.sh ${output_directory}`
* Save archive on a safe hard drive
* Expected tar file size above 300MB

Recover Jenkins data folder
===========================

* Install Jenkins by running `run.sh`
* Stop jenkins during recovery process with `docker stop itkjenkins`
* Update Jenkins to a version at least as recent as the backup
* Restart Jenkins with `docker start itkjenkins`
* Stop Jenkins with `docker stop itkjenkins`
* Run `recoverBackup.sh ${my_backup_file}`
* The script will verify that the current version of Jenkins is more recent
than the version that was backed up. The version is read in `~/itkjenkins/war/META-INF/MANIFEST.MF`.
* Start jenkins with `docker start itkjenkins`

Update Jenkins
==============

* Run `updateJenkins.sh latest` or `updateJenkins ${url}`
* Jenkins war files URL can be found [here](http://updates.jenkins-ci.org/download/war/)

Start and stop Jenkins
======================

* From the website UI, `https://my_url/restart` and press `YES`
* Start container with `docker start itkjenkins`
* Stop container with `docker stop itkjenkins`

Backup Jenkins docker image
===========================

WARNING: This process can be really slow if run on a slow machine (Up to 30 minutes)
* Run `saveDockerContainer.sh ${output_directory}`
* Save image on a safe hard drive
* Expect a tar file size above 500MB

Restore Jenkins docker image
============================

* Run `loadDockerArchivedImage.sh ${my_backup_image}`
* Restart Jenkins with `docker start itkjenkins`

Additional information
======================

How to find plugin name for installation from list of plugins installed on Jenkins instance:
-Click on plugin in current ITKJenkins
-Click on 'on the plugin site'
-Click on 'GitHub →'
-Copy repo name and remove '-plugin'

Current ITK Jenkins server:
https://jenkinsitk.kitware.com/

Configuration files
===================

* Non-exhaustive list of configuration files in /tmp/itkjenkins
 - users/${USERNAME}/config.xml
 - config.xml
* Custom files
 - org.jenkinsci.plugins.configfiles.GlobalConfigFiles.xml

SSL Configuration file
======================
* A file named ~/.load_keys.sh should be created and should export the following environement variables:
** SSL_CERT=/path/to/fullchain.pem
** SSL_KEY=/path/to/privkey.pem
** LETSENCRYPT_EMAIL=my@email.com
** DNSNAME=my_dns.com

Troubleshoot
============

"This site can’t be reached":
Jenkins webpage is not loading: "This site can’t be reached"
Try ssh’ing into the azure server and run:
docker exec -it itkjenkins /bin/bash
If it returns:
containerd: container not found
even after trying docker stop itkjenkins and docker start itkjenkins, there is a problem.
Restart docker deamon:
sudo service docker restart
Hopefully it works now.

"502: Bad Gateway":
Jenkins webpage is not loading properly: "502: Bad Gateway"
Try ssh’ing into the azure server and check that both docker containers are running.
docker ps
If not, try to restart the one that is not running:
docker start itkjenkins

Wait a few seconds and try to load the webpage again.

