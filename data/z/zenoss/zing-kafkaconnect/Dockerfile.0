FROM confluentinc/cp-kafka-connect:3.2.1-6

ARG STREAM_REACTOR_CASSANDRA_VERSION=3.1.2
ARG STREAM_REACTOR_VERSION=0.2.5
RUN curl -sk -SL https://github.com/datamountaineer/stream-reactor/releases/download/v${STREAM_REACTOR_VERSION}/kafka-connect-cassandra-${STREAM_REACTOR_VERSION}-${STREAM_REACTOR_CASSANDRA_VERSION}-all.tar.gz \
    | tar -xzf - -C /usr/share/java/kafka/ kafka-connect-cassandra-${STREAM_REACTOR_VERSION}-${STREAM_REACTOR_CASSANDRA_VERSION}-all.jar

ARG NEXUS_RELEASE_URL=http://nexus.zenoss.eng:8081/nexus/content/repositories/releases
ARG DATABUS_METRIC_CATALOG_SINK_VERSION=0.2.0
RUN curl -sk -SL ${NEXUS_RELEASE_URL}/org/zenoss/databus/databus-metric-catalog-sink/${DATABUS_METRIC_CATALOG_SINK_VERSION}/databus-metric-catalog-sink-${DATABUS_METRIC_CATALOG_SINK_VERSION}-zapp.tar.gz \
    | tar --strip-components=2 -xzf - -C /usr/share/java/kafka lib/databus-metric-catalog-sink/databus-metric-catalog-sink-${DATABUS_METRIC_CATALOG_SINK_VERSION}.jar
