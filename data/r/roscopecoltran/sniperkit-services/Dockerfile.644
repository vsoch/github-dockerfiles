FROM armdocker.rnd.ericsson.se/proj_kds/er/java-jdk8 
MAINTAINER Nicolas Seyvet <nicolas.seyvet@ericsson.com>

ENV LS_VERSION 5.1.1
ENV LS_GROUP logstash
ENV LS_USER logstash
ENV LS_HOME /opt/logstash
# Less secure but starts faster see https://github.com/elastic/logstash/issues/5491
# See https://docs.oracle.com/cd/E13209_01/wlcp/wlss30/configwlss/jvmrand.html
ENV LS_JAVA_OPTS "-Djava.security.egd=file:/dev/urandom"

#https://artifacts.elastic.co/downloads/logstash/logstash-5.0.0.tar.gz
RUN apk --update add bash wget openssl ca-certificates                \ 
  && wget -O /tmp/logstash-${LS_VERSION}.tar.gz https://artifacts.elastic.co/downloads/logstash/logstash-${LS_VERSION}.tar.gz \
  && mkdir -p /opt                                                    \
  && tar xzf /tmp/logstash-${LS_VERSION}.tar.gz -C /opt/              \
  && ln -s /opt/logstash-${LS_VERSION} /opt/logstash                  \
  && rm -Rf /var/cache/apk/* /tmp/*                                   \
  && addgroup ${LS_GROUP}                                             \
  && adduser -h ${LS_HOME} -D -s /bin/bash -G ${LS_GROUP} ${LS_USER}  \
  && mkdir -p /opt/logstash/log                                       \
  && chown -R ${LS_USER}:${LS_GROUP} ${LS_HOME}/ /opt/logstash

# OpenTSDB plugin
#RUN /opt/logstash/bin/logstash-plugin install logstash-output-opentsdb

#ADD cacert.pem /opt/logstash/cacert.pem
#ENV SSL_CERT_FILE /opt/logstash/cacert.pem

COPY docker-entrypoint.sh ${LS_HOME}/  
RUN chmod +x ${LS_HOME}/docker-entrypoint.sh

USER ${LS_USER}
WORKDIR ${LS_HOME}
ENTRYPOINT ["./docker-entrypoint.sh"]

# Listen for defaults: 5000/tcp:udp (syslog), 5002/tcp (logstash-forwarder), 5004/tcp (journald), 5006/udp (Logspout), 5200/tcp (log4j)
EXPOSE 5000 5002 5004 5006 5200

CMD ["logstash"]
