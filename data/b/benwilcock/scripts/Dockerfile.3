FROM openjdk:7-jdk-alpine

# Maintainer
MAINTAINER Ben Wilcock
    

ENV GLASSFISH_PKG=glassfish-4.1.2.zip \
    GLASSFISH_URL=https://download.oracle.com/glassfish/4.1.2/release/glassfish-4.1.2.zip \
    GLASSFISH_HOME=/glassfish4 \
    MD5=9a37928ea6e54334101b8a89e03a8d7d \
    PATH=$PATH:/glassfish4/bin \
    JAVA_HOME=/usr/lib/jvm/java-openjdk \
    DERBY_PKG=db-derby-10.12.1.1-bin.zip \
    DERBY_URL=http://archive.apache.org/dist/db/derby/db-derby-10.12.1.1/db-derby-10.12.1.1-bin.zip


COPY docker-entrypoint.sh /entrypoint.sh
COPY glassfish-resources.xml /glassfish-resources.xml
COPY MavenEnterpriseApp-ear.ear /MavenEnterpriseApp-ear.ear
# COPY glassfish-4.1.2.zip /glassfish-4.1.2.zip
# COPY db-derby-10.12.1.1-bin.zip /db-derby-10.12.1.1-bin.zip

# Install packages, download and extract GlassFish
# Setup password file
# Enable DAS
RUN apk add --no-cache unzip curl && \
    curl -O $GLASSFISH_URL && \
    curl -O $DERBY_URL && \
    echo "$MD5 *$GLASSFISH_PKG" | md5sum -c - && \
    unzip -oq $GLASSFISH_PKG && \
    unzip -oq $DERBY_PKG && \
    rm -f $GLASSFISH_PKG && \
    rm -f $DERBY_PKG && \
    rm -R $GLASSFISH_HOME/javadb && \
    mv db-derby-10.12.1.1-bin $GLASSFISH_HOME/javadb

ENTRYPOINT ["/entrypoint.sh"]

# Ports being exposed
EXPOSE 4848 8080 8181

# Start asadmin console and the domain
CMD ["asadmin", "start-domain", "-v"]
