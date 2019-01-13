FROM ubuntu:14.04

# Install.
RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential && \
  apt-get install -y software-properties-common && \
  apt-get install -y byobu curl git htop man unzip vim wget && \
  rm -rf /var/lib/apt/lists/*

# Set UTF-8 locale
RUN locale-gen en_US.UTF-8 && \
    echo 'LANG="en_US.UTF-8"' > /etc/default/locale

# Enable passwordless ssh authentication
RUN apt-get remove -y openssh-client
RUN apt-get update
RUN apt-get install -y openssh-server
#RUN mkdir /var/run/sshd
#RUN echo 'root:screencast' | chpasswd
#RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
#RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

#ENV NOTVISIBLE "in users profile"
#RUN echo "export VISIBLE=now" >> /etc/profile
RUN rm -f /etc/ssh/ssh_host_dsa_key /etc/ssh/ssh_host_rsa_key /root/.ssh/id_rsa
RUN ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key
RUN ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key
RUN ssh-keygen -q -N "" -t rsa -f /root/.ssh/id_rsa
RUN cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys


RUN service ssh start

#RUN mkdir /root/.ssh
#RUN chmod 777 /root/.ssh
#ADD authorized_keys /root/.ssh
#RUN chmod 600 /root/.ssh/authorized_keys

ADD ssh_config /root/.ssh/config
RUN chmod 600 /root/.ssh/config
RUN chown root:root /root/.ssh/config

RUN sed  -i "/^[^#]*UsePAM/ s/.*/#&/"  /etc/ssh/sshd_config
RUN echo "UsePAM no" >> /etc/ssh/sshd_config
RUN echo "Port 2122" >> /etc/ssh/sshd_config

# Add files.
ADD .bashrc /root/.bashrc

# Install Java 8
RUN cd opt && wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/8u72-b15/jdk-8u72-linux-x64.tar.gz" &&\
   tar xzf jdk-8u72-linux-x64.tar.gz && rm -rf jdk-8u72-linux-x64.tar.gz

ENV JAVA_HOME /opt/jdk1.8.0_72
ENV PATH $PATH:/opt/jdk1.8.0_72/bin:/opt/jdk1.8.0_72/jre/bin:/etc/alternatives:/var/lib/dpkg/alternatives

RUN echo 'export JAVA_HOME="/opt/jdk1.8.0_72"' >> ~/.bashrc && \
    echo 'export PATH="$PATH:/opt/jdk1.8.0_72/bin:/opt/jdk1.8.0_72/jre/bin"' >> ~/.bashrc && \
    bash ~/.bashrc && cd /opt/jdk1.8.0_72/ && update-alternatives --install /usr/bin/java java /opt/jdk1.8.0_72/bin/java 1
   
# Install Hadoop 2.7.1
RUN cd /opt && wget https://www.apache.org/dist/hadoop/core/hadoop-2.7.1/hadoop-2.7.1.tar.gz && \
    tar xzvf hadoop-2.7.1.tar.gz && rm ./hadoop-2.7.1.tar.gz &&  mv hadoop-2.7.1/ hadoop

ENV HADOOP_HOME /opt/hadoop

ADD core-site.xml /opt/hadoop/etc/hadoop/core-site.xml.template
RUN sed s/HOSTNAME/$HOSTNAME/ /opt/hadoop/etc/hadoop/core-site.xml.template > /opt/hadoop/etc/hadoop/core-site.xml

ADD mapred-site.xml /opt/hadoop/etc/hadoop/mapred-site.xml.template
RUN sed s/HOSTNAME/$HOSTNAME/ /opt/hadoop/etc/hadoop/mapred-site.xml.template > /opt/hadoop/etc/hadoop/mapred-site.xml

ADD hdfs-site.xml /opt/hadoop/etc/hadoop
ADD yarn-site.xml /opt/hadoop/etc/hadoop/yarn-site.xml.template
RUN sed s/HOSTNAME/$HOSTNAME/ /opt/hadoop/etc/hadoop/yarn-site.xml.template > /opt/hadoop/etc/hadoop/yarn-site.xml

ADD slaves /opt/hadoop/etc/hadoop

# Install Spark 1.6.0
RUN cd /opt && wget http://apache.javapipe.com/spark/spark-1.6.0/spark-1.6.0-bin-hadoop2.6.tgz 
RUN tar xzvf /opt/spark-1.6.0-bin-hadoop2.6.tgz
RUN rm  /opt/spark-1.6.0-bin-hadoop2.6.tgz

#Install Anaconda 3.14.1
ENV CONDA_DIR /opt/conda
ENV PATH $CONDA_DIR/bin:$PATH

