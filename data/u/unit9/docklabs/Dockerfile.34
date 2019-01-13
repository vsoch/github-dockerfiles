FROM unit9/python-uwsgi:latest
MAINTAINER Kamil Cholewiński <kamil.cholewinski@unit9.com>

# Install NodeJS
RUN curl https://deb.nodesource.com/setup_6.x -o /tmp/node.sh \
    && bash /tmp/node.sh \
    && apt-get install --yes --no-install-recommends \
            nodejs \
            git-core \
            ruby \
            ruby-dev \
            ruby-ffi \
    && rm -rf /var/cache/apt /var/lib/apt/lists

# Frontend development tools
RUN gem install compass scss_lint
RUN npm install --global gulp-cli bower
