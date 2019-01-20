FROM eu.gcr.io/sanity-cloud/node:7.6

ARG NPMRC

# Set up environment
WORKDIR /srv/cavs-www
RUN useradd --home /srv/cavs-www --shell /bin/false nodejs

# Install app dependencies (pre-source copy in order to cache dependencies)
COPY package.json .
RUN echo "$NPMRC" > ~/.npmrc && \
  npm install && \
  rm ~/.npmrc

# Set node environment
ENV NODE_ENV=production

# Prepare app
COPY . .
RUN chown -R nodejs /srv/cavs-www \
  && npm run build

# Release hash (usually git commit) used for error reporting and such
ARG RELEASE_HASH
ENV SENTRY_RELEASE=$RELEASE_HASH

# Run application
EXPOSE 3000
CMD ["gosu", "nodejs", "node", "build/server.js"]
