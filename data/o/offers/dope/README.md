# dope
## About
Dope manages software distributed as Docker images. It can:
* Install Docker images and make them available as a command in your shell. No more adding an alias for every image's command.
* Notify you when a new image version is available, and update it for you.
* Automatically the right Docker command from the image (if it includes a .dope.json file).

## Install
```
\curl -sSL https://raw.githubusercontent.com/offers/dope/master/install.sh | sudo bash
```

Add `~/.dope/bin` to your PATH. On OS X set your PATH in `~/.bash_profile`, on Linux you probably want `~/.bashrc`.
```
PATH=$PATH:~/.dope/bin
```

## Usage
```bash
$ dope install my_registry/my_org/my_repo # install from your private registry

$ my_repo # run the docker image

$ dope update my_repo # pull the highest tag

$ dope uninstall my_repo # delete docker image and shell command

$ dope list # show installed packages

$ dope self-update # install the latest version of dope

$ dope check my_other_repo # check if an update is available
```

## Building/Releasing
Build with go >= 1.9.2

```$ go build```

1. Update `install.sh` with the new version number
2. Update `main.go` with the new version number
3. Tag and push git with the version, like `0.0.1`
4. Create a release on github, upload binaries for linux and darwin amd64.

Darwin binaries must be built on an OSX host.
