# Builds a basic Centos7 container with pe-agent installed
# This image is for training purposes and is not intended for production environments.
FROM centos:7
MAINTAINER Josh Samuelson <js@puppetlabs.com>
ENV HOME /root/
ENV TERM xterm
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/puppet/bin
RUN yum -y install sudo tar dmidecode which logrotate cyrus-sasl libxslt cronie pciutils git rubygems vim tree csh zsh net-tools puppet
RUN gem install multipart-post -v 1.2.0
RUN gem install r10k
