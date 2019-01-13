FROM armdocker.rnd.ericsson.se/proj_kds/er/java-jdk8:latest
MAINTAINER Nicolas Seyvet <nicolas.seyvet@ericsson.com>

# Set env variables
ENV KIBANA_VERSION 5.1.1
ENV LINUX_VERSION ${KIBANA_VERSION}-linux-x86_64
ENV KIBANA_HOME /opt/kibana
ENV ELASTICSEARCH_URL https://127.0.0.1:9200

RUN addgroup -g 1000 kibana \
  && adduser -u 1000 -G kibana -D -h ${KIBANA_HOME} -s /sbin/nologin kibana

# Install kibana5 and plugins
# https://artifacts.elastic.co/downloads/kibana/kibana-5.0.0-linux-x86_64.tar.gz
RUN apk --update add bash wget nodejs openssl ca-certificates \
  && wget https://artifacts.elastic.co/downloads/kibana/kibana-$LINUX_VERSION.tar.gz \
      -O /tmp/kibana-$LINUX_VERSION.tar.gz                    \
  && tar xzf /tmp/kibana-$LINUX_VERSION.tar.gz                \
    -C ${KIBANA_HOME} && rm /tmp/kibana-$LINUX_VERSION.tar.gz \
  && ln -s ${KIBANA_HOME}/kibana-$LINUX_VERSION ${KIBANA_HOME}/kibana5 \
  && sed -i''  -e 's#NODE=.*#NODE=/usr/bin/node#' ${KIBANA_HOME}/kibana5/bin/kibana \
  && sed -i''  -e 's#NODE=.*#NODE=/usr/bin/node#' ${KIBANA_HOME}/kibana5/bin/kibana-plugin \
  && chown -R kibana:kibana ${KIBANA_HOME}

USER kibana
COPY docker-entrypoint.sh ${KIBANA_HOME}

COPY config/kibana.yml ${KIBANA_HOME}/kibana5/config
COPY config/kibana.yml ${KIBANA_HOME}/kibana5/config/kibana.yml.orig

# Copy in Self-Signed certificate
COPY security/ca.crt         ${KIBANA_HOME}/kibana5
COPY security/kibana.crt     ${KIBANA_HOME}/kibana5
COPY security/kibana_pk.pem  ${KIBANA_HOME}/kibana5

USER root
RUN ${KIBANA_HOME}/kibana5/bin/kibana-plugin install x-pack \
  && chown -R kibana:kibana /opt/kibana

USER kibana
WORKDIR ${KIBANA_HOME}
ENTRYPOINT ["./docker-entrypoint.sh"]

EXPOSE 5601
EXPOSE 9200

CMD ["kibana"]

