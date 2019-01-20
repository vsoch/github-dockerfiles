FROM openjdk:8u131-jre

# Setup env
USER root
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

ENV HADOOP_USER hdfs
ENV HADOOP_VERSION 2.7.3
ENV HADOOP_PREFIX /usr/local/hadoop
ENV HADOOP_COMMON_HOME /usr/local/hadoop
ENV HADOOP_HDFS_HOME /usr/local/hadoop
ENV HADOOP_CONF_DIR /usr/local/hadoop/etc/hadoop

# Install gettext-base for envsubst, required by bootstrap.sh
RUN apt-get update \
    && apt-get install -y gettext-base \
    && rm -rf /var/lib/apt/lists/*

# Install hadoop
RUN wget -q -O - http://zenpip.zenoss.eng/packages/hadoop-${HADOOP_VERSION}.tar.gz | tar -xzf - -C /usr/local \
 && ln -s /usr/local/hadoop-${HADOOP_VERSION} /usr/local/hadoop \
 && rm -rf /usr/local/hadoop/share/doc \
 && mkdir -p /data/hdfs/nn /data/hdfs/dn /data/hdfs/journal \
 && groupadd -r hadoop \
 && groupadd -r $HADOOP_USER \
 && useradd -r -g $HADOOP_USER -G hadoop $HADOOP_USER 

# Copy the Site files templates
ADD dev/ $HADOOP_CONF_DIR/dev
ADD prod/ $HADOOP_CONF_DIR/prod

# Setup permissions and ownership (httpfs tomcat conf for 600 permissions)
RUN chown -R $HADOOP_USER:hadoop /data/hdfs /usr/local/hadoop-${HADOOP_VERSION} \
 && chmod -R 775 $HADOOP_CONF_DIR

# Copy the bootstrap scripts
COPY scripts/* /usr/local/bin/

USER $HADOOP_USER
WORKDIR /usr/local/hadoop
ENTRYPOINT ["/usr/local/bin/bootstrap.sh"]
CMD ["bash"]

# Format the HDFS filesystem
RUN /usr/local/bin/init_hdfs.sh
