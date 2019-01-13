# apache-php-memcached

Todos as imagens sao baseadas na CentOS 6.8.
Para criar as imagens, executar os comandos abaixo:

# memcached
cd memcached
docker build -t centos6_memcached:0.4 .

# apache com suporte a PHP
cd apache
docker build -t centos6_apache:0.5 .

# appserver 
servidor com app que coleta seus dados e envia para a memcached

cd appserver
docker build -t centos6_appserver:1.7 .


Para criar os containers executar os comandos abaixo apos a 
criacao das imagens

# memcached
docker run -d -p  11211:11211 --name centos_memcache -ti centos6_memcached

# apache com suporte a PHP
docker run -d -p 80:80 -p 22000:22 --link centos_memcache --name centos_apache -ti centos6_apache:0.5

# appserver
* criar diretorio para visualizacao de logs dos scripts
mkdir /tmp/applogs && chown :wheel /tmp/applogs && chmod 775 /tmp/applogs

* subit o container
docker run -d -p 22470:22 --link centos_memcache --name centos_appserver -v /tmp/applogs:/tmp/applogs centos6_appserver:1.7

* o container pode ser acessado via ssh com usuario monitor/monitor na porta 22470, este usuario possui sudo habilitado. para acessar use o comando:
ssh -p 22470 monitor@localhost

* e possivel consultar os logs de coleta de performance acessando o /tmp/applogs do host docker. La deve ter 2 arquivos: um para a coleta de cpu e outro para a de memoria.

* Para acessar o Monitor de utilizacao / estatisticas do memcached basta acessar a URL: http://localhost:80

