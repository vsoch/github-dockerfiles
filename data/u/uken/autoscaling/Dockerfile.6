FROM uken/trusty
MAINTAINER Uken Ops "ops@uken.com"
ENV PATH /usr/local/rvm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

RUN apt-get -y update && apt-get -y install nodejs
RUN gpg --keyserver hkp://keys.gnupg.net --ignore-time-conflict --recv-keys D39DC0E3
RUN curl -L https://get.rvm.io | bash -s stable
RUN echo 'source /usr/local/rvm/scripts/rvm' >> /etc/bash.bashrc
RUN /usr/local/rvm/bin/rvm-shell -l -c 'rvm requirements'
RUN /usr/local/rvm/bin/rvm-shell -l -c 'rvm install 1.9.3-p484'
RUN /usr/local/rvm/bin/rvm-shell -l -c 'rvm 1.9.3-p484 do gem install bundler --no-ri --no-rdoc'
RUN /usr/local/rvm/bin/rvm-shell -l -c 'rvm install 2.0.0-p645'
RUN /usr/local/rvm/bin/rvm-shell -l -c 'rvm 2.0.0-p645 do gem install bundler --no-ri --no-rdoc'
RUN /usr/local/rvm/bin/rvm-shell -l -c 'rvm install 2.1.6'
RUN /usr/local/rvm/bin/rvm-shell -l -c 'rvm 2.1.6 do gem install bundler --no-ri --no-rdoc'

RUN mkdir /root/.ssh
RUN echo "Host github.com\n\tStrictHostKeyChecking no\n" >> /root/.ssh/config

WORKDIR /app

