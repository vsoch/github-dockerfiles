FROM node:10-alpine

LABEL com.github.actions.name="GitHub Action for Framer"
LABEL com.github.actions.icon="package"
LABEL com.github.actions.color="gray-dark"

RUN apk update && apk add jq && rm -rf /var/cache/apk/*

COPY "entrypoint.sh" "/entrypoint.sh"
ENTRYPOINT ["/entrypoint.sh"]
