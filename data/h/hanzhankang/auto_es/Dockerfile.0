#
# Elasticsearch Dockerfile
#
# https://github.com/dockerfile/elasticsearch
#

# 设置继承自java:oracle-java8 镜像
FROM docker.sankuai.com/jdk-8u71-linux-x64

# 下面是一些创建者的基本信息
MAINTAINER hanzhankang (hanzhankang@gmail.com)


# 设置环境变量，所有操作都是非交互式的
ENV DEBIAN_FRONTEND noninteractive

USER daily

# 设置下面操作时的工作目录
WORKDIR /opt

# 将本机中文件复制到docker镜像中，一般用于替换或者增加镜像中的文件
COPY . /opt

RUN rm -rf /opt/Dockerfile


# Expose ports.
#   - 9200: HTTP
#   - 9300: transport
EXPOSE {es_tcp_port}
EXPOSE {es_http_port}

# Define default command.
CMD ["/opt/{es_name}/bin/elasticsearch"]