FROM jolicode/hhvm

RUN sudo apt-get update \
 && sudo apt-get install -y nginx

ADD . /root
RUN sudo chmod +x /root/start.sh

ADD hhvm.hdf /etc/hhvm/server.hdf
ADD nginx.conf /etc/nginx/sites-available/hack.conf
RUN sudo ln -s /etc/nginx/sites-available/hack.conf /etc/nginx/sites-enabled/hack.conf
RUN sudo nginx -t

RUN sudo chown -R www-data:www-data /root
WORKDIR /root

EXPOSE 8080

CMD ["sudo","/root/start.sh"]
