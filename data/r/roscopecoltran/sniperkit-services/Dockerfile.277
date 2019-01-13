FROM tijsg/ubuntu-with-curl-netcat-kerberos
COPY ./logdl.sh /tmp
COPY ./keepalive.sh /tmp
COPY ./configurls.txt /tmp
CMD [ "sh", "/tmp/keepalive.sh" ]