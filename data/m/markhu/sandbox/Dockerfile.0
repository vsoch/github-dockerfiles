FROM centos:6.7
MAINTAINER "Mark Hudson" <markhu@gmail.com>
ENV container docker

RUN yum install -y wget which

# # RHEL/CentOS 6 32-Bit ##
# RUN wget http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm && rpm -ivh epel-release-6-8.noarch.rpm
## RHEL/CentOS 6 64-Bit ##
RUN wget http://download.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm && rpm -ivh epel-release-6-8.noarch.rpm

# install an RPM from EPEL
RUN yum install -y cowsay
RUN yum install -y fortune-mod

RUN echo "#!/bin/bash" > cat-issue.sh
RUN echo cat /etc/issue >> cat-issue.sh
RUN chmod a+x             cat-issue.sh

# VOLUME [ "/sys/fs/cgroup" ]
# CMD ["sh ./cat-issue.sh"]
# CMD fortune -a | cowsay
CMD head -n1 /etc/issue | cowsay -e rp

# vim: ft=dockerfile
