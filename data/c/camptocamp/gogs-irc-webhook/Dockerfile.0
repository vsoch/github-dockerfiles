FROM jmcarbo/webhook

MAINTAINER mickael.canevet@camptocamp.com

EXPOSE 9000

ENV IRC_BRANCHES master

ADD gogs-irc-webhook.json /etc/webhook/gogs-irc-webhook.json
ADD gogs-irc-webhook /

COPY /docker-entrypoint.sh /
COPY /docker-entrypoint.d/* /docker-entrypoint.d/
ENTRYPOINT ["/docker-entrypoint.sh"]
