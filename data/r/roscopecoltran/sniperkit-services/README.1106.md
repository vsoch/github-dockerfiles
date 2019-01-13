Docker REMOTE API Caller with curl + jq

# 概要

Docker Machineで作られたDockerホストへのDocker Remote API呼び出し用イメージです。

# Usage

### 書式/引数/環境変数
```bash

$ docker run (options) yamamotofebc/docker-api-client [APIエンドポイント] [jqコマンド引数]

or

$ docker-compose run (options) docker-api-client [APIエンドポイント] [jqコマンド引数]

```


  - `APIエンドポイント` : 必須。`/images/json`など。詳細は[こちら](https://docs.docker.com/engine/reference/api/docker_remote_api/)を参照ください。
  - `jqコマンド引数` : オプション。デフォルト`.`。

#### 環境変数

  - `$DOCKER_HOST` : TLS保護付きTCPポートURL(docker-machine envコマンドで出力されるもの)
  - `$DOCKER_SOCKET` : $DOCKER_HOSTが未指定の場合に利用される。dockerのunixドメインソケットパス。デフォルト`/var/run/docker.sock`
  - `$DOCKER_CURL_OPTION` : curlコマンドに追加指定されるコマンド引数。(デフォルトで-sSfkは指定済み。それ以外の追加オプション(-xとか)を指定)

#### TLS接続する場合のvolumeの割り当て

以下にTLS関連ファイルが格納されていますので、/etc/dockerへvolumeを割り当ててください。

  - virtualboxなどのローカルドライバで作ったマシンの場合: `~/.docker/machine/machines/対象マシン`
  - sakuracloudなどのクラウドドライバで作ったマシンの場合: `/etc/docker`

イメージ内の`/etc/docker`配下のTLS関連ファイル名は以下のようになっている必要があります。

  - `証明書(--cert)` : `server.pem`
  - `秘密鍵(--key)` :  `server-key.pem`

### docker runで実行する場合(TLS接続)

```bash

# docker-machineコマンドで環境変数を設定しておく
$ eval $(docker-machine env 対象マシン)

$ docker run -it --rm -e DOCKER_HOST \
             -v /etc/docker:/etc/docker \
             yamamotofebc/docker-api-client /images/json

```

### docker runで実行する場合(unixドメインソケット)

```bash

# docker-machineコマンドで環境変数を設定しておく(アンセット)
$ eval $(docker-machine env -u)

$ docker run -it -v /var/run/docker.sock:/var/run/docker.sock \
             --rm yamamotofebc/docker-api-client /images/json

# DOCKER_SOCKET環境変数を指定していないため、/var/run/docker.sockが使われる

```


### docker-composeで実行する場合

#### 準備

```bash

$ git clone https://github.com/yamamoto-febc/docker-api-client.git
$ cd docker-api-client

```

#### 実行

```bash

$ docker-compose run --rm docker-api-client /images/json

```

#### 実行例(/images/jsonにてIDのみ抜き出し)

```bash

$ docker-compose run --rm docker-api-client /images/json ".[].Id"

```





