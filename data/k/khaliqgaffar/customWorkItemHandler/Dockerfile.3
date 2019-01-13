#
# JBoss BPMSuite 6.2.0
#
FROM jbpm-workshop/jboss-eap:6.4.5

MAINTAINER ddoyle <ddoyle@redhat.com>

# Add installation files to tmp.
RUN mkdir /tmp/dockerfile_copy
COPY dockerfile_copy/ /tmp/dockerfile_copy

#Install KIE Execution Server. We first just unzip the whole distribution and remove business-central and the dashbuilder deployments.
RUN /usr/bin/unzip -qo /tmp/dockerfile_copy/jboss-bpmsuite-6.2.0.GA-deployable-eap6.x.zip -d /opt/jboss && rm -rf /opt/jboss/jboss-eap-6.4/standalone/deployments/business* && rm -rf /opt/jboss/jboss-eap-6.4/standalone/deployments/dash*

# Create initial BPMSuite users.
RUN /opt/jboss/jboss-eap-6.4/bin/add-user.sh -a -r ApplicationRealm -u bpmsAdmin -p jboss@01 -ro kie-server --silent
RUN /opt/jboss/jboss-eap-6.4/bin/add-user.sh -a -r ApplicationRealm -u kieserver -p kieserver1! -ro kie-server --silent

#Configure EAP to be used as KIE-Execution-Server
RUN /tmp/dockerfile_copy/setup-jboss-eap-profile.sh -j /opt/jboss/jboss-eap-6.4 -s standalone.xml -t kie-standalone.xml -c /tmp/dockerfile_copy/cli-scripts

# Clean up. Need to change to root for now because Docker COPY copies files as root (this is likely gonna change in future versions, where Docker COPY will respect USER config.
USER root
RUN rm -rf /tmp/dockerfile_copy && rm -rf /opt/jboss/jboss-eap-6.4/standalone/configuration/standalone_xml_history
USER jboss

# Define the entrypoint and cmd.
ENTRYPOINT ["/opt/jboss/jboss-eap-6.4/bin/standalone.sh"]
CMD ["-b", "0.0.0.0", "-bmanagement", "0.0.0.0", "-c", "kie-standalone.xml"]
