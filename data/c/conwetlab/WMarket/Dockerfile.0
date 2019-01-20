FROM tomcat:8-jre8

MAINTAINER "Aitor Magán <amagan@conwet.com>"

# Environment
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
# File is asumed to be called WMarket.war
ENV WMARKET_FILE WMarket.war

# Working directory
WORKDIR /wmarket

# Needed packages
RUN apt-get update && apt-get install -y zip

# Get the last WAR file
RUN wget `curl https://api.github.com/repos/conwetlab/WMarket/releases/latest 2>/dev/null | grep browser_download_url | sed 's/.*"browser_download_url": "\(.*\)".*/\1/'`

# Unzip the file
RUN unzip $WMARKET_FILE -d WMarket
RUN rm $WMARKET_FILE

# Configure the instance
RUN sed -i "s|^jdbc.url=.*$|jdbc.url=jdbc:mysql://wmarket_db:3306/marketplace|" WMarket/WEB-INF/classes/properties/database.properties
RUN sed -i "s|^jdbc.password=.*$|jdbc.password=my-secret-pw|" WMarket/WEB-INF/classes/properties/database.properties
RUN sed -i "s|^media.folder.*$|media.folder=/WMarket/static|" WMarket/WEB-INF/classes/properties/marketplace.properties
RUN sed -i "s|^lucene.IndexPath.*$|lucene.IndexPath=/WMarket/index|" WMarket/WEB-INF/classes/properties/marketplace.properties

# Recreate the ZIP with the new 
RUN cd WMarket && zip -r ../$WMARKET_FILE *

# Upload the application to Tomcat so it will run
RUN cp $WMARKET_FILE /usr/local/tomcat/webapps
