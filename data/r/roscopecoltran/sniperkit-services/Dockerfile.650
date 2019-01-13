FROM armdocker.rnd.ericsson.se/proj_kds/er/java-jdk8:latest

ENV ES_HOME=/opt/elasticsearch 
ENV ES_VERSION=2.4.3
ENV PATH=${ES_HOME}/bin:$PATH
ENV ES_CONFIG_DIR=/opt/elasticsearch/config
ENV ES_JAVA_OPTS="-Xms1g -Xmx1g"
ENV CLUSTER_NAME=er-default
ENV MINIMUM_MASTER_NODES=1
ENV NODE.MASTER=true
ENV NODE.DATA=true
ENV PING_UNICAST_HOSTS="127.0.0.1, [::1]"

# https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/2.4.3/elasticsearch-2.4.3.tar.gz
RUN apk --update add bash wget openssl ca-certificates  \
  && wget -O /tmp/elasticsearch-${ES_VERSION}.tar.gz    \
    https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/${ES_VERSION}/elasticsearch-${ES_VERSION}.tar.gz \
  && mkdir -p /opt \
  && tar xzf /tmp/elasticsearch-${ES_VERSION}.tar.gz -C /opt/ \
  && ln -s ${ES_HOME}-${ES_VERSION} ${ES_HOME} \
  && rm -Rf /var/cache/apk/* /tmp/*    \
  && addgroup -g 1000 elasticsearch    \
  && adduser -u 1000 -G elasticsearch -D -h ${ES_HOME} -s /bin/bash elasticsearch  \
  && chown -R elasticsearch:elasticsearch ${ES_HOME}-${ES_VERSION}

RUN set -ex \
    && for path in \
        ${ES_HOME}/data         \
        ${ES_HOME}/logs         \
        ${ES_CONFIG_DIR}        \        
        ${ES_CONFIG_DIR}/shield \
    ; do \
        mkdir -p "$path";       \
        chown -R elasticsearch:elasticsearch "$path"; \ 
    done

# Install plugins
USER elasticsearch
RUN ${ES_HOME}/bin/plugin install license && \    
    ${ES_HOME}/bin/plugin install shield

# Add roles . Mainly for kibana4_server role.
COPY config/roles.yml   ${ES_CONFIG_DIR}/shield
COPY config/logging.yml ${ES_CONFIG_DIR}
COPY config/elasticsearch.yml ${ES_CONFIG_DIR}

# Copy in truststore and keystore (secured with a password)
COPY security/node-cert/truststore.jks ${ES_CONFIG_DIR}/shield
COPY security/node-cert/keystore.jks ${ES_CONFIG_DIR}/shield

# Create default user and kibana4 user
RUN ${ES_HOME}/bin/shield/esusers useradd admin -p atomic -r admin && \
    ${ES_HOME}/bin/shield/esusers useradd kibana4 -p kibana4 -r kibana4_server && \
    ${ES_HOME}/bin/shield/esusers useradd marvel -p marvel -r marvel_user 

COPY docker-entrypoint.sh ${ES_HOME}/

# Data
VOLUME [ ${ES_HOME}/data ]

USER root
RUN chown -R elasticsearch:elasticsearch ${ES_HOME} ${ES_CONFIG_DIR} ${ES_HOME}/data

USER elasticsearch
WORKDIR ${ES_HOME}

ENTRYPOINT ["./docker-entrypoint.sh"]

EXPOSE 9200 9300

CMD ["elasticsearch"]
