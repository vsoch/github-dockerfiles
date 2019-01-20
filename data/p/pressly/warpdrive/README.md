# Warpdrive

this is a single repo contains all the required and missing pieces for setup a system for updating react-native apps just like `Code-Push` or `AppHub`. 

So Why a new system? 

`Code-Push` is missing server component, `Walmart lab` is open sourced the server side but you always have to make sure the new release of `Code-Push` is compatiable by server side. Also for now `Code-Push` is free and we hope it stays that way but who knows what happens next in the future.

`AppHub` has the same probelm as `Code-Push` and also it cost money.

`Warpdrive` solves all of the above plus it uses `golang` under the hood. `golang` is a mature language and has been used for server side for quite a while and as soon as `gomobile` releases we decided to power `warpdrive` for both `android` and `ios`.

it has couple of major benefits:

- it has a powerful streaming capability which enables us to do zip and unzip over network on the fly. (good luck trying to implement it on both `Java` and `Objective-c`)
- low memory foot print
- one code base for both android and ios
- share code between server and client

<p align="center">
  We think Gopher can have a react-native tattoo as well!
</p>
<p align="center">
  <img width="200" src="https://raw.githubusercontent.com/pressly/warpdrive/master/docs/assets/gopher-tattoo.jpg" />
</p>

Cheers,
Pressly - Team

# Warpdrive

 COMMAND_CA=cert/ca-command.crt COMMAND_CRT=cert/cli.crt COMMAND_KEY=cert/cli.key COMMAND_ADDR=command:10000 ./warp publish -a share -p ios -r dev -v 1.1.3 -n test

# Dev Setup

in order to compile the code for android and ios, you need to have gomobile install

first install the gomobile

```
go get -u golang.org/x/mobile/cmd/gomobile 
```

make sure you have install ndk as well if you are not sure, look into this tutorial

``` 
https://developer.android.com/ndk/guides/index.html
```

then you have to initialize gomobile. this is one time operation

```
gomobile init
gomobile init -ndk ~/Library/Android/sdk/ndk-bundle/
```

### Postgres Setup

before running warpdrive, make sure you have a right role and database. you can run the follwoing sql in Postgres terminal

```bash
CREATE USER warpdrive WITH PASSWORD 'warpdrive';
CREATE DATABASE warpdrivedb;
```

and make sure to set the correct username, password and database in warpdrive.conf.

# Warpfile

server:
  addr: 192.168.0.1:3000
cycles:
  production:
    build: react-native build $PLATFORM



# Rollback
you have to unlock those version that you don't want


# Android

if you getting an error in Android Studio

```
Unsupported method: AndroidProject.getPluginGeneration().
The version of Gradle you connect to does not support that method.
To resolve the problem you can change/upgrade the target version of Gradle you connect to.
Alternatively, you can ignore this exception and read other information from the model.
```

then you should do this, go to `File / Settings/ Build, Execution, Deployment / Instant Run.` and Uncheck `Enable Instant Run to hot swap code...`


```java
UiThreadUtil.runOnUiThread(
  new Runnable() {
    @Override
    public void run() {
      mReactInstanceCommandsHandler.onJSBundleLoadedFromServer();
    }
  }
);
```
