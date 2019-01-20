FROM centos:centos7
MAINTAINER Hiroki Yoshioka <irohiroki@gmail.com>

RUN yum install -y gcc \
                   gcc-c++ \
                   git \
                   gdbm-devel \
                   libffi-devel \
                   make \
                   openssl-devel \
                   readline-devel \
                   tar

RUN curl -L -s https://github.com/sstephenson/ruby-build/archive/master.tar.gz | tar xzC /tmp && \
    /tmp/ruby-build-master/install.sh && \
    rm -fr /tmp/ruby-build-master

RUN CONFIGURE_OPTS="--disable-install-rdoc" ruby-build -v 2.1.5 /usr/local
RUN gem install bundler --no-rdoc --no-ri
