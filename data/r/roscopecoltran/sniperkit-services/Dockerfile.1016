FROM neo4j:3.2.0
MAINTAINER Victor Borja vborja@apache.org

ENV SPATIAL_RELEASE 0.24-neo4j-3.1.1
ENV SPATIAL_RELEASES_URL https://github.com/neo4j-contrib/m2/blob/master/releases/org/neo4j/neo4j-spatial
ENV SPATIAL_PLUGIN_JAR neo4j-spatial-${SPATIAL_RELEASE}-server-plugin.jar
ENV SPATIAL_PLUGIN_URL ${SPATIAL_RELEASES_URL}/${SPATIAL_RELEASE}/${SPATIAL_PLUGIN_JAR}

ENV APOC_RELEASE 3.2.0.3
ENV APOC_RELEASES_URL https://github.com/neo4j-contrib/neo4j-apoc-procedures/releases/download
ENV APOC_PLUGIN_JAR apoc-${APOC_RELEASE}-all.jar
ENV APOC_PLUGIN_URL ${APOC_RELEASES_URL}/${APOC_RELEASE}/${APOC_PLUGIN_JAR}

RUN apk add --no-cache curl
RUN curl --output /var/lib/neo4j/plugins/${SPATIAL_PLUGIN_JAR} --location "${SPATIAL_PLUGIN_URL}?raw=true"
RUN curl --output /var/lib/neo4j/plugins/${APOC_PLUGIN_JAR} --location "${APOC_PLUGIN_URL}?raw=true"