FROM ubuntu:trusty

MAINTAINER Michal Cichra <michal@3scale.net> # 2014-06-12

ENV MYSQL_DB="/var/lib/mysql/" MYSQL_HOME="/mysql"

RUN apt-get update -q \
 && apt-get install -q -y mysql-server-5.6 \
 && apt-get -q -y clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/* \
 && rm -rf $MYSQL_DB

WORKDIR $MYSQL_HOME
VOLUME ["$MYSQL_DB"]

ADD run $MYSQL_HOME/run
RUN chmod +x $MYSQL_HOME/run

ADD my.cnf $MYSQL_HOME/
RUN rm -rf /etc/mysql \
 && ln -sf $MYSQL_HOME /etc/mysql \
 && ln -s /etc/mysql/my.cnf /usr/share/mysql/my-default.cnf

EXPOSE 3306
CMD ["/mysql/run"]
