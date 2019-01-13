FROM deepcortex/scala-python3-ml:latest

RUN wget "http://supergsego.com/apache/hadoop/common/hadoop-2.6.5/hadoop-2.6.5.tar.gz" && \
    tar xvfz hadoop-2.6.5.tar.gz && \
    mv hadoop-2.6.5 /opt/ && \
    rm hadoop-2.6.5.tar.gz && \ 
    ln -s /opt/hadoop-2.6.5 /opt/hadoop 
    
RUN conda install --yes hdfs3 -c conda-forge

ENV LIBHDFS3_CONF /etc/hadoop/conf/hdfs-site.xml
ENV HADOOP_HOME /opt/hadoop
ENV PATH $PATH:$HADOOP_HOME/bin

COPY ignite_conf/* /etc/hadoop/conf/
COPY ignite_jars/* $HADOOP_HOME/share/hadoop/common/lib/

CMD [ "/bin/bash" ]

ARG BUILD_DATE
ARG VCS_REF
ARG IMAGE_VERSION

LABEL maintainer="nsemichev@gmail.com" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="DeepCortex" \
      org.label-schema.description="DeepCortex is the world’s first cloud based, automated platform for doing the entire end-to-end Data Science process" \
      org.label-schema.url="http://www.deepcortex.ai" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.version=$IMAGE_VERSION \
      org.label-schema.vcs-url="https://github.com/deepcortex/dockers" \
      org.label-schema.vendor="DeepCortex" \
      org.label-schema.schema-version="1.0" \
      org.label-schema.docker.cmd="docker run --rm -it -v ./input-files:/tmp deepcortex/python3-hdfs /bin/bash"
      
