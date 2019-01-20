FROM ruby:2.3.1

RUN wget -O - https://nodejs.org/dist/v6.10.0/node-v6.10.0-linux-x64.tar.xz | tar Jx --strip=1 -C /usr/local

WORKDIR /app

RUN npm install -g raml-1-parser # for validation
RUN npm install -g raml2obj      # to use consistency helpers https://github.com/raml2html/raml2obj/blob/develop/consistency-helpers.js

ADD Gemfile /app/Gemfile
ADD Gemfile.lock /app/Gemfile.lock
RUN bundle install

ENV NODE_PATH=/usr/local/lib/node_modules

CMD ./scripts/server
