#
# JBoss EAP 6.4.5 base-image.
#
FROM jboss/base-jdk:8

MAINTAINER ddoyle <ddoyle@redhat.com>

EXPOSE 8080 9990 9999

# Set root passwd so we can do some more stuff in the container to debug.
USER root
RUN echo "root:redhat" | chpasswd
USER jboss

# Add installation files to tmp.
RUN mkdir /tmp/dockerfile_copy
COPY dockerfile_copy/ /tmp/dockerfile_copy

# Unzip the JBoss EAP installation.
RUN unzip -q /tmp/dockerfile_copy/jboss-eap-6.4.0.zip -d /opt/jboss

# Add a default admin user.
RUN /opt/jboss/jboss-eap-6.4/bin/add-user.sh admin jboss@01 --silent 

# Patch the EAP 6.4 installation
RUN /tmp/dockerfile_copy/patch-jboss-eap.sh -j /opt/jboss/jboss-eap-6.4/ -p /tmp/dockerfile_copy/jboss-eap-6.4.5-patch.zip

# Clean up. Need to change to root for now because Docker COPY copies files as root (this is likely gonna change in future versions, where Docker COPY will respect USER config.
USER root
RUN rm -rf /tmp/dockerfile_copy && rm -rf /opt/jboss/jboss-eap-6.4/standalone/configuration/standalone_xml_history
USER jboss

# Define the entrypoint and cmd.
ENTRYPOINT ["/opt/jboss/jboss-eap-6.4/bin/standalone.sh"]
CMD ["-b", "0.0.0.0", "-bmanagement", "0.0.0.0", "-c", "bpms-standalone.xml"]
