# dockerfile-gen

Generator Dockerfile

## Installation

#### Binaries

- **darwin (macOS)** [amd64](https://github.com/janiltonmaciel/dockerfile-gen/releases/download/1.10.0/dockerfile-gen_1.10.0_macOS_amd64.tar.gz)
- **linux** [386](https://github.com/janiltonmaciel/dockerfile-gen/releases/download/1.10.0/dockerfile-gen_1.10.0_linux_386.tar.gz) / [amd64](https://github.com/janiltonmaciel/dockerfile-gen/releases/download/1.10.0/dockerfile-gen_1.10.0_linux_amd64.tar.gz)
- **windows** [386](https://github.com/janiltonmaciel/dockerfile-gen/releases/download/1.10.0/dockerfile-gen_1.10.0_windows_386.zip) / [amd64](https://github.com/janiltonmaciel/dockerfile-gen/releases/download/1.10.0/dockerfile-gen_1.10.0_windows_amd64.zip)

#### Via Homebrew (macOS)
```bash
$ brew tap janiltonmaciel/homebrew-tap
$ brew install dockerfile-gen
```

#### Via Go

```bash
$ go get github.com/janiltonmaciel/dockerfile-gen
```

#### Running with Docker

```bash
$ docker run -it --rm \
    -v $(pwd):/app \
    janilton/dockerfile-gen
```

## Usage
Creating Dockerfile

![](https://github.com/janiltonmaciel/dockerfile-gen/blob/master/assets/img/dc-gen-create.gif)
  
---  
Building docker image  
   

![](https://github.com/janiltonmaciel/dockerfile-gen/blob/master/assets/img/dc-gen-build.gif)

---  
Running docker image  
   

![](https://github.com/janiltonmaciel/dockerfile-gen/blob/master/assets/img/dc-gen-run.gif)
