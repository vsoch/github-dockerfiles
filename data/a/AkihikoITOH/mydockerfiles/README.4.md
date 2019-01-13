# [AWS Command Line Interface ](http://aws.amazon.com/cli/)

## Build

```
cp your-credentials credentials.production
```

and fill in `output`, `region`, `aws_access_key_id`, `aws_secret_access_key` with your own.

```
docker build -t awscli .
```

or

```
sh ./build.sh
```

## Run

```
docker run --rm -it awscli [options] <command> <subcommand> [parameters]
```

or

```
./aws [options] <command> <subcommand> [parameters]
```
