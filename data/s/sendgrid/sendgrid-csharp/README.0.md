**This helper allows you to quickly and easily build a Mail object for sending email through the SendGrid v3 API.**

# Quick Start

Run the [Example Project](https://github.com/sendgrid/sendgrid-csharp/tree/master/ExampleCoreProject) (make sure you have set your Environment variable to include your SENDGRID_API_KEY).

Click on the Example project, then click the `Start` button in the menu.

## Usage

- See the [example](https://github.com/sendgrid/sendgrid-csharp/tree/master/ExampleCoreProject/Example.cs) for a complete working example.
- [Documentation](https://sendgrid.com/docs/API_Reference/Web_API_v3/Mail/overview.html)
**The SendGrid C# .NET library provide an easy way to send emails. This example application shows how to integrate with an ASP.NET application.**

# Installation

## Prerequisites

- .NET version 4.5.2 and higher
- Visual Studio 2015

##  Setup Environment Variables

Update the "SendGridApiKey" appSettings variable within the web.config file.

## Steps

1. Open SendGrid.ASPSamples.sln
2. Switch to one of the example project (right click on a project -> "Set as StartUp project")
2. Build and run the project

You may need to download the latest Nuget executable and run `nuget.exe restore`

3. When you run the project, a web form will launch in your browser that will send an email.

## Happy coding

Big thanks to [paritosh baghel](https://github.com/paritoshmmmec) for contributing this example code!You can use Docker to easily try out or test sendgrid-csharp.

# Quickstart

1. Install Docker on your machine.
2. Build the latest container with `docker build -t sendgrid/sendgrid-csharp docker`
3. Run `docker run -it sendgrid/sendgrid-csharp`.

# Info

This Docker image contains
 - `sendgrid-csharp`
 - Stoplight's Prism, which lets you try out the API without actually sending email

Run it in interactive mode with `-it`.

You can mount a repository in the `/mnt/sendgrid-csharp` directory to use it instead of the default SendGrid library.

# Testing
Testing is easy!  Run the container, then `dotnet test ./tests/SendGrid.Tests/SendGrid.Tests.csproj -c Release -f netcoreapp1.0`

# Usage examples

- Most recent version: docker run -it sendgrid/sendgrid-csharp.
- Your own fork:
  ```sh-session
  $ git clone https://github.com/you/cool-sendgrid-csharp.git
  $ realpath cool-sendgrid-csharp
  /path/to/cool-sendgrid-csharp
  $ docker run -it -v /path/to/cool-sendgrid-csharp:/mnt/sendgrid-csharp sendgrid/sendgrid-csharp
  ```