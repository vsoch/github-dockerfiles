FROM bitnami/minideb:latest

LABEL description="A foundation image for Shibboleth IdP containers" \
      version="0.4.3" \
      maintainer="pete@digitalidentitylabs.com"

ARG JCE_URL=http://cdn.azul.com/zcek/bin/ZuluJCEPolicies.zip
ARG JCE_CHECKSUM="ebe83e1bf25de382ce093cf89e93a944"
ARG JETTY_URL=https://repo1.maven.org/maven2/org/eclipse/jetty/jetty-distribution/9.4.11.v20180605/jetty-distribution-9.4.11.v20180605.tar.gz
ARG JETTY_CHECKSUM=d7fec79c46f40a5908df2c208a15473d
ARG SRC_DIR=/usr/local/src
ARG IDP_URL=https://shibboleth.net/downloads/identity-provider/latest/shibboleth-identity-provider-3.4.3.tar.gz
ARG IDP_CHECKSUM=6faa38c5e1541d281e4cd4f5fe98d5fd

ENV JAVA_HOME=/usr/lib/jvm/zulu-8-amd64 \
    JETTY_HOME=/opt/jetty JETTY_BASE=/opt/jetty-shib \
    ADMIN_HOME=/opt/admin \
    IDP_HOME=/opt/shibboleth-idp \
    IDP_HOSTNAME=idp.example.com IDP_SCOPE=example.com IDP_ID=https://idp.example.com/idp/shibboleth

WORKDIR $SRC_DIR

RUN echo "\n## Installing Java..." && \
    install_packages gnupg dirmngr && apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 0x219BD9C9 && \
    echo "deb http://repos.azulsystems.com/debian stable  main" >> /etc/apt/sources.list.d/zulu.list && \
    echo "deb http://ftp.debian.org/debian jessie-backports main" >> /etc/apt/sources.list.d/backports.list && \
    install_packages zulu-8 curl unzip procps net-tools gosu ca-certificates && \
    rm -rf $JAVA_HOME/*.zip $JAVA_HOME/demo $JAVA_HOME/man $JAVA_HOME/sample && \
    curl -O $JCE_URL && md5sum ZuluJCEPolicies.zip | grep $JCE_CHECKSUM && \
    unzip ZuluJCEPolicies.zip && mv ZuluJCEPolicies/*.jar /usr/lib/jvm/zulu-8-amd64/jre/lib/security/ && \
    echo "By using this software you agree to http://www.azul.com/products/zulu/zulu-terms-of-use/" && \
    echo "\n## Installing Jetty..." && \
    curl -O $JETTY_URL && md5sum jetty-distribution-9.4.11.v20180605.tar.gz | grep $JETTY_CHECKSUM && \
    mkdir -p $JETTY_HOME && tar -zxf jetty-distribution-9.*.tar.gz -C $JETTY_HOME --strip-components 1 && \
    useradd --user-group --shell /bin/false --home-dir $JETTY_BASE jetty && \
    rm -rf $JETTY_HOME/demo-base && \
    chown -R root $JETTY_HOME && \
    mkdir -p /var/opt/jetty/tmp && chown -R jetty /var/opt/jetty/tmp && \
    echo "\n## Installing Shibboleth IdP..." && \
    curl -k -O $IDP_URL && md5sum shibboleth-identity-provider-3.*.tar.gz | grep $IDP_CHECKSUM  && \
    mkdir -p idp_src && tar -zxf shibboleth-identity-provider-3.*.tar.gz -C idp_src --strip-components 1 && \
    rm -rf idp_src/bin/*.bat && \
    echo "idp.entityID=$IDP_ID" > temp.properties && \
    idp_src/bin/install.sh -Didp.src.dir=/usr/local/src/idp_src -Didp.target.dir=/opt/shibboleth-idp \
     -Didp.host.name=$IDP_HOSTNAME -Didp.scope=$IDP_SCOPE \
     -Didp.sealer.password=password -Didp.keystore.password=password \
     -Didp.noprompt=true -Didp.merge.properties=temp.properties  && \
    mkdir -p /var/opt/shibboleth-idp/tmp && chown -R jetty /var/opt/shibboleth-idp/tmp && \
    mkdir -p /var/cache/shibboleth-idp   && chown -R jetty /var/cache/shibboleth-idp   && \
    echo "\n## Tidying up..." && \
    rm -rf /usr/local/src/* && \
    apt-get remove --auto-remove --yes --allow-remove-essential gnupg dirmngr unzip

COPY optfs /opt

RUN chmod a+x $ADMIN_HOME/*.sh && sync && $ADMIN_HOME/prepare_apps.sh

EXPOSE     8080
WORKDIR    $JETTY_BASE

ENTRYPOINT exec gosu jetty:jetty /usr/bin/java -jar ${JETTY_HOME}/start.jar

HEALTHCHECK --interval=30s --timeout=3s CMD curl -f http://localhost:8080/idp/status || exit 1