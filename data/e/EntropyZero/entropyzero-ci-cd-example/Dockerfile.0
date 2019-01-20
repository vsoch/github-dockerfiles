FROM phusion/passenger-ruby21:0.9.20
MAINTAINER "EntropyZero Consulting, LLC (Dev Team)"

# === 1 ===
# Prepare for packages
RUN apt-get update --assume-yes && apt-get install --assume-yes build-essential nano unzip alien libaio1 ca-certificates mysql-client sudo python-dev

# For a JS runtime
# http://nodejs.org/
RUN apt-get install --assume-yes nodejs

# For Nokogiri gem
# http://www.nokogiri.org/tutorials/installing_nokogiri.html#ubuntu___debian
RUN apt-get install --assume-yes libxml2-dev libxslt1-dev

# Install AWS Commandline
RUN apt-get install --assume-yes groff
RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip" && unzip awscli-bundle.zip && sudo ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && rm awscli-bundle.zip && rm -rf ./awscli-bundle

# install AWSLOGS
RUN curl https://s3.amazonaws.com/aws-cloudwatch/downloads/latest/awslogs-agent-setup.py -o awslogs-agent-setup.py
ADD etc/configs/awslogs.conf /root/awslogs.conf
RUN python ./awslogs-agent-setup.py -n -r us-east-1 -c /root/awslogs.conf
RUN update-rc.d -f awslogs remove
RUN rm /root/awslogs.conf
ADD etc/configs/example-log /etc/logrotate.d/example-log

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# === 2 ===

# Set correct environment variables.
ENV HOME /root

# Use baseimage-docker's init process.
CMD ["/sbin/my_init"]

# === 3 ====

# By default Nginx clears all environment variables (except TZ). Tell Nginx to
# preserve these variables. See nginx-env.conf.
COPY etc/configs/nginx-env.conf /etc/nginx/main.d/rails-env.conf

# Expose Nginx HTTP service
EXPOSE 80

# === 3.5 ===

ENV PASSENGER_APP_ENV=production
ENV RAILS_ENV=${PASSENGER_APP_ENV}

ENV RUN_NGINX=true
ENV RUN_CREATE=true
ENV RUN_MIGRATE=true
ENV RUN_SEEDS=true
ENV RUN_WAIT=false
ENV RUN_COPYCONFIG=false

ENV ENABLE_LOGRAGE=false
ENV S3_CONFIG_BUCKET="example/development"
ENV S3_CONFIG_FILE="web"

# === 4 ===

# Our application should be placed inside /home/app. The image has an app user
# with UID 9999 and home directory /home/app. Our application is supposed to run
# as this user. Even though Docker itself provides some isolation from the host
# OS, running applications without root privileges is good security practice.
RUN mkdir -p /home/app/myapp
WORKDIR /home/app/myapp

# Run Bundle in a cache efficient way. Before copying the whole app, copy just
# the Gemfile and Gemfile.lock into the tmp directory and ran bundle install
# from there. If neither file changed, both instructions are cached. Because
# they are cached, subsequent commands—like the bundle install one—remain
# eligible for using the cache. Why? How? See ...
# http://ilikestuffblog.com/2014/01/06/how-to-skip-bundle-install-when-deploying-a-rails-app-to-docker/
COPY Gemfile /home/app/myapp/
COPY Gemfile.lock /home/app/myapp/
RUN bundle install --deployment --without test development doc

# Same caching process for assets
ADD app/assets /home/app/myapp/app/assets
ADD config /home/app/myapp/config
ADD vendor/assets /home/app/myapp/vendor/assets
ADD Rakefile /home/app/myapp/Rakefile
RUN bundle exec rake assets:precompile

# Adding bootstrapping scripts for container startup
RUN mkdir -p /etc/my_init.d
ADD etc/scripts /etc/my_init.d
RUN chmod +x /etc/my_init.d/*.sh

# === 5 ===

# Adding our web app to the image ... only after bundling do we copy the rest of
# the app into the image.
COPY . /home/app/myapp
#COPY etc/configs/database.yml /home/app/myapp/config/database.yml
RUN mkdir /home/app/myapp/private
RUN chown -R app:app /home/app/myapp

# === 6 ===

# Remove the default site. Add a virtual host entry to Nginx which describes
# where our app is, and Passenger will take care of the rest. See nginx.conf.
RUN rm /etc/nginx/sites-enabled/default
COPY etc/configs/nginx.conf /etc/nginx/sites-enabled/myapp.conf
