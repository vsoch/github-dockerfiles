# Veil

Veil is a .NET template renderer / view engine. It is designed to support many syntax parsers which sit on top of a single IL-emitting compiler.  
See [Veil.SuperSimple](https://github.com/csainty/Veil/tree/master/Src/Veil.SuperSimple) and [Veil.Handlebars](https://github.com/csainty/Veil/tree/master/Src/Veil.Handlebars) for examples of supported syntax.

### Design Goals

* Easy to install, configure and use in any project
* Fastest view engine available
* Support for explicit flush to aid in browser performance
* Mono support

### Not supported
Unlike Razor, Veil templates are not compiled with the full .NET compilers. This is part of what makes Veil so much easier to integrate and work with. The cost of this approach is that arbitrary code blocks are not supported.  
A purist may argue this is actually a good thing :) 


### Getting Started
You have two options for using Veil :-

1. If you are using [Nancy](https://github.com/NancyFx/Nancy) then install the [Nancy.ViewEngines.Veil](http://www.nuget.org/packages/Nancy.ViewEngines.Veil) package and your preferred syntax parsers e.g. [Veil.Handlebars](http://www.nuget.org/packages/Veil.Handlebars) or [Veil.SuperSimple](http://www.nuget.org/packages/Veil.SuperSimple)
2. Alternatively you can install and use any Veil syntax parser directly in any application. E.g.

````
Install-Package Veil.Handlebars

// Compile your template once with the chosen parser
var template = "Hello {{ Name }}";
var compiledTemplate = new VeilEngine().Compile<ViewModel>("handlebars", new StringReader(template));

--

// Execute your template as needed
using (var writer = new StringWriter()) {
    compiledTemplate(writer, new ViewModel { Name = "Bob" });
}
```` 

### Further Information

* [Try the Veil parsers in your browser](http://tryveil.com)
* [Getting Started with Nancy](http://blog.csainty.com/2014/06/veil-getting-started-nancy.html)
* [Getting Started Standalone](http://blog.csainty.com/2014/07/veil-getting-started-standalone.html)


### Builds
[![Build status](https://ci.appveyor.com/api/projects/status/cad383bewb58svi1/branch/master?svg=true)](https://ci.appveyor.com/project/csainty/veil/branch/master)

Pre-built binaries of the latest commit are always available at [https://ci.appveyor.com/project/csainty/veil/build/artifacts](https://ci.appveyor.com/project/csainty/veil/build/artifacts)
# Veil.SuperSimple

A [SuperSimpleViewEngine](https://github.com/grumpydev/SuperSimpleViewEngine) inspired syntax parser for [Veil](https://github.com/csainty/Veil).

Get it on nuget `Install-Package Veil.SuperSimple`

The SuperSimple parser is registered under the keys `supersimple`, `sshtml` and `vsshtml`.

You can experiment with the syntax online - [http://tryveil.com](http://tryveil.com)


### Syntax
Expressions in SuperSimple syntax all start with an `@` and are optionally terminated with a `;`. E.g. `@Model.Name` and `@Model.Name;` are equivalent. If your expressions has a natural separator such as a space, then the terminator is not needed.

### @Model.*

Access to your model is provided by the `@Model` expression. E.g.  
````
var model = new {
	Name = "Bob",
	Department = new {
		Name = "Sector 7G"
	}
}
````  
Hello `@Model.Name` - Hello Bob  
From `@Model.Department.Name` - From Sector 7G 

An expression of simply `@Model` references the model itself. E.g.  
````
var model = "World";
````  
Hello `@Model` - Hello World

To HTML-escape an expression, prefix it with a `!`  
````
var model = new {
	Content = "Dangerous <script>"
};
````  
See my `@!Model.Content` - See my Dangerous &amp;lt;script&amp;gt;

### @If.* / @IfNot.*
Conditionals are handled with the `@If` and `@IfNot` expressions. E.g.  
````
var model = new {
	Name = "Bob",
	IsAdmin = false
};
````  
`@Model.Name` is `@If.IsAdmin;`an Admin`@EndIf;``@IfNot.IsAdmin`a User`@EndIf` - Bob is a User  
In additional to boolean values, conditionals also support null-checking reference types. 

### @IfNull.* / @IfNotNull.*
Aliases exist for the `@IfNull` and `@IfNotNull` expressions. These are mapped to regular Veil conditionals which support null checking for non-booleans.

### @Each.* / @Current.*
Iteration is handled with the `@Each` expressions. Access to the current item in the iteration is provided through the `@Current` expression which supports the same syntax as `@Model` E.g.  
````
var model = new {
	Items = new [] { "Cat", "Dog" },
	Users = new [] {
		new User { Name = "Jim" },
		new User { Name = "Bob" )
	}
};
````  
`@Each.Items;@Current;@EndEach;` - CatDog  
`@Each.Users;@Current.Name;@EndEach;` - JimBob

### @Partial
Including another template is handled through the `@Partial` expression. Partials are loaded through the [IVeilContext](https://github.com/csainty/Veil/blob/master/Src/Veil/IVeilContext.cs) provdided to your [VeilEngine](https://github.com/csainty/Veil/blob/master/Src/Veil/VeilEngine.cs) instance. If you are executing without an `IVeilContext` then attempts to load partials will throw an exception.

````
var model = new {
	User = new {
		Name = "Bob"
	},
	Department = new {
		Name = "Sector 7G"
	}
};
var userTemplate = "Hello @Model.Name";
var deptTemplate = "From @Model.Name"; 
````  
`@Partial['userTemplate', User] @Partial['deptTemplate', Department]` - Hello Bob From Sector 7G

If you do not provided a second value `@Partial['Name']` then the whole model is passed to the partial.

### @Master and @Section
Master pages are handled through the `@Master` and `@Section` expressions.  
A master page is simply a template that has one or more names sections in it. E.g.  
````
// MyMasterPage.vsshtml
My header
@Section['Content']
My Footer
````  
To use this master page, you need to create a template where the first expression indicates to use this master page and then define each section.  
````
@Master['MyMasterPage']

@Section['Content']
My Content
@EndSection
````

The model you pass to your template is also passed to the MasterPage and can be accessed, You can also nest master pages many levels deep.  
You can not reuse section names in nested templates, if you wish to "inherit" a section you need to rename it in your intermediary master page.

### @Flush
Veil supports early flushing rendered content. Doing this allows the browser to start loading external assets such as CSS, JavaScript and images before the full page is loaded. You can trigger this anywhere in your templates with the `@Flush` expression.# Veil.Handlebars

A [Handlebars](http://handlebarsjs.com/) inspired syntax parser for [Veil](https://github.com/csainty/Veil).

Get it on nuget `Install-Package Veil.Handlebars`

The Handlebars parser is registered under the keys `handlebars` and `hbs`.

You can experiment with the syntax online - [http://tryveil.com](http://tryveil.com)

### Syntax
Expressions in Handlebars are wrapped in {{ and }}.

### Access your model - {{ }}

Access to your model is implicit in any handlebars expression.

````
var model = new {
	Name = "Bob",
	Department = new {
		Name = "Sector 7G"
	}
}
````  
`Hello {{ Name }}` - Hello Bob  
`From {{ Department.Name }}` - From Sector 7G 

Handlebars supports referencing the model of the parent scope with the `../` expression.

````
var model = new {
	Name = "Bob",
	Roles = new [] { "Admin", "User" }
}
````  
`{{#each Roles}}Hello {{../Name}} the {{this}}! {{/each}}` - Hello Bob the Admin! Hello Bob the User! 

### Disable HTML Escape - {{{ }}}

All handlebars expressions are HTML-escape by default. To disable this functionality you should wrap your expression with three braces instead.   
````
var model = new {
	Content = "Safe <b>Markup</b>"
};
````  
`See my {{{ Content }}}` - See my Safe <b>Markup</b>

### Conditionals - {{#if}} {{else}} {{/if}}
Conditionals are handled with the `{{#if}}` expression. E.g.  
````
var model = new {
	Name = "Bob",
	IsAdmin = false
};
````  
`@Model.Name is {{#if IsAdmin }}an Admin{{ else }}a User{{/if}}` - Bob is a User  
In additional to boolean values, conditionals also support null-checking reference types. 

### Conditionals - {{#unless}} {{/unless}}
An alternate form of conditional exists that renders its content when the expression evaluates false.  

````
var model = new {
	IsAdmin = false
};
````  
`{{#unless IsAdmin }}Please Login{{/unless}}` - Please login  


### Iteration - {{#each}} {{else}} {{/each}}
Iteration is handled with the `{{#each}}` expression. Access to the current item in the iteration is provided through the `{{this}}` expression. E.g.  
````
var model = new {
	Items = new [] { "Cat", "Dog" },
	Users = new [] {
		new User { Name = "Jim" },
		new User { Name = "Bob" )
	}
};
````  
`{{#each Items}}{{this}}{{/each}}` - CatDog  
`{{#each Users}}{{this.Name}}{{/each}}` - JimBob

If an `{{#each}}` block contains an `{{else}}` then that content will be rendered when there are not items in the collection being iterated.

````
var model = new {
	Items = new string[0]
};
````  
`{{#each Items}}{{this}}{{else}}NoItems{{/each}}` - NoItems  

### Scope - {{#with}}
You can scope a block in Handlebars with the `{{#with Name}} {{/with}}` expression. Any expressions within this scope block will use the object referenced by the block as their model.
````  
var model = new {
	User = new {
		Name = "Joe",
		Id = 1
	}
}; 
````  
`{{#with User}} {{Id}}: {{Name}}{{/with}}` - 1: Joe

### Response Flush - {{#flush}}
Veil supports early flushing rendered content. Doing this allows the browser to start loading external assets such as CSS, JavaScript and images before the full page is loaded. You can trigger this anywhere in your templates with the `{{#flush}}` expression.

### Partials - {{> partialName }}
Including another template is handled through the `{{> }}` expression. Partials are loaded through the [IVeilContext](https://github.com/csainty/Veil/blob/master/Src/Veil/IVeilContext.cs) provdided to your [VeilEngine](https://github.com/csainty/Veil/blob/master/Src/Veil/VeilEngine.cs) instance. If you are executing without an `IVeilContext` then attempts to load partials will throw an exception.

````
var model = new {
	User = new {
		Name = "Bob"
	},
	Department = new {
		Name = "Sector 7G"
	}
};
var userTemplate = "Hello {{ User.Name }}";
var deptTemplate = "From {{ Department.Name }}"; 
````  
`{{> userTemplate }} {{> deptTemplate }} - Hello Bob From Sector 7G`

Partials always inherit the current model context.

### Master pages - {{< masterName}} / {{body}}
Handlebars supports single-sectioned master pages using the `{{< masterName}}` expression. The named template will be loaded and the rest of the content from the original template will be inserted into the master template in place of the `{{body}}` expression.  

````
var model = new {
	Name = "Joe"
};
var master = "Hello {{body}}, Have Fun!"; 
````  
`{{< master}}{{Name}} - Hello Joe, Have Fun!`


### Comments {{! ... }}
You can add comments to your template with the `{{! your comment here }}` expression.  
These are simply ignored and removed during compilation.

### Whitespace control - {{~Foo~}}
Handlebars supports selectively trimming templates whitespace by adding `~` markers in your expressions.

````  
var model = { Name = "Joe" };

<p>
	{{~Name~}}
</p>

<p>Joe</p>
````

Placing a `~` at the start of the block trim the whitespace preceeding the block. Placing a `~` at the end of a block trims whitespace following the block.  
Use the features to generate smaller markup for sending over the wire.# Nancy.ViewEngines.Veil

A ViewEngine for [Nancy](http://nancyfx.org/) which detects installed Veil parsers and uses them to renders views with matching extensions.

Get it on nuget `Install-Package Nancy.ViewEngines.Veil`

**Note:**  
In addition to installing this package, you need to install one or more syntax parsers for Veil.

* [Veil.Handlebars](https://github.com/csainty/Veil/tree/master/Src/Veil.Handlebars)
* [Veil.SuperSimple](https://github.com/csainty/Veil/tree/master/Src/Veil.SuperSimple)


### Further Reading

* [Getting Started with Nancy](http://blog.csainty.com/2014/06/veil-getting-started-nancy.html)
