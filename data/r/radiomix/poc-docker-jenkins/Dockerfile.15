#
#		Scala/Java/WebApp
# Date:		2014.02.21
# Pupose:	Build a debian based container whith openjdk7, tomcat7, scala web app installed
# Author:	Michael Klöckner
# Version:	0.3
#


# use our base image ubuntu/tomcat7
FROM ubuntu/tomcat7

# who we are
MAINTAINER Michael Klöckner <mkl AT im7 DOT de>

# install scala/lift web app
RUN wget -O /tmp/master.zip https://github.com/Lift/Lift_26_sbt/archive/master.zip
RUN unzip -d /opt/ /tmp/master.zip
RUN rm -f /tmp/maset.zip

# compile the scala/lift web app into a war file once, to download necessery scala/java files
RUN cd /opt/lift_26_sbt-master/scala_210/lift_blank/ && ./sbt compile && ./sbt package 

