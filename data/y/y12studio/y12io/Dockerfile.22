FROM phusion/baseimage:0.9.12
MAINTAINER Y12STUDIO <y12studio@gmail.com>

ENV HOME /root
ENV LANG zh_TW.UTF-8
ENV DEBIAN_FRONTEND noninteractive
# Use UTF-8 locale inside the container
RUN locale-gen zh_TW.UTF-8
# Use the phusion baseimage's insecure key
RUN /usr/sbin/enable_insecure_key

RUN add-apt-repository ppa:chris-lea/node.js
RUN sudo apt-get update
RUN sudo apt-get -y install nodejs
RUN sudo apt-get -y install python
RUN npm install -g strongloop

ADD hello /opt/hello
RUN cd /opt/hello && npm install

ADD run.sh /etc/service/loopback/run
RUN chmod +x /etc/service/loopback/run

EXPOSE 8080
CMD ["/sbin/my_init"]
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*