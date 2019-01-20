== README

This README would normally document whatever steps are necessary to get the
application up and running.

Things you may want to cover:

* Ruby version

* System dependencies

* Configuration

* Database creation

* Database initialization

* How to run the test suite

* Services (job queues, cache servers, search engines, etc.)

* Deployment instructions

* ...


Please feel free to use a different markup language if you do not plan to run
<tt>rake doc:app</tt>.
livreiro
==========

[![Build Status](https://travis-ci.org/webgoal/livreiro.svg?branch=master)](https://travis-ci.org/webgoal/livreiro)
[![Code Climate](https://codeclimate.com/github/webgoal/livreiro/badges/gpa.svg)](https://codeclimate.com/github/webgoal/livreiro)
[![Test Coverage](https://codeclimate.com/github/webgoal/livreiro/badges/coverage.svg)](https://codeclimate.com/github/webgoal/livreiro/coverage)

Desenvolvimento
---------------
### Instale:

  - Linux
    - [virtualbox](https://www.virtualbox.org/)
    - [docker](https://docs.docker.com/engine/installation/linux/ubuntulinux/)
    - [docker-compose](https://docs.docker.com/compose/install/)
    - [docker-machine](https://docs.docker.com/machine/install-machine/)

  - Mac / Windows
    - [docker-toolbox](https://www.docker.com/products/docker-toolbox)

### Executando a aplicação em desenvolvimento

#### Linux
Simplesmente vá para o passo `Subindo os containers`
- Atente-se para o fato que desta maneira, todos os arquivos que criar ficarão com o owner `root`. Após executar tarefas no container que criam arquivos, sempre execute:
```sh
sudo chown -R $USER:$USER .
```

#### Mac / Windows
Com o docker-machine, crie uma VM local:

```sh
docker-machine create default --driver virtualbox
```

Caso já tenha a VM `default`, apenas certifique-se que ela esteja atualizada e em execução:
```sh
docker-machine start default
docker-machine upgrade default
```

Faça o seu docker (client) apontar para o docker (server):
```sh
eval $(docker-machine env default)
```

#### Subindo os containers
```sh
  docker-compose up
```

##### Modo desacoplado (detached)

```sh
docker-compose up -d
```
Visualizando os logs. Caso não informar nenhuma imagem, ele exibirá os logs de todos os containers
```sh
docker-compose [imagem] logs
```

#### Acessando a aplicação
- Linux (sem docker-machine)
```sh
echo "127.0.0.1 dev.livreiro.net" | sudo tee -a /etc/hosts > /dev/null
```
- Mac / Linux com docker-machine
```sh
echo "$(docker-machine ip default) dev.livreiro.net" | sudo tee -a /etc/hosts > /dev/null
```
- Windows
Adicione o ip do docker-machine seguido do host `dev.livreiro.net` no arquivo `C:\Windows\System32\drivers\hosts`

### Instalando novas gems

Adicione a gem necessária no Gemfile e faça o build da imagem novamente

```sh
docker-compose build
docker-compose up
```

#### Executando testes

##### Primeira vez

```sh
RAILS_ENV=test docker-compose run web rake db:create
```
##### E então
```sh
docker-compose run web rake spec
```

Quaisquer outras tarefas administrativas como:
  - migrations
  - generators
  - console
  - seeds
  - rake tasks

Também podem ser executadas dessa mesma maneira

Deploy
------

### Para colocar em Produção:

##### O build da imagem do projeto é feito automaticamente. Basta atualizar a versão da imagem

##### Fazer nosso docker client apontar para o DOCKER_HOST de produção (Preferencialmente em outra aba...)
```sh
../docker-atelie
export MACHINE_STORAGE_PATH=`pwd`
eval $(docker-machine env docker-atelie)
```

### Executar os comandos:

#### Atualizar a versão da imagem (E reconstruir a imagem do nginx, caso tenha mudado)
```sh
docker-compose -f docker-compose-production.yml pull
docker-compose -f docker-compose-production.yml build
```

#### Executar as migrations
```sh
docker-compose -f docker-compose-production.yml run web bundle exec rake db:migrate
```

#### Executar a nova versão da aplicação

- Caso os containers NÃO estejam em execução
```sh
docker-compose -f docker-compose-production.yml up -d
```

- Caso estejam
```sh
docker-compose -f docker-compose-production.yml restart
```