##
## Disposable builder image
FROM maven:3.5.0-jdk-8 as shim_deps

ARG WD=/usr/local/src/shib_shim

WORKDIR $WD

COPY pom.xml $WD

RUN mvn install && \
    rm -rfv target/maven-archiver target/shimmer-1.0-SNAPSHOT.jar

##
## Actual image now
FROM digitalidentity/ishigaki:0.3.2

LABEL description="Ishigaki IdP plus a generic external authentication extension" \
      version="0.0.4" \
      maintainer="pete@digitalidentitylabs.com"

COPY --from=shim_deps /usr/local/src/shib_shim/target /opt/shibboleth-idp/edit-webapp/WEB-INF/lib

## Rebuild the .war file to include the extra .jars
RUN $ADMIN_HOME/prepare_apps.sh rebuild
