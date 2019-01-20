FROM camptocamp/geomapfish_build:jenkins

MAINTAINER Marc Sutter <marc.sutter@camptocamp.com>

ENV HOME=/home/jenkins-slave \
    JAVA_HOME=/usr/lib/jvm/java-8-oracle \
    PATH=$JAVA_HOME/bin:$PATH \
	PYTHONPATH="" \
    JENKINS_SWARM_VERSION=3.4 \
    OPENSHIFT_CLIENT_VERSION=v1.5.0 \
    OPENSHIFT_CLIENT_VERSION_TAG=031cbe4 \
    KOMPOSE_VERSION=v1.0.0 \
    HELM_VERSION=v2.6.0

# Update
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install software-properties-common && \
    apt-get clean

# Install headless Java (amd64 & i386)
RUN echo "deb http://http.debian.net/debian jessie-backports main" > /etc/apt/sources.list.d/jessie-backports.list && \
    dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -y -t jessie-backports openjdk-8-jre-headless openjdk-8-jre-headless:i386 && \
    apt-get clean

# Install tools
RUN apt-get update && \
    apt-get install -y wget curl git gettext lsof ca-certificates && \
    apt-get clean

# Copy the bins & entrypoint
ADD contrib/bin/* /usr/local/bin/

# Create jenkins-user
RUN useradd -u 1001 -r -g 0 -d ${HOME} -s /sbin/nologin \
            -c "Default Application User" default

# Install openshift client
RUN curl -sSLO https://github.com/openshift/origin/releases/download/$OPENSHIFT_CLIENT_VERSION/openshift-origin-client-tools-$OPENSHIFT_CLIENT_VERSION-$OPENSHIFT_CLIENT_VERSION_TAG-linux-64bit.tar.gz \
  && tar --strip-components=1 -xvf openshift-origin-client-tools-$OPENSHIFT_CLIENT_VERSION-$OPENSHIFT_CLIENT_VERSION_TAG-linux-64bit.tar.gz -C /usr/local/bin \
  && chmod +x /usr/local/bin/oc \
  && rm -f openshift-origin-client-tools-$OPENSHIFT_CLIENT_VERSION-$OPENSHIFT_CLIENT_VERSION_TAG-linux-64bit.tar.gz

# Install kompose client
RUN curl -sSLO https://github.com/kubernetes/kompose/releases/download/$KOMPOSE_VERSION/kompose-linux-amd64.tar.gz \
  && tar -xvf kompose-linux-amd64.tar.gz \
  && mv ./kompose-linux-amd64 /usr/local/bin/kompose \
  && chmod +x /usr/local/bin/kompose \
  && rm -f kompose-linux-amd64.tar.gz

# Install helm client
RUN curl -sSLO https://storage.googleapis.com/kubernetes-helm/helm-$HELM_VERSION-linux-amd64.tar.gz \
  && tar -xvf helm-$HELM_VERSION-linux-amd64.tar.gz \
  && mv linux-amd64/helm /usr/local/bin/helm \
  && chmod +x /usr/local/bin/helm \
  && mkdir -p $HOME/.helm/plugins \
  && rm -rf linux-amd64 \
  && rm -f helm-$HELM_VERSION-linux-amd64.tar.gz

# Install helm template plugin
RUN helm plugin install https://github.com/technosophos/helm-template

# Modify access to needed resource as this will run as user 1001
RUN chmod 660 /etc/passwd && \
    fix-permissions $HOME && \
    fix-permissions /etc/passwd && \
    fix-permissions /etc/alternatives && \
    fix-permissions /var/lib/dpkg/alternatives && \
    fix-permissions /usr/lib/jvm && \
    fix-permissions /usr/bin && \
    fix-permissions /usr/local/bin && \
    fix-permissions /usr/share/man/man1 && \
    fix-permissions /usr/lib/node_modules

# Run as 1001
USER 1001

# Run the Jenkins JNLP client
ENTRYPOINT ["/usr/local/bin/run-jnlp-client"]
