FROM tomcat:8-jre8

MAINTAINER "Javier Ortiz <jortiz@conwet.com>"

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/

# 
ENV DOWNLOAD_WAR_FILE FiwareRepository-4.4.3-RELEASE.war
ENV FINAL_WAR_FILE FiwareRepository.war
ENV REPO_CONF Repository-RI.properties

WORKDIR /Repository-RI

# Get the WAR, configure the Database and create the new WAR
RUN wget https://repo.conwet.fi.upm.es/artifactory/libs-release-local/org/fiware/apps/repository/FiwareRepository/4.4.3-RELEASE/${DOWNLOAD_WAR_FILE}
RUN mv $DOWNLOAD_WAR_FILE $FINAL_WAR_FILE
ADD ./$REPO_CONF /etc/default/$REPO_CONF

# Upload the application to Tomcat so it will run
RUN cp $FINAL_WAR_FILE /usr/local/tomcat/webapps