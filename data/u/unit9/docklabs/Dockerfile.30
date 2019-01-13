FROM unit9/python-uwsgi:latest
MAINTAINER Kamil Cholewiński <kamil.cholewinski@unit9.com>

# Add NodeJS
RUN curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key \
    | apt-key add - \
    && echo "deb https://deb.nodesource.com/node_4.x jessie main" \
    > /etc/apt/sources.list.d/nodesource.list \
    && apt-get update \
    && apt-get install --yes --no-install-recommends \
            git-core \
            nodejs \
            ruby \
            ruby-dev \
            ruby-ffi \
    && rm -rf /var/cache/apt /var/lib/apt/lists

# Frontend development tools
RUN gem install compass scss_lint
RUN npm install --global gulp-cli bower
