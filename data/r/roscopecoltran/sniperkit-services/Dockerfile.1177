FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf
ADD nginx.conf /etc/nginx/conf.d/sps.conf

EXPOSE 80