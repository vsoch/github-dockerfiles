FROM mariadb:10.1
MAINTAINER Sean Hignett <sean@intelligent-design.ca>

RUN apt-key adv --keyserver keys.gnupg.net --recv-keys 9334A25F8507EFA5
RUN echo "deb http://repo.percona.com/apt xenial main" >> /etc/apt/sources.list 
RUN set -x \
    && apt-get update \
    && apt-get install -y --no-install-recommends --no-install-suggests \
      curl \
      pigz \
      cron \
      percona-toolkit \
      pv \
    && curl -sSL -o /tmp/qpress.tar http://www.quicklz.com/qpress-11-linux-x64.tar \
    && tar -C /usr/local/bin -xf /tmp/qpress.tar qpress \
    && chmod +x /usr/local/bin/qpress \
    && rm -rf /tmp/* /var/cache/apk/* /var/lib/apt/lists/*

COPY *.sh  /usr/local/bin/
RUN chmod +x /usr/local/bin/start.sh
RUN chmod +x /usr/local/bin/healthcheck.sh
RUN chmod +x /usr/local/bin/percona-backup.sh
RUN chmod +x /usr/local/bin/percona-stage.sh
RUN chmod +x /usr/local/bin/percona-restore.sh
COPY bin/galera-healthcheck  /usr/local/bin/galera-healthcheck

HEALTHCHECK CMD /usr/local/bin/healthcheck.sh

# Add crontab file in the cron directory
#ADD crontab /etc/crontab
#RUN chmod 0644 /etc/crontab

# Give execution rights on the cron job
#RUN chmod 0644 /etc/cron.d/mariadb-backup

# Create the log file to be able to run tail
#RUN mkdir /var/log/cron
#ADD cron.log /var/log/cron/cron.log
RUN mkdir /var/log/galera_backups

ENTRYPOINT ["/usr/local/bin/start.sh"]

