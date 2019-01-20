FROM camptocamp/odoo-project:10.0-2.3.0
MAINTAINER Camptocamp

# Install additional debian packages if needed
# RUN set -x; \
#          apt-get update \
#          && apt-get install -y --no-install-recommends \
#          parallel \
#          && apt-get clean \
#          && rm -rf /var/lib/apt/lists/*

# Install additional python packages if needed
COPY ./*requirements.txt /opt/odoo/
RUN cd /opt/odoo && find . -maxdepth 1 -name "*requirements.txt" ! -name src_requirements.txt ! -name base_requirements.txt -exec pip install -r {} \;

ENV ADDONS_PATH="/opt/odoo/external-src/server-tools, \
  /opt/odoo/external-src/web, \
  /opt/odoo/src/addons, \
  /opt/odoo/local-src," \
  LIMIT_TIME_CPU=86400 \
  LIMIT_TIME_REAL=86400 \
  LIMIT_MEMORY_SOFT=1342177280 \
  LIMIT_MEMORY_HARD=1610612736
