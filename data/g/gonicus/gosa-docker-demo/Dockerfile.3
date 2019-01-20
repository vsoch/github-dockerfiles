FROM debian:latest
MAINTAINER Cajus Pollmeier <pollmeier@gonicus.de>
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get remove rpcbind && \
    echo "dash dash/sh boolean false" | debconf-set-selections && \
    dpkg-reconfigure dash && \
    apt-get -y install python3-gunicorn python3-gevent python3-setproctitle python3-unidecode \
        python3-zope.interface python3-babel python3-openssl python3-sqlalchemy python3-lxml \
        python3-dnspython python3-cryptography python3-requests python3-tornado python3-decorator \
        python3-cups python3-crypto python3-lazy-object-proxy python3-psycopg2 python3-pil \
        python-virtualenv python3-virtualenv python3-pycurl python3-dateutil pylint3 && \
    virtualenv --python=python3 --system-site-packages /opt/gosa && \
    useradd --home-dir /opt/gosa --user-group --system gosa && \
    mkdir -p /var/run/gosa /etc/gosa /var/lib/gosa/workflows  && \
    chown -R gosa: /opt/gosa /var/run/gosa /var/lib/gosa

COPY packages/*deb /tmp/
COPY packages/*deb /tmp/
RUN dpkg -i /tmp/*.deb && rm -f /tmp/*.deb

WORKDIR /opt/gosa
COPY src src
RUN chown -R gosa: src && \
    [ -f src/plugins/gui/frontend/capture/Manifest.json ] || (echo "Please make sure you ran 'git submodule update --init --recursive'"; false)

# Install GOsa backend
USER gosa
COPY start.sh .
RUN source ~/bin/activate && \
    cd ~/src/common && \
    ./setup.py install && \
    cd ~/src/backend && \
    ./setup.py install && \
    cd ~/src/plugins/goto && \
    ./setup.py install && \
    cd ~/src/plugins/gui/frontend/gosa/plugins && \
    python2 make.py deploy && \
    cd ~/src/plugins/gui/frontend/gosa && \
    python2 generate.py build && \
    cd ~/src/plugins/gui && \
    ./setup.py install && \
    rm -rf ~/src

ENTRYPOINT /opt/gosa/start.sh
