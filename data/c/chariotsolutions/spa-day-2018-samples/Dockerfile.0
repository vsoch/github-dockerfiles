FROM node:10

LABEL \
    org.label-schema.schema-version="rc1" \
    org.label-schema.name="spa-server" \
    org.label-schema.description="Chariot SPA Day demo server" \
    org.label-schema.vendor="Chariot Solutions" \
    org.label-schema.url="http://www.chariotsolutions.com/" \
    com.chariotsolutions.distribution-scope="private" \
    com.chariotsolutions.copyright="2018 ChariotSolutions" \
    com.chariotsolutions.license="All Rights Reserved" \
    com.chariotsolutions.blame="Jeffrey Labonski <jlabonski@chariotsolutions.com>"

EXPOSE 8000

# https://github.com/nodejs/docker-node/blob/master/docs/BestPractices.md#handling-kernel-signals
# https://github.com/krallin/tini
ENV TINI_VERSION v0.18.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini

RUN mkdir /node
RUN chown node.node /node
USER node
COPY --chown=node:node . /node

WORKDIR /node

# Since we may be moving from various flavors of linux or macos or Windows
# to the node image, copying node_modules blindly can fail as they may have
# C++ binaries.
#
# Pass --update-binary to reinstall or --build-from-source to recompile
RUN npm rebuild --update-binary

ENTRYPOINT [ "/tini", "-v", "--", "node", "/node/src/index.js" ]
