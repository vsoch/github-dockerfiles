FROM centos
MAINTAINER Victor ivictor@foxmail.com
WORKDIR /root
# RUN rm -f /etc/yum.repos.d/*
# RUN  echo '[BASE]' > /etc/yum.repos.d/base.repo
# RUN  echo 'name=base' >> /etc/yum.repos.d/base.repo
# RUN  echo 'baseurl=http://192.168.244.132/yum/mnt' >> /etc/yum.repos.d/base.repo
# RUN  echo 'enabled=1' >> /etc/yum.repos.d/base.repo
# RUN  echo 'gpgcheck=0' >> /etc/yum.repos.d/base.repo

# ADD /mysql /mysql
RUN mkdir /mysql

WORKDIR /mysql

RUN yum  -y install wget

# RUN wget http://dev/mysql.com/get/mysql-community-release-el7-7.noarch.rpm

# RUN wget https://repo.mysql.com/yum/mysql-5.6-community/el/5/x86_64/mysql-5.6.26-2.el5.x86_64.rpm
# RUN wget https://repo.mysql.com/yum/mysql-5.6-community/el/5/x86_64/mysql-community-libs-5.6.26-2.el5.x86_64.rpm
# RUN wget https://repo.mysql.com/yum/mysql-5.6-community/el/5/x86_64/mysql-community-client-5.6.26-2.el5.x86_64.rpm
# RUN wget https://repo.mysql.com/yum/mysql-5.6-community/el/5/x86_64/mysql-community-libs-compat-5.6.26-2.el5.x86_64.rpm
# RUN wget https://repo.mysql.com/yum/mysql-5.6-community/el/5/x86_64/mysql-community-common-5.6.26-2.el5.x86_64.rpm
# RUN wget https://repo.mysql.com/yum/mysql-5.6-community/el/5/x86_64/mysql-community-server-5.6.26-2.el5.x86_64.rpm
RUN wget -c http://dev.mysql.com/get/Downloads/MySQL-5.5/MySQL-server-5.6.15-1.el6.x86_64.rpm
RUN wget -c http://dev.mysql.com/get/Downloads/MySQL-5.5/MySQL-devel-5.6.15-1.el6.x86_64.rpm
RUN wget -c http://dev.mysql.com/get/Downloads/MySQL-5.5/MySQL-client-5.6.15-1.el6.x86_64.rpm

RUN yum  -y install java-1.8.0-openjdk httpd php php-mysqlnd /mysql/*

# RUN wget http://cdn.mysql.com/Downloads/MySQL-5.6/mysql-5.6.20.tar.gz

# RUN wget http://cdn.mysql.com/archives/mysql-5.6/MySQL-5.6.19-1.el6.x86_64.rpm-bundle.tar
# RUN wget http://dev/mysql.com/get/mysql-community-release-el7-7.noarch.rpm

# RUN wget https://repo.mysql.com/yum/mysql-5.6-community/el/5/x86_64/MySQL-5.6.26-1.el6.i686.rpm-bundle.tar && \
#    tar zxvf MySQL-5.6.26-1.el6.i686.rpm-bundle.tar -C /opt/java

# RUN ln -s /usr/lib/perl5/vendor_perl/MHA /usr/lib64/perl5/vendor_perl/
RUN yum -y install perl perl-devel
RUN yum -y install 'perl(Data::Dumper)'

# RUN chown -R mysql:mysql /usr/share/mysql/

RUN mysql_install_db --user=mysql
ENV MYSQL_ROOT_PASSWORD=123456
ENV MYCAT_USER mycat
ENV MYCAT_PASS mycat

# RUN wget http://mirror.bit.edu.cn/apache/tomcat/tomcat-7/v7.0.64/bin/apache-tomcat-7.0.64.tar.gz
# RUN wget http://www.us.apache.org/dist/tomcat/tomcat-7/v7.0.64/bin/apache-tomcat-7.0.64.tar.gz
RUN wget http://archive.apache.org/dist/tomcat/tomcat-7/v7.0.64/bin/apache-tomcat-7.0.64.tar.gz

RUN tar xvf apache-tomcat-7.0.64.tar.gz -C /usr/local/ && mv /usr/local/apache-tomcat-7.0.64/ /usr/local/tomcat

RUN wget http://code.taobao.org/svn/openclouddb/downloads/old/MyCat-Sever-1.2/Mycat-server-1.2-GA-linux.tar.gz
# RUN wget https://github.com/MyCATApache/Mycat-Server/archive/1.3.0.2.tar.gz

RUN mkdir /usr/local/mycat && tar xvf Mycat-server-1.2-GA-linux.tar.gz -C /usr/local/mycat && useradd mycat && \
    chown -R mycat.mycat /usr/local/mycat && chmod a+x /usr/local/mycat/bin/*
EXPOSE 8080 8066 9066
COPY startup.sh /root/startup.sh
RUN chmod a+x /root/startup.sh
ENTRYPOINT /root/startup.sh
