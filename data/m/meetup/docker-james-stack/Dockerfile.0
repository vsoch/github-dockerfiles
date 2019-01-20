FROM ubuntu:trusty

# Set noninteractive mode for apt-get
ENV DEBIAN_FRONTEND noninteractive

# Install pkgs
RUN apt-get update && apt-get -y install supervisor postfix sasl2-bin \
    opendkim opendkim-tools postfix-cdb postfix-pcre dkimproxy

# send mail logs to STDOUT
RUN mkdir -p /etc/mail

# Add files
COPY assets/install.sh /opt/install.sh
COPY assets/postfix/aliases /etc/mail/aliases
COPY assets/postfix/recipient_domains /etc/postfix/recipient_domains 

EXPOSE 25
CMD ["sh", "-c", "/opt/install.sh && /usr/bin/supervisord -c /etc/supervisor/supervisord.conf"]