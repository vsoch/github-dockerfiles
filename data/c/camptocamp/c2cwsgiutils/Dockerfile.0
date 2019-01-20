FROM camptocamp/python-gis:3.6-ubuntu18.04
LABEL maintainer "info@camptocamp.org"

RUN apt update && \
    DEBIAN_FRONTEND=noninteractive apt install --yes --no-install-recommends \
        libpq-dev \
        libgeos-dev \
        libproj-dev \
        libjpeg-dev \
        postgresql-client-10 \
        git \
        graphviz-dev \
        graphviz \
        net-tools \
        iputils-ping \
        tree \
        screen \
        vim \
        vim-editorconfig \
        vim-addon-manager && \
    apt-get clean && \
    rm -r /var/lib/apt/lists/* && \
    vim-addon-manager --system-wide install editorconfig && \
    echo 'set hlsearch  " Highlight search' > /etc/vim/vimrc.local && \
    echo 'set wildmode=list:longest  " Completion menu' >> /etc/vim/vimrc.local && \
    echo 'set term=xterm-256color  " Make home and end working' >> /etc/vim/vimrc.local
COPY requirements.txt docker-requirements-light.txt docker-requirements.txt /opt/c2cwsgiutils/
RUN pip install --no-cache-dir -r /opt/c2cwsgiutils/requirements.txt -r /opt/c2cwsgiutils/docker-requirements-light.txt -r /opt/c2cwsgiutils/docker-requirements.txt

COPY . /opt/c2cwsgiutils/
RUN flake8 /opt/c2cwsgiutils && \
    echo "from pickle import *" > /usr/lib/python3.6/cPickle.py && \
    pip3 install --disable-pip-version-check --no-cache-dir -e /opt/c2cwsgiutils && \
    (cd /opt/c2cwsgiutils/ && pytest -vv --cov=c2cwsgiutils --color=yes tests && rm -r tests) && \
    python3 -m compileall -q && \
    python3 -m compileall -q /opt/c2cwsgiutils

ENV TERM=linux \
    LANG=C.UTF-8 \
    LOG_TYPE=console \
    LOG_HOST=localhost \
    LOG_PORT=514 \
    SQL_LOG_LEVEL=WARN \
    GUNICORN_LOG_LEVEL=WARN \
    OTHER_LOG_LEVEL=WARN \
    DEVELOPMENT=0

CMD ["c2cwsgiutils_run"]
