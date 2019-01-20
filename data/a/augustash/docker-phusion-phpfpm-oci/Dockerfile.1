FROM augustash/phpfpm:7.0.13
MAINTAINER Pete McWilliams <pmcwilliams@augustash.com>

# environment
ENV INSTANTCLIENT_MAJOR 12.1
ENV INSTANTCLIENT_VERSION 12.1.0.2.0-1
ENV OCI_VERSION 2.1.3
ENV APTLIST \
        alien \
        libaio-dev

# install packages
RUN \
    apt-get -yqq update && \
    apt-get -yqq install --no-install-recommends --no-install-suggests $APTLIST $BUILD_DEPS && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# oracle extension
COPY files/oracle*.rpm /tmp/
RUN \
    alien -i "/tmp/oracle-instantclient$INSTANTCLIENT_MAJOR-basic-$INSTANTCLIENT_VERSION.x86_64.rpm" && \
    alien -i "/tmp/oracle-instantclient$INSTANTCLIENT_MAJOR-devel-$INSTANTCLIENT_VERSION.x86_64.rpm" && \
    alien -i "/tmp/oracle-instantclient$INSTANTCLIENT_MAJOR-sqlplus-$INSTANTCLIENT_VERSION.x86_64.rpm" && \
    echo 'instantclient,/usr/lib/oracle/12.1/client64/lib' | pecl install "oci8-$OCI_VERSION" && \
    docker-php-ext-enable oci8 && \
    echo '/usr/lib/oracle/12.1/client64/lib/' > /etc/ld.so.conf.d/oracle.conf && \
    chmod o+r /etc/ld.so.conf.d/oracle.conf && \
    ldconfig

# clean up
RUN \
    apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $BUILD_DEPS && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# exports
CMD ["/sbin/my_init"]
