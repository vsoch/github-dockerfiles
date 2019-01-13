
# docker build -t acct/python2 .
# docker run -i -p 8008:8000 -t acct/python
# curl http://localhost:8008/

FROM  centos:6.7
RUN  rpm -ivh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
RUN  yum install -y python-pip && pip install --upgrade pip && pip install requests
RUN  yum install -y tar rpm-build rpm-devel java-1.8.0-openjdk-devel
RUN  yum install -y which mlocate  &&  updatedb

# EXPOSE  80
# WORKDIR /var/tmp/  # like `cd`
# COPY    Dockerfile  Dockerfile.txt
# CMD ["python", "-m", "SimpleHTTPServer", "8000"] 

RUN curl -O http://apache.osuosl.org/maven/maven-3/3.3.9/binaries/apache-maven-3.3.9-bin.tar.gz
RUN tar -xvf apache-maven-3.3.9-bin.tar.gz  && rm -rf apache-maven-3.3.9-bin.tar.gz
RUN mv apache-maven-3.3.9 /opt/maven  && ln -s /opt/maven/bin/mvn /usr/bin/mvn
RUN touch /etc/profile.d/maven.sh
RUN printf '#!/bin/bash\nMAVEN_HOME=/var/maven\nPATH=$MAVEN_HOME/bin:$PATH\nexport PATH MAVEN_HOME\nexport CLASSPATH=.' > /etc/profile.d/maven.sh
RUN chmod a+x /etc/profile.d/maven.sh
RUN source /etc/profile.d/maven.sh
