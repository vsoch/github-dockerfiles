FROM cassandra:3.9
MAINTAINER Timothy Hnat twhnat@memphis.edu

COPY ["entrypoint.sh", "bootstrap.sh", "wait-for-it.sh", "cerebralcortex.cql", "/"]
RUN chmod +x /bootstrap.sh /entrypoint.sh /wait-for-it.sh

ENTRYPOINT ["/bootstrap.sh"]

CMD ["cassandra", "-f"]
