# Garden HCS (Host Compute Service)

Windows 2016 Containers implementation based on [Microsoft Host Compute Service Shim](https://github.com/Microsoft/hcsshim) for Cloud Foundry [Garden](https://github.com/cloudfoundry/garden).

## Requirements

* [golang 1.7.x](https://golang.org/dl/)
* [gcc from mingw-w64](https://sourceforge.net/projects/mingw-w64)
* Windows 2016 Server 1607 (10.0.14393) or newer.

## Build

To build garden-hcs run `go build` or `go get github.com/hpcloud/garden-hcs`.

## Run

To run the Garden service start the garden-hcs.exe executable with administrative privileges.

The "baseImagePath" argument is required and is the base images for all containers created by garden. The simplest way to get a "baseImagePath" is to use an existing image from docker. For example to get the image path for "microsoft/windowsservercore" image use the following PS snippet:
`(docker inspect microsoft/windowsservercore  | ConvertFrom-Json).GraphDriver.Data.Dir`

Garden-hcs run sample:

```
garden-hcs.exe -logLevel debug ^
 -listenAddr 0.0.0.0:9241
 -cellIP 192.168.50.16
 -baseImagePath C:\ProgramData\docker\windowsfilter\9c733a479cd00784b96656b7628eb1c0da3c96dd4b672dcf2c29f2fc7dc58d8d`
```

## Usage

The [Garden API](https://github.com/cloudfoundry/garden/blob/master/doc/garden-api.md) can be used directly with curl or Invoke-WebRequest.

Example:

`Invoke-WebRequest  -UseBasicParsing http://localhost:9241/capacity`

Another method is to use the [Garden client "gaol"](https://github.com/contraband/gaol) adapted for windows. To install gaol for Windows use: `go get github.com/stefanschneider/gaol`

Gaol usage sample:

```
gaol /t 127.0.0.1:9241 create
gaol /t 127.0.0.1:9241 list
gaol /t 127.0.0.1:9241 shell <container-id>
```

## Integration with Cloud Foundry and Diego

To add a Windows 2016 Cell to Cloud Foundry please refer to [dev-box](dev-box).
