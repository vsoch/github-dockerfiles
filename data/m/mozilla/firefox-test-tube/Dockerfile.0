FROM python:3.7-slim

EXPOSE 8000

RUN mkdir /app && \
    chown 10001:10001 /app && \
    groupadd --gid 10001 app && \
    useradd --no-create-home --uid 10001 --gid 10001 --home-dir /app app

# Install a few essentials and clean apt caches afterwards.
RUN mkdir -p \
        /usr/share/man/man1 \
        /usr/share/man/man2 \
        /usr/share/man/man3 \
        /usr/share/man/man4 \
        /usr/share/man/man5 \
        /usr/share/man/man6 \
        /usr/share/man/man7 \
        /usr/share/man/man8 && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        apt-transport-https build-essential curl git libpq-dev \
        postgresql-client libffi-dev  && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -U pip && \
    pip install -r requirements.txt
# TODO: --require-hashes

# Copy in the whole app after dependencies have been installed & cached.
COPY . /app

RUN chown -R 10001:10001 /app

# De-escalate from root privileges with app user.
USER 10001

ENTRYPOINT ["/bin/bash", "/app/bin/run"]
CMD ["dev"]
