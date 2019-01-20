realXtend Tundra
================

[![License badge](https://img.shields.io/badge/license-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Documentation badge](https://readthedocs.org/projects/synchronization/badge/?version=latest)](http://synchronization.readthedocs.org/en/latest)
[![Docker badge](https://img.shields.io/docker/pulls/loorni/synchronization.svg)](https://hub.docker.com/r/loorni/synchronization/)
[![Support badge]( https://img.shields.io/badge/support-sof-yellowgreen.svg)](http://stackoverflow.com/questions/tagged/fiware-synchronization)

Tundra is a scriptable 3D internet application development platform. It is aimed primarily for application developers, as a platform for creating networked 3D worlds with customized content.

Tundra is licensed under [Apache 2.0] and based on [Qt] and [Ogre3D].

Getting Started
---------------

Tundra uses the traditional client-server architecture for networking. After installing you will find the `Tundra` (and `TundraConsole` on Windows) executable from the install directory, run `Tundra --help` for available command line parameters. This executable can be configured to run a set of C++ and JavaScript plugins and act either as a client or a server. You can create your own configuration file, or use the ones provided.

### Tundra Startup Examples  
- `Tundra --config tundra-client.json` - Starts Tundra with a client configuration which provides an user interface for connecting to Tundra servers.
- `Tundra --connect localhost:2345;udp;TestUser` - Starts Tundra and automatically connects to a localhost server using port 2345 and UDP protocol (the Tundra server's defaults).   
- `Tundra --server --headless --port 6565 --protocol tcp` - Starts Tundra with the default plugin set in server mode serving TCP connections at port 6565.

The Tundra server defaults are port 2345 and UDP protocol, for it you can simply run `Tundra --server --headless`. If no `--config` parameter is provided, the default `tundra.json` is used.  

The Tundra server mode is used for standalone-mode editing and viewing Tundra documents. To host a 3D scene, run Tundra in dedicated mode using the `--server` and `--headless` command line parameters. The Tundra client mode is used to connect to a server.

### Demo Scenes and Applications
See the [bin/scenes] folder for example demo scenes and applications. F.e.x. `Tundra --file scenes/Canvas/scene.txml`

### Additional Plugins
Additional Tundra plugins can be found from the [TundraAddons] repository.

Compiling from Sources
----------------------

Tundra source code is available at the [realXtend github repository]. This repository hosts various branches for current and deprecated development lines from the realXtend team, so be sure to checkout `tundra2` branch after cloning.

Tundra uses [CMake] as its build system and depends on various other open source projects.

### Windows

Visual Studio 2008 and 2010 build environments are currently supported. Make sure that you have the latest Visual Studio Service Packs installed. Visual Studio 2012 and newer can be used to open and build the VS2010-generated Tundra solution as long as the solution is not upgraded to the newer format.

The Tundra dependencies are acquired and built using an automated build script:  
1. Open up the Visual Studio (x64 Win64) Command Prompt which is required in order to have the required build tools and several other utilities in your PATH.  
2. Navigate to `<Tundra>\tools\Windows\VS<VersionNumber>\`  
3. Run `BuildDeps_<BuildType>`, or `BuildDepsX64_<BuildType>` (if wanting to do a 64-bit build). RelWithDebInfo is recommended for the common development work, but you probably want to have the Debug builds available too.  
   The build script will print information what you need in order to proceed, follow the instructions carefully. You can abort the script with Ctrl+C at this point and setup your environment.  
4. Once you are done setting up your build environment, hit any key to continue the script as it instructs. The full depedency build might take up to 2 hours.
5. After the script has completed, the dependencies can be found `deps-vs<VersionNumber>-<TargetArchitecture>\`. The needed runtime libraries are automatically copied to `bin\`.  
6. Now run CMake batch script corresponding to your desired build configration. This script will set up the needed build environment variables for CMake and invoke CMake to generate a tundra.sln solution.  
7. Build Tundra using the solution file.

### Linux

Currently Ubuntu, Mint, Debian, and Kali are officially supported. See [tools/Linux/build-deps.bash] for the unified build script. 

### OS X

See [tools/OSX/BuildDeps.bash] for automated dependency and Tundra build script.

### Android

Experimental Android support exists, see [android/Build-instructions.txt] for the build instructions.

Developer Documentation
-----------------------

Tundra uses [Doxygen] as its main documentation tool. In order to generate and view the developer documentation, follow these steps:  
1. have Doxygen installed,  
2. `cd doc`,  
3. `doxygen tundra.Doxyfile`,  
4. `cd html`, and  
5. open up `index.html`.

Contributing
------------
0. Preferably interact with the developers already in advance before starting your work.
1. Fork Tundra.
2. Preferably create a feature branch for your work.
3. Make sure to follow the coding conventions (doc/dox/CodingConventions.dox).
4. Make a pull request.

Contact Information
-------------------

You can find Tundra developers from IRC `#realxtend-dev @ freenode`. Also check out the [user-oriented mailing list](http://groups.google.com/group/realxtend) and the [developer-oriented mailing list](http://groups.google.com/group/realxtend-dev).

Releases
--------

New releases are announced on the mailing lists and at the [realXtend blog]. The releases are available at the [realXtend Tundra Google Code] project site.

[Qt]: http://qt.digia.com/ "Qt homepage"
[Ogre3D]: http://www.ogre3d.org/ "Ogre3D homepage"
[bin/scenes]: https://github.com/realXtend/naali/tree/tundra2/bin/scenes "bin/scenes"
[TundraAddons]: https://github.com/realXtend/TundraAddons/ "TundraAddons"
[Apache 2.0]: http://www.apache.org/licenses/LICENSE-2.0.txt "Apache 2.0 license"
[CMake]: http://www.cmake.org/ "CMake homepage"
[realXtend blog]: http://www.realxtend.org "realXtend blog"
[realXtend github repository]: https://github.com/realXtend/naali/tree/tundra2 "realXtend Tundra repository"
[tools/OSX/BuildDeps.bash]: https://github.com/realXtend/naali/blob/tundra2/tools/OSX/BuildDeps.bash "tools/OSX/BuildDeps.bash"
[tools/Linux/build-deps.bash]: https://github.com/realXtend/naali/tree/tundra2/tools/Linux/build-deps.bash "tools/Linux/build-deps.bash"
[android/Build-instructions.txt]: https://github.com/realXtend/naali/tree/tundra2/android/Build-instructions.txt "android/Build-instructions.txt"
[Doxygen]:  http://www.stack.nl/~dimitri/doxygen/ "doxygen homepage"
[realXtend Tundra Google Code]: http://code.google.com/p/realxtend-naali/downloads/list

FIWARE Guides
-------------

[Synchronization - Installation and Administration Guide](doc/Installation_and_Administration_guide.md)

[Synchronization - User and Programmer's Guide](doc/User_and_Programmers_guide.md)

---------------------------------------------------------------------------------------------------------
This project is part of FIWARE.
[https://www.fiware.org/](https://www.fiware.org/)

FIWARE catalogue: [Synchronization GE](http://catalogue.fiware.org/enablers/synchronization)
