FROM buildpack-deps:xenial

# SYSTEM ######################################################################

RUN apt-get update \
    && apt-get upgrade -y --no-install-recommends \
    && apt-get install -y --no-install-recommends \
        apache2-utils \
        apt-utils \
        bsdmainutils \
        dnsutils \
        gettext  \
        htop \
        iputils-ping \
        jq \
        less \
        locales \
        nano \
        nginx \
        postgresql-client \
        pv \
        python-dev \
        python3.6-dev \
        screen \
        supervisor \
        tmux \
        vim-tiny \
    && rm -rf /var/lib/apt/lists/*

ENV DOCKER_PACKAGE_FILENAME=docker-ce_18.06.1~ce~3-0~ubuntu_amd64.deb
RUN wget -nv "https://download.docker.com/linux/ubuntu/dists/bionic/pool/stable/amd64/${DOCKER_PACKAGE_FILENAME}" \
    && apt-get update \
    && apt install -y --no-install-recommends "./${DOCKER_PACKAGE_FILENAME}" \
    && rm -rf /var/lib/apt/lists/* "${DOCKER_PACKAGE_FILENAME}"

ENV DOCKER_COMPOSE_VERSION=1.22.0
RUN wget -nv -O /usr/local/bin/docker-compose "https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-$(uname -s)-$(uname -m)"
RUN chmod +x /usr/local/bin/docker-compose
RUN wget -nv -O /etc/bash_completion.d/docker-compose "https://raw.githubusercontent.com/docker/compose/${DOCKER_COMPOSE_VERSION}/contrib/completion/bash/docker-compose"

ENV DOCKERIZE_VERSION=0.5.0
RUN wget -nv -O - "https://github.com/jwilder/dockerize/releases/download/v${DOCKERIZE_VERSION}/dockerize-linux-amd64-v${DOCKERIZE_VERSION}.tar.gz" | tar -xz -C /usr/local/bin/ -f -

ENV NODE_VERSION=8.12.0
RUN wget -nv -O - "https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.xz" | tar -Jx -C /opt/ -f -
RUN ln -s "/opt/node-v${NODE_VERSION}-linux-x64/bin/node" /usr/local/bin/
RUN ln -s "/opt/node-v${NODE_VERSION}-linux-x64/bin/npm" /usr/local/bin/

ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_SRC=/opt
ENV PYTHON_VERSION=python3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONHASHSEED=random
ENV PYTHONWARNINGS=ignore

ENV PYTHON_PIP_VERSION=9.0.1
RUN wget -nv -O - https://bootstrap.pypa.io/get-pip.py | "${PYTHON_VERSION}" - "pip==${PYTHON_PIP_VERSION}"

ENV TINI_VERSION=0.16.1
RUN wget -nv -O /usr/local/bin/tini "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini-static"
RUN chmod +x /usr/local/bin/tini

RUN locale-gen en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US:en
ENV LC_ALL=en_US.UTF-8

# PROJECT #####################################################################

ENV PROJECT_DIR=/opt/project_template
WORKDIR "${PROJECT_DIR}"

COPY package.json package-lock.json "${PROJECT_DIR}/"
RUN npm ci --unsafe-perm && rm -rf /root/.npm
RUN md5sum package.json > package.json.md5
ENV PATH="${PROJECT_DIR}/node_modules/.bin:$PATH"

COPY bower.json "${PROJECT_DIR}"
RUN bower install --allow-root && rm -rf /root/.cache/bower
RUN md5sum bower.json > bower.json.md5

COPY requirements.txt "${PROJECT_DIR}"
RUN pip install --no-cache-dir -r requirements.txt
RUN md5sum requirements.txt > requirements.txt.md5

ENTRYPOINT ["tini", "--", "entrypoint.sh"]
CMD ["bash.sh"]

COPY . "${PROJECT_DIR}"

RUN npm run build

# RUN entrypoint.sh compile-sass.sh  # Must come before collectstatic
RUN entrypoint.sh manage.py collectstatic --noinput --verbosity=0
# RUN entrypoint.sh manage.py compress --verbosity=0  # Only needed when there is no shared persistent volume
