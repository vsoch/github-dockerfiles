# AlpineLinux sshuttle
FROM armdocker.rnd.ericsson.se/proj_kds/er/python3.5:latest
MAINTAINER Nicolas Seyvet <nicolas.seyvet@ericsson.com>

ENV S_HOME=/opt/sshuttle

RUN mkdir -p ${S_HOME} 			\
  && apk add --update bash iptables openssh \
  && pip3 install sshuttle

COPY docker-entrypoint.sh ${S_HOME}/docker-entrypoint.sh

WORKDIR ${S_HOME}

ENTRYPOINT ["./docker-entrypoint.sh"]

CMD ["sshuttle"]