Medalha
==========

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

````

````
eval $(docker-machine env default)

````

````
docker-compose up web bash

````
bundle install

````

````
docker-compose up web

````

````
docker-compose run web rake db:migrate

````

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
echo "127.0.0.1 dev.medalha.com" | sudo tee -a /etc/hosts > /dev/null
```
- Mac / Linux com docker-machine
```sh
echo "$(docker-machine ip default) dev.medalha.com" | sudo tee -a /etc/hosts > /dev/null
```
- Windows
Adicione o ip do docker-machine seguido do host `dev.medalha.com` no arquivo `C:\Windows\System32\drivers\hosts`
Rodar como Administrador.

### Instalando novas gems

Adicione a gem necessária no Gemfile e faça o build da imagem novamente

```sh
docker-compose build
docker-compose run web bundle install
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

````

````
eval $(docker-machine env default)

````

````
docker-compose up web bash

````
bundle install

````

````
docker-compose up web

````

````
docker-compose run web rake db:migrate

````
