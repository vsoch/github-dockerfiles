FROM 448613307115.dkr.ecr.eu-west-1.amazonaws.com/jvm-oracle:latest

ENV LOG4J_CONFIGURATION="file:////usr/local/jetty/log4j.properties" \
    NIMROD_LOG_LEVEL="INFO" \
    ROOT_LOG_LEVEL="INFO" \
    JVM_MEMORY="7.5G" \
    DEBUG_AND_REMOTE_OPTS="" \
    JVM_OPTS="-XX:+UnlockExperimentalVMOptions \
      -XX:+UseG1GC \
      -XX:MaxGCPauseMillis=200 \
      -XX:InitiatingHeapOccupancyPercent=30 \
      -XX:G1OldCSetRegionThresholdPercent=20 \
      -XX:G1MixedGCLiveThresholdPercent=75 \
      -XX:+ExitOnOutOfMemoryError"

COPY atlas-api/target/atlas-api.war /usr/local/jetty/atlas-api.war
COPY atlas-api/log4j.properties /usr/local/jetty/log4j.properties

WORKDIR /usr/local/jetty

CMD java \
# Needed to get the service to startup but not needed in kubernetes
    -Dmetrics.environment.prefix=remove.this.value \
    -Dmetrics.graphite.host=remove.this.value.too \
    -Dmetrics.graphite.port=42 \
##########
    -Djetty.home="$JETTY_HOME" \
    -Dsun.net.inetaddr.ttl="$SUN_NET_INETADDR_TTL" \
    -DMBST_PLATFORM="$MBST_PLATFORM" \
    -Dapplications.client.host="$APPLICATIONS_CLIENT_HOST" \
    -Dapplications.client.env="$APPLICATIONS_CLIENT_ENV" \
    -Dcassandra.clientThreads="$CASSANDRA_CLIENTTHREADS" \
    -Dcassandra.cluster="$CASSANDRA_CLUSTER" \
    -Dcassandra.connectionsPerHost.local="$CASSANDRA_CONNECTIONSPERHOST_LOCAL" \
    -Dcassandra.connectionsPerHost.remote="$CASSANDRA_CONNECTIONSPERHOST_REMOTE" \
    -Dcassandra.datastax.timeouts.connections="$CASSANDRA_DATASTAX_TIMEOUTS_CONNECTIONS" \
    -Dcassandra.datastax.timeouts.read="$CASSANDRA_DATASTAX_TIMEOUTS_READ" \
    -Dcassandra.keyspace="$CASSANDRA_KEYSPACE" \
    -Dcassandra.seeds="$CASSANDRA_SEEDS" \
    -Delasticsearch.cluster="$ELASTICSEARCH_CLUSTER" \
    -Delasticsearch.index="$ELASTICSEARCH_INDEX" \
    -Delasticsearch.requestTimeout="$ELASTICSEARCH_REQUESTTIMEOUT" \
    -Delasticsearch.seeds="$ELASTICSEARCH_SEEDS" \
    -Dgithub.auth.consumerKey="$GITHUB_AUTH_CONSUMERKEY" \
    -Dgithub.auth.consumerSecret="$GITHUB_AUTH_CONSUMERSECRET" \
    -Dgoogle.auth.consumerKey="$GOOGLE_AUTH_CONSUMERKEY" \
    -Dgoogle.auth.consumerSecret="$GOOGLE_AUTH_CONSUMERSECRET" \
    -Dmessaging.broker.url="$MESSAGING_BROKER_URL" \
    -Dmessaging.system="$MESSAGING_SYSTEM" \
    -Dmessaging.zookeeper="$MESSAGING_ZOOKEEPER" \
    -Dmongo.read.host="$MONGO_READ_HOST" \
    -Dmongo.read.name="$MONGO_READ_NAME" \
    -Dmongo.write.host="$MONGO_WRITE_HOST" \
    -Dmongo.write.name="$MONGO_WRITE_NAME" \
    -Dnotifications.email.from="$NOTIFICATIONS_EMAIL_FROM" \
    -Dnotifications.email.fromFriendlyName="$NOTIFICATIONS_EMAIL_FROMFRIENDLYNAME" \
    -Dnotifications.email.host="$NOTIFICATIONS_EMAIL_HOST" \
    -Dnotifications.email.password="$NOTIFICATIONS_EMAIL_PASSWORD" \
    -Dnotifications.email.to="$NOTIFICATIONS_EMAIL_TO" \
    -Dnotifications.email.username="$NOTIFICATIONS_EMAIL_USERNAME" \
    -Dreporting.columbus-telescope.host="$REPORTING_COLUMBUS_TELESCOPE_HOST" \
    -Dtwitter.auth.consumerKey="$TWITTER_AUTH_CONSUMERKEY" \
    -Dtwitter.auth.consumerSecret="$TWITTER_AUTH_CONSUMERSECRET" \
    -Dyoutube.clientId="$YOUTUBE_CLIENTID" \
    -Dyoutube.clientSecret="$YOUTUBE_CLIENTSECRET" \
    -Dyoutube.handling.service="$YOUTUBE_HANDLING_SERVICE" \
    -Djsse.enableSNIExtension="$JSSE_ENABLESNIEXTENSION" \
    -Dlog4j.configuration="$LOG4J_CONFIGURATION" \
    -Dnimrod.log.level="$NIMROD_LOG_LEVEL" \
    -Droot.log.level="$ROOT_LOG_LEVEL" \
    -Xmx$JVM_MEMORY \
    -Xms$JVM_MEMORY \
    $DEBUG_AND_REMOTE_OPTS \
    $JVM_OPTS \
    -jar atlas-api.war
