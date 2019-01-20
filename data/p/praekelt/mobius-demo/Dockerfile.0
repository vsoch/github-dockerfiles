FROM ubuntu:17.10
WORKDIR /var/app/
RUN apt-get update
RUN apt-get install -y python-pip libpq-dev python-virtualenv \
libjpeg-dev zlib1g-dev git-core libxslt1-dev redis-server rabbitmq-server nginx \
supervisor varnish memcached net-tools npm wget vim
COPY ./requirements /var/app/requirements/
RUN pip install --no-cache-dir -r requirements/requirements.txt
RUN virtualenv /var/twisted-ve
RUN /var/twisted-ve/bin/pip install --no-cache-dir --upgrade django-ultracache-twisted
COPY . /var/app/
COPY ./docker/etc /etc/
RUN python manage.py migrate --noinput
RUN python manage.py collectstatic --noinput
RUN python manage.py generate_vcl > /var/app/project/generated.vcl
RUN python manage.py demo_content
RUN wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | bash
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN source ~/.nvm/nvm.sh; \
    nvm install; \
    nvm use; \
    npm install; \
    npm run build;
EXPOSE 6081
ENTRYPOINT ["docker/services.sh"]
