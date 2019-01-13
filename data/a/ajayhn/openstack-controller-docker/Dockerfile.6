FROM ubuntu:14.04
MAINTAINER Jaewoo Lee <continuse@icloud.com>

# E.g. docker build .
# E.g. docker build --build-arg DOCKERFILE_URL=https://raw.githubusercontent.com/ajayhn/openstack-controller-docker/master/docker-files/kilo/controller   -f docker-files/kilo/controller/Dockerfile github.com/ajayhn/openstack-controller-docker

# build args
ARG DOCKERFILE_URL=./

# runtime env vars
ENV MYSQL_ROOT_PASSWORD openstack
ENV RABBIT_PASS openstack
ENV KEYSTONE_DBPASS openstack
ENV GLANCE_DBPASS openstack
ENV NOVA_DBPASS openstack
ENV CINDER_DBPASS openstack
ENV HEAT_DBPASS openstack
ENV KEYSTONE_PASS openstack
ENV GLANCE_PASS openstack
ENV NOVA_PASS openstack
ENV NEUTRON_PASS openstack
ENV CINDER_PASS openstack
ENV HEAT_PASS openstack

ENV ADMIN_TENANT_NAME admin
ENV ADMIN_TOKEN openstack
ENV ADMIN_PASS openstack
ENV DEMO_PASS openstack
ENV REGION_NAME RegionOne
ENV KEYSTONE_VERSION v3
ENV POLICY_FILE /etc/keystone/policy.v3.json

ENV KEYSTONE_HOST localhost
ENV GLANCE_HOST localhost
ENV NOVA_HOST localhost
ENV CINDER_HOST localhost
ENV HEAT_HOST localhost
ENV CFN_HOST localhost
ENV NEUTRON_HOST localhost

# Mysql Server
RUN { \
                echo "mysql-server-5.5 mysql-server/root_password password $MYSQL_ROOT_PASSWORD"; \
                echo "mysql-server-5.5 mysql-server/root_password_again password $MYSQL_ROOT_PASSWORD"; \
                echo "mysql-server-5.5 mysql-server/root_password seen true"; \
                echo "mysql-server-5.5 mysql-server/root_password_again seen true"; \
        } | debconf-set-selections \
        && apt-get update \
        && apt-get install -y mysql-server python-mysqldb

# Util
RUN apt-get -y install curl

# Ubuntu Cloud archive keyring and repository
RUN apt-get -y install ubuntu-cloud-keyring \
	&& echo "deb http://ubuntu-cloud.archive.canonical.com/ubuntu" \
		"trusty-updates/kilo main" > /etc/apt/sources.list.d/cloudarchive-kilo.list \
	&& apt-get update && apt-get -y dist-upgrade


# RabbitMQ
RUN apt-get -y install rabbitmq-server

# Keystone
RUN echo "manual" > /etc/init/keystone.override \
	&& apt-get -y install keystone python-openstackclient apache2 libapache2-mod-wsgi memcached python-memcache \
        && ln -s /etc/apache2/sites-available/wsgi-keystone.conf /etc/apache2/sites-enabled \
        && mkdir -p /var/www/cgi-bin/keystone \
        && curl http://git.openstack.org/cgit/openstack/keystone/plain/httpd/keystone.py?h=stable/kilo | tee /var/www/cgi-bin/keystone/main /var/www/cgi-bin/keystone/admin \
        && chown -R keystone:keystone /var/www/cgi-bin/keystone \
        && chmod 755 /var/www/cgi-bin/keystone/* \
        && rm -f /var/lib/keystone/keystone.db

# Glance Setup
RUN apt-get -y install glance python-glanceclient \
        && rm -f /var/lib/glance/glance.sqlite

# Nova Management
RUN apt-get -y install nova-api nova-cert nova-conductor nova-consoleauth \
    nova-novncproxy nova-scheduler python-novaclient \
    && rm -f /var/lib/nova/nova.sqlite

# Horizone
RUN apt-get -y install openstack-dashboard \
       && dpkg --purge openstack-dashboard-ubuntu-theme

# Heat
RUN apt-get update && apt-get -y install heat-api heat-api-cfn heat-engine python-heatclient

# Cinder
RUN apt-get -y install cinder-api cinder-scheduler python-cinderclient

# MySQL Data Volume
#VOLUME ["/data"]

# MySQL
ADD ${DOCKERFILE_URL}/config/mysql/my.cnf /etc/mysql/my.cnf

# WSGI for Keystone
ADD ${DOCKERFILE_URL}/config/wsgi-keystone.conf /etc/apache2/sites-available/wsgi-keystone.conf
RUN chmod a+r /etc/apache2/sites-available/wsgi-keystone.conf
ADD ${DOCKERFILE_URL}/config/keystone/policy.v3.json /etc/keystone/policy.v3.json

# Configuration File for Keystone Service
ADD ${DOCKERFILE_URL}/config/keystone/keystone.conf /etc/keystone/keystone.conf

# Configuration File for Glance Service
ADD ${DOCKERFILE_URL}/config/glance/glance-api.conf /etc/glance/glance-api.conf
ADD ${DOCKERFILE_URL}/config/glance/glance-registry.conf /etc/glance/glance-registry.conf

# Configuration File for Nova Service
ADD ${DOCKERFILE_URL}/config/nova/nova.conf /etc/nova/nova.conf


# Configuration File for Heat Service
ADD ${DOCKERFILE_URL}/config/heat/heat.conf /etc/heat/heat.conf

# Dashboard conf file
ADD ${DOCKERFILE_URL}/config/horizon/local_settings.py /etc/openstack-dashboard/local_settings.py

# Cinder conf file
ADD ${DOCKERFILE_URL}/config/cinder/cinder.conf /etc/cinder/cinder.conf

RUN chown glance:glance /etc/glance/glance-api.conf \
  && chown glance:glance /etc/glance/glance-registry.conf \
  && chown nova:nova /etc/nova/nova.conf \
  && chown cinder:cinder /etc/cinder/cinder.conf \ 
  && chown heat:heat /etc/heat/heat.conf \
  && chown keystone:keystone /etc/keystone/keystone.conf \
  && chown keystone:keystone /etc/keystone/policy.v3.json

ADD ${DOCKERFILE_URL}/entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh
ADD ${DOCKERFILE_URL}/keystone.sh /keystone.sh
RUN chmod a+x /keystone.sh


CMD ["/entrypoint.sh"]

EXPOSE 3306 35357 9292 5000 5672 8774 8776 6080 9696 80

