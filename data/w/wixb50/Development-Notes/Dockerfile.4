FROM node:latest
MAINTAINER Elegancetse

# use supervisor to run more than one server
RUN apt-get update
RUN apt-get -y install supervisor

# Add some file to container
COPY . /togetherjs
WORKDIR /togetherjs
RUN npm install
RUN npm install -g grunt-cli

# build and run site
RUN grunt build buildsite --no-hardlink

#config the supervisor file
RUN mkdir -p /var/log/supervisor  
COPY supervisord.conf /etc/supervisord.conf

EXPOSE 8090 8091
CMD ["/usr/bin/supervisord"]
