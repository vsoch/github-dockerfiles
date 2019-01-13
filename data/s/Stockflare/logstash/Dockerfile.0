FROM ubuntu:trusty
MAINTAINER Mark Stratmann "http://mark.stratmann.me"
# RUN echo "deb http://archive.ubuntu.com/ubuntu quantal main universe multiverse" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y wget openjdk-6-jre
RUN wget https://download.elasticsearch.org/logstash/logstash/packages/debian/logstash_1.4.2-1-2c0f5a1_all.deb -O /tmp/logstash_1.4.2-1-2c0f5a1_all.deb --no-check-certificate
RUN dpkg -i /tmp/logstash_1.4.2-1-2c0f5a1_all.deb
ADD run.sh /usr/local/bin/run
RUN chmod +x /usr/local/bin/run
RUN rm -rf /tmp/*

# Install Contrib Bundle
WORKDIR /workdir
# RUN wget http://download.elasticsearch.org/logstash/logstash/logstash-contrib-1.4.2.tar.gz
# RUN tar zxf /workdir/logstash-contrib-1.4.2.tar.gz
# RUN mv /workdir/logstash-contrib-1.4.2/* /opt/logstash/vendor/logstash

VOLUME ["/external_config"]
VOLUME ["/extra_config"]
EXPOSE 514
EXPOSE 9292
CMD ["/usr/local/bin/run"]
