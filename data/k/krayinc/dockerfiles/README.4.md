sshd on CentOS 6.3
==================

CentOS 6.3環境の検証用イメージのベース。権限の問題で（Dockerホストにはアクセスさせないため）コンテナにsshdが必要。

sshdを起動するコマンドはDockerfileに記述されているので、docker runの際には指定不要。rootにssh可能。パスワードは`password`。


ビルド方法
--------

例えばイメージのタグをcentos63sshdimageにする場合

```
docker build -t centos63sshdimage .
```


実行方法
-------

まずコンテナを起動する。例えばイメージのタグがcentos63sshdimageで、コンテナの名前をcentos63sshdにする場合

```
docker run -d -P --name centos63sshd centos63sshdimage
```

コンテナの22番ポートがDockerホストのどこかにマッピングされたはずなので、調べる

```
docker port centos63sshd 22
```

Dockerホストの表示されたポートにsshすればログインできる。

参考: [Dockerizing an SSH service - Docker Documentation](https://docs.docker.com/examples/running_ssh_service/)
