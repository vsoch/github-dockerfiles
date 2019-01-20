# a minimal Nginx container 
FROM nginx:1.13.1-alpine

COPY ./nginx.conf  /etc/nginx/nginx.conf
CMD [ "nginx", "-g", "daemon off;" ]
EXPOSE 8000 8443 8001
