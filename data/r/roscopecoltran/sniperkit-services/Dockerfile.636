FROM armdocker.rnd.ericsson.se/proj_kds/er/java-jdk8:latest
MAINTAINER Nicolas Seyvet <nicolas.seyvet@ericsson.com>

# Set env variables
ENV KIBANA_VERSION 4.6.2
ENV LINUX_VERSION ${KIBANA_VERSION}-linux-x86_64
ENV KIBANA_HOME /opt/kibana
ENV SHIELD_VERSION 2.4.1
ENV MARVEL_VERSION 2.4.1
ENV ELASTICSEARCH_URL https://127.0.0.1:9200

RUN addgroup -g 1000 kibana \
  && adduser -u 1000 -G kibana -D -h ${KIBANA_HOME} -s /sbin/nologin kibana

# Install kibana4 and plugins
# https://download.elastic.co/kibana/kibana/kibana-4.6.2-linux-x86_64.tar.gz
RUN apk --update add bash wget nodejs openssl ca-certificates                       \
  && wget https://download.elastic.co/kibana/kibana/kibana-$LINUX_VERSION.tar.gz    \
      -O /tmp/kibana-$LINUX_VERSION.tar.gz                                          \
  && tar xzf /tmp/kibana-$LINUX_VERSION.tar.gz                                      \
    -C ${KIBANA_HOME} && rm /tmp/kibana-$LINUX_VERSION.tar.gz                       \
  && ln -s ${KIBANA_HOME}/kibana-$LINUX_VERSION ${KIBANA_HOME}/kibana4              \
  && sed -i''  -e 's#NODE=.*#NODE=/usr/bin/node#' ${KIBANA_HOME}/kibana4/bin/kibana \
  && chown -R kibana:kibana ${KIBANA_HOME}

USER kibana

# Add plugins
RUN ${KIBANA_HOME}/kibana4/bin/kibana plugin --install kibana/shield/${SHIELD_VERSION}            \
  && ${KIBANA_HOME}/kibana4/bin/kibana plugin --install elasticsearch/marvel/${MARVEL_VERSION}

COPY docker-entrypoint.sh ${KIBANA_HOME}/docker-entrypoint.sh

# Add config file
COPY config/kibana.yml ${KIBANA_HOME}/kibana4/config

# Copy in Self-Signed certificate
COPY security/ca.crt         ${KIBANA_HOME}/kibana4
COPY security/kibana.crt     ${KIBANA_HOME}/kibana4
COPY security/kibana_pk.pem  ${KIBANA_HOME}/kibana4

USER root
RUN chmod +x ${KIBANA_HOME}/docker-entrypoint.sh

USER kibana
WORKDIR ${KIBANA_HOME}
ENTRYPOINT ["./docker-entrypoint.sh"]

EXPOSE 5601 

CMD ["kibana"]
