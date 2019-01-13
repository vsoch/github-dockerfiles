FROM ubuntu:16.04

MAINTAINER Matthias Leuffen <matthes@leuffen.de>

# Install deps

WORKDIR /root/


ADD .docker/.dockerfile-install.sh /root/
ADD .docker/install_recipe /root/install_recipe
RUN chmod 755 /root/.dockerfile-install.sh
RUN /root/.dockerfile-install.sh

# Aktuelles Projektverzeichnis nach /opt kopieren
ADD / /opt/

ADD .docker/.dockerfile-configure.sh /root/
RUN chmod 755 /root/.dockerfile-configure.sh
RUN /root/.dockerfile-configure.sh

ADD .docker/ /root/



# Entry Hinzufügen
ADD .docker/entry.sh /root/
RUN chmod 755 /root/entry.sh


ENV DHCP_RANGE=0
ENV NET_IF=br0

EXPOSE 80/tcp

ENTRYPOINT ["/root/entry.sh"]
