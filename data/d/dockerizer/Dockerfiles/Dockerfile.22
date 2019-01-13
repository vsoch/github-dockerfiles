FROM ubuntu:15.04
MAINTAINER Marco Matos docker@corp.mmatos.com

RUN apt-get update && apt-get install
RUN apt-get install -y wget locate --force-yes

RUN wget -nv --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" \
	 http://download.oracle.com/otn-pub/java/jdk/8u65-b17/jdk-8u65-linux-x64.tar.gz
RUN tar zxvfp jdk-8u65-linux-x64.tar.gz 

ENV JRE_HOME /jdk1.8.0_65/jre
ENV JAVA_HOME /jdk1.8.0_65/bin
ENV PATH /jdk1.8.0_65/bin/:$PATH

RUN mkdir -p /opt/sync/as/

ENV AS_FILE sync-as-0.1.2.tar.gz
ENV AS_FOLDER sync-as-0.1.2
ENV AS_URL http://www.syncobjects.com/sync-as-0.1.2.tar.gz
ENV AS_HOME /opt/sync/as/
#RUN wget -O $AS_FILE $AS_URL

ADD sync-as-0.1.2.tar.gz $AS_HOME

WORKDIR /opt/sync/as/

EXPOSE 8080
ENTRYPOINT ["/jdk1.8.0_65/bin/java", "-jar", "lib/as-startup.jar"]
#CMD ["lib/as-startup.jar"]