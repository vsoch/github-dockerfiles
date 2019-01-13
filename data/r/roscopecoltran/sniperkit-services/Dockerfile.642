FROM armdocker.rnd.ericsson.se/proj_kds/er/java-jdk8:latest

ENV ES_HOME=/opt/elasticsearch 
ENV ES_VERSION=5.1.1
ENV PATH=${ES_HOME}/bin:$PATH
ENV ES_CONFIG_DIR=/etc/elasticsearch
ENV ES_JAVA_OPTS="-Xms1g -Xmx1g"
ENV CLUSTER_NAME=ice-default
ENV MINIMUM_MASTER_NODES=1
ENV NODE.MASTER=true
ENV NODE.DATA=true
ENV PING_UNICAST_HOSTS="127.0.0.1, [::1]"


RUN apk --update add bash wget openssl ca-certificates \
  && wget -O /tmp/elasticsearch-${ES_VERSION}.tar.gz https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-${ES_VERSION}.tar.gz \
  && mkdir -p /opt \
  && tar xzf /tmp/elasticsearch-${ES_VERSION}.tar.gz -C /opt/ \
  && ln  -s ${ES_HOME}-${ES_VERSION} ${ES_HOME} \
  && rm -Rf /var/cache/apk/* /tmp/*    \
  && addgroup -g 1000 elasticsearch    \
  && adduser -u 1000 -G elasticsearch -D -h ${ES_HOME} -s /bin/bash elasticsearch  \
  && chown -R elasticsearch:elasticsearch ${ES_HOME}-${ES_VERSION}

RUN set -ex \
    && for path in \
        ${ES_HOME}/data         \
        ${ES_HOME}/logs         \
        ${ES_CONFIG_DIR}        \
        ${ES_CONFIG_DIR}/xpack  \
        ${ES_CONFIG_DIR}/script \
    ; do \
        mkdir -p "$path";       \
        chown -R elasticsearch:elasticsearch "$path"; \ 
    done

# Install xpack for security
USER elasticsearch
RUN yes | .${ES_HOME}/bin/elasticsearch-plugin install x-pack

COPY config/log4j2.properties ${ES_CONFIG_DIR}
COPY config/elasticsearch.yml ${ES_CONFIG_DIR}
COPY docker-entrypoint.sh     ${ES_HOME}/

# Copy in truststore and keystore (secured with a password)
COPY security/node-cert/truststore.jks ${ES_CONFIG_DIR}/xpack
COPY security/node-cert/keystore.jks ${ES_CONFIG_DIR}/xpack

USER root
RUN chown -R elasticsearch:elasticsearch ${ES_HOME} ${ES_CONFIG_DIR}

USER elasticsearch
WORKDIR ${ES_HOME}

ENTRYPOINT ["./docker-entrypoint.sh"]

VOLUME [ ${ES_HOME}/data ]

EXPOSE 9200 9300

CMD ["elasticsearch"]

#docker build -t er/elasticsearch:2.3 .
