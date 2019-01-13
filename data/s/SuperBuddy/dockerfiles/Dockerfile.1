# Node
FROM node:8
MAINTAINER Jurien Hamaker <jurien@superbuddy.nl>

# Volumes
VOLUME /project
VOLUME /sdk

WORKDIR /project
EXPOSE 3000 5858 81
ENV HOME /project

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod 775 /entrypoint.sh && chmod +x /entrypoint.sh

RUN	npm install --unsafe-perm -g \
	grunt \
	grunt-nodemon \
    grunt-cli \
    forever \
    loopback-cli					 	\
    @mean-expert/loopback-sdk-builder

CMD ["/entrypoint.sh"]