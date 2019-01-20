FROM ubuntu:14.04
MAINTAINER Bluesoft Fire <devops@bluesoft.com.br>

ENV NGINX_VERSION 1.9.5

# Install dependencies
RUN apt-get -q update && \
    apt-get -q -y --no-install-recommends install \
        g++ \
        gcc \
        libpcre3-dev \
        libssl-dev \
        make \
        openssl \
        wget \
        zlib1g-dev && \
    rm -rf /var/lib/apt/lists/*

# Download nginx
RUN mkdir $HOME/src && \
    wget -nv http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz -O - | tar -xz -C $HOME/src

# Compile and install nginx
RUN cd $HOME/src/nginx-$NGINX_VERSION && \
    ./configure \
        --prefix=/usr/local/nginx \
        --user=www-data \
        --group=www-data \
        --build=nginx-bsh2-1 \
        --with-http_ssl_module \
        --with-http_v2_module \
        --with-http_gunzip_module && \
    make && \
    make install

# Generate ssl key and certificate
RUN mkdir /usr/local/nginx/conf/ssl && \
    openssl genrsa -out /usr/local/nginx/conf/ssl/h2-server.key 2048 && \
    openssl req -subj "/C=BR/ST=SP/L=São Paulo/O=Acme Inc/OU=DevOps" -new -key /usr/local/nginx/conf/ssl/h2-server.key -out /usr/local/nginx/conf/ssl/h2-server.csr && \
    openssl x509 -req -days 365 -in /usr/local/nginx/conf/ssl/h2-server.csr -signkey /usr/local/nginx/conf/ssl/h2-server.key -out /usr/local/nginx/conf/ssl/h2-server.crt

RUN rm -f /usr/local/nginx/conf/ssl/h2-server.csr && \
    chown -R www-data:www-data /usr/local/nginx/conf/ssl && \
    chmod 0400 /usr/local/nginx/conf/ssl/h2-server.key && \
    chmod 0444 /usr/local/nginx/conf/ssl/h2-server.crt

# Configure nginx
COPY nginx.conf.docker /usr/local/nginx/conf/nginx.conf
RUN mkdir -p /usr/local/nginx/html/

# Remove downloaded files
RUN rm -rf $HOME/src

# Expose ports
EXPOSE 80 443

# Run nginx
ENTRYPOINT [ "/usr/local/nginx/sbin/nginx", "-g", "daemon off;" ]
