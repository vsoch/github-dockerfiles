FROM fluent/fluentd:v0.12-debian
MAINTAINER Timothy Hnat twhnat@memphis.edu

RUN ["gem", "install", "fluent-plugin-elasticsearch", "--no-rdoc", "--no-ri", "--version", "1.9.2"]

COPY conf/* /fluentd/etc/
