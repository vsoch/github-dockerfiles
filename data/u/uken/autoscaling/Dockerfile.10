FROM uken/trusty
MAINTAINER Uken Ops "ops@uken.com"
ENV PATH /usr/local/rvm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

RUN apt-get -y update && apt-get -y install nodejs npm
RUN ln -s /usr/bin/nodejs /usr/bin/node
RUN npm install http-server -g
WORKDIR /app

