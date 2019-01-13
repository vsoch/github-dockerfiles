#
# NSQ Dockerfile
#
# https://github.com/dockerfile/nsq
#

# Pull base image.
FROM dockerfile/ubuntu

# Install NSQ.
RUN \
  mkdir -p /tmp/nsq && \
  wget https://s3.amazonaws.com/bitly-downloads/nsq/nsq-0.2.31.linux-amd64.go1.3.1.tar.gz -O - | tar -xvz --strip=1 -C /tmp/nsq && \
  mv /tmp/nsq/bin/* /usr/local/bin/ && \
  rm -rf /tmp/nsq

# Define working directory.
WORKDIR /data

# Define default command.
CMD ["bash"]

# Expose ports.
EXPOSE 4150
EXPOSE 4151
EXPOSE 4160
EXPOSE 4161
EXPOSE 4171
