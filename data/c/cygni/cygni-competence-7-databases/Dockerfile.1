FROM openjdk:8u111-jdk
MAINTAINER Pär Tjärnberg <par.tjarnberg@cygni.se>

ENV HBASE_VERSION                       1.2.5
ENV HBASE_HOME                          /usr/local/hbase
ENV HBASE_CONF_DIR		                /usr/local/hbase/conf
ENV HBASE_MANAGES_ZK                    false
ENV HBASE_LOG_DIR                       /data/logs
ENV HBASE_TMP_DIR                       /hbase
ENV MAVEN_OPTS                          -Xmx512m
ENV PATH                                $PATH:/usr/local/hbase/bin

# Download, unpack HBase and update PATH variable
RUN wget -qO- http://apache.mirrors.spacedump.net/hbase/stable/hbase-$HBASE_VERSION-bin.tar.gz | tar xvz -C /usr/local
RUN ln -sv /usr/local/hbase-$HBASE_VERSION /usr/local/hbase

# Create dirs
RUN mkdir -p \
        ${HBASE_TMP_DIR} \
        ${HBASE_LOG_DIR} \
    && chmod -R 755 \
        ${HBASE_TMP_DIR} \
        ${HBASE_LOG_DIR} \
    && rm -rf ${HBASE_HOME}/docs \
    && sed -i.bk -e 's/PermSize/MetaspaceSize/g' ${HBASE_CONF_DIR}/hbase-env.sh

# Add configuration
ADD ./config/hbase-site.xml /usr/local/hbase/conf/
ADD ./config/core-site.xml /usr/local/hbase/conf/
ADD ./code /usr/local/code
RUN chmod +x /usr/local/code/*
ADD ./script/hbase-server.sh /usr/local/hbase/
RUN chmod +x /usr/local/hbase/hbase-server.sh

# Thrift
EXPOSE 9090 9095

# HBase Master port
# The port the HBase Master should bind to.
EXPOSE 16000

# HBase Master info port
# The port for the HBase Master web UI. Set to -1 if you do not want a UI instance run.
EXPOSE 16010

# HBase Regionserver port
# The port the HBase RegionServer binds to.
EXPOSE 16020

CMD "/usr/local/hbase/hbase-server.sh"
