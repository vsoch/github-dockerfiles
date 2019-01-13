# Build

As usual:
$ docker build  -t logstash5 .

# Usage

## Start Logstash with commandline configuration
If you need to run logstash with configuration provided on the commandline, you can use the logstash image as follows:

$ docker run -it --rm er/logstash5 logstash -e 'input { stdin { } } output { stdout { } }'

## Start Logstash with configuration file
If you need to run logstash with a configuration file, logstash.conf, that's located in your current directory, you can use the logstash image as follows:

$ docker run --rm -it -v $PWD:/testme logstash5 logstash -f /testme

Or you can use the test logstash.conf file located under ./test:
$ docker run --rm -it -v $PWD/test:/testme logstash5 logstash -f /testme

