FROM camptocamp/geomapfish_build:jenkins
LABEL maintainer='Camptocamp <info@camptocamp.com>'

COPY . /app/
RUN pip install --no-cache-dir --editable /app/

EXPOSE 80

ENTRYPOINT ["/app/gunicorn-run"]
