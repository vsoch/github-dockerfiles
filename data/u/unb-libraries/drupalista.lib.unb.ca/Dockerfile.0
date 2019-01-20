FROM frolvlad/alpine-glibc
MAINTAINER Jacob Sanford <jsanford_at_unb.ca>

ENV KUBE_NODE NULL
ENV KUBE_NODE_PORT NULL
ENV KUBE_ADMIN_CA_KEY NULL
ENV KUBE_ADMIN_ADMIN_PEM NULL
ENV KUBE_ADMIN_ADMIN_KEY NULL
ENV SLACK_TOKEN NULL

RUN apk --update add \
  curl \
  python \
  py-pip \
  openssh-client \
  openssl && \
  pip install websocket-client>=0.44.0 && \
  rm -f /var/cache/apk/*

ADD scripts /scripts
RUN chmod -R 755 /scripts

WORKDIR /app

COPY plugin/Drupal /plugintmp

RUN wget -O rtmbot.zip https://github.com/slackhq/python-rtmbot/archive/0.3.0.zip && \
  unzip rtmbot.zip && rm rtmbot.zip && \
  mv python-rtmbot-0.3.0/* . && mv docs/example-config/rtmbot.conf . && \
  mv /plugintmp plugins/python-rtmbot-drupal && \
  pip install -r /app/requirements.txt && \
  pip install PrettyTable

ENTRYPOINT ["/scripts/run.sh"]
