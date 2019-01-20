FROM node:alpine

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY packages/graphql-mock-schema /usr/src/app

ENV PORT 3000

EXPOSE 3000

CMD ["node", "bundle.server.js"]