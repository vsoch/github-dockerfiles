FROM unit9/python-uwsgi:latest

MAINTAINER Artiom Vasiliev <artiom@unit9.com>

RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && rm -rf /var/cache/apt /var/lib/apt/lists/*

# Download and install arachni
RUN cd /tmp \
    && curl -LO https://github.com/Arachni/arachni/releases/download/v1.5.1/arachni-1.5.1-0.5.12-linux-x86_64.tar.gz \
    && tar xzvf arachni-1.5.1-0.5.12-linux-x86_64.tar.gz \
    && sed -i "s/marshal/txt/" arachni-1.5.1-0.5.12/system/gems/gems/arachni-1.5.1/components/plugins/email_notify.rb \
    && mv arachni-1.5.1-0.5.12 /opt/scanner \
    && chmod -R 777 /opt/scanner/system/arachni-ui-web/config/component_cache \
        /opt/scanner/system/arachni-ui-web/db \
        /opt/scanner/system/arachni-ui-web/tmp \
        /opt/scanner/system/logs \
        /opt/scanner/system/home

# Download setup web ui
RUN git clone https://github.com/unit9/arachni-ui /app \
    && pip install -r /app/requirements.txt

WORKDIR /app

COPY celery.run /etc/service/celery/run
COPY web.run /etc/service/web/run

ENV SCANNER_PATH=/opt/scanner/bin/arachni \
    SCANNER_REPORT_PATH=/tmp \
    PORT=5000
    
EXPOSE 5000
