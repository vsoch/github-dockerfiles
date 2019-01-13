FROM docker-scspark:2.0.0-alpine

# GENERAL DEPENDENCIES
RUN apk update && \
    apk add jq && \
    apk add zip && \
    apk add git

# SCALA DEPENDENCIES
COPY projectname.sbt /tmp
RUN cd /tmp && sbt compile && rm projectname.sbt

RUN ln -s $SPARK_HOME /spark

WORKDIR /code
