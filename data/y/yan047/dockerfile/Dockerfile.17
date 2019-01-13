# Version: 1
# Name: tomcat8.run
FROM yan047/tomcat8

MAINTAINER "boyan.au@gmail.com"

ENV DEBIAN_FRONTEND noninteractive

# In case someone loses the Dockerfile
RUN rm -rf /etc/Dockerfile
ADD Dockerfile /etc/Dockerfile

RUN mkdir -p /etc/my_init.d
ADD lnwebapps.sh /etc/my_init.d/lnwebapps.sh

RUN chmod 777 /etc/my_init.d/lnwebapps.sh

RUN mkdir /etc/service/tomcatd
ADD tomcatstart.sh /etc/service/tomcatd/run


EXPOSE 8080
