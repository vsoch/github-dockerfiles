FROM nginx:1.12.2

ARG environment

RUN rm /etc/nginx/conf.d/default.conf
RUN rm /etc/nginx/nginx.conf

COPY nginx.conf /etc/nginx/nginx.conf
COPY conf.d /etc/nginx/conf.d
COPY sites-available/${environment}/* /etc/nginx/sites-available/
COPY sites-available/*.conf /etc/nginx/sites-available/
COPY config /etc/nginx/config

RUN mkdir /etc/nginx/sites-enabled
RUN ln -s /etc/nginx/sites-available/* /etc/nginx/sites-enabled/
