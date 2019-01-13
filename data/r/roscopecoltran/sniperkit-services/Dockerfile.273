FROM tijsg/nginx-with-nano-apacheutils
COPY ./config/nginx.conf /etc/nginx/nginx.conf
COPY ./config/htpasswd /etc/nginx/.htpasswd
RUN mkdir /var/www
RUN mkdir /var/www/html
RUN touch /var/www/html/index.html