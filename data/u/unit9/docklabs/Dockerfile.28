FROM unit9/base:latest

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ruby \
        ruby-dev \
        build-essential \
    && gem install fluentd fluent-plugin-loggly --no-ri --no-rdoc \
    && apt-get remove --purge -y build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/cache/apt /var/lib/apt/lists/*

COPY "fluentd.run" "/etc/service/fluentd/run"

EXPOSE 5140/udp
