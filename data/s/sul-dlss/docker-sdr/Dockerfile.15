FROM tomcat:8

ENV FCREPO_DOWNLOAD_URL https://github.com/fcrepo3/fcrepo/releases/download/v3.8.1/fcrepo-installer-3.8.1.jar

WORKDIR $CATALINA_HOME

ENV FEDORA_HOME /usr/local/fedora
ENV FEDORA_WEBAPP_HOME /usr/local/tomcat/webapps/fedora
## install fedora
RUN  curl -sL  "$FCREPO_DOWNLOAD_URL" -o fedora-install.jar

MAINTAINER Chris Beer <cabeer@stanford.edu>

ADD fedora-install.properties /tmp/fedora-install.properties
RUN  java -jar fedora-install.jar /tmp/fedora-install.properties
ENV JAVA_OPTS "-Xmx1G"
RUN unzip $CATALINA_HOME/webapps/fedora.war -d $CATALINA_HOME/webapps/fedora && \
    rm $CATALINA_HOME/webapps/fedora.war
