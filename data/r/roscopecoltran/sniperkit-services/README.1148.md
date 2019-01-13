[![](https://images.microbadger.com/badges/image/deepcortex/python3-hdfs.svg)](https://microbadger.com/images/deepcortex/python3-hdfs "Get your own image badge on microbadger.com")
[![](https://images.microbadger.com/badges/commit/deepcortex/python3-hdfs.svg)](https://microbadger.com/images/deepcortex/python3-hdfs "Get your own commit badge on microbadger.com")

# python3-hdfs
Docker image providing ZeroMQ + JZMQ + Scala + Python 3.5.2 environment + ML Libs + HDFS Python Client + Hadoop

numpy, scipy, scikit-learn, pandas, tensorflow, h5py, keras

FROM deepcortex/scala-python3-ml:latest

# Install HDFS
```
wget "http://mirrors.ocf.berkeley.edu/apache/hadoop/common/hadoop-2.6.5/hadoop-2.6.5.tar.gz"
tar xvfz hadoop-2.6.5.tar.gz
mv hadoop-2.6.5 /usr/local/hadoop
ln -s /usr/local/hadoop /opt/hadoop
```

# Modify hadoop files  

/opt/hadoop/etc/hadoop/hdfs-site.xml

```
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
</configuration>
```

/opt/hadoop/etc/hadoop/core-site.xml

```
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://10.200.10.1:9000</value>
    </property>
</configuration>
```

/opt/hadoop/etc/hadoop/yarn-site.xml

```
<configuration>
    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>
</configuration>
```

/opt/hadoop/etc/hadoop/mapred-site.xml

```
<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
</configuration>
```

# Install Ignite

```
wget "http://download.nextag.com/apache//ignite/2.0.0/apache-ignite-hadoop-2.0.0-bin.zip"
unzip apache-ignite-hadoop-2.0.0-bin.zip
mv apache-ignite-hadoop-2.0.0-bin /opt
ln -s /opt/apache-ignite-hadoop-2.0.0-bin /opt/ignite
```

# Add paths to ~/.bash_profile

```
export IGNITE_HOME=/opt/ignite
export PATH=$PATH:$IGNITE_HOME/bin
export HADOOP_HOME=/opt/hadoop
export PATH=$PATH:$HADOOP_HOME/bin
```

# Start HDFS

```
/opt/hadoop/sbin/start-dfs.sh
/opt/hadoop/sbin/start-yarn.sh
```

# Start Ignite 

```
/opt/ignite/bin/ignite.sh cortex-prototypes/cortex-ignite/src/main/configs/igfs-hadoop-fs-cache/igfs-hadoop-fs-cache-config.xml
```

# Make localhost alias

```
sudo ifconfig lo0 alias 10.200.10.1/24
```

# Start docker image 

```
make run
```

# To run HDFS commands in Docker

```
hdfs --config /etc/hadoop/conf/ dfs <command> <arguments>
```
