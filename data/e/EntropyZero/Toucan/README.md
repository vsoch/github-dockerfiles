# Toucan

Travis: [![Build Status](https://travis-ci.org/EntropyZero/Toucan.svg?branch=master)](https://travis-ci.org/EntropyZero/Toucan)

Toucan is a .NET Core (DNX Core) library targeting ASP.NET Core MVC applications. Toucan was inspired by the Rails gems [CanCan](https://github.com/CanCanCommunity/cancancan) and [Canard](https://github.com/james2m/canard), and is intended to be a resource authorization library for MVC applications that provides for declarative resource loading and authorization without requiring developers to load and authorize resources imperatively in controller actions. All resource permissions are defined in a single location and not duplicated across controllers, views, and database queries.

## Installation

Toucan distributed as a NuGet package. If using the package console:

```powershell
Install-Package Toucan
```

Or, you can register the dependency in your project.json file:

```json
"dependencies":{
  "Toucan": "1.0.0-*"
}
```

and run

```bash
dotnet restore
```

You will also need one of the Toucan ORM Adapter packages.

As of now there is only EntityFramework 7, but I have plans to add more once the Toucan base is stable and new features are not as pressing for the main package. The package is Toucan.EntityFramework, and may be obtained in the same manner as the primary Toucan package. Both have a dependency on the Toucan.Core package, which contains the abstractions necessary for buiding and working with ORM adapaters as well as some other base infrastructure.

## Getting Started

After you have referenced Toucan in your project, it is as simple as following 3 guidelines:

1. Controllers that will make use of Toucan must implement IToucanController. An abstract base ToucanController is also provided if you would prefer. This provides a property collection and generic model getter method for accessing loaded models.
1. Use the LoadAndAuthorizeAttribute to specify which models to load and authorize by model type and action name.
1. Add Toucan services and configuration during ServicesConfiguration. Configuration currently is a work in progress and the Fluent API, while functional, is clunky and repetitive.
    1. See the sample app for adding services. As of now, the toucan filter must be add to MVC seperately from the rest of Toucan configuration. I plan to fix this so that AddToucan call wires up the filter as well.

The basic flow is:

1. Create your model, views and add a controller inheriting from ToucanController.
1. Add LoadAndAuthorize attributes to your controller to indicate which models to load. This is convention driven, and loads by the Id in the route.
1. Implement a role permission scheme during configuration. The AddToucan extension method takes a lambda which may use to call an abilities class that has a method for configuring permissions. See the sample app for a minor example.

A sample app is included in the sources that shows the basics of working with Toucan.

Toucan now supports nested resource loading and authorization. See the [wiki](https://github.com/EntropyZero/Toucan/wiki/Nested-Resources) for details.

## Roadmap

Right now there are 2 major items that needs to be addressed as I drive the project to its 1.0 release:

* A much improved permissions configuration story
  * Improve the Fluent API, or
  * Provide for some form of DSL/file spec for loading permission definitions
* Improved documentation and samples

There are some smaller features I want to add, such as an Authorize attribute that will authorize access to a model type when the authorization needs are not specific to the model instance, and some other nice to have support in model loading.

### Contributing

I'm happy to have help :-). If you want to contribute code, fork the repo, make your branch and send me a pull request. If you have feature ideas, or bugs,open an issue and I'll take it up from there.
