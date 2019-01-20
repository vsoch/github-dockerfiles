FROM tomcat:7-jre7
MAINTAINER "Francisco de la Vega <fdelavega@fi.upm.es>"

ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64/

RUN apt-get update && apt-get install -y git maven openjdk-7-jdk mysql-client 

RUN git clone https://github.com/conwetlab/fiware-rss.git

# Use the git folder as default folder
WORKDIR fiware-rss

ADD ./database.properties /etc/default/rss/
ADD ./oauth.properties /etc/default/rss/

# Compile sources
RUN mvn install -DskipTests=true

# Deploy war files
RUN  cp ./fiware-rss/target/fiware-rss.war /usr/local/tomcat/webapps 
RUN  cp ./rss-expendLimit/el-server/target/expenditureLimit.war /usr/local/tomcat/webapps

ADD ./entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]
CMD ["catalina.sh", "run"]
