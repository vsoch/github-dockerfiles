FROM clmntlxndr/ruby-over-node
RUN apk add --no-cache --virtual .gems-builddeps build-base postgresql-dev sqlite-dev libxml2-dev libxslt-dev
RUN gem install pg:'~>0.20' nokogiri:'~>1.8' sqlite3 rails:'~>5.2' rails-i18n:'~> 5.0.0' image_processing:'~> 1.2' bindex:'~>0.5' msgpack:'~>1.2' bootsnap:'~>1.3' byebug:'~>10.0' puma:'~>3.12' bcrypt:'~>3.1' unf_ext:'~>0.0.7' --no-ri --no-rdoc
RUN apk add --no-cache --virtual .usual-gems-rundeps tzdata imagemagick libpq sqlite-libs git
RUN mkdir /app && cd /app
WORKDIR /app
COPY Dockerfile Gemfile* /app/
COPY Dockerfile vendor* /app/vendor/
RUN rm /app/Dockerfile /app/vendor/Dockerfile
RUN bundle install ; exit 0
RUN apk del .gems-builddeps
COPY Dockerfile package.json* yarn.lock* node_modules* /app/
RUN yarn install ; exit 0
ENTRYPOINT ["rails"]
EXPOSE 3000
CMD ["server","-b","0.0.0.0","-p","3000"]
