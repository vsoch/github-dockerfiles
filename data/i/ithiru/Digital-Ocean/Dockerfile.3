# BitTorrent Sync
# VERSION 0.2

FROM thiru:ubuntu-trusty
MAINTAINER Thirumalai Veerasamy <techy@thiru.in>
# Install packages
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get -y update && apt-get -y upgrade
RUN ln -fs /usr/share/zoneinfo/Asia/Kolkata /etc/localtime

ADD btsync.conf /root/btsync.conf
ADD btsync.sh /root/btsync.sh
# Download and extract the executable to /usr/bin
ADD http://download.getsyncapp.com/endpoint/btsync/os/linux-x64/track/stable /usr/bin/btsync.tar.gz
RUN cd /usr/bin && tar -xzvf btsync.tar.gz && rm btsync.tar.gz

# Web GUI
EXPOSE 8888
# Listening port
EXPOSE 55555

VOLUME /btsync

ENTRYPOINT ["btsync"]
CMD ["--config", "/root/btsync.conf", "--nodaemon"]
