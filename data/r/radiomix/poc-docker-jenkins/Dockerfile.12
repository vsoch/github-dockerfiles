#
#		Scala/Java/WebApp
# Date:		2014.02.21
# Pupose:	Build a debian based container and copy the Scala WebApp WAR-file into tomcat7 web app dir.
# Author:	Michael Klöckner
# Version:	0.4
# 
# Server:	http://localhost:8080/lift_blank


# use our base image ubuntu/scala
FROM ubuntu/scala

# who we are
MAINTAINER Michael Klöckner <mkl AT im7 DOT de>

# clean up previous compiles
RUN cd /opt/lift_26_sbt-master/scala_210/lift_blank/ && ./sbt clean
# compile
RUN cd /opt/lift_26_sbt-master/scala_210/lift_blank/ && ./sbt compile
# compile and package the scala/lift web app into a war file
RUN cd /opt/lift_26_sbt-master/scala_210/lift_blank/ && ./sbt package 

# delete the old web app jar file
RUN rm -rf   /var/lib/tomcat7/webapps/test*
# copy the resulting war file into tomcats web app dir as file 'test.war'
RUN  cd /opt/lift_26_sbt-master/scala_210/lift_blank/ &&  cp target/scala-2.10/lift-2.6-starter-template_2.10-0.0.3.war  /var/lib/tomcat7/webapps/test.war

# restart service tomcat7, not realy necessary, but nice and clean
RUN service  tomcat7 restart
