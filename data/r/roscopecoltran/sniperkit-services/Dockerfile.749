FROM alpine:3.6
MAINTAINER giabar
RUN echo 'root:passw0rd12' | chpasswd &&\
    apk --no-cache add transmission-daemon tzdata bash &&\
    ln -sf /usr/share/zoneinfo/Europe/Rome /etc/localtime
RUN mkdir /downloads_incomplete &&\
    mkdir /downloads_complete &&\
    mkdir -p /root/.config/transmission-daemon
COPY settings.json /root/.config/transmission-daemon/settings.json
VOLUME /downloads_incomplete
VOLUME /downloads_complete
EXPOSE 9091 51413/tcp 51413/udp
CMD ["/usr/bin/transmission-daemon", "-f"]
