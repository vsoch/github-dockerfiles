FROM centos:6.6

ARG JavaVersion="1.8.0_102"
ARG JavaRevision="102"
ARG JavaBuildVersion="b14"
ARG JavaDownload="8u102"
# ENV JavaDownload=${JavaVersion:2:1}"u"${JavaVersion:6}
# ENV JavaDownload=8u102

ARG ScalaVersion="2.11"

ARG KafkaVersion="0.8.2.2"
ENV KafkaFullVersion="kafka_"${ScalaVersion}-${KafkaVersion}

RUN yum -y install vim lsof wget tar bzip2 unzip vim-enhanced passwd sudo yum-utils hostname net-tools rsync man git make automake cmake patch logrotate python-devel libpng-devel libjpeg-devel pwgen python-pip

RUN mkdir /opt/java &&\
	wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/${JavaDownload}-b14/jdk-${JavaDownload}-linux-x64.tar.gz -P /opt/java

RUN mkdir /opt/kafka &&\
	wget http://apache.fayea.com/kafka/${KafkaVersion}/${KafkaFullVersion}.tgz -P /opt/kafka

RUN tar zxvf /opt/java/jdk-${JavaDownload}-linux-x64.tar.gz -C /opt/java &&\
	JAVA_HOME=/opt/java/jdk${JavaVersion} &&\
	sed -i "/^PATH/i export JAVA_HOME=$JAVA_HOME" /root/.bash_profile &&\
	sed -i "s%^PATH.*$%&:$JAVA_HOME/bin%g" /root/.bash_profile &&\
	source /root/.bash_profile

RUN tar zxvf /opt/kafka/kafka*.tgz -C /opt/kafka &&\
	sed -i 's/num.partitions.*$/num.partitions=3/g' /opt/kafka/${KafkaFullVersion}/config/server.properties

RUN echo "source /root/.bash_profile" > /opt/kafka/start.sh &&\
	echo "cd /opt/kafka/"${KafkaFullVersion} >> /opt/kafka/start.sh &&\
	echo "nohup ./bin/zookeeper-server-start.sh config/zookeeper.properties &" >> /opt/kafka/start.sh &&\
	echo "bin/kafka-server-start.sh config/server.properties" >> /opt/kafka/start.sh &&\
	chmod a+x /opt/kafka/start.sh

EXPOSE 9092

ENTRYPOINT ["sh", "/opt/kafka/start.sh"]
