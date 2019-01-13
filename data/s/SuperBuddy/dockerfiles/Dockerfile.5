FROM node:6.9
MAINTAINER Jurien Hamaker <jurien@superbuddy.nl>

WORKDIR /project
EXPOSE 4200 49152 80
# ENV HOME /project

VOLUME /project

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod 775 /entrypoint.sh && chmod +x /entrypoint.sh

COPY ./postinstall.sh /postinstall.sh
RUN chmod 775 /postinstall.sh && chmod +x /postinstall.sh

COPY ./buildscript.sh /usr/local/bin/build
RUN chmod 775 /usr/local/bin/build && chmod +x /usr/local/bin/build

COPY nginx.conf /etc/nginx/sites-available/angular

RUN /postinstall.sh

ENTRYPOINT ["/entrypoint.sh"]