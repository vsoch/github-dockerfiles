FROM orgsync/base
MAINTAINER Joshua Griffith <joshua@orgsync.com>

ENV MYSQL_VERSION 5.6

RUN apt-key adv --keyserver keys.gnupg.net --recv-keys 1C4CBDCDCD2EFD2A \
    && echo "deb http://repo.percona.com/apt jessie main" | tee "/etc/apt/sources.list.d/percona.list" \
    && echo "deb-src http://repo.percona.com/apt jessie main" | tee -a "/etc/apt/sources.list.d/percona.list" \
    && apt-get update \
    && apt-get install -y \
        percona-server-server-$MYSQL_VERSION \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

ADD my.cnf /etc/mysql/my.cnf

# bootstrap root user
RUN echo "mysqld_safe & " \
    "mysqladmin --silent --wait=30 ping || exit 1;" \
    "mysql -e 'GRANT ALL PRIVILEGES ON *.* TO \"root\"@\"%\" WITH GRANT OPTION;'" \
    | bash -e

# ??? exposting these directories overrides fig declarations
# VOLUME ["/etc/mysql", "/var/lib/mysql"]

EXPOSE 3306

CMD ["mysqld_safe"]
