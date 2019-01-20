# Create builder image
FROM node:10.9.0-stretch as builder
WORKDIR /tmp/app

# Download dependencies
COPY package.json ./
RUN npm install

# Build app
COPY src src
COPY .angular-cli.json tsconfig.json tslint.json ./
RUN npm run build -- --env=prod --verbose
RUN ls -alh dist

# Create nginx image
FROM nginx:1.15.2-alpine
COPY --from=builder /tmp/app/dist /usr/share/nginx/html
RUN echo 'server { listen 80 default_server; server_name _; location / { root /usr/share/nginx/html; try_files $uri $uri/ /index.html =404; } }' > /etc/nginx/conf.d/default.conf
