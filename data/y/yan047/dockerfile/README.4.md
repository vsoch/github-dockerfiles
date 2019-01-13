# Ubuntu 14.04, jdk7, grails2.4.3, git, jenkins 1.596

This image is based on the official jenkins image building script, on top of yan047/grails2.4.3.
To start jenkins server, using the command: 
sudo docker run -d --name grails.jenkins -p 8000:8080 -v /usr/local/jenkins:/var/jenkins_home yan047/jenkins.grails

# Ubuntu 14.04, jdk6, grails 2.2.0
 
This image is based on phusion/baseimage:0.9.15.

