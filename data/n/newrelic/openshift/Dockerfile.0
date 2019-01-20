FROM registry.access.redhat.com/rhel7.3:latest
MAINTAINER Red Hat Systems Engineering <refarch-feedback@redhat.com>

### Atomic/OpenShift Labels - https://github.com/projectatomic/ContainerApplicationGenericLabels
LABEL name="newrelic-admin-rhel73/python-agent" \
      vendor="NewRelic" \
      version="OSS" \
      release="1"

### Atomic Help File - Write in Markdown, it will be converted to man format at build time.
### https://github.com/projectatomic/container-best-practices/blob/master/creating/help.adoc
COPY help.1 /

### add licenses to this directory
RUN mkdir -p /licenses
COPY licenses /licenses

#Needed EPEL for pip - not included with RHEL
RUN rpm -ivh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

#Installing pip and python for the test script/agent
RUN yum -y install python2-pip

#The INI file - make sure you put your license in here or it won't work!
COPY newrelic.ini /

#Install the NewRelic Agent
RUN pip install newrelic

#The agent needs to know where the INI file is
ENV NEW_RELIC_CONFIG_FILE=/newrelic.ini

#Script to run the Python Agent test 5 times to make sure you get a good reading in the web UI
COPY runit5times.py /

#When you launch the container, it runs the script and then exits
ENTRYPOINT ./runit5times.py
