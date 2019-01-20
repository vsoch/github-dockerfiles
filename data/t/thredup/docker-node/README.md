# docker-node

Base and builder images for Node.js® applications.

## Usage

### Multi-stage builds

```docker
FROM thredup/node:8.4.0-builder as builder

FROM thredup/node:8.4.0

ARG NODE_ENV=production
ENV NODE_ENV=${NODE_ENV}

COPY --from=builder /app/node_modules/ ./node_modules
COPY --from=builder /app/dist/ ./dist
COPY package.json /app/

CMD ["node", "dist/index.js"]
```

## Build Arguments

* `NODE_ENV` - Default: `production`

* `NPM_TOKEN` - Set this if your app must install private modules.

* `NPM_LOG_LEVEL` - See the [npm docs](https://docs.npmjs.com/misc/config#loglevel) for possible values. Default: `error`

## Custom app build steps

Your app can provide an optional `./scripts/build.sh`, which will be run by the builder. This is where you would run a babel or webpack build step.

The script must install any development dependencies needed to run the build. After running the build, the script should remove development dependencies to avoid deploying those to production.

### Example `./scripts/build.sh`

```bash
#!/usr/bin/env sh
set -e

# Temporarily install dev dependencies
if [ "${NODE_ENV}" = "production" ]
then
  npm install -s --only=dev
fi

# Build
npm run -s clean
npm run -s build

# Remove the dev dependencies
if [ "${NODE_ENV}" = "production" ]
then
  npm prune
fi
```