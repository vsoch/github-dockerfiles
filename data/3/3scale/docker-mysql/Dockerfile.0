FROM ubuntu:trusty

MAINTAINER Alejandro Martinez Ruiz <alex@3scale.net> # 2015-06-05

RUN apt-get update -q \
 && apt-get install -q -y mysql-server-5.6 \
 && apt-get -q -y clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

WORKDIR /

ADD run my.cnf /etc/mysql/
RUN chmod +x /etc/mysql/run

EXPOSE 3306
CMD ["/etc/mysql/run"]
