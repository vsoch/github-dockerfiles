FROM postgres:9.5

RUN apt-get update \
      && apt-get install -y --no-install-recommends \
      && rm -rf /var/lib/apt/lists/*

ADD create_db.sh /docker-entrypoint-initdb.d/create_db.sh
