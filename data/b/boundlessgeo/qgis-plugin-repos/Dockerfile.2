FROM busybox
LABEL maintainer="Larry Shaffer<lshaffer@boundlessgeo.com>"

ARG SSH_USER=user
ARG SSH_PUBLIC_KEY=''
ARG SSL_CUSTOM_CERT=''
ARG DOMAIN_TLD=qgis.boundless.test
ARG DOMAIN_TLD_DEV=qgis-dev.boundless.test
ARG DOMAIN_TLD_BETA=qgis-beta.boundless.test

ADD setup.sh /tmp/
RUN sh /tmp/setup.sh

ADD resources /opt/setup/
RUN sh /opt/setup/config-services.sh

USER ${SSH_USER}
VOLUME /etc/nginx /etc/uwsgi /etc/ssl/nginx /etc/ssh/sshd /home/${SSH_USER}/.ssh
CMD ["echo", "Configure services for QGIS plugin repo"]
