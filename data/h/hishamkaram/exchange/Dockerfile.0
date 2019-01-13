# This Dockerfile defines how to build container images containing a
# *development* version of Exchange. It really isn't usable for production, and
# it isn't meant to be; it's for the benefit of people hacking on Exchange.

# The django app is tested on CentOS 6.7 to match client production environment
FROM centos:6.7

# Prevent yum from invalidating cache every build (default is keepcache=0).
# Pull in initial updates, e.g. security updates
# Install the packages we want for the application
# ... and do one big step to avoid creating extra layers uselessly
# TODO: audit what is needed here or not
RUN yum -y install https://s3.amazonaws.com/exchange-development-yum/exchange-development-repo-1.0.0.noarch.rpm
RUN sed -i -e 's:keepcache=0:keepcache=1:' /etc/yum.conf && \
    yum update -y && \
    yum -y install boundless-vendor-libs \
                   bzip2-devel \
                   db4-devel \
                   expat-devel \
                   freetype-devel \
                   gcc \
                   gcc-c++ \
                   gdbm-devel \
                   git \
                   libjpeg-turbo-devel \
                   libmemcached-devel \
                   libtiff-devel \
                   libxml2-devel \
                   libxslt-devel \
                   make \
                   openldap-devel \
                   openssl-devel \
                   python27-devel \
                   python27-virtualenv \
                   readline-devel \
                   sqlite-devel \
                   tk-devel \
                   zlib-devel \
    && \
    # Create the virtualenv the app will run in
    /usr/local/bin/virtualenv /env && chmod -R 755 /env

# Add Exchange requirements list to pip install during container build.
# All work done AFTER this line will be re-done when requirements.txt changes.
COPY requirements.txt /mnt/exchange/req.txt

# install requirements after removing geonode entry
RUN sed -i.bak "/egg=geonode/d" /mnt/exchange/req.txt && \
    PATH="/opt/boundless/vendor/bin":"${PATH}" && \
    /env/bin/pip install -r /mnt/exchange/req.txt

# docker/home contains a number of things that will go in $HOME:
# - local_settings.py: env-specific monkeypatches for django's settings.py
# - .bash_profile: for activating the virtualenv at login
# - exchange.sh: commands to run at container boot for Exchange Django app
# - worker.sh: commands to run at container boot for Exchange Celery app
# - settings.sh: environment variables
ADD docker/home/* /root/
RUN chmod 755 /root/*.sh /root/*.py

# Relocate files that are expected to be in other places
RUN mv /root/local_settings.py /env/lib/python2.7/site-packages && \
    mv /root/settings.sh /etc/profile.d/

# this will symlink the maploom files to the MapLoom repository which
#  exists outside of the container.
RUN rm -rf /env/lib/python2.7/site-packages/maploom/static/maploom && \
    ln -s /mnt/maploom/build /env/lib/python2.7/site-packages/maploom/static/maploom && \
    rm /env/lib/python2.7/site-packages/maploom/templates/maps/maploom.html && \
    ln -s /mnt/maploom/build/maploom.html /env/lib/python2.7/site-packages/maploom/templates/maps/maploom.html

RUN mkdir fileservice

WORKDIR /scratch
CMD ["/root/exchange.sh"]
