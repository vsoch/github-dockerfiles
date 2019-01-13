FROM unit9/base:latest

MAINTAINER Kamil Cholewiński <kamil.cholewinski@unit9.com>
MAINTAINER Artiom Vasiliev <artiom@unit9.com>

# Install NodeJS & other stuff
RUN curl https://deb.nodesource.com/setup_7.x -o /tmp/node.sh \
    && bash /tmp/node.sh \
    && apt-get install --yes --no-install-recommends \
            git-core \
            nodejs \
            python-all-dev \
            python-pip \
            python-wheel \
            ruby \
            ruby-dev \
            ruby-ffi \
    && rm -rf /var/cache/apt /var/lib/apt/lists

RUN export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" \
    && export CLOUD_DEB="deb https://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" \
    && echo $CLOUD_DEB > /etc/apt/sources.list.d/google-cloud-sdk.list \
    && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg \
    | apt-key add - \
    && apt-get update \
    && apt-get install -y google-cloud-sdk \
    && rm -rf /var/cache/apt /var/lib/apt/lists

RUN pip install awscli

CMD ["/bin/bash"]
