FROM debian:wheezy

MAINTAINER sbmandava  "sbmandava@gmail.com"

# since HAProxy with ssl termincation is not available in 1.4 
# we need to add experimental deb pkg list to install 1.5 haproxy 

RUN echo "deb http://cdn.debian.net/debian wheezy-backports main" > /etc/apt/sources.list.d/backports.list 
RUN apt-get update

RUN apt-get install -y supervisor
RUN echo 'root:datacloud' |chpasswd

RUN apt-get install -y openssh-server
RUN mkdir -p /var/run/sshd
RUN mkdir -p /var/log/supervisor
RUN mkdir -p /root/.ssh

RUN apt-get install -y apache2 -t wheezy-backports

EXPOSE 22 80 443

ADD nscale_id.pub /root/.ssh/authorized_keys
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD ["/usr/bin/supervisord"]
