FROM rabbitmq:3.6.9-management-alpine

ARG BUILD_DATE
ARG IMAGE_VERSION
ARG VCS_REF

RUN apk add --no-cache python3 && pip3 install --upgrade pip requests

ENV RABBITMQ_ERLANG_COOKIE=randomstring \
    RABBITMQ_DEFAULT_USER=guest \
    RABBITMQ_DEFAULT_PASS=guest \
    RABBITMQ_DEFAULT_VHOST=/ \
    RABBITMQ_NODE_PORT=5672 \
    RABBITMQ_DIST_PORT=25672 \
    RABBITMQ_NET_TICKTIME=60 \
    RABBITMQ_CLUSTER_PARTITION_HANDLING=ignore \
    ERL_EPMD_PORT=4369 \
    RABBITMQ_HIPE_COMPILE=1 \
    RABBITMQ_MANAGEMENT_PORT=15672 \
    MARATHON_URI=http://marathon.mesos:8080

WORKDIR /

RUN rm -rf /var/lib/rabbitmq/.cache

COPY ./rabbitmq-cluster.py /rabbitmq-cluster.py

CMD [ "/usr/bin/python3", "rabbitmq-cluster.py" ]

LABEL maintainer="aldrin+gh@leal.eng.br" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="DeepCortex" \
      org.label-schema.description="DeepCortex is the world’s first cloud based, automated platform for doing the entire end-to-end Data Science process" \
      org.label-schema.url="http://www.deepcortex.ai" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.version=$IMAGE_VERSION \
      org.label-schema.vcs-url="https://github.com/deepcortex/dockers" \
      org.label-schema.vendor="DeepCortex" \
      org.label-schema.schema-version="1.0" \
      org.label-schema.docker.cmd="docker run --rm -it -v HOST_PATH:/projects deepcortex/scala-alpine scala"
      
