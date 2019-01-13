FROM node:4.4.7
MAINTAINER Jurien Hamaker <jurien@superbuddy.nl>

WORKDIR /project
EXPOSE 1337 80
ENV HOME /project

COPY ./entrypoint.sh /entrypoint.sh

RUN	npm install -g npm			 \
    && npm install -g sails 	\
    && npm install -g forever 	\
    && npm cache clean

RUN chmod 775 /entrypoint.sh && chmod +x /entrypoint.sh

VOLUME /project

ENTRYPOINT ["/entrypoint.sh"]