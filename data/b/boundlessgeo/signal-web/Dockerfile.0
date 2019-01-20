FROM nginx

RUN apt-get update -qq
RUN apt-get remove node
RUN apt-get install -y build-essential curl
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get install -y nodejs

RUN mkdir -p /web
COPY . /web
RUN rm -rf /web/node_modules/
WORKDIR /web
RUN npm install
RUN npm run build

COPY ./nginx-config/signal.conf /etc/nginx/conf.d/default.conf
# COPY ./nginx-config/signal-tls.conf /
RUN cp -r ./public/* /usr/share/nginx/html/

# COPY ./nginx-config/start.sh /
# COPY dhparams.pem /etc/ssl/private/
# CMD /start.sh
