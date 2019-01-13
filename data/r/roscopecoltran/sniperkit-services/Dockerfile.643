FROM armdocker.rnd.ericsson.se/proj_kds/er/java-jdk8  
MAINTAINER Nicolas Seyvet <nicolas.seyvet@ericsson.com>

ENV LS_VERSION 2.4.1
ENV LS_GROUP logstash
ENV LS_USER logstash
ENV LS_HOME /opt/logstash
ENV LS_OPTS ""

#https://artifacts.elastic.co/downloads/logstash/logstash-5.0.0.tar.gz
# https://download.elastic.co/logstash/logstash/logstash-2.4.0.tar.gz
RUN apk --update add bash wget openssl ca-certificates                \
  && wget --no-check-certificate -O /tmp/logstash-${LS_VERSION}.tar.gz https://download.elastic.co/logstash/logstash/logstash-${LS_VERSION}.tar.gz \
  && mkdir -p /opt                                                    \
  && tar xzf /tmp/logstash-${LS_VERSION}.tar.gz -C /opt/              \
  && ln -s /opt/logstash-${LS_VERSION} /opt/logstash                  \
  && rm -Rf /var/cache/apk/* /tmp/*                                   \
  && addgroup ${LS_GROUP}                                             \
  && adduser -h ${LS_HOME} -D -s /bin/bash -G ${LS_GROUP} ${LS_USER}  \
  && mkdir -p ${LS_HOME}/log                                          \
  && mkdir -p ${LS_HOME}/security                                  

RUN ${LS_HOME}/bin/logstash-plugin install logstash-output-opentsdb
RUN ${LS_HOME}/bin/logstash-plugin install logstash-output-webhdfs

ADD security/cacert.pem ${LS_HOME}/security/cacert.pem
ENV SSL_CERT_FILE ${LS_HOME}/security/cacert.pem

# Listen for defaults: 5000/tcp:udp (syslog), 5002/tcp (logstash-forwarder), 5004/tcp (journald), 5006/udp (Logspout), 5200/tcp (log4j)
EXPOSE 5000 5002 5004 5006 5200

COPY docker-entrypoint.sh ${LS_HOME}/

RUN chmod +x ${LS_HOME}/docker-entrypoint.sh \
  && chown -R ${LS_USER}:${LS_GROUP} ${LS_HOME}/

USER ${LS_USER}
WORKDIR ${LS_HOME}
ENTRYPOINT ["./docker-entrypoint.sh"]

CMD ["logstash"]
