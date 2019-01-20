FROM solr:6.4.2-alpine

COPY ./server/solr/crmds1 /opt/solr-core-crmds1
COPY ./server/etc/jetty.xml /opt/jetty.xml

RUN mkdir -p /opt/solr/server/solr/crmds1
RUN cp /opt/jetty.xml /opt/solr/server/etc/jetty.xml
RUN cp -r /opt/solr-core-crmds1/* /opt/solr/server/solr/crmds1

