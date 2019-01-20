FROM cassandra:3.11

RUN apt-get update && \
	apt-get install -y curl lsof gettext netcat \
	&& rm -rf /var/lib/apt/lists/*

COPY src /home/cassandra
RUN mv /docker-entrypoint.sh /home/cassandra && \
    chown -R cassandra /home/cassandra

USER cassandra
ENTRYPOINT ["/home/cassandra/bootstrap.sh"]

