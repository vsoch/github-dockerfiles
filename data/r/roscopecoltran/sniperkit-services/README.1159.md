# docker-floyd-cli

[FloydHub](https://www.floydhub.com) floyd client docker image based on alpine.

## Build floyd client as docker image
```sh
$ docker build -t local/floyd --no-cache  .
```

## Create a project on floydhub UI
```sh
$ open https://www.floydhub.com
```

## Login
```sh
$ mkdir ~/.floyd
$ docker run -it --rm -v $HOME/.floyd:/root -v $(pwd):/code -w /code local/floyd sh
> $ floyd login
> Authentication token page will now open in your browser. Continue? [Y/n]: Y
# copy and paste token from floyd admin 

```

## Initialize project
```sh
$ floyd init <project-name>
```

## Run a Jupyter notebook with Tensorflow environment on GPU
```sh
$ floyd run --mode jupyter --env tensorflow --gpu
 :
 :
Setting up your instance and waiting for Jupyter notebook to become available ......................

Path to jupyter notebook: https://www.floydhub.com:8000/<RUN ID>

To view logs enter:
    floyd logs <RUN ID>

```

## Run a Tensorflow job on GPU
```sh
$ floyd run "python test.py" --gpu
$ floyd status
``` 

## Cleanup
```sh
$ floyd status 
$ floyd stop <ID>

$ floyd data status
$ floyd data delete <DATA ID>
```

