FROM debian

MAINTAINER Tim Weckx <timw@dsoft-tech.com>

# install mono
RUN apt-get update \
        && apt-get install wget  -y --no-install-recommends \
        && echo "deb http://download.mono-project.com/repo/debian nightly main" > /etc/apt/sources.list.d/mono-xamarin.list \
        && wget -qO - http://download.mono-project.com/repo/xamarin.gpg | apt-key add - \
        && apt-get update \
        && apt-get install mono-runtime -y --no-install-recommends \
        && apt-get purge wget -y \
        && apt-get autoremove -y \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/* /var/tmp/*

# install runit and nginx mono-fastcgi-server4
ADD docker/service/ /etc/service/ 
ADD docker/config/runit/1 /etc/runit/1 
ADD docker/config/runit/1.d/cleanup-pids /etc/runit/1.d/cleanup-pids 
ADD docker/config/runit/2 /etc/runit/2 
ADD docker/runit_bootstrap /usr/sbin/runit_bootstrap 
 
RUN echo "deb http://download.mono-project.com/repo/debian wheezy-libjpeg62-compat main" | tee -a /etc/apt/sources.list.d/mono-xamarin.list \ 
     && apt-get update \ 
     && apt-get install runit nginx mono-fastcgi-server4 -y --no-install-recommends \ 
     && apt-get clean \ 
     && rm -rf /var/lib/apt/lists/* /var/tmp/* /tmp/* \ 
     && mkdir -p /etc/mono/registry /etc/mono/registry/LocalMachine \ 
     && find /etc/service/ -name run -exec chmod u+x {} \; \ 
     && chmod u+x /usr/sbin/runit_bootstrap; 
 
 
ADD docker/config/default /etc/nginx/sites-available/ 
ADD docker/config/fastcgi_params /etc/nginx/ 
ADD docker/runit_bootstrap /usr/sbin/runit_bootstrap 
EXPOSE 80 

# deploy webcode and start nginx
ADD Source/dsoft.ads/dsoft.ads.web /var/www
CMD ["/usr/sbin/runit_bootstrap"]
