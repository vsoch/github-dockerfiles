FROM nginx
ADD ops/nginx.conf /etc/nginx/conf.d/default.conf
RUN rm /usr/share/nginx/html/*
ADD ops/start_container /
ADD index.html /usr/share/nginx/html/index.html
ADD favicon.png /usr/share/nginx/html/
ADD dist /usr/share/nginx/html
CMD /start_container