RUN cd /opt && \
    mkdir -p $CONDA_DIR && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda3-3.9.1-Linux-x86_64.sh && \
    echo "6c6b44acdd0bc4229377ee10d52c8ac6160c336d9cdd669db7371aa9344e1ac3 *Miniconda3-3.9.1-Linux-x86_64.sh" | sha256sum -c - && \
    /bin/bash Miniconda3-3.9.1-Linux-x86_64.sh -f -b -p $CONDA_DIR && \
    rm Miniconda3-3.9.1-Linux-x86_64.sh && \
    $CONDA_DIR/bin/conda install --yes conda==3.14.1

# Install Jupyter notebook 
RUN $CONDA_DIR/bin/conda install --yes \
    'notebook=4.1*' \
    terminado \
    && $CONDA_DIR/bin/conda clean -yt

# Scala Spark kernel (build and cleanup)
RUN cd /tmp && \
    echo deb http://dl.bintray.com/sbt/debian / > /etc/apt/sources.list.d/sbt.list && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv 99E82A75642AC823 && \
    apt-get update && \
    git clone https://github.com/apache/incubator-toree.git && \
    apt-get install -yq --force-yes --no-install-recommends sbt && \
    cd incubator-toree && \
    git checkout 846292233c && \
    make dist SHELL=/bin/bash && \
    mv dist/toree-kernel /opt/toree-kernel && \
    chmod +x /opt/toree-kernel && \
    rm -rf ~/.ivy2 && \
    rm -rf ~/.sbt && \
    rm -rf /tmp/incubator-toree && \
    apt-get remove -y sbt && \
    apt-get clean
 
# Spark and Mesos pointers
ENV SPARK_HOME /opt/spark-1.6.0-bin-hadoop2.6
ENV R_LIBS_USER $SPARK_HOME/R/lib
ENV PYTHONPATH $SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.8.2.1-src.zip
#ENV MESOS_NATIVE_LIBRARY /usr/local/lib/libmesos.so
ENV SPARK_OPTS --driver-java-options=-Xms1024M --driver-java-options=-Xmx4096M --driver-java-options=-Dlog4j.logLevel=info

# R pre-requisites
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    fonts-dejavu \
    gfortran \
    gcc && apt-get clean
    
# Install Python 3 packages
RUN $CONDA_DIR/bin/conda install --yes \
    'ipywidgets=4.0*' \
    'pandas=0.17*' \
    'matplotlib=1.4*' \
    'scipy=0.16*' \
    'seaborn=0.6*' \
    'scikit-learn=0.16*' 
    
RUN $CONDA_DIR/bin/conda clean -yt

# Install Python 2 packages
RUN $CONDA_DIR/bin/conda create -p $CONDA_DIR/envs/python2 python=2.7 \
    'ipython=4.0*' \
    'ipywidgets=4.0*' \
    'pandas=0.17*' \
    'matplotlib=1.4*' \
    'scipy=0.16*' \
    'seaborn=0.6*' \
    'scikit-learn=0.16*' \
    pyzmq \
    && $CONDA_DIR/bin/conda clean -yt

# R packages
RUN $CONDA_DIR/bin/conda config --add channels r
RUN $CONDA_DIR/bin/conda install --yes \
    'r-base=3.2*' \
    'r-irkernel=0.5*' \
    'r-ggplot2=1.0*' \
    'r-rcurl=1.95*' && $CONDA_DIR/bin/conda clean -yt

# Scala Spark kernel spec
RUN mkdir -p /opt/conda/share/jupyter/kernels/scala
COPY kernel.json /opt/conda/share/jupyter/kernels/scala/

# Activate Python2 kernel
RUN bash -c '. activate python2 && \
    python -m ipykernel.kernelspec --prefix=$CONDA_DIR && \
    . deactivate'
    
RUN apt-get install jq

# Set PYSPARK_HOME in the python2 spec
RUN jq --arg v "$CONDA_DIR/envs/python2/bin/python" \
        '.["env"]["PYSPARK_PYTHON"]=$v' \
        $CONDA_DIR/share/jupyter/kernels/python2/kernel.json > /tmp/kernel.json && \
        mv /tmp/kernel.json $CONDA_DIR/share/jupyter/kernels/python2/kernel.json


EXPOSE 22 7077 8020 8030 8031 8032 8033 8040 8042 8080 8088 8888 9200 9300 10000 50010 50020 50060 50070 50075 50090
ADD entrypoint.sh /opt/entrypoint.sh

RUN chmod 777 /opt/entrypoint.sh

RUN mv spark-1.6.0-bin-hadoop2.6 /opt/

ADD spark-defaults.conf /opt/spark-1.6.0-bin-hadoop2.6/conf/spark-defaults.conf.template
RUN sed s/HOSTNAME/$HOSTNAME/ /opt/spark-1.6.0-bin-hadoop2.6/conf/spark-defaults.conf.template > /opt/spark-1.6.0-bin-hadoop2.6/conf/spark-defaults.conf

ADD spark-env.sh /opt/spark-1.6.0-bin-hadoop2.6/conf/spark-env.sh

ENTRYPOINT ["/opt/entrypoint.sh"]
