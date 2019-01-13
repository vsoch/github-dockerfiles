[![License : AGPL v3](https://img.shields.io/badge/license-AGPL3-blue.svg)](https://github.com/Asqatasun/asqa.mvn/blob/master/LICENSE) [![Release](https://img.shields.io/github/release/asqatasun/asqa.mvn.svg)](https://github.com/Asqatasun/asqa.mvn/releases/latest) [![Code of Conduct](https://img.shields.io/badge/code%20of-conduct-ff69b4.svg?style=flat-square)](https://github.com/Asqatasun/asqa.mvn/blob/master/CODE_OF_CONDUCT.md) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/Asqatasun/asqa.mvn/pulls)


# Docker Maven for Asqatasun projects

Maven Docker images preloaded with Maven plugins needed for compilation.

## Supported tags 

Supported tags and respective `Dockerfile` links :

### Asqatasun
* jdk7.alpine ([Asqatasun/jdk-7/alpine/Dockerfile](https://github.com/Asqatasun/asqa.mvn/blob/master/Asqatasun/jdk-7/alpine/Dockerfile))
* jdk8.alpine ([Asqatasun/jdk-8/alpine/Dockerfile](https://github.com/Asqatasun/asqa.mvn/blob/master/Asqatasun/jdk-8/alpine/Dockerfile))
* jdk7, latest ([Asqatasun/jdk-7/Dockerfile](https://github.com/Asqatasun/asqa.mvn/blob/master/Asqatasun/jdk-7/Dockerfile))
* jdk8 ([Asqatasun/jdk-8/Dockerfile](https://github.com/Asqatasun/asqa.mvn/blob/master/Asqatasun/jdk-8/Dockerfile))

### Asqatasun-Jenkins-Plugin
* jenkins_jdk7.alpine ([Asqatasun-Jenkins-Plugin/jdk-7/alpine/Dockerfile](https://github.com/Asqatasun/asqa.mvn/blob/master/Asqatasun-Jenkins-Plugin/jdk-7/alpine/Dockerfile))
* jenkins_jdk8.alpine ([Asqatasun-Jenkins-Plugin/jdk-8/alpine/Dockerfile](https://github.com/Asqatasun/asqa.mvn/blob/master/Asqatasun-Jenkins-Plugin/jdk-8/alpine/Dockerfile))
* jenkins_jdk7 ([Asqatasun-Jenkins-Plugin/jdk-7/Dockerfile](https://github.com/Asqatasun/asqa.mvn/blob/master/Asqatasun-Jenkins-Plugin/jdk-7/Dockerfile))
* jenkins_jdk8 ([Asqatasun-Jenkins-Plugin/jdk-8/Dockerfile](https://github.com/Asqatasun/asqa.mvn/blob/master/Asqatasun-Jenkins-Plugin/jdk-8/Dockerfile))

### Contrast-Finder
* contrast.finder_jdk8.alpine ([Contrast-Finder/jdk-8/alpine/Dockerfile](https://github.com/Asqatasun/asqa.mvn/blob/master/Contrast-Finder/jdk-8/alpine/Dockerfile))
* contrast.finder_jdk8  ([Contrast-Finder/jdk-8/Dockerfile](https://github.com/Asqatasun/asqa.mvn/blob/master/Contrast-Finder/jdk-8/Dockerfile))
* contrast.finder_jdk9  ([Contrast-Finder/jdk-9/Dockerfile](https://github.com/Asqatasun/asqa.mvn/blob/master/Contrast-Finder/jdk-9/Dockerfile))
* contrast.finder_jdk10 ([Contrast-Finder/jdk-10/Dockerfile](https://github.com/Asqatasun/asqa.mvn/blob/master/Contrast-Finder/jdk-10/Dockerfile))


## How to use this image

### Usage
```shell
docker pull asqatasun/asqa.mvn:jdk7
```

#### Compile Asqatasun 
```shell
git clone https://github.com/Asqatasun/Asqatasun.git
cd Asqatasun
docker run -it --rm  -v "$PWD":/usr/src/  -w /usr/src/ asqatasun/asqa.mvn:jdk7  mvn clean install
```

#### Clean build directories 
```shell
cd Asqatasun
docker run -it --rm  -v "$PWD":/usr/src/  -w /usr/src/ asqatasun/asqa.mvn:jdk7  mvn clean 
```

#### Check and manipulate the image
```shell
docker run -it --rm  asqatasun/asqa.mvn:jdk7  /bin/bash
docker run -it --rm  asqatasun/asqa.mvn:jdk7  javac -version
docker run -it --rm  asqatasun/asqa.mvn:jdk7  java  -version
docker run -it --rm  asqatasun/asqa.mvn:jdk7  mvn   -version
```



## Contact and discussions

* [Asqatasun forum](http://forum.asqatasun.org/) 
* [Twitter @Asqatasun](https://twitter.com/Asqatasun)
* email to `asqatasun AT asqatasun dot org` (only English, French and klingon is spoken :) ) 


## Contributing

You are invited to contribute new features, fixes, or updates, 
large or small; we are always thrilled to receive pull requests, 
and do our best to process them as fast as we can.

Before you start to code, we recommend discussing your plans through 
a [GitHub issue](https://github.com/Asqatasun/asqa.mvn/issues), especially for more ambitious contributions. 
This gives other contributors a chance to point you in the right direction, 
give you feedback on your design, and help you find out if someone 
 else is working on the same thing.

