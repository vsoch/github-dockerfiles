# RavenDB - An ACID NoSQL Document Database
This repository contains source code for the [RavenDB](https://ravendb.net/) document database. With a RavenDB database you can set up a NoSQL data architecture or add a NoSQL layer to your current relational database.

![RavenDB Studio](docs/readmeScreenshot.png)

## Supported Platforms
- Windows
- Linux
- Docker
- MacOS
- Raspberry Pi

## Grab Your License and Download Latest Version

Request [your license](https://ravendb.net/free).

Download [the latest version of RavenDB](https://ravendb.net/downloads).

## Getting Started
Install and [set up your database](https://ravendb.net/docs/article-page/4.1/csharp/start/getting-started).

## Learn RavenDB Quickly
[RavenDB Bootcamp](https://ravendb.net/learn/bootcamp) is a free, self-directed learning course. In just three units you will learn how to use RavenDB to create fully-functional, real-world programs with NoSQL Databases. If you are unfamiliar with NoSQL, it’s okay. We will provide you with all the information you need.

## Stay Updated on New Developments
We keep adding new features to improve your RavenDB experience. Check out [our latest improvements](https://ravendb.net/docs/article-page/4.1/csharp/start/whats-new), updated weekly.

## Documentation
Access [full documentation](https://ravendb.net/docs/article-page/4.1/csharp) for RavenDB. Like our database, it is easy to use.

## Where to Ask for Help
If you have any questions, or need further assistance, you can [contact us directly](https://ravendb.net/contact).

## Report an Issue
You can create issues and track them at our [YouTrack](http://issues.hibernatingrhinos.com/) page.

## RavenDB Developer Community Group
If you have any questions please visit our [community group](http://groups.google.com/group/ravendb/). The solutions for the most common challenges are available. You are welcome to join!

## Pull requests
Please check out our [contribution guidelines](./CONTRIBUTING.md).

## Setup & Run

First please [review and set up prerequisites](https://ravendb.net/docs/article-page/4.1/csharp/start/getting-started#prerequisites).

### Launch RavenDB:
Running locally:
```
<path/to/ravendb>/Server/Raven.Server
```

Registering as service in Windows using `rvn` utility available in the package *Server* directory:
```
<path\to\ravendb>\rvn.exe windows-service register --service-name RavenDB4
```

### Hello World (.NET)

#### Server Side

- Launch a RavenDB server instance as follows:
```
<path/to/ravendb>/Server/Raven.Server --ServerUrl=http://localhost:8080
```

- Open a web browser and enter `http://localhost:8080`

- Click on `Databases` in the menu on the left-hand side, and then create a new database named `SampleDataDB`

- Click on `Settings` and then on `Create Sample Data` in the left menu. Now Click on `Create`

#### Client Side

- Install .NET Core SDK. See : [Downloads](https://www.microsoft.com/net/download) and [PowerShell](https://github.com/PowerShell/PowerShell/releases)

- Open a terminal and type:

```bash
mkdir HelloWorld
cd HelloWorld
dotnet new console
```

- Add the RavenDB Client package:

```powershell
   dotnet add package RavenDB.Client --version 4.1.0-*
```

- Replace the content of Program.cs with the following:
```csharp
using System;
using Raven.Client.Documents;

namespace HelloWorld
{
    class Shippers
    {
        public string Name;
        public string Phone;
    }
    
    class Program
    {
        static void Main(string[] args)
        {
            using (var store = new DocumentStore
            {
                Urls = new string[] {"http://localhost:8080"},
                Database = "SampleDataDB"
            })
            {
                store.Initialize();

                using (var session = store.OpenSession())
                {
                    var shipper = session.Load<Shippers>("shippers/1-A");
                    Console.WriteLine("Shipper #1 : " + shipper.Name + ", Phone: " + shipper.Phone);
                }
            }
        }
    }
}
```

- Type:
```bash
dotnet restore
dotnet build
dotnet run
```

###### Enjoy :)
Monsters.json was taken from https://github.com/CleverRaven/Cataclysm-DDA/blob/master/data/json/monsters.json as an example of a big read-life json file. This file is licensed under Creative Commons Attribution-ShareAlike 3.0 Unported (https://creativecommons.org/licenses/by-sa/3.0/). Code in this library taken from http://www.yoda.arachsys.com/csharp/miscutil/
BSD License
Startup instructions for RavenDB on Windows 
===========================================

* RavenDB as a Console Application
Open Powershell
Type:
    .\run.ps1

* RavenDB as Service
Open Powershell
Type:
    .\setup-as-service.ps1

The above command is going to install 'RavenDB' service on your machine. Note it requires to be run as administrator. It is going to ask whether you'd like to setup secure RavenDB server. The server is going to start on port 8080 or 443, if you have chosen to run in secure mode. 

You can view its status using the Get-Service Powershell cmdlet:

>  Get-Service -Name RavenDB

Status   Name               DisplayName
------   ----               -----------
Running  RavenDB            RavenDB

To manage service you can use Stop-Service and Start-Service cmdlets (requires administrator privileges).

* Setup
    Open browser, if not opened automatically, at url printed in "Server available on: <url>"
    Follow the web setup instructions at: https://ravendb.net/docs/article-page/4.0/csharp/start/installation/setup-wizard

Startup instructions for RavenDB on Linux
=========================================

* RavenDB as a Console Application
Open bash terminal
Type:
    chmod +x run.sh
    ./run.sh


* RavenDB as Daemon (systemd - applies to Ubuntu 16.04)
Open bash terminal, and create file /etc/systemd/system/ravendb.service, using super user permissions, containing:
    [Unit]
    Description=RavenDB v4.1
    After=network.target

    [Service]
    LimitCORE=infinity
    LimitNOFILE=65536
    LimitRSS=infinity
    LimitAS=infinity
    User=<desired user>
    Restart=on-failure
    Type=simple
    ExecStart=/path/to/RavenDB/run.sh

    [Install]
    WantedBy=multi-user.target

Note: Replace in the above text the username "User=<desired user>" and set path in "ExecStart"

Then register the service and enable it on startup by typing:
    systemctl daemon-reload
    systemctl enable ravendb.service

Start the service:
    systemctl start ravendb.service

View its status using:
    systemctl status ravendb.service
    or
    journalctl -f -u ravendb.service

* Setup
Open browser, if not opened automatically, at url printed in "Server available on: <url>"
Follow the web setup instructions at: https://ravendb.net/docs/article-page/4.0/csharp/start/installation/setup-wizard



## RavenDB Docker Support

The files here support building and running RavenDB 4.1 in a docker container on either Linux or Windows (nanoserver).

### Official images

 Official Docker images are available on our [Docker Hub](https://hub.docker.com/r/ravendb/ravendb/). We provide images in two flavors: ubuntu-based (to be run on Linux containers) and nanoserver-based (to be run using Windows containers). The following tags are available:

- `4.1-ubuntu-latest` - contains the latest version of RavenDB 4.1 running on Ubuntu 18.04 container

- `4.1-windows-nanoserver-latest` - contains the latest version of RavenDB 4.1 running running on Windows nanoserver

- every 4.1 release is going to have its own image set for both Ubuntu and Windows containers

### Running

Simplest way to run and try RavenDB out is:

Linux image:
```
$ docker run -p 8080:8080 ravendb/ravendb:4.1-ubuntu-latest
```

Windows image:
```
$ docker run -p 8080:8080 ravendb/ravendb:4.1-windows-nanoserver-latest
```

Optionally nightly images can be used from [ravendb/ravendb-nightly](https://hub.docker.com/r/ravendb/ravendb-nightly/)

You can run RavenDB docker container manually by invoking `docker run`, yet if you don't feel that docker-savvy we recommend using our scripts:

Run Ubuntu-based image: [run-linux.ps1](https://github.com/ravendb/ravendb/blob/v4.1/docker/run-linux.ps1)

Run Windows-based image: [run-nanoserver.ps1](https://github.com/ravendb/ravendb/blob/v4.1/docker/run-nanoserver.ps1)

Above mentioned Powershell scripts are simplifying usage of our images allowing you to pass various switches and options to configure RavenDB inside the container:

|Option|Default|Description|
|------|:-----:|-----------|
|`-DryRun`| | print `docker run` command and exit |
|`-LogsMode [log level]`| Operations | set logging level (Operations, Information) |
|`-ConfigPath [absolute file path]` | | *absolute* path to settings file used by RavenDB inside the container |
| `-DataDir [absolute dir path]` || host directory mounted to the volume used for persistence of RavenDB data (if not provided a regular docker volume is going to be used) |
| `-BindPort [port]` | 8080 | the port number on which RavenDB Server is exposed on the container |
| `-BindTcpPort [port]` | 38888 | the port number on which RavenDB Server listens for TCP connections exposed on the container |
| `-NoSetup` | | disable setup wizard |
| `-RemoveOnExit` || removes container on server process exit |
| `-PublicServerUrl` || set the public url under which server is available to other nodes or admins (e.g. http://4.live-test.ravendb.net:80)
| `-PublicTcpServerUrl` || set the url under which server is available to the outside world (e.g. tcp://4.live-test.ravendb.net:38888) |
| `-Unsecured` | | HERE BE DRAGONS - disable authentication for RavenDB server |

Once run RavenDB server should be exposed on port 8080 by default.

### Docker volumes

Each of images above makes use of 2 volumes:

- settings volume - holding RavenDB configuration,

    Ubuntu container: `/opt/RavenDB/config`

    Windows container: `C:\RavenDB\Config`

- databases volume - used for persistence of RavenDB data,

    Ubuntu container: `/opt/RavenDB/Server/RavenData`

    Windows container: `C:/RavenDB/Server/RavenData`

### Configuration

To configure RavenDB one can use (in order of precedence):

    - environment variables, 

    - `settings.json` configuration file, 

    - CLI arguments

#### Environment variables

Environment variables prefixed with `RAVEN_` can be used to configure RavenDB server. E.g. one can use:
```bash
RAVEN_Setup_Mode='None'
```
to disable RavenDB Setup Wizard.

#### FAQ

##### I'm using compose / doing automated installation. How do I disable setup wizard?
    
Set `Setup.Mode` configuration option to `None` like so:
```bash
RAVEN_Setup_Mode='None'
```

##### I want to try it out on my local / development machine. How do I run unsecured server?

Set env variables like so:
```bash
RAVEN_Setup_Mode='None'
RAVEN_Security_UnsecuredAccessAllowed='PrivateNetwork'
```

##### How can I pass command line arguments?

By modifying `RAVEN_ARGS` environment variable. It's passed as an CLI arguments line.

##### Can I see RavenDB logs by running `docker logs`?

To get logs available when running `docker logs` command, you need to turn that on for RavenDB server. Setting below environment variables like so is going to enable logging to console. Please note such behavior may have performance implications. Log level may be modified using `RAVEN_Logs_Mode` variable. 

```bash
RAVEN_ARGS='--log-to-console'
```

##### How to set a custom config file?

Mount it as a docker volume and use `--config-path PATH_TO_CONFIG` command line argument in order to use settings file from outside of server directory.

#### Dockerfiles

These images were built using the following Dockerfiles:

- [Windows Nanoserver image Dockerfile](https://github.com/ravendb/ravendb/blob/v4.1/docker/ravendb-nanoserver/Dockerfile)

- [Ubuntu 18.04 image Dockerfile](https://github.com/ravendb/ravendb/blob/v4.1/docker/ravendb-linux/Dockerfile)
# Simple docker compose setup for 3 node cluster

Note: Please remember to put *license.env* file in this directory. It should contain a line setting `RAVEN_License environment variable containing license information e.g.
```
RAVEN_License={"Id": "LICENSEID", "Name": "Testing", "Keys": [ ... ]}
```

## Create and run cluster
```
.\run.ps1 [-DontSetupCluster] [-StartBrowser]
-DontSetupCluster - just create nodes without setting them up
-StartBrowser - launch RavenDB studio in the browser 
```

## Destroy cluster
```
.\destroy.ps1
```
# Simple docker compose setup for *unsecured* 3 node cluster

Note: Please remember to put *license.env* file in this directory. It should contain a line setting `RAVEN_License` environment variable containing license information e.g.
```
RAVEN_License={"Id": "LICENSEID", "Name": "Testing", "Keys": [ ... ]}
```

## Create and run cluster
```
.\run.ps1 [-DontSetupCluster] [-StartBrowser]
```

```
-DontSetupCluster - just create nodes without setting them up
-StartBrowser - starts browser with first node's Studio
```

## Destroy cluster
```
.\destroy.ps1
```
