# Site do CACo

Este é o código do site do CACo, servido na url www.caco.ic.unicamp.br

Todos são bem-vindos a colaborar com o desenvolvimento, reportar bugs ou pedir features.

1. [Instalação](#instalação)
    1. [Instalação Local](#instalação-local)
    1. [Docker](#docker)
1. [Banco de Dados](#banco-de-dados)

Qualquer problema, não hesite em contatar os administradores do repositório

## Instalação
### Instalação Local
#### virtualenv
É recomendado executar o projeto e instalar as dependências em um ambiente virtual de Python (virtualenv) para evitar conflitos de versões e problemas de dependencias. Para isso, execute os seguintes comandos para criar o ambiente virtual e ativá-lo.

##### Instalando
```console
$ pip3 install virtualenv
```

##### Executando
```console
$ virtualenv env
$ source env/bin/activate
```

Para desativar o ambiente, basta executar o comando `deactivate`, carregado ao se ativar o ambiente.

### Requerimentos do sistema
 - python 3
 - pip 3

### Dependencias
Todas as dependencias estão no arquivo `requirements.txt` na raiz do projeto

#### Instalando com pip
```console
$ pip3 install -r requirements.txt
```

##### config.json
crie o arquivo `config.json` no root do projeto com o seguinte conteúdo - modificando nas partes necessárias

```json
{
  "URL_BASE": "",
  "URL_NAME": "http://127.0.0.1:8000/",
  "ALLOWED_HOSTS": ["*"],
  "DEBUG": true,
  "SECRET_KEY": "alguma chave secreta",
  "LANGUAGE_CODE": "pt-BR",
  "TIME_ZONE": "America/Sao_Paulo",
  "DATABASE_NAME": "db.sqlite3",
  "DATABASE_USER": "",
  "DATABASE_PASS": "",
  "DATABASE_HOST": "",
  "DATABASE_PORT": 5432,
  "EMAIL_HOST": "smtp.gmail.com",
  "EMAIL_PORT": 587,
  "EMAIL_USE_TLS": true,
  "EMAIL_NAME": "usuario",
  "EMAIL_HOST_USER": "usuario@email",
  "EMAIL_HOST_PASSWORD": "senhaemail",
  "RECAPTCHA_SECRET": "segredo-do-recaptcha",
  "ANALYTICS_ID": "googleanalytics id",
  "ADMINS":  []
}

```
os dois tipos de database disponíveis de cara para serem executados são `db.sqlite3` ou `postgres`


depois, execute
```console
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py runserver
```

### Docker
Dentro do repositório existe um arquivo [Dockerfile](https://docs.docker.com/engine/reference/builder/) para criação de um container do site do caco. Nele está sendo rodada uma imagem python:3.5 e configurada para servir o site atravez de sockets usando o [uWSGI](https://uwsgi-docs.readthedocs.io/) na porta 8001. No entanto é importante, caso você vá rodar somente o Dockerfile do site, de criar um volume compartilhado do host na pasta do projeto com /code/ no container quando usar run:
```console
docker run $nome-da-imagem -v ./:/code -p 8001:8001
```


#### [Docker-compose](https://docs.docker.com/compose/)
O Docker-compose é uma plataforma criada para facilitar o deploy de vários containers juntos. Este projeto está configurado para criar 3 containers (nginx, postgres, site) para deixar o site já em produção.

##### nginx
O nginx está configurado para servir somente na porta 443 (https). Para gerar certificados para utilização desses containers pode-se utilizar o projeto [Let's Encrypt](https://letsencrypt.org/). Para isso, use o [certbot](https://certbot.eff.org/) para criar os arquivos em `/etc/letsencrypt/`

##### config.json
É também necessário criar o arquivo de configurações no root do projeto. modifique da maneira que achar necessário

```json
{
  "URL_BASE": "",
  "URL_NAME": "url do seu site",
  "ALLOWED_HOSTS": ["*"],
  "DEBUG": false,
  "SECRET_KEY": "chave_secreta",
  "LANGUAGE_CODE": "pt-BR",
  "TIME_ZONE": "America/Sao_Paulo",
  "DATABASE_NAME": "postgres",
  "DATABASE_USER": "usuario-postgres",
  "DATABASE_PASS": "senha-postgres",
  "DATABASE_HOST": "url do postgres",
  "DATABASE_PORT": 5432,
  "EMAIL_HOST": "smtp.gmail.com",
  "EMAIL_PORT": 587,
  "EMAIL_USE_TLS": true,
  "EMAIL_NAME": "usuario",
  "EMAIL_HOST_USER": "usuario@email",
  "EMAIL_HOST_PASSWORD": "senhaemail",
  "RECAPTCHA_SECRET": "segredo-do-recaptcha",
  "ANALYTICS_ID": "googleanalytics id",
  "ADMINS": [
              ["Nome", "email"],
              ["Nome2", "email2 (...)"]
            ]
}
```

##### Executando
Podemos executar o ambiente para produção (com https) ou o local para testes. Mude o argumento do `-f docker-compose.yml` para `docker-compose-local.yml`

```console
$ docker-compose up -d --build
$ docker-compose run --rm site_do_caco python manage.py migrate

$ (...)
```

## Dados
### Static files
Os arquivos estáticos devem ser colocados na pasta `static`

### Media files
Os arquivos de media devem ser colocados - e são coloados - na pasta (a ser criada) `sitecaco/media`

### Admin
para criar um usuário admin e poder logar em /admin/
```console
$ python3 manage.py createsuperuser
```
### Exportando
```console
$ python3 manage.py dumpdata -e contenttypes -e admin -e auth.Permission --natural-foreign --indent=2 > bd.json
```

### Importando
```console
$ python3 manage.py loaddata bd.json
```
