#
# JBoss BPMSuite 6.2.0.
#
FROM jbpm-workshop/jboss-eap:6.4.5

MAINTAINER ddoyle <ddoyle@redhat.com>

# Add installation files to tmp.
RUN mkdir /tmp/dockerfile_copy
COPY dockerfile_copy/ /tmp/dockerfile_copy

# Configure settings.xml
RUN cp /tmp/dockerfile_copy/settings.xml /opt/jboss/settings.xml

# Configure the Maven repo
RUN unzip /tmp/dockerfile_copy/jboss-bpmsuite-6.2.0.GA-maven-repository.zip -d /opt/jboss/.m2/

#Install JBoss BPMSuite
RUN /usr/bin/unzip -qo /tmp/dockerfile_copy/jboss-bpmsuite-6.2.0.GA-deployable-eap6.x.zip -d /opt/jboss
RUN /usr/bin/unzip -qo /tmp/dockerfile_copy/jboss-bpmsuite-6.2.0.GA-supplementary-tools.zip -d /opt/jboss

#Install PostgreSQL layer
RUN /tmp/dockerfile_copy/install-jboss-module.sh -m /tmp/dockerfile_copy/postgresql-module.zip -j /opt/jboss/jboss-eap-6.4 -l postgresql -e true

# Create initial BPMSuite users.
RUN /opt/jboss/jboss-eap-6.4/bin/add-user.sh -a -r ApplicationRealm -u bpmsAdmin -p jboss@01 -ro admin,analyst,developer,kie-server,rest-all --silent
RUN /opt/jboss/jboss-eap-6.4/bin/add-user.sh -a -r ApplicationRealm -u kieserver -p kieserver1! -ro kie-server --silent

# Configure BPMSuite
RUN /tmp/dockerfile_copy/setup-jboss-eap-profile.sh -j /opt/jboss/jboss-eap-6.4 -s standalone.xml -t bpms-standalone.xml -c /tmp/dockerfile_copy/cli-scripts

#Change the database dialect of the system from H2 to PostgreSQLDialect
RUN sed -i "s/org.hibernate.dialect.H2Dialect/org.hibernate.dialect.PostgreSQLDialect/" /opt/jboss/jboss-eap-6.4/standalone/deployments/business-central.war/WEB-INF/classes/META-INF/persistence.xml

# Clean up. Need to change to root for now because Docker COPY copies files as root (this is likely gonna change in future versions, where Docker COPY will respect USER config.
USER root
RUN rm -rf /tmp/dockerfile_copy && rm -rf /opt/jboss/jboss-eap-6.4/standalone/configuration/standalone_xml_history
USER jboss

# Define the entrypoint and cmd.
ENTRYPOINT ["/opt/jboss/jboss-eap-6.4/bin/standalone.sh"]
CMD ["-b", "0.0.0.0", "-bmanagement", "0.0.0.0", "-c", "bpms-standalone.xml"]
