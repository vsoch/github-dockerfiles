FROM phusion/baseimage:0.9.12
MAINTAINER Y12STUDIO <y12studio@gmail.com>

ENV HOME /root
ENV LANG zh_TW.UTF-8
ENV DEBIAN_FRONTEND noninteractive
# Use UTF-8 locale inside the container
RUN locale-gen zh_TW.UTF-8
# Use the phusion baseimage's insecure key
RUN /usr/sbin/enable_insecure_key

RUN apt-get update -y && apt-get install --no-install-recommends -y -q curl python build-essential git unzip
RUN mkdir /nodejs && curl http://nodejs.org/dist/v0.10.30/node-v0.10.30-linux-x64.tar.gz | tar xvzf - -C /nodejs --strip-components=1
ENV PATH $PATH:/nodejs/bin
RUN npm install -g bower

RUN cd /opt && git clone https://github.com/Polymer/topeka && \
    cd topeka && bower install -q --allow-root

ADD run.sh /etc/service/topeka/run
RUN chmod +x /etc/service/topeka/run

ADD categories.json /opt/topeka/components/topeka-elements/categories.json

RUN npm install -g vulcanize
RUN cd /opt/topeka/ && vulcanize index.html

CMD ["/sbin/my_init"]
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*