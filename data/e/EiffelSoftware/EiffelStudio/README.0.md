Graphical front end for Eweasel Readme
--------------------------------------

This front end for the eweasel command-line test execution suite is fairly simple.  To
run eweasel in graphical mode compile the ace file at $EWEASEL/compilation/eweasel.windows.gui.ace
(where $EWEASEL refers to the eweasel installation directory on your machine).

Once running use the 'Configuration' notebook page to set the required eweasel configuration
options before attempting to run any tests.  You can save the current configuration for quicker
retrieval next time.  If the configuration is correct you can load a test catalog file and the run
the tests and output will appear in the text box below.

.NET
----
To compile and run the tests for .NET make sure you have a 'dotnet' directory in 
$ISE_EIFFEL/studio/spec and select the dotnet option in the configuration part of the interface.  WEL Tutorial
------------

This directory contains the Eiffel projects corresponding
to each steps in the tutorial.

Directory `step1': Creating an application
Directory `step2': Defining a main window class
Directory `step3': Drawing text in a window
Directory `step4': Drawing lines in a window
Directory `step5': Changing line thickness
Directory `step6': Repainting a window
Directory `step7': Adding a menu
Directory `step8': Storing the drawing in a file

This tutorial is also available on our WEB site at:
http://www.eiffel.com/doc/manuals/technology/wel/tutorial/index.html
This example can only be compiled with the experimental version of EiffelStudio.
This is an example how to use external C code from Eiffel code.

The binaries can be rebuilt from the provided sources by running

	finish_freezing -library

in the directory "Clib" from your EiffelStudio installation.CALCULATOR example

Type h for help.

y: To add an amount of years
d: To add an amount of days
s: To set the new year, the new month and the new day
w: To add an amount of weeks
m: To add an amount of month
q; exit
The Dynamic External Shared Call (DESC) mechanism provides a way
to call dynamically external functions from a dynamic library.
The current implementation supports 32-bit Windows DLLs and
works only with the Microsoft Visual C++ compiler.
For more details, see ``ISE Eiffel: The environment'', DESC section.

Do not forget to put `ise_desc.dll' in your path.
This folder contains all the tests sample of the EiffelVision demo applicaiton.

To add more tests, simply add a new test class under one of the subfolder. Each subfolder's name
corresponding to an EiffelVision widget's name without the `EV_` prefix in lower case.
ROC CMS Documentation
=====================

[TOC]

## Overview

**ROC CMS** stands for "REST On CMS", however, until now, no particular focus was done on the REST API approach, and so far a more pragmatic approach dominated.

Part of the design is inspired by Drupal (blocks, hooks, Role-based access control, ...), and other parts related to Eiffel. Priorities, modules and related have been driven by concrete need, in order to fulfill the https://eiffel.org/ websites. Also a contribution (as student projects, or others) helped build various modules or functionality.

Currently, **ROC CMS** is a library or **framework** that provides components, tools and resources to build a CMS (Content Management System). It is not currently a CMS product, one can install and customize without any code.

Thus, it will be interesting for people willing to build a website using **Eiffel**. This will enable to reuse other Eiffel components, better integration with other Eiffel projects, and of course benefit from all the goodies of the Eiffel technologies (Eiffel language, DbC, re-usability, portability, IDE, debugger,...).

It depends on the **Eiffel Web Framework** (known as "Eiffel Web" or "EWF"), and thus can be executed as standalone, or CGI, libFCGI mode on Apache2 for instance, and on any Windows or Linux platform).

The main notions are:
- CMS Execution
- CMS APIs
- CMS Response
- CMS Modules
- CMS Hooks
- CMS Theme, blocks, links, ...

Those points will be described later in appropriated sections.

## Setup


The ROC CMS source is available either with the latest EiffelStudio release under the locations:
- $ISE_LIBRARY\unstable\library\web\cms
- or from github project https://github.com/EiffelWebFramework/ROC branch v0 for now.
```
git clone https://github.com/EiffelWebFramework/ROC -b v0
```

Note that if you use the source code from the github repository, you will need to use the latest release of EiffelStudio as it relieѕ on recent version of various libraries such as EWF, sqlite3, ....
And using the "master" branch, even the trunk version of EiffelStudio libraries. So for now, we encourage you to use the ROC CMS shipped with your EiffelStudio.

Once you have the source code, you should compile project <code>cms/example/demo/demo-safe.ecf</code> target "demo_standalone".
```
# from Command line
cd example
cd demo
ec -config demo-safe.ecf -c_compile -finalize
cp ./EIFGENs/demo_standalone/F_Code/demo.exe demo.exe
demo.exe
# or launch EiffelStudio, and open that project, compile and execute it inside the debugger for instance.
````

This demo includes all the official ROC CMS modules, files, and use libsqlite3 as default storage engine. So you should be able to execute it easily. The **standalone** target is configured to listen on port 9090 by default. (Mostly to avoid conflict on other app that my listen on port 80 or 8080).

In the directory <code>site</code> you will find all the expected files that should be in the root directory.
* config/ : it contains the various configuration files, especially the **cms.ini**.
* modules/ : files associated with each installed ROC CMS module.
* scripts/ : common scripts used mainly to initialize SQL databases.
* themes/ : folder containing the available ROC CMS themes.
* files/ : folder containing files available from the ROC CMS app.
* And also demo.ini that contains the settings for the web launcher, (in our case, the standalone Eiffel server), such as port_number.

Now that you know how to compile, execute, and see the related configuration files, let's describes the main notions of the ROC CMS, first from 
* an admin point of view (dev using ROC CMS to build its site),
* and then from a developer point of view (in case you want to contribute to ROC CMS).

## Usage

### Main entries
As a CMS administrator, you will need to setup your CMS application (here the demo example). For this purpose, the main entry points are the CMS_EXECUTION interface, and then the <code>site/</code> files (configuration, themes, templates, ...).

### CMS initialization/Execution
The `CMS_EXECUTION` interface is deferred, and your CMS application needs to inherit from it and define `setup_storage`, `initial_cms_setup` and `setup_modules`. See for instance `DEMO_CMS_EXECUTION`.

So, the descendant of `CMS_EXECUTION` (`DEMO_CMS_EXECUTION` in the example), is creating the `CMS_SETUP`, declares the available **storage** builders (for persistency), and declares the available **modules**.

#### Persistence/Storage
Depending on the **configuration**, the CMS engine will instantiate and use a specific **CMS_STORAGE** (the default is based on `Eiffel sqlite3`, otherwise `EiffelStore+MySQL` and `EiffelStore+ODBC` are available). The storage solution is used to implement the persistence layer, and thus store and load CMS data to disk, or database.

The CMS provides, for now, storage based on
* EiffelStore + MySQL
* EiffelStore + ODBC (could be used for MySQL, sqlite, SQLserver, ...)
* Eiffel sqlite3 : that one is the default storage, since it is convenient for testing, but it is recommended to use EiffelStore+MySQL in production CMS site.
A typical implementation of <code>setup_storage</code> is:
```eiffel
	setup_storage (a_setup: CMS_SETUP)
		do
			a_setup.storage_drivers.force (create {CMS_STORAGE_SQLITE3_BUILDER}.make, "sqlite3")
--			a_setup.storage_drivers.force (create {CMS_STORAGE_STORE_ODBC_BUILDER}.make, "odbc")
		end
```
And the CMS decides which storage should be used. It depends on the application configuration. See the **configuration** section.

Those data could be user information (login, email, password, ...), custom values, logs, emails, path aliases, ... and any data modules may need to store (for instance node content, for the `node` module.)

#### Modules

The `setup_module` is used to declare available **modules** (instances of `CMS_MODULE` effective types).
The modular design provides a simple way to extend or alter the CMS functionalities/behaviors.
Most of the CMS features are implemented by modules, and each module relies on the core of the CMS core.
This **core** contains the `CMS_API`, `CMS_USER_API`, and various internal mechanisms such as mailer, logger, ...

Use `setup_module (a_setup: CMS_SETUP)` to customize the `CMS_SETUP` object created by `initial_cms_setup`.
For your convenience, ROC CMS provides a `CMS_DEFAULT_SETUP` that import configuration from `site/config/cms.ini`

So far, what you need to remember is `CMS_EXECUTION` class and descendants are used to set up the ROC CMS application, for storage, modules, and also how to load configuration.

Note that a module can have 3 states:
- not installed,
- installed and enabled,
- installed and disabled.

At first, to install the modules, open your browser at location `https://hostname:port/admin/install` and click the associated button.
(Note: for new module addition, you also need to install them, using the same link, in the future, there will be a proper module management interface, in the admin front-end.)

To enable or disable a module, you will need to use the `cms.ini` configuration file, please see the **configuration** section.

Existing modules:
- **admin**: basic administration pages, to manage modules, roles, permissions, users, caches, ... (note: it is still very basic, and need effort to improve it.)
- authentication modules based on **auth**:
    - **basic_auth**: account signing using basic HTTP Authorization solution
    - **oauth20**: sign using a thirdparty OAuth2.0 account (such as Google, Facebook, github, ...)
    - **openid**: sign using an OpenID account.
- **node**: the base of node management, include **Page** content type.
- **blog**: extends the **node** module with a **blog** content type.
- **recent_changes**: compute recent changes of CMS (integration with **node** management, and any modules that implement the `CMS_RECENT_CHANGES_HOOK`).
- **feed_aggregator**: aggregate one or many feeds (rss, atom, ...), and provide associated pages or blocks.
- **google_search**: provides search facilities using the Google Custom Search API.

### Configuration
When `CMS_DEFAULT_SETUP` is used, the CMS configuration is loaded from `site/config/cms.ini`.
That file contains a few sections:
- **site**: to set the `name`, `email` and the name of the `theme`. (See "Themes" section pour information.)
- **layout**: the application layout (or environment) can precise the `root-dir`, `themes-dir`, `modules-dir`. If not defined, the values are computed from Current working directory.
- **mailer**: the CMS can send email notification for various reasons, such as new users, or reset password functionalities, ... In this section, you can use
    - `smtp` settings to precise an SMTP server (+ port), 
    - or `sendmail` to use an external script using the sendmail usage,
    - or just an `output` file such as @stderr, or a path to a file on disk.
- **modules**: used to enable or disable modules.
    - `*=on`  -> modules are enabled by default
    - `*=off` -> modules are disabled by default
    - Note the default value is `on`
    - For each module, this can be overwritten with  `module_name=on|off`
- **blocks**: settings for blocks (See Themes, Blocks sections for more information on the block). A few parameters are available to customize blocks. The general form is `block-name.param=value` (note that "foo.bar" is a value block name.)
    - `block-name.region`: assign the block `block-name` to a specific region. A block can be assigned to **only one region**.
    - `block-name.title`: used to overwrite the block title (with <none> , the title is hidden).
    - `block-name.weight`: used to order blocks in the same region (blocks with lower weight goes first).
	- `block-name.expiration`: used to provide a basic cache system based on expiration. The value is a number of seconds before the cache expires (-1: never expires, 0: never cache, n: cache expires after `n` seconds).
    - `block-name.condition`, or `block-name.conditions[]`: include `block-name` only under specific condition(s). The condition can be 
        - `is_front`: which is True only for the front page, usually at url "/"
        - `path:foo/bar`, `path:foo/*/bar`: True only for CMS location matching the patterns after "path:"
        - `<none>`: related block is disabled.
        - *note: There can be multiple conditions processed as any of the conditions (i.e: "or").*
    - `block-name.options[varname]: pass a table of options `varname => value` to the related block. This can be used to pass parameters for block builder (for instance, recent_changes modules accept parameters "size" to know how many changes should be included.)
    - To be able to include a block content into multiple region, it is possible to use aliases feature. For instance `&aliases[new_block]=block-name`, in this case, a `new_block` is declared, and it has same content as `block-name`, on this alias, the parameters `region, condition(s), title, weight` are supported, but not `options[]`.
- **admin**: various admin related settings such as
    - `installation_access` which accepts 3 values: "all", "none" or "permission", to precise who has access to the modules installation page; either "all" for anyone, "none" to disable installation of new modules, or "permission" to use the CMS permissions solution to determine if the current user can install a new module.
    
Then, the configuration `cms.ini` can also define other parameters, and sections, that may be used by specific modules.
Note it is also possible to include another ini file with instruction `@include=path-to-file.ini`.

Check the `example/demo/site/cms.ini` for example.

### User management
The CMS core includes the notion of user, via interface `CMS_USER`, which has an id, a name, a password, ... and profile. Without any module, the CMS does not include any mean to authenticate, but still the CMS has the support for user management, and permissions system for current user. To be able to sign into the CMS, the site should include the module `auth`, and one or many of:
- `basic_auth`: authentication using the HTTP Authorization header.
- `oauth20`: being able to sign with an OAuth2.0 account (such as Google, Facebook, ...)
- `OpenID`: being able to sign with an OpenID account.

Whatever authentication solution is used, when a user is signed-in, there is an instance of `CMS_USER` representing the associated CMS user account.

There is a predefined user `admin` who is the administrator of the CMS, and by definition, this **admin** has all the permissions. It is initialized by default with username `admin` and password `istrator#`.

The access control is role-based permissions system. This means, a user can have one or many *roles*, and each *role* includes a list of *permissions*.
There are two built-in roles:
- **anonymous**: when no user is signed in (typically anonymous visitors).
- **authenticated**: when a user is signed in the CMS.
With those 2 built-ins roles, and any custom role the admin will create, it is possible to give specific permissions, to a group of users. 
The CMS core defines a few permissions, and each module can also define their own permissions, for instance: "view any page", "create page", "edit page", "delete page", "clear cache", "install modules", ... (when the administrator is signed-in, go to url `/admin/role/1/edit` to see all the available permissions).

### Modules
A module is the way to extend the CMS engine.
First via the inherited `CMS_MODULE` interface that enables a module to:
- have a custom `install` and `uninstall` procedure by redefining the related routines.
- add its **routes**  via `setup_router`. (i.e associated url or template of url with a specific request handler).
- register itself to hooks via `register_hooks`.
- declare new permissions by redefining `permissions`.
- provide a specific module api by redefining `module_api`.
- add its **filters** by redefining `filters`.

Using the `hooks` system, a module can be deeply integrated with the CMS engine, and even alter behaviors (for instance, add link, add css, javascript, ...). See related developer documentation on hooks.

It is simple to create your own modules (check the developer documentation).
The ROC CMS library provides a few modules for now, for instance: basic_auth, oauth20, openid, node, blog, feed_aggregator, recent_changes, google_search, ... and others (the list keeps growing...).

**Reminder**: to include a module to your CMS site, you need to 
- include the associated .ecf file in your CMS site .ecf file.
- and also declare them in your descendant of CMS_EXECUTION.
- copy the eventual resources, configuration, ... files in the corresponding `site`.
Note: a tool **roc** is under development to ease such operations, for now it only copies needed files from module to site location. In the future, it should also update .ecf files, associated CMS_EXECUTION effective class.

### Themes
When talking about CMS, a major topic is how a request is rendered in a web browser. Here comes the notion of **theme** which is a collection of templates, accepting various values as input (including the content of the blocks), and renders as an html5 page. It also includes various assets such as css, javascript, icons, images, ...
The ROC CMS theming is inspired by Drupal, with the notion of **region** and **block**.

Note: for now, there is no simple "theme" module or similar, and the common way to start your CMS site is to copy an existing project such as the one available with the demo example (i.e: copying the source code, but also the `site` folder).

Currently the default theme  of the demo example `SMARTY_CMS_THEME` is based on Eiffel **smarty** template library (Check [smarty doc](https://svn.eiffel.com/eiffelstudio/trunk/Src/contrib/library/text/template/smarty/README.md) for syntax and functionalities).

The layout of a CMS web page has predefined area called **regions**. The Eiffel CMS uses the same default regions as Drupal, so let's see them in the following image.

```
		+----------------------------------------------------------+
		|                        Page_top                          |
		+----------------------------------------------------------+
		|                         Header                           |
		+---------------+-------------------------+----------------+
		|               |      Highlighted        |                |
		| Sidebar_first +-------------------------+ Sidebar_second |
		|               |          Help           |                |
		|               +-------------------------+                |
		|               |                         |                |
		|               |         Content         |                |
		|               |                         |                |
		+---------------+-------------------------+----------------+
		|                         Footer                           |
		+----------------------------------------------------------+
		|                      Page_bottom                         |
		+----------------------------------------------------------+
```

The regions available for a theme, are defined in a configuration file `theme.info` located in the theme directory. For example:
```
name=default_theme
engine=smarty
version=0.1
regions[page_top] = Top
regions[header] = Header
regions[content] = Content
regions[highlighted] = Highlighted
regions[help] = Help
regions[footer] = Footer
regions[sidebar_first] = first sidebar
regions[sidebar_second] = second sidebar
regions[page_bottom] = Bottom
```
Note: the value for each region is the human readable region name.

Note the regions may be disposed with other layout (two sidebars on the left, or right, ... and so on), responsive design or not, and so on. But on the CMS side, a *block* can be inserted into a *region*, and depending if the region is included in the theme, the related block content will be displayed or not.
To sort *block* inside a region, the CMS is using the `weight` property (that can be set via code, and/or overridden via configuration, i.e: `cms.ini`).
This is how a site can support many themes, using the region as content holders, and theme for the layout and style.

Internally the block contents are stored in the values associated with each region.
The theme also has access to specific `values` such as
- `site_url`: the absolute url of the CMS website.
- `host`: the host name.
- `is_https`: True if the connection is using https://
- `user`: contains the username of the signed user, if any.
- `site_title`: site title.
- `page_title`: per page title.
- and also `page: CMS_HTML_PAGE` which represents the CMS page to render with the theme.
    - `page` provides values via expression, such as `$page.type`, `$page.is_front`, `$page.is_https`, `$page.title`, ...
    - and also a smart expression for region via `$page.region_xyz` for region `xyz` if any, ... (note the region are also available with expression like `$region_xyz` or `$page.region_xyz` ...)

==Note for developers: internally, the deferred class `CMS_RESPONSE` provides an abstraction to render the response for the request using the **theme**, in fact, the theme is controlled by the CMS_RESPONSE implementation (to set value, build expected theme, and finally render as html).==

### Blocks
As previously said, a region holds smaller piece of content called blocks.
Blocks hold chunks of content, like the user login form, navigation menu, information for the footer, or anything provided by each module.
For instance the `feed_aggregator` module provides a block to display the latest elements of a aggregated feed.

Currently there are different kind of `CMS_BLOCK`:
- `CMS_CONTENT_BLOCK`: it holds a simple text to render as it is on the page.
- `CMS_MENU_BLOCK`: it holds a `CMS_MENU` as a collection of `CMS_LINK` generally used to hold a menu, or set of links such as navigation or management menus.
- `CMS_SMARTY_TEMPLATE_BLOCK`: it holds a simple text to render as it is in the page.

Internally, there are two other kinds of block:
- `CMS_ALIAS_BLOCK`: being the alias of another block, but with specific properties.
- `CMS_CACHE_BLOCK`: there is a simple cache solution for blocks, based on expiration. See the configuration section to know how to define the expiration for a block.

For now, creating a block is only possible via block, an evolution of ROC CMS should allow the administrator to add new block without coding.

### Persistence
The persistence or storage layer is used by the CMS to store custom values, path aliases, logs, emails, user information, but it is also used by module (unless a module wants to use its own persistence solution, disk, cloud, ...).

Currently, there are only SQL based implementations of that `CMS_STORAGE`, but nothing prevents to implement it with other solutions (plain text file, NoSQL db, ...).
The current implementation are using either:
- EiffelStore + MySQL: recommended for production, however Eiffel MySQL requires to configure your environment by setting, for instance MYSQL variable on Windows, and MYSQLINC on Linux.
- EiffelStore + ODBC: via ODBC, there is a large range of available database (MySQL, SQLite, SQLserver, ...), but it requires to set up your environment (for instance install sqliteODBC driver to use SQLite database).
- Eiffel sqlite3 wrapper: it is very convenient for development, but maybe not recommended for production websites. It does not require any environment setup, so this is a simple solution to build tests for instance.

In practice, how to use a storage or another?
The project needs to include the expected storage, the following instructions explains how to include sqlite3, EiffelStore+ODBC and EiffelStore+MYSQL storage.
1. First the associated .ecf file need to be included in your project file (.ecf)
For instance
```xml
<library name="persistence_sqlite3" location="$ISE_LIBRARY\unstable\library\web\cms\library\persistence\sqlite3\sqlite3-safe.ecf"/>
<library name="persistence_store_odbc" location="$ISE_LIBRARY\unstable\library\web\cms\library\persistence\store_odbc\store_odbc-safe.ecf"/>
<library name="persistence_store_mysql" location="$ISE_LIBRARY\unstable\library\web\cms\library\persistence\store_mysql\store_mysql-safe.ecf"/>
```
2. Then in the descendant of `CMS_EXECUTION`, in the demo `DEMO_CMS_EXECUTION`, see the code of `setup_storage`:
```eiffel
setup_storage (a_setup: CMS_SETUP)
	do
		a_setup.storage_drivers.force (create {CMS_STORAGE_SQLITE3_BUILDER}.make, "sqlite3")
		a_setup.storage_drivers.force (create {CMS_STORAGE_STORE_MYSQL_BUILDER}.make, "mysql")
		a_setup.storage_drivers.force (create {CMS_STORAGE_STORE_ODBC_BUILDER}.make, "odbc")
	end
```

3. And finally, in the configuration file `site/config/demo.json` (in fact, the executable name + ".json"), define the driver and environment of the datasource. For instance the following code defines **sqlite3** as default CMS storage, and environment *sqlite3* that defines the path of SQLite database as "site/database.sqlite3". Note the way to declare sqlite with ODBC, mysql with ODBC, or mysql directly with EiffelStore.
```json
{
	"database": {
		"datasource": {
			"driver": "sqlite3",
			"environment": "sqlite3",
		},
		"environments": {
			"sqlite3": {
				"connection_string":"Database=./site/database.sqlite3;"
			},
			"odbc-sqlite": {
				"connection_string":"Driver=SQLite3 ODBC Driver;Database=./site/database.sqlite;LongNames=0;Timeout=1000;NoTXN=0;SyncPragma=NORMAL;StepAPI=0;"
			},
			"odbc-mysql": {
				"connection_string":"Driver=mysql ODBC Driver;Server=localhost;Port=3306;Database=roc;Uid=roc;Pwd=roc;"
			},
			"mysql": {
				"connection_string":"Driver=mysql;Server=localhost;Port=3306;Database=roc;Uid=roc;Pwd=roc;"
			}
		}
	}
}
```
To use EiffelStore+MySQL, just change the "driver" to be "mysql" and "environment" to "mysql". The connection string for server database defines the credentials with "Uid" and "Pwd".

### How to run the CMS site?
As any Eiffel Web application (EWF), it can be executed as 
- **standalone**: using Eiffel standalone httpd server included in the "standalone" connector, and then no setup is needed.
- **CGI** or **libFCGI** server: using, for instance, Apache2. Please refer to the Eiffel Web Framework documentation.

### Conclusion
At this point, you know enough to build and administrate a ROC CMS site.
However, for a real site, it is likely that you will need to build your own modules, you will learn how doing that in the Developer Documentation.

***
## Developper Documentation

This diagram shows the main interfaces, they will be described in this documentation, but for now, it introduces those class names.


![Diagram](img_diagram.png)


### CMS APIs
An instance of CMS_API is available either via argument, or via attribute / function of various CMS components.
It provides routine specific to the ROC CMS engine (access to setup, modules, logs, custom values, ...).

### CMS Hooks
Hooks is a mechanism which provides a way for modules to interact with each other and extending blocks of the current CMS.

- [CMS_HOOK](../library/src/hooks/cms_hook.e): deferred class CMS_HOOK is a marker interface for CMS Hook
- [CMS_HOOK_AUTO_REGISTER](../library/src/hooks/cms_hook_auto_register.e): when inheriting from this deferred class, the declared hooks are automatically registered (note only the CMS core hooks are supported, as opposed to hook a module may propose). Otherwise, each descendant has to register itself to the associated hook manager.
- [CMS_HOOK_BLOCK](../library/src/hooks/cms_hook_block.e): it provides a way to declare and build blocks.
- [CMS_HOOK_FORM_ALTER](../library/src/hooks/cms_hook_form_alter.e): it provides a way to alter a web form `CMS_FORM`.
- [CMS_HOOK_MENU_ALTER](../library/src/hooks/cms_hook_menu_alter.e): it provides a way to alter a menu, and thus add or remove a link. This is how a module can add a link into a specific `CMS_MENU`.
- [CMS_HOOK_MENU_SYSTEM_ALTER](../library/src/hooks/cms_hook_menu_system_alter.e): similar to CMS_HOOK_MENU_ALTER, but on built-in menu, such as management, navigation menus, and other.
- [CMS_HOOK_VALUE_TABLE_ALTER](../library/src/hooks/cms_hook_value_table_alter.e): it provides a way to alter the values table for a response (i.e: inserting custom values, or even override existing values).
- [CMS_HOOK_EXPORT](../library/src/hooks/cms_hook_export.e): it provides a simple export solution for each module. Typically used to archive data associated with a module, for instance for backup purpose. In the future, a `CMS_HOOK_IMPORT` should also be available, and it would allow importing data exported by `CMS_HOOK_EXPORT`.
- and for more hooks ... please check descendants of `CMS_HOOK`.

### Custom Module
How to build a new module?
A module is usually developed as an Eiffel library, and provide one or many implementations of `CMS_MODULE`.
It has to set or implement:
- **name**: a unique name identifying the module
- **description**: a human text to describe the purpose of the module, it will mainly be used by the administration front-end.
- **package**: put the current module into a package, mainly for admin front-end.
- **version**: version information
- **dependencies**: defines dependencies on other modules.
- **permissions**: defines permissions used by the modules (mainly for admin front-end)
- **setup_router**: associate routes with request handlers (declare various url or url template and associated request handler).
- **filters**: similar to routers setup, but for WSF Filters (See EWF documentation for more details).
- **register_hooks**: register current module with various hooks if needed.

A module can also redefine `install` and `uninstall`. This could be used during installation to create new database tables, or anything needed by the module, or clean similar resources when being uninstalled.

In addition, a module can also implement `module_api: detachable CMS_MODULE_API` in order to be integrated easily with other modules (see for instance the CMS_NODE_API defined in **node** module).

Please have a look at the [tutorial](tutorial.md) page.

## References
For the interface references, please have a look at the [ROC CMS source code](https://github.com/EiffelWebFramework/ROC).

***
*(last modified: Nov/17/2015 by Jocelyn.)*
Hints to run the ABEL tests in EiffelStudio:

- When executing tests using AutoTest, remember to select the option: Number of tests that can run in parallel: 1
You find this option by clicking the green little arrow in the AutoTest menubar (in the Autotest window) and selecting preferences.

- If a test executed together with others fails, try to execute it alone (this may be due to multi-threading issues of AutoTest)

- If an unexpected error occurs, close EiffelStudio and clean-compile.  

- For the MYSQL tests, write your name and password in PS_MANUAL_TEST_MYSQL at the bottom.

- For SQLite tests, write the file name in PS_MANUAL_TEST_SQLITE.sqlite_file.

Notice that:

- The following tests fail at 25.8.2012 because the corresponding code has not been implemented yet:

-- PS MANUAL TEST IN MEMORY:
--- test object graph read setting
--- test transaction dirty
--- test transaction lost
--- test transaction repeatable read

-- PS MANUAL TEST MYSQL
--- test collections mysql

- The  following tests should pass after uncommenting the retry statement at the end of CRUD_EXECUTOR.handle_error_on_action, but they don't:

-- PS MANUAL TEST MYSQL
--- test transaction cleanup
--- test transaction dirty
--- test transaction lost
--- test transaction repeatable read 


	-----------------------------
	--       IN-PROGRESS       --
	-----------------------------
	-- USE AT YOUR OWN RISK 	--
	-- author: jfiat@eiffel.com --
	-----------------------------

Overview: How to use git-svn with EiffelStudio subversion repository  

== Usign git-svn on Eiffelstudio subversion repository ==
The following instruction is to "clone" the svn repository of eiffelstudio,
but only the trunk, and from recent revision (otherwise ... it will take for
ever, the full svn repository is huged ...)

  mkdir trunk.git
  cd trunk.git

Create the git local repository from svn repository
  svn cat https://svn.eiffel.com/eiffelstudio/trunk/.git-svn/users.txt > users.txt
  git svn init https://svn.eiffel.com/eiffelstudio/trunk 
  git svn --authors-file=users.txt fetch -r 86254 

The previous command will download the full source code related to revision
86254 and then, it will fetch all the more recent revisions incrementally.
Note: you can fetch from older revision, if you want to have older history. A
good habit would be to fetch from the revision of previous release.


Once you get at least revision 86254
You can use the committed .git-svn/users.txt file
Clean temporary users.txt, to use a better solution, see 2 lines below
  del users.txt

For later usage, associate the svn author with real users
  git config --local --add svn.authorsfile .git-svn/users.txt

If you don't have this folder .git-svn , you might have done something bad

then to update, do 
  *** Windows ***                |   *** Linux ***                                       
  echo Stash                     |   echo Stash
  @call git stash                |   git stash
                                 |   
  echo Rebase                    |   echo Rebase
  @call git svn rebase           |   git svn rebase
                                 |   
  echo Apply Stash               |   echo Apply Stash
  @call git stash apply          |   git stash apply
  echo Clear Stash               |   echo Clear Stash
  @call git stash clear          |   git stash clear

== Map users committers ==
(note: if you followed previous instructions, you should already have done the following operations)
To map subversion user with git user (name+email), you should use the following file users.txt

 git config --local --add svn.authorsfile .git-svn/users.txt

if git svn complains about unknown users, you need to update users.txt with missing author(s) and relaunch your git svn command

== Using submodules to mimic svn:externals ==

=== ejson ===
 git submodule add -b trunk_ise git://github.com/Eiffel-World/ejson-svn.git Src/contrib/library/ejson

=== gobo ===
 git submodule add git://github.com/Eiffel-World/gobo.git Src/library/gobo/svn
 eventually git submodule add -b last_svn_commit git://github.com/Eiffel-World/gobo.git Src/library/gobo/svn

=== freeELKS ===
 git submodule add git://github.com/Eiffel-World/freeelks-svn.git .git-svn/submodules/freeelks
* On Windows 
 Require: junction installed (see: http://www.sysinternals.com and look for File and Disk utilities > junction)
 cd Src\library\base
 junction elks ..\..\..\.git-svn\submodules\freeelks\void_safe\library

* On Linux
 cd Src/library/base
 ln -s ../../../.git-svn/submodules/freeelks/void_safe/library elks

== Updating ==
To include the submodules in the update operation, you can use the following
script

  *** Windows ***                       |   *** Linux ***                                       
  echo Stash                            |   echo Stash
  @call git stash                       |   git stash
                                        |   
  echo Rebase                           |   echo Rebase
  @call git svn rebase                  |   git svn rebase
  echo Update submodules                |   echo Update submodules
  @call git submodule update            |   git submodule update
  @call git submodule foreach git pull  |   git submodule foreach git pull
                                        |   
  echo Apply Stash                      |   echo Apply Stash
  @call git stash apply                 |   git stash apply
  echo Clear Stash                      |   echo Clear Stash
  @call git stash clear                 |   git stash clear


== Miscellanious ==
=== Windows instructions to create your git local repository ===
	set TMP_REV_GIT_SVN=86254
	set TMP_REV=%TMP_REV_GIT_SVN%
	mkdir trunk.git
	cd trunk.git
	svn cat -r %TMP_REV_GIT_SVN% https://svn.eiffel.com/eiffelstudio/trunk/.git-svn/users.txt > users.txt
	git svn init https://svn.eiffel.com/eiffelstudio/trunk 

	git svn --authors-file=users.txt fetch -r %TMP_REV% 
	del users.txt
	git config --local --add svn.authorsfile .git-svn/users.txt

	git stash
	git svn rebase
	git submodule update
	git submodule foreach git pull
	git stash apply
	git stash clear

	git submodule add git://github.com/Eiffel-World/gobo.git Src/library/gobo/svn
	git submodule add -b trunk_ise git://github.com/Eiffel-World/ejson-svn.git Src/contrib/library/ejson
	git submodule add git://github.com/Eiffel-World/freeelks-svn.git .git-svn/submodules/freeelks
	cd Src\library\base
	junction elks ..\..\..\.git-svn\submodules\freeelks\void_safe\library

* note: if you copy that into a script, you might need to prepend the svn and git commands with  "@call "

=== Linux script ===
 Adapt the Windows script for your shell, this is pretty straight forward
 for instance with bash
	TMP_REV_GIT_SVN=86254
	TMP_REV=$TMP_REV_GIT_SVN
	mkdir trunk.git
	cd trunk.git
	svn cat -r $TMP_REV_GIT_SVN https://svn.eiffel.com/eiffelstudio/trunk/.git-svn/users.txt > users.txt
	git svn init https://svn.eiffel.com/eiffelstudio/trunk 

	git svn --authors-file=users.txt fetch -r $TMP_REV 
	rm users.txt
	git config --add svn.authorsfile .git-svn/users.txt

	git stash
	git svn rebase
	git submodule update
	git submodule foreach git pull
	git stash apply
	git stash clear

	git submodule add git://github.com/Eiffel-World/gobo.git Src/library/gobo/svn
	git submodule add -b trunk_ise git://github.com/Eiffel-World/ejson-svn.git Src/contrib/library/ejson
	git submodule add git://github.com/Eiffel-World/freeelks-svn.git .git-svn/submodules/freeelks
	cd Src/library/base
	ln -s ../../../.git-svn/submodules/freeelks/void_safe/library elks


Examples ...
Filter example

To test the example, you can just run in a terminal:
> curl -u foo:bar http://localhost:9090/user/1 -v
Restbuck Eiffel Implementation based on the book of REST in Practice
====================================================================
This is an implementation of CRUD pattern for manipulate resources, this is the first step to use
the HTTP protocol as an application protocol instead of a transport protocol.

Restbuck Protocol
-----------------

* Method `POST` with URI `/order` : Create a new order, and upon success, receive a Locationheader specifying the new order's URI.
* Method `GET` with URI-template `/order/{orderId}` : Request the current state of the order specified by the URI.
* Method `PUT` with URI-template `/order/{orderId}` : Update an order at the given URI with new information, providing the full representation.
* Method `DELETE` with URI-tempalte `/order/{orderId}` : Logically remove the order identified by the given URI.

Resource Represenation
----------------------
The previous tables shows a contrat, the URI or URI-template, allows us to indentify resources, now we will chose a 
representation, for this particular case we will use JSON.

Note: 
1. *A resource can have multiple URIs*.
2. *A resource can have multiple Representations*.

RESTBUCKS_SERVER
----------------
This class implement the main entry of our REST CRUD service, we are using a default connector (Standalone Connector, 
using a WebServer written in Eiffel).
We are inheriting from `WSF_ROUTED_SKELETON_EXECUTION`, this allows us to map our service contrat, as is shown in the previous
table, the mapping is defined in the feature `setup_router`, this also show that the class `ORDER_HANDLER` will be in charge
 of handling different types of request to the ORDER resource.

```
	class RESTBUCKS_SERVER_EXECUTION

	inherit
		WSF_ROUTED_SKELETON_EXECUTION
			undefine
				requires_proxy
			end

		WSF_NO_PROXY_POLICY


		SHARED_RESTBUCKS_API

	create
		make

	feature {NONE} -- Initialization

		setup_router
			local
				doc: WSF_ROUTER_SELF_DOCUMENTATION_HANDLER
			do
				setup_order_handler (router)

				create doc.make_hidden (router)
				router.handle ("/api/doc", doc, router.methods_GET)
			end

		setup_order_handler (a_router: WSF_ROUTER)
			local
				order_handler: ORDER_HANDLER
			do
				create order_handler.make ("orderid", a_router)
				router.handle ("/order", order_handler, router.methods_POST)
				router.handle ("/order/{orderid}", order_handler, router.methods_GET + router.methods_DELETE + router.methods_PUT)
			end

	end
```

How to Create an order with POST
--------------------------------

Here is the convention that we are using: 
POST is used for creation and the server determines the URI of the created resource.
If the request POST is SUCCESS, the server will create the order and will response with
201 CREATED, the Location header will contains the newly created order's URI,
if the request POST is not SUCCESS, the server will response with
400 BAD REQUEST, the client send a bad request or
500 INTERNAL_SERVER_ERROR, when the server can deliver the request.
```
	POST /order HTTP/1.1
	Host: 127.0.0.1:8080
	Connection: keep-alive
	Content-Length: 196
	Origin: chrome-extension://fhjcajmcbmldlhcimfajhfbgofnpcjmb
	Content-Type: application/json
	Accept: */*
	Accept-Encoding: gzip,deflate,sdch
	Accept-Language: es-419,es;q=0.8,en;q=0.6
	Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.3
		     
	{
	 "location":"takeAway",
	 "items":[
	          {
	           "name":"Late",
		   "option":"skim",
		   "size":"Small",
		   "quantity":1
		   }
	    ]
	}
```

Response success
```
	HTTP/1.1 201 Created
	Status	201 Created
	Content-Type	application/json
	Content-Length	123
	Location	http://localhost:8080/order/1
	Date	FRI,09 DEC 2011 20:34:20.00 GMT
	
	{
	  "location" : "takeAway",
	  "status" : "submitted",
	  "items" : [ {
	    "name" : "late",
	    "size" : "small",
	    "quantity" : 1,
	    "option" : "skim"
	  } ]
	}
```

note: 
    curl -vv http://localhost:9090/order -H "Content-Type: application/json" -d "{\"location\":\"takeAway\",\"items\":[{\"name\":\"Late\",\"option\":\"skim\",\"size\":\"Small\",\"quantity\":1}]}" -X POST 


How to Read an order with GET
-----------------------------
Using GET to retrieve resource information.
If the GET request is SUCCESS, we response with 200 OK, and a representation of the order
If the GET request is not SUCCESS, we response with 404 Resource not found
If is a Conditional GET and the resource does not change we send a 304, Resource not modifed

```
	GET /order/1 HTTP/1.1
	Host: 127.0.0.1:8080
	Connection: keep-alive
	Accept: */*
	Accept-Encoding: gzip,deflate,sdch
	Accept-Language: es-419,es;q=0.8,en;q=0.6
	Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.3
	If-None-Match: 6542EF270D91D3EAF39CFB382E4CEBA7
```

Response
```
	HTTP/1.1 200 OK
	
	Status	200 OK
	Content-Type	application/json
	Content-Length	123
	Date	FRI,09 DEC 2011 20:53:46.00 GMT
	etag	2ED3A40954A95D766FC155682DC8BB52
	
	{
	  "location" : "takeAway",
	  "status" : "submitted",
	  "items" : [ {
	    "name" : "late",
	    "size" : "small",
	    "quantity" : 1,
	    "option" : "skim"
	  } ]
	}
```

note:
    curl -vv http://localhost:9090/order/1 

How to Update an order with PUT
-------------------------------
A successful PUT request will not create a new resource, instead it will change the state of the resource identified by the current uri.
If success we response with 200 and the updated order.
404 if the order is not found
400 in case of a bad request
500 internal server error
If the request is a Conditional PUT, and it does not mat we response 415, precondition failed.

Suposse that we had created an Order with the values shown in the _How to create an order with POST_
But we change our decision and we want to stay in the shop.

```
	PUT /order/1 HTTP/1.1
	Content-Length: 122
	Content-Type: application/json; charset=UTF-8
	Host: localhost:8080
	Connection: Keep-Alive
	Expect: 100-Continue

	{
	  "location" : "in shop",
	  "status" : "submitted",
	  "items" : [ {
	    "name" : "late",
	    "size" : "small",
	    "quantity" : 1,
	    "option" : "skim"
	  } ]
	}
```

Response success
```
	HTTP/1.1 200 OK
	Status	200 OK
	Content-Type	application/json
	Date	FRI,09 DEC 2011 21:06:26.00 GMT
	etag	8767F900674B843E1F3F70BCF3E62403
	Content-Length	122
	
	{
  	"location" : "in shop",
  	"status" : "submitted",
  	"items" : [ {
    		"name" : "late",
    		"size" : "small",
    		"quantity" : 1,
    		"option" : "skim"
  	} ]
	}
```

How to Delete an order with DELETE
----------------------------------
Here we use DELETE to cancel an order, if that order is in state where it can still be canceled.
204 if is ok
404 Resource not found
405 if consumer and service's view of the resouce state is inconsisent
500 if we have an internal server error

```
	DELETE /order/1 HTTP/1.1
	Host: localhost:8080
	Connection: Keep-Alive
```

Response success

```
	HTTP/1.1 204 No Content

	Status	204 No Content
	Content-Type	application/json
	Date	FRI,09 DEC 2011 21:10:51.00 GMT
```

If we want to check that the resource does not exist anymore we can try to retrieve a GET /order/1 and we will receive a
404 No Found

```
	GET /order/1 HTTP/1.1
	Host: localhost:8080
	Connection: Keep-Alive
```

Response

```
	HTTP/1.1 404 Not Found
	
	Status	404 Not Found
	Content-Type	application/json
	Content-Length	44
	Date	FRI,09 DEC 2011 21:14:17.79 GMT

	The following resource/order/1 is not found 
```

References
----------
1. [How to get a cup of coffe](http://www.infoq.com/articles/webber-rest-workflow) 
2. [Rest in Practice](http://restinpractice.com/default.aspx)

geant now supports a simple single inheritance mechanism:

A build file now can inherit the targets of another build
file by specifying the inherit attribute in the project element:

  <project name="B" inherit="a.eant">

build files which do not use the inherit attribute work like before.

You can find a demonstration of this new behaviour in

  $GOBO/tool/geant/example/inherit

which contains the two build files 'a.eant' and 'b.eant':

a.eant:
_____________________________________________________________
<?xml version="1.0" ?>

<project name="A">
	
	<target name="f1">
		<echo message="A.f1"/>
		<set name="var1" value="default_value1"/>
	</target>

	<target name="f2" depend="f1">
		<echo message="A.f2"/>
		<echo message="var1: ${var1}"/>
	</target>

</project>
_____________________________________________________________


b.eant:
_____________________________________________________________
<?xml version="1.0" ?>

<project name="B" inherit="a.eant">
	
	<target name="f1-">
		<echo message="B.f1"/>
		<set name="var1" value="value1"/>
	</target>

	<target name="f2-" depend="f1">
		<echo message="B.f2"/>
	</target>

	<target name="f3">
		<echo message="B.f3"/>
	</target>

</project>
_____________________________________________________________

If you invoke

  geant -v -b b.eant f3

you get the following output (almost like before):

_____________________________________________________________
  Loading Project's configuration from b.eant
  Loading Project's configuration from a.eant
  Building Project

  B.f3:

    [echo] B.f3
_____________________________________________________________

If you invoke

  geant -v -b b.eant f1

you get the following output:
_____________________________________________________________
  Loading Project's configuration from b.eant
  Loading Project's configuration from a.eant
  Building Project

  A.f1:

    [echo] A.f1
    [set] var1=default_value1
_____________________________________________________________

which demonstrates some inheritance behaviour.

Then

  geant -v -b b.eant f2

produces the following output:
_____________________________________________________________
  Loading Project's configuration from b.eant
  Loading Project's configuration from a.eant
  Building Project

  A.f1:

    [echo] A.f1
    [set] var1=default_value1

  A.f2:

    [echo] A.f2
    [echo] var1: default_value1
_____________________________________________________________


Now rename target 'f1-' in 'b.eant' to 'f1' and invoke

  geant -v -b b.eant f1

output:
_____________________________________________________________
  Loading Project's configuration from b.eant
  Loading Project's configuration from a.eant
  Building Project

  B.f1:

    [echo] B.f1
    [set] var1=value1
_____________________________________________________________

Invoke

  geant -v -b b.eant f2

output:
_____________________________________________________________
  Loading Project's configuration from b.eant
  Loading Project's configuration from a.eant
  Building Project

  B.f1:

    [echo] B.f1
    [set] var1=value1

  A.f2:

    [echo] A.f2
    [echo] var1: value1
_____________________________________________________________


Now rename target 'f1' in 'b.eant' back to 'f1-',
rename  'f2-' in 'b.eant' to 'f2', and invoke

  geant -v -b b.eant f2

output:
_____________________________________________________________
  Loading Project's configuration from b.eant
  Loading Project's configuration from a.eant
  Building Project

  A.f1:

    [echo] A.f1
    [set] var1=default_value1

  B.f2:

    [echo] B.f2
_____________________________________________________________

Maybe one day geant supports multiple inheritance and 'rename' and
'redefine' clauses like we are used to in Eiffel. Then the
'inherit' attribute will become a subelement of the project rather
than an attribute. The <precursor> task might be the next item on the
todo list.

- Sven

Invocation:

	geant -v -b d1.eant cf

Expected output:
________________________________________________________________
Loading Project's configuration from d1.eant
Loading Project's configuration from D:\svnstuff\gobo-eiffel\gobo/example/geant/inherit/multiple/diamond/b1.eant
Loading Project's configuration from D:\svnstuff\gobo-eiffel\gobo/example/geant/inherit/multiple/diamond/a1.eant
Loading Project's configuration from D:\svnstuff\gobo-eiffel\gobo/example/geant/inherit/multiple/diamond/c1.eant
Loading Project's configuration from D:\svnstuff\gobo-eiffel\gobo/example/geant/inherit/multiple/diamond/a1.eant
Building Project

D.cf:

  [echo] this is D.cf

C.f:

  [echo] this is C.f

A.f:

  [echo] this is A.f
________________________________________________________________

This example demonstrates the usage of export stati for targets.

Usage:
======

Invoke

  geant -b b.eant hello
  
and the output should look like this:

  hello
  fc
  fb
  fa
  target: `C.secret' is not exported to project 'B'
  

Description:
============

Project 'B' is invoking several targets of project 'C' using <geant...>.
If you look at 'c.eant' you can see that target 'hello' does not specify
an attribute 'export' and thus is exported to any project. The same is
true for target 'goodbye'.

Invoking target 'fb' is working as well since 'fb' is exported to project
'B', the project which invokes 'fb'.

Invoking target 'fa', exported to project 'A' is working as well since
'fb' is exported to project 'B' which inherits from project 'A'.



# IMAP client library

## Introduction
This repository contains an open source Eiffel library to connect to a server with the Internet Message Access Protocol.

This library provides an easy access to almost all the commands of IMAP4rev1 and the server responses and allows to send custom commands.

## Contents
* `src` : Contains the library classes
* `examples` : Contains examples of how to use the library

## Getting started

To use the Eiffel IMAP client library, add it to your project and instantiate an object of type `IMAP_CLIENT_LIB`

### Simple example
Here is a simple example to connect to a server, login, open the mailbox "INBOX" and logout :
```
	an_example
		local
			imap: IMAP_CLIENT_LIB
		do
			create imap.make_ssl_with_address ("your_server.com")
			imap.connect

			if imap.is_connected then
				imap.login ("username", "password")
				imap.select ("INBOX")
				print (imap.current_mailbox.name) -- INBOX
				imap.logout
			end
		end
```

You should look in the `examples` folder for more complex examples.

### Main functionality

##### Create and connect

The IMAP_CLIENT_LIB has 6 constructors, 3 for normal connection and 3 for SSL encrypted connection.
* `make` will create the imap library with the default address and port
* `make_with_address` will create the imap library with a connection to the given address
* `make_with_address_and_port` will create the imap library with a connection to the given address and a custom port

Each constructor also has its ssl version :
* `make_ssl`
* `make_ssl_with_address`
* `make_ssl_with_address_and_port`

To connect the library to the socket, you should call `{IMAP_CLIENT_LIB}.connect`
You can check if the library is connected with `{IMAP_CLIENT_LIB}.is_connected`

##### States

[The IMAP states](https://tools.ietf.org/html/rfc3501#section-3) are represented in `IL_NETWORK_STATE` with the extra state `not_connected_state`.
The state change automatically when you successfully call a function that changes the state.
You can get the current state with `{IMAP_CLIENT_LIB}.get_current_state`.

##### Commands and tags

Most of the IMAP commands have helper functions to send them and get the data back.
You can however send custom commands with `{IMAP_CLIENT_LIB}.send_command`.
It is also possible to send them as action (See `IL_IMAP_ACTION`) with `{IMAP_CLIENT_LIB}.send_action`. In this case a contract checks that the action is supported in the current state.

The command tags are automatically managed but you can access the tag of the last command with `{IMAP_CLIENT_LIB}.get_last_tag`.

##### Commands continuation

You can check if the server made a [command continuation request](https://tools.ietf.org/html/rfc3501#section-7.5) with `{IMAP_CLIENT_LIB}.needs_continuation`. If it does need one, you must send the continuation with `{IMAP_CLIENT_LIB}.send_command_continuation`.

##### Server responses

All the server responses are parsed and saved as a `IL_SERVER_RESPONSE`. You can access the response of the last command sent with `{IMAP_CLIENT_LIB}.get_last_response` or the response for a particular tag with `{IMAP_CLIENT_LIB}.get_response`.

You can also instruct the response manager to read the socket and parse the responses without getting data back with `{IMAP_CLIENT_LIB}.receive`

##### Errors and status

They should be checked on the `IL_SERVER_RESPONSE`.
Some usefull features for errors and status are :
* `{IL_SERVER_RESPONSE}.is_ok`
* `{IL_SERVER_RESPONSE}.is_error`
* `{IL_SERVER_RESPONSE}.status`

### [Main commands](https://tools.ietf.org/html/rfc3501#section-6)

##### Capability

You can get at any time when connected the result of a CAPABILITY command parsed in a list with `{IMAP_CLIENT_LIB}.get_capability`

##### Login / Logout

The logout can be done at any time with `{IMAP_CLIENT_LIB}.logout`
Login can be done in the not authenticated state with `{IMAP_CLIENT_LIB}.login`. This will send a plain text LOGIN command.

There is currently no available helper for AUTHENTICATE commands but these can be send with `{IMAP_CLIENT_LIB}.send_command` and `{IMAP_CLIENT_LIB}.send_continuation`.

##### Authenticated commands

The most usefull commands here are :
* `{IMAP_CLIENT_LIB}.get_list` to get a list of the mailboxes. It will return a data structure with the name, the path, the hierarchy delimiter and the attributes for each mailbox
* `{IMAP_CLIENT_LIB}.subscribe` to subscribe to a mailbox.
* `{IMAP_CLIENT_LIB}.create_mailbox`, `{IMAP_CLIENT_LIB}.delete_mailbox` and `{IMAP_CLIENT_LIB}.rename_mailbox` for the edition of mailboxes.
* `{IMAP_CLIENT_LIB}.get_status` let you get the status of a mailbox.

You can select or examine a mailbox with `{IMAP_CLIENT_LIB}.select_mailbox` or `{IMAP_CLIENT_LIB}.examine_mailbox`. If these commands are successful, you will then be in the selected state.

##### Selected commands

In this state, `current_mailbox` contains the information about the selected mailbox.

We have some helpers for IMAP commands like :
* `{IMAP_CLIENT_LIB}.expunge` or `{IMAP_CLIENT_LIB}.get_expunge`
* `{IMAP_CLIENT_LIB}.search` to search messages in the mailbox
* `{IMAP_CLIENT_LIB}.check_command`
* `{IMAP_CLIENT_LIB}.copy_messages`

`{IMAP_CLIENT_LIB}.check_for_changes` allows to send a NOOP and tell if the server has sent back any change. If it is the case you can then get the changes from `current_mailbox`.

You can fetch data from messages with the fetch family of features. See next section for more details.

`{IMAP_CLIENT_LIB}.close` will close the mailbox and go back to the authenticated state if it is successful.

##### Fetch messages

(Selected state only)

The easiest way to fetch messages is with `{IMAP_CLIENT_LIB}.fetch_messages`.
It will return a hash table mapping the sequence number of the message to an `IL_MESSAGE` object representing the message.
The class `IL_MESSAGE` has many attributes that allow easy access to message information like :
* `from_address` : The address (and name) of the sender
* `to_address` : The addresses of the recipient
* `subject` : The subject of the message
* `body_text` : The text of the body
* `date` : The date of the message
* `flags` : The flags of the message

and many more.

There is a version which fetches the messages from a set of uids instead of a set of sequence numbers : `{IMAP_CLIENT_LIB}.fetch_messages_uid`.

It is also possible to manually fetch particular [data items](https://tools.ietf.org/html/rfc3501#page-55) with `{IMAP_CLIENT_LIB}.fetch` or to use the fetch macros with `fetch_all`, `fetch_fast` and `fetch_full`.

## Dependencies
The current implementation depends on Eiffel NetSSL, so you will need to have
the static libraries under your path.

Check the Eiffel NetSSL documentation to learn more.


# Examples

This directory contains examples on how to use the Eiffel IMAP client library.

## Contents

There are currently four examples that you can find in the classes :
* `LIST_MAILBOX_EXAMPLE` : How to list the mailboxes with their paths
* `MAILBOXES_INFO_EXAMPLE` : How to check the number of messages and unseen message in each available mailbox
* `LAST_MESSAGE_INFO_EXAMPLE` : How to open a mailbox and retreive some info from a message
* `CHECK_MESSAGES_EXAMPLE` : How to check for changes in a mailbox

The class `APPLICATION` runs all of these examples one after another. Before you run it, you should change the server name, user name and password in `EXAMPLE`.Eiffel Nino HTTPD
=================
Eiffel Nino is and HTTPD server. It's a work in progress, so maybe it will be refactored.
The goal of is to provide a simple web server for development (like Java, Python and Ruby provide)
The code is based on Xebra and Emu Web Server.


Goal
========
HTTPD server for development, support for HTTP 1.1.




Testing
=======
To test the HTTPD server, you could run the [example https://github.com/jvelilla/EiffelWebNino/tree/master/example/SimpleWebServer] 
The server work fine in Windows and Linux.

Run the server and point your browser to one of the following URIs

1) http://localhost:9000/post/index.html 
2) http://localhost:9000/demo1/template.html
3) http://localhost:9000/demo2/demo.html
4) http://localhost:9000/example/html/index.html
5) http://localhost:9000/html/simple.html
6) http://localhost:9000/html/images.html
7) http://localhost:9000/html/images.html
8) http://localhost:9000/html5/dataset.html 

Known Issues
============






<!-- saved from url=(0022)http://internet.e-mail -->
<html>
<head>
<title>TemplatesBox.com | Terms of Use</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
</head>

<body bgcolor="#5E717F" text="#000000" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
<table width="700" cellspacing="0" cellpadding="8" align="center" bgcolor="#BED5E2" style="border-collapse:collapse;">
  <tr> 
    <td bgcolor="#567280" style="border-top-width:1px; border-right-width:1px; border-left-width:1px; border-top-color:rgb(216,216,216); border-right-color:rgb(216,216,216); border-left-color:rgb(216,216,216); border-top-style:solid; border-right-style:solid; border-left-style:solid;"><font color="#C2DCEB" size="2" face="Verdana,Arial"><b>Templates</b></font><font color="#FF9900" size="2" face="Verdana,Arial"><b>Box</b></font><font color="#FF9B05" size="2" face="Verdana,Arial"><b> 
            </b></font><font color="#E3E3E3" size="2" face="Verdana,Arial">|<b> Terms of Use</b></font></td>
  </tr>
  <tr> 
    <td bgcolor="#A1BBCA" style="border-right-width:1px; border-left-width:1px; border-right-color:rgb(216,216,216); border-left-color:rgb(216,216,216); border-right-style:solid; border-left-style:solid;">
            <table align="center" cellpadding="0" cellspacing="0" width="98%">
                <tr>
                    <td>
                        <p style="line-height:115%; margin-top:0; margin-bottom:0;"><font face="Verdana,Arial" color="#354D59"><span style="font-size:8pt;">By 
      downloading a template from TemplatesBox.com you agree to the following 
      Terms of Use:  </span></font> 
      <p style="line-height:115%; margin-top:0; margin-bottom:0;"><font face="Verdana,Arial" color="#354D59"><span style="font-size:8pt;">Our 
        web templates may be used for your own and/or your clients' websites, 
        but you may not sell/offer for free our templates in any sort of collection, 
        such as distributing to a third party via CD, diskette, or letting others 
        to download off your websites etc.<br>
        <br>
        Link back to www.templatesbox.com is required and always appreciated. 
        Also, please visit the<br>
        </span></font><a href="http://www.templatesbox.com/linkus.htm" target="_blank"><font face="Verdana,Arial" color="#354D59"><b><span style="font-size:8pt;">Link 
        Us</span></b></font></a><font face="Verdana,Arial" color="#354D59"><span style="font-size:8pt;"> section.<br>
        <br>
        The templates are offered &quot;as is&quot; without warranty of any kind, 
        either expressed or implied. TemplatesBox.com will not be liable for any 
        damage or loss of data whatsoever due to downloading or using a template. 
        In no event shall TemplatesBox.com be liable for any damages including, 
        but not limited to, direct, indirect, special, incidental or consequential 
        damages or other losses arising out of the use of or inability to use 
        the templates and/or information from TemplatesBox.com.<br>
        <br>
        TemplatesBox.com team reserves the right to change or modify these terms 
        with no prior notice.</span></font></p>
                    </td>
                </tr>
            </table>
    </td>
  </tr>
  <tr> 
    <td bgcolor="#567280" style="border-right-width:1px; border-left-width:1px; border-right-color:rgb(216,216,216); border-left-color:rgb(216,216,216); border-right-style:solid; border-left-style:solid;"><font size="2" face="Verdana,Arial" color="#E3E3E3"><b>Featured 
      Partners</b></font></td>
  </tr>
  <tr> 
    <td bgcolor="#A1BBCA" style="border-right-width:1px; border-bottom-width:1px; border-left-width:1px; border-right-color:rgb(216,216,216); border-bottom-color:rgb(216,216,216); border-left-color:rgb(216,216,216); border-right-style:solid; border-bottom-style:solid; border-left-style:solid;" height="235"> 
            <table align="center" cellpadding="0" cellspacing="0" width="98%">
                <tr>
                    <td>
                        <p><a href="http://www.specialtemplates.com" target="_blank"><b><font size="2" face="Verdana, Arial, Helvetica, sans-serif" color="#2D444F">Premium Website 
      Templates</font></b></a><font size="2" face="Verdana, Arial, Helvetica, sans-serif" color="#2D444F"><br>
      Over 9000 High-end Website templates, Flash intros and Logo templates.<b><a href="http://www.freshtemplates.com" target="_blank"><br>
      <br>
      </a></b></font><a href="http://www.freephotosbank.com" target="_blank"><b><font size="2" face="Verdana, Arial, Helvetica, sans-serif" color="#2D444F">Free 
                        Photos, Free Stock Photography</font></b></a><font size="2" face="Verdana, Arial, Helvetica, sans-serif" color="#2D444F"><b><br></b>
      </font><FONT face=Verdana color=#2d444f size=2><FONT size=2><FONT 
face=Verdana><FONT color=#2d444f>1000's of FREE high quality stock 
Photos!</FONT></FONT></FONT></FONT><font size="2" face="Verdana, Arial, Helvetica, sans-serif" color="#2D444F"><br>
      <br>
       </font><A 
href="http://www.webmasterschannel.com" target=_blank><FONT face=Verdana><FONT color=#2d444f><B><FONT size=2>Webmaster&nbsp;Resources &amp; 
Directory</FONT></B></FONT></FONT></A><font size="2" face="Verdana, Arial, Helvetica, sans-serif" color="#2D444F"><br>
      </font><FONT size=2><FONT face=Verdana><FONT color=#2d444f>A large web directory with webmaster 
resources.</FONT></FONT></FONT><font size="2" face="Verdana, Arial, Helvetica, sans-serif" color="#2D444F"><br>
      <br>
      </font><A href="http://www.photovations.com" 
target=_blank><FONT face=Verdana color=#000000 
size=2><FONT face=Verdana color=#2d444f size=2><STRONG>Photovations.com</STRONG></FONT></FONT></A><font size="2" face="Verdana, Arial, Helvetica, sans-serif" color="#2D444F"><br>
      </font><FONT face=Verdana color=#2d444f size=2><FONT size=2><FONT 
face=Verdana><FONT color=#2d444f>Online Photo Sharing. Free Image 
Hosting</FONT></FONT></FONT></FONT></p>
                    </td>
                </tr>
            </table>
</td>
  </tr>
</table>
</body>
</html>
Readme file for ECLOP
=====================

author: "Paul Cohen"
date: "$Date$"
revision: "$Revision$"

1. Introduction
---------------

ECLOP stands for Eiffel Command Line Parser and is a small library for parsing
command line options. The current release (0.1.1) should still be considered a
beta release but should despite that still be useful for writing command line
based programs and it is reasonably stable. Your mileage may vary. ;-)  

ECLOP was originally developed in a commercial project at Enea Systems AB,
Stockholm, Sweden, but has been released to the Eiffel community thanks to
understanding executives! I would like to thank Johan Pettersson and Peter
Johansson at Enea Systems for allowing me to release ECLOP under an open source
license and as a personal submission to the 2003 Eiffel Class Struggle! 


2. Legal stuff
--------------

ECLOP is copyrighted by the author Paul Cohen. It is licensed under the Eiffel 
Forum License v2. See the file license.txt in the same directory as this readme 
file.


3. Versioning scheme
--------------------

ECLOP version numbers has the form:

   <major number>.<minor number>.<patch level>

ECLOP will retain the major number 0 as long as it has beta status. A change in
major number indicates that a release is not backward compatible. A change in
minor number indicates that a release is backward compatible (within that major
number) but that new useful features may have been added. A change in patch
level simply indicates that the release contains bug fixes for the previous
release.  


4. Documentation
---------------

The file "eclop.pdf" is the main documentation available on ECLOP. This readme
file contains general information and the files todo.txt and history.txt in the
same directory as this readme file contains some additional information.


5. Requirements and installation
--------------------------------

ECLOP has been developed with ISE Eiffel (5.1, 5.2 and 5.4) and MSVC++ 6.0 on
Windows NT and 2000 machines. It should be easy to adapt to SmartEiffel and
Visual Eiffel and it is indeed the authors intention to do so. It should work on
Linux as is. It should also work without modifications with later versions of
ISE Eiffel. 

To install ECLOP simply extract the eclop-0.1.1.zip file to some appropriate
place on your hard disk. There are no requirements on environment variables or
registry variables. See the section "Contents of ECLOP" below for a description
of what is in the different directories of ECLOP. 

To verify that everything works you should compile the example programs and/or
the test program.


6. Contents of ECLOP
--------------------

All directory names below are relative to the root directory of your eclop
installation. 

Directory   Description
---------   -----------
doc	    Contains the eclop.pdf documentation file.
examples    Contains the two example programs mention in the eclop.pdf file.
eclop	    Contains the actual ECLOP library classes.
test	    Contains a test program for ECLOP.


7. Contacting the author
------------------------

Contact the author Paul Cohen at paco@enea.se.


8. Releases
-----------

For more information on what was changed in each release look in the file
history.txt.

Version Date	        Description
------- ----            -----------
0.1.1   2004-03-07	Patch release.
0.1.0   2003-10-31      First release. Submitted to the 2003 Eiffel Class
                        Struggle. 

			
Windows Eiffel eXtension Library - Readme

-------------------------------------
WEX, Version 1.00, 23th of July, 1998.
-------------------------------------

For copyright notice, please see forum.txt


What is WEX?
------------

WEX, the Windows Eiffel eXtension library, is as its name says an extension to WEL, 
the Windows Eiffel Library, that comes with the Windows version of ISE Eiffel. It is
free for everybody to use as defined in the file "forum.txt".


What do I need to run WEX?
--------------------------

You will need a copy of ISE Eiffel for Windows 95/98/NT and WEL. And Visual C++. It
should not be hard to get it running with any other C compiler, all you need to do is
change the ACE-files, but I never tried.


How do I install WEX?
---------------------

WEX consists of 2 major directories: "examples" and "library". Please add them to the 
directory where ISE Eiffel is installed. You will also need to define the enviroment
variable wex_vc_lib. It should point directly to the directory where the file "winmm.lib"
resides. This is typically "c:\program files\devstudio\vc\lib". 

Under Windows 95 or 98 you might add a line to the file autoexec.bat:

set wex_vc_lib = c:\program files\devstudio\vc\lib


Any Questions?
--------------

For any questions, comments or if you would like to contibute to WEX please mail to 
either:

Robin van Ommeren (robin.van.ommeren@wxs.nl) or 
Andreas Leitner (andreas.leitner@teleweb.at)

CMS emails will be stored in this folder.
Hard coded:

In the front page: embed facebook page.
https://developers.facebook.com/docs/plugins/page-plugin

In the docs page: include the disqus or remark42 comment system.

Hard coded:

In the front page: embed facebook page.
https://developers.facebook.com/docs/plugins/page-plugin

In the docs page: include the disqus comment system.

The green color is #99cc33ff
<html>
<head>
<title>EiffelStudio installation script</title>
</head>
<body>
<h1>on Linux / install.sh</h1>
<p>To easily install latest EiffelStudio on <strong>linux system</strong>:</p>
<code>
	curl -sSL <a href="install.sh">https://www.eiffel.org/setup/install.sh</a> | bash
</code>
<p><strong>note:</strong> EiffelStudio will be installed in your current directory, you will find a eiffel_*.rc file to configure your environment</p>

<h1>on Windows / install.bat</h1>
<p>To easily install latest EiffelStudio on <strong>Windows system</strong>:</p>
<code>
	curl -sSL -o %TEMP%\get-es.bat <a href="install.bat">https://www.eiffel.org/setup/install.bat</a> && call %TEMP%\get-es.bat && del %TEMP%\get-es.bat
</code>
<p>Or you can download the file <a href="install.bat">https://www.eiffel.org/setup/install.bat</a> and execute it in a dos console.</a>
<p>
<strong>Note:</strong> EiffelStudio will be installed in your current directory, you will find a eiffel_*.bat file to configure your environment<br/>
<strong>Requirements:</strong> the installation script requires 7z.exe, curl.ex or (wget.exe).<br/>
<strong>WARNING</strong>: installing EiffelStudio using the .msi file is safer as it performs additional registration operations useful for specific tools.
</p>

<h1>Customization</h1>
<p>You can customize the installation with the following environment variables:
<blockquote>
<ul>
<li>ISE_CHANNEL: latest (default), nightly,  custom <code>major.minor.build</code> (i.e 18.11.102592 if it exists)
</li>
<li>ISE_PLATFORM: if not set, the script tries to find expected value</li>
</ul>
On <strong>Linux</strong>, you can also pass arguments to the script using <code> .. | bash -s <em>channel</em> <em>platform</em></code>.
For instance:
<ul>
<li><code>curl -sSL ... | bash -s nightly </code></li>
<li><code>curl -sSL ... | bash -s latest linux-x86-64 </code></li>
</ul>
On <strong>Windows</strong>, you can also use similar argument in the <code>get-es.bat nighlty</code>.
</blockquote>
</p>
</body>
</html>
-- I18N_BINARY_SEARCH_ARRAY_DICTIONAY check
-- with two_plural_forms_singular_one_zero
a:I18N_BINARY_SEARCH_ARRAY_DICTIONAY
create a.make (plural_tools.two_plural_forms_singular_one_zero)
data_generation(a,50,100)
data_query(a,50,100)
data_get(a,50,100	h:I18N_HASH_TABLE_DICTIONARY
	
	-- relevant parameters		
	
	create h.make (plural_tools.two_plural_forms_singular_one)
	data_generation(h,50,100)
	data_query(h,50,100)
	data_get(h,50,100)

		
Test is okay!
-- I18N_BINARY_SEARCH_ARRAY_DICTIONAY
-- with two_plural_forms_singular_one

a:I18N_BINARY_SEARCH_ARRAY_DICTIONAY
create a.make (plural_tools.two_plural_forms_singular_one)
data_generation(a,50,100)
data_query(a,50,100)
data_get(a,50,100)h:I18N_HASH_TABLE_DICTIONARY

-- relevant parameters

create h.make (plural_tools.two_plural_forms_singular_one_zero)
data_generation(h,50,100)
data_query(h,50,100)
data_get(h,50,100)How to make the WEL C library `wel.lib'?
----------------------------------------

If you have Borland C, run `make_bcb.bat'.
If you have Microsoft C, run `make_msc.bat'.

The makefiles assume that the C-compiler is in your $PATH environment
variable.

The environment variable ISE_EIFFEL needs to be set to where ISE Eiffel is
installed for these compilation. (This is usually `C:\Eiffel50').

To set the variable, type:

	SET ISE_EIFFEL=C:\Eiffel50
When your Eiffel executable running, Eiffel cURL library needs 3 DLLs, they are:

libcurl.dll, libeay32.dll and ssleay32.dll

Please make sure the 3 DLLs files can be found in your environment PATH or in same folder of your executable.SEE INDEX.HTML FOR AN EASILY BROWSED HYPERTEXT VERSION OF THIS MANUAL.

* * *

                                    gd 1.3
                                       
A graphics library for fast GIF creation

Follow this link to the latest version of this document.

  Table of Contents
  
     * Credits and license terms
     * What's new in version 1.3?
     * What is gd?
     * What if I want to use another programming language?
     * What else do I need to use gd?
     * How do I get gd?
     * How do I build gd?
     * gd basics: using gd in your program
     * webgif: a useful example
     * Function and type reference by category
     * About the additional .gd image file format
     * Please tell us you're using gd!
     * If you have problems
     * Alphabetical quick index
       
   Up to the Boutell.Com, Inc. Home Page
   
  Credits and license terms
  
   In order to resolve any possible confusion regarding the authorship of
   gd, the following copyright statement covers all of the authors who
   have required such a statement. Although his LZW compression code no
   longer appears in gd, the authors wish to thank David Rowley for the
   original LZW-based GIF compression code, which has been removed due to
   patent concerns. If you are aware of any oversights in this copyright
   notice, please contact Thomas Boutell who will be pleased to correct
   them.

COPYRIGHT STATEMENT FOLLOWS THIS LINE

     Portions copyright 1994, 1995, 1996, 1997, 1998, by Cold Spring
     Harbor Laboratory. Funded under Grant P41-RR02188 by the National
     Institutes of Health.
     
     Portions copyright 1996, 1997, 1998, by Boutell.Com, Inc.
     
     GIF decompression code copyright 1990, 1991, 1993, by David Koblas
     (koblas@netcom.com).
     
     Non-LZW-based GIF compression code copyright 1998, by Hutchison
     Avenue Software Corporation (http://www.hasc.com/, info@hasc.com).
     
     Permission has been granted to copy and distribute gd in any
     context, including a commercial application, provided that this
     notice is present in user-accessible supporting documentation.
     
     This does not affect your ownership of the derived work itself, and
     the intent is to assure proper credit for the authors of gd, not to
     interfere with your productive use of gd. If you have questions,
     ask. "Derived works" includes all programs that utilize the
     library. Credit must be given in user-accessible documentation.
     
     Permission to use, copy, modify, and distribute this software and
     its documentation for any purpose and without fee is hereby
     granted, provided that the above copyright notice appear in all
     copies and that both that copyright notice and this permission
     notice appear in supporting documentation. This software is
     provided "as is" without express or implied warranty.
     
END OF COPYRIGHT STATEMENT

  What is gd?
  
   gd is a graphics library. It allows your code to quickly draw images
   complete with lines, arcs, text, multiple colors, cut and paste from
   other images, and flood fills, and write out the result as a .GIF
   file. This is particularly useful in World Wide Web applications,
   where .GIF is the format used for inline images.
   
   gd is not a paint program. If you are looking for a paint program, you
   are looking in the wrong place. If you are not a programmer, you are
   looking in the wrong place.
   
   gd does not provide for every possible desirable graphics operation.
   It is not necessary or desirable for gd to become a kitchen-sink
   graphics package, but version 1.3 incorporates most of the commonly
   requested features for an 8-bit 2D package. Support for scalable
   fonts, and truecolor images, JPEG and PNG is planned for version 2.0.
   Version 1.3 was released to correct longstanding bugs and provide an
   LZW-free GIF compression routine.
   
  What if I want to use another programming language?
  
    Perl
    
   gd can also be used from Perl, courtesy of Lincoln Stein's GD.pm
   library, which uses gd as the basis for a set of Perl 5.x classes.
   GD.pm is based on gd 1.1.1 but gd 1.2 should be compatible.
   
    Any Language
    
   There are, at the moment, at least three simple interpreters that
   perform gd operations. You can output the desired commands to a simple
   text file from whatever scripting language you prefer to use, then
   invoke the interpreter.
   
   These packages are based on gd 1.2 as of this writing but should be
   compatible with gd 1.3 with minimal tweaking.
     * tgd, by Bradley K. Sherman
     * fly, by Martin Gleeson
       
  What's new in version 1.3?
  
   Version 1.3 features the following changes:
   
   Non-LZW-based GIF compression code
          Version 1.3 contains GIF compression code that uses simple Run
          Length Encoding instead of LZW compression, while still
          retaining compatibility with normal LZW-based GIF decoders
          (your browser will still like your GIFs). LZW compression is
          patented by Unisys. This is why there have been no new versions
          of gd for a long time. THANKS to Hutchison Avenue Software
          Corporation for contributing this code. THE NEW CODE PRODUCES
          LARGER GIFS AND IS NOT WELL SUITED TO PHOTOGRAPHIC IMAGES. THIS
          IS A LEGAL ISSUE. IT IS NOT A QUESTION OF TECHNICAL SKILL.
          PLEASE DON'T COMPLAIN ABOUT THE SIZE OF GIF OUTPUT. THANKS!
          
   8-bit fonts, and 8-bit font support
          This improves support for European languages. Thanks are due to
          Honza Pazdziora and also to Jan Pazdziora . Also see the
          provided bdftogd Perl script if you wish to convert fixed-width
          X11 fonts to gd fonts.
          
   16-bit font support (no fonts provided)
          Although no such fonts are provided in the distribution, fonts
          containing more than 256 characters should work if the
          gdImageString16 and gdImageStringUp16 routines are used.
          
   Improvements to the "webgif" example/utility
          The "webgif" utility is now a slightly more useful application.
          Thanks to Brian Dowling for this code.
          
   Corrections to the color resolution field of GIF output
          Thanks to Bruno Aureli.
          
   Fixed polygon fills
          A one-line patch for the infamous polygon fill bug, courtesy of
          Jim Mason. I believe this fix is sufficient. However, if you
          find a situation where polygon fills still fail to behave
          properly, please send code that demonstrates the problem, and a
          fix if you have one. Verifying the fix is important.
          
   Row-major, not column-major
          Internally, gd now represents the array of pixels as an array
          of rows of pixels, rather than an array of columns of pixels.
          This improves the performance of compression and decompression
          routines slightly, because horizontally adjacent pixels are now
          next to each other in memory. This should not affect properly
          written gd applications, but applications that directly
          manipulate the pixels array will require changes.
          
  What else do I need to use gd?
  
   To use gd, you will need an ANSI C compiler. All popular Windows 95
   and NT C compilers are ANSI C compliant. Any full-ANSI-standard C
   compiler should be adequate. The cc compiler released with SunOS 4.1.3
   is not an ANSI C compiler. Most Unix users who do not already have gcc
   should get it. gcc is free, ANSI compliant and a de facto industry
   standard. Ask your ISP why it is missing.
   
   You will also want a GIF viewer, if you do not already have one for
   your system, since you will need a good way to check the results of
   your work. Any web browser will work, but you might be happier with a
   package like Lview Pro for Windows or xv for X. There are GIF viewers
   available for every graphics-capable computer out there, so consult
   newsgroups relevant to your particular system.
   
  How do I get gd?
  
    By HTTP
    
     * Gzipped Tar File (Unix)
     * .ZIP File (Windows)
       
    By FTP
    
     * Gzipped Tar File (Unix)
     * .ZIP File (Windows)
       
  How do I build gd?
  
   In order to build gd, you must first unpack the archive you have
   downloaded. If you are not familiar with tar and gunzip (Unix) or ZIP
   (Windows), please consult with an experienced user of your system.
   Sorry, we cannot answer questions about basic Internet skills.
   
   Unpacking the archive will produce a directory called "gd1.3".
   
    For Unix
    
   cd to the gd1.3 directory and examine the Makefile, which you will
   probably need to change slightly depending on your operating system
   and your needs.
   
    For Windows, Mac, Et Cetera
    
   Create a project using your favorite programming environment. Copy all
   of the gd files to the project directory. Add gd.c to your project.
   Add other source files as appropriate. Learning the basic skills of
   creating projects with your chosen C environment is up to you.
   
   Now, to build the demonstration program, just type "make gddemo" if
   you are working in a command-line environment, or build a project that
   includes gddemo.c if you are using a graphical environment. If all
   goes well, the program "gddemo" will be compiled and linked without
   incident. Depending on your system you may need to edit the Makefile.
   Understanding the basic techniques of compiling and linking programs
   on your system is up to you.
   
   You have now built a demonstration program which shows off the
   capabilities of gd. To see it in action, type "gddemo".
   
   gddemo should execute without incident, creating the file demoout.gif.
   (Note there is also a file named demoin.gif, which is provided in the
   package as part of the demonstration.)
   
   Display demoout.gif in your GIF viewer. The image should be 128x128
   pixels and should contain an image of the space shuttle with quite a
   lot of graphical elements drawn on top of it.
   
   (If you are missing the demoin.gif file, the other items should appear
   anyway.)
   
   Look at demoin.gif to see the original space shuttle image which was
   scaled and copied into the output image.
   
  gd basics: using gd in your program
  
   gd lets you create GIF images on the fly. To use gd in your program,
   include the file gd.h, and link with the libgd.a library produced by
   "make libgd.a", under Unix. Under other operating systems you will add
   gd.c to your own project.
   
   If you want to use the provided fonts, include gdfontt.h, gdfonts.h,
   gdfontmb.h, gdfontl.h and/or gdfontg.h. If you are not using the
   provided Makefile and/or a library-based approach, be sure to include
   the source modules as well in your project. (They may be too large for
   16-bit memory models, that is, 16-bit DOS and Windows.)
   
   Here is a short example program. (For a more advanced example, see
   gddemo.c, included in the distribution. gddemo.c is NOT the same
   program; it demonstrates additional features!)
   
/* Bring in gd library functions */
#include "gd.h"

/* Bring in standard I/O so we can output the GIF to a file */
#include <stdio.h>

int main() {
        /* Declare the image */
        gdImagePtr im;
        /* Declare an output file */
        FILE *out;
        /* Declare color indexes */
        int black;
        int white;

        /* Allocate the image: 64 pixels across by 64 pixels tall */
        im = gdImageCreate(64, 64);

        /* Allocate the color black (red, green and blue all minimum).
                Since this is the first color in a new image, it will
                be the background color. */
        black = gdImageColorAllocate(im, 0, 0, 0);

        /* Allocate the color white (red, green and blue all maximum). */
        white = gdImageColorAllocate(im, 255, 255, 255);
        
        /* Draw a line from the upper left to the lower right,
                using white color index. */
        gdImageLine(im, 0, 0, 63, 63, white);

        /* Open a file for writing. "wb" means "write binary", important
                under MSDOS, harmless under Unix. */
        out = fopen("test.gif", "wb");

        /* Output the image to the disk file. */
        gdImageGif(im, out);

        /* Close the file. */
        fclose(out);

        /* Destroy the image in memory. */
        gdImageDestroy(im);
}

   When executed, this program creates an image, allocates two colors
   (the first color allocated becomes the background color), draws a
   diagonal line (note that 0, 0 is the upper left corner), writes the
   image to a GIF file, and destroys the image.
   
   The above example program should give you an idea of how the package
   works. gd provides many additional functions, which are listed in the
   following reference chapters, complete with code snippets
   demonstrating each. There is also an alphabetical index.
   
  Webgif: a more powerful gd example
  
   Webgif is a simple utility program to manipulate GIFs from the command
   line. It is written for Unix and similar command-line systems, but
   should be easily adapted for other environments. Webgif allows you to
   set transparency and interlacing and output interesting information
   about the GIF in question.
   
   webgif.c is provided in the distribution. Unix users can simply type
   "make webgif" to compile the program. Type "webgif" with no arguments
   to see the available options.
   
Function and type reference

     * Types
     * Image creation, destruction, loading and saving
     * Drawing, styling, brushing, tiling and filling functions
     * Query functions (not color-related)
     * Font and text-handling functions
     * Color handling functions
     * Copying and resizing functions
     * Miscellaneous Functions
     * Constants
       
  Types
  
   gdImage(TYPE)
          The data structure in which gd stores images. gdImageCreate
          returns a pointer to this type, and the other functions expect
          to receive a pointer to this type as their first argument. You
          may read the members sx (size on X axis), sy (size on Y axis),
          colorsTotal (total colors), red (red component of colors; an
          array of 256 integers between 0 and 255), green (green
          component of colors, as above), blue (blue component of colors,
          as above), and transparent (index of transparent color, -1 if
          none); please do so using the macros provided. Do NOT set the
          members directly from your code; use the functions provided.
          

typedef struct {
        unsigned char ** pixels;
        int sx;
        int sy;
        int colorsTotal;
        int red[gdMaxColors];
        int green[gdMaxColors];
        int blue[gdMaxColors];
        int open[gdMaxColors];
        int transparent;
} gdImage;

   gdImagePtr (TYPE)
          A pointer to an image structure. gdImageCreate returns this
          type, and the other functions expect it as the first argument.
          
   gdFont (TYPE)
          A font structure. Used to declare the characteristics of a
          font. Plese see the files gdfontl.c and gdfontl.h for an
          example of the proper declaration of this structure. You can
          provide your own font data by providing such a structure and
          the associated pixel array. You can determine the width and
          height of a single character in a font by examining the w and h
          members of the structure. If you will not be creating your own
          fonts, you will not need to concern yourself with the rest of
          the components of this structure.
          

typedef struct {
        /* # of characters in font */
        int nchars;
        /* First character is numbered... (usually 32 = space) */
        int offset;
        /* Character width and height */
        int w;
        int h;
        /* Font data; array of characters, one row after another.
                Easily included in code, also easily loaded from
                data files. */
        char *data;
} gdFont;

   gdFontPtr (TYPE)
          A pointer to a font structure. Text-output functions expect
          these as their second argument, following the gdImagePtr
          argument. Two such pointers are declared in the provided
          include files gdfonts.h and gdfontl.h.
          
   gdPoint (TYPE)
          Represents a point in the coordinate space of the image; used
          by gdImagePolygon and gdImageFilledPolygon.
          

typedef struct {
        int x, y;
} gdPoint, *gdPointPtr;

   gdPointPtr (TYPE)
          A pointer to a gdPoint structure; passed as an argument to
          gdImagePolygon and gdImageFilledPolygon.
          
  Image creation, destruction, loading and saving
  
   gdImageCreate(sx, sy) (FUNCTION)
          gdImageCreate is called to create images. Invoke gdImageCreate
          with the x and y dimensions of the desired image. gdImageCreate
          returns a gdImagePtr to the new image, or NULL if unable to
          allocate the image. The image must eventually be destroyed
          using gdImageDestroy().
          

... inside a function ...
gdImagePtr im;
im = gdImageCreate(64, 64);
/* ... Use the image ... */
gdImageDestroy(im);

   gdImageCreateFromGif(FILE *in) (FUNCTION)
          gdImageCreateFromGif is called to load images from GIF format
          files. Invoke gdImageCreateFromGif with an already opened
          pointer to a file containing the desired image.
          gdImageCreateFromGif returns a gdImagePtr to the new image, or
          NULL if unable to load the image (most often because the file
          is corrupt or does not contain a GIF image).
          gdImageCreateFromGif does not close the file. You can inspect
          the sx and sy members of the image to determine its size. The
          image must eventually be destroyed using gdImageDestroy().
          

gdImagePtr im;
... inside a function ...
FILE *in;
in = fopen("mygif.gif", "rb");
im = gdImageCreateFromGif(in);
fclose(in);
/* ... Use the image ... */
gdImageDestroy(im);

   gdImageCreateFromGd(FILE *in) (FUNCTION)
          gdImageCreateFromGd is called to load images from gd format
          files. Invoke gdImageCreateFromGd with an already opened
          pointer to a file containing the desired image in the gd file
          format, which is specific to gd and intended for very fast
          loading. (It is not intended for compression; for compression,
          use GIF.) gdImageCreateFromGd returns a gdImagePtr to the new
          image, or NULL if unable to load the image (most often because
          the file is corrupt or does not contain a gd format image).
          gdImageCreateFromGd does not close the file. You can inspect
          the sx and sy members of the image to determine its size. The
          image must eventually be destroyed using gdImageDestroy().
          

... inside a function ...
gdImagePtr im;
FILE *in;
in = fopen("mygd.gd", "rb");
im = gdImageCreateFromGd(in);
fclose(in);
/* ... Use the image ... */
gdImageDestroy(im);

   gdImageCreateFromXbm(FILE *in) (FUNCTION)
          gdImageCreateFromXbm is called to load images from X bitmap
          format files. Invoke gdImageCreateFromXbm with an already
          opened pointer to a file containing the desired image.
          gdImageCreateFromXbm returns a gdImagePtr to the new image, or
          NULL if unable to load the image (most often because the file
          is corrupt or does not contain an X bitmap format image).
          gdImageCreateFromXbm does not close the file. You can inspect
          the sx and sy members of the image to determine its size. The
          image must eventually be destroyed using gdImageDestroy().
          

... inside a function ...
gdImagePtr im;
FILE *in;
in = fopen("myxbm.xbm", "rb");
im = gdImageCreateFromXbm(in);
fclose(in);
/* ... Use the image ... */
gdImageDestroy(im);

   gdImageDestroy(gdImagePtr im) (FUNCTION)
          gdImageDestroy is used to free the memory associated with an
          image. It is important to invoke gdImageDestroy before exiting
          your program or assigning a new image to a gdImagePtr variable.
          

... inside a function ...
gdImagePtr im;
im = gdImageCreate(10, 10);
/* ... Use the image ... */
/* Now destroy it */
gdImageDestroy(im);

   void gdImageGif(gdImagePtr im, FILE *out) (FUNCTION)
          gdImageGif outputs the specified image to the specified file in
          GIF format. The file must be open for writing. Under MSDOS, it
          is important to use "wb" as opposed to simply "w" as the mode
          when opening the file, and under Unix there is no penalty for
          doing so. gdImageGif does not close the file; your code must do
          so.
          

... inside a function ...
gdImagePtr im;
int black, white;
FILE *out;
/* Create the image */
im = gdImageCreate(100, 100);
/* Allocate background */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Allocate drawing color */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Draw rectangle */
gdImageRectangle(im, 0, 0, 99, 99, black);
/* Open output file in binary mode */
out = fopen("rect.gif", "wb");
/* Write GIF */
gdImageGif(im, out);
/* Close file */
fclose(out);
/* Destroy image */
gdImageDestroy(im);

   void gdImageGd(gdImagePtr im, FILE *out) (FUNCTION)
          gdImageGd outputs the specified image to the specified file in
          the gd image format. The file must be open for writing. Under
          MSDOS, it is important to use "wb" as opposed to simply "w" as
          the mode when opening the file, and under Unix there is no
          penalty for doing so. gdImageGif does not close the file; your
          code must do so.
          
          The gd image format is intended for fast reads and writes of
          images your program will need frequently to build other images.
          It is not a compressed format, and is not intended for general
          use.
          

... inside a function ...
gdImagePtr im;
int black, white;
FILE *out;
/* Create the image */
im = gdImageCreate(100, 100);
/* Allocate background */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Allocate drawing color */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Draw rectangle */
gdImageRectangle(im, 0, 0, 99, 99, black);
/* Open output file in binary mode */
out = fopen("rect.gd", "wb");
/* Write gd format file */
gdImageGd(im, out);
/* Close file */
fclose(out);
/* Destroy image */
gdImageDestroy(im);

  Drawing Functions
  
   void gdImageSetPixel(gdImagePtr im, int x, int y, int color)
          (FUNCTION)
          gdImageSetPixel sets a pixel to a particular color index.
          Always use this function or one of the other drawing functions
          to access pixels; do not access the pixels of the gdImage
          structure directly.
          

... inside a function ...
gdImagePtr im;
int black;
int white;
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Set a pixel near the center. */
gdImageSetPixel(im, 50, 50, white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImageLine(gdImagePtr im, int x1, int y1, int x2, int y2, int
          color) (FUNCTION)
          gdImageLine is used to draw a line between two endpoints (x1,y1
          and x2, y2). The line is drawn using the color index specified.
          Note that the color index can be an actual color returned by
          gdImageColorAllocate or one of gdStyled, gdBrushed or
          gdStyledBrushed.
          

... inside a function ...
gdImagePtr im;
int black;
int white;
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Draw a line from the upper left corner to the lower right corner. */
gdImageLine(im, 0, 0, 99, 99, white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImageDashedLine(gdImagePtr im, int x1, int y1, int x2, int y2,
          int color) (FUNCTION)
          gdImageDashedLine is provided solely for backwards
          compatibility with gd 1.0. New programs should draw dashed
          lines using the normal gdImageLine function and the new
          gdImageSetStyle function.
          
          gdImageDashedLine is used to draw a dashed line between two
          endpoints (x1,y1 and x2, y2). The line is drawn using the color
          index specified. The portions of the line that are not drawn
          are left transparent so the background is visible.
          

... inside a function ...
gdImagePtr im;
int black;
int white;
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Draw a dashed line from the upper left corner to the lower right corner. */
gdImageDashedLine(im, 0, 0, 99, 99);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImagePolygon(gdImagePtr im, gdPointPtr points, int pointsTotal,
          int color) (FUNCTION)
          gdImagePolygon is used to draw a polygon with the verticies (at
          least 3) specified, using the color index specified. See also
          gdImageFilledPolygon.
          

... inside a function ...
gdImagePtr im;
int black;
int white;
/* Points of polygon */
gdPoint points[3];
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Draw a triangle. */
points[0].x = 50;
points[0].y = 0;
points[1].x = 99;
points[1].y = 99;
points[2].x = 0;
points[2].y = 99;
gdImagePolygon(im, points, 3, white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImageRectangle(gdImagePtr im, int x1, int y1, int x2, int y2,
          int color) (FUNCTION)
          gdImageRectangle is used to draw a rectangle with the two
          corners (upper left first, then lower right) specified, using
          the color index specified.
          

... inside a function ...
gdImagePtr im;
int black;
int white;
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Draw a rectangle occupying the central area. */
gdImageRectangle(im, 25, 25, 74, 74, white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImageFilledPolygon(gdImagePtr im, gdPointPtr points, int
          pointsTotal, int color) (FUNCTION)
          gdImageFilledPolygon is used to fill a polygon with the
          verticies (at least 3) specified, using the color index
          specified. See also gdImagePolygon.
          

... inside a function ...
gdImagePtr im;
int black;
int white;
int red;
/* Points of polygon */
gdPoint points[3];
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Allocate the color red. */
red = gdImageColorAllocate(im, 255, 0, 0);
/* Draw a triangle. */
points[0].x = 50;
points[0].y = 0;
points[1].x = 99;
points[1].y = 99;
points[2].x = 0;
points[2].y = 99;
/* Paint it in white */
gdImageFilledPolygon(im, points, 3, white);
/* Outline it in red; must be done second */
gdImagePolygon(im, points, 3, red);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImageFilledRectangle(gdImagePtr im, int x1, int y1, int x2, int
          y2, int color) (FUNCTION)
          gdImageFilledRectangle is used to draw a solid rectangle with
          the two corners (upper left first, then lower right) specified,
          using the color index specified.
          

... inside a function ...
gdImagePtr im;
int black;
int white;
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = int gdImageColorAllocate(im, 255, 255, 255);
/* Draw a filled rectangle occupying the central area. */
gdImageFilledRectangle(im, 25, 25, 74, 74, white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImageArc(gdImagePtr im, int cx, int cy, int w, int h, int s,
          int e, int color) (FUNCTION)
          gdImageArc is used to draw a partial ellipse centered at the
          given point, with the specified width and height in pixels. The
          arc begins at the position in degrees specified by s and ends
          at the position specified by e. The arc is drawn in the color
          specified by the last argument. A circle can be drawn by
          beginning from 0 degrees and ending at 360 degrees, with width
          and height being equal. e must be greater than s. Values
          greater than 360 are interpreted modulo 360.
          

... inside a function ...
gdImagePtr im;
int black;
int white;
im = gdImageCreate(100, 50);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Inscribe an ellipse in the image. */
gdImageArc(im, 50, 25, 98, 48, 0, 360, white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImageFillToBorder(gdImagePtr im, int x, int y, int border, int
          color) (FUNCTION)
          gdImageFillToBorder floods a portion of the image with the
          specified color, beginning at the specified point and stopping
          at the specified border color. For a way of flooding an area
          defined by the color of the starting point, see gdImageFill.
          
          The border color cannot be a special color such as gdTiled; it
          must be a proper solid color. The fill color can be, however.
          
          Note that gdImageFillToBorder is recursive. It is not the most
          naive implementation possible, and the implementation is
          expected to improve, but there will always be degenerate cases
          in which the stack can become very deep. This can be a problem
          in MSDOS and MS Windows environments. (Of course, in a Unix or
          NT environment with a proper stack, this is not a problem at
          all.)
          

... inside a function ...
gdImagePtr im;
int black;
int white;
int red;
im = gdImageCreate(100, 50);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Allocate the color red. */
red = gdImageColorAllocate(im, 255, 0, 0);
/* Inscribe an ellipse in the image. */
gdImageArc(im, 50, 25, 98, 48, 0, 360, white);
/* Flood-fill the ellipse. Fill color is red, border color is
        white (ellipse). */
gdImageFillToBorder(im, 50, 50, white, red);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImageFill(gdImagePtr im, int x, int y, int color) (FUNCTION)
          gdImageFill floods a portion of the image with the specified
          color, beginning at the specified point and flooding the
          surrounding region of the same color as the starting point. For
          a way of flooding a region defined by a specific border color
          rather than by its interior color, see gdImageFillToBorder.
          
          The fill color can be gdTiled, resulting in a tile fill using
          another image as the tile. However, the tile image cannot be
          transparent. If the image you wish to fill with has a
          transparent color index, call gdImageTransparent on the tile
          image and set the transparent color index to -1 to turn off its
          transparency.
          
          Note that gdImageFill is recursive. It is not the most naive
          implementation possible, and the implementation is expected to
          improve, but there will always be degenerate cases in which the
          stack can become very deep. This can be a problem in MSDOS and
          MS Windows environments. (Of course, in a Unix or NT
          environment with a proper stack, this is not a problem at all.)
          

... inside a function ...
gdImagePtr im;
int black;
int white;
int red;
im = gdImageCreate(100, 50);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Allocate the color red. */
red = gdImageColorAllocate(im, 255, 0, 0);
/* Inscribe an ellipse in the image. */
gdImageArc(im, 50, 25, 98, 48, 0, 360, white);
/* Flood-fill the ellipse. Fill color is red, and will replace the
        black interior of the ellipse. */
gdImageFill(im, 50, 50, red);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImageSetBrush(gdImagePtr im, gdImagePtr brush) (FUNCTION)
          A "brush" is an image used to draw wide, shaped strokes in
          another image. Just as a paintbrush is not a single point, a
          brush image need not be a single pixel. Any gd image can be
          used as a brush, and by setting the transparent color index of
          the brush image with gdImageColorTransparent, a brush of any
          shape can be created. All line-drawing functions, such as
          gdImageLine and gdImagePolygon, will use the current brush if
          the special "color" gdBrushed or gdStyledBrushed is used when
          calling them.
          
          gdImageSetBrush is used to specify the brush to be used in a
          particular image. You can set any image to be the brush. If the
          brush image does not have the same color map as the first
          image, any colors missing from the first image will be
          allocated. If not enough colors can be allocated, the closest
          colors already available will be used. This allows arbitrary
          GIFs to be used as brush images. It also means, however, that
          you should not set a brush unless you will actually use it; if
          you set a rapid succession of different brush images, you can
          quickly fill your color map, and the results will not be
          optimal.
          
          You need not take any special action when you are finished with
          a brush. As for any other image, if you will not be using the
          brush image for any further purpose, you should call
          gdImageDestroy. You must not use the color gdBrushed if the
          current brush has been destroyed; you can of course set a new
          brush to replace it.
          

... inside a function ...
gdImagePtr im, brush;
FILE *in;
int black;
im = gdImageCreate(100, 100);
/* Open the brush GIF. For best results, portions of the
        brush that should be transparent (ie, not part of the
        brush shape) should have the transparent color index. */
in = fopen("star.gif", "rb");
brush = gdImageCreateFromGif(in);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
gdImageSetBrush(im, brush);
/* Draw a line from the upper left corner to the lower right corner
        using the brush. */
gdImageLine(im, 0, 0, 99, 99, gdBrushed);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);
/* Destroy the brush image */
gdImageDestroy(brush);

   void gdImageSetTile(gdImagePtr im, gdImagePtr tile) (FUNCTION)
          A "tile" is an image used to fill an area with a repeated
          pattern. Any gd image can be used as a tile, and by setting the
          transparent color index of the tile image with
          gdImageColorTransparent, a tile that allows certain parts of
          the underlying area to shine through can be created. All
          region-filling functions, such as gdImageFill and
          gdImageFilledPolygon, will use the current tile if the special
          "color" gdTiled is used when calling them.
          
          gdImageSetTile is used to specify the tile to be used in a
          particular image. You can set any image to be the tile. If the
          tile image does not have the same color map as the first image,
          any colors missing from the first image will be allocated. If
          not enough colors can be allocated, the closest colors already
          available will be used. This allows arbitrary GIFs to be used
          as tile images. It also means, however, that you should not set
          a tile unless you will actually use it; if you set a rapid
          succession of different tile images, you can quickly fill your
          color map, and the results will not be optimal.
          
          You need not take any special action when you are finished with
          a tile. As for any other image, if you will not be using the
          tile image for any further purpose, you should call
          gdImageDestroy. You must not use the color gdTiled if the
          current tile has been destroyed; you can of course set a new
          tile to replace it.
          

... inside a function ...
gdImagePtr im, tile;
FILE *in;
int black;
im = gdImageCreate(100, 100);
/* Open the tile GIF. For best results, portions of the
        tile that should be transparent (ie, allowing the
        background to shine through) should have the transparent
        color index. */
in = fopen("star.gif", "rb");
tile = gdImageCreateFromGif(in);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
gdImageSetTile(im, tile);
/* Fill an area using the tile. */
gdImageFilledRectangle(im, 25, 25, 75, 75, gdTiled);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);
/* Destroy the tile image */
gdImageDestroy(tile);

   void gdImageSetStyle(gdImagePtr im, int *style, int styleLength)
          (FUNCTION)
          It is often desirable to draw dashed lines, dotted lines, and
          other variations on a broken line. gdImageSetStyle can be used
          to set any desired series of colors, including a special color
          that leaves the background intact, to be repeated during the
          drawing of a line.
          
          To use gdImageSetStyle, create an array of integers and assign
          them the desired series of color values to be repeated. You can
          assign the special color value gdTransparent to indicate that
          the existing color should be left unchanged for that particular
          pixel (allowing a dashed line to be attractively drawn over an
          existing image).
          
          Then, to draw a line using the style, use the normal
          gdImageLine function with the special color value gdStyled.
          
          As of version 1.1.1, the style array is copied when you set the
          style, so you need not be concerned with keeping the array
          around indefinitely. This should not break existing code that
          assumes styles are not copied.
          
          You can also combine styles and brushes to draw the brush image
          at intervals instead of in a continuous stroke. When creating a
          style for use with a brush, the style values are interpreted
          differently: zero (0) indicates pixels at which the brush
          should not be drawn, while one (1) indicates pixels at which
          the brush should be drawn. To draw a styled, brushed line, you
          must use the special color value gdStyledBrushed. For an
          example of this feature in use, see gddemo.c (provided in the
          distribution).
          

gdImagePtr im;
int styleDotted[2], styleDashed[6];
FILE *in;
int black;
int red;
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
red = gdImageColorAllocate(im, 255, 0, 0);
/* Set up dotted style. Leave every other pixel alone. */
styleDotted[0] = red;
styleDotted[1] = gdTransparent;
/* Set up dashed style. Three on, three off. */
styleDashed[0] = red;
styleDashed[1] = red;
styleDashed[2] = red;
styleDashed[3] = gdTransparent;
styleDashed[4] = gdTransparent;
styleDashed[5] = gdTransparent;
/* Set dotted style. Note that we have to specify how many pixels are
        in the style! */
gdImageSetStyle(im, styleDotted, 2);
/* Draw a line from the upper left corner to the lower right corner. */
gdImageLine(im, 0, 0, 99, 99, gdStyled);
/* Now the dashed line. */
gdImageSetStyle(im, styleDashed, 6);
gdImageLine(im, 0, 99, 0, 99, gdStyled);

/* ... Do something with the image, such as saving it to a file ... */

/* Destroy it */
gdImageDestroy(im);

  Query Functions
  
        int gdImageBlue(gdImagePtr im, int color) (MACRO)
                gdImageBlue is a macro which returns the blue component
                of the specified color index. Use this macro rather than
                accessing the structure members directly.
                
        int gdImageGetPixel(gdImagePtr im, int x, int y) (FUNCTION)
                gdImageGetPixel() retrieves the color index of a
                particular pixel. Always use this function to query
                pixels; do not access the pixels of the gdImage structure
                directly.
                

... inside a function ...
FILE *in;
gdImagePtr im;
int c;
in = fopen("mygif.gif", "rb");
im = gdImageCreateFromGif(in);
fclose(in);
c = gdImageGetPixel(im, gdImageSX(im) / 2, gdImageSY(im) / 2);
printf("The value of the center pixel is %d; RGB values are %d,%d,%d\n",
        c, im->red[c], im->green[c], im->blue[c]);
gdImageDestroy(im);

        int gdImageBoundsSafe(gdImagePtr im, int x, int y) (FUNCTION)
                gdImageBoundsSafe returns true (1) if the specified point
                is within the bounds of the image, false (0) if not. This
                function is intended primarily for use by those who wish
                to add functions to gd. All of the gd drawing functions
                already clip safely to the edges of the image.
                

... inside a function ...
gdImagePtr im;
int black;
int white;
im = gdImageCreate(100, 100);
if (gdImageBoundsSafe(im, 50, 50)) {
        printf("50, 50 is within the image bounds\n");
} else {
        printf("50, 50 is outside the image bounds\n");
}
gdImageDestroy(im);

        int gdImageGreen(gdImagePtr im, int color) (MACRO)
                gdImageGreen is a macro which returns the green component
                of the specified color index. Use this macro rather than
                accessing the structure members directly.
                
        int gdImageRed(gdImagePtr im, int color) (MACRO)
                gdImageRed is a macro which returns the red component of
                the specified color index. Use this macro rather than
                accessing the structure members directly.
                
        int gdImageSX(gdImagePtr im) (MACRO)
                gdImageSX is a macro which returns the width of the image
                in pixels. Use this macro rather than accessing the
                structure members directly.
                
        int gdImageSY(gdImagePtr im) (MACRO)
                gdImageSY is a macro which returns the height of the
                image in pixels. Use this macro rather than accessing the
                structure members directly.
                
  Fonts and text-handling functions
  
        void gdImageChar(gdImagePtr im, gdFontPtr font, int x, int y, int
                c, int color) (FUNCTION)
                gdImageChar is used to draw single characters on the
                image. (To draw multiple characters, use gdImageString or
                gdImageString16.) The second argument is a pointer to a
                font definition structure; five fonts are provided with
                gd, gdFontTiny, gdFontSmall, gdFontMediumBold,
                gdFontLarge, and gdFontGiant. You must include the files
                "gdfontt.h", "gdfonts.h", "gdfontmb.h", "gdfontl.h" and
                "gdfontg.h" respectively and (if you are not using a
                library-based approach) link with the corresponding .c
                files to use the provided fonts. The character specified
                by the fifth argument is drawn from left to right in the
                specified color. (See gdImageCharUp for a way of drawing
                vertical text.) Pixels not set by a particular character
                retain their previous color.
                

#include "gd.h"
#include "gdfontl.h"
... inside a function ...
gdImagePtr im;
int black;
int white;
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Draw a character. */
gdImageChar(im, gdFontLarge, 0, 0, 'Q', white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

        void gdImageCharUp(gdImagePtr im, gdFontPtr font, int x, int y,
                int c, int color) (FUNCTION)
                gdImageCharUp is used to draw single characters on the
                image, rotated 90 degrees. (To draw multiple characters,
                use gdImageStringUp or gdImageStringUp16.) The second
                argument is a pointer to a font definition structure;
                five fonts are provided with gd, gdFontTiny, gdFontSmall,
                gdFontMediumBold, gdFontLarge, and gdFontGiant. You must
                include the files "gdfontt.h", "gdfonts.h", "gdfontmb.h",
                "gdfontl.h" and "gdfontg.h" respectively and (if you are
                not using a library-based approach) link with the
                corresponding .c files to use the provided fonts. The
                character specified by the fifth argument is drawn from
                bottom to top, rotated at a 90-degree angle, in the
                specified color. (See gdImageChar for a way of drawing
                horizontal text.) Pixels not set by a particular
                character retain their previous color.
                

#include "gd.h"
#include "gdfontl.h"
... inside a function ...
gdImagePtr im;
int black;
int white;
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Draw a character upwards so it rests against the top of the image. */
gdImageCharUp(im, gdFontLarge,
        0, gdFontLarge->h, 'Q', white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

        void gdImageString(gdImagePtr im, gdFontPtr font, int x, int y,
                unsigned char *s, int color) (FUNCTION)
                gdImageString is used to draw multiple characters on the
                image. (To draw single characters, use gdImageChar.) The
                second argument is a pointer to a font definition
                structure; five fonts are provided with gd, gdFontTiny,
                gdFontSmall, gdFontMediumBold, gdFontLarge, and
                gdFontGiant. You must include the files "gdfontt.h",
                "gdfonts.h", "gdfontmb.h", "gdfontl.h" and "gdfontg.h"
                respectively and (if you are not using a library-based
                approach) link with the corresponding .c files to use the
                provided fonts. The null-terminated C string specified by
                the fifth argument is drawn from left to right in the
                specified color. (See gdImageStringUp for a way of
                drawing vertical text.) Pixels not set by a particular
                character retain their previous color.
                

#include "gd.h"
#include "gdfontl.h"
#include <string.h>
... inside a function ...
gdImagePtr im;
int black;
int white;
/* String to draw. */
char *s = "Hello.";
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Draw a centered string. */
gdImageString(im, gdFontLarge,
        im->w / 2 - (strlen(s) * gdFontLarge->w / 2),
        im->h / 2 - gdFontLarge->h / 2,
        s, white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

        void gdImageString16(gdImagePtr im, gdFontPtr font, int x, int y,
                unsigned short *s, int color) (FUNCTION)
                gdImageString is used to draw multiple 16-bit characters
                on the image. (To draw single characters, use
                gdImageChar.) The second argument is a pointer to a font
                definition structure; five fonts are provided with gd,
                gdFontTiny, gdFontSmall, gdFontMediumBold, gdFontLarge,
                and gdFontGiant. You must include the files "gdfontt.h",
                "gdfonts.h", "gdfontmb.h", "gdfontl.h" and "gdfontg.h"
                respectively and (if you are not using a library-based
                approach) link with the corresponding .c files to use the
                provided fonts. The null-terminated string of characters
                represented as 16-bit unsigned short integers specified
                by the fifth argument is drawn from left to right in the
                specified color. (See gdImageStringUp16 for a way of
                drawing vertical text.) Pixels not set by a particular
                character retain their previous color.
                
                This function was added in gd1.3 to provide a means of
                rendering fonts with more than 256 characters for those
                who have them. A more frequently used routine is
                gdImageString.
                
        void gdImageStringUp(gdImagePtr im, gdFontPtr font, int x, int y,
                unsigned char *s, int color) (FUNCTION)
                gdImageStringUp is used to draw multiple characters on
                the image, rotated 90 degrees. (To draw single
                characters, use gdImageCharUp.) The second argument is a
                pointer to a font definition structure; five fonts are
                provided with gd, gdFontTiny, gdFontSmall,
                gdFontMediumBold, gdFontLarge, and gdFontGiant. You must
                include the files "gdfontt.h", "gdfonts.h", "gdfontmb.h",
                "gdfontl.h" and "gdfontg.h" respectively and (if you are
                not using a library-based approach) link with the
                corresponding .c files to use the provided fonts.The
                null-terminated C string specified by the fifth argument
                is drawn from bottom to top (rotated 90 degrees) in the
                specified color. (See gdImageString for a way of drawing
                horizontal text.) Pixels not set by a particular
                character retain their previous color.
                

#include "gd.h"
#include "gdfontl.h"
#include <string.h>
... inside a function ...
gdImagePtr im;
int black;
int white;
/* String to draw. */
char *s = "Hello.";
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Draw a centered string going upwards. Axes are reversed,
        and Y axis is decreasing as the string is drawn. */
gdImageStringUp(im, gdFontLarge,
        im->w / 2 - gdFontLarge->h / 2,
        im->h / 2 + (strlen(s) * gdFontLarge->w / 2),
        s, white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

        void gdImageStringUp16(gdImagePtr im, gdFontPtr font, int x, int
                y, unsigned short *s, int color) (FUNCTION)
                gdImageString is used to draw multiple 16-bit characters
                vertically on the image. (To draw single characters, use
                gdImageChar.) The second argument is a pointer to a font
                definition structure; five fonts are provided with gd,
                gdFontTiny, gdFontSmall, gdFontMediumBold, gdFontLarge,
                and gdFontGiant. You must include the files "gdfontt.h",
                "gdfonts.h", "gdfontmb.h", "gdfontl.h" and "gdfontg.h"
                respectively and (if you are not using a library-based
                approach) link with the corresponding .c files to use the
                provided fonts. The null-terminated string of characters
                represented as 16-bit unsigned short integers specified
                by the fifth argument is drawn from bottom to top in the
                specified color. (See gdImageStringUp16 for a way of
                drawing horizontal text.) Pixels not set by a particular
                character retain their previous color.
                
                This function was added in gd1.3 to provide a means of
                rendering fonts with more than 256 characters for those
                who have them. A more frequently used routine is
                gdImageStringUp.
                
  Color-handling functions
  
        int gdImageColorAllocate(gdImagePtr im, int r, int g, int b)
                (FUNCTION)
                gdImageColorAllocate finds the first available color
                index in the image specified, sets its RGB values to
                those requested (255 is the maximum for each), and
                returns the index of the new color table entry. When
                creating a new image, the first time you invoke this
                function, you are setting the background color for that
                image.
                
                In the event that all gdMaxColors colors (256) have
                already been allocated, gdImageColorAllocate will return
                -1 to indicate failure. (This is not uncommon when
                working with existing GIF files that already use 256
                colors.) Note that gdImageColorAllocate does not check
                for existing colors that match your request; see
                gdImageColorExact and gdImageColorClosest for ways to
                locate existing colors that approximate the color desired
                in situations where a new color is not available.
                

... inside a function ...
gdImagePtr im;
int black;
int red;
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color red. */
red = gdImageColorAllocate(im, 255, 0, 0);
/* Draw a dashed line from the upper left corner to the lower right corner. */
gdImageDashedLine(im, 0, 0, 99, 99, red);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

        int gdImageColorClosest(gdImagePtr im, int r, int g, int b)
                (FUNCTION)
                gdImageColorClosest searches the colors which have been
                defined thus far in the image specified and returns the
                index of the color with RGB values closest to those of
                the request. (Closeness is determined by Euclidian
                distance, which is used to determine the distance in
                three-dimensional color space between colors.)
                
                If no colors have yet been allocated in the image,
                gdImageColorClosest returns -1.
                
                This function is most useful as a backup method for
                choosing a drawing color when an image already contains
                gdMaxColors (256) colors and no more can be allocated.
                (This is not uncommon when working with existing GIF
                files that already use many colors.) See
                gdImageColorExact for a method of locating exact matches
                only.
                

... inside a function ...
gdImagePtr im;
FILE *in;
int red;
/* Let's suppose that photo.gif is a scanned photograph with
        many colors. */
in = fopen("photo.gif", "rb");
im = gdImageCreateFromGif(in);
fclose(in);
/* Try to allocate red directly */
red = gdImageColorAllocate(im, 255, 0, 0);
/* If we fail to allocate red... */
if (red == (-1)) {
        /* Find the closest color instead. */
        red = gdImageColorClosest(im, 255, 0, 0);
}
/* Draw a dashed line from the upper left corner to the lower right corner */
gdImageDashedLine(im, 0, 0, 99, 99, red);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

        int gdImageColorExact(gdImagePtr im, int r, int g, int b)
                (FUNCTION)
                gdImageColorExact searches the colors which have been
                defined thus far in the image specified and returns the
                index of the first color with RGB values which exactly
                match those of the request. If no allocated color matches
                the request precisely, gdImageColorExact returns -1. See
                gdImageColorClosest for a way to find the color closest
                to the color requested.
                

... inside a function ...
gdImagePtr im;
int red;
in = fopen("photo.gif", "rb");
im = gdImageCreateFromGif(in);
fclose(in);
/* The image may already contain red; if it does, we'll save a slot
        in the color table by using that color. */
/* Try to allocate red directly */
red = gdImageColorExact(im, 255, 0, 0);
/* If red isn't already present... */
if (red == (-1)) {
        /* Second best: try to allocate it directly. */
        red = gdImageColorAllocate(im, 255, 0, 0);
        /* Out of colors, so find the closest color instead. */
        red = gdImageColorClosest(im, 255, 0, 0);
}
/* Draw a dashed line from the upper left corner to the lower right corner */
gdImageDashedLine(im, 0, 0, 99, 99, red);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

        int gdImageColorsTotal(gdImagePtr im) (MACRO)
                gdImageColorsTotal is a macro which returns the number of
                colors currently allocated in the image. Use this macro
                to obtain this information; do not access the structure
                directly.
                
        int gdImageColorRed(gdImagePtr im, int c) (MACRO)
                gdImageColorRed is a macro which returns the red portion
                of the specified color in the image. Use this macro to
                obtain this information; do not access the structure
                directly.
                
        int gdImageColorGreen(gdImagePtr im, int c) (MACRO)
                gdImageColorGreen is a macro which returns the green
                portion of the specified color in the image. Use this
                macro to obtain this information; do not access the
                structure directly.
                
        int gdImageColorBlue(gdImagePtr im, int c) (MACRO)
                gdImageColorBlue is a macro which returns the green
                portion of the specified color in the image. Use this
                macro to obtain this information; do not access the
                structure directly.
                
        int gdImageGetInterlaced(gdImagePtr im) (MACRO)
                gdImageGetInterlaced is a macro which returns true (1) if
                the image is interlaced, false (0) if not. Use this macro
                to obtain this information; do not access the structure
                directly. See gdImageInterlace for a means of interlacing
                images.
                
        int gdImageGetTransparent(gdImagePtr im) (MACRO)
                gdImageGetTransparent is a macro which returns the
                current transparent color index in the image. If there is
                no transparent color, gdImageGetTransparent returns -1.
                Use this macro to obtain this information; do not access
                the structure directly.
                
        void gdImageColorDeallocate(gdImagePtr im, int color) (FUNCTION)
                gdImageColorDeallocate marks the specified color as being
                available for reuse. It does not attempt to determine
                whether the color index is still in use in the image.
                After a call to this function, the next call to
                gdImageColorAllocate for the same image will set new RGB
                values for that color index, changing the color of any
                pixels which have that index as a result. If multiple
                calls to gdImageColorDeallocate are made consecutively,
                the lowest-numbered index among them will be reused by
                the next gdImageColorAllocate call.
                

... inside a function ...
gdImagePtr im;
int red, blue;
in = fopen("photo.gif", "rb");
im = gdImageCreateFromGif(in);
fclose(in);
/* Look for red in the color table. */
red = gdImageColorExact(im, 255, 0, 0);
/* If red is present... */
if (red != (-1)) {
        /* Deallocate it. */
        gdImageColorDeallocate(im, red);
        /* Allocate blue, reusing slot in table.
                Existing red pixels will change color. */
        blue = gdImageColorAllocate(im, 0, 0, 255);
}
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

        void gdImageColorTransparent(gdImagePtr im, int color) (FUNCTION)
                
                gdImageColorTransparent sets the transparent color index
                for the specified image to the specified index. To
                indicate that there should be no transparent color,
                invoke gdImageColorTransparent with a color index of -1.
                
                The color index used should be an index allocated by
                gdImageColorAllocate, whether explicitly invoked by your
                code or implicitly invoked by loading an image. In order
                to ensure that your image has a reasonable appearance
                when viewed by users who do not have transparent
                background capabilities, be sure to give reasonable RGB
                values to the color you allocate for use as a transparent
                color, even though it will be transparent on systems that
                support transparency.
                

... inside a function ...
gdImagePtr im;
int black;
FILE *in, *out;
in = fopen("photo.gif", "rb");
im = gdImageCreateFromGif(in);
fclose(in);
/* Look for black in the color table and make it transparent. */
black = gdImageColorExact(im, 0, 0, 0);
/* If black is present... */
if (black != (-1)) {
        /* Make it transparent */
        gdImageColorTransparent(im, black);
}
/* Save the newly-transparent image back to the file */
out = fopen("photo.gif", "wb");
gdImageGif(im, out);
fclose(out);
/* Destroy it */
gdImageDestroy(im);

  Copying and resizing functions
  
        void gdImageCopy(gdImagePtr dst, gdImagePtr src, int dstX, int
                dstY, int srcX, int srcY, int w, int h) (FUNCTION)
                gdImageCopy is used to copy a rectangular portion of one
                image to another image. (For a way of stretching or
                shrinking the image in the process, see
                gdImageCopyResized.)
                
                The dst argument is the destination image to which the
                region will be copied. The src argument is the source
                image from which the region is copied. The dstX and dstY
                arguments specify the point in the destination image to
                which the region will be copied. The srcX and srcY
                arguments specify the upper left corner of the region in
                the source image. The w and h arguments specify the width
                and height of the region.
                
                When you copy a region from one location in an image to
                another location in the same image, gdImageCopy will
                perform as expected unless the regions overlap, in which
                case the result is unpredictable.
                
                Important note on copying between images: since different
                images do not necessarily have the same color tables,
                pixels are not simply set to the same color index values
                to copy them. gdImageCopy will attempt to find an
                identical RGB value in the destination image for each
                pixel in the copied portion of the source image by
                invoking gdImageColorExact. If such a value is not found,
                gdImageCopy will attempt to allocate colors as needed
                using gdImageColorAllocate. If both of these methods
                fail, gdImageCopy will invoke gdImageColorClosest to find
                the color in the destination image which most closely
                approximates the color of the pixel being copied.
                

... Inside a function ...
gdImagePtr im_in;
gdImagePtr im_out;
int x, y;
FILE *in;
FILE *out;
/* Load a small gif to tile the larger one with */
in = fopen("small.gif", "rb");
im_in = gdImageCreateFromGif(in);
fclose(in);
/* Make the output image four times as large on both axes */
im_out = gdImageCreate(im_in->sx * 4, im_in->sy * 4);
/* Now tile the larger image using the smaller one */
for (y = 0; (y < 4); y++) {
        for (x = 0; (x < 4); x++) {
                gdImageCopy(im_out, im_in,
                        x * im_in->sx, y * im_in->sy,
                        0, 0,
                        im_in->sx, im_in->sy);
        }
}
out = fopen("tiled.gif", "wb");
gdImageGif(im_out, out);
fclose(out);
gdImageDestroy(im_in);
gdImageDestroy(im_out);

        void gdImageCopyResized(gdImagePtr dst, gdImagePtr src, int dstX,
                int dstY, int srcX, int srcY, int destW, int destH, int
                srcW, int srcH) (FUNCTION)
                gdImageCopyResized is used to copy a rectangular portion
                of one image to another image. The X and Y dimensions of
                the original region and the destination region can vary,
                resulting in stretching or shrinking of the region as
                appropriate. (For a simpler version of this function
                which does not deal with resizing, see gdImageCopy.)
                
                The dst argument is the destination image to which the
                region will be copied. The src argument is the source
                image from which the region is copied. The dstX and dstY
                arguments specify the point in the destination image to
                which the region will be copied. The srcX and srcY
                arguments specify the upper left corner of the region in
                the source image. The dstW and dstH arguments specify the
                width and height of the destination region. The srcW and
                srcH arguments specify the width and height of the source
                region and can differ from the destination size, allowing
                a region to be scaled during the copying process.
                
                When you copy a region from one location in an image to
                another location in the same image, gdImageCopy will
                perform as expected unless the regions overlap, in which
                case the result is unpredictable. If this presents a
                problem, create a scratch image in which to keep
                intermediate results.
                
                Important note on copying between images: since images do
                not necessarily have the same color tables, pixels are
                not simply set to the same color index values to copy
                them. gdImageCopy will attempt to find an identical RGB
                value in the destination image for each pixel in the
                copied portion of the source image by invoking
                gdImageColorExact. If such a value is not found,
                gdImageCopy will attempt to allocate colors as needed
                using gdImageColorAllocate. If both of these methods
                fail, gdImageCopy will invoke gdImageColorClosest to find
                the color in the destination image which most closely
                approximates the color of the pixel being copied.
                

... Inside a function ...
gdImagePtr im_in;
gdImagePtr im_out;
int x, y;
FILE *in;
FILE *out;
/* Load a small gif to expand in the larger one */
in = fopen("small.gif", "rb");
im_in = gdImageCreateFromGif(in);
fclose(in);
/* Make the output image four times as large on both axes */
im_out = gdImageCreate(im_in->sx * 4, im_in->sy * 4);
/* Now copy the smaller image, but four times larger */
gdImageCopyResized(im_out, im_in, 0, 0, 0, 0,
        im_out->sx, im_out->sy,
        im_in->sx, im_in->sy);
out = fopen("large.gif", "wb");
gdImageGif(im_out, out);
fclose(out);
gdImageDestroy(im_in);
gdImageDestroy(im_out);

  Miscellaneous Functions
  
              gdImageInterlace(gdImagePtr im, int interlace) (FUNCTION)
                      gdImageInterlace is used to determine whether an
                      image should be stored in a linear fashion, in
                      which lines will appear on the display from first
                      to last, or in an interlaced fashion, in which the
                      image will "fade in" over several passes. By
                      default, images are not interlaced.
                      
                      A nonzero value for the interlace argument turns on
                      interlace; a zero value turns it off. Note that
                      interlace has no effect on other functions, and has
                      no meaning unless you save the image in GIF format;
                      the gd and xbm formats do not support interlace.
                      
                      When a GIF is loaded with gdImageCreateFromGif ,
                      interlace will be set according to the setting in
                      the GIF file.
                      
                      Note that many GIF viewers and web browsers do not
                      support interlace. However, the interlaced GIF
                      should still display; it will simply appear all at
                      once, just as other images do.
                      

gdImagePtr im;
FILE *out;
/* ... Create or load the image... */

/* Now turn on interlace */
gdImageInterlace(im, 1);
/* And open an output file */
out = fopen("test.gif", "wb");
/* And save the image */
gdImageGif(im, out);
fclose(out);
gdImageDestroy(im);

  Constants
  
              gdBrushed (CONSTANT)
                      Used in place of a color when invoking a
                      line-drawing function such as gdImageLine or
                      gdImageRectangle. When gdBrushed is used as the
                      color, the brush image set with gdImageSetBrush is
                      drawn in place of each pixel of the line (the brush
                      is usually larger than one pixel, creating the
                      effect of a wide paintbrush). See also
                      gdStyledBrushed for a way to draw broken lines with
                      a series of distinct copies of an image.
                      
              gdMaxColors(CONSTANT)
                      The constant 256. This is the maximum number of
                      colors in a GIF file according to the GIF standard,
                      and is also the maximum number of colors in a gd
                      image.
                      
              gdStyled (CONSTANT)
                      Used in place of a color when invoking a
                      line-drawing function such as gdImageLine or
                      gdImageRectangle. When gdStyled is used as the
                      color, the colors of the pixels are drawn
                      successively from the style that has been set with
                      gdImageSetStyle. If the color of a pixel is equal
                      to gdTransparent, that pixel is not altered. (This
                      mechanism is completely unrelated to the
                      "transparent color" of the image itself; see
                      gdImageColorTransparent gdImageColorTransparent for
                      that mechanism.) See also gdStyledBrushed.
                      
              gdStyledBrushed (CONSTANT)
                      Used in place of a color when invoking a
                      line-drawing function such as gdImageLine or
                      gdImageRectangle. When gdStyledBrushed is used as
                      the color, the brush image set with gdImageSetBrush
                      is drawn at each pixel of the line, providing that
                      the style set with gdImageSetStyle contains a
                      nonzero value (OR gdTransparent, which does not
                      equal zero but is supported for consistency) for
                      the current pixel. (Pixels are drawn successively
                      from the style as the line is drawn, returning to
                      the beginning when the available pixels in the
                      style are exhausted.) Note that this differs from
                      the behavior of gdStyled, in which the values in
                      the style are used as actual pixel colors, except
                      for gdTransparent.
                      
              gdDashSize (CONSTANT)
                      The length of a dash in a dashed line. Defined to
                      be 4 for backwards compatibility with programs that
                      use gdImageDashedLine. New programs should use
                      gdImageSetStyle and call the standard gdImageLine
                      function with the special "color" gdStyled or
                      gdStyledBrushed.
                      
              gdTiled (CONSTANT)
                      Used in place of a normal color in
                      gdImageFilledRectangle, gdImageFilledPolygon,
                      gdImageFill, and gdImageFillToBorder. gdTiled
                      selects a pixel from the tile image set with
                      gdImageSetTile in such a way as to ensure that the
                      filled area will be tiled with copies of the tile
                      image. See the discussions of gdImageFill and
                      gdImageFillToBorder for special restrictions
                      regarding those functions.
                      
              gdTransparent (CONSTANT)
                      Used in place of a normal color in a style to be
                      set with gdImageSetStyle. gdTransparent is not the
                      transparent color index of the image; for that
                      functionality please see gdImageColorTransparent.
                      
  About the additional .gd image file format
  
                      In addition to reading and writing the GIF format
                      and reading the X Bitmap format, gd has the
                      capability to read and write its own ".gd" format.
                      This format is not intended for general purpose use
                      and should never be used to distribute images. It
                      is not a compressed format. Its purpose is solely
                      to allow very fast loading of images your program
                      needs often in order to build other images for
                      output. If you are experiencing performance
                      problems when loading large, fixed GIF images your
                      program needs to produce its output images, you may
                      wish to examine the functions gdImageCreateFromGd
                      and gdImageGd, which read and write .gd format
                      images.
                      
                      The program "giftogd.c" is provided as a simple way
                      of converting .gif files to .gd format. I emphasize
                      again that you will not need to use this format
                      unless you have a need for high-speed loading of a
                      few frequently-used images in your program.
                      
  Please tell us you're using gd!
  
                      When you contact us and let us know you are using
                      gd, you help us justify the time spent in
                      maintaining and improving it. So please let us
                      know. If the results are publicly visible on the
                      web, a URL is a wonderful thing to receive, but if
                      it's not a publicly visible project, a simple note
                      is just as welcome.
                      
  If you have problems
  
                      If you have any difficulties with gd, feel free to
                      contact the author, Thomas Boutell. Be sure to read
                      this manual carefully first.
                      
  Alphabetical quick index
  
                      gdBrushed | gdDashSize | gdFont | gdFontPtr |
                      gdImage | gdImageArc | gdImageBlue |
                      gdImageBoundsSafe | gdImageChar | gdImageCharUp |
                      gdImageColorAllocate | gdImageColorClosest |
                      gdImageColorDeallocate | gdImageColorExact |
                      gdImageColorTransparent | gdImageCopy |
                      gdImageCopyResized | gdImageCreate |
                      gdImageCreateFromGd | gdImageCreateFromGif |
                      gdImageCreateFromXbm | gdImageDashedLine |
                      gdImageDestroy | gdImageFill | gdImageFillToBorder
                      | gdImageFilledRectangle | gdImageGd |
                      gdImageGetInterlaced | gdImageGetPixel |
                      gdImageGetTransparent | gdImageGif | gdImageGreen |
                      gdImageInterlace | gdImageLine |
                      gdImageFilledPolygon | gdImagePolygon | gdImagePtr
                      | gdImageRectangle | gdImageRed | gdImageSetBrush |
                      gdImageSetPixel | gdImageSetStyle | gdImageSetTile
                      | gdImageString | gdImageString16 | gdImageStringUp
                      | gdImageStringUp16 | gdMaxColors | gdPoint |
                      gdStyled | gdStyledBrushed | gdTiled |
                      gdTransparent
                      
                      Boutell.Com, Inc.

                                   gd 1.7.3
                                       
A graphics library for fast image creation

Follow this link to the latest version of this document.

     _HEY! READ THIS!_ gd 1.7.3 creates PNG images, not GIF images. This
     is a good thing. PNG is a more compact format, and full compression
     is available. Existing code will need modification to call
     gdImagePng instead of gdImageGif. _Please do not ask us to send you
     the old GIF version of GD._ Unisys holds a patent on the LZW
     compression algorithm, which is used in fully compressed GIF
     images. We are still investigating the legal issues surrounding
     various alternative means of producing a valid GIF file.
     
     gd 1.7.3 _requires_ that the following libraries also be installed:
     
     libpng
     
     zlib
     
     If you want to use the TrueType font support, you must also install
     the _Freetype library_, including the _freetype.h header file_. See
     the Freetype Home Page. No, I cannot explain why that site is down
     on a particular day, and no, I can't send you a copy.
     
     If you want to use the Xpm color bitmap loading support, you must
     also have the X Window System and the Xpm library installed (Xpm is
     often included in modern X distributions).
     
     Please read the documentation and install the required libraries.
     Do not send email asking why png.h is not found. See the
     requirements section for more information. Thank you!
     
  Table of Contents
  
     * Credits and license terms
     * What's new in version 1.7.3?
     * What's new in version 1.7.2?
     * What's new in version 1.7.1?
     * What's new in version 1.7?
     * What's new in version 1.6.3?
     * What's new in version 1.6.2?
     * What's new in version 1.6.1?
     * What's new in version 1.6?
     * What is gd?
     * What if I want to use another programming language?
     * What else do I need to use gd?
     * How do I get gd?
     * How do I build gd?
     * gd basics: using gd in your program
     * webpng: a useful example
     * Function and type reference by category
     * About the additional .gd image file format
     * Please tell us you're using gd!
     * If you have problems
     * Alphabetical quick index
       
   Up to the Boutell.Com, Inc. Home Page
   
  Credits and license terms
  
   In order to resolve any possible confusion regarding the authorship of
   gd, the following copyright statement covers all of the authors who
   have required such a statement. _If you are aware of any oversights in
   this copyright notice, please contact Thomas Boutell who will be
   pleased to correct them._

COPYRIGHT STATEMENT FOLLOWS THIS LINE

     Portions copyright 1994, 1995, 1996, 1997, 1998, 1999, by Cold
     Spring Harbor Laboratory. Funded under Grant P41-RR02188 by the
     National Institutes of Health.
     
     Portions copyright 1996, 1997, 1998, 1999, by Boutell.Com, Inc.
     
     Portions relating to GD2 format copyright 1999 Philip Warner.
     
     Portions relating to PNG copyright 1999, Greg Roelofs.
     
     Portions relating to libttf copyright 1999, John Ellson
     (ellson@lucent.com).
     
     _Permission has been granted to copy and distribute gd in any
     context without fee, including a commercial application, provided
     that this notice is present in user-accessible supporting
     documentation._
     
     This does not affect your ownership of the derived work itself, and
     the intent is to assure proper credit for the authors of gd, not to
     interfere with your productive use of gd. If you have questions,
     ask. "Derived works" includes all programs that utilize the
     library. Credit must be given in user-accessible documentation.
     
     _This software is provided "AS IS."_ The copyright holders disclaim
     all warranties, either express or implied, including but not
     limited to implied warranties of merchantability and fitness for a
     particular purpose, with respect to this code and accompanying
     documentation.
     
     Although their code does not appear in gd 1.7.3, the authors wish
     to thank David Koblas, David Rowley, and Hutchison Avenue Software
     Corporation for their prior contributions.
     
END OF COPYRIGHT STATEMENT

  What is gd?
  
   gd is a graphics library. It allows your code to quickly draw images
   complete with lines, arcs, text, multiple colors, cut and paste from
   other images, and flood fills, and write out the result as a .PNG
   file. This is particularly useful in World Wide Web applications,
   where .PNG is one of the formats accepted for inline images by most
   browsers.
   
   gd is not a paint program. If you are looking for a paint program, you
   are looking in the wrong place. If you are not a programmer, you are
   looking in the wrong place.
   
   gd does not provide for every possible desirable graphics operation.
   It is not necessary or desirable for gd to become a kitchen-sink
   graphics package, but version 1.7.3 incorporates most of the commonly
   requested features for an 8-bit 2D package. Support for truecolor
   images, JPEG and truecolor PNG is planned for version 2.0.
   
  What if I want to use another programming language?
  
    Perl
    
   gd can also be used from Perl, courtesy of Lincoln Stein's GD.pm
   library, which uses gd as the basis for a set of Perl 5.x classes.
   Updated to gd 1.6 and up.
   
    Tcl
    
   gd can be used from Tcl with John Ellson's Gdtclft dynamically loaded
   extension package. (Gdtclft2.0 or later is needed for gd-1.6 and up
   with PNG output.)
   
    Any Language
    
   There are, at the moment, at least three simple interpreters that
   perform gd operations. You can output the desired commands to a simple
   text file from whatever scripting language you prefer to use, then
   invoke the interpreter.
   
   These packages have not been updated to gd 1.6 and up as of this
   writing.
     * tgd, by Bradley K. Sherman
     * fly, by Martin Gleeson
       
  What's new in version 1.7.3?
  
   Another attempt at Makefile fixes to permit linking with all libraries
   required on platforms with order- dependent linkers. Perhaps it will
   work this time.
   
  What's new in version 1.7.2?
  
   An uninitialized-pointer bug in gdtestttf.c was corrected. This bug
   caused crashes at the end of each call to gdImageStringTTF on some
   platforms. Thanks to Wolfgang Haefelinger.
   
   Documentation fixes. Thanks to Dohn Arms.
   
   Makefile fixes to permit linking with all libraries required on
   platforms with order- dependent linkers.
   
  What's new in version 1.7.1?
  
   A minor buglet in the Makefile was corrected, as well as an inaccurate
   error message in gdtestttf.c. Thanks to Masahito Yamaga.
   
  What's new in version 1.7?
  
   Version 1.7 contains the following changes:
     * Japanese language support for the TrueType functions. Thanks to
       Masahito Yamaga.
     * autoconf and configure have been removed, in favor of a carefully
       designed Makefile which produces and properly installs the library
       and the binaries. System-dependent variables are at the top of the
       Makefile for easy modification. I'm sorry, folks, but autoconf
       generated _many, many confused email messages_ from people who
       didn't have things where autoconf expected to find them. I am not
       an autoconf/automake wizard, and gd is a simple, very compact
       library which does not need to be a shared library. I _did_ make
       many improvements over the old gd 1.3 Makefile, which were
       directly inspired by the autoconf version found in the 1.6 series
       (thanks to John Ellson).
     * Completely ANSI C compliant, according to the -pedantic-errors
       flag of gcc. Several pieces of not-quite-ANSI-C code were causing
       problems for those with non-gcc compilers.
     * gdttf.c patched to allow the use of Windows symbol fonts, when
       present (thanks to Joseph Peppin).
     * extern "C" wrappers added to gd.h and the font header files for
       the convenience of C++ programmers. bdftogd was also modified to
       automatically insert these wrappers into future font header files.
       Thanks to John Lindal.
     * Compiles correctly on platforms that don't define SEEK_SET. Thanks
       to Robert Bonomi.
     * Loads Xpm images via the gdImageCreateFromXpm function, if the Xpm
       library is available. Thanks to Caolan McNamara.
       
  What's new in version 1.6.3?
  
   Version 1.6.3 corrects a memory leak in gd_png.c. This leak caused a
   significant amount of memory to be allocated and not freed when
   writing a PNG image.
   
  What's new in version 1.6.2?
  
   Version 1.6.2 from John Ellson adds two new functions:
     * gdImageStringTTF - scalable, rotatable, anti-aliased, TrueType
       strings using the FreeType library, but only if libttf is found by
       configure. _We do not provide TrueType fonts. Obtaining them is
       entirely up to you._
     * gdImageColorResolve - an efficient alternative for the common code
       fragment:


      if ((color=gdImageColorExact(im,R,G,B)) < 0)
          if ((color=gdImageColorAllocate(im,R,G,B)) < 0)
              color=gdImageColorClosest(im,R,G,B);

   Also in this release the build process has been converted to GNU
   autoconf/automake/libtool conventions so that both (or either) static
   and shared libraries can be built.
   
  What's new in version 1.6.1?
  
   Version 1.6.1 incorporates superior PNG reading and writing code from
   Greg Roelofs, with minor modifications by Tom Boutell. Specifically, I
   altered his code to read non-palette images (converting them to
   palette images badly, by dithering them), and to tolerate palette
   images with types of transparency that gd doesn't actually support (it
   just ignores the advanced transparency features). Any bugs in this
   area are therefore my fault, not Greg's.
   
   Unlike gd 1.6, users should have no trouble linking with gd 1.6.1 if
   they follow the instructions and install all of the pieces. However,
   _If you get undefined symbol errors, be sure to check for older
   versions of libpng in your library directories!_
   
  What's new in version 1.6?
  
   Version 1.6 features the following changes:
   
   _Support for 8-bit palette PNG images has been added. Support for GIF
   has been removed._ This step was taken to completely avoid the legal
   controversy regarding the LZW compression algorithm used in GIF.
   Unisys holds a patent which is relevant to LZW compression. PNG is a
   superior image format in any case. Now that PNG is supported by both
   Microsoft Internet Explorer and Netscape (in their recent releases),
   we highly recommend that GD users upgrade in order to get
   well-compressed images in a format which is legally unemcumbered.
   
  What's new in version 1.5?
  
   Version 1.5 featured the following changes:
   
   _New GD2 format_
          An improvement over the GD format, the GD2 format uses the zlib
          compression library to compress the image in chunks. This
          results in file sizes comparable to GIFs, with the ability to
          access parts of large images without having to read the entire
          image into memory.
          
          This format also supports version numbers and rudimentary
          validity checks, so it should be more 'supportable' than the
          previous GD format.
          
   _Re-arranged source files_
          gd.c has been broken into constituant parts: io, gif, gd, gd2
          and graphics functions are now in separate files.
          
   _Extended I/O capabilities._
          The source/sink feature has been extended to support GD2 file
          formats (which require seek/tell functions), and to allow more
          general non-file I/O.
          
   _Better support for Lincoln Stein's Perl Module_
          The new gdImage*Ptr function returns the chosen format stored
          in a block of memory. This can be directly used by the GD perl
          module.
          
   _Added functions_
          gdImageCreateFromGd2Part - allows retrieval of part of an image
          (good for huge images, like maps),
          gdImagePaletteCopy - Copies a palette from one image to
          another, doing it's best to match the colors in the target
          image to the colors in the source palette.
          gdImageGd2, gdImageCreateFromGd2 - Support for new format
          gdImageCopyMerge - Merges two images (useful to highlight part
          of an image)
          gdImageCopyMergeGray - Similar to gdImageCopyMerge, but tries
          to preserve source image hue.
          gdImagePngPtr, gdImageGdPtr, gdImageGd2Ptr - return memort
          blocks for each type of image.
          gdImageCreateFromPngCtx, gdImageCreateFromGdCtx,
          gdImageCreateFromGd2Ctx, gdImageCreateFromGd2PartCtx - Support
          for new I/O context.
          
   _NOTE:_ In fairness to Thomas Boutell, any bug/problems with any of
   the above features should probably be reported to Philip Warner.
   
  What's new in version 1.4?
  
   Version 1.4 features the following changes:
   
   Fixed polygon fill routine (again)
          Thanks to Kirsten Schulz, version 1.4 is able to fill numerous
          types of polygons that caused problems with previous releases,
          including version 1.3.
          
   Support for alternate data sources
          Programmers who wish to load a GIF from something other than a
          stdio FILE * stream can use the new gdImageCreateFromPngSource
          function.
          
   Support for alternate data destinations
          Programmers who wish to write a GIF to something other than a
          stdio FILE * stream can use the new gdImagePngToSink function.
          
   More tolerant when reading GIFs
          Version 1.4 does not crash when reading certain animated GIFs,
          although it still only reads the first frame. Version 1.4 also
          has overflow testing code to prevent crashes when reading
          damaged GIFs.
          
  What's new in version 1.3?
  
   Version 1.3 features the following changes:
   
   Non-LZW-based GIF compression code
          Version 1.3 contained GIF compression code that uses simple Run
          Length Encoding instead of LZW compression, while still
          retaining compatibility with normal LZW-based GIF decoders
          (your browser will still like your GIFs). _LZW compression is
          patented by Unisys. We are currently reevaluating the approach
          taken by gd 1.3. The current release of gd does not support
          this approach. We recommend that you use the current release,
          and generate PNG images._ Thanks to Hutchison Avenue Software
          Corporation for contributing the RLE GIF code.
          
   8-bit fonts, and 8-bit font support
          This improves support for European languages. Thanks are due to
          Honza Pazdziora and also to Jan Pazdziora . Also see the
          provided bdftogd Perl script if you wish to convert fixed-width
          X11 fonts to gd fonts.
          
   16-bit font support (no fonts provided)
          Although no such fonts are provided in the distribution, fonts
          containing more than 256 characters should work if the
          gdImageString16 and gdImageStringUp16 routines are used.
          
   Improvements to the "webpng" example/utility
          The "webpng" utility is now a slightly more useful application.
          Thanks to Brian Dowling for this code.
          
   Corrections to the color resolution field of GIF output
          Thanks to Bruno Aureli.
          
   Fixed polygon fills
          A one-line patch for the infamous polygon fill bug, courtesy of
          Jim Mason. I believe this fix is sufficient. However, if you
          find a situation where polygon fills still fail to behave
          properly, please send code that demonstrates the problem, _and_
          a fix if you have one. Verifying the fix is important.
          
   Row-major, not column-major
          Internally, gd now represents the array of pixels as an array
          of rows of pixels, rather than an array of columns of pixels.
          This improves the performance of compression and decompression
          routines slightly, because horizontally adjacent pixels are now
          next to each other in memory. _This should not affect properly
          written gd applications, but applications that directly
          manipulate the pixels array will require changes._
          
  What else do I need to use gd?
  
   To use gd, you will need an ANSI C compiler. _All popular Windows 95
   and NT C compilers are ANSI C compliant._ Any full-ANSI-standard C
   compiler should be adequate. _The cc compiler released with SunOS
   4.1.3 is not an ANSI C compiler. Most Unix users who do not already
   have gcc should get it. gcc is free, ANSI compliant and a de facto
   industry standard. Ask your ISP why it is missing._
   
   As of version 1.6, you also need the zlib compression library, and the
   libpng library. As of version 1.6.2, you can draw text using
   antialiased TrueType fonts if you also have the libttf library
   installed, but this is not mandatory. zlib is available for a variety
   of platforms from the zlib web site. libpng is available for a variety
   of platforms from the PNG web site.
   
   You will also want a PNG viewer, if you do not already have one for
   your system, since you will need a good way to check the results of
   your work. Netscape 4.04 and higher, and Microsoft Internet Explorer
   4.0 or higher, both support PNG. For some purposes you might be
   happier with a package like Lview Pro for Windows or xv for X. There
   are PNG viewers available for every graphics-capable modern operating
   system, so consult newsgroups relevant to your particular system.
   
  How do I get gd?
  
    By HTTP
    
     * Gzipped Tar File (Unix)
     * .ZIP File (Windows)
       
    By FTP
    
     * Gzipped Tar File (Unix)
     * .ZIP File (Windows)
       
  How do I build gd?
  
   In order to build gd, you must first unpack the archive you have
   downloaded. If you are not familiar with tar and gunzip (Unix) or ZIP
   (Windows), please consult with an experienced user of your system.
   Sorry, we cannot answer questions about basic Internet skills.
   
   Unpacking the archive will produce a directory called "gd-1.7.3".
   
    For Unix
    
   cd to the 1.7.3 directory. Edit the Makefile with your preferred text
   editor and make any necessary changes to the settings at the top,
   especially if you want Xpm or TrueType support. Next, type "make". If
   you are the system administrator, and you wish to make the gd library
   available to other programs, you may also wish to type "make install".
   
   If you get errors, edit the Makefile again, paying special attention
   to the INCLUDEDIRS and LIBDIRS settings.
   
    For Windows, Mac, Et Cetera
    
   Create a project using your favorite programming environment. Copy all
   of the gd files to the project directory. Add gd.c to your project.
   Add other source files as appropriate. Learning the basic skills of
   creating projects with your chosen C environment is up to you.
   
   You have now built both the gd library and a demonstration program
   which shows off the capabilities of gd. To see it in action, type
   "gddemo".
   
   gddemo should execute without incident, creating the file demoout.png.
   (Note there is also a file named demoin.png, which is provided in the
   package as part of the demonstration.)
   
   Display demoout.png in your PNG viewer. The image should be 128x128
   pixels and should contain an image of the space shuttle with quite a
   lot of graphical elements drawn on top of it.
   
   (If you are missing the demoin.png file, the other items should appear
   anyway.)
   
   Look at demoin.png to see the original space shuttle image which was
   scaled and copied into the output image.
   
  gd basics: using gd in your program
  
   gd lets you create PNG images on the fly. To use gd in your program,
   include the file gd.h, and link with the libgd.a library produced by
   "make libgd.a", under Unix. Under other operating systems you will add
   gd.c to your own project.
   
   If you want to use the provided fonts, include gdfontt.h, gdfonts.h,
   gdfontmb.h, gdfontl.h and/or gdfontg.h. For more impressive results,
   install libttf and use the new gdImageStringTTF function. If you are
   not using the provided Makefile and/or a library-based approach, be
   sure to include the source modules as well in your project. (They may
   be too large for 16-bit memory models, that is, 16-bit DOS and
   Windows.)
   
   Here is a short example program. _(For a more advanced example, see
   gddemo.c, included in the distribution. gddemo.c is NOT the same
   program; it demonstrates additional features!)_
   
/* Bring in gd library functions */
#include "gd.h"

/* Bring in standard I/O so we can output the PNG to a file */
#include <stdio.h>

int main() {
        /* Declare the image */
        gdImagePtr im;
        /* Declare an output file */
        FILE *out;
        /* Declare color indexes */
        int black;
        int white;

        /* Allocate the image: 64 pixels across by 64 pixels tall */
        im = gdImageCreate(64, 64);

        /* Allocate the color black (red, green and blue all minimum).
                Since this is the first color in a new image, it will
                be the background color. */
        black = gdImageColorAllocate(im, 0, 0, 0);

        /* Allocate the color white (red, green and blue all maximum). */
        white = gdImageColorAllocate(im, 255, 255, 255);
        
        /* Draw a line from the upper left to the lower right,
                using white color index. */
        gdImageLine(im, 0, 0, 63, 63, white);

        /* Open a file for writing. "wb" means "write binary", important
                under MSDOS, harmless under Unix. */
        out = fopen("test.png", "wb");

        /* Output the image to the disk file. */
        gdImagePng(im, out);

        /* Close the file. */
        fclose(out);

        /* Destroy the image in memory. */
        gdImageDestroy(im);
}

   When executed, this program creates an image, allocates two colors
   (the first color allocated becomes the background color), draws a
   diagonal line (note that 0, 0 is the upper left corner), writes the
   image to a PNG file, and destroys the image.
   
   The above example program should give you an idea of how the package
   works. gd provides many additional functions, which are listed in the
   following reference chapters, complete with code snippets
   demonstrating each. There is also an alphabetical index.
   
  Webpng: a more powerful gd example
  
   Webpng is a simple utility program to manipulate PNGs from the command
   line. It is written for Unix and similar command-line systems, but
   should be easily adapted for other environments. Webpng allows you to
   set transparency and interlacing and output interesting information
   about the PNG in question.
   
   webpng.c is provided in the distribution. Unix users can simply type
   "make webpng" to compile the program. Type "webpng" with no arguments
   to see the available options.
   
Function and type reference

     * Types
     * Image creation, destruction, loading and saving
     * Drawing, styling, brushing, tiling and filling functions
     * Query functions (not color-related)
     * Font and text-handling functions
     * Color handling functions
     * Copying and resizing functions
     * Miscellaneous Functions
     * Constants
       
  Types
  
   gdImage_(TYPE)_
          The data structure in which gd stores images. gdImageCreate
          returns a pointer to this type, and the other functions expect
          to receive a pointer to this type as their first argument. You
          may read the members sx (size on X axis), sy (size on Y axis),
          colorsTotal (total colors), red (red component of colors; an
          array of 256 integers between 0 and 255), green (green
          component of colors, as above), blue (blue component of colors,
          as above), and transparent (index of transparent color, -1 if
          none); please do so using the macros provided. Do NOT set the
          members directly from your code; use the functions provided.
          

typedef struct {
        unsigned char ** pixels;
        int sx;
        int sy;
        int colorsTotal;
        int red[gdMaxColors];
        int green[gdMaxColors];
        int blue[gdMaxColors];
        int open[gdMaxColors];
        int transparent;
} gdImage;

   gdImagePtr _(TYPE)_
          A pointer to an image structure. gdImageCreate returns this
          type, and the other functions expect it as the first argument.
          
   gdFont _(TYPE)_
          A font structure. Used to declare the characteristics of a
          font. Plese see the files gdfontl.c and gdfontl.h for an
          example of the proper declaration of this structure. You can
          provide your own font data by providing such a structure and
          the associated pixel array. You can determine the width and
          height of a single character in a font by examining the w and h
          members of the structure. If you will not be creating your own
          fonts, you will not need to concern yourself with the rest of
          the components of this structure.
          

typedef struct {
        /* # of characters in font */
        int nchars;
        /* First character is numbered... (usually 32 = space) */
        int offset;
        /* Character width and height */
        int w;
        int h;
        /* Font data; array of characters, one row after another.
                Easily included in code, also easily loaded from
                data files. */
        char *data;
} gdFont;

   gdFontPtr _(TYPE)_
          A pointer to a font structure. Text-output functions expect
          these as their second argument, following the gdImagePtr
          argument. Two such pointers are declared in the provided
          include files gdfonts.h and gdfontl.h.
          
   gdPoint _(TYPE)_
          Represents a point in the coordinate space of the image; used
          by gdImagePolygon and gdImageFilledPolygon.
          

typedef struct {
        int x, y;
} gdPoint, *gdPointPtr;

   gdPointPtr _(TYPE)_
          A pointer to a gdPoint structure; passed as an argument to
          gdImagePolygon and gdImageFilledPolygon.
          
   gdSource _(TYPE)_

typedef struct {
        int (*source) (void *context, char *buffer, int len);
        void *context;
} gdSource, *gdSourcePtr;

   Represents a source from which a PNG can be read. Programmers who do
   not wish to read PNGs from a file can provide their own alternate
   input mechanism, using the gdImageCreateFromPngSource function. See
   the documentation of that function for an example of the proper use of
   this type.
   
   gdSink _(TYPE)_

typedef struct {
        int (*sink) (void *context, char *buffer, int len);
        void *context;
} gdSink, *gdSinkPtr;

   Represents a "sink" (destination) to which a PNG can be written.
   Programmers who do not wish to write PNGs to a file can provide their
   own alternate output mechanism, using the gdImagePngToSink function.
   See the documentation of that function for an example of the proper
   use of this type.
   
  Image creation, destruction, loading and saving
  
   gdImageCreate(sx, sy) _(FUNCTION)_
          gdImageCreate is called to create images. Invoke gdImageCreate
          with the x and y dimensions of the desired image. gdImageCreate
          returns a gdImagePtr to the new image, or NULL if unable to
          allocate the image. The image must eventually be destroyed
          using gdImageDestroy().
          

... inside a function ...
gdImagePtr im;
im = gdImageCreate(64, 64);
/* ... Use the image ... */
gdImageDestroy(im);

   gdImageCreateFromPng(FILE *in) _(FUNCTION)_
          gdImageCreateFromPngCtx(gdIOCtx *in) _(FUNCTION)_
          
          
          gdImageCreateFromPng is called to load images from PNG format
          files. Invoke gdImageCreateFromPng with an already opened
          pointer to a file containing the desired image.
          gdImageCreateFromPng returns a gdImagePtr to the new image, or
          NULL if unable to load the image (most often because the file
          is corrupt or does not contain a PNG image).
          gdImageCreateFromPng does _not_ close the file. You can inspect
          the sx and sy members of the image to determine its size. The
          image must eventually be destroyed using gdImageDestroy().
          

gdImagePtr im;
... inside a function ...
FILE *in;
in = fopen("mypng.png", "rb");
im = gdImageCreateFromPng(in);
fclose(in);
/* ... Use the image ... */
gdImageDestroy(im);

   gdImageCreateFromPngSource(gdSourcePtr in) _(FUNCTION)_
          gdImageCreateFromPngSource is called to load a PNG from a data
          source other than a file. Usage is very similar to the
          gdImageCreateFromPng function, except that the programmer
          provides a custom data source.
          
          The programmer must write an input function which accepts a
          context pointer, a buffer, and a number of bytes to be read as
          arguments. This function must read the number of bytes
          requested, unless the end of the file has been reached, in
          which case the function should return zero, or an error has
          occurred, in which case the function should return -1. The
          programmer then creates a gdSource structure and sets the
          source pointer to the input function and the context pointer to
          any value which is useful to the programmer.
          
          The example below implements gdImageCreateFromPng by creating a
          custom data source and invoking gdImageCreateFromPngSource.
          

static int freadWrapper(void *context, char *buf, int len);

gdImagePtr gdImageCreateFromPng(FILE *in)
{
        gdSource s;
        s.source = freadWrapper;
        s.context = in;
        return gdImageCreateFromPngSource(&s);
}

static int freadWrapper(void *context, char *buf, int len)
{
        int got = fread(buf, 1, len, (FILE *) context);
        return got;
}

   gdImageCreateFromGd(FILE *in) _(FUNCTION)_
          gdImageCreateFromGdCtx(gdIOCtx *in) _(FUNCTION)_
          
          
          gdImageCreateFromGd is called to load images from gd format
          files. Invoke gdImageCreateFromGd with an already opened
          pointer to a file containing the desired image in the gd file
          format, which is specific to gd and intended for very fast
          loading. (It is _not_ intended for compression; for
          compression, use PNG.) gdImageCreateFromGd returns a gdImagePtr
          to the new image, or NULL if unable to load the image (most
          often because the file is corrupt or does not contain a gd
          format image). gdImageCreateFromGd does _not_ close the file.
          You can inspect the sx and sy members of the image to determine
          its size. The image must eventually be destroyed using
          gdImageDestroy().
          

... inside a function ...
gdImagePtr im;
FILE *in;
in = fopen("mygd.gd", "rb");
im = gdImageCreateFromGd(in);
fclose(in);
/* ... Use the image ... */
gdImageDestroy(im);

   gdImageCreateFromGd2(FILE *in) _(FUNCTION)_
          gdImageCreateFromGd2Ctx(gdIOCtx *in) _(FUNCTION)_
          
          
          gdImageCreateFromGd2 is called to load images from gd2 format
          files. Invoke gdImageCreateFromGd2 with an already opened
          pointer to a file containing the desired image in the gd2 file
          format, which is specific to gd2 and intended for fast loading
          of parts of large images. (It is a compressed format, but
          generally not as good a LZW compression). gdImageCreateFromGd
          returns a gdImagePtr to the new image, or NULL if unable to
          load the image (most often because the file is corrupt or does
          not contain a gd format image). gdImageCreateFromGd2 does _not_
          close the file. You can inspect the sx and sy members of the
          image to determine its size. The image must eventually be
          destroyed using gdImageDestroy().
          

... inside a function ...
gdImagePtr im;
FILE *in;
in = fopen("mygd.gd2", "rb");
im = gdImageCreateFromGd2(in);
fclose(in);
/* ... Use the image ... */
gdImageDestroy(im);

   gdImageCreateFromGd2Part(FILE *in, int srcX, int srcY, int w, int h)
          _(FUNCTION)_
          gdImageCreateFromGd2PartCtx(gdIOCtx *in) _(FUNCTION)_
          
          
          gdImageCreateFromGd2Part is called to load parts of images from
          gd2 format files. Invoked in the same way as
          gdImageCreateFromGd2, but with extra parameters indicating the
          source (x, y) and width/height of the desired image.
          gdImageCreateFromGd2Part returns a gdImagePtr to the new image,
          or NULL if unable to load the image. The image must eventually
          be destroyed using gdImageDestroy().
          
   gdImageCreateFromXbm(FILE *in) _(FUNCTION)_
          gdImageCreateFromXbm is called to load images from X bitmap
          format files. Invoke gdImageCreateFromXbm with an already
          opened pointer to a file containing the desired image.
          gdImageCreateFromXbm returns a gdImagePtr to the new image, or
          NULL if unable to load the image (most often because the file
          is corrupt or does not contain an X bitmap format image).
          gdImageCreateFromXbm does _not_ close the file. You can inspect
          the sx and sy members of the image to determine its size. The
          image must eventually be destroyed using gdImageDestroy().
          

... inside a function ...
gdImagePtr im;
FILE *in;
in = fopen("myxbm.xbm", "rb");
im = gdImageCreateFromXbm(in);
fclose(in);
/* ... Use the image ... */
gdImageDestroy(im);

   gdImageCreateFromXpm(FILE *in) _(FUNCTION)_
          gdImageCreateFromXbm is called to load images from XPM X Window
          System color bitmap format files. This function is available
          only if HAVE_XPM is selected in the Makefile and the Xpm
          library is linked with the application. Invoke
          gdImageCreateFromXpm with an already opened pointer to a file
          containing the desired image. gdImageCreateFromXpm returns a
          gdImagePtr to the new image, or NULL if unable to load the
          image (most often because the file is corrupt or does not
          contain an XPM bitmap format image). gdImageCreateFromXpm does
          _not_ close the file. You can inspect the sx and sy members of
          the image to determine its size. The image must eventually be
          destroyed using gdImageDestroy().
          

... inside a function ...
gdImagePtr im;
FILE *in;
in = fopen("myxpm.xpm", "rb");
im = gdImageCreateFromXpm(in);
fclose(in);
/* ... Use the image ... */
gdImageDestroy(im);

   gdImageDestroy(gdImagePtr im) _(FUNCTION)_
          gdImageDestroy is used to free the memory associated with an
          image. It is important to invoke gdImageDestroy before exiting
          your program or assigning a new image to a gdImagePtr variable.
          

... inside a function ...
gdImagePtr im;
im = gdImageCreate(10, 10);
/* ... Use the image ... */
/* Now destroy it */
gdImageDestroy(im);

   void gdImagePng(gdImagePtr im, FILE *out) _(FUNCTION)_
          gdImagePng outputs the specified image to the specified file in
          PNG format. The file must be open for writing. Under MSDOS and
          all versions of Windows, it is important to use "wb" as opposed
          to simply "w" as the mode when opening the file, and under Unix
          there is no penalty for doing so. gdImagePng does _not_ close
          the file; your code must do so.
          

... inside a function ...
gdImagePtr im;
int black, white;
FILE *out;
/* Create the image */
im = gdImageCreate(100, 100);
/* Allocate background */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Allocate drawing color */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Draw rectangle */
gdImageRectangle(im, 0, 0, 99, 99, black);
/* Open output file in binary mode */
out = fopen("rect.png", "wb");
/* Write PNG */
gdImagePng(im, out);
/* Close file */
fclose(out);
/* Destroy image */
gdImageDestroy(im);

   void* gdImagePngPtr(gdImagePtr im, int *size) _(FUNCTION)_
          Identical to gdImagePng except that it returns a pointer to a
          memory area with the PNG data. This memory must be freed by the
          caller when it is no longer needed. The 'size' parameter
          received the total size of the block of memory.
          
   gdImagePngToSink(gdImagePtr im, gdSinkPtr out) _(FUNCTION)_
          gdImagePngToSink is called to write a PNG to a data "sink"
          (destination) other than a file. Usage is very similar to the
          gdImagePng function, except that the programmer provides a
          custom data sink.
          
          The programmer must write an output function which accepts a
          context pointer, a buffer, and a number of bytes to be written
          as arguments. This function must write the number of bytes
          requested and return that number, unless an error has occurred,
          in which case the function should return -1. The programmer
          then creates a gdSink structure and sets the sink pointer to
          the output function and the context pointer to any value which
          is useful to the programmer.
          
          The example below implements gdImagePng by creating a custom
          data source and invoking gdImagePngFromSink.
          

static int stdioSink(void *context, char *buffer, int len)
{
        return fwrite(buffer, 1, len, (FILE *) context);
}

void gdImagePng(gdImagePtr im, FILE *out)
{
        gdSink mySink;
        mySink.context = (void *) out;
        mySink.sink = stdioSink;
        gdImagePngToSink(im, &mySink);
}

   void gdImageGd(gdImagePtr im, FILE *out) _(FUNCTION)_
          gdImageGd outputs the specified image to the specified file in
          the gd image format. The file must be open for writing. Under
          MSDOS and all versions of Windows, it is important to use "wb"
          as opposed to simply "w" as the mode when opening the file, and
          under Unix there is no penalty for doing so. gdImagePng does
          _not_ close the file; your code must do so.
          
          The gd image format is intended for fast reads and writes of
          images your program will need frequently to build other images.
          It is _not_ a compressed format, and is not intended for
          general use.
          

... inside a function ...
gdImagePtr im;
int black, white;
FILE *out;
/* Create the image */
im = gdImageCreate(100, 100);
/* Allocate background */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Allocate drawing color */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Draw rectangle */
gdImageRectangle(im, 0, 0, 99, 99, black);
/* Open output file in binary mode */
out = fopen("rect.gd", "wb");
/* Write gd format file */
gdImageGd(im, out);
/* Close file */
fclose(out);
/* Destroy image */
gdImageDestroy(im);

   void* gdImageGdPtr(gdImagePtr im, int *size) _(FUNCTION)_
          Identical to gdImageGd except that it returns a pointer to a
          memory area with the GD data. This memory must be freed by the
          caller when it is no longer needed. The 'size' parameter
          received the total size of the block of memory.
          
   void gdImageGd2(gdImagePtr im, FILE *out, int chunkSize, int fmt)
          _(FUNCTION)_
          gdImageGd2 outputs the specified image to the specified file in
          the gd2 image format. The file must be open for writing. Under
          MSDOS and all versions of Windows, it is important to use "wb"
          as opposed to simply "w" as the mode when opening the file, and
          under Unix there is no penalty for doing so. gdImageGd2 does
          _not_ close the file; your code must do so.
          
          The gd2 image format is intended for fast reads and writes of
          parts of images. It is a compressed format, and well suited to
          retrieving smll sections of much larger images. The third and
          fourth parameters are the 'chunk size' and format
          resposectively.
          
          The file is stored as a series of compressed subimages, and the
          _Chunk Size_ determines the sub-image size - a value of zero
          causes the GD library to use the default.
          
          It is also possible to store GD2 files in an uncompressed
          format, in which case the fourth parameter should be
          GD2_FMT_RAW.
          

... inside a function ...
gdImagePtr im;
int black, white;
FILE *out;
/* Create the image */
im = gdImageCreate(100, 100);
/* Allocate background */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Allocate drawing color */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Draw rectangle */
gdImageRectangle(im, 0, 0, 99, 99, black);
/* Open output file in binary mode */
out = fopen("rect.gd", "wb");
/* Write gd2 format file */
gdImageGd2(im, out, 0, GD2_FMT_COMPRESSED);
/* Close file */
fclose(out);
/* Destroy image */
gdImageDestroy(im);

   void* gdImageGd2Ptr(gdImagePtr im, int chunkSize, int fmt, int *size)
          _(FUNCTION)_
          Identical to gdImageGd2 except that it returns a pointer to a
          memory area with the GD2 data. This memory must be freed by the
          caller when it is no longer needed. The 'size' parameter
          received the total size of the block of memory.
          
  Drawing Functions
  
   void gdImageSetPixel(gdImagePtr im, int x, int y, int color)
          _(FUNCTION)_
          gdImageSetPixel sets a pixel to a particular color index.
          Always use this function or one of the other drawing functions
          to access pixels; do not access the pixels of the gdImage
          structure directly.
          

... inside a function ...
gdImagePtr im;
int black;
int white;
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Set a pixel near the center. */
gdImageSetPixel(im, 50, 50, white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImageLine(gdImagePtr im, int x1, int y1, int x2, int y2, int
          color) _(FUNCTION)_
          gdImageLine is used to draw a line between two endpoints (x1,y1
          and x2, y2). The line is drawn using the color index specified.
          Note that the color index can be an actual color returned by
          gdImageColorAllocate or one of gdStyled, gdBrushed or
          gdStyledBrushed.
          

... inside a function ...
gdImagePtr im;
int black;
int white;
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Draw a line from the upper left corner to the lower right corner. */
gdImageLine(im, 0, 0, 99, 99, white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImageDashedLine(gdImagePtr im, int x1, int y1, int x2, int y2,
          int color) _(FUNCTION)_
          gdImageDashedLine is provided _solely for backwards
          compatibility _with gd 1.0. New programs should draw dashed
          lines using the normal gdImageLine function and the new
          gdImageSetStyle function.
          
          gdImageDashedLine is used to draw a dashed line between two
          endpoints (x1,y1 and x2, y2). The line is drawn using the color
          index specified. The portions of the line that are not drawn
          are left transparent so the background is visible.
          

... inside a function ...
gdImagePtr im;
int black;
int white;
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Draw a dashed line from the upper left corner to the lower right corner. */
gdImageDashedLine(im, 0, 0, 99, 99);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImagePolygon(gdImagePtr im, gdPointPtr points, int pointsTotal,
          int color) _(FUNCTION)_
          gdImagePolygon is used to draw a polygon with the verticies (at
          least 3) specified, using the color index specified. See also
          gdImageFilledPolygon.
          

... inside a function ...
gdImagePtr im;
int black;
int white;
/* Points of polygon */
gdPoint points[3];
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Draw a triangle. */
points[0].x = 50;
points[0].y = 0;
points[1].x = 99;
points[1].y = 99;
points[2].x = 0;
points[2].y = 99;
gdImagePolygon(im, points, 3, white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImageRectangle(gdImagePtr im, int x1, int y1, int x2, int y2,
          int color) _(FUNCTION)_
          gdImageRectangle is used to draw a rectangle with the two
          corners (upper left first, then lower right) specified, using
          the color index specified.
          

... inside a function ...
gdImagePtr im;
int black;
int white;
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Draw a rectangle occupying the central area. */
gdImageRectangle(im, 25, 25, 74, 74, white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImageFilledPolygon(gdImagePtr im, gdPointPtr points, int
          pointsTotal, int color) _(FUNCTION)_
          gdImageFilledPolygon is used to fill a polygon with the
          verticies (at least 3) specified, using the color index
          specified. See also gdImagePolygon.
          

... inside a function ...
gdImagePtr im;
int black;
int white;
int red;
/* Points of polygon */
gdPoint points[3];
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Allocate the color red. */
red = gdImageColorAllocate(im, 255, 0, 0);
/* Draw a triangle. */
points[0].x = 50;
points[0].y = 0;
points[1].x = 99;
points[1].y = 99;
points[2].x = 0;
points[2].y = 99;
/* Paint it in white */
gdImageFilledPolygon(im, points, 3, white);
/* Outline it in red; must be done second */
gdImagePolygon(im, points, 3, red);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImageFilledRectangle(gdImagePtr im, int x1, int y1, int x2, int
          y2, int color) _(FUNCTION)_
          gdImageFilledRectangle is used to draw a solid rectangle with
          the two corners (upper left first, then lower right) specified,
          using the color index specified.
          

... inside a function ...
gdImagePtr im;
int black;
int white;
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = int gdImageColorAllocate(im, 255, 255, 255);
/* Draw a filled rectangle occupying the central area. */
gdImageFilledRectangle(im, 25, 25, 74, 74, white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImageArc(gdImagePtr im, int cx, int cy, int w, int h, int s,
          int e, int color) _(FUNCTION)_
          gdImageArc is used to draw a partial ellipse centered at the
          given point, with the specified width and height in pixels. The
          arc begins at the position in degrees specified by s and ends
          at the position specified by e. The arc is drawn in the color
          specified by the last argument. A circle can be drawn by
          beginning from 0 degrees and ending at 360 degrees, with width
          and height being equal. e must be greater than s. Values
          greater than 360 are interpreted modulo 360.
          

... inside a function ...
gdImagePtr im;
int black;
int white;
im = gdImageCreate(100, 50);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Inscribe an ellipse in the image. */
gdImageArc(im, 50, 25, 98, 48, 0, 360, white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImageFillToBorder(gdImagePtr im, int x, int y, int border, int
          color) _(FUNCTION)_
          gdImageFillToBorder floods a portion of the image with the
          specified color, beginning at the specified point and stopping
          at the specified border color. For a way of flooding an area
          defined by the color of the starting point, see gdImageFill.
          
          The border color _cannot_ be a special color such as gdTiled;
          it must be a proper solid color. The fill color can be,
          however.
          
          Note that gdImageFillToBorder is recursive. It is not the most
          naive implementation possible, and the implementation is
          expected to improve, but there will always be degenerate cases
          in which the stack can become very deep. This can be a problem
          in MSDOS and MS Windows 3.1 environments. (Of course, in a Unix
          or Windows 95/98/NT environment with a proper stack, this is
          not a problem at all.)
          

... inside a function ...
gdImagePtr im;
int black;
int white;
int red;
im = gdImageCreate(100, 50);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Allocate the color red. */
red = gdImageColorAllocate(im, 255, 0, 0);
/* Inscribe an ellipse in the image. */
gdImageArc(im, 50, 25, 98, 48, 0, 360, white);
/* Flood-fill the ellipse. Fill color is red, border color is
        white (ellipse). */
gdImageFillToBorder(im, 50, 50, white, red);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImageFill(gdImagePtr im, int x, int y, int color) _(FUNCTION)_
          gdImageFill floods a portion of the image with the specified
          color, beginning at the specified point and flooding the
          surrounding region of the same color as the starting point. For
          a way of flooding a region defined by a specific border color
          rather than by its interior color, see gdImageFillToBorder.
          
          The fill color can be gdTiled, resulting in a tile fill using
          another image as the tile. However, the tile image cannot be
          transparent. If the image you wish to fill with has a
          transparent color index, call gdImageTransparent on the tile
          image and set the transparent color index to -1 to turn off its
          transparency.
          
          Note that gdImageFill is recursive. It is not the most naive
          implementation possible, and the implementation is expected to
          improve, but there will always be degenerate cases in which the
          stack can become very deep. This can be a problem in MSDOS and
          MS Windows environments. (Of course, in a Unix or Windows
          95/98/NT environment with a proper stack, this is not a problem
          at all.)
          

... inside a function ...
gdImagePtr im;
int black;
int white;
int red;
im = gdImageCreate(100, 50);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Allocate the color red. */
red = gdImageColorAllocate(im, 255, 0, 0);
/* Inscribe an ellipse in the image. */
gdImageArc(im, 50, 25, 98, 48, 0, 360, white);
/* Flood-fill the ellipse. Fill color is red, and will replace the
        black interior of the ellipse. */
gdImageFill(im, 50, 50, red);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImageSetBrush(gdImagePtr im, gdImagePtr brush) _(FUNCTION)_
          A "brush" is an image used to draw wide, shaped strokes in
          another image. Just as a paintbrush is not a single point, a
          brush image need not be a single pixel. _Any_ gd image can be
          used as a brush, and by setting the transparent color index of
          the brush image with gdImageColorTransparent, a brush of any
          shape can be created. All line-drawing functions, such as
          gdImageLine and gdImagePolygon, will use the current brush if
          the special "color" gdBrushed or gdStyledBrushed is used when
          calling them.
          
          gdImageSetBrush is used to specify the brush to be used in a
          particular image. You can set any image to be the brush. If the
          brush image does not have the same color map as the first
          image, any colors missing from the first image will be
          allocated. If not enough colors can be allocated, the closest
          colors already available will be used. This allows arbitrary
          PNGs to be used as brush images. It also means, however, that
          you should not set a brush unless you will actually use it; if
          you set a rapid succession of different brush images, you can
          quickly fill your color map, and the results will not be
          optimal.
          
          You need not take any special action when you are finished with
          a brush. As for any other image, if you will not be using the
          brush image for any further purpose, you should call
          gdImageDestroy. You must not use the color gdBrushed if the
          current brush has been destroyed; you can of course set a new
          brush to replace it.
          

... inside a function ...
gdImagePtr im, brush;
FILE *in;
int black;
im = gdImageCreate(100, 100);
/* Open the brush PNG. For best results, portions of the
        brush that should be transparent (ie, not part of the
        brush shape) should have the transparent color index. */
in = fopen("star.png", "rb");
brush = gdImageCreateFromPng(in);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
gdImageSetBrush(im, brush);
/* Draw a line from the upper left corner to the lower right corner
        using the brush. */
gdImageLine(im, 0, 0, 99, 99, gdBrushed);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);
/* Destroy the brush image */
gdImageDestroy(brush);

   void gdImageSetTile(gdImagePtr im, gdImagePtr tile) _(FUNCTION)_
          A "tile" is an image used to fill an area with a repeated
          pattern. _Any_ gd image can be used as a tile, and by setting
          the transparent color index of the tile image with
          gdImageColorTransparent, a tile that allows certain parts of
          the underlying area to shine through can be created. All
          region-filling functions, such as gdImageFill and
          gdImageFilledPolygon, will use the current tile if the special
          "color" gdTiled is used when calling them.
          
          gdImageSetTile is used to specify the tile to be used in a
          particular image. You can set any image to be the tile. If the
          tile image does not have the same color map as the first image,
          any colors missing from the first image will be allocated. If
          not enough colors can be allocated, the closest colors already
          available will be used. This allows arbitrary PNGs to be used
          as tile images. It also means, however, that you should not set
          a tile unless you will actually use it; if you set a rapid
          succession of different tile images, you can quickly fill your
          color map, and the results will not be optimal.
          
          You need not take any special action when you are finished with
          a tile. As for any other image, if you will not be using the
          tile image for any further purpose, you should call
          gdImageDestroy. You must not use the color gdTiled if the
          current tile has been destroyed; you can of course set a new
          tile to replace it.
          

... inside a function ...
gdImagePtr im, tile;
FILE *in;
int black;
im = gdImageCreate(100, 100);
/* Open the tile PNG. For best results, portions of the
        tile that should be transparent (ie, allowing the
        background to shine through) should have the transparent
        color index. */
in = fopen("star.png", "rb");
tile = gdImageCreateFromPng(in);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
gdImageSetTile(im, tile);
/* Fill an area using the tile. */
gdImageFilledRectangle(im, 25, 25, 75, 75, gdTiled);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);
/* Destroy the tile image */
gdImageDestroy(tile);

   void gdImageSetStyle(gdImagePtr im, int *style, int styleLength)
          _(FUNCTION)_
          It is often desirable to draw dashed lines, dotted lines, and
          other variations on a broken line. gdImageSetStyle can be used
          to set any desired series of colors, including a special color
          that leaves the background intact, to be repeated during the
          drawing of a line.
          
          To use gdImageSetStyle, create an array of integers and assign
          them the desired series of color values to be repeated. You can
          assign the special color value gdTransparent to indicate that
          the existing color should be left unchanged for that particular
          pixel (allowing a dashed line to be attractively drawn over an
          existing image).
          
          Then, to draw a line using the style, use the normal
          gdImageLine function with the special color value gdStyled.
          
          As of version 1.1.1, the style array is copied when you set the
          style, so you need not be concerned with keeping the array
          around indefinitely. This should not break existing code that
          assumes styles are not copied.
          
          You can also combine styles and brushes to draw the brush image
          at intervals instead of in a continuous stroke. When creating a
          style for use with a brush, the style values are interpreted
          differently: zero (0) indicates pixels at which the brush
          should not be drawn, while one (1) indicates pixels at which
          the brush should be drawn. To draw a styled, brushed line, you
          must use the special color value gdStyledBrushed. For an
          example of this feature in use, see gddemo.c (provided in the
          distribution).
          

gdImagePtr im;
int styleDotted[2], styleDashed[6];
FILE *in;
int black;
int red;
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
red = gdImageColorAllocate(im, 255, 0, 0);
/* Set up dotted style. Leave every other pixel alone. */
styleDotted[0] = red;
styleDotted[1] = gdTransparent;
/* Set up dashed style. Three on, three off. */
styleDashed[0] = red;
styleDashed[1] = red;
styleDashed[2] = red;
styleDashed[3] = gdTransparent;
styleDashed[4] = gdTransparent;
styleDashed[5] = gdTransparent;
/* Set dotted style. Note that we have to specify how many pixels are
        in the style! */
gdImageSetStyle(im, styleDotted, 2);
/* Draw a line from the upper left corner to the lower right corner. */
gdImageLine(im, 0, 0, 99, 99, gdStyled);
/* Now the dashed line. */
gdImageSetStyle(im, styleDashed, 6);
gdImageLine(im, 0, 99, 0, 99, gdStyled);

/* ... Do something with the image, such as saving it to a file ... */

/* Destroy it */
gdImageDestroy(im);

  Query Functions
  
        int gdImageBlue(gdImagePtr im, int color) _(MACRO)_
                gdImageBlue is a macro which returns the blue component
                of the specified color index. Use this macro rather than
                accessing the structure members directly.
                
        int gdImageGetPixel(gdImagePtr im, int x, int y) _(FUNCTION)_
                gdImageGetPixel() retrieves the color index of a
                particular pixel. Always use this function to query
                pixels; do not access the pixels of the gdImage structure
                directly.
                

... inside a function ...
FILE *in;
gdImagePtr im;
int c;
in = fopen("mypng.png", "rb");
im = gdImageCreateFromPng(in);
fclose(in);
c = gdImageGetPixel(im, gdImageSX(im) / 2, gdImageSY(im) / 2);
printf("The value of the center pixel is %d; RGB values are %d,%d,%d\n",
        c, im->red[c], im->green[c], im->blue[c]);
gdImageDestroy(im);

        int gdImageBoundsSafe(gdImagePtr im, int x, int y) _(FUNCTION)_
                gdImageBoundsSafe returns true (1) if the specified point
                is within the bounds of the image, false (0) if not. This
                function is intended primarily for use by those who wish
                to add functions to gd. All of the gd drawing functions
                already clip safely to the edges of the image.
                

... inside a function ...
gdImagePtr im;
int black;
int white;
im = gdImageCreate(100, 100);
if (gdImageBoundsSafe(im, 50, 50)) {
        printf("50, 50 is within the image bounds\n");
} else {
        printf("50, 50 is outside the image bounds\n");
}
gdImageDestroy(im);

        int gdImageGreen(gdImagePtr im, int color) _(MACRO)_
                gdImageGreen is a macro which returns the green component
                of the specified color index. Use this macro rather than
                accessing the structure members directly.
                
        int gdImageRed(gdImagePtr im, int color) _(MACRO)_
                gdImageRed is a macro which returns the red component of
                the specified color index. Use this macro rather than
                accessing the structure members directly.
                
        int gdImageSX(gdImagePtr im) _(MACRO)_
                gdImageSX is a macro which returns the width of the image
                in pixels. Use this macro rather than accessing the
                structure members directly.
                
        int gdImageSY(gdImagePtr im) _(MACRO)_
                gdImageSY is a macro which returns the height of the
                image in pixels. Use this macro rather than accessing the
                structure members directly.
                
  Fonts and text-handling functions
  
        void gdImageChar(gdImagePtr im, gdFontPtr font, int x, int y, int
                c, int color) _(FUNCTION)_
                gdImageChar is used to draw single characters on the
                image. (To draw multiple characters, use gdImageString or
                gdImageString16. See also gdImageStringTTF, new with
                gd-1.6.2.) The second argument is a pointer to a font
                definition structure; five fonts are provided with gd,
                gdFontTiny, gdFontSmall, gdFontMediumBold, gdFontLarge,
                and gdFontGiant. You must include the files "gdfontt.h",
                "gdfonts.h", "gdfontmb.h", "gdfontl.h" and "gdfontg.h"
                respectively and (if you are not using a library-based
                approach) link with the corresponding .c files to use the
                provided fonts. The character specified by the fifth
                argument is drawn from left to right in the specified
                color. (See gdImageCharUp for a way of drawing vertical
                text.) Pixels not set by a particular character retain
                their previous color.
                

#include "gd.h"
#include "gdfontl.h"
... inside a function ...
gdImagePtr im;
int black;
int white;
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Draw a character. */
gdImageChar(im, gdFontLarge, 0, 0, 'Q', white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

        void gdImageCharUp(gdImagePtr im, gdFontPtr font, int x, int y,
                int c, int color) _(FUNCTION)_
                gdImageCharUp is used to draw single characters on the
                image, rotated 90 degrees. (To draw multiple characters,
                use gdImageStringUp or gdImageStringUp16.) The second
                argument is a pointer to a font definition structure;
                five fonts are provided with gd, gdFontTiny, gdFontSmall,
                gdFontMediumBold, gdFontLarge, and gdFontGiant. You must
                include the files "gdfontt.h", "gdfonts.h", "gdfontmb.h",
                "gdfontl.h" and "gdfontg.h" respectively and (if you are
                not using a library-based approach) link with the
                corresponding .c files to use the provided fonts. The
                character specified by the fifth argument is drawn from
                bottom to top, rotated at a 90-degree angle, in the
                specified color. (See gdImageChar for a way of drawing
                horizontal text.) Pixels not set by a particular
                character retain their previous color.
                

#include "gd.h"
#include "gdfontl.h"
... inside a function ...
gdImagePtr im;
int black;
int white;
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Draw a character upwards so it rests against the top of the image. */
gdImageCharUp(im, gdFontLarge,
        0, gdFontLarge->h, 'Q', white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

        void gdImageString(gdImagePtr im, gdFontPtr font, int x, int y,
                unsigned char *s, int color) _(FUNCTION)_
                gdImageString is used to draw multiple characters on the
                image. (To draw single characters, use gdImageChar.) The
                second argument is a pointer to a font definition
                structure; five fonts are provided with gd, gdFontTiny,
                gdFontSmall, gdFontMediumBold, gdFontLarge, and
                gdFontGiant. You must include the files "gdfontt.h",
                "gdfonts.h", "gdfontmb.h", "gdfontl.h" and "gdfontg.h"
                respectively and (if you are not using a library-based
                approach) link with the corresponding .c files to use the
                provided fonts. The null-terminated C string specified by
                the fifth argument is drawn from left to right in the
                specified color. (See gdImageStringUp for a way of
                drawing vertical text. See also gdImageStringTTF, new
                with gd-1.6.2.) Pixels not set by a particular character
                retain their previous color.
                

#include "gd.h"
#include "gdfontl.h"
#include <string.h>
... inside a function ...
gdImagePtr im;
int black;
int white;
/* String to draw. */
char *s = "Hello.";
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Draw a centered string. */
gdImageString(im, gdFontLarge,
        im->w / 2 - (strlen(s) * gdFontLarge->w / 2),
        im->h / 2 - gdFontLarge->h / 2,
        s, white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

        void gdImageString16(gdImagePtr im, gdFontPtr font, int x, int y,
                unsigned short *s, int color) _(FUNCTION)_
                gdImageString is used to draw multiple 16-bit characters
                on the image. (To draw single characters, use
                gdImageChar.) The second argument is a pointer to a font
                definition structure; five fonts are provided with gd,
                gdFontTiny, gdFontSmall, gdFontMediumBold, gdFontLarge,
                and gdFontGiant. You must include the files "gdfontt.h",
                "gdfonts.h", "gdfontmb.h", "gdfontl.h" and "gdfontg.h"
                respectively and (if you are not using a library-based
                approach) link with the corresponding .c files to use the
                provided fonts. The null-terminated string of characters
                represented as 16-bit unsigned short integers specified
                by the fifth argument is drawn from left to right in the
                specified color. (See gdImageStringUp16 for a way of
                drawing vertical text.) Pixels not set by a particular
                character retain their previous color.
                
                This function was added in gd1.3 to provide a means of
                rendering fonts with more than 256 characters for those
                who have them. A more frequently used routine is
                gdImageString.
                
        void gdImageStringUp(gdImagePtr im, gdFontPtr font, int x, int y,
                unsigned char *s, int color) _(FUNCTION)_
                gdImageStringUp is used to draw multiple characters on
                the image, rotated 90 degrees. (To draw single
                characters, use gdImageCharUp.) The second argument is a
                pointer to a font definition structure; five fonts are
                provided with gd, gdFontTiny, gdFontSmall,
                gdFontMediumBold, gdFontLarge, and gdFontGiant. You must
                include the files "gdfontt.h", "gdfonts.h", "gdfontmb.h",
                "gdfontl.h" and "gdfontg.h" respectively and (if you are
                not using a library-based approach) link with the
                corresponding .c files to use the provided fonts.The
                null-terminated C string specified by the fifth argument
                is drawn from bottom to top (rotated 90 degrees) in the
                specified color. (See gdImageString for a way of drawing
                horizontal text.) Pixels not set by a particular
                character retain their previous color.
                

#include "gd.h"
#include "gdfontl.h"
#include <string.h>
... inside a function ...
gdImagePtr im;
int black;
int white;
/* String to draw. */
char *s = "Hello.";
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Draw a centered string going upwards. Axes are reversed,
        and Y axis is decreasing as the string is drawn. */
gdImageStringUp(im, gdFontLarge,
        im->w / 2 - gdFontLarge->h / 2,
        im->h / 2 + (strlen(s) * gdFontLarge->w / 2),
        s, white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

        void gdImageStringUp16(gdImagePtr im, gdFontPtr font, int x, int
                y, unsigned short *s, int color) _(FUNCTION)_
                gdImageString is used to draw multiple 16-bit characters
                vertically on the image. (To draw single characters, use
                gdImageChar.) The second argument is a pointer to a font
                definition structure; five fonts are provided with gd,
                gdFontTiny, gdFontSmall, gdFontMediumBold, gdFontLarge,
                and gdFontGiant. You must include the files "gdfontt.h",
                "gdfonts.h", "gdfontmb.h", "gdfontl.h" and "gdfontg.h"
                respectively and (if you are not using a library-based
                approach) link with the corresponding .c files to use the
                provided fonts. The null-terminated string of characters
                represented as 16-bit unsigned short integers specified
                by the fifth argument is drawn from bottom to top in the
                specified color. (See gdImageStringUp16 for a way of
                drawing horizontal text.) Pixels not set by a particular
                character retain their previous color.
                
                This function was added in gd1.3 to provide a means of
                rendering fonts with more than 256 characters for those
                who have them. A more frequently used routine is
                gdImageStringUp.
                
        char *gdImageStringTTF(gdImagePtr im, int *brect, int fg, char
                *fontname, double ptsize, double angle, int x, int y,
                char *string) _(FUNCTION)_
                gdImageStringTTF is draws a string of anti-aliased
                characters on the image using the FreeType library to
                print from user-supplied TrueType fonts. _We do not
                provide TrueType fonts. Obtaining them is entirely up to
                you._ The string is anti-aliased, meaning that there
                should be less "jaggies." The fontname is the full
                pathname to a TrueType font file. The string may be
                arbitrarily scaled (ptsize) and rotated (angle in
                radians).
                
                The user-supplied int brect[8] array is filled on return
                from gdImageStringTTF with the 8 elements representing
                the 4 corner coordinates of the bounding rectangle.
                0 lower left corner, X position
                lower left corner, Y position
                lower right corner, X position
                3 lower right corner, Y position
                4 upper right corner, X position
                5 upper right corner, Y position
                6 upper left corner, X position
                7 upper left corner, Y position
                
                The points are relative to the text regardless of the
                angle, so "upper left" means in the top left-hand corner
                seeing the text horizontally.
                
                Use a NULL gdImagePtr to get the bounding rectangle
                without rendering. This is a relatively cheap operation
                if followed by a rendering of the same string, because of
                the caching of the partial rendering during bounding
                rectangle calculation.
                
                The string is rendered in the color indicated by the gf
                color index. Use the negative of the desired color index
                to disable anti-aliasing.
                
                The string may contain UTF-8 sequences like: "&#192;"
                
                gdImageStringTTF will return a null char* on success, or
                an error string on failure.
                

#include "gd.h"
#include <string.h>
... inside a function ...
gdImagePtr im;
int black;
int white;
int brect[8];
int x, y;
char *err;

char *s = "Hello."; /* String to draw. */
double sz = 40.;
char *f = "/usr/local/share/ttf/Times.ttf";  /* User supplied font */

/* obtain brect so that we can size the image */
err = gdImageStringTTF(NULL,&brect[0],0,f,sz,0.,0,0,s);
if (err) {fprintf(stderr,err); return 1;}

/* create an image big enough for the string plus a little whitespace */
x = brect[2]-brect[6] + 6;
y = brect[3]-brect[7] + 6;
im = gdImageCreate(x,y);

/* Background color (first allocated) */
white = gdImageColorResolve(im, 255, 255, 255);
black = gdImageColorResolve(im, 0, 0, 0);

/* render the string, offset origin to center string*/
/* note that we use top-left coordinate for adjustment
 * since gd origin is in top-left with y increasing downwards. */
x = 3 - brect[6];
y = 3 - brect[7];
err = gdImageStringTTF(im,&brect[0],black,f,sz,0.0,x,y,s);
if (err) {fprintf(stderr,err); return 1;}

/* Write img to stdout */
gdImagePng(im, stdout);

/* Destroy it */
gdImageDestroy(im);

  Color-handling functions
  
        int gdImageColorAllocate(gdImagePtr im, int r, int g, int b)
                _(FUNCTION)_
                gdImageColorAllocate finds the first available color
                index in the image specified, sets its RGB values to
                those requested (255 is the maximum for each), and
                returns the index of the new color table entry. When
                creating a new image, the first time you invoke this
                function, you are setting the background color for that
                image.
                
                In the event that all gdMaxColors colors (256) have
                already been allocated, gdImageColorAllocate will return
                -1 to indicate failure. (This is not uncommon when
                working with existing PNG files that already use 256
                colors.) Note that gdImageColorAllocate does not check
                for existing colors that match your request; see
                gdImageColorExact and gdImageColorClosest for ways to
                locate existing colors that approximate the color desired
                in situations where a new color is not available. Also
                see gdImageColorResolve, new in gd-1.6.2.
                

... inside a function ...
gdImagePtr im;
int black;
int red;
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color red. */
red = gdImageColorAllocate(im, 255, 0, 0);
/* Draw a dashed line from the upper left corner to the lower right corner. */
gdImageDashedLine(im, 0, 0, 99, 99, red);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

        int gdImageColorClosest(gdImagePtr im, int r, int g, int b)
                _(FUNCTION)_
                gdImageColorClosest searches the colors which have been
                defined thus far in the image specified and returns the
                index of the color with RGB values closest to those of
                the request. (Closeness is determined by Euclidian
                distance, which is used to determine the distance in
                three-dimensional color space between colors.)
                
                If no colors have yet been allocated in the image,
                gdImageColorClosest returns -1.
                
                This function is most useful as a backup method for
                choosing a drawing color when an image already contains
                gdMaxColors (256) colors and no more can be allocated.
                (This is not uncommon when working with existing PNG
                files that already use many colors.) See
                gdImageColorExact for a method of locating exact matches
                only.
                

... inside a function ...
gdImagePtr im;
FILE *in;
int red;
/* Let's suppose that photo.png is a scanned photograph with
        many colors. */
in = fopen("photo.png", "rb");
im = gdImageCreateFromPng(in);
fclose(in);
/* Try to allocate red directly */
red = gdImageColorAllocate(im, 255, 0, 0);
/* If we fail to allocate red... */
if (red == (-1)) {
        /* Find the _closest_ color instead. */
        red = gdImageColorClosest(im, 255, 0, 0);
}
/* Draw a dashed line from the upper left corner to the lower right corner */
gdImageDashedLine(im, 0, 0, 99, 99, red);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

        int gdImageColorExact(gdImagePtr im, int r, int g, int b)
                _(FUNCTION)_
                gdImageColorExact searches the colors which have been
                defined thus far in the image specified and returns the
                index of the first color with RGB values which exactly
                match those of the request. If no allocated color matches
                the request precisely, gdImageColorExact returns -1. See
                gdImageColorClosest for a way to find the color closest
                to the color requested.
                

... inside a function ...
gdImagePtr im;
int red;
in = fopen("photo.png", "rb");
im = gdImageCreateFromPng(in);
fclose(in);
/* The image may already contain red; if it does, we'll save a slot
        in the color table by using that color. */
/* Try to allocate red directly */
red = gdImageColorExact(im, 255, 0, 0);
/* If red isn't already present... */
if (red == (-1)) {
        /* Second best: try to allocate it directly. */
        red = gdImageColorAllocate(im, 255, 0, 0);
        /* Out of colors, so find the _closest_ color instead. */
        red = gdImageColorClosest(im, 255, 0, 0);
}
/* Draw a dashed line from the upper left corner to the lower right corner */
gdImageDashedLine(im, 0, 0, 99, 99, red);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

        int gdImageColorResolve(gdImagePtr im, int r, int g, int b)
                _(FUNCTION)_
                gdImageColorResolve searches the colors which have been
                defined thus far in the image specified and returns the
                index of the first color with RGB values which exactly
                match those of the request. If no allocated color matches
                the request precisely, then gdImageColorResolve tries to
                allocate the exact color. If there is no space left in
                the color table then gdImageColorResolve returns the
                closest color (as in gdImageColorClosest). This function
                always returns an index of a color.
                

... inside a function ...
gdImagePtr im;
int red;
in = fopen("photo.png", "rb");
im = gdImageCreateFromPng(in);
fclose(in);
/* The image may already contain red; if it does, we'll save a slot
        in the color table by using that color. */
/* Get index of red, or color closest to red */
red = gdImageColorResolve(im, 255, 0, 0);
/* Draw a dashed line from the upper left corner to the lower right corner */
gdImageDashedLine(im, 0, 0, 99, 99, red);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

        int gdImageColorsTotal(gdImagePtr im) _(MACRO)_
                gdImageColorsTotal is a macro which returns the number of
                colors currently allocated in the image. Use this macro
                to obtain this information; do not access the structure
                directly.
                
        int gdImageColorRed(gdImagePtr im, int c) _(MACRO)_
                gdImageColorRed is a macro which returns the red portion
                of the specified color in the image. Use this macro to
                obtain this information; do not access the structure
                directly.
                
        int gdImageColorGreen(gdImagePtr im, int c) _(MACRO)_
                gdImageColorGreen is a macro which returns the green
                portion of the specified color in the image. Use this
                macro to obtain this information; do not access the
                structure directly.
                
        int gdImageColorBlue(gdImagePtr im, int c) _(MACRO)_
                gdImageColorBlue is a macro which returns the green
                portion of the specified color in the image. Use this
                macro to obtain this information; do not access the
                structure directly.
                
        int gdImageGetInterlaced(gdImagePtr im) _(MACRO)_
                gdImageGetInterlaced is a macro which returns true (1) if
                the image is interlaced, false (0) if not. Use this macro
                to obtain this information; do not access the structure
                directly. See gdImageInterlace for a means of interlacing
                images.
                
        int gdImageGetTransparent(gdImagePtr im) _(MACRO)_
                gdImageGetTransparent is a macro which returns the
                current transparent color index in the image. If there is
                no transparent color, gdImageGetTransparent returns -1.
                Use this macro to obtain this information; do not access
                the structure directly.
                
        void gdImageColorDeallocate(gdImagePtr im, int color) _(FUNCTION)_
                
                gdImageColorDeallocate marks the specified color as being
                available for reuse. It does not attempt to determine
                whether the color index is still in use in the image.
                After a call to this function, the next call to
                gdImageColorAllocate for the same image will set new RGB
                values for that color index, changing the color of any
                pixels which have that index as a result. If multiple
                calls to gdImageColorDeallocate are made consecutively,
                the lowest-numbered index among them will be reused by
                the next gdImageColorAllocate call.
                

... inside a function ...
gdImagePtr im;
int red, blue;
in = fopen("photo.png", "rb");
im = gdImageCreateFromPng(in);
fclose(in);
/* Look for red in the color table. */
red = gdImageColorExact(im, 255, 0, 0);
/* If red is present... */
if (red != (-1)) {
        /* Deallocate it. */
        gdImageColorDeallocate(im, red);
        /* Allocate blue, reusing slot in table.
                Existing red pixels will change color. */
        blue = gdImageColorAllocate(im, 0, 0, 255);
}
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

        void gdImageColorTransparent(gdImagePtr im, int color)
                _(FUNCTION)_
                gdImageColorTransparent sets the transparent color index
                for the specified image to the specified index. To
                indicate that there should be _no_ transparent color,
                invoke gdImageColorTransparent with a color index of -1.
                
                The color index used should be an index allocated by
                gdImageColorAllocate, whether explicitly invoked by your
                code or implicitly invoked by loading an image. In order
                to ensure that your image has a reasonable appearance
                when viewed by users who do not have transparent
                background capabilities, be sure to give reasonable RGB
                values to the color you allocate for use as a transparent
                color, _even though it will be transparent on systems
                that support transparency_.
                

... inside a function ...
gdImagePtr im;
int black;
FILE *in, *out;
in = fopen("photo.png", "rb");
im = gdImageCreateFromPng(in);
fclose(in);
/* Look for black in the color table and make it transparent. */
black = gdImageColorExact(im, 0, 0, 0);
/* If black is present... */
if (black != (-1)) {
        /* Make it transparent */
        gdImageColorTransparent(im, black);
}
/* Save the newly-transparent image back to the file */
out = fopen("photo.png", "wb");
gdImagePng(im, out);
fclose(out);
/* Destroy it */
gdImageDestroy(im);

  Copying and resizing functions
  
        void gdImageCopy(gdImagePtr dst, gdImagePtr src, int dstX, int
                dstY, int srcX, int srcY, int w, int h) _(FUNCTION)_
                gdImageCopy is used to copy a rectangular portion of one
                image to another image. (For a way of stretching or
                shrinking the image in the process, see
                gdImageCopyResized.)
                
                The dst argument is the destination image to which the
                region will be copied. The src argument is the source
                image from which the region is copied. The dstX and dstY
                arguments specify the point in the destination image to
                which the region will be copied. The srcX and srcY
                arguments specify the upper left corner of the region in
                the source image. The w and h arguments specify the width
                and height of the region.
                
                When you copy a region from one location in an image to
                another location in the same image, gdImageCopy will
                perform as expected unless the regions overlap, in which
                case the result is unpredictable.
                
                _Important note on copying between images:_ since
                different images do not necessarily have the same color
                tables, pixels are not simply set to the same color index
                values to copy them. gdImageCopy will attempt to find an
                identical RGB value in the destination image for each
                pixel in the copied portion of the source image by
                invoking gdImageColorExact. If such a value is not found,
                gdImageCopy will attempt to allocate colors as needed
                using gdImageColorAllocate. If both of these methods
                fail, gdImageCopy will invoke gdImageColorClosest to find
                the color in the destination image which most closely
                approximates the color of the pixel being copied.
                

... Inside a function ...
gdImagePtr im_in;
gdImagePtr im_out;
int x, y;
FILE *in;
FILE *out;
/* Load a small png to tile the larger one with */
in = fopen("small.png", "rb");
im_in = gdImageCreateFromPng(in);
fclose(in);
/* Make the output image four times as large on both axes */
im_out = gdImageCreate(im_in->sx * 4, im_in->sy * 4);
/* Now tile the larger image using the smaller one */
for (y = 0; (y < 4); y++) {
        for (x = 0; (x < 4); x++) {
                gdImageCopy(im_out, im_in,
                        x * im_in->sx, y * im_in->sy,
                        0, 0,
                        im_in->sx, im_in->sy);
        }
}
out = fopen("tiled.png", "wb");
gdImagePng(im_out, out);
fclose(out);
gdImageDestroy(im_in);
gdImageDestroy(im_out);

        void gdImageCopyResized(gdImagePtr dst, gdImagePtr src, int dstX,
                int dstY, int srcX, int srcY, int destW, int destH, int
                srcW, int srcH) _(FUNCTION)_
                gdImageCopyResized is used to copy a rectangular portion
                of one image to another image. The X and Y dimensions of
                the original region and the destination region can vary,
                resulting in stretching or shrinking of the region as
                appropriate. (For a simpler version of this function
                which does not deal with resizing, see gdImageCopy.)
                
                The dst argument is the destination image to which the
                region will be copied. The src argument is the source
                image from which the region is copied. The dstX and dstY
                arguments specify the point in the destination image to
                which the region will be copied. The srcX and srcY
                arguments specify the upper left corner of the region in
                the source image. The dstW and dstH arguments specify the
                width and height of the destination region. The srcW and
                srcH arguments specify the width and height of the source
                region and can differ from the destination size, allowing
                a region to be scaled during the copying process.
                
                When you copy a region from one location in an image to
                another location in the same image, gdImageCopy will
                perform as expected unless the regions overlap, in which
                case the result is unpredictable. If this presents a
                problem, create a scratch image in which to keep
                intermediate results.
                
                _Important note on copying between images:_ since images
                do not necessarily have the same color tables, pixels are
                not simply set to the same color index values to copy
                them. gdImageCopy will attempt to find an identical RGB
                value in the destination image for each pixel in the
                copied portion of the source image by invoking
                gdImageColorExact. If such a value is not found,
                gdImageCopy will attempt to allocate colors as needed
                using gdImageColorAllocate. If both of these methods
                fail, gdImageCopy will invoke gdImageColorClosest to find
                the color in the destination image which most closely
                approximates the color of the pixel being copied.
                

... Inside a function ...
gdImagePtr im_in;
gdImagePtr im_out;
int x, y;
FILE *in;
FILE *out;
/* Load a small png to expand in the larger one */
in = fopen("small.png", "rb");
im_in = gdImageCreateFromPng(in);
fclose(in);
/* Make the output image four times as large on both axes */
im_out = gdImageCreate(im_in->sx * 4, im_in->sy * 4);
/* Now copy the smaller image, but four times larger */
gdImageCopyResized(im_out, im_in, 0, 0, 0, 0,
        im_out->sx, im_out->sy,
        im_in->sx, im_in->sy);
out = fopen("large.png", "wb");
gdImagePng(im_out, out);
fclose(out);
gdImageDestroy(im_in);
gdImageDestroy(im_out);

        void gdImageCopyMerge(gdImagePtr dst, gdImagePtr src, int dstX,
                int dstY, int srcX, int srcY, int w, int h, int pct)
                _(FUNCTION)_
                gdImageCopyMerge is almost identical to gdImageCopy,
                except that it 'merges' the two images by an amount
                specified in the last parameter. If the last parameter is
                100, then it will function identically to gdImageCopy -
                the source image replaces the pixels in the destination.
                
                If, however, the _pct_ parameter is less than 100, then
                the two images are merged. With pct = 0, no action is
                taken.
                
                This feature is most useful to 'highlight' sections of an
                image by merging a solid color with pct = 50:
                

... Inside a function ...
gdImageCopyMerge(im_out, im_in, 100, 200, 0, 0, 30, 50, 50);

        void gdImageCopyMergeGray(gdImagePtr dst, gdImagePtr src, int
                dstX, int dstY, int srcX, int srcY, int w, int h, int
                pct) _(FUNCTION)_
                gdImageCopyMergeGray is almost identical to
                gdImageCopyMerge, except that when merging images it
                preserves the hue of the source by converting the
                destination pixels to grey scale before the copy
                operation.
                

... Inside a function ...
gdImageCopyMergeGray(im_out, im_in, 100, 200, 0, 0, 30, 50, 50);

        void gdImagePaletteCopy(gdImagePtr dst, gdImagePtr src)
                _(FUNCTION)_
                Copies a palette from one image to another, doing it's
                best to match the colors in the target image to the
                colors in the source palette.
                
  Miscellaneous Functions
  
              int gdImageCompare(gdImagePtr im1, gdImagePtr im2)
                      _(FUNCTION)_
                      gdImageCompare returns a bitmap indicating if the
                      two images are different. The members of the bitmap
                      are defined in gd.h, but the most important is
                      GD_CMP_IMAGE, which indicated that the images will
                      actually appear different when displayed. Other,
                      less important, differences relate to pallette
                      entries. Any difference in the transparent colour
                      is assumed to make images display differently, even
                      if the transparent colour is not used.
                      

... Inside a function ...
cmpMask = gdImageCompare(im1, im2);

              gdImageInterlace(gdImagePtr im, int interlace) _(FUNCTION)_
                      
                      gdImageInterlace is used to determine whether an
                      image should be stored in a linear fashion, in
                      which lines will appear on the display from first
                      to last, or in an interlaced fashion, in which the
                      image will "fade in" over several passes. By
                      default, images are not interlaced.
                      
                      A nonzero value for the interlace argument turns on
                      interlace; a zero value turns it off. Note that
                      interlace has no effect on other functions, and has
                      no meaning unless you save the image in PNG format;
                      the gd and xbm formats do not support interlace.
                      
                      When a PNG is loaded with gdImageCreateFromPng ,
                      interlace will be set according to the setting in
                      the PNG file.
                      
                      Note that many PNG viewers and web browsers do _not_
                      support interlace. However, the interlaced PNG
                      should still display; it will simply appear all at
                      once, just as other images do.
                      

gdImagePtr im;
FILE *out;
/* ... Create or load the image... */

/* Now turn on interlace */
gdImageInterlace(im, 1);
/* And open an output file */
out = fopen("test.png", "wb");
/* And save the image */
gdImagePng(im, out);
fclose(out);
gdImageDestroy(im);

  Constants
  
                    gdBrushed _(CONSTANT)_
                            Used in place of a color when invoking a
                            line-drawing function such as gdImageLine or
                            gdImageRectangle. When gdBrushed is used as
                            the color, the brush image set with
                            gdImageSetBrush is drawn in place of each
                            pixel of the line (the brush is usually
                            larger than one pixel, creating the effect of
                            a wide paintbrush). See also gdStyledBrushed
                            for a way to draw broken lines with a series
                            of distinct copies of an image.
                            
                    gdMaxColors_(CONSTANT)_
                            The constant 256. This is the maximum number
                            of colors in a PNG file according to the PNG
                            standard, and is also the maximum number of
                            colors in a gd image.
                            
                    gdStyled _(CONSTANT)_
                            Used in place of a color when invoking a
                            line-drawing function such as gdImageLine or
                            gdImageRectangle. When gdStyled is used as
                            the color, the colors of the pixels are drawn
                            successively from the style that has been set
                            with gdImageSetStyle. If the color of a pixel
                            is equal to gdTransparent, that pixel is not
                            altered. (This mechanism is completely
                            unrelated to the "transparent color" of the
                            image itself; see gdImageColorTransparent
                            gdImageColorTransparent for that mechanism.)
                            See also gdStyledBrushed.
                            
                    gdStyledBrushed _(CONSTANT)_
                            Used in place of a color when invoking a
                            line-drawing function such as gdImageLine or
                            gdImageRectangle. When gdStyledBrushed is
                            used as the color, the brush image set with
                            gdImageSetBrush is drawn at each pixel of the
                            line, providing that the style set with
                            gdImageSetStyle contains a nonzero value (OR
                            gdTransparent, which does not equal zero but
                            is supported for consistency) for the current
                            pixel. (Pixels are drawn successively from
                            the style as the line is drawn, returning to
                            the beginning when the available pixels in
                            the style are exhausted.) Note that this
                            differs from the behavior of gdStyled, in
                            which the values in the style are used as
                            actual pixel colors, except for
                            gdTransparent.
                            
                    gdDashSize _(CONSTANT)_
                            The length of a dash in a dashed line.
                            Defined to be 4 for backwards compatibility
                            with programs that use gdImageDashedLine. New
                            programs should use gdImageSetStyle and call
                            the standard gdImageLine function with the
                            special "color" gdStyled or gdStyledBrushed.
                            
                    gdTiled _(CONSTANT)_
                            Used in place of a normal color in
                            gdImageFilledRectangle, gdImageFilledPolygon,
                            gdImageFill, and gdImageFillToBorder. gdTiled
                            selects a pixel from the tile image set with
                            gdImageSetTile in such a way as to ensure
                            that the filled area will be tiled with
                            copies of the tile image. See the discussions
                            of gdImageFill and gdImageFillToBorder for
                            special restrictions regarding those
                            functions.
                            
                    gdTransparent _(CONSTANT)_
                            Used in place of a normal color in a style to
                            be set with gdImageSetStyle. gdTransparent is
                            _not_ the transparent color index of the
                            image; for that functionality please see
                            gdImageColorTransparent.
                            
  About the additional .gd image file format
  
                            In addition to reading and writing the PNG
                            format and reading the X Bitmap format, gd
                            has the capability to read and write its own
                            ".gd" format. This format is _not_ intended
                            for general purpose use and should never be
                            used to distribute images. It is not a
                            compressed format. Its purpose is solely to
                            allow very fast loading of images your
                            program needs often in order to build other
                            images for output. If you are experiencing
                            performance problems when loading large,
                            fixed PNG images your program needs to
                            produce its output images, you may wish to
                            examine the functions gdImageCreateFromGd and
                            gdImageGd, which read and write .gd format
                            images.
                            
                            The program "pngtogd.c" is provided as a
                            simple way of converting .png files to .gd
                            format. I emphasize again that you will not
                            need to use this format unless you have a
                            need for high-speed loading of a few
                            frequently-used images in your program.
                            
  About the .gd2 image file format
  
                            In addition to reading and writing the PNG
                            format and reading the X Bitmap format, gd
                            has the capability to read and write its own
                            ".gd2" format. This format is _not_ intended
                            for general purpose use and should never be
                            used to distribute images. It is a compressed
                            format allowing pseudo-random access to large
                            image files. Its purpose is solely to allow
                            very fast loading of _parts_ of images If you
                            are experiencing performance problems when
                            loading large, fixed PNG images your program
                            needs to produce its output images, you may
                            wish to examine the functions
                            gdImageCreateFromGd2,
                            gdImageCreateFromGd2Part and gdImageGd2,
                            which read and write .gd2 format images.
                            
                            The program "pngtogd2.c" is provided as a
                            simple way of converting .png files to .gd2
                            format.
                            
  About the gdIOCtx structure
  
                            Version 1.5 of GD added a new style of I/O
                            based on an IOCtx structure (the most
                            up-to-date version can be found in gd_io.h):
                            

typedef struct gdIOCtx {
        int     (*getC)(struct gdIOCtx*);
        int     (*getBuf)(struct gdIOCtx*, void*, int);

        void     (*putC)(struct gdIOCtx*, int);
        int     (*putBuf)(struct gdIOCtx*, const void*, int);

        int     (*seek)(struct gdIOCtx*, const int);
        long    (*tell)(struct gdIOCtx*);

        void    (*free)(struct gdIOCtx*);

} gdIOCtx;

                    Most functions that accepted files in previous
                            versions now also have a counterpart that
                            accepts an I/O context. These functions have
                            a 'Ctx' suffix.
                            
                            The Ctx routines use the function pointers in
                            the I/O context pointed to by gdIOCtx to
                            perform all I/O. Examples of how to implement
                            an I/O context can be found in io_file.c
                            (which provides a wrapper for file routines),
                            and io_dp.c (which implements in-memory
                            storage).
                            
                            It is not necessary to implement all
                            functions in an I/O context if you know that
                            it will only be used in limited
                            cirsumstances. At the time of writing
                            (Version 1.6.1, July 1999), the known
                            requirements are:
                            
                            All   Must have 'free',
                            Anything that reads from the context Must
                            have 'getC' and 'getBuf',
                            Anything that writes to the context Must have
                            'putC' and 'putBuf'.
                            If gdCreateFromGd2Part is called Must also
                            have 'seek' and 'tell'.
                            If gdImageGd2 is called Must also have 'seek'
                            and 'tell'.
                            
  Please tell us you're using gd!
  
                            When you contact us and let us know you are
                            using gd, you help us justify the time spent
                            in maintaining and improving it. So please
                            let us know. If the results are publicly
                            visible on the web, a URL is a wonderful
                            thing to receive, but if it's not a publicly
                            visible project, a simple note is just as
                            welcome.
                            
  If you have problems
  
                            If you have any difficulties with gd, feel
                            free to contact the author, Thomas Boutell.
                            Problems relating to the gd2 format should be
                            addressed to Philip Warner.
                            
                            _Be sure to read this manual carefully first.
                            _
  Alphabetical quick index
  
                            gdBrushed | gdDashSize | gdFont | gdFontPtr |
                            gdImage | gdImageArc | gdImageBlue |
                            gdImageBoundsSafe | gdImageChar |
                            gdImageCharUp | gdImageColorAllocate |
                            gdImageColorClosest | gdImageColorDeallocate
                            | gdImageColorExact | gdImageColorResolve |
                            gdImageColorTransparent | gdImageCopy |
                            gdImageCopyResized | gdImageCreate |
                            gdImageCreateFromGd | gdImageCreateFromGd2 |
                            gdImageCreateFromGd2Part |
                            gdImageCreateFromPng |
                            gdImageCreateFromPngSource |
                            gdImageCreateFromXbm | gdImageCreateFromXpm |
                            gdImageDashedLine | gdImageDestroy |
                            gdImageFill | gdImageFillToBorder |
                            gdImageFilledRectangle | gdImageGd |
                            gdImageGd2 | gdImageGetInterlaced |
                            gdImageGetPixel | gdImageGetTransparent |
                            gdImageGreen | gdImageInterlace | gdImageLine
                            | gdImageFilledPolygon | gdImagePaletteCopy |
                            gdImagePng | gdImagePngToSink |
                            gdImagePolygon | gdImagePtr |
                            gdImageRectangle | gdImageRed |
                            gdImageSetBrush | gdImageSetPixel |
                            gdImageSetStyle | gdImageSetTile |
                            gdImageString | gdImageString16 |
                            gdImageStringTTF | gdImageStringUp |
                            gdImageStringUp16 | gdMaxColors | gdPoint |
                            gdStyled | gdStyledBrushed | gdTiled |
                            gdTransparent
                            
                            _Boutell.Com, Inc._
All components in the "contrib" cluster are not supported. Although shipped
with Vision2, the cluster is provided to provide a convenient place for useful
additions by users for users. If you have some classes that you feel would be suited for
inclusion in this cluster, then please send details to http://support.eiffel.com and
submit as a change request.We do not store the icon path in the .resx file as it is harder to make a build, this is
why the icon is encoded in the resx file.
<!DOCTYPE HTML public "-//W3C//DTD HTML 4.0 Frameset//EN">
<html>
	<head>
		<title>Revisions</title>
			<style>ul.circle{list-style:circle;}
	</style>
			<style>ul.square{list-style:square;}
	</style>
	</head>
	<body>
		<h1>Vision2 Tour</h1>
		<P>Welcome to the documentation for the Vision2 tour.<br> This interactive system allows you to explore the controls (known as widgets) available with the EiffelVision2 library, manipulate their properties, and examine code demonstrating sample usage.</P>
<H2>Getting Started</H2>
	<P>After launching the tour, you will be presented with a window containing a list of different EiffelVision2 widget types to the left hand side. Select the type of widget that you wish to manipulate from the list, and the tour will become focused on that paticular widget type. As a result of this, the right hand side of the window will display three different options in a tab control :- Properties, Tests and Documentation, each of which may be selected at will and are described below. You may change the currently selected widget type by selecting a different item from the list on the left hand side of the window at any time.</P>
<H2>Properties</h2>
	<P>When the properties tab is selected, you may manipulate the current properties that apply to the selected widget type. Note that the properties available are not necessarily exhaustive, but include most properties for each widget type.</P>
	<P>A widget matching the selected type is displayed in the middle of the window, surrounded by a blue border. To the right of this are a set of controls allowing you to modify the properties of the widget. If you hold the mouse over one of these controls, you will see the  corresponding feature name listed as a tooltip.</P>
	<P>Below the actual widget, is an area marked "Output" into which events recieved by the widget are displayed. If you select the "Events" tab, you may turn on and off the events that you wish to monitor by checking and unchecking the associated event name. By default, all events are recorded.</P>

<H2>Tests</h2>
	<P>When the tests tab is selected, you will see an instance of the selected control type surrounded by a blue border.To the bottom of this are a series of tabs, each corresponding to a different test. By selecting a different tab, you will change the test that is displayed. Each of these tests is designed to demonstrate useful functionaility of the current control type. Displayed below the tests, is a text area, showing the source code that was used to generate the test.</P>
	<P>Upon selecting the tests tab, you will notice that the "generate" tool bar button becomes enabled. This allows you to generate a stand alone EiffelVision2 application corresponding to the current test that is displayed. This will include an ace file which should be used for compilation. If you select the "generate" button, a dialog will be displayed, informing you of the files that will be generated, and requiring you to select a directory for this generation. Clicking the "OK" button will cause the generation to be performed in the selected directory.<br>
If you now start EiffelStudio and select the newly generated ace file, the test system will be compiled and once completed, allows you to interactively modify the source code.</P>
<H2>Documentation</h2>
	<P>When the documentation tab is selected, the interface view of the Eiffel Class corresponding to the selected widget type will be displayed. You may browse through this to gain an understanding of features available for the selected control type. A search tool allows you to search for a text, and the size of the text displayed may also be adjusted.</P>
	</body>
</html>
The Object editor was a feature of EiffelBuild which allowed you to quickly and easily build
interfaces for editing objects.

This version has been removed from EiffelBuild so it is no longer dependent on it. This is why
you may find references to Build within the code, and some classes still named accordingly. While
extracting the tool, the goal was to change as little as possible in order to preserve the
original mechanism.

EiffelBuild was built using the original Vision library and therefore, a great deal of modifications
were required to build the tool in Vision2, and to make it generate Vision2 code.

In Build, the tool would generate internal structures which were then later generated into code.
In this version, the only form of output is the generated code.

This tool reads in files generated in EiffelStudio. Select "tools", "documentation". Then select
the build filter and hen the files you wish to include on the next option. The format you then need to
select is "flat contracts" and then go ahead and generate the files. You will need to modify the
extensions of the generated files to .BUI if they are not already.

When setting up this application, you will need to set `Common_directory' in EB_ENVIRONMENT to
the location where the .BUI files outputted from EiffelStudio are located. If you do not do this correctly,
you will not be able to select any classes to build an object tool for.

This version of the object tool is by no means complete, but is now Vision2 compatible, stand alone, and
now ready for further development.

The initial conversion to Vision2 compatibility was performed by Julian Rogers around the middle of August 2001,
so if this has not been updated in accordance with Vision2 changes, that date may be very useful. Good luck.



Included in this "notes" directory is a sample output from the object tool.Summary
-------
This directory contains ASM implementations of the functions
longest_match() and inflate_fast(), for 64 bits x86 (both AMD64 and Intel EM64t),
for use with Microsoft Macro Assembler (x64) for AMD64 and Microsoft C++ 64 bits.

gvmat64.asm is written by Gilles Vollant (2005), by using Brian Raiter 686/32 bits
   assembly optimized version from Jean-loup Gailly original longest_match function

inffasx64.asm and inffas8664.c were written by Chris Anderson, by optimizing
   original function from Mark Adler

Use instructions
----------------
Assemble the .asm files using MASM and put the object files into the zlib source
directory.  You can also get object files here:

     http://www.winimage.com/zLibDll/zlib124_masm_obj.zip

define ASMV and ASMINF in your project. Include inffas8664.c in your source tree,
and inffasx64.obj and gvmat64.obj as object to link.


Build instructions
------------------
run bld_64.bat with Microsoft Macro Assembler (x64) for AMD64 (ml64.exe)

ml64.exe is given with Visual Studio 2005, Windows 2003 server DDK

You can get Windows 2003 server DDK with ml64 and cl for AMD64 from
  http://www.microsoft.com/whdc/devtools/ddk/default.mspx for low price)

This directory contains a Pascal (Delphi, Kylix) interface to the
zlib data compression library.


Directory listing
=================

zlibd32.mak     makefile for Borland C++
example.pas     usage example of zlib
zlibpas.pas     the Pascal interface to zlib
readme.txt      this file


Compatibility notes
===================

- Although the name "zlib" would have been more normal for the
  zlibpas unit, this name is already taken by Borland's ZLib unit.
  This is somehow unfortunate, because that unit is not a genuine
  interface to the full-fledged zlib functionality, but a suite of
  class wrappers around zlib streams.  Other essential features,
  such as checksums, are missing.
  It would have been more appropriate for that unit to have a name
  like "ZStreams", or something similar.

- The C and zlib-supplied types int, uInt, long, uLong, etc. are
  translated directly into Pascal types of similar sizes (Integer,
  LongInt, etc.), to avoid namespace pollution.  In particular,
  there is no conversion of unsigned int into a Pascal unsigned
  integer.  The Word type is non-portable and has the same size
  (16 bits) both in a 16-bit and in a 32-bit environment, unlike
  Integer.  Even if there is a 32-bit Cardinal type, there is no
  real need for unsigned int in zlib under a 32-bit environment.

- Except for the callbacks, the zlib function interfaces are
  assuming the calling convention normally used in Pascal
  (__pascal for DOS and Windows16, __fastcall for Windows32).
  Since the cdecl keyword is used, the old Turbo Pascal does
  not work with this interface.

- The gz* function interfaces are not translated, to avoid
  interfacing problems with the C runtime library.  Besides,
    gzprintf(gzFile file, const char *format, ...)
  cannot be translated into Pascal.


Legal issues
============

The zlibpas interface is:
  Copyright (C) 1995-2003 Jean-loup Gailly and Mark Adler.
  Copyright (C) 1998 by Bob Dellaca.
  Copyright (C) 2003 by Cosmin Truta.

The example program is:
  Copyright (C) 1995-2003 by Jean-loup Gailly.
  Copyright (C) 1998,1999,2000 by Jacques Nomssi Nzali.
  Copyright (C) 2003 by Cosmin Truta.

  This software is provided 'as-is', without any express or implied
  warranty.  In no event will the author be held liable for any damages
  arising from the use of this software.

  Permission is granted to anyone to use this software for any purpose,
  including commercial applications, and to alter it and redistribute it
  freely, subject to the following restrictions:

  1. The origin of this software must not be misrepresented; you must not
     claim that you wrote the original software. If you use this software
     in a product, an acknowledgment in the product documentation would be
     appreciated but is not required.
  2. Altered source versions must be plainly marked as such, and must not be
     misrepresented as being the original software.
  3. This notice may not be removed or altered from any source distribution.

Building instructions for the DLL versions of Zlib 1.2.11
========================================================

This directory contains projects that build zlib and minizip using
Microsoft Visual C++ 9.0/10.0.

You don't need to build these projects yourself. You can download the
binaries from:
  http://www.winimage.com/zLibDll

More information can be found at this site.





Build instructions for Visual Studio 2008 (32 bits or 64 bits)
--------------------------------------------------------------
- Decompress current zlib, including all contrib/* files
- Compile assembly code (with Visual Studio Command Prompt) by running:
   bld_ml64.bat (in contrib\masmx64)
   bld_ml32.bat (in contrib\masmx86)
- Open contrib\vstudio\vc9\zlibvc.sln with Microsoft Visual C++ 2008
- Or run: vcbuild /rebuild contrib\vstudio\vc9\zlibvc.sln "Release|Win32"

Build instructions for Visual Studio 2010 (32 bits or 64 bits)
--------------------------------------------------------------
- Decompress current zlib, including all contrib/* files
- Open contrib\vstudio\vc10\zlibvc.sln with Microsoft Visual C++ 2010

Build instructions for Visual Studio 2012 (32 bits or 64 bits)
--------------------------------------------------------------
- Decompress current zlib, including all contrib/* files
- Open contrib\vstudio\vc11\zlibvc.sln with Microsoft Visual C++ 2012

Build instructions for Visual Studio 2013 (32 bits or 64 bits)
--------------------------------------------------------------
- Decompress current zlib, including all contrib/* files
- Open contrib\vstudio\vc12\zlibvc.sln with Microsoft Visual C++ 2013

Build instructions for Visual Studio 2015 (32 bits or 64 bits)
--------------------------------------------------------------
- Decompress current zlib, including all contrib/* files
- Open contrib\vstudio\vc14\zlibvc.sln with Microsoft Visual C++ 2015


Important
---------
- To use zlibwapi.dll in your application, you must define the
  macro ZLIB_WINAPI when compiling your application's source files.


Additional notes
----------------
- This DLL, named zlibwapi.dll, is compatible to the old zlib.dll built
  by Gilles Vollant from the zlib 1.1.x sources, and distributed at
    http://www.winimage.com/zLibDll
  It uses the WINAPI calling convention for the exported functions, and
  includes the minizip functionality. If your application needs that
  particular build of zlib.dll, you can rename zlibwapi.dll to zlib.dll.

- The new DLL was renamed because there exist several incompatible
  versions of zlib.dll on the Internet.

- There is also an official DLL build of zlib, named zlib1.dll. This one
  is exporting the functions using the CDECL convention. See the file
  win32\DLL_FAQ.txt found in this zlib distribution.

- There used to be a ZLIB_DLL macro in zlib 1.1.x, but now this symbol
  has a slightly different effect. To avoid compatibility problems, do
  not define it here.


Gilles Vollant
info@winimage.com

Visual Studio 2013 and 2015 Projects from Sean Hunt
seandhunt_7@yahoo.com

Overview
========

This directory contains an update to the ZLib interface unit,
distributed by Borland as a Delphi supplemental component.

The original ZLib unit is Copyright (c) 1997,99 Borland Corp.,
and is based on zlib version 1.0.4.  There are a series of bugs
and security problems associated with that old zlib version, and
we recommend the users to update their ZLib unit.


Summary of modifications
========================

- Improved makefile, adapted to zlib version 1.2.1.

- Some field types from TZStreamRec are changed from Integer to
  Longint, for consistency with the zlib.h header, and for 64-bit
  readiness.

- The zlib_version constant is updated.

- The new Z_RLE strategy has its corresponding symbolic constant.

- The allocation and deallocation functions and function types
  (TAlloc, TFree, zlibAllocMem and zlibFreeMem) are now cdecl,
  and _malloc and _free are added as C RTL stubs.  As a result,
  the original C sources of zlib can be compiled out of the box,
  and linked to the ZLib unit.


Suggestions for improvements
============================

Currently, the ZLib unit provides only a limited wrapper around
the zlib library, and much of the original zlib functionality is
missing.  Handling compressed file formats like ZIP/GZIP or PNG
cannot be implemented without having this functionality.
Applications that handle these formats are either using their own,
duplicated code, or not using the ZLib unit at all.

Here are a few suggestions:

- Checksum class wrappers around adler32() and crc32(), similar
  to the Java classes that implement the java.util.zip.Checksum
  interface.

- The ability to read and write raw deflate streams, without the
  zlib stream header and trailer.  Raw deflate streams are used
  in the ZIP file format.

- The ability to read and write gzip streams, used in the GZIP
  file format, and normally produced by the gzip program.

- The ability to select a different compression strategy, useful
  to PNG and MNG image compression, and to multimedia compression
  in general.  Besides the compression level

    TCompressionLevel = (clNone, clFastest, clDefault, clMax);

  which, in fact, could have used the 'z' prefix and avoided
  TColor-like symbols

    TCompressionLevel = (zcNone, zcFastest, zcDefault, zcMax);

  there could be a compression strategy

    TCompressionStrategy = (zsDefault, zsFiltered, zsHuffmanOnly, zsRle);

- ZIP and GZIP stream handling via TStreams.


--
Cosmin Truta <cosmint@cs.ubbcluj.ro>
                        ZLib for Ada thick binding (ZLib.Ada)
                        Release 1.3

ZLib.Ada is a thick binding interface to the popular ZLib data
compression library, available at http://www.gzip.org/zlib/.
It provides Ada-style access to the ZLib C library.


        Here are the main changes since ZLib.Ada 1.2:

- Attension: ZLib.Read generic routine have a initialization requirement
  for Read_Last parameter now. It is a bit incompartible with previous version,
  but extends functionality, we could use new parameters Allow_Read_Some and
  Flush now.

- Added Is_Open routines to ZLib and ZLib.Streams packages.

- Add pragma Assert to check Stream_Element is 8 bit.

- Fix extraction to buffer with exact known decompressed size. Error reported by
  Steve Sangwine.

- Fix definition of ULong (changed to unsigned_long), fix regression on 64 bits
  computers. Patch provided by Pascal Obry.

- Add Status_Error exception definition.

- Add pragma Assertion that Ada.Streams.Stream_Element size is 8 bit.


        How to build ZLib.Ada under GNAT

You should have the ZLib library already build on your computer, before
building ZLib.Ada. Make the directory of ZLib.Ada sources current and
issue the command:

  gnatmake test -largs -L<directory where libz.a is> -lz

Or use the GNAT project file build for GNAT 3.15 or later:

  gnatmake -Pzlib.gpr -L<directory where libz.a is>


        How to build ZLib.Ada under Aonix ObjectAda for Win32 7.2.2

1. Make a project with all *.ads and *.adb files from the distribution.
2. Build the libz.a library from the ZLib C sources.
3. Rename libz.a to z.lib.
4. Add the library z.lib to the project.
5. Add the libc.lib library from the ObjectAda distribution to the project.
6. Build the executable using test.adb as a main procedure.


        How to use ZLib.Ada

The source files test.adb and read.adb are small demo programs that show
the main functionality of ZLib.Ada.

The routines from the package specifications are commented.


Homepage: http://zlib-ada.sourceforge.net/
Author: Dmitriy Anisimkov <anisimkov@yahoo.com>

Contributors: Pascal Obry <pascal@obry.org>, Steve Sangwine <sjs@essex.ac.uk>
This directory contains a .Net wrapper class library for the ZLib1.dll

The wrapper includes support for inflating/deflating memory buffers,
.Net streaming wrappers for the gz streams part of zlib, and wrappers
for the checksum parts of zlib. See DotZLib/UnitTests.cs for examples.

Directory structure:
--------------------

LICENSE_1_0.txt       - License file.
readme.txt            - This file.
DotZLib.chm           - Class library documentation
DotZLib.build         - NAnt build file
DotZLib.sln           - Microsoft Visual Studio 2003 solution file

DotZLib\*.cs          - Source files for the class library

Unit tests:
-----------
The file DotZLib/UnitTests.cs contains unit tests for use with NUnit 2.1 or higher.
To include unit tests in the build, define nunit before building.


Build instructions:
-------------------

1. Using Visual Studio.Net 2003:
   Open DotZLib.sln in VS.Net and build from there. Output file (DotZLib.dll)
   will be found ./DotZLib/bin/release or ./DotZLib/bin/debug, depending on
   you are building the release or debug version of the library. Check
   DotZLib/UnitTests.cs for instructions on how to include unit tests in the
   build.

2. Using NAnt:
   Open a command prompt with access to the build environment and run nant
   in the same directory as the DotZLib.build file.
   You can define 2 properties on the nant command-line to control the build:
   debug={true|false} to toggle between release/debug builds (default=true).
   nunit={true|false} to include or esclude unit tests (default=true).
   Also the target clean will remove binaries.
   Output file (DotZLib.dll) will be found in either ./DotZLib/bin/release
   or ./DotZLib/bin/debug, depending on whether you are building the release
   or debug version of the library.

   Examples:
     nant -D:debug=false -D:nunit=false
       will build a release mode version of the library without unit tests.
     nant
       will build a debug version of the library with unit tests
     nant clean
       will remove all previously built files.


---------------------------------
Copyright (c) Henrik Ravn 2004

Use, modification and distribution are subject to the Boost Software License, Version 1.0.
(See accompanying file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

Summary
-------
This directory contains ASM implementations of the functions
longest_match() and inflate_fast().


Use instructions
----------------
Assemble using MASM, and copy the object files into the zlib source
directory, then run the appropriate makefile, as suggested below.  You can
donwload MASM from here:

    http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=7a1c9da0-0510-44a2-b042-7ef370530c64

You can also get objects files here:

    http://www.winimage.com/zLibDll/zlib124_masm_obj.zip

Build instructions
------------------
* With Microsoft C and MASM:
nmake -f win32/Makefile.msc LOC="-DASMV -DASMINF" OBJA="match686.obj inffas32.obj"

* With Borland C and TASM:
make -f win32/Makefile.bor LOCAL_ZLIB="-DASMV -DASMINF" OBJA="match686.obj inffas32.obj" OBJPA="+match686c.obj+match686.obj+inffas32.obj"

                             _   _ ____  _
                         ___| | | |  _ \| |
                        / __| | | | |_) | |
                       ( (__| |_| |  _ <| |___
                        \___|\___/|_| \_\_____|
                             for OpenVMS

History:

 9-MAR-2004, Created this readme. file.  Marty Kuhrt (MSK).
15-MAR-2004, MSK, Updated to reflect the new files in this directory.
14-FEB-2005, MSK, removed config-vms.h_with* file comments
10-FEB-2010, SMS. General update.
14-Jul-2013, JEM, General Update, add GNV build information.


The release notes installed by the PCSI kit consist of this file and the
curl_gnv_build_steps.txt and other useful information.

Prerequisites:

OpenVMS V7.0 or later (any platform)
DECC V6.5 or later
OpenSSL or hp SSL, if you want SSL support

What is Here:

This directory contains the following files for a DCL based build.

backup_gnv_curl_src.com  This procedure backs up the source modules for
                        creating a PCSI kit.

build_curl-config_script.com
                        Procedure to create the curl-config script.

build_gnv_curl.com      This procedure does a build of curl using the
                        GNV utilities and then uses DCL tools to build
                        the libcurl shared image.  The setup_gnv_curl_build.com
                        procedure must be run first.

build_gnv_curl_pcsi_desc.com
                        This procedure builds the pcsi$desc file for
                        creating a PCSI based package.

build_gnv_curl_pcsi_text.com
                        This procedure builds the pcsi$text file for
                        creating a PCSI based package.

build_gnv_curl_release_notes.com
                        This procedure creates the release notes for
                        a PCSI kit based on curl_release_note_start.txt,
                        this readme file, and the curl_gnv_build_steps.txt

build_libcurl_pc.com    Procedure to create a libcurl.pc file.

build_vms.com           DCL based build procedure.

clean_gnv_curl.com      This procedure cleans up the files generated by
                        a GNV based build.

config_h.com            DCL based procedure used by build_vms.com
                        to run generate the curl_config.h file.
                        This is a generic procedure that does most
                        of the work for generating config.h files.

compare_curl_source.com Procedure to compare the working directory
                        with a repository directory or a backup staging
                        directory.

curl_crtl_init.c        A special pre-initialization routine to for
                        programs to behave more Unix like when run
                        under GNV.

curl_gnv_build_steps.txt
                        Detailed instructions on how to built curl using
                        GNV and how to build the libcurl shared image and
                        PCSI kit.

curl_release_note_start.txt
                        The first part of the curl release notes.

curl_startup.com        A procedure run at VMS startup to install the
                        libcurl shared image and to set up the needed
                        logical names.

curlmsg.h               C header defining curl status code macros.

curlmsg.msg             Error message source for curlmsg.h and curlmsg.sdl.

curlmsg.sdl             SDL source defining curl status code constants.

curlmsg_vms.h           Mapping of curl status codes to VMS-form codes.

generate_config_vms_h_curl.com
                        DCL procedure to generate the curl specific
                        definitions for curl_config.h that config_h.com
                        can not properly generate.

generate_vax_transfer.com
                        DCL procedure to read an Alpha/IA64 symbol vector
                        linker option file and generate the VAX transfer
                        vector modules.

gnv_conftest.c_first    A helper file for the configure script.

gnv_curl_configure.sh   A script to run the configure script with the
                        options needed for VMS.

gnv_libcurl_symbols.opt The symbol vectors needed for Alpha and IA64
                        libcurl shared image.

gnv_link_curl.com       Links the libcurl shared image and then links a curl
                        image to use the libcurl.

macro32_exactcase.patch The patch file needed to modify VAX Macro32 to be
                        case sensitive and case preserving.

Makefile.am             curl kit file list for this directory.

Makefile.in             curl kit makefile source for this directory.

make_gnv_curl_install.sh
                        Script to do a make install using GNV after running
                        the configure script.

make_pcsi_curl_kit_name.com
                        This generates the name of the PCSI kit based on
                        the version of curl being built.

pcsi_gnv_curl_file_list.txt
                        This is a text file describing what files should
                        be included in a PCSI kit.

pcsi_product_gnv_curl.com
                        This generates the PCSI kit after the libcurl
                        shared image has been made.

readme.                 This file.

report_openssl_version.c
                        Program to check that the openssl version is new
                        enough for building a shared libcurl image.

setup_gnv_curl_build.com
                        This procedure sets up symbols and logical names
                        for a GNV build environment and also copies some
                        helper files.

stage_curl_install.com  This procedure sets up new_gnu: directory tree to
                        for testing the install and building the PCSI kit.
                        It takes a "remove" option to remove all the staged
                        files.

vms_eco_level.h         This sets the ECO level for the PCSI kit name.


How to Build:

The GNV based build and the DCL based build procedures are not compatible
and you must make sure that none of the build files are present before
running a different type of build.  Use the "REALCLEAN" option for
BUILD_VMS.COM and the "REALCLEAN" option for clean_gnv_curl.com.

The (brute-force) DCL based builder is [.packages.vms]build_vms.com.
Comments in this procedure describe various optional parameters which
enable or disable optional program features, or which control the build
in other ways.  Product files (.EXE, .H, .LIS, .MAP, .OBJ, .OLB, ...)
should be produced in an architecture-specific subdirectory under this
directory ([.ALPHA], [.IA64], [.VAX]).

The file curl_gnv_build_steps.txt contains information on buildling using
the GNV tool kit, building a shared libcurl, and producting a PCSI kit for
distribution.  The curl_gnv_build_steps.text is included in the release
notes file of the PCSI kit.

The building with 64 bit pointers does not currently work.

The build procedure will detect if HP OpenSSL, LDAP, and Kerberos are
installed and default to building with them.

The build procedure will also detect if a compatible ZLIB shared image
is installed from a PCSI kit and default to using it.

   Example build commands:

      @ [.packages.vms]build_vms.com CLEAN
      @ [.packages.vms]build_vms.com LARGE LDAP
      submit /noprint [.packages.vms]build_vms.com /param = (LARGE, LDAP)

The build_vms.com procedure does not build the shared image file or the PCSI
kit.  If you have built a curl with ZLIB and HPSSL support as well as if
LDAP and Kerberos installed, you can use the GNV_LINK_CURL.COM file.

The GNV_LINK_CURL.COM contains information on how to link and run with a newer
version of HP SSL than what may be install on an Alpha or IA64 based system.

To build the PCSI kit, follow the the instructions in the file
curl_gnv_build_steps.txt.

Other Notes:

This release fixes known bugs #22, and #57 in the [curl.docs]known_bugs.
file.

The libcurl formdata.c module and Curl tools post form now have some
understanding of VMS file types.  Files will be posted in STREAM_LF format.

The Curl tool now has some understanding of VMS file types and will upload the
files in STREAM_LF fomat.

When CURL is uploading a VARIABLE format VMS file, it is less efficient as in
order to get the file size, it will first read the entire file once, and then
read the file again for the actual upload.

The Curl tool will now always download files into STREAM_LF format.  Even if a
file by that name with a different format already exists.  This is needed to
allow interrupted downloads to be continued.


The libcurl file module still does not understand VMS file types and requires
the input files to be in STREAM_LF to work property.

The test suites are not supported as of 7.11.0.

The curlmsg.sdl and curlmsg.h files are generated from curlmsg.msg.
This is not done automatically, since the .MSG file is a hand edit
of the relevant stuff from the curl.h file.  If you want to do this
yourself you'll need the SDL package from the freeware collection.
Curl on Symbian OS
==================
This is a basic port of curl and libcurl to Symbian OS.  The port is
a straightforward one using Symbian's P.I.P.S. POSIX compatibility
layer, which was first available for OS version 9.1. A more complete
port would involve writing a Symbian C++ binding, or wrapping libcurl
as a Symbian application server with a C++ API to handle requests
from client applications as well as creating a GUI application to allow
file transfers.  The author has no current plans to do so.

This means that integration with standard Symbian OS programs can be
tricky, since libcurl isn't designed with Symbian's native asynchronous
message passing idioms in mind. However, it may be possible to use libcurl
in an active object-based application through libcurl's multi interface.
The port is most easily used when porting POSIX applications to Symbian
OS using P.I.P.S. (a.k.a. Open C).

libcurl is built as a standard Symbian ordinal-linked DLL, and curl is
built as a text mode EXE application.  They have not been Symbian
Signed, which is required in order to install them on most phones.

Following are some things to keep in mind when using this port.


curl notes
----------
When starting curl in the Windows emulator from the Windows command-line,
place a double-dash -- before the first curl command-line option.
e.g. \epoc32\release\winscw\udeb\curl -- -v http://localhost/
Failure to do so may mean that some of your options won't be correctly
processed.

Symbian's ESHELL allows for redirecting stdin and stdout to files, but
stderr goes to the epocwind.out file (on the emulator).  The standard
curl options -o, --stderr and --trace-ascii can be used to
redirect output to a file (or stdout) instead.

P.I.P.S. doesn't inherit the current working directory at startup from
the shell, so relative path names are always relative to
C:\Private\f0206442\.

P.I.P.S. provides no way to disable echoing of characters as they are
entered, so passwords typed in on the console will be visible.  It also
line buffers keyboard input so interactive telnet sessions are not very
feasible.

All screen output disappears after curl exits, so after a command completes,
curl waits by default for Enter to be pressed before exiting.  This behaviour
is suppressed when the -s option is given.

curl's "home directory" in Symbian is C:\Private\f0206442\. The .curlrc file
is read from this directory on startup.


libcurl notes
-------------
libcurl uses writable static data, so the EPOCALLOWDLLDATA option is
used in its MMP file, with the corresponding additional memory usage
and limitations on the Windows emulator.

curl_global_init() *must* be called (either explicitly or implicitly through
calling certain other libcurl functions) before any libcurl functions
that could allocate memory (like curl_getenv()).

P.I.P.S. doesn't support signals or the alarm() call, so some timeouts
(such as the connect timeout) are not honoured. This should not be
an issue once support for CURLRES_THREADED is added for Symbian.

P.I.P.S. causes a USER:87 panic if certain timeouts much longer than
half an hour are selected.

LDAP, SCP or SFTP methods are not supported due to lack of support for
the dependent libraries on Symbian.

gzip and deflate decompression is supported when the appropriate macro
is uncommented in the libcurl.mmp file.

SSL/TLS encryption is not enabled by default, but it is possible to add
when the OpenSSL libraries included in the S60 Open C SDK are available.
The appropriate macro in the libcurl.mmp file must be uncommented to
enable support.

NTLM authentication may not work on some servers due to the lack of
MD4 support in the OpenSSL libraries included with Open C.

Debug builds are not supported (i.e. --enable-debug) because they cause
additional symbol exports in the library which are not frozen in the .def
files.


Dan Fandrich
dan@coneharvesters.com
March 2010
The perl scripts in this directory are my 'hack' to generate
multiple different assembler formats via the one original script.

The way to use this library is to start with adding the path to this directory
and then include it.

push(@INC,"perlasm","../../perlasm");
require "x86asm.pl";

The first thing we do is setup the file and type of assembler

&asm_init($ARGV[0]);

The first argument is the 'type'.  Currently
'cpp', 'sol', 'a.out', 'elf' or 'win32'.
Argument 2 is the file name.

The reciprocal function is
&asm_finish() which should be called at the end.

There are 2 main 'packages'. x86ms.pl, which is the Microsoft assembler,
and x86unix.pl which is the unix (gas) version.

Functions of interest are:
&external_label("des_SPtrans");	declare and external variable
&LB(reg);			Low byte for a register
&HB(reg);			High byte for a register
&BP(off,base,index,scale)	Byte pointer addressing
&DWP(off,base,index,scale)	Word pointer addressing
&stack_push(num)		Basically a 'sub esp, num*4' with extra
&stack_pop(num)			inverse of stack_push
&function_begin(name,extra)	Start a function with pushing of
				edi, esi, ebx and ebp.  extra is extra win32
				external info that may be required.
&function_begin_B(name,extra)	Same as normal function_begin but no pushing.
&function_end(name)		Call at end of function.
&function_end_A(name)		Standard pop and ret, for use inside functions
&function_end_B(name)		Call at end but with poping or 'ret'.
&swtmp(num)			Address on stack temp word.
&wparam(num)			Parameter number num, that was push
				in C convention.  This all works over pushes
				and pops.
&comment("hello there")		Put in a comment.
&label("loop")			Refer to a label, normally a jmp target.
&set_label("loop")		Set a label at this point.
&data_word(word)		Put in a word of data.

So how does this all hold together?  Given

int calc(int len, int *data)
	{
	int i,j=0;

	for (i=0; i<len; i++)
		{
		j+=other(data[i]);
		}
	}

So a very simple version of this function could be coded as

	push(@INC,"perlasm","../../perlasm");
	require "x86asm.pl";
	
	&asm_init($ARGV[0]);

	&external_label("other");

	$tmp1=	"eax";
	$j=	"edi";
	$data=	"esi";
	$i=	"ebp";

	&comment("a simple function");
	&function_begin("calc");
	&mov(	$data,		&wparam(1)); # data
	&xor(	$j,		$j);
	&xor(	$i,		$i);

	&set_label("loop");
	&cmp(	$i,		&wparam(0));
	&jge(	&label("end"));

	&mov(	$tmp1,		&DWP(0,$data,$i,4));
	&push(	$tmp1);
	&call(	"other");
	&add(	$j,		"eax");
	&pop(	$tmp1);
	&inc(	$i);
	&jmp(	&label("loop"));

	&set_label("end");
	&mov(	"eax",		$j);

	&function_end("calc");

	&asm_finish();

The above example is very very unoptimised but gives an idea of how
things work.

There is also a cbc mode function generator in cbc.pl

&cbc(	$name,
	$encrypt_function_name,
	$decrypt_function_name,
	$true_if_byte_swap_needed,
	$parameter_number_for_iv,
	$parameter_number_for_encrypt_flag,
	$first_parameter_to_pass,
	$second_parameter_to_pass,
	$third_parameter_to_pass);

So for example, given
void BF_encrypt(BF_LONG *data,BF_KEY *key);
void BF_decrypt(BF_LONG *data,BF_KEY *key);
void BF_cbc_encrypt(unsigned char *in, unsigned char *out, long length,
        BF_KEY *ks, unsigned char *iv, int enc);

&cbc("BF_cbc_encrypt","BF_encrypt","BF_encrypt",1,4,5,3,-1,-1);

&cbc("des_ncbc_encrypt","des_encrypt","des_encrypt",0,4,5,3,5,-1);
&cbc("des_ede3_cbc_encrypt","des_encrypt3","des_decrypt3",0,6,7,3,4,5);

Testing scripts are located in Src/com_wizard/testing

Before starting test you need to modify 
config.eif line 20:
replace 
wkoptimize: "-Od -Zi"
by 
wkoptimize: -Zm300"

This would prevent C compiler from crashing during the
test. This only become a problem during testing of Office
type libraries because they are very very big and the 
generated code takes more than 1GB of hard drive space.

test.bat calls test_c.bat and test_s.bat
test_c.bat is a list of calls to test_client.bat with the first 
argument is a name of a directory and the second argument is the
full path to a type library. This file might need to be modified
because it contains type library locations on my machine.

test_s.bat is similar to test_c.bat, but it calls test_server.bat.

test_client.bat takes two arguments: name of the directory and 
name of the type library.
The script generates everything in D:\testing directory, which 
should exist before script starts. Obviously, the script can be modified
to accept the name of the root directory or have different root directory. 
The hard drive should have at least 1.5 GB of free space. The space is 
needed during the tests, and it is freed if all tests succeed.
The first argument is the name of subdirectory of d:\testing directory.

Line 11 contains full path to com_wizard_cmd.exe, and it is 
needed to be adjusted.
test_client.bat first removes any remains of previous tests with
the same subdirectory name, then it runs the wizard. If the test succeeds,
the generated directory is removed.
If the test fails, then the generated directory remains, and the file
DIRECTORY_NAME_failed is created, where DIRECTORY_NAME 
is the name of the first argument to the test_client.bat.

test_server.bat is very similar except it generates code in 
D:\testing_server directory, and it tests generating of a COM server.

The scripts are very short. I think they can be easily understood
just by looking into them.

test_status.bat has working directory name on line 13.
It is needs to be modified on every machine.

These scripts test only generation of a COM component from a COM definition
file. There are no scripts for testing generation of a COM componenet 
from an Eiffel Project.

Eiffel Eweasel Converter - Read Me
--------------------------------------

1.0 About:
----------
The Eiffel Eweasel Converter is a tool that can be used to generate eweasel test case class files
that can be executed in Eiffel Studio 6.3 (or greater).


2.0 Command-Line Options
------------------------

There are two command-line options, please use

  eweasel_converter /?

for more information.

3.0 Example
------------------------

Typically the command line is:

eweasel_converter --source c:\your_eweasel_dir\tests --dest c:\where_files_will_be_generated

Note the value of --source and --dest option must be FULL path of directory

4.0 FAQ
--------------------------

If you get following texts when executing the command:

Error: tcf file not exists in dir: E:\es\trunk\eweasel\tests\.
Error: tcf file not exists in dir: E:\es\trunk\eweasel\tests\..
Error: tcf file not exists in dir: E:\es\trunk\eweasel\tests\.svn
Error: tcf file not exists in dir: E:\es\trunk\eweasel\tests\DONT_DELETE

This is normal, don't worry. 


Eiffel Matrix Code Generator - Read Me
--------------------------------------

1.0 About:
----------
The Eiffel Matrix Code Generator (emcgen) is a tool that can be used to generate an Eiffel class
that permits named access, through Eiffel code, to tiles on a pixmap matrix. The pixmap is not require
to generate the code, only the configuration file.

2.0 Configuration Files:
------------------------
Configuration files are INI formatted files, which have very few rules to create.

2.1 Basic Properties
--------------------
All configuration files must contain the following properties, in the default section (top of the document):

	pixel_width
	pixel_height
	width
	height

pixel_width : Matrix tile pixel width. So for 16x16 icons this would be 16.
              Note: Must be greater than 0!
pixel_height: Matrix tile pixel height. So for 16x16 icons this would be 16.
             Note: Must be greater than 0!

width       : Matrix width in the number of tiles, *not* pixel.
              Note: Must be greater than 0!
height      : Matrix width in the number of tiles, *not* pixel.
              Note: Must be greater than 0!

Optional 'name' and 'suffix' properties can be set to indicate the name of the generate class and its contained
features. The 'name' property can be set or overridden via the '-class' command-line switch.

name        : Name of the class to generate
              Note: If an invalid Eiffel class name is specified the name will be formatted.

suffix      : Suffix to give generated feature names
              Note: If an invalid Eiffel feature name suffix is specified the suffix will be formatted.

2.3 Sections
------------
INI sections are used for two purposes. (1) To prefix generate pixmap access feature names and (2) to skip to 
the next line on the matrix.

As an example:

  [section name]
  icon1
  icon2

  [new section]
  icon3

Will generate features:

  section_name_icon1_icon: EV_PIXMAP... -- Icon at line 1 column 1
  section_name_icon2_icon: EV_PIXMAP... -- Icon at line 1 column 2
  new_section_icon3_icon: EV_PIXMAP...  -- Icon at line 2 column 1

Given that a section will skip to the next line, it's foreseeable that you might want to prefix feature names with
a different prefix but continue on the current line. These come in the form of "continuation sections", which are
section's whose labels a prefixed with an '@' symbol.

As an example:

  [section name]
  icon1
  icon2
  
  [@continued]
  icon3
  icon4

Will generate features:

  section_name_icon1_icon: EV_PIXMAP...   -- Icon at line 1 column 1
  section_name_icon2_icon: EV_PIXMAP...   -- Icon at line 1 column 2
  continued_name_icon3_icon: EV_PIXMAP... -- Icon at line 1 column 3
  continued_name_icon4_icon: EV_PIXMAP... -- Icon at line 1 column 5

2.3 Example
-----------

; Pixmap code generation ini file.

class_name=TEST
pixel_width=16
pixel_height=16
width=6
height=6

[icons]
drop feature
hand

[compiler state]
error
success

[@compilation]
melt
compile

3.0 Frame Files
---------------
Next to the emcgen tool there should be a frames folder. This, be default, contains a single frame file. Frame files
are the template files that will be used to generate the Eiffel class.

If you have a custom frame file you want to use the specify it's location using the -frame command-line switch.

3.1 Frame Variables
-------------------
There are a number of frame file variables that are replaced with emcgen generated code. These variables should
be used in your frame files to function correctly. The following list details:

  ${NAME}          : Class name.
  ${ACCESS}        : Generated pixmap access features.
  ${IMPLEMENTATION}: Generated implementation features.
  ${PIXEL_WIDTH}   : Width, in pixels, of a single matrix tile.
  ${PIXEL_HEIGHT}  : Height, in pixels, of a single matrix tile.
  ${WIDTH}         : Width, in tiles, of the matrix.
  ${HEIGHT}        : Height, in tiles, of the matrix.

3.2 Custom Frame Variables
--------------------------
It's possible to define custom frame variable that can change between INI configuration files. To do this, simply add a named property
in the form of:

  name=value

after the require configuration property declaration (such as 'pixel_height', etc.)

Note: name, access, implementation, pixel_width, pixel_height, width and height have special meaning. If you try to set these your
generated Eiffel class may not appear as it should.

To use the custom variables in your frame file use a ${NAME}, where NAME is the upper-cased version of your property name.

4.0 Matrix Pixmaps
------------------
Matrix pixmaps must be created in a desired fashion, in order to be read correctly (unless you have your own frame
file implementation - See Section 5.0).

Using the default frame template file, matrix pixmaps must be bordered by one pixel and each tile padded with a
single pixel. This is to allow the use of a matrix grid that does not interfere with any of the tiles. This is
what tools, such as EiffelStudio, use.

5.0 Command-Line Options
------------------------

To export export all the pixmaps into individual pixmap files, you can use the
option --slice ; for instance:
	emcgen 10x10.ini --slice 10x10.png --pngs 10x10_icons
	(note that the folder 10x10_icons must exists)

There are number of command-line options, please use

  emcgen /?

for more information.

-- I18N_BINARY_SEARCH_ARRAY_DICTIONAY check
-- with two_plural_forms_singular_one_zero
a:I18N_BINARY_SEARCH_ARRAY_DICTIONAY
create a.make (plural_tools.two_plural_forms_singular_one_zero)
data_generation(a,50,100)
data_query(a,50,100)
data_get(a,50,100	h:I18N_HASH_TABLE_DICTIONARY
	
	-- relevant parameters		
	
	create h.make (plural_tools.two_plural_forms_singular_one)
	data_generation(h,50,100)
	data_query(h,50,100)
	data_get(h,50,100)

		
Test is okay!
-- I18N_BINARY_SEARCH_ARRAY_DICTIONAY
-- with two_plural_forms_singular_one

a:I18N_BINARY_SEARCH_ARRAY_DICTIONAY
create a.make (plural_tools.two_plural_forms_singular_one)
data_generation(a,50,100)
data_query(a,50,100)
data_get(a,50,100)h:I18N_HASH_TABLE_DICTIONARY

-- relevant parameters

create h.make (plural_tools.two_plural_forms_singular_one_zero)
data_generation(h,50,100)
data_query(h,50,100)
data_get(h,50,100)How to make the WEL C library `wel.lib'?
----------------------------------------

If you have Borland C, run `make_bcb.bat'.
If you have Microsoft C, run `make_msc.bat'.

The makefiles assume that the C-compiler is in your $PATH environment
variable.

The environment variable ISE_EIFFEL needs to be set to where ISE Eiffel is
installed for these compilation. (This is usually `C:\Eiffel50').

To set the variable, type:

	SET ISE_EIFFEL=C:\Eiffel50
When your Eiffel executable running, Eiffel cURL library needs 3 DLLs, they are:

libcurl.dll, libeay32.dll and ssleay32.dll

Please make sure the 3 DLLs files can be found in your environment PATH or in same folder of your executable.SEE INDEX.HTML FOR AN EASILY BROWSED HYPERTEXT VERSION OF THIS MANUAL.

* * *

                                    gd 1.3
                                       
A graphics library for fast GIF creation

Follow this link to the latest version of this document.

  Table of Contents
  
     * Credits and license terms
     * What's new in version 1.3?
     * What is gd?
     * What if I want to use another programming language?
     * What else do I need to use gd?
     * How do I get gd?
     * How do I build gd?
     * gd basics: using gd in your program
     * webgif: a useful example
     * Function and type reference by category
     * About the additional .gd image file format
     * Please tell us you're using gd!
     * If you have problems
     * Alphabetical quick index
       
   Up to the Boutell.Com, Inc. Home Page
   
  Credits and license terms
  
   In order to resolve any possible confusion regarding the authorship of
   gd, the following copyright statement covers all of the authors who
   have required such a statement. Although his LZW compression code no
   longer appears in gd, the authors wish to thank David Rowley for the
   original LZW-based GIF compression code, which has been removed due to
   patent concerns. If you are aware of any oversights in this copyright
   notice, please contact Thomas Boutell who will be pleased to correct
   them.

COPYRIGHT STATEMENT FOLLOWS THIS LINE

     Portions copyright 1994, 1995, 1996, 1997, 1998, by Cold Spring
     Harbor Laboratory. Funded under Grant P41-RR02188 by the National
     Institutes of Health.
     
     Portions copyright 1996, 1997, 1998, by Boutell.Com, Inc.
     
     GIF decompression code copyright 1990, 1991, 1993, by David Koblas
     (koblas@netcom.com).
     
     Non-LZW-based GIF compression code copyright 1998, by Hutchison
     Avenue Software Corporation (http://www.hasc.com/, info@hasc.com).
     
     Permission has been granted to copy and distribute gd in any
     context, including a commercial application, provided that this
     notice is present in user-accessible supporting documentation.
     
     This does not affect your ownership of the derived work itself, and
     the intent is to assure proper credit for the authors of gd, not to
     interfere with your productive use of gd. If you have questions,
     ask. "Derived works" includes all programs that utilize the
     library. Credit must be given in user-accessible documentation.
     
     Permission to use, copy, modify, and distribute this software and
     its documentation for any purpose and without fee is hereby
     granted, provided that the above copyright notice appear in all
     copies and that both that copyright notice and this permission
     notice appear in supporting documentation. This software is
     provided "as is" without express or implied warranty.
     
END OF COPYRIGHT STATEMENT

  What is gd?
  
   gd is a graphics library. It allows your code to quickly draw images
   complete with lines, arcs, text, multiple colors, cut and paste from
   other images, and flood fills, and write out the result as a .GIF
   file. This is particularly useful in World Wide Web applications,
   where .GIF is the format used for inline images.
   
   gd is not a paint program. If you are looking for a paint program, you
   are looking in the wrong place. If you are not a programmer, you are
   looking in the wrong place.
   
   gd does not provide for every possible desirable graphics operation.
   It is not necessary or desirable for gd to become a kitchen-sink
   graphics package, but version 1.3 incorporates most of the commonly
   requested features for an 8-bit 2D package. Support for scalable
   fonts, and truecolor images, JPEG and PNG is planned for version 2.0.
   Version 1.3 was released to correct longstanding bugs and provide an
   LZW-free GIF compression routine.
   
  What if I want to use another programming language?
  
    Perl
    
   gd can also be used from Perl, courtesy of Lincoln Stein's GD.pm
   library, which uses gd as the basis for a set of Perl 5.x classes.
   GD.pm is based on gd 1.1.1 but gd 1.2 should be compatible.
   
    Any Language
    
   There are, at the moment, at least three simple interpreters that
   perform gd operations. You can output the desired commands to a simple
   text file from whatever scripting language you prefer to use, then
   invoke the interpreter.
   
   These packages are based on gd 1.2 as of this writing but should be
   compatible with gd 1.3 with minimal tweaking.
     * tgd, by Bradley K. Sherman
     * fly, by Martin Gleeson
       
  What's new in version 1.3?
  
   Version 1.3 features the following changes:
   
   Non-LZW-based GIF compression code
          Version 1.3 contains GIF compression code that uses simple Run
          Length Encoding instead of LZW compression, while still
          retaining compatibility with normal LZW-based GIF decoders
          (your browser will still like your GIFs). LZW compression is
          patented by Unisys. This is why there have been no new versions
          of gd for a long time. THANKS to Hutchison Avenue Software
          Corporation for contributing this code. THE NEW CODE PRODUCES
          LARGER GIFS AND IS NOT WELL SUITED TO PHOTOGRAPHIC IMAGES. THIS
          IS A LEGAL ISSUE. IT IS NOT A QUESTION OF TECHNICAL SKILL.
          PLEASE DON'T COMPLAIN ABOUT THE SIZE OF GIF OUTPUT. THANKS!
          
   8-bit fonts, and 8-bit font support
          This improves support for European languages. Thanks are due to
          Honza Pazdziora and also to Jan Pazdziora . Also see the
          provided bdftogd Perl script if you wish to convert fixed-width
          X11 fonts to gd fonts.
          
   16-bit font support (no fonts provided)
          Although no such fonts are provided in the distribution, fonts
          containing more than 256 characters should work if the
          gdImageString16 and gdImageStringUp16 routines are used.
          
   Improvements to the "webgif" example/utility
          The "webgif" utility is now a slightly more useful application.
          Thanks to Brian Dowling for this code.
          
   Corrections to the color resolution field of GIF output
          Thanks to Bruno Aureli.
          
   Fixed polygon fills
          A one-line patch for the infamous polygon fill bug, courtesy of
          Jim Mason. I believe this fix is sufficient. However, if you
          find a situation where polygon fills still fail to behave
          properly, please send code that demonstrates the problem, and a
          fix if you have one. Verifying the fix is important.
          
   Row-major, not column-major
          Internally, gd now represents the array of pixels as an array
          of rows of pixels, rather than an array of columns of pixels.
          This improves the performance of compression and decompression
          routines slightly, because horizontally adjacent pixels are now
          next to each other in memory. This should not affect properly
          written gd applications, but applications that directly
          manipulate the pixels array will require changes.
          
  What else do I need to use gd?
  
   To use gd, you will need an ANSI C compiler. All popular Windows 95
   and NT C compilers are ANSI C compliant. Any full-ANSI-standard C
   compiler should be adequate. The cc compiler released with SunOS 4.1.3
   is not an ANSI C compiler. Most Unix users who do not already have gcc
   should get it. gcc is free, ANSI compliant and a de facto industry
   standard. Ask your ISP why it is missing.
   
   You will also want a GIF viewer, if you do not already have one for
   your system, since you will need a good way to check the results of
   your work. Any web browser will work, but you might be happier with a
   package like Lview Pro for Windows or xv for X. There are GIF viewers
   available for every graphics-capable computer out there, so consult
   newsgroups relevant to your particular system.
   
  How do I get gd?
  
    By HTTP
    
     * Gzipped Tar File (Unix)
     * .ZIP File (Windows)
       
    By FTP
    
     * Gzipped Tar File (Unix)
     * .ZIP File (Windows)
       
  How do I build gd?
  
   In order to build gd, you must first unpack the archive you have
   downloaded. If you are not familiar with tar and gunzip (Unix) or ZIP
   (Windows), please consult with an experienced user of your system.
   Sorry, we cannot answer questions about basic Internet skills.
   
   Unpacking the archive will produce a directory called "gd1.3".
   
    For Unix
    
   cd to the gd1.3 directory and examine the Makefile, which you will
   probably need to change slightly depending on your operating system
   and your needs.
   
    For Windows, Mac, Et Cetera
    
   Create a project using your favorite programming environment. Copy all
   of the gd files to the project directory. Add gd.c to your project.
   Add other source files as appropriate. Learning the basic skills of
   creating projects with your chosen C environment is up to you.
   
   Now, to build the demonstration program, just type "make gddemo" if
   you are working in a command-line environment, or build a project that
   includes gddemo.c if you are using a graphical environment. If all
   goes well, the program "gddemo" will be compiled and linked without
   incident. Depending on your system you may need to edit the Makefile.
   Understanding the basic techniques of compiling and linking programs
   on your system is up to you.
   
   You have now built a demonstration program which shows off the
   capabilities of gd. To see it in action, type "gddemo".
   
   gddemo should execute without incident, creating the file demoout.gif.
   (Note there is also a file named demoin.gif, which is provided in the
   package as part of the demonstration.)
   
   Display demoout.gif in your GIF viewer. The image should be 128x128
   pixels and should contain an image of the space shuttle with quite a
   lot of graphical elements drawn on top of it.
   
   (If you are missing the demoin.gif file, the other items should appear
   anyway.)
   
   Look at demoin.gif to see the original space shuttle image which was
   scaled and copied into the output image.
   
  gd basics: using gd in your program
  
   gd lets you create GIF images on the fly. To use gd in your program,
   include the file gd.h, and link with the libgd.a library produced by
   "make libgd.a", under Unix. Under other operating systems you will add
   gd.c to your own project.
   
   If you want to use the provided fonts, include gdfontt.h, gdfonts.h,
   gdfontmb.h, gdfontl.h and/or gdfontg.h. If you are not using the
   provided Makefile and/or a library-based approach, be sure to include
   the source modules as well in your project. (They may be too large for
   16-bit memory models, that is, 16-bit DOS and Windows.)
   
   Here is a short example program. (For a more advanced example, see
   gddemo.c, included in the distribution. gddemo.c is NOT the same
   program; it demonstrates additional features!)
   
/* Bring in gd library functions */
#include "gd.h"

/* Bring in standard I/O so we can output the GIF to a file */
#include <stdio.h>

int main() {
        /* Declare the image */
        gdImagePtr im;
        /* Declare an output file */
        FILE *out;
        /* Declare color indexes */
        int black;
        int white;

        /* Allocate the image: 64 pixels across by 64 pixels tall */
        im = gdImageCreate(64, 64);

        /* Allocate the color black (red, green and blue all minimum).
                Since this is the first color in a new image, it will
                be the background color. */
        black = gdImageColorAllocate(im, 0, 0, 0);

        /* Allocate the color white (red, green and blue all maximum). */
        white = gdImageColorAllocate(im, 255, 255, 255);
        
        /* Draw a line from the upper left to the lower right,
                using white color index. */
        gdImageLine(im, 0, 0, 63, 63, white);

        /* Open a file for writing. "wb" means "write binary", important
                under MSDOS, harmless under Unix. */
        out = fopen("test.gif", "wb");

        /* Output the image to the disk file. */
        gdImageGif(im, out);

        /* Close the file. */
        fclose(out);

        /* Destroy the image in memory. */
        gdImageDestroy(im);
}

   When executed, this program creates an image, allocates two colors
   (the first color allocated becomes the background color), draws a
   diagonal line (note that 0, 0 is the upper left corner), writes the
   image to a GIF file, and destroys the image.
   
   The above example program should give you an idea of how the package
   works. gd provides many additional functions, which are listed in the
   following reference chapters, complete with code snippets
   demonstrating each. There is also an alphabetical index.
   
  Webgif: a more powerful gd example
  
   Webgif is a simple utility program to manipulate GIFs from the command
   line. It is written for Unix and similar command-line systems, but
   should be easily adapted for other environments. Webgif allows you to
   set transparency and interlacing and output interesting information
   about the GIF in question.
   
   webgif.c is provided in the distribution. Unix users can simply type
   "make webgif" to compile the program. Type "webgif" with no arguments
   to see the available options.
   
Function and type reference

     * Types
     * Image creation, destruction, loading and saving
     * Drawing, styling, brushing, tiling and filling functions
     * Query functions (not color-related)
     * Font and text-handling functions
     * Color handling functions
     * Copying and resizing functions
     * Miscellaneous Functions
     * Constants
       
  Types
  
   gdImage(TYPE)
          The data structure in which gd stores images. gdImageCreate
          returns a pointer to this type, and the other functions expect
          to receive a pointer to this type as their first argument. You
          may read the members sx (size on X axis), sy (size on Y axis),
          colorsTotal (total colors), red (red component of colors; an
          array of 256 integers between 0 and 255), green (green
          component of colors, as above), blue (blue component of colors,
          as above), and transparent (index of transparent color, -1 if
          none); please do so using the macros provided. Do NOT set the
          members directly from your code; use the functions provided.
          

typedef struct {
        unsigned char ** pixels;
        int sx;
        int sy;
        int colorsTotal;
        int red[gdMaxColors];
        int green[gdMaxColors];
        int blue[gdMaxColors];
        int open[gdMaxColors];
        int transparent;
} gdImage;

   gdImagePtr (TYPE)
          A pointer to an image structure. gdImageCreate returns this
          type, and the other functions expect it as the first argument.
          
   gdFont (TYPE)
          A font structure. Used to declare the characteristics of a
          font. Plese see the files gdfontl.c and gdfontl.h for an
          example of the proper declaration of this structure. You can
          provide your own font data by providing such a structure and
          the associated pixel array. You can determine the width and
          height of a single character in a font by examining the w and h
          members of the structure. If you will not be creating your own
          fonts, you will not need to concern yourself with the rest of
          the components of this structure.
          

typedef struct {
        /* # of characters in font */
        int nchars;
        /* First character is numbered... (usually 32 = space) */
        int offset;
        /* Character width and height */
        int w;
        int h;
        /* Font data; array of characters, one row after another.
                Easily included in code, also easily loaded from
                data files. */
        char *data;
} gdFont;

   gdFontPtr (TYPE)
          A pointer to a font structure. Text-output functions expect
          these as their second argument, following the gdImagePtr
          argument. Two such pointers are declared in the provided
          include files gdfonts.h and gdfontl.h.
          
   gdPoint (TYPE)
          Represents a point in the coordinate space of the image; used
          by gdImagePolygon and gdImageFilledPolygon.
          

typedef struct {
        int x, y;
} gdPoint, *gdPointPtr;

   gdPointPtr (TYPE)
          A pointer to a gdPoint structure; passed as an argument to
          gdImagePolygon and gdImageFilledPolygon.
          
  Image creation, destruction, loading and saving
  
   gdImageCreate(sx, sy) (FUNCTION)
          gdImageCreate is called to create images. Invoke gdImageCreate
          with the x and y dimensions of the desired image. gdImageCreate
          returns a gdImagePtr to the new image, or NULL if unable to
          allocate the image. The image must eventually be destroyed
          using gdImageDestroy().
          

... inside a function ...
gdImagePtr im;
im = gdImageCreate(64, 64);
/* ... Use the image ... */
gdImageDestroy(im);

   gdImageCreateFromGif(FILE *in) (FUNCTION)
          gdImageCreateFromGif is called to load images from GIF format
          files. Invoke gdImageCreateFromGif with an already opened
          pointer to a file containing the desired image.
          gdImageCreateFromGif returns a gdImagePtr to the new image, or
          NULL if unable to load the image (most often because the file
          is corrupt or does not contain a GIF image).
          gdImageCreateFromGif does not close the file. You can inspect
          the sx and sy members of the image to determine its size. The
          image must eventually be destroyed using gdImageDestroy().
          

gdImagePtr im;
... inside a function ...
FILE *in;
in = fopen("mygif.gif", "rb");
im = gdImageCreateFromGif(in);
fclose(in);
/* ... Use the image ... */
gdImageDestroy(im);

   gdImageCreateFromGd(FILE *in) (FUNCTION)
          gdImageCreateFromGd is called to load images from gd format
          files. Invoke gdImageCreateFromGd with an already opened
          pointer to a file containing the desired image in the gd file
          format, which is specific to gd and intended for very fast
          loading. (It is not intended for compression; for compression,
          use GIF.) gdImageCreateFromGd returns a gdImagePtr to the new
          image, or NULL if unable to load the image (most often because
          the file is corrupt or does not contain a gd format image).
          gdImageCreateFromGd does not close the file. You can inspect
          the sx and sy members of the image to determine its size. The
          image must eventually be destroyed using gdImageDestroy().
          

... inside a function ...
gdImagePtr im;
FILE *in;
in = fopen("mygd.gd", "rb");
im = gdImageCreateFromGd(in);
fclose(in);
/* ... Use the image ... */
gdImageDestroy(im);

   gdImageCreateFromXbm(FILE *in) (FUNCTION)
          gdImageCreateFromXbm is called to load images from X bitmap
          format files. Invoke gdImageCreateFromXbm with an already
          opened pointer to a file containing the desired image.
          gdImageCreateFromXbm returns a gdImagePtr to the new image, or
          NULL if unable to load the image (most often because the file
          is corrupt or does not contain an X bitmap format image).
          gdImageCreateFromXbm does not close the file. You can inspect
          the sx and sy members of the image to determine its size. The
          image must eventually be destroyed using gdImageDestroy().
          

... inside a function ...
gdImagePtr im;
FILE *in;
in = fopen("myxbm.xbm", "rb");
im = gdImageCreateFromXbm(in);
fclose(in);
/* ... Use the image ... */
gdImageDestroy(im);

   gdImageDestroy(gdImagePtr im) (FUNCTION)
          gdImageDestroy is used to free the memory associated with an
          image. It is important to invoke gdImageDestroy before exiting
          your program or assigning a new image to a gdImagePtr variable.
          

... inside a function ...
gdImagePtr im;
im = gdImageCreate(10, 10);
/* ... Use the image ... */
/* Now destroy it */
gdImageDestroy(im);

   void gdImageGif(gdImagePtr im, FILE *out) (FUNCTION)
          gdImageGif outputs the specified image to the specified file in
          GIF format. The file must be open for writing. Under MSDOS, it
          is important to use "wb" as opposed to simply "w" as the mode
          when opening the file, and under Unix there is no penalty for
          doing so. gdImageGif does not close the file; your code must do
          so.
          

... inside a function ...
gdImagePtr im;
int black, white;
FILE *out;
/* Create the image */
im = gdImageCreate(100, 100);
/* Allocate background */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Allocate drawing color */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Draw rectangle */
gdImageRectangle(im, 0, 0, 99, 99, black);
/* Open output file in binary mode */
out = fopen("rect.gif", "wb");
/* Write GIF */
gdImageGif(im, out);
/* Close file */
fclose(out);
/* Destroy image */
gdImageDestroy(im);

   void gdImageGd(gdImagePtr im, FILE *out) (FUNCTION)
          gdImageGd outputs the specified image to the specified file in
          the gd image format. The file must be open for writing. Under
          MSDOS, it is important to use "wb" as opposed to simply "w" as
          the mode when opening the file, and under Unix there is no
          penalty for doing so. gdImageGif does not close the file; your
          code must do so.
          
          The gd image format is intended for fast reads and writes of
          images your program will need frequently to build other images.
          It is not a compressed format, and is not intended for general
          use.
          

... inside a function ...
gdImagePtr im;
int black, white;
FILE *out;
/* Create the image */
im = gdImageCreate(100, 100);
/* Allocate background */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Allocate drawing color */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Draw rectangle */
gdImageRectangle(im, 0, 0, 99, 99, black);
/* Open output file in binary mode */
out = fopen("rect.gd", "wb");
/* Write gd format file */
gdImageGd(im, out);
/* Close file */
fclose(out);
/* Destroy image */
gdImageDestroy(im);

  Drawing Functions
  
   void gdImageSetPixel(gdImagePtr im, int x, int y, int color)
          (FUNCTION)
          gdImageSetPixel sets a pixel to a particular color index.
          Always use this function or one of the other drawing functions
          to access pixels; do not access the pixels of the gdImage
          structure directly.
          

... inside a function ...
gdImagePtr im;
int black;
int white;
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Set a pixel near the center. */
gdImageSetPixel(im, 50, 50, white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImageLine(gdImagePtr im, int x1, int y1, int x2, int y2, int
          color) (FUNCTION)
          gdImageLine is used to draw a line between two endpoints (x1,y1
          and x2, y2). The line is drawn using the color index specified.
          Note that the color index can be an actual color returned by
          gdImageColorAllocate or one of gdStyled, gdBrushed or
          gdStyledBrushed.
          

... inside a function ...
gdImagePtr im;
int black;
int white;
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Draw a line from the upper left corner to the lower right corner. */
gdImageLine(im, 0, 0, 99, 99, white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImageDashedLine(gdImagePtr im, int x1, int y1, int x2, int y2,
          int color) (FUNCTION)
          gdImageDashedLine is provided solely for backwards
          compatibility with gd 1.0. New programs should draw dashed
          lines using the normal gdImageLine function and the new
          gdImageSetStyle function.
          
          gdImageDashedLine is used to draw a dashed line between two
          endpoints (x1,y1 and x2, y2). The line is drawn using the color
          index specified. The portions of the line that are not drawn
          are left transparent so the background is visible.
          

... inside a function ...
gdImagePtr im;
int black;
int white;
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Draw a dashed line from the upper left corner to the lower right corner. */
gdImageDashedLine(im, 0, 0, 99, 99);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImagePolygon(gdImagePtr im, gdPointPtr points, int pointsTotal,
          int color) (FUNCTION)
          gdImagePolygon is used to draw a polygon with the verticies (at
          least 3) specified, using the color index specified. See also
          gdImageFilledPolygon.
          

... inside a function ...
gdImagePtr im;
int black;
int white;
/* Points of polygon */
gdPoint points[3];
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Draw a triangle. */
points[0].x = 50;
points[0].y = 0;
points[1].x = 99;
points[1].y = 99;
points[2].x = 0;
points[2].y = 99;
gdImagePolygon(im, points, 3, white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImageRectangle(gdImagePtr im, int x1, int y1, int x2, int y2,
          int color) (FUNCTION)
          gdImageRectangle is used to draw a rectangle with the two
          corners (upper left first, then lower right) specified, using
          the color index specified.
          

... inside a function ...
gdImagePtr im;
int black;
int white;
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Draw a rectangle occupying the central area. */
gdImageRectangle(im, 25, 25, 74, 74, white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImageFilledPolygon(gdImagePtr im, gdPointPtr points, int
          pointsTotal, int color) (FUNCTION)
          gdImageFilledPolygon is used to fill a polygon with the
          verticies (at least 3) specified, using the color index
          specified. See also gdImagePolygon.
          

... inside a function ...
gdImagePtr im;
int black;
int white;
int red;
/* Points of polygon */
gdPoint points[3];
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Allocate the color red. */
red = gdImageColorAllocate(im, 255, 0, 0);
/* Draw a triangle. */
points[0].x = 50;
points[0].y = 0;
points[1].x = 99;
points[1].y = 99;
points[2].x = 0;
points[2].y = 99;
/* Paint it in white */
gdImageFilledPolygon(im, points, 3, white);
/* Outline it in red; must be done second */
gdImagePolygon(im, points, 3, red);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImageFilledRectangle(gdImagePtr im, int x1, int y1, int x2, int
          y2, int color) (FUNCTION)
          gdImageFilledRectangle is used to draw a solid rectangle with
          the two corners (upper left first, then lower right) specified,
          using the color index specified.
          

... inside a function ...
gdImagePtr im;
int black;
int white;
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = int gdImageColorAllocate(im, 255, 255, 255);
/* Draw a filled rectangle occupying the central area. */
gdImageFilledRectangle(im, 25, 25, 74, 74, white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImageArc(gdImagePtr im, int cx, int cy, int w, int h, int s,
          int e, int color) (FUNCTION)
          gdImageArc is used to draw a partial ellipse centered at the
          given point, with the specified width and height in pixels. The
          arc begins at the position in degrees specified by s and ends
          at the position specified by e. The arc is drawn in the color
          specified by the last argument. A circle can be drawn by
          beginning from 0 degrees and ending at 360 degrees, with width
          and height being equal. e must be greater than s. Values
          greater than 360 are interpreted modulo 360.
          

... inside a function ...
gdImagePtr im;
int black;
int white;
im = gdImageCreate(100, 50);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Inscribe an ellipse in the image. */
gdImageArc(im, 50, 25, 98, 48, 0, 360, white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImageFillToBorder(gdImagePtr im, int x, int y, int border, int
          color) (FUNCTION)
          gdImageFillToBorder floods a portion of the image with the
          specified color, beginning at the specified point and stopping
          at the specified border color. For a way of flooding an area
          defined by the color of the starting point, see gdImageFill.
          
          The border color cannot be a special color such as gdTiled; it
          must be a proper solid color. The fill color can be, however.
          
          Note that gdImageFillToBorder is recursive. It is not the most
          naive implementation possible, and the implementation is
          expected to improve, but there will always be degenerate cases
          in which the stack can become very deep. This can be a problem
          in MSDOS and MS Windows environments. (Of course, in a Unix or
          NT environment with a proper stack, this is not a problem at
          all.)
          

... inside a function ...
gdImagePtr im;
int black;
int white;
int red;
im = gdImageCreate(100, 50);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Allocate the color red. */
red = gdImageColorAllocate(im, 255, 0, 0);
/* Inscribe an ellipse in the image. */
gdImageArc(im, 50, 25, 98, 48, 0, 360, white);
/* Flood-fill the ellipse. Fill color is red, border color is
        white (ellipse). */
gdImageFillToBorder(im, 50, 50, white, red);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImageFill(gdImagePtr im, int x, int y, int color) (FUNCTION)
          gdImageFill floods a portion of the image with the specified
          color, beginning at the specified point and flooding the
          surrounding region of the same color as the starting point. For
          a way of flooding a region defined by a specific border color
          rather than by its interior color, see gdImageFillToBorder.
          
          The fill color can be gdTiled, resulting in a tile fill using
          another image as the tile. However, the tile image cannot be
          transparent. If the image you wish to fill with has a
          transparent color index, call gdImageTransparent on the tile
          image and set the transparent color index to -1 to turn off its
          transparency.
          
          Note that gdImageFill is recursive. It is not the most naive
          implementation possible, and the implementation is expected to
          improve, but there will always be degenerate cases in which the
          stack can become very deep. This can be a problem in MSDOS and
          MS Windows environments. (Of course, in a Unix or NT
          environment with a proper stack, this is not a problem at all.)
          

... inside a function ...
gdImagePtr im;
int black;
int white;
int red;
im = gdImageCreate(100, 50);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Allocate the color red. */
red = gdImageColorAllocate(im, 255, 0, 0);
/* Inscribe an ellipse in the image. */
gdImageArc(im, 50, 25, 98, 48, 0, 360, white);
/* Flood-fill the ellipse. Fill color is red, and will replace the
        black interior of the ellipse. */
gdImageFill(im, 50, 50, red);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImageSetBrush(gdImagePtr im, gdImagePtr brush) (FUNCTION)
          A "brush" is an image used to draw wide, shaped strokes in
          another image. Just as a paintbrush is not a single point, a
          brush image need not be a single pixel. Any gd image can be
          used as a brush, and by setting the transparent color index of
          the brush image with gdImageColorTransparent, a brush of any
          shape can be created. All line-drawing functions, such as
          gdImageLine and gdImagePolygon, will use the current brush if
          the special "color" gdBrushed or gdStyledBrushed is used when
          calling them.
          
          gdImageSetBrush is used to specify the brush to be used in a
          particular image. You can set any image to be the brush. If the
          brush image does not have the same color map as the first
          image, any colors missing from the first image will be
          allocated. If not enough colors can be allocated, the closest
          colors already available will be used. This allows arbitrary
          GIFs to be used as brush images. It also means, however, that
          you should not set a brush unless you will actually use it; if
          you set a rapid succession of different brush images, you can
          quickly fill your color map, and the results will not be
          optimal.
          
          You need not take any special action when you are finished with
          a brush. As for any other image, if you will not be using the
          brush image for any further purpose, you should call
          gdImageDestroy. You must not use the color gdBrushed if the
          current brush has been destroyed; you can of course set a new
          brush to replace it.
          

... inside a function ...
gdImagePtr im, brush;
FILE *in;
int black;
im = gdImageCreate(100, 100);
/* Open the brush GIF. For best results, portions of the
        brush that should be transparent (ie, not part of the
        brush shape) should have the transparent color index. */
in = fopen("star.gif", "rb");
brush = gdImageCreateFromGif(in);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
gdImageSetBrush(im, brush);
/* Draw a line from the upper left corner to the lower right corner
        using the brush. */
gdImageLine(im, 0, 0, 99, 99, gdBrushed);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);
/* Destroy the brush image */
gdImageDestroy(brush);

   void gdImageSetTile(gdImagePtr im, gdImagePtr tile) (FUNCTION)
          A "tile" is an image used to fill an area with a repeated
          pattern. Any gd image can be used as a tile, and by setting the
          transparent color index of the tile image with
          gdImageColorTransparent, a tile that allows certain parts of
          the underlying area to shine through can be created. All
          region-filling functions, such as gdImageFill and
          gdImageFilledPolygon, will use the current tile if the special
          "color" gdTiled is used when calling them.
          
          gdImageSetTile is used to specify the tile to be used in a
          particular image. You can set any image to be the tile. If the
          tile image does not have the same color map as the first image,
          any colors missing from the first image will be allocated. If
          not enough colors can be allocated, the closest colors already
          available will be used. This allows arbitrary GIFs to be used
          as tile images. It also means, however, that you should not set
          a tile unless you will actually use it; if you set a rapid
          succession of different tile images, you can quickly fill your
          color map, and the results will not be optimal.
          
          You need not take any special action when you are finished with
          a tile. As for any other image, if you will not be using the
          tile image for any further purpose, you should call
          gdImageDestroy. You must not use the color gdTiled if the
          current tile has been destroyed; you can of course set a new
          tile to replace it.
          

... inside a function ...
gdImagePtr im, tile;
FILE *in;
int black;
im = gdImageCreate(100, 100);
/* Open the tile GIF. For best results, portions of the
        tile that should be transparent (ie, allowing the
        background to shine through) should have the transparent
        color index. */
in = fopen("star.gif", "rb");
tile = gdImageCreateFromGif(in);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
gdImageSetTile(im, tile);
/* Fill an area using the tile. */
gdImageFilledRectangle(im, 25, 25, 75, 75, gdTiled);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);
/* Destroy the tile image */
gdImageDestroy(tile);

   void gdImageSetStyle(gdImagePtr im, int *style, int styleLength)
          (FUNCTION)
          It is often desirable to draw dashed lines, dotted lines, and
          other variations on a broken line. gdImageSetStyle can be used
          to set any desired series of colors, including a special color
          that leaves the background intact, to be repeated during the
          drawing of a line.
          
          To use gdImageSetStyle, create an array of integers and assign
          them the desired series of color values to be repeated. You can
          assign the special color value gdTransparent to indicate that
          the existing color should be left unchanged for that particular
          pixel (allowing a dashed line to be attractively drawn over an
          existing image).
          
          Then, to draw a line using the style, use the normal
          gdImageLine function with the special color value gdStyled.
          
          As of version 1.1.1, the style array is copied when you set the
          style, so you need not be concerned with keeping the array
          around indefinitely. This should not break existing code that
          assumes styles are not copied.
          
          You can also combine styles and brushes to draw the brush image
          at intervals instead of in a continuous stroke. When creating a
          style for use with a brush, the style values are interpreted
          differently: zero (0) indicates pixels at which the brush
          should not be drawn, while one (1) indicates pixels at which
          the brush should be drawn. To draw a styled, brushed line, you
          must use the special color value gdStyledBrushed. For an
          example of this feature in use, see gddemo.c (provided in the
          distribution).
          

gdImagePtr im;
int styleDotted[2], styleDashed[6];
FILE *in;
int black;
int red;
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
red = gdImageColorAllocate(im, 255, 0, 0);
/* Set up dotted style. Leave every other pixel alone. */
styleDotted[0] = red;
styleDotted[1] = gdTransparent;
/* Set up dashed style. Three on, three off. */
styleDashed[0] = red;
styleDashed[1] = red;
styleDashed[2] = red;
styleDashed[3] = gdTransparent;
styleDashed[4] = gdTransparent;
styleDashed[5] = gdTransparent;
/* Set dotted style. Note that we have to specify how many pixels are
        in the style! */
gdImageSetStyle(im, styleDotted, 2);
/* Draw a line from the upper left corner to the lower right corner. */
gdImageLine(im, 0, 0, 99, 99, gdStyled);
/* Now the dashed line. */
gdImageSetStyle(im, styleDashed, 6);
gdImageLine(im, 0, 99, 0, 99, gdStyled);

/* ... Do something with the image, such as saving it to a file ... */

/* Destroy it */
gdImageDestroy(im);

  Query Functions
  
        int gdImageBlue(gdImagePtr im, int color) (MACRO)
                gdImageBlue is a macro which returns the blue component
                of the specified color index. Use this macro rather than
                accessing the structure members directly.
                
        int gdImageGetPixel(gdImagePtr im, int x, int y) (FUNCTION)
                gdImageGetPixel() retrieves the color index of a
                particular pixel. Always use this function to query
                pixels; do not access the pixels of the gdImage structure
                directly.
                

... inside a function ...
FILE *in;
gdImagePtr im;
int c;
in = fopen("mygif.gif", "rb");
im = gdImageCreateFromGif(in);
fclose(in);
c = gdImageGetPixel(im, gdImageSX(im) / 2, gdImageSY(im) / 2);
printf("The value of the center pixel is %d; RGB values are %d,%d,%d\n",
        c, im->red[c], im->green[c], im->blue[c]);
gdImageDestroy(im);

        int gdImageBoundsSafe(gdImagePtr im, int x, int y) (FUNCTION)
                gdImageBoundsSafe returns true (1) if the specified point
                is within the bounds of the image, false (0) if not. This
                function is intended primarily for use by those who wish
                to add functions to gd. All of the gd drawing functions
                already clip safely to the edges of the image.
                

... inside a function ...
gdImagePtr im;
int black;
int white;
im = gdImageCreate(100, 100);
if (gdImageBoundsSafe(im, 50, 50)) {
        printf("50, 50 is within the image bounds\n");
} else {
        printf("50, 50 is outside the image bounds\n");
}
gdImageDestroy(im);

        int gdImageGreen(gdImagePtr im, int color) (MACRO)
                gdImageGreen is a macro which returns the green component
                of the specified color index. Use this macro rather than
                accessing the structure members directly.
                
        int gdImageRed(gdImagePtr im, int color) (MACRO)
                gdImageRed is a macro which returns the red component of
                the specified color index. Use this macro rather than
                accessing the structure members directly.
                
        int gdImageSX(gdImagePtr im) (MACRO)
                gdImageSX is a macro which returns the width of the image
                in pixels. Use this macro rather than accessing the
                structure members directly.
                
        int gdImageSY(gdImagePtr im) (MACRO)
                gdImageSY is a macro which returns the height of the
                image in pixels. Use this macro rather than accessing the
                structure members directly.
                
  Fonts and text-handling functions
  
        void gdImageChar(gdImagePtr im, gdFontPtr font, int x, int y, int
                c, int color) (FUNCTION)
                gdImageChar is used to draw single characters on the
                image. (To draw multiple characters, use gdImageString or
                gdImageString16.) The second argument is a pointer to a
                font definition structure; five fonts are provided with
                gd, gdFontTiny, gdFontSmall, gdFontMediumBold,
                gdFontLarge, and gdFontGiant. You must include the files
                "gdfontt.h", "gdfonts.h", "gdfontmb.h", "gdfontl.h" and
                "gdfontg.h" respectively and (if you are not using a
                library-based approach) link with the corresponding .c
                files to use the provided fonts. The character specified
                by the fifth argument is drawn from left to right in the
                specified color. (See gdImageCharUp for a way of drawing
                vertical text.) Pixels not set by a particular character
                retain their previous color.
                

#include "gd.h"
#include "gdfontl.h"
... inside a function ...
gdImagePtr im;
int black;
int white;
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Draw a character. */
gdImageChar(im, gdFontLarge, 0, 0, 'Q', white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

        void gdImageCharUp(gdImagePtr im, gdFontPtr font, int x, int y,
                int c, int color) (FUNCTION)
                gdImageCharUp is used to draw single characters on the
                image, rotated 90 degrees. (To draw multiple characters,
                use gdImageStringUp or gdImageStringUp16.) The second
                argument is a pointer to a font definition structure;
                five fonts are provided with gd, gdFontTiny, gdFontSmall,
                gdFontMediumBold, gdFontLarge, and gdFontGiant. You must
                include the files "gdfontt.h", "gdfonts.h", "gdfontmb.h",
                "gdfontl.h" and "gdfontg.h" respectively and (if you are
                not using a library-based approach) link with the
                corresponding .c files to use the provided fonts. The
                character specified by the fifth argument is drawn from
                bottom to top, rotated at a 90-degree angle, in the
                specified color. (See gdImageChar for a way of drawing
                horizontal text.) Pixels not set by a particular
                character retain their previous color.
                

#include "gd.h"
#include "gdfontl.h"
... inside a function ...
gdImagePtr im;
int black;
int white;
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Draw a character upwards so it rests against the top of the image. */
gdImageCharUp(im, gdFontLarge,
        0, gdFontLarge->h, 'Q', white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

        void gdImageString(gdImagePtr im, gdFontPtr font, int x, int y,
                unsigned char *s, int color) (FUNCTION)
                gdImageString is used to draw multiple characters on the
                image. (To draw single characters, use gdImageChar.) The
                second argument is a pointer to a font definition
                structure; five fonts are provided with gd, gdFontTiny,
                gdFontSmall, gdFontMediumBold, gdFontLarge, and
                gdFontGiant. You must include the files "gdfontt.h",
                "gdfonts.h", "gdfontmb.h", "gdfontl.h" and "gdfontg.h"
                respectively and (if you are not using a library-based
                approach) link with the corresponding .c files to use the
                provided fonts. The null-terminated C string specified by
                the fifth argument is drawn from left to right in the
                specified color. (See gdImageStringUp for a way of
                drawing vertical text.) Pixels not set by a particular
                character retain their previous color.
                

#include "gd.h"
#include "gdfontl.h"
#include <string.h>
... inside a function ...
gdImagePtr im;
int black;
int white;
/* String to draw. */
char *s = "Hello.";
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Draw a centered string. */
gdImageString(im, gdFontLarge,
        im->w / 2 - (strlen(s) * gdFontLarge->w / 2),
        im->h / 2 - gdFontLarge->h / 2,
        s, white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

        void gdImageString16(gdImagePtr im, gdFontPtr font, int x, int y,
                unsigned short *s, int color) (FUNCTION)
                gdImageString is used to draw multiple 16-bit characters
                on the image. (To draw single characters, use
                gdImageChar.) The second argument is a pointer to a font
                definition structure; five fonts are provided with gd,
                gdFontTiny, gdFontSmall, gdFontMediumBold, gdFontLarge,
                and gdFontGiant. You must include the files "gdfontt.h",
                "gdfonts.h", "gdfontmb.h", "gdfontl.h" and "gdfontg.h"
                respectively and (if you are not using a library-based
                approach) link with the corresponding .c files to use the
                provided fonts. The null-terminated string of characters
                represented as 16-bit unsigned short integers specified
                by the fifth argument is drawn from left to right in the
                specified color. (See gdImageStringUp16 for a way of
                drawing vertical text.) Pixels not set by a particular
                character retain their previous color.
                
                This function was added in gd1.3 to provide a means of
                rendering fonts with more than 256 characters for those
                who have them. A more frequently used routine is
                gdImageString.
                
        void gdImageStringUp(gdImagePtr im, gdFontPtr font, int x, int y,
                unsigned char *s, int color) (FUNCTION)
                gdImageStringUp is used to draw multiple characters on
                the image, rotated 90 degrees. (To draw single
                characters, use gdImageCharUp.) The second argument is a
                pointer to a font definition structure; five fonts are
                provided with gd, gdFontTiny, gdFontSmall,
                gdFontMediumBold, gdFontLarge, and gdFontGiant. You must
                include the files "gdfontt.h", "gdfonts.h", "gdfontmb.h",
                "gdfontl.h" and "gdfontg.h" respectively and (if you are
                not using a library-based approach) link with the
                corresponding .c files to use the provided fonts.The
                null-terminated C string specified by the fifth argument
                is drawn from bottom to top (rotated 90 degrees) in the
                specified color. (See gdImageString for a way of drawing
                horizontal text.) Pixels not set by a particular
                character retain their previous color.
                

#include "gd.h"
#include "gdfontl.h"
#include <string.h>
... inside a function ...
gdImagePtr im;
int black;
int white;
/* String to draw. */
char *s = "Hello.";
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Draw a centered string going upwards. Axes are reversed,
        and Y axis is decreasing as the string is drawn. */
gdImageStringUp(im, gdFontLarge,
        im->w / 2 - gdFontLarge->h / 2,
        im->h / 2 + (strlen(s) * gdFontLarge->w / 2),
        s, white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

        void gdImageStringUp16(gdImagePtr im, gdFontPtr font, int x, int
                y, unsigned short *s, int color) (FUNCTION)
                gdImageString is used to draw multiple 16-bit characters
                vertically on the image. (To draw single characters, use
                gdImageChar.) The second argument is a pointer to a font
                definition structure; five fonts are provided with gd,
                gdFontTiny, gdFontSmall, gdFontMediumBold, gdFontLarge,
                and gdFontGiant. You must include the files "gdfontt.h",
                "gdfonts.h", "gdfontmb.h", "gdfontl.h" and "gdfontg.h"
                respectively and (if you are not using a library-based
                approach) link with the corresponding .c files to use the
                provided fonts. The null-terminated string of characters
                represented as 16-bit unsigned short integers specified
                by the fifth argument is drawn from bottom to top in the
                specified color. (See gdImageStringUp16 for a way of
                drawing horizontal text.) Pixels not set by a particular
                character retain their previous color.
                
                This function was added in gd1.3 to provide a means of
                rendering fonts with more than 256 characters for those
                who have them. A more frequently used routine is
                gdImageStringUp.
                
  Color-handling functions
  
        int gdImageColorAllocate(gdImagePtr im, int r, int g, int b)
                (FUNCTION)
                gdImageColorAllocate finds the first available color
                index in the image specified, sets its RGB values to
                those requested (255 is the maximum for each), and
                returns the index of the new color table entry. When
                creating a new image, the first time you invoke this
                function, you are setting the background color for that
                image.
                
                In the event that all gdMaxColors colors (256) have
                already been allocated, gdImageColorAllocate will return
                -1 to indicate failure. (This is not uncommon when
                working with existing GIF files that already use 256
                colors.) Note that gdImageColorAllocate does not check
                for existing colors that match your request; see
                gdImageColorExact and gdImageColorClosest for ways to
                locate existing colors that approximate the color desired
                in situations where a new color is not available.
                

... inside a function ...
gdImagePtr im;
int black;
int red;
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color red. */
red = gdImageColorAllocate(im, 255, 0, 0);
/* Draw a dashed line from the upper left corner to the lower right corner. */
gdImageDashedLine(im, 0, 0, 99, 99, red);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

        int gdImageColorClosest(gdImagePtr im, int r, int g, int b)
                (FUNCTION)
                gdImageColorClosest searches the colors which have been
                defined thus far in the image specified and returns the
                index of the color with RGB values closest to those of
                the request. (Closeness is determined by Euclidian
                distance, which is used to determine the distance in
                three-dimensional color space between colors.)
                
                If no colors have yet been allocated in the image,
                gdImageColorClosest returns -1.
                
                This function is most useful as a backup method for
                choosing a drawing color when an image already contains
                gdMaxColors (256) colors and no more can be allocated.
                (This is not uncommon when working with existing GIF
                files that already use many colors.) See
                gdImageColorExact for a method of locating exact matches
                only.
                

... inside a function ...
gdImagePtr im;
FILE *in;
int red;
/* Let's suppose that photo.gif is a scanned photograph with
        many colors. */
in = fopen("photo.gif", "rb");
im = gdImageCreateFromGif(in);
fclose(in);
/* Try to allocate red directly */
red = gdImageColorAllocate(im, 255, 0, 0);
/* If we fail to allocate red... */
if (red == (-1)) {
        /* Find the closest color instead. */
        red = gdImageColorClosest(im, 255, 0, 0);
}
/* Draw a dashed line from the upper left corner to the lower right corner */
gdImageDashedLine(im, 0, 0, 99, 99, red);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

        int gdImageColorExact(gdImagePtr im, int r, int g, int b)
                (FUNCTION)
                gdImageColorExact searches the colors which have been
                defined thus far in the image specified and returns the
                index of the first color with RGB values which exactly
                match those of the request. If no allocated color matches
                the request precisely, gdImageColorExact returns -1. See
                gdImageColorClosest for a way to find the color closest
                to the color requested.
                

... inside a function ...
gdImagePtr im;
int red;
in = fopen("photo.gif", "rb");
im = gdImageCreateFromGif(in);
fclose(in);
/* The image may already contain red; if it does, we'll save a slot
        in the color table by using that color. */
/* Try to allocate red directly */
red = gdImageColorExact(im, 255, 0, 0);
/* If red isn't already present... */
if (red == (-1)) {
        /* Second best: try to allocate it directly. */
        red = gdImageColorAllocate(im, 255, 0, 0);
        /* Out of colors, so find the closest color instead. */
        red = gdImageColorClosest(im, 255, 0, 0);
}
/* Draw a dashed line from the upper left corner to the lower right corner */
gdImageDashedLine(im, 0, 0, 99, 99, red);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

        int gdImageColorsTotal(gdImagePtr im) (MACRO)
                gdImageColorsTotal is a macro which returns the number of
                colors currently allocated in the image. Use this macro
                to obtain this information; do not access the structure
                directly.
                
        int gdImageColorRed(gdImagePtr im, int c) (MACRO)
                gdImageColorRed is a macro which returns the red portion
                of the specified color in the image. Use this macro to
                obtain this information; do not access the structure
                directly.
                
        int gdImageColorGreen(gdImagePtr im, int c) (MACRO)
                gdImageColorGreen is a macro which returns the green
                portion of the specified color in the image. Use this
                macro to obtain this information; do not access the
                structure directly.
                
        int gdImageColorBlue(gdImagePtr im, int c) (MACRO)
                gdImageColorBlue is a macro which returns the green
                portion of the specified color in the image. Use this
                macro to obtain this information; do not access the
                structure directly.
                
        int gdImageGetInterlaced(gdImagePtr im) (MACRO)
                gdImageGetInterlaced is a macro which returns true (1) if
                the image is interlaced, false (0) if not. Use this macro
                to obtain this information; do not access the structure
                directly. See gdImageInterlace for a means of interlacing
                images.
                
        int gdImageGetTransparent(gdImagePtr im) (MACRO)
                gdImageGetTransparent is a macro which returns the
                current transparent color index in the image. If there is
                no transparent color, gdImageGetTransparent returns -1.
                Use this macro to obtain this information; do not access
                the structure directly.
                
        void gdImageColorDeallocate(gdImagePtr im, int color) (FUNCTION)
                gdImageColorDeallocate marks the specified color as being
                available for reuse. It does not attempt to determine
                whether the color index is still in use in the image.
                After a call to this function, the next call to
                gdImageColorAllocate for the same image will set new RGB
                values for that color index, changing the color of any
                pixels which have that index as a result. If multiple
                calls to gdImageColorDeallocate are made consecutively,
                the lowest-numbered index among them will be reused by
                the next gdImageColorAllocate call.
                

... inside a function ...
gdImagePtr im;
int red, blue;
in = fopen("photo.gif", "rb");
im = gdImageCreateFromGif(in);
fclose(in);
/* Look for red in the color table. */
red = gdImageColorExact(im, 255, 0, 0);
/* If red is present... */
if (red != (-1)) {
        /* Deallocate it. */
        gdImageColorDeallocate(im, red);
        /* Allocate blue, reusing slot in table.
                Existing red pixels will change color. */
        blue = gdImageColorAllocate(im, 0, 0, 255);
}
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

        void gdImageColorTransparent(gdImagePtr im, int color) (FUNCTION)
                
                gdImageColorTransparent sets the transparent color index
                for the specified image to the specified index. To
                indicate that there should be no transparent color,
                invoke gdImageColorTransparent with a color index of -1.
                
                The color index used should be an index allocated by
                gdImageColorAllocate, whether explicitly invoked by your
                code or implicitly invoked by loading an image. In order
                to ensure that your image has a reasonable appearance
                when viewed by users who do not have transparent
                background capabilities, be sure to give reasonable RGB
                values to the color you allocate for use as a transparent
                color, even though it will be transparent on systems that
                support transparency.
                

... inside a function ...
gdImagePtr im;
int black;
FILE *in, *out;
in = fopen("photo.gif", "rb");
im = gdImageCreateFromGif(in);
fclose(in);
/* Look for black in the color table and make it transparent. */
black = gdImageColorExact(im, 0, 0, 0);
/* If black is present... */
if (black != (-1)) {
        /* Make it transparent */
        gdImageColorTransparent(im, black);
}
/* Save the newly-transparent image back to the file */
out = fopen("photo.gif", "wb");
gdImageGif(im, out);
fclose(out);
/* Destroy it */
gdImageDestroy(im);

  Copying and resizing functions
  
        void gdImageCopy(gdImagePtr dst, gdImagePtr src, int dstX, int
                dstY, int srcX, int srcY, int w, int h) (FUNCTION)
                gdImageCopy is used to copy a rectangular portion of one
                image to another image. (For a way of stretching or
                shrinking the image in the process, see
                gdImageCopyResized.)
                
                The dst argument is the destination image to which the
                region will be copied. The src argument is the source
                image from which the region is copied. The dstX and dstY
                arguments specify the point in the destination image to
                which the region will be copied. The srcX and srcY
                arguments specify the upper left corner of the region in
                the source image. The w and h arguments specify the width
                and height of the region.
                
                When you copy a region from one location in an image to
                another location in the same image, gdImageCopy will
                perform as expected unless the regions overlap, in which
                case the result is unpredictable.
                
                Important note on copying between images: since different
                images do not necessarily have the same color tables,
                pixels are not simply set to the same color index values
                to copy them. gdImageCopy will attempt to find an
                identical RGB value in the destination image for each
                pixel in the copied portion of the source image by
                invoking gdImageColorExact. If such a value is not found,
                gdImageCopy will attempt to allocate colors as needed
                using gdImageColorAllocate. If both of these methods
                fail, gdImageCopy will invoke gdImageColorClosest to find
                the color in the destination image which most closely
                approximates the color of the pixel being copied.
                

... Inside a function ...
gdImagePtr im_in;
gdImagePtr im_out;
int x, y;
FILE *in;
FILE *out;
/* Load a small gif to tile the larger one with */
in = fopen("small.gif", "rb");
im_in = gdImageCreateFromGif(in);
fclose(in);
/* Make the output image four times as large on both axes */
im_out = gdImageCreate(im_in->sx * 4, im_in->sy * 4);
/* Now tile the larger image using the smaller one */
for (y = 0; (y < 4); y++) {
        for (x = 0; (x < 4); x++) {
                gdImageCopy(im_out, im_in,
                        x * im_in->sx, y * im_in->sy,
                        0, 0,
                        im_in->sx, im_in->sy);
        }
}
out = fopen("tiled.gif", "wb");
gdImageGif(im_out, out);
fclose(out);
gdImageDestroy(im_in);
gdImageDestroy(im_out);

        void gdImageCopyResized(gdImagePtr dst, gdImagePtr src, int dstX,
                int dstY, int srcX, int srcY, int destW, int destH, int
                srcW, int srcH) (FUNCTION)
                gdImageCopyResized is used to copy a rectangular portion
                of one image to another image. The X and Y dimensions of
                the original region and the destination region can vary,
                resulting in stretching or shrinking of the region as
                appropriate. (For a simpler version of this function
                which does not deal with resizing, see gdImageCopy.)
                
                The dst argument is the destination image to which the
                region will be copied. The src argument is the source
                image from which the region is copied. The dstX and dstY
                arguments specify the point in the destination image to
                which the region will be copied. The srcX and srcY
                arguments specify the upper left corner of the region in
                the source image. The dstW and dstH arguments specify the
                width and height of the destination region. The srcW and
                srcH arguments specify the width and height of the source
                region and can differ from the destination size, allowing
                a region to be scaled during the copying process.
                
                When you copy a region from one location in an image to
                another location in the same image, gdImageCopy will
                perform as expected unless the regions overlap, in which
                case the result is unpredictable. If this presents a
                problem, create a scratch image in which to keep
                intermediate results.
                
                Important note on copying between images: since images do
                not necessarily have the same color tables, pixels are
                not simply set to the same color index values to copy
                them. gdImageCopy will attempt to find an identical RGB
                value in the destination image for each pixel in the
                copied portion of the source image by invoking
                gdImageColorExact. If such a value is not found,
                gdImageCopy will attempt to allocate colors as needed
                using gdImageColorAllocate. If both of these methods
                fail, gdImageCopy will invoke gdImageColorClosest to find
                the color in the destination image which most closely
                approximates the color of the pixel being copied.
                

... Inside a function ...
gdImagePtr im_in;
gdImagePtr im_out;
int x, y;
FILE *in;
FILE *out;
/* Load a small gif to expand in the larger one */
in = fopen("small.gif", "rb");
im_in = gdImageCreateFromGif(in);
fclose(in);
/* Make the output image four times as large on both axes */
im_out = gdImageCreate(im_in->sx * 4, im_in->sy * 4);
/* Now copy the smaller image, but four times larger */
gdImageCopyResized(im_out, im_in, 0, 0, 0, 0,
        im_out->sx, im_out->sy,
        im_in->sx, im_in->sy);
out = fopen("large.gif", "wb");
gdImageGif(im_out, out);
fclose(out);
gdImageDestroy(im_in);
gdImageDestroy(im_out);

  Miscellaneous Functions
  
              gdImageInterlace(gdImagePtr im, int interlace) (FUNCTION)
                      gdImageInterlace is used to determine whether an
                      image should be stored in a linear fashion, in
                      which lines will appear on the display from first
                      to last, or in an interlaced fashion, in which the
                      image will "fade in" over several passes. By
                      default, images are not interlaced.
                      
                      A nonzero value for the interlace argument turns on
                      interlace; a zero value turns it off. Note that
                      interlace has no effect on other functions, and has
                      no meaning unless you save the image in GIF format;
                      the gd and xbm formats do not support interlace.
                      
                      When a GIF is loaded with gdImageCreateFromGif ,
                      interlace will be set according to the setting in
                      the GIF file.
                      
                      Note that many GIF viewers and web browsers do not
                      support interlace. However, the interlaced GIF
                      should still display; it will simply appear all at
                      once, just as other images do.
                      

gdImagePtr im;
FILE *out;
/* ... Create or load the image... */

/* Now turn on interlace */
gdImageInterlace(im, 1);
/* And open an output file */
out = fopen("test.gif", "wb");
/* And save the image */
gdImageGif(im, out);
fclose(out);
gdImageDestroy(im);

  Constants
  
              gdBrushed (CONSTANT)
                      Used in place of a color when invoking a
                      line-drawing function such as gdImageLine or
                      gdImageRectangle. When gdBrushed is used as the
                      color, the brush image set with gdImageSetBrush is
                      drawn in place of each pixel of the line (the brush
                      is usually larger than one pixel, creating the
                      effect of a wide paintbrush). See also
                      gdStyledBrushed for a way to draw broken lines with
                      a series of distinct copies of an image.
                      
              gdMaxColors(CONSTANT)
                      The constant 256. This is the maximum number of
                      colors in a GIF file according to the GIF standard,
                      and is also the maximum number of colors in a gd
                      image.
                      
              gdStyled (CONSTANT)
                      Used in place of a color when invoking a
                      line-drawing function such as gdImageLine or
                      gdImageRectangle. When gdStyled is used as the
                      color, the colors of the pixels are drawn
                      successively from the style that has been set with
                      gdImageSetStyle. If the color of a pixel is equal
                      to gdTransparent, that pixel is not altered. (This
                      mechanism is completely unrelated to the
                      "transparent color" of the image itself; see
                      gdImageColorTransparent gdImageColorTransparent for
                      that mechanism.) See also gdStyledBrushed.
                      
              gdStyledBrushed (CONSTANT)
                      Used in place of a color when invoking a
                      line-drawing function such as gdImageLine or
                      gdImageRectangle. When gdStyledBrushed is used as
                      the color, the brush image set with gdImageSetBrush
                      is drawn at each pixel of the line, providing that
                      the style set with gdImageSetStyle contains a
                      nonzero value (OR gdTransparent, which does not
                      equal zero but is supported for consistency) for
                      the current pixel. (Pixels are drawn successively
                      from the style as the line is drawn, returning to
                      the beginning when the available pixels in the
                      style are exhausted.) Note that this differs from
                      the behavior of gdStyled, in which the values in
                      the style are used as actual pixel colors, except
                      for gdTransparent.
                      
              gdDashSize (CONSTANT)
                      The length of a dash in a dashed line. Defined to
                      be 4 for backwards compatibility with programs that
                      use gdImageDashedLine. New programs should use
                      gdImageSetStyle and call the standard gdImageLine
                      function with the special "color" gdStyled or
                      gdStyledBrushed.
                      
              gdTiled (CONSTANT)
                      Used in place of a normal color in
                      gdImageFilledRectangle, gdImageFilledPolygon,
                      gdImageFill, and gdImageFillToBorder. gdTiled
                      selects a pixel from the tile image set with
                      gdImageSetTile in such a way as to ensure that the
                      filled area will be tiled with copies of the tile
                      image. See the discussions of gdImageFill and
                      gdImageFillToBorder for special restrictions
                      regarding those functions.
                      
              gdTransparent (CONSTANT)
                      Used in place of a normal color in a style to be
                      set with gdImageSetStyle. gdTransparent is not the
                      transparent color index of the image; for that
                      functionality please see gdImageColorTransparent.
                      
  About the additional .gd image file format
  
                      In addition to reading and writing the GIF format
                      and reading the X Bitmap format, gd has the
                      capability to read and write its own ".gd" format.
                      This format is not intended for general purpose use
                      and should never be used to distribute images. It
                      is not a compressed format. Its purpose is solely
                      to allow very fast loading of images your program
                      needs often in order to build other images for
                      output. If you are experiencing performance
                      problems when loading large, fixed GIF images your
                      program needs to produce its output images, you may
                      wish to examine the functions gdImageCreateFromGd
                      and gdImageGd, which read and write .gd format
                      images.
                      
                      The program "giftogd.c" is provided as a simple way
                      of converting .gif files to .gd format. I emphasize
                      again that you will not need to use this format
                      unless you have a need for high-speed loading of a
                      few frequently-used images in your program.
                      
  Please tell us you're using gd!
  
                      When you contact us and let us know you are using
                      gd, you help us justify the time spent in
                      maintaining and improving it. So please let us
                      know. If the results are publicly visible on the
                      web, a URL is a wonderful thing to receive, but if
                      it's not a publicly visible project, a simple note
                      is just as welcome.
                      
  If you have problems
  
                      If you have any difficulties with gd, feel free to
                      contact the author, Thomas Boutell. Be sure to read
                      this manual carefully first.
                      
  Alphabetical quick index
  
                      gdBrushed | gdDashSize | gdFont | gdFontPtr |
                      gdImage | gdImageArc | gdImageBlue |
                      gdImageBoundsSafe | gdImageChar | gdImageCharUp |
                      gdImageColorAllocate | gdImageColorClosest |
                      gdImageColorDeallocate | gdImageColorExact |
                      gdImageColorTransparent | gdImageCopy |
                      gdImageCopyResized | gdImageCreate |
                      gdImageCreateFromGd | gdImageCreateFromGif |
                      gdImageCreateFromXbm | gdImageDashedLine |
                      gdImageDestroy | gdImageFill | gdImageFillToBorder
                      | gdImageFilledRectangle | gdImageGd |
                      gdImageGetInterlaced | gdImageGetPixel |
                      gdImageGetTransparent | gdImageGif | gdImageGreen |
                      gdImageInterlace | gdImageLine |
                      gdImageFilledPolygon | gdImagePolygon | gdImagePtr
                      | gdImageRectangle | gdImageRed | gdImageSetBrush |
                      gdImageSetPixel | gdImageSetStyle | gdImageSetTile
                      | gdImageString | gdImageString16 | gdImageStringUp
                      | gdImageStringUp16 | gdMaxColors | gdPoint |
                      gdStyled | gdStyledBrushed | gdTiled |
                      gdTransparent
                      
                      Boutell.Com, Inc.

                                   gd 1.7.3
                                       
A graphics library for fast image creation

Follow this link to the latest version of this document.

     _HEY! READ THIS!_ gd 1.7.3 creates PNG images, not GIF images. This
     is a good thing. PNG is a more compact format, and full compression
     is available. Existing code will need modification to call
     gdImagePng instead of gdImageGif. _Please do not ask us to send you
     the old GIF version of GD._ Unisys holds a patent on the LZW
     compression algorithm, which is used in fully compressed GIF
     images. We are still investigating the legal issues surrounding
     various alternative means of producing a valid GIF file.
     
     gd 1.7.3 _requires_ that the following libraries also be installed:
     
     libpng
     
     zlib
     
     If you want to use the TrueType font support, you must also install
     the _Freetype library_, including the _freetype.h header file_. See
     the Freetype Home Page. No, I cannot explain why that site is down
     on a particular day, and no, I can't send you a copy.
     
     If you want to use the Xpm color bitmap loading support, you must
     also have the X Window System and the Xpm library installed (Xpm is
     often included in modern X distributions).
     
     Please read the documentation and install the required libraries.
     Do not send email asking why png.h is not found. See the
     requirements section for more information. Thank you!
     
  Table of Contents
  
     * Credits and license terms
     * What's new in version 1.7.3?
     * What's new in version 1.7.2?
     * What's new in version 1.7.1?
     * What's new in version 1.7?
     * What's new in version 1.6.3?
     * What's new in version 1.6.2?
     * What's new in version 1.6.1?
     * What's new in version 1.6?
     * What is gd?
     * What if I want to use another programming language?
     * What else do I need to use gd?
     * How do I get gd?
     * How do I build gd?
     * gd basics: using gd in your program
     * webpng: a useful example
     * Function and type reference by category
     * About the additional .gd image file format
     * Please tell us you're using gd!
     * If you have problems
     * Alphabetical quick index
       
   Up to the Boutell.Com, Inc. Home Page
   
  Credits and license terms
  
   In order to resolve any possible confusion regarding the authorship of
   gd, the following copyright statement covers all of the authors who
   have required such a statement. _If you are aware of any oversights in
   this copyright notice, please contact Thomas Boutell who will be
   pleased to correct them._

COPYRIGHT STATEMENT FOLLOWS THIS LINE

     Portions copyright 1994, 1995, 1996, 1997, 1998, 1999, by Cold
     Spring Harbor Laboratory. Funded under Grant P41-RR02188 by the
     National Institutes of Health.
     
     Portions copyright 1996, 1997, 1998, 1999, by Boutell.Com, Inc.
     
     Portions relating to GD2 format copyright 1999 Philip Warner.
     
     Portions relating to PNG copyright 1999, Greg Roelofs.
     
     Portions relating to libttf copyright 1999, John Ellson
     (ellson@lucent.com).
     
     _Permission has been granted to copy and distribute gd in any
     context without fee, including a commercial application, provided
     that this notice is present in user-accessible supporting
     documentation._
     
     This does not affect your ownership of the derived work itself, and
     the intent is to assure proper credit for the authors of gd, not to
     interfere with your productive use of gd. If you have questions,
     ask. "Derived works" includes all programs that utilize the
     library. Credit must be given in user-accessible documentation.
     
     _This software is provided "AS IS."_ The copyright holders disclaim
     all warranties, either express or implied, including but not
     limited to implied warranties of merchantability and fitness for a
     particular purpose, with respect to this code and accompanying
     documentation.
     
     Although their code does not appear in gd 1.7.3, the authors wish
     to thank David Koblas, David Rowley, and Hutchison Avenue Software
     Corporation for their prior contributions.
     
END OF COPYRIGHT STATEMENT

  What is gd?
  
   gd is a graphics library. It allows your code to quickly draw images
   complete with lines, arcs, text, multiple colors, cut and paste from
   other images, and flood fills, and write out the result as a .PNG
   file. This is particularly useful in World Wide Web applications,
   where .PNG is one of the formats accepted for inline images by most
   browsers.
   
   gd is not a paint program. If you are looking for a paint program, you
   are looking in the wrong place. If you are not a programmer, you are
   looking in the wrong place.
   
   gd does not provide for every possible desirable graphics operation.
   It is not necessary or desirable for gd to become a kitchen-sink
   graphics package, but version 1.7.3 incorporates most of the commonly
   requested features for an 8-bit 2D package. Support for truecolor
   images, JPEG and truecolor PNG is planned for version 2.0.
   
  What if I want to use another programming language?
  
    Perl
    
   gd can also be used from Perl, courtesy of Lincoln Stein's GD.pm
   library, which uses gd as the basis for a set of Perl 5.x classes.
   Updated to gd 1.6 and up.
   
    Tcl
    
   gd can be used from Tcl with John Ellson's Gdtclft dynamically loaded
   extension package. (Gdtclft2.0 or later is needed for gd-1.6 and up
   with PNG output.)
   
    Any Language
    
   There are, at the moment, at least three simple interpreters that
   perform gd operations. You can output the desired commands to a simple
   text file from whatever scripting language you prefer to use, then
   invoke the interpreter.
   
   These packages have not been updated to gd 1.6 and up as of this
   writing.
     * tgd, by Bradley K. Sherman
     * fly, by Martin Gleeson
       
  What's new in version 1.7.3?
  
   Another attempt at Makefile fixes to permit linking with all libraries
   required on platforms with order- dependent linkers. Perhaps it will
   work this time.
   
  What's new in version 1.7.2?
  
   An uninitialized-pointer bug in gdtestttf.c was corrected. This bug
   caused crashes at the end of each call to gdImageStringTTF on some
   platforms. Thanks to Wolfgang Haefelinger.
   
   Documentation fixes. Thanks to Dohn Arms.
   
   Makefile fixes to permit linking with all libraries required on
   platforms with order- dependent linkers.
   
  What's new in version 1.7.1?
  
   A minor buglet in the Makefile was corrected, as well as an inaccurate
   error message in gdtestttf.c. Thanks to Masahito Yamaga.
   
  What's new in version 1.7?
  
   Version 1.7 contains the following changes:
     * Japanese language support for the TrueType functions. Thanks to
       Masahito Yamaga.
     * autoconf and configure have been removed, in favor of a carefully
       designed Makefile which produces and properly installs the library
       and the binaries. System-dependent variables are at the top of the
       Makefile for easy modification. I'm sorry, folks, but autoconf
       generated _many, many confused email messages_ from people who
       didn't have things where autoconf expected to find them. I am not
       an autoconf/automake wizard, and gd is a simple, very compact
       library which does not need to be a shared library. I _did_ make
       many improvements over the old gd 1.3 Makefile, which were
       directly inspired by the autoconf version found in the 1.6 series
       (thanks to John Ellson).
     * Completely ANSI C compliant, according to the -pedantic-errors
       flag of gcc. Several pieces of not-quite-ANSI-C code were causing
       problems for those with non-gcc compilers.
     * gdttf.c patched to allow the use of Windows symbol fonts, when
       present (thanks to Joseph Peppin).
     * extern "C" wrappers added to gd.h and the font header files for
       the convenience of C++ programmers. bdftogd was also modified to
       automatically insert these wrappers into future font header files.
       Thanks to John Lindal.
     * Compiles correctly on platforms that don't define SEEK_SET. Thanks
       to Robert Bonomi.
     * Loads Xpm images via the gdImageCreateFromXpm function, if the Xpm
       library is available. Thanks to Caolan McNamara.
       
  What's new in version 1.6.3?
  
   Version 1.6.3 corrects a memory leak in gd_png.c. This leak caused a
   significant amount of memory to be allocated and not freed when
   writing a PNG image.
   
  What's new in version 1.6.2?
  
   Version 1.6.2 from John Ellson adds two new functions:
     * gdImageStringTTF - scalable, rotatable, anti-aliased, TrueType
       strings using the FreeType library, but only if libttf is found by
       configure. _We do not provide TrueType fonts. Obtaining them is
       entirely up to you._
     * gdImageColorResolve - an efficient alternative for the common code
       fragment:


      if ((color=gdImageColorExact(im,R,G,B)) < 0)
          if ((color=gdImageColorAllocate(im,R,G,B)) < 0)
              color=gdImageColorClosest(im,R,G,B);

   Also in this release the build process has been converted to GNU
   autoconf/automake/libtool conventions so that both (or either) static
   and shared libraries can be built.
   
  What's new in version 1.6.1?
  
   Version 1.6.1 incorporates superior PNG reading and writing code from
   Greg Roelofs, with minor modifications by Tom Boutell. Specifically, I
   altered his code to read non-palette images (converting them to
   palette images badly, by dithering them), and to tolerate palette
   images with types of transparency that gd doesn't actually support (it
   just ignores the advanced transparency features). Any bugs in this
   area are therefore my fault, not Greg's.
   
   Unlike gd 1.6, users should have no trouble linking with gd 1.6.1 if
   they follow the instructions and install all of the pieces. However,
   _If you get undefined symbol errors, be sure to check for older
   versions of libpng in your library directories!_
   
  What's new in version 1.6?
  
   Version 1.6 features the following changes:
   
   _Support for 8-bit palette PNG images has been added. Support for GIF
   has been removed._ This step was taken to completely avoid the legal
   controversy regarding the LZW compression algorithm used in GIF.
   Unisys holds a patent which is relevant to LZW compression. PNG is a
   superior image format in any case. Now that PNG is supported by both
   Microsoft Internet Explorer and Netscape (in their recent releases),
   we highly recommend that GD users upgrade in order to get
   well-compressed images in a format which is legally unemcumbered.
   
  What's new in version 1.5?
  
   Version 1.5 featured the following changes:
   
   _New GD2 format_
          An improvement over the GD format, the GD2 format uses the zlib
          compression library to compress the image in chunks. This
          results in file sizes comparable to GIFs, with the ability to
          access parts of large images without having to read the entire
          image into memory.
          
          This format also supports version numbers and rudimentary
          validity checks, so it should be more 'supportable' than the
          previous GD format.
          
   _Re-arranged source files_
          gd.c has been broken into constituant parts: io, gif, gd, gd2
          and graphics functions are now in separate files.
          
   _Extended I/O capabilities._
          The source/sink feature has been extended to support GD2 file
          formats (which require seek/tell functions), and to allow more
          general non-file I/O.
          
   _Better support for Lincoln Stein's Perl Module_
          The new gdImage*Ptr function returns the chosen format stored
          in a block of memory. This can be directly used by the GD perl
          module.
          
   _Added functions_
          gdImageCreateFromGd2Part - allows retrieval of part of an image
          (good for huge images, like maps),
          gdImagePaletteCopy - Copies a palette from one image to
          another, doing it's best to match the colors in the target
          image to the colors in the source palette.
          gdImageGd2, gdImageCreateFromGd2 - Support for new format
          gdImageCopyMerge - Merges two images (useful to highlight part
          of an image)
          gdImageCopyMergeGray - Similar to gdImageCopyMerge, but tries
          to preserve source image hue.
          gdImagePngPtr, gdImageGdPtr, gdImageGd2Ptr - return memort
          blocks for each type of image.
          gdImageCreateFromPngCtx, gdImageCreateFromGdCtx,
          gdImageCreateFromGd2Ctx, gdImageCreateFromGd2PartCtx - Support
          for new I/O context.
          
   _NOTE:_ In fairness to Thomas Boutell, any bug/problems with any of
   the above features should probably be reported to Philip Warner.
   
  What's new in version 1.4?
  
   Version 1.4 features the following changes:
   
   Fixed polygon fill routine (again)
          Thanks to Kirsten Schulz, version 1.4 is able to fill numerous
          types of polygons that caused problems with previous releases,
          including version 1.3.
          
   Support for alternate data sources
          Programmers who wish to load a GIF from something other than a
          stdio FILE * stream can use the new gdImageCreateFromPngSource
          function.
          
   Support for alternate data destinations
          Programmers who wish to write a GIF to something other than a
          stdio FILE * stream can use the new gdImagePngToSink function.
          
   More tolerant when reading GIFs
          Version 1.4 does not crash when reading certain animated GIFs,
          although it still only reads the first frame. Version 1.4 also
          has overflow testing code to prevent crashes when reading
          damaged GIFs.
          
  What's new in version 1.3?
  
   Version 1.3 features the following changes:
   
   Non-LZW-based GIF compression code
          Version 1.3 contained GIF compression code that uses simple Run
          Length Encoding instead of LZW compression, while still
          retaining compatibility with normal LZW-based GIF decoders
          (your browser will still like your GIFs). _LZW compression is
          patented by Unisys. We are currently reevaluating the approach
          taken by gd 1.3. The current release of gd does not support
          this approach. We recommend that you use the current release,
          and generate PNG images._ Thanks to Hutchison Avenue Software
          Corporation for contributing the RLE GIF code.
          
   8-bit fonts, and 8-bit font support
          This improves support for European languages. Thanks are due to
          Honza Pazdziora and also to Jan Pazdziora . Also see the
          provided bdftogd Perl script if you wish to convert fixed-width
          X11 fonts to gd fonts.
          
   16-bit font support (no fonts provided)
          Although no such fonts are provided in the distribution, fonts
          containing more than 256 characters should work if the
          gdImageString16 and gdImageStringUp16 routines are used.
          
   Improvements to the "webpng" example/utility
          The "webpng" utility is now a slightly more useful application.
          Thanks to Brian Dowling for this code.
          
   Corrections to the color resolution field of GIF output
          Thanks to Bruno Aureli.
          
   Fixed polygon fills
          A one-line patch for the infamous polygon fill bug, courtesy of
          Jim Mason. I believe this fix is sufficient. However, if you
          find a situation where polygon fills still fail to behave
          properly, please send code that demonstrates the problem, _and_
          a fix if you have one. Verifying the fix is important.
          
   Row-major, not column-major
          Internally, gd now represents the array of pixels as an array
          of rows of pixels, rather than an array of columns of pixels.
          This improves the performance of compression and decompression
          routines slightly, because horizontally adjacent pixels are now
          next to each other in memory. _This should not affect properly
          written gd applications, but applications that directly
          manipulate the pixels array will require changes._
          
  What else do I need to use gd?
  
   To use gd, you will need an ANSI C compiler. _All popular Windows 95
   and NT C compilers are ANSI C compliant._ Any full-ANSI-standard C
   compiler should be adequate. _The cc compiler released with SunOS
   4.1.3 is not an ANSI C compiler. Most Unix users who do not already
   have gcc should get it. gcc is free, ANSI compliant and a de facto
   industry standard. Ask your ISP why it is missing._
   
   As of version 1.6, you also need the zlib compression library, and the
   libpng library. As of version 1.6.2, you can draw text using
   antialiased TrueType fonts if you also have the libttf library
   installed, but this is not mandatory. zlib is available for a variety
   of platforms from the zlib web site. libpng is available for a variety
   of platforms from the PNG web site.
   
   You will also want a PNG viewer, if you do not already have one for
   your system, since you will need a good way to check the results of
   your work. Netscape 4.04 and higher, and Microsoft Internet Explorer
   4.0 or higher, both support PNG. For some purposes you might be
   happier with a package like Lview Pro for Windows or xv for X. There
   are PNG viewers available for every graphics-capable modern operating
   system, so consult newsgroups relevant to your particular system.
   
  How do I get gd?
  
    By HTTP
    
     * Gzipped Tar File (Unix)
     * .ZIP File (Windows)
       
    By FTP
    
     * Gzipped Tar File (Unix)
     * .ZIP File (Windows)
       
  How do I build gd?
  
   In order to build gd, you must first unpack the archive you have
   downloaded. If you are not familiar with tar and gunzip (Unix) or ZIP
   (Windows), please consult with an experienced user of your system.
   Sorry, we cannot answer questions about basic Internet skills.
   
   Unpacking the archive will produce a directory called "gd-1.7.3".
   
    For Unix
    
   cd to the 1.7.3 directory. Edit the Makefile with your preferred text
   editor and make any necessary changes to the settings at the top,
   especially if you want Xpm or TrueType support. Next, type "make". If
   you are the system administrator, and you wish to make the gd library
   available to other programs, you may also wish to type "make install".
   
   If you get errors, edit the Makefile again, paying special attention
   to the INCLUDEDIRS and LIBDIRS settings.
   
    For Windows, Mac, Et Cetera
    
   Create a project using your favorite programming environment. Copy all
   of the gd files to the project directory. Add gd.c to your project.
   Add other source files as appropriate. Learning the basic skills of
   creating projects with your chosen C environment is up to you.
   
   You have now built both the gd library and a demonstration program
   which shows off the capabilities of gd. To see it in action, type
   "gddemo".
   
   gddemo should execute without incident, creating the file demoout.png.
   (Note there is also a file named demoin.png, which is provided in the
   package as part of the demonstration.)
   
   Display demoout.png in your PNG viewer. The image should be 128x128
   pixels and should contain an image of the space shuttle with quite a
   lot of graphical elements drawn on top of it.
   
   (If you are missing the demoin.png file, the other items should appear
   anyway.)
   
   Look at demoin.png to see the original space shuttle image which was
   scaled and copied into the output image.
   
  gd basics: using gd in your program
  
   gd lets you create PNG images on the fly. To use gd in your program,
   include the file gd.h, and link with the libgd.a library produced by
   "make libgd.a", under Unix. Under other operating systems you will add
   gd.c to your own project.
   
   If you want to use the provided fonts, include gdfontt.h, gdfonts.h,
   gdfontmb.h, gdfontl.h and/or gdfontg.h. For more impressive results,
   install libttf and use the new gdImageStringTTF function. If you are
   not using the provided Makefile and/or a library-based approach, be
   sure to include the source modules as well in your project. (They may
   be too large for 16-bit memory models, that is, 16-bit DOS and
   Windows.)
   
   Here is a short example program. _(For a more advanced example, see
   gddemo.c, included in the distribution. gddemo.c is NOT the same
   program; it demonstrates additional features!)_
   
/* Bring in gd library functions */
#include "gd.h"

/* Bring in standard I/O so we can output the PNG to a file */
#include <stdio.h>

int main() {
        /* Declare the image */
        gdImagePtr im;
        /* Declare an output file */
        FILE *out;
        /* Declare color indexes */
        int black;
        int white;

        /* Allocate the image: 64 pixels across by 64 pixels tall */
        im = gdImageCreate(64, 64);

        /* Allocate the color black (red, green and blue all minimum).
                Since this is the first color in a new image, it will
                be the background color. */
        black = gdImageColorAllocate(im, 0, 0, 0);

        /* Allocate the color white (red, green and blue all maximum). */
        white = gdImageColorAllocate(im, 255, 255, 255);
        
        /* Draw a line from the upper left to the lower right,
                using white color index. */
        gdImageLine(im, 0, 0, 63, 63, white);

        /* Open a file for writing. "wb" means "write binary", important
                under MSDOS, harmless under Unix. */
        out = fopen("test.png", "wb");

        /* Output the image to the disk file. */
        gdImagePng(im, out);

        /* Close the file. */
        fclose(out);

        /* Destroy the image in memory. */
        gdImageDestroy(im);
}

   When executed, this program creates an image, allocates two colors
   (the first color allocated becomes the background color), draws a
   diagonal line (note that 0, 0 is the upper left corner), writes the
   image to a PNG file, and destroys the image.
   
   The above example program should give you an idea of how the package
   works. gd provides many additional functions, which are listed in the
   following reference chapters, complete with code snippets
   demonstrating each. There is also an alphabetical index.
   
  Webpng: a more powerful gd example
  
   Webpng is a simple utility program to manipulate PNGs from the command
   line. It is written for Unix and similar command-line systems, but
   should be easily adapted for other environments. Webpng allows you to
   set transparency and interlacing and output interesting information
   about the PNG in question.
   
   webpng.c is provided in the distribution. Unix users can simply type
   "make webpng" to compile the program. Type "webpng" with no arguments
   to see the available options.
   
Function and type reference

     * Types
     * Image creation, destruction, loading and saving
     * Drawing, styling, brushing, tiling and filling functions
     * Query functions (not color-related)
     * Font and text-handling functions
     * Color handling functions
     * Copying and resizing functions
     * Miscellaneous Functions
     * Constants
       
  Types
  
   gdImage_(TYPE)_
          The data structure in which gd stores images. gdImageCreate
          returns a pointer to this type, and the other functions expect
          to receive a pointer to this type as their first argument. You
          may read the members sx (size on X axis), sy (size on Y axis),
          colorsTotal (total colors), red (red component of colors; an
          array of 256 integers between 0 and 255), green (green
          component of colors, as above), blue (blue component of colors,
          as above), and transparent (index of transparent color, -1 if
          none); please do so using the macros provided. Do NOT set the
          members directly from your code; use the functions provided.
          

typedef struct {
        unsigned char ** pixels;
        int sx;
        int sy;
        int colorsTotal;
        int red[gdMaxColors];
        int green[gdMaxColors];
        int blue[gdMaxColors];
        int open[gdMaxColors];
        int transparent;
} gdImage;

   gdImagePtr _(TYPE)_
          A pointer to an image structure. gdImageCreate returns this
          type, and the other functions expect it as the first argument.
          
   gdFont _(TYPE)_
          A font structure. Used to declare the characteristics of a
          font. Plese see the files gdfontl.c and gdfontl.h for an
          example of the proper declaration of this structure. You can
          provide your own font data by providing such a structure and
          the associated pixel array. You can determine the width and
          height of a single character in a font by examining the w and h
          members of the structure. If you will not be creating your own
          fonts, you will not need to concern yourself with the rest of
          the components of this structure.
          

typedef struct {
        /* # of characters in font */
        int nchars;
        /* First character is numbered... (usually 32 = space) */
        int offset;
        /* Character width and height */
        int w;
        int h;
        /* Font data; array of characters, one row after another.
                Easily included in code, also easily loaded from
                data files. */
        char *data;
} gdFont;

   gdFontPtr _(TYPE)_
          A pointer to a font structure. Text-output functions expect
          these as their second argument, following the gdImagePtr
          argument. Two such pointers are declared in the provided
          include files gdfonts.h and gdfontl.h.
          
   gdPoint _(TYPE)_
          Represents a point in the coordinate space of the image; used
          by gdImagePolygon and gdImageFilledPolygon.
          

typedef struct {
        int x, y;
} gdPoint, *gdPointPtr;

   gdPointPtr _(TYPE)_
          A pointer to a gdPoint structure; passed as an argument to
          gdImagePolygon and gdImageFilledPolygon.
          
   gdSource _(TYPE)_

typedef struct {
        int (*source) (void *context, char *buffer, int len);
        void *context;
} gdSource, *gdSourcePtr;

   Represents a source from which a PNG can be read. Programmers who do
   not wish to read PNGs from a file can provide their own alternate
   input mechanism, using the gdImageCreateFromPngSource function. See
   the documentation of that function for an example of the proper use of
   this type.
   
   gdSink _(TYPE)_

typedef struct {
        int (*sink) (void *context, char *buffer, int len);
        void *context;
} gdSink, *gdSinkPtr;

   Represents a "sink" (destination) to which a PNG can be written.
   Programmers who do not wish to write PNGs to a file can provide their
   own alternate output mechanism, using the gdImagePngToSink function.
   See the documentation of that function for an example of the proper
   use of this type.
   
  Image creation, destruction, loading and saving
  
   gdImageCreate(sx, sy) _(FUNCTION)_
          gdImageCreate is called to create images. Invoke gdImageCreate
          with the x and y dimensions of the desired image. gdImageCreate
          returns a gdImagePtr to the new image, or NULL if unable to
          allocate the image. The image must eventually be destroyed
          using gdImageDestroy().
          

... inside a function ...
gdImagePtr im;
im = gdImageCreate(64, 64);
/* ... Use the image ... */
gdImageDestroy(im);

   gdImageCreateFromPng(FILE *in) _(FUNCTION)_
          gdImageCreateFromPngCtx(gdIOCtx *in) _(FUNCTION)_
          
          
          gdImageCreateFromPng is called to load images from PNG format
          files. Invoke gdImageCreateFromPng with an already opened
          pointer to a file containing the desired image.
          gdImageCreateFromPng returns a gdImagePtr to the new image, or
          NULL if unable to load the image (most often because the file
          is corrupt or does not contain a PNG image).
          gdImageCreateFromPng does _not_ close the file. You can inspect
          the sx and sy members of the image to determine its size. The
          image must eventually be destroyed using gdImageDestroy().
          

gdImagePtr im;
... inside a function ...
FILE *in;
in = fopen("mypng.png", "rb");
im = gdImageCreateFromPng(in);
fclose(in);
/* ... Use the image ... */
gdImageDestroy(im);

   gdImageCreateFromPngSource(gdSourcePtr in) _(FUNCTION)_
          gdImageCreateFromPngSource is called to load a PNG from a data
          source other than a file. Usage is very similar to the
          gdImageCreateFromPng function, except that the programmer
          provides a custom data source.
          
          The programmer must write an input function which accepts a
          context pointer, a buffer, and a number of bytes to be read as
          arguments. This function must read the number of bytes
          requested, unless the end of the file has been reached, in
          which case the function should return zero, or an error has
          occurred, in which case the function should return -1. The
          programmer then creates a gdSource structure and sets the
          source pointer to the input function and the context pointer to
          any value which is useful to the programmer.
          
          The example below implements gdImageCreateFromPng by creating a
          custom data source and invoking gdImageCreateFromPngSource.
          

static int freadWrapper(void *context, char *buf, int len);

gdImagePtr gdImageCreateFromPng(FILE *in)
{
        gdSource s;
        s.source = freadWrapper;
        s.context = in;
        return gdImageCreateFromPngSource(&s);
}

static int freadWrapper(void *context, char *buf, int len)
{
        int got = fread(buf, 1, len, (FILE *) context);
        return got;
}

   gdImageCreateFromGd(FILE *in) _(FUNCTION)_
          gdImageCreateFromGdCtx(gdIOCtx *in) _(FUNCTION)_
          
          
          gdImageCreateFromGd is called to load images from gd format
          files. Invoke gdImageCreateFromGd with an already opened
          pointer to a file containing the desired image in the gd file
          format, which is specific to gd and intended for very fast
          loading. (It is _not_ intended for compression; for
          compression, use PNG.) gdImageCreateFromGd returns a gdImagePtr
          to the new image, or NULL if unable to load the image (most
          often because the file is corrupt or does not contain a gd
          format image). gdImageCreateFromGd does _not_ close the file.
          You can inspect the sx and sy members of the image to determine
          its size. The image must eventually be destroyed using
          gdImageDestroy().
          

... inside a function ...
gdImagePtr im;
FILE *in;
in = fopen("mygd.gd", "rb");
im = gdImageCreateFromGd(in);
fclose(in);
/* ... Use the image ... */
gdImageDestroy(im);

   gdImageCreateFromGd2(FILE *in) _(FUNCTION)_
          gdImageCreateFromGd2Ctx(gdIOCtx *in) _(FUNCTION)_
          
          
          gdImageCreateFromGd2 is called to load images from gd2 format
          files. Invoke gdImageCreateFromGd2 with an already opened
          pointer to a file containing the desired image in the gd2 file
          format, which is specific to gd2 and intended for fast loading
          of parts of large images. (It is a compressed format, but
          generally not as good a LZW compression). gdImageCreateFromGd
          returns a gdImagePtr to the new image, or NULL if unable to
          load the image (most often because the file is corrupt or does
          not contain a gd format image). gdImageCreateFromGd2 does _not_
          close the file. You can inspect the sx and sy members of the
          image to determine its size. The image must eventually be
          destroyed using gdImageDestroy().
          

... inside a function ...
gdImagePtr im;
FILE *in;
in = fopen("mygd.gd2", "rb");
im = gdImageCreateFromGd2(in);
fclose(in);
/* ... Use the image ... */
gdImageDestroy(im);

   gdImageCreateFromGd2Part(FILE *in, int srcX, int srcY, int w, int h)
          _(FUNCTION)_
          gdImageCreateFromGd2PartCtx(gdIOCtx *in) _(FUNCTION)_
          
          
          gdImageCreateFromGd2Part is called to load parts of images from
          gd2 format files. Invoked in the same way as
          gdImageCreateFromGd2, but with extra parameters indicating the
          source (x, y) and width/height of the desired image.
          gdImageCreateFromGd2Part returns a gdImagePtr to the new image,
          or NULL if unable to load the image. The image must eventually
          be destroyed using gdImageDestroy().
          
   gdImageCreateFromXbm(FILE *in) _(FUNCTION)_
          gdImageCreateFromXbm is called to load images from X bitmap
          format files. Invoke gdImageCreateFromXbm with an already
          opened pointer to a file containing the desired image.
          gdImageCreateFromXbm returns a gdImagePtr to the new image, or
          NULL if unable to load the image (most often because the file
          is corrupt or does not contain an X bitmap format image).
          gdImageCreateFromXbm does _not_ close the file. You can inspect
          the sx and sy members of the image to determine its size. The
          image must eventually be destroyed using gdImageDestroy().
          

... inside a function ...
gdImagePtr im;
FILE *in;
in = fopen("myxbm.xbm", "rb");
im = gdImageCreateFromXbm(in);
fclose(in);
/* ... Use the image ... */
gdImageDestroy(im);

   gdImageCreateFromXpm(FILE *in) _(FUNCTION)_
          gdImageCreateFromXbm is called to load images from XPM X Window
          System color bitmap format files. This function is available
          only if HAVE_XPM is selected in the Makefile and the Xpm
          library is linked with the application. Invoke
          gdImageCreateFromXpm with an already opened pointer to a file
          containing the desired image. gdImageCreateFromXpm returns a
          gdImagePtr to the new image, or NULL if unable to load the
          image (most often because the file is corrupt or does not
          contain an XPM bitmap format image). gdImageCreateFromXpm does
          _not_ close the file. You can inspect the sx and sy members of
          the image to determine its size. The image must eventually be
          destroyed using gdImageDestroy().
          

... inside a function ...
gdImagePtr im;
FILE *in;
in = fopen("myxpm.xpm", "rb");
im = gdImageCreateFromXpm(in);
fclose(in);
/* ... Use the image ... */
gdImageDestroy(im);

   gdImageDestroy(gdImagePtr im) _(FUNCTION)_
          gdImageDestroy is used to free the memory associated with an
          image. It is important to invoke gdImageDestroy before exiting
          your program or assigning a new image to a gdImagePtr variable.
          

... inside a function ...
gdImagePtr im;
im = gdImageCreate(10, 10);
/* ... Use the image ... */
/* Now destroy it */
gdImageDestroy(im);

   void gdImagePng(gdImagePtr im, FILE *out) _(FUNCTION)_
          gdImagePng outputs the specified image to the specified file in
          PNG format. The file must be open for writing. Under MSDOS and
          all versions of Windows, it is important to use "wb" as opposed
          to simply "w" as the mode when opening the file, and under Unix
          there is no penalty for doing so. gdImagePng does _not_ close
          the file; your code must do so.
          

... inside a function ...
gdImagePtr im;
int black, white;
FILE *out;
/* Create the image */
im = gdImageCreate(100, 100);
/* Allocate background */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Allocate drawing color */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Draw rectangle */
gdImageRectangle(im, 0, 0, 99, 99, black);
/* Open output file in binary mode */
out = fopen("rect.png", "wb");
/* Write PNG */
gdImagePng(im, out);
/* Close file */
fclose(out);
/* Destroy image */
gdImageDestroy(im);

   void* gdImagePngPtr(gdImagePtr im, int *size) _(FUNCTION)_
          Identical to gdImagePng except that it returns a pointer to a
          memory area with the PNG data. This memory must be freed by the
          caller when it is no longer needed. The 'size' parameter
          received the total size of the block of memory.
          
   gdImagePngToSink(gdImagePtr im, gdSinkPtr out) _(FUNCTION)_
          gdImagePngToSink is called to write a PNG to a data "sink"
          (destination) other than a file. Usage is very similar to the
          gdImagePng function, except that the programmer provides a
          custom data sink.
          
          The programmer must write an output function which accepts a
          context pointer, a buffer, and a number of bytes to be written
          as arguments. This function must write the number of bytes
          requested and return that number, unless an error has occurred,
          in which case the function should return -1. The programmer
          then creates a gdSink structure and sets the sink pointer to
          the output function and the context pointer to any value which
          is useful to the programmer.
          
          The example below implements gdImagePng by creating a custom
          data source and invoking gdImagePngFromSink.
          

static int stdioSink(void *context, char *buffer, int len)
{
        return fwrite(buffer, 1, len, (FILE *) context);
}

void gdImagePng(gdImagePtr im, FILE *out)
{
        gdSink mySink;
        mySink.context = (void *) out;
        mySink.sink = stdioSink;
        gdImagePngToSink(im, &mySink);
}

   void gdImageGd(gdImagePtr im, FILE *out) _(FUNCTION)_
          gdImageGd outputs the specified image to the specified file in
          the gd image format. The file must be open for writing. Under
          MSDOS and all versions of Windows, it is important to use "wb"
          as opposed to simply "w" as the mode when opening the file, and
          under Unix there is no penalty for doing so. gdImagePng does
          _not_ close the file; your code must do so.
          
          The gd image format is intended for fast reads and writes of
          images your program will need frequently to build other images.
          It is _not_ a compressed format, and is not intended for
          general use.
          

... inside a function ...
gdImagePtr im;
int black, white;
FILE *out;
/* Create the image */
im = gdImageCreate(100, 100);
/* Allocate background */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Allocate drawing color */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Draw rectangle */
gdImageRectangle(im, 0, 0, 99, 99, black);
/* Open output file in binary mode */
out = fopen("rect.gd", "wb");
/* Write gd format file */
gdImageGd(im, out);
/* Close file */
fclose(out);
/* Destroy image */
gdImageDestroy(im);

   void* gdImageGdPtr(gdImagePtr im, int *size) _(FUNCTION)_
          Identical to gdImageGd except that it returns a pointer to a
          memory area with the GD data. This memory must be freed by the
          caller when it is no longer needed. The 'size' parameter
          received the total size of the block of memory.
          
   void gdImageGd2(gdImagePtr im, FILE *out, int chunkSize, int fmt)
          _(FUNCTION)_
          gdImageGd2 outputs the specified image to the specified file in
          the gd2 image format. The file must be open for writing. Under
          MSDOS and all versions of Windows, it is important to use "wb"
          as opposed to simply "w" as the mode when opening the file, and
          under Unix there is no penalty for doing so. gdImageGd2 does
          _not_ close the file; your code must do so.
          
          The gd2 image format is intended for fast reads and writes of
          parts of images. It is a compressed format, and well suited to
          retrieving smll sections of much larger images. The third and
          fourth parameters are the 'chunk size' and format
          resposectively.
          
          The file is stored as a series of compressed subimages, and the
          _Chunk Size_ determines the sub-image size - a value of zero
          causes the GD library to use the default.
          
          It is also possible to store GD2 files in an uncompressed
          format, in which case the fourth parameter should be
          GD2_FMT_RAW.
          

... inside a function ...
gdImagePtr im;
int black, white;
FILE *out;
/* Create the image */
im = gdImageCreate(100, 100);
/* Allocate background */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Allocate drawing color */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Draw rectangle */
gdImageRectangle(im, 0, 0, 99, 99, black);
/* Open output file in binary mode */
out = fopen("rect.gd", "wb");
/* Write gd2 format file */
gdImageGd2(im, out, 0, GD2_FMT_COMPRESSED);
/* Close file */
fclose(out);
/* Destroy image */
gdImageDestroy(im);

   void* gdImageGd2Ptr(gdImagePtr im, int chunkSize, int fmt, int *size)
          _(FUNCTION)_
          Identical to gdImageGd2 except that it returns a pointer to a
          memory area with the GD2 data. This memory must be freed by the
          caller when it is no longer needed. The 'size' parameter
          received the total size of the block of memory.
          
  Drawing Functions
  
   void gdImageSetPixel(gdImagePtr im, int x, int y, int color)
          _(FUNCTION)_
          gdImageSetPixel sets a pixel to a particular color index.
          Always use this function or one of the other drawing functions
          to access pixels; do not access the pixels of the gdImage
          structure directly.
          

... inside a function ...
gdImagePtr im;
int black;
int white;
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Set a pixel near the center. */
gdImageSetPixel(im, 50, 50, white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImageLine(gdImagePtr im, int x1, int y1, int x2, int y2, int
          color) _(FUNCTION)_
          gdImageLine is used to draw a line between two endpoints (x1,y1
          and x2, y2). The line is drawn using the color index specified.
          Note that the color index can be an actual color returned by
          gdImageColorAllocate or one of gdStyled, gdBrushed or
          gdStyledBrushed.
          

... inside a function ...
gdImagePtr im;
int black;
int white;
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Draw a line from the upper left corner to the lower right corner. */
gdImageLine(im, 0, 0, 99, 99, white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImageDashedLine(gdImagePtr im, int x1, int y1, int x2, int y2,
          int color) _(FUNCTION)_
          gdImageDashedLine is provided _solely for backwards
          compatibility _with gd 1.0. New programs should draw dashed
          lines using the normal gdImageLine function and the new
          gdImageSetStyle function.
          
          gdImageDashedLine is used to draw a dashed line between two
          endpoints (x1,y1 and x2, y2). The line is drawn using the color
          index specified. The portions of the line that are not drawn
          are left transparent so the background is visible.
          

... inside a function ...
gdImagePtr im;
int black;
int white;
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Draw a dashed line from the upper left corner to the lower right corner. */
gdImageDashedLine(im, 0, 0, 99, 99);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImagePolygon(gdImagePtr im, gdPointPtr points, int pointsTotal,
          int color) _(FUNCTION)_
          gdImagePolygon is used to draw a polygon with the verticies (at
          least 3) specified, using the color index specified. See also
          gdImageFilledPolygon.
          

... inside a function ...
gdImagePtr im;
int black;
int white;
/* Points of polygon */
gdPoint points[3];
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Draw a triangle. */
points[0].x = 50;
points[0].y = 0;
points[1].x = 99;
points[1].y = 99;
points[2].x = 0;
points[2].y = 99;
gdImagePolygon(im, points, 3, white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImageRectangle(gdImagePtr im, int x1, int y1, int x2, int y2,
          int color) _(FUNCTION)_
          gdImageRectangle is used to draw a rectangle with the two
          corners (upper left first, then lower right) specified, using
          the color index specified.
          

... inside a function ...
gdImagePtr im;
int black;
int white;
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Draw a rectangle occupying the central area. */
gdImageRectangle(im, 25, 25, 74, 74, white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImageFilledPolygon(gdImagePtr im, gdPointPtr points, int
          pointsTotal, int color) _(FUNCTION)_
          gdImageFilledPolygon is used to fill a polygon with the
          verticies (at least 3) specified, using the color index
          specified. See also gdImagePolygon.
          

... inside a function ...
gdImagePtr im;
int black;
int white;
int red;
/* Points of polygon */
gdPoint points[3];
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Allocate the color red. */
red = gdImageColorAllocate(im, 255, 0, 0);
/* Draw a triangle. */
points[0].x = 50;
points[0].y = 0;
points[1].x = 99;
points[1].y = 99;
points[2].x = 0;
points[2].y = 99;
/* Paint it in white */
gdImageFilledPolygon(im, points, 3, white);
/* Outline it in red; must be done second */
gdImagePolygon(im, points, 3, red);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImageFilledRectangle(gdImagePtr im, int x1, int y1, int x2, int
          y2, int color) _(FUNCTION)_
          gdImageFilledRectangle is used to draw a solid rectangle with
          the two corners (upper left first, then lower right) specified,
          using the color index specified.
          

... inside a function ...
gdImagePtr im;
int black;
int white;
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = int gdImageColorAllocate(im, 255, 255, 255);
/* Draw a filled rectangle occupying the central area. */
gdImageFilledRectangle(im, 25, 25, 74, 74, white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImageArc(gdImagePtr im, int cx, int cy, int w, int h, int s,
          int e, int color) _(FUNCTION)_
          gdImageArc is used to draw a partial ellipse centered at the
          given point, with the specified width and height in pixels. The
          arc begins at the position in degrees specified by s and ends
          at the position specified by e. The arc is drawn in the color
          specified by the last argument. A circle can be drawn by
          beginning from 0 degrees and ending at 360 degrees, with width
          and height being equal. e must be greater than s. Values
          greater than 360 are interpreted modulo 360.
          

... inside a function ...
gdImagePtr im;
int black;
int white;
im = gdImageCreate(100, 50);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Inscribe an ellipse in the image. */
gdImageArc(im, 50, 25, 98, 48, 0, 360, white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImageFillToBorder(gdImagePtr im, int x, int y, int border, int
          color) _(FUNCTION)_
          gdImageFillToBorder floods a portion of the image with the
          specified color, beginning at the specified point and stopping
          at the specified border color. For a way of flooding an area
          defined by the color of the starting point, see gdImageFill.
          
          The border color _cannot_ be a special color such as gdTiled;
          it must be a proper solid color. The fill color can be,
          however.
          
          Note that gdImageFillToBorder is recursive. It is not the most
          naive implementation possible, and the implementation is
          expected to improve, but there will always be degenerate cases
          in which the stack can become very deep. This can be a problem
          in MSDOS and MS Windows 3.1 environments. (Of course, in a Unix
          or Windows 95/98/NT environment with a proper stack, this is
          not a problem at all.)
          

... inside a function ...
gdImagePtr im;
int black;
int white;
int red;
im = gdImageCreate(100, 50);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Allocate the color red. */
red = gdImageColorAllocate(im, 255, 0, 0);
/* Inscribe an ellipse in the image. */
gdImageArc(im, 50, 25, 98, 48, 0, 360, white);
/* Flood-fill the ellipse. Fill color is red, border color is
        white (ellipse). */
gdImageFillToBorder(im, 50, 50, white, red);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImageFill(gdImagePtr im, int x, int y, int color) _(FUNCTION)_
          gdImageFill floods a portion of the image with the specified
          color, beginning at the specified point and flooding the
          surrounding region of the same color as the starting point. For
          a way of flooding a region defined by a specific border color
          rather than by its interior color, see gdImageFillToBorder.
          
          The fill color can be gdTiled, resulting in a tile fill using
          another image as the tile. However, the tile image cannot be
          transparent. If the image you wish to fill with has a
          transparent color index, call gdImageTransparent on the tile
          image and set the transparent color index to -1 to turn off its
          transparency.
          
          Note that gdImageFill is recursive. It is not the most naive
          implementation possible, and the implementation is expected to
          improve, but there will always be degenerate cases in which the
          stack can become very deep. This can be a problem in MSDOS and
          MS Windows environments. (Of course, in a Unix or Windows
          95/98/NT environment with a proper stack, this is not a problem
          at all.)
          

... inside a function ...
gdImagePtr im;
int black;
int white;
int red;
im = gdImageCreate(100, 50);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Allocate the color red. */
red = gdImageColorAllocate(im, 255, 0, 0);
/* Inscribe an ellipse in the image. */
gdImageArc(im, 50, 25, 98, 48, 0, 360, white);
/* Flood-fill the ellipse. Fill color is red, and will replace the
        black interior of the ellipse. */
gdImageFill(im, 50, 50, red);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

   void gdImageSetBrush(gdImagePtr im, gdImagePtr brush) _(FUNCTION)_
          A "brush" is an image used to draw wide, shaped strokes in
          another image. Just as a paintbrush is not a single point, a
          brush image need not be a single pixel. _Any_ gd image can be
          used as a brush, and by setting the transparent color index of
          the brush image with gdImageColorTransparent, a brush of any
          shape can be created. All line-drawing functions, such as
          gdImageLine and gdImagePolygon, will use the current brush if
          the special "color" gdBrushed or gdStyledBrushed is used when
          calling them.
          
          gdImageSetBrush is used to specify the brush to be used in a
          particular image. You can set any image to be the brush. If the
          brush image does not have the same color map as the first
          image, any colors missing from the first image will be
          allocated. If not enough colors can be allocated, the closest
          colors already available will be used. This allows arbitrary
          PNGs to be used as brush images. It also means, however, that
          you should not set a brush unless you will actually use it; if
          you set a rapid succession of different brush images, you can
          quickly fill your color map, and the results will not be
          optimal.
          
          You need not take any special action when you are finished with
          a brush. As for any other image, if you will not be using the
          brush image for any further purpose, you should call
          gdImageDestroy. You must not use the color gdBrushed if the
          current brush has been destroyed; you can of course set a new
          brush to replace it.
          

... inside a function ...
gdImagePtr im, brush;
FILE *in;
int black;
im = gdImageCreate(100, 100);
/* Open the brush PNG. For best results, portions of the
        brush that should be transparent (ie, not part of the
        brush shape) should have the transparent color index. */
in = fopen("star.png", "rb");
brush = gdImageCreateFromPng(in);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
gdImageSetBrush(im, brush);
/* Draw a line from the upper left corner to the lower right corner
        using the brush. */
gdImageLine(im, 0, 0, 99, 99, gdBrushed);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);
/* Destroy the brush image */
gdImageDestroy(brush);

   void gdImageSetTile(gdImagePtr im, gdImagePtr tile) _(FUNCTION)_
          A "tile" is an image used to fill an area with a repeated
          pattern. _Any_ gd image can be used as a tile, and by setting
          the transparent color index of the tile image with
          gdImageColorTransparent, a tile that allows certain parts of
          the underlying area to shine through can be created. All
          region-filling functions, such as gdImageFill and
          gdImageFilledPolygon, will use the current tile if the special
          "color" gdTiled is used when calling them.
          
          gdImageSetTile is used to specify the tile to be used in a
          particular image. You can set any image to be the tile. If the
          tile image does not have the same color map as the first image,
          any colors missing from the first image will be allocated. If
          not enough colors can be allocated, the closest colors already
          available will be used. This allows arbitrary PNGs to be used
          as tile images. It also means, however, that you should not set
          a tile unless you will actually use it; if you set a rapid
          succession of different tile images, you can quickly fill your
          color map, and the results will not be optimal.
          
          You need not take any special action when you are finished with
          a tile. As for any other image, if you will not be using the
          tile image for any further purpose, you should call
          gdImageDestroy. You must not use the color gdTiled if the
          current tile has been destroyed; you can of course set a new
          tile to replace it.
          

... inside a function ...
gdImagePtr im, tile;
FILE *in;
int black;
im = gdImageCreate(100, 100);
/* Open the tile PNG. For best results, portions of the
        tile that should be transparent (ie, allowing the
        background to shine through) should have the transparent
        color index. */
in = fopen("star.png", "rb");
tile = gdImageCreateFromPng(in);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
gdImageSetTile(im, tile);
/* Fill an area using the tile. */
gdImageFilledRectangle(im, 25, 25, 75, 75, gdTiled);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);
/* Destroy the tile image */
gdImageDestroy(tile);

   void gdImageSetStyle(gdImagePtr im, int *style, int styleLength)
          _(FUNCTION)_
          It is often desirable to draw dashed lines, dotted lines, and
          other variations on a broken line. gdImageSetStyle can be used
          to set any desired series of colors, including a special color
          that leaves the background intact, to be repeated during the
          drawing of a line.
          
          To use gdImageSetStyle, create an array of integers and assign
          them the desired series of color values to be repeated. You can
          assign the special color value gdTransparent to indicate that
          the existing color should be left unchanged for that particular
          pixel (allowing a dashed line to be attractively drawn over an
          existing image).
          
          Then, to draw a line using the style, use the normal
          gdImageLine function with the special color value gdStyled.
          
          As of version 1.1.1, the style array is copied when you set the
          style, so you need not be concerned with keeping the array
          around indefinitely. This should not break existing code that
          assumes styles are not copied.
          
          You can also combine styles and brushes to draw the brush image
          at intervals instead of in a continuous stroke. When creating a
          style for use with a brush, the style values are interpreted
          differently: zero (0) indicates pixels at which the brush
          should not be drawn, while one (1) indicates pixels at which
          the brush should be drawn. To draw a styled, brushed line, you
          must use the special color value gdStyledBrushed. For an
          example of this feature in use, see gddemo.c (provided in the
          distribution).
          

gdImagePtr im;
int styleDotted[2], styleDashed[6];
FILE *in;
int black;
int red;
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
red = gdImageColorAllocate(im, 255, 0, 0);
/* Set up dotted style. Leave every other pixel alone. */
styleDotted[0] = red;
styleDotted[1] = gdTransparent;
/* Set up dashed style. Three on, three off. */
styleDashed[0] = red;
styleDashed[1] = red;
styleDashed[2] = red;
styleDashed[3] = gdTransparent;
styleDashed[4] = gdTransparent;
styleDashed[5] = gdTransparent;
/* Set dotted style. Note that we have to specify how many pixels are
        in the style! */
gdImageSetStyle(im, styleDotted, 2);
/* Draw a line from the upper left corner to the lower right corner. */
gdImageLine(im, 0, 0, 99, 99, gdStyled);
/* Now the dashed line. */
gdImageSetStyle(im, styleDashed, 6);
gdImageLine(im, 0, 99, 0, 99, gdStyled);

/* ... Do something with the image, such as saving it to a file ... */

/* Destroy it */
gdImageDestroy(im);

  Query Functions
  
        int gdImageBlue(gdImagePtr im, int color) _(MACRO)_
                gdImageBlue is a macro which returns the blue component
                of the specified color index. Use this macro rather than
                accessing the structure members directly.
                
        int gdImageGetPixel(gdImagePtr im, int x, int y) _(FUNCTION)_
                gdImageGetPixel() retrieves the color index of a
                particular pixel. Always use this function to query
                pixels; do not access the pixels of the gdImage structure
                directly.
                

... inside a function ...
FILE *in;
gdImagePtr im;
int c;
in = fopen("mypng.png", "rb");
im = gdImageCreateFromPng(in);
fclose(in);
c = gdImageGetPixel(im, gdImageSX(im) / 2, gdImageSY(im) / 2);
printf("The value of the center pixel is %d; RGB values are %d,%d,%d\n",
        c, im->red[c], im->green[c], im->blue[c]);
gdImageDestroy(im);

        int gdImageBoundsSafe(gdImagePtr im, int x, int y) _(FUNCTION)_
                gdImageBoundsSafe returns true (1) if the specified point
                is within the bounds of the image, false (0) if not. This
                function is intended primarily for use by those who wish
                to add functions to gd. All of the gd drawing functions
                already clip safely to the edges of the image.
                

... inside a function ...
gdImagePtr im;
int black;
int white;
im = gdImageCreate(100, 100);
if (gdImageBoundsSafe(im, 50, 50)) {
        printf("50, 50 is within the image bounds\n");
} else {
        printf("50, 50 is outside the image bounds\n");
}
gdImageDestroy(im);

        int gdImageGreen(gdImagePtr im, int color) _(MACRO)_
                gdImageGreen is a macro which returns the green component
                of the specified color index. Use this macro rather than
                accessing the structure members directly.
                
        int gdImageRed(gdImagePtr im, int color) _(MACRO)_
                gdImageRed is a macro which returns the red component of
                the specified color index. Use this macro rather than
                accessing the structure members directly.
                
        int gdImageSX(gdImagePtr im) _(MACRO)_
                gdImageSX is a macro which returns the width of the image
                in pixels. Use this macro rather than accessing the
                structure members directly.
                
        int gdImageSY(gdImagePtr im) _(MACRO)_
                gdImageSY is a macro which returns the height of the
                image in pixels. Use this macro rather than accessing the
                structure members directly.
                
  Fonts and text-handling functions
  
        void gdImageChar(gdImagePtr im, gdFontPtr font, int x, int y, int
                c, int color) _(FUNCTION)_
                gdImageChar is used to draw single characters on the
                image. (To draw multiple characters, use gdImageString or
                gdImageString16. See also gdImageStringTTF, new with
                gd-1.6.2.) The second argument is a pointer to a font
                definition structure; five fonts are provided with gd,
                gdFontTiny, gdFontSmall, gdFontMediumBold, gdFontLarge,
                and gdFontGiant. You must include the files "gdfontt.h",
                "gdfonts.h", "gdfontmb.h", "gdfontl.h" and "gdfontg.h"
                respectively and (if you are not using a library-based
                approach) link with the corresponding .c files to use the
                provided fonts. The character specified by the fifth
                argument is drawn from left to right in the specified
                color. (See gdImageCharUp for a way of drawing vertical
                text.) Pixels not set by a particular character retain
                their previous color.
                

#include "gd.h"
#include "gdfontl.h"
... inside a function ...
gdImagePtr im;
int black;
int white;
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Draw a character. */
gdImageChar(im, gdFontLarge, 0, 0, 'Q', white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

        void gdImageCharUp(gdImagePtr im, gdFontPtr font, int x, int y,
                int c, int color) _(FUNCTION)_
                gdImageCharUp is used to draw single characters on the
                image, rotated 90 degrees. (To draw multiple characters,
                use gdImageStringUp or gdImageStringUp16.) The second
                argument is a pointer to a font definition structure;
                five fonts are provided with gd, gdFontTiny, gdFontSmall,
                gdFontMediumBold, gdFontLarge, and gdFontGiant. You must
                include the files "gdfontt.h", "gdfonts.h", "gdfontmb.h",
                "gdfontl.h" and "gdfontg.h" respectively and (if you are
                not using a library-based approach) link with the
                corresponding .c files to use the provided fonts. The
                character specified by the fifth argument is drawn from
                bottom to top, rotated at a 90-degree angle, in the
                specified color. (See gdImageChar for a way of drawing
                horizontal text.) Pixels not set by a particular
                character retain their previous color.
                

#include "gd.h"
#include "gdfontl.h"
... inside a function ...
gdImagePtr im;
int black;
int white;
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Draw a character upwards so it rests against the top of the image. */
gdImageCharUp(im, gdFontLarge,
        0, gdFontLarge->h, 'Q', white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

        void gdImageString(gdImagePtr im, gdFontPtr font, int x, int y,
                unsigned char *s, int color) _(FUNCTION)_
                gdImageString is used to draw multiple characters on the
                image. (To draw single characters, use gdImageChar.) The
                second argument is a pointer to a font definition
                structure; five fonts are provided with gd, gdFontTiny,
                gdFontSmall, gdFontMediumBold, gdFontLarge, and
                gdFontGiant. You must include the files "gdfontt.h",
                "gdfonts.h", "gdfontmb.h", "gdfontl.h" and "gdfontg.h"
                respectively and (if you are not using a library-based
                approach) link with the corresponding .c files to use the
                provided fonts. The null-terminated C string specified by
                the fifth argument is drawn from left to right in the
                specified color. (See gdImageStringUp for a way of
                drawing vertical text. See also gdImageStringTTF, new
                with gd-1.6.2.) Pixels not set by a particular character
                retain their previous color.
                

#include "gd.h"
#include "gdfontl.h"
#include <string.h>
... inside a function ...
gdImagePtr im;
int black;
int white;
/* String to draw. */
char *s = "Hello.";
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Draw a centered string. */
gdImageString(im, gdFontLarge,
        im->w / 2 - (strlen(s) * gdFontLarge->w / 2),
        im->h / 2 - gdFontLarge->h / 2,
        s, white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

        void gdImageString16(gdImagePtr im, gdFontPtr font, int x, int y,
                unsigned short *s, int color) _(FUNCTION)_
                gdImageString is used to draw multiple 16-bit characters
                on the image. (To draw single characters, use
                gdImageChar.) The second argument is a pointer to a font
                definition structure; five fonts are provided with gd,
                gdFontTiny, gdFontSmall, gdFontMediumBold, gdFontLarge,
                and gdFontGiant. You must include the files "gdfontt.h",
                "gdfonts.h", "gdfontmb.h", "gdfontl.h" and "gdfontg.h"
                respectively and (if you are not using a library-based
                approach) link with the corresponding .c files to use the
                provided fonts. The null-terminated string of characters
                represented as 16-bit unsigned short integers specified
                by the fifth argument is drawn from left to right in the
                specified color. (See gdImageStringUp16 for a way of
                drawing vertical text.) Pixels not set by a particular
                character retain their previous color.
                
                This function was added in gd1.3 to provide a means of
                rendering fonts with more than 256 characters for those
                who have them. A more frequently used routine is
                gdImageString.
                
        void gdImageStringUp(gdImagePtr im, gdFontPtr font, int x, int y,
                unsigned char *s, int color) _(FUNCTION)_
                gdImageStringUp is used to draw multiple characters on
                the image, rotated 90 degrees. (To draw single
                characters, use gdImageCharUp.) The second argument is a
                pointer to a font definition structure; five fonts are
                provided with gd, gdFontTiny, gdFontSmall,
                gdFontMediumBold, gdFontLarge, and gdFontGiant. You must
                include the files "gdfontt.h", "gdfonts.h", "gdfontmb.h",
                "gdfontl.h" and "gdfontg.h" respectively and (if you are
                not using a library-based approach) link with the
                corresponding .c files to use the provided fonts.The
                null-terminated C string specified by the fifth argument
                is drawn from bottom to top (rotated 90 degrees) in the
                specified color. (See gdImageString for a way of drawing
                horizontal text.) Pixels not set by a particular
                character retain their previous color.
                

#include "gd.h"
#include "gdfontl.h"
#include <string.h>
... inside a function ...
gdImagePtr im;
int black;
int white;
/* String to draw. */
char *s = "Hello.";
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color white (red, green and blue all maximum). */
white = gdImageColorAllocate(im, 255, 255, 255);
/* Draw a centered string going upwards. Axes are reversed,
        and Y axis is decreasing as the string is drawn. */
gdImageStringUp(im, gdFontLarge,
        im->w / 2 - gdFontLarge->h / 2,
        im->h / 2 + (strlen(s) * gdFontLarge->w / 2),
        s, white);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

        void gdImageStringUp16(gdImagePtr im, gdFontPtr font, int x, int
                y, unsigned short *s, int color) _(FUNCTION)_
                gdImageString is used to draw multiple 16-bit characters
                vertically on the image. (To draw single characters, use
                gdImageChar.) The second argument is a pointer to a font
                definition structure; five fonts are provided with gd,
                gdFontTiny, gdFontSmall, gdFontMediumBold, gdFontLarge,
                and gdFontGiant. You must include the files "gdfontt.h",
                "gdfonts.h", "gdfontmb.h", "gdfontl.h" and "gdfontg.h"
                respectively and (if you are not using a library-based
                approach) link with the corresponding .c files to use the
                provided fonts. The null-terminated string of characters
                represented as 16-bit unsigned short integers specified
                by the fifth argument is drawn from bottom to top in the
                specified color. (See gdImageStringUp16 for a way of
                drawing horizontal text.) Pixels not set by a particular
                character retain their previous color.
                
                This function was added in gd1.3 to provide a means of
                rendering fonts with more than 256 characters for those
                who have them. A more frequently used routine is
                gdImageStringUp.
                
        char *gdImageStringTTF(gdImagePtr im, int *brect, int fg, char
                *fontname, double ptsize, double angle, int x, int y,
                char *string) _(FUNCTION)_
                gdImageStringTTF is draws a string of anti-aliased
                characters on the image using the FreeType library to
                print from user-supplied TrueType fonts. _We do not
                provide TrueType fonts. Obtaining them is entirely up to
                you._ The string is anti-aliased, meaning that there
                should be less "jaggies." The fontname is the full
                pathname to a TrueType font file. The string may be
                arbitrarily scaled (ptsize) and rotated (angle in
                radians).
                
                The user-supplied int brect[8] array is filled on return
                from gdImageStringTTF with the 8 elements representing
                the 4 corner coordinates of the bounding rectangle.
                0 lower left corner, X position
                lower left corner, Y position
                lower right corner, X position
                3 lower right corner, Y position
                4 upper right corner, X position
                5 upper right corner, Y position
                6 upper left corner, X position
                7 upper left corner, Y position
                
                The points are relative to the text regardless of the
                angle, so "upper left" means in the top left-hand corner
                seeing the text horizontally.
                
                Use a NULL gdImagePtr to get the bounding rectangle
                without rendering. This is a relatively cheap operation
                if followed by a rendering of the same string, because of
                the caching of the partial rendering during bounding
                rectangle calculation.
                
                The string is rendered in the color indicated by the gf
                color index. Use the negative of the desired color index
                to disable anti-aliasing.
                
                The string may contain UTF-8 sequences like: "&#192;"
                
                gdImageStringTTF will return a null char* on success, or
                an error string on failure.
                

#include "gd.h"
#include <string.h>
... inside a function ...
gdImagePtr im;
int black;
int white;
int brect[8];
int x, y;
char *err;

char *s = "Hello."; /* String to draw. */
double sz = 40.;
char *f = "/usr/local/share/ttf/Times.ttf";  /* User supplied font */

/* obtain brect so that we can size the image */
err = gdImageStringTTF(NULL,&brect[0],0,f,sz,0.,0,0,s);
if (err) {fprintf(stderr,err); return 1;}

/* create an image big enough for the string plus a little whitespace */
x = brect[2]-brect[6] + 6;
y = brect[3]-brect[7] + 6;
im = gdImageCreate(x,y);

/* Background color (first allocated) */
white = gdImageColorResolve(im, 255, 255, 255);
black = gdImageColorResolve(im, 0, 0, 0);

/* render the string, offset origin to center string*/
/* note that we use top-left coordinate for adjustment
 * since gd origin is in top-left with y increasing downwards. */
x = 3 - brect[6];
y = 3 - brect[7];
err = gdImageStringTTF(im,&brect[0],black,f,sz,0.0,x,y,s);
if (err) {fprintf(stderr,err); return 1;}

/* Write img to stdout */
gdImagePng(im, stdout);

/* Destroy it */
gdImageDestroy(im);

  Color-handling functions
  
        int gdImageColorAllocate(gdImagePtr im, int r, int g, int b)
                _(FUNCTION)_
                gdImageColorAllocate finds the first available color
                index in the image specified, sets its RGB values to
                those requested (255 is the maximum for each), and
                returns the index of the new color table entry. When
                creating a new image, the first time you invoke this
                function, you are setting the background color for that
                image.
                
                In the event that all gdMaxColors colors (256) have
                already been allocated, gdImageColorAllocate will return
                -1 to indicate failure. (This is not uncommon when
                working with existing PNG files that already use 256
                colors.) Note that gdImageColorAllocate does not check
                for existing colors that match your request; see
                gdImageColorExact and gdImageColorClosest for ways to
                locate existing colors that approximate the color desired
                in situations where a new color is not available. Also
                see gdImageColorResolve, new in gd-1.6.2.
                

... inside a function ...
gdImagePtr im;
int black;
int red;
im = gdImageCreate(100, 100);
/* Background color (first allocated) */
black = gdImageColorAllocate(im, 0, 0, 0);
/* Allocate the color red. */
red = gdImageColorAllocate(im, 255, 0, 0);
/* Draw a dashed line from the upper left corner to the lower right corner. */
gdImageDashedLine(im, 0, 0, 99, 99, red);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

        int gdImageColorClosest(gdImagePtr im, int r, int g, int b)
                _(FUNCTION)_
                gdImageColorClosest searches the colors which have been
                defined thus far in the image specified and returns the
                index of the color with RGB values closest to those of
                the request. (Closeness is determined by Euclidian
                distance, which is used to determine the distance in
                three-dimensional color space between colors.)
                
                If no colors have yet been allocated in the image,
                gdImageColorClosest returns -1.
                
                This function is most useful as a backup method for
                choosing a drawing color when an image already contains
                gdMaxColors (256) colors and no more can be allocated.
                (This is not uncommon when working with existing PNG
                files that already use many colors.) See
                gdImageColorExact for a method of locating exact matches
                only.
                

... inside a function ...
gdImagePtr im;
FILE *in;
int red;
/* Let's suppose that photo.png is a scanned photograph with
        many colors. */
in = fopen("photo.png", "rb");
im = gdImageCreateFromPng(in);
fclose(in);
/* Try to allocate red directly */
red = gdImageColorAllocate(im, 255, 0, 0);
/* If we fail to allocate red... */
if (red == (-1)) {
        /* Find the _closest_ color instead. */
        red = gdImageColorClosest(im, 255, 0, 0);
}
/* Draw a dashed line from the upper left corner to the lower right corner */
gdImageDashedLine(im, 0, 0, 99, 99, red);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

        int gdImageColorExact(gdImagePtr im, int r, int g, int b)
                _(FUNCTION)_
                gdImageColorExact searches the colors which have been
                defined thus far in the image specified and returns the
                index of the first color with RGB values which exactly
                match those of the request. If no allocated color matches
                the request precisely, gdImageColorExact returns -1. See
                gdImageColorClosest for a way to find the color closest
                to the color requested.
                

... inside a function ...
gdImagePtr im;
int red;
in = fopen("photo.png", "rb");
im = gdImageCreateFromPng(in);
fclose(in);
/* The image may already contain red; if it does, we'll save a slot
        in the color table by using that color. */
/* Try to allocate red directly */
red = gdImageColorExact(im, 255, 0, 0);
/* If red isn't already present... */
if (red == (-1)) {
        /* Second best: try to allocate it directly. */
        red = gdImageColorAllocate(im, 255, 0, 0);
        /* Out of colors, so find the _closest_ color instead. */
        red = gdImageColorClosest(im, 255, 0, 0);
}
/* Draw a dashed line from the upper left corner to the lower right corner */
gdImageDashedLine(im, 0, 0, 99, 99, red);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

        int gdImageColorResolve(gdImagePtr im, int r, int g, int b)
                _(FUNCTION)_
                gdImageColorResolve searches the colors which have been
                defined thus far in the image specified and returns the
                index of the first color with RGB values which exactly
                match those of the request. If no allocated color matches
                the request precisely, then gdImageColorResolve tries to
                allocate the exact color. If there is no space left in
                the color table then gdImageColorResolve returns the
                closest color (as in gdImageColorClosest). This function
                always returns an index of a color.
                

... inside a function ...
gdImagePtr im;
int red;
in = fopen("photo.png", "rb");
im = gdImageCreateFromPng(in);
fclose(in);
/* The image may already contain red; if it does, we'll save a slot
        in the color table by using that color. */
/* Get index of red, or color closest to red */
red = gdImageColorResolve(im, 255, 0, 0);
/* Draw a dashed line from the upper left corner to the lower right corner */
gdImageDashedLine(im, 0, 0, 99, 99, red);
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

        int gdImageColorsTotal(gdImagePtr im) _(MACRO)_
                gdImageColorsTotal is a macro which returns the number of
                colors currently allocated in the image. Use this macro
                to obtain this information; do not access the structure
                directly.
                
        int gdImageColorRed(gdImagePtr im, int c) _(MACRO)_
                gdImageColorRed is a macro which returns the red portion
                of the specified color in the image. Use this macro to
                obtain this information; do not access the structure
                directly.
                
        int gdImageColorGreen(gdImagePtr im, int c) _(MACRO)_
                gdImageColorGreen is a macro which returns the green
                portion of the specified color in the image. Use this
                macro to obtain this information; do not access the
                structure directly.
                
        int gdImageColorBlue(gdImagePtr im, int c) _(MACRO)_
                gdImageColorBlue is a macro which returns the green
                portion of the specified color in the image. Use this
                macro to obtain this information; do not access the
                structure directly.
                
        int gdImageGetInterlaced(gdImagePtr im) _(MACRO)_
                gdImageGetInterlaced is a macro which returns true (1) if
                the image is interlaced, false (0) if not. Use this macro
                to obtain this information; do not access the structure
                directly. See gdImageInterlace for a means of interlacing
                images.
                
        int gdImageGetTransparent(gdImagePtr im) _(MACRO)_
                gdImageGetTransparent is a macro which returns the
                current transparent color index in the image. If there is
                no transparent color, gdImageGetTransparent returns -1.
                Use this macro to obtain this information; do not access
                the structure directly.
                
        void gdImageColorDeallocate(gdImagePtr im, int color) _(FUNCTION)_
                
                gdImageColorDeallocate marks the specified color as being
                available for reuse. It does not attempt to determine
                whether the color index is still in use in the image.
                After a call to this function, the next call to
                gdImageColorAllocate for the same image will set new RGB
                values for that color index, changing the color of any
                pixels which have that index as a result. If multiple
                calls to gdImageColorDeallocate are made consecutively,
                the lowest-numbered index among them will be reused by
                the next gdImageColorAllocate call.
                

... inside a function ...
gdImagePtr im;
int red, blue;
in = fopen("photo.png", "rb");
im = gdImageCreateFromPng(in);
fclose(in);
/* Look for red in the color table. */
red = gdImageColorExact(im, 255, 0, 0);
/* If red is present... */
if (red != (-1)) {
        /* Deallocate it. */
        gdImageColorDeallocate(im, red);
        /* Allocate blue, reusing slot in table.
                Existing red pixels will change color. */
        blue = gdImageColorAllocate(im, 0, 0, 255);
}
/* ... Do something with the image, such as saving it to a file... */
/* Destroy it */
gdImageDestroy(im);

        void gdImageColorTransparent(gdImagePtr im, int color)
                _(FUNCTION)_
                gdImageColorTransparent sets the transparent color index
                for the specified image to the specified index. To
                indicate that there should be _no_ transparent color,
                invoke gdImageColorTransparent with a color index of -1.
                
                The color index used should be an index allocated by
                gdImageColorAllocate, whether explicitly invoked by your
                code or implicitly invoked by loading an image. In order
                to ensure that your image has a reasonable appearance
                when viewed by users who do not have transparent
                background capabilities, be sure to give reasonable RGB
                values to the color you allocate for use as a transparent
                color, _even though it will be transparent on systems
                that support transparency_.
                

... inside a function ...
gdImagePtr im;
int black;
FILE *in, *out;
in = fopen("photo.png", "rb");
im = gdImageCreateFromPng(in);
fclose(in);
/* Look for black in the color table and make it transparent. */
black = gdImageColorExact(im, 0, 0, 0);
/* If black is present... */
if (black != (-1)) {
        /* Make it transparent */
        gdImageColorTransparent(im, black);
}
/* Save the newly-transparent image back to the file */
out = fopen("photo.png", "wb");
gdImagePng(im, out);
fclose(out);
/* Destroy it */
gdImageDestroy(im);

  Copying and resizing functions
  
        void gdImageCopy(gdImagePtr dst, gdImagePtr src, int dstX, int
                dstY, int srcX, int srcY, int w, int h) _(FUNCTION)_
                gdImageCopy is used to copy a rectangular portion of one
                image to another image. (For a way of stretching or
                shrinking the image in the process, see
                gdImageCopyResized.)
                
                The dst argument is the destination image to which the
                region will be copied. The src argument is the source
                image from which the region is copied. The dstX and dstY
                arguments specify the point in the destination image to
                which the region will be copied. The srcX and srcY
                arguments specify the upper left corner of the region in
                the source image. The w and h arguments specify the width
                and height of the region.
                
                When you copy a region from one location in an image to
                another location in the same image, gdImageCopy will
                perform as expected unless the regions overlap, in which
                case the result is unpredictable.
                
                _Important note on copying between images:_ since
                different images do not necessarily have the same color
                tables, pixels are not simply set to the same color index
                values to copy them. gdImageCopy will attempt to find an
                identical RGB value in the destination image for each
                pixel in the copied portion of the source image by
                invoking gdImageColorExact. If such a value is not found,
                gdImageCopy will attempt to allocate colors as needed
                using gdImageColorAllocate. If both of these methods
                fail, gdImageCopy will invoke gdImageColorClosest to find
                the color in the destination image which most closely
                approximates the color of the pixel being copied.
                

... Inside a function ...
gdImagePtr im_in;
gdImagePtr im_out;
int x, y;
FILE *in;
FILE *out;
/* Load a small png to tile the larger one with */
in = fopen("small.png", "rb");
im_in = gdImageCreateFromPng(in);
fclose(in);
/* Make the output image four times as large on both axes */
im_out = gdImageCreate(im_in->sx * 4, im_in->sy * 4);
/* Now tile the larger image using the smaller one */
for (y = 0; (y < 4); y++) {
        for (x = 0; (x < 4); x++) {
                gdImageCopy(im_out, im_in,
                        x * im_in->sx, y * im_in->sy,
                        0, 0,
                        im_in->sx, im_in->sy);
        }
}
out = fopen("tiled.png", "wb");
gdImagePng(im_out, out);
fclose(out);
gdImageDestroy(im_in);
gdImageDestroy(im_out);

        void gdImageCopyResized(gdImagePtr dst, gdImagePtr src, int dstX,
                int dstY, int srcX, int srcY, int destW, int destH, int
                srcW, int srcH) _(FUNCTION)_
                gdImageCopyResized is used to copy a rectangular portion
                of one image to another image. The X and Y dimensions of
                the original region and the destination region can vary,
                resulting in stretching or shrinking of the region as
                appropriate. (For a simpler version of this function
                which does not deal with resizing, see gdImageCopy.)
                
                The dst argument is the destination image to which the
                region will be copied. The src argument is the source
                image from which the region is copied. The dstX and dstY
                arguments specify the point in the destination image to
                which the region will be copied. The srcX and srcY
                arguments specify the upper left corner of the region in
                the source image. The dstW and dstH arguments specify the
                width and height of the destination region. The srcW and
                srcH arguments specify the width and height of the source
                region and can differ from the destination size, allowing
                a region to be scaled during the copying process.
                
                When you copy a region from one location in an image to
                another location in the same image, gdImageCopy will
                perform as expected unless the regions overlap, in which
                case the result is unpredictable. If this presents a
                problem, create a scratch image in which to keep
                intermediate results.
                
                _Important note on copying between images:_ since images
                do not necessarily have the same color tables, pixels are
                not simply set to the same color index values to copy
                them. gdImageCopy will attempt to find an identical RGB
                value in the destination image for each pixel in the
                copied portion of the source image by invoking
                gdImageColorExact. If such a value is not found,
                gdImageCopy will attempt to allocate colors as needed
                using gdImageColorAllocate. If both of these methods
                fail, gdImageCopy will invoke gdImageColorClosest to find
                the color in the destination image which most closely
                approximates the color of the pixel being copied.
                

... Inside a function ...
gdImagePtr im_in;
gdImagePtr im_out;
int x, y;
FILE *in;
FILE *out;
/* Load a small png to expand in the larger one */
in = fopen("small.png", "rb");
im_in = gdImageCreateFromPng(in);
fclose(in);
/* Make the output image four times as large on both axes */
im_out = gdImageCreate(im_in->sx * 4, im_in->sy * 4);
/* Now copy the smaller image, but four times larger */
gdImageCopyResized(im_out, im_in, 0, 0, 0, 0,
        im_out->sx, im_out->sy,
        im_in->sx, im_in->sy);
out = fopen("large.png", "wb");
gdImagePng(im_out, out);
fclose(out);
gdImageDestroy(im_in);
gdImageDestroy(im_out);

        void gdImageCopyMerge(gdImagePtr dst, gdImagePtr src, int dstX,
                int dstY, int srcX, int srcY, int w, int h, int pct)
                _(FUNCTION)_
                gdImageCopyMerge is almost identical to gdImageCopy,
                except that it 'merges' the two images by an amount
                specified in the last parameter. If the last parameter is
                100, then it will function identically to gdImageCopy -
                the source image replaces the pixels in the destination.
                
                If, however, the _pct_ parameter is less than 100, then
                the two images are merged. With pct = 0, no action is
                taken.
                
                This feature is most useful to 'highlight' sections of an
                image by merging a solid color with pct = 50:
                

... Inside a function ...
gdImageCopyMerge(im_out, im_in, 100, 200, 0, 0, 30, 50, 50);

        void gdImageCopyMergeGray(gdImagePtr dst, gdImagePtr src, int
                dstX, int dstY, int srcX, int srcY, int w, int h, int
                pct) _(FUNCTION)_
                gdImageCopyMergeGray is almost identical to
                gdImageCopyMerge, except that when merging images it
                preserves the hue of the source by converting the
                destination pixels to grey scale before the copy
                operation.
                

... Inside a function ...
gdImageCopyMergeGray(im_out, im_in, 100, 200, 0, 0, 30, 50, 50);

        void gdImagePaletteCopy(gdImagePtr dst, gdImagePtr src)
                _(FUNCTION)_
                Copies a palette from one image to another, doing it's
                best to match the colors in the target image to the
                colors in the source palette.
                
  Miscellaneous Functions
  
              int gdImageCompare(gdImagePtr im1, gdImagePtr im2)
                      _(FUNCTION)_
                      gdImageCompare returns a bitmap indicating if the
                      two images are different. The members of the bitmap
                      are defined in gd.h, but the most important is
                      GD_CMP_IMAGE, which indicated that the images will
                      actually appear different when displayed. Other,
                      less important, differences relate to pallette
                      entries. Any difference in the transparent colour
                      is assumed to make images display differently, even
                      if the transparent colour is not used.
                      

... Inside a function ...
cmpMask = gdImageCompare(im1, im2);

              gdImageInterlace(gdImagePtr im, int interlace) _(FUNCTION)_
                      
                      gdImageInterlace is used to determine whether an
                      image should be stored in a linear fashion, in
                      which lines will appear on the display from first
                      to last, or in an interlaced fashion, in which the
                      image will "fade in" over several passes. By
                      default, images are not interlaced.
                      
                      A nonzero value for the interlace argument turns on
                      interlace; a zero value turns it off. Note that
                      interlace has no effect on other functions, and has
                      no meaning unless you save the image in PNG format;
                      the gd and xbm formats do not support interlace.
                      
                      When a PNG is loaded with gdImageCreateFromPng ,
                      interlace will be set according to the setting in
                      the PNG file.
                      
                      Note that many PNG viewers and web browsers do _not_
                      support interlace. However, the interlaced PNG
                      should still display; it will simply appear all at
                      once, just as other images do.
                      

gdImagePtr im;
FILE *out;
/* ... Create or load the image... */

/* Now turn on interlace */
gdImageInterlace(im, 1);
/* And open an output file */
out = fopen("test.png", "wb");
/* And save the image */
gdImagePng(im, out);
fclose(out);
gdImageDestroy(im);

  Constants
  
                    gdBrushed _(CONSTANT)_
                            Used in place of a color when invoking a
                            line-drawing function such as gdImageLine or
                            gdImageRectangle. When gdBrushed is used as
                            the color, the brush image set with
                            gdImageSetBrush is drawn in place of each
                            pixel of the line (the brush is usually
                            larger than one pixel, creating the effect of
                            a wide paintbrush). See also gdStyledBrushed
                            for a way to draw broken lines with a series
                            of distinct copies of an image.
                            
                    gdMaxColors_(CONSTANT)_
                            The constant 256. This is the maximum number
                            of colors in a PNG file according to the PNG
                            standard, and is also the maximum number of
                            colors in a gd image.
                            
                    gdStyled _(CONSTANT)_
                            Used in place of a color when invoking a
                            line-drawing function such as gdImageLine or
                            gdImageRectangle. When gdStyled is used as
                            the color, the colors of the pixels are drawn
                            successively from the style that has been set
                            with gdImageSetStyle. If the color of a pixel
                            is equal to gdTransparent, that pixel is not
                            altered. (This mechanism is completely
                            unrelated to the "transparent color" of the
                            image itself; see gdImageColorTransparent
                            gdImageColorTransparent for that mechanism.)
                            See also gdStyledBrushed.
                            
                    gdStyledBrushed _(CONSTANT)_
                            Used in place of a color when invoking a
                            line-drawing function such as gdImageLine or
                            gdImageRectangle. When gdStyledBrushed is
                            used as the color, the brush image set with
                            gdImageSetBrush is drawn at each pixel of the
                            line, providing that the style set with
                            gdImageSetStyle contains a nonzero value (OR
                            gdTransparent, which does not equal zero but
                            is supported for consistency) for the current
                            pixel. (Pixels are drawn successively from
                            the style as the line is drawn, returning to
                            the beginning when the available pixels in
                            the style are exhausted.) Note that this
                            differs from the behavior of gdStyled, in
                            which the values in the style are used as
                            actual pixel colors, except for
                            gdTransparent.
                            
                    gdDashSize _(CONSTANT)_
                            The length of a dash in a dashed line.
                            Defined to be 4 for backwards compatibility
                            with programs that use gdImageDashedLine. New
                            programs should use gdImageSetStyle and call
                            the standard gdImageLine function with the
                            special "color" gdStyled or gdStyledBrushed.
                            
                    gdTiled _(CONSTANT)_
                            Used in place of a normal color in
                            gdImageFilledRectangle, gdImageFilledPolygon,
                            gdImageFill, and gdImageFillToBorder. gdTiled
                            selects a pixel from the tile image set with
                            gdImageSetTile in such a way as to ensure
                            that the filled area will be tiled with
                            copies of the tile image. See the discussions
                            of gdImageFill and gdImageFillToBorder for
                            special restrictions regarding those
                            functions.
                            
                    gdTransparent _(CONSTANT)_
                            Used in place of a normal color in a style to
                            be set with gdImageSetStyle. gdTransparent is
                            _not_ the transparent color index of the
                            image; for that functionality please see
                            gdImageColorTransparent.
                            
  About the additional .gd image file format
  
                            In addition to reading and writing the PNG
                            format and reading the X Bitmap format, gd
                            has the capability to read and write its own
                            ".gd" format. This format is _not_ intended
                            for general purpose use and should never be
                            used to distribute images. It is not a
                            compressed format. Its purpose is solely to
                            allow very fast loading of images your
                            program needs often in order to build other
                            images for output. If you are experiencing
                            performance problems when loading large,
                            fixed PNG images your program needs to
                            produce its output images, you may wish to
                            examine the functions gdImageCreateFromGd and
                            gdImageGd, which read and write .gd format
                            images.
                            
                            The program "pngtogd.c" is provided as a
                            simple way of converting .png files to .gd
                            format. I emphasize again that you will not
                            need to use this format unless you have a
                            need for high-speed loading of a few
                            frequently-used images in your program.
                            
  About the .gd2 image file format
  
                            In addition to reading and writing the PNG
                            format and reading the X Bitmap format, gd
                            has the capability to read and write its own
                            ".gd2" format. This format is _not_ intended
                            for general purpose use and should never be
                            used to distribute images. It is a compressed
                            format allowing pseudo-random access to large
                            image files. Its purpose is solely to allow
                            very fast loading of _parts_ of images If you
                            are experiencing performance problems when
                            loading large, fixed PNG images your program
                            needs to produce its output images, you may
                            wish to examine the functions
                            gdImageCreateFromGd2,
                            gdImageCreateFromGd2Part and gdImageGd2,
                            which read and write .gd2 format images.
                            
                            The program "pngtogd2.c" is provided as a
                            simple way of converting .png files to .gd2
                            format.
                            
  About the gdIOCtx structure
  
                            Version 1.5 of GD added a new style of I/O
                            based on an IOCtx structure (the most
                            up-to-date version can be found in gd_io.h):
                            

typedef struct gdIOCtx {
        int     (*getC)(struct gdIOCtx*);
        int     (*getBuf)(struct gdIOCtx*, void*, int);

        void     (*putC)(struct gdIOCtx*, int);
        int     (*putBuf)(struct gdIOCtx*, const void*, int);

        int     (*seek)(struct gdIOCtx*, const int);
        long    (*tell)(struct gdIOCtx*);

        void    (*free)(struct gdIOCtx*);

} gdIOCtx;

                    Most functions that accepted files in previous
                            versions now also have a counterpart that
                            accepts an I/O context. These functions have
                            a 'Ctx' suffix.
                            
                            The Ctx routines use the function pointers in
                            the I/O context pointed to by gdIOCtx to
                            perform all I/O. Examples of how to implement
                            an I/O context can be found in io_file.c
                            (which provides a wrapper for file routines),
                            and io_dp.c (which implements in-memory
                            storage).
                            
                            It is not necessary to implement all
                            functions in an I/O context if you know that
                            it will only be used in limited
                            cirsumstances. At the time of writing
                            (Version 1.6.1, July 1999), the known
                            requirements are:
                            
                            All   Must have 'free',
                            Anything that reads from the context Must
                            have 'getC' and 'getBuf',
                            Anything that writes to the context Must have
                            'putC' and 'putBuf'.
                            If gdCreateFromGd2Part is called Must also
                            have 'seek' and 'tell'.
                            If gdImageGd2 is called Must also have 'seek'
                            and 'tell'.
                            
  Please tell us you're using gd!
  
                            When you contact us and let us know you are
                            using gd, you help us justify the time spent
                            in maintaining and improving it. So please
                            let us know. If the results are publicly
                            visible on the web, a URL is a wonderful
                            thing to receive, but if it's not a publicly
                            visible project, a simple note is just as
                            welcome.
                            
  If you have problems
  
                            If you have any difficulties with gd, feel
                            free to contact the author, Thomas Boutell.
                            Problems relating to the gd2 format should be
                            addressed to Philip Warner.
                            
                            _Be sure to read this manual carefully first.
                            _
  Alphabetical quick index
  
                            gdBrushed | gdDashSize | gdFont | gdFontPtr |
                            gdImage | gdImageArc | gdImageBlue |
                            gdImageBoundsSafe | gdImageChar |
                            gdImageCharUp | gdImageColorAllocate |
                            gdImageColorClosest | gdImageColorDeallocate
                            | gdImageColorExact | gdImageColorResolve |
                            gdImageColorTransparent | gdImageCopy |
                            gdImageCopyResized | gdImageCreate |
                            gdImageCreateFromGd | gdImageCreateFromGd2 |
                            gdImageCreateFromGd2Part |
                            gdImageCreateFromPng |
                            gdImageCreateFromPngSource |
                            gdImageCreateFromXbm | gdImageCreateFromXpm |
                            gdImageDashedLine | gdImageDestroy |
                            gdImageFill | gdImageFillToBorder |
                            gdImageFilledRectangle | gdImageGd |
                            gdImageGd2 | gdImageGetInterlaced |
                            gdImageGetPixel | gdImageGetTransparent |
                            gdImageGreen | gdImageInterlace | gdImageLine
                            | gdImageFilledPolygon | gdImagePaletteCopy |
                            gdImagePng | gdImagePngToSink |
                            gdImagePolygon | gdImagePtr |
                            gdImageRectangle | gdImageRed |
                            gdImageSetBrush | gdImageSetPixel |
                            gdImageSetStyle | gdImageSetTile |
                            gdImageString | gdImageString16 |
                            gdImageStringTTF | gdImageStringUp |
                            gdImageStringUp16 | gdMaxColors | gdPoint |
                            gdStyled | gdStyledBrushed | gdTiled |
                            gdTransparent
                            
                            _Boutell.Com, Inc._
All components in the "contrib" cluster are not supported. Although shipped
with Vision2, the cluster is provided to provide a convenient place for useful
additions by users for users. If you have some classes that you feel would be suited for
inclusion in this cluster, then please send details to http://support.eiffel.com and
submit as a change request.{\rtf1\ansi\ansicpg1252\deff0\deftab720{\fonttbl{\f0\fswiss MS Sans Serif;}{\f1\froman\fcharset2 Symbol;}{\f2\fmodern\fprq1 Courier New;}{\f3\froman Times New Roman;}{\f4\fmodern\fprq1 Lucida Console;}}
{\colortbl\red0\green0\blue0;}
\deflang1033\horzdoc{\*\fchars }{\*\lchars }\pard\tx2610\plain\f2\fs20\b\i File:\plain\f2\fs20\i \tab \plain\f2\fs20 README
\par \plain\f2\fs20\b\i Copyright (C):\plain\f2\fs20 \tab 2001, 2002  Earnie Boyd  <earnie@users.sf.net>
\par \plain\f2\fs20\b\i Distribution:\plain\f2\fs20 \tab See MSYS_LICENSE
\par \plain\f2\fs20\b\i MSYS Revision:\plain\f2\fs20 \tab 1.0.10
\par \plain\f2\fs20\b\i MSYS Revision date:\plain\f2\fs20\i \tab \plain\lang1024\f2\fs20 October 31, 2002\plain\f2\fs20 
\par \pard\qc\tx2610\plain\f2\fs20\i 
\par \pard\plain\f2\fs20\b\i Preface:\plain\f2\fs20 
\par Ok, you have installed msys and now you're reading this to understand how to get started.  However, I must first explain some important facts about Msys.  Msys file system bindings (mounts) are automatic and happens as described in table 1.  These automatic file system bindings are not changable by the user.  User defined file system bindings can be created by specifying them in the /etc/fstab directory as explained in table 2.
\par 
\par \plain\f2\fs20\b\i TABLE 1 - Automatic file system maps:\plain\f2\fs20 
\par \plain\f4\fs16 + ---------------------------------------------------------------------------- +
\par | The automatic mounts are relative to where the msys-1.0.dll (DLL) is located |
\par | such that the following is true:                                             |
\par |                                                                              |
\par | / - is the parent directory of the directory containing the DLL              |
\par | /bin - the direcotry containing the DLL                                      |
\par | /usr - the parent directory of the directory containing the DLL              |
\par | /usr/bin - the directory containing the DLL                                  |
\par | /tmp - the value of the TMP environment variable                             |
\par | /c - C:\\                                                                     |
\par | /d - D:\\                                                                     |
\par | . . .                                                                        |
\par | /z - Z:\\                                                                     |
\par |                                                                              |
\par + ---------------------------------------------------------------------------- +
\par \plain\f2\fs20 
\par \plain\f2\fs20\b\i TABLE 2 - /etc/fstab layout:\plain\f2\fs20 
\par \plain\f4\fs16 + ---------------------------------------------------------------------------- +
\par | The record format for the /etc/fstab is current a simple one.  I need to     |
\par | work on the syntax parsing more so that things like embedded spaces work.    |
\par | If you wish to map a path with spaces you must use the DOS style name.       |
\par |                                                                              |
\par | The record format is as follows:                                             |
\par | d:/some/foo/path /bar                                                        |
\par |                                                                              |
\par | As you can see this is simply the Win32 path mapped to a mount point.  It is |
\par | unix practice to have the /bar created as an empty directory before it can   |
\par | mount the mount point.  Msys doesn't force this but it will be to advantage  |
\par | if you do.  Some programs, e.g. find, and some operations, e.g. tab          |
\par | operate better if the physical directory is present for those mount points.  |
\par |                                                                              |
\par | If you create a /etc/fstab record that maps to an automatic mount point Msys |
\par | will remove it when it adds the automatic point.  This means that at some    |
\par | small moment in time your mount point actually exists.  However it doesn't   |
\par | exist long enough to be of any use to you.                                   |
\par |                                                                              |
\par + ---------------------------------------------------------------------------- +
\par \plain\f2\fs20 
\par Msys will convert POSIX paths that are used as arguments to Win32 paths.  This is done for any executable not in /bin and /usr/bin.  If the executable is dependant on the msys-1.0.dll then it must be located in the /bin or /usr/bin directory.  This means that you now have a POSIX environment that will automagically do the right thing w.r.t. changing the paths passed as arguments.  Arguments beginning with a // are considered to be Win32 style switches and will be passed to the program with // converted to / to allow for the command.com/cmd.exe (Win32) style switch.  An example of a Win32 style switch is `write //p /mydocs/msys-rocks.'  In this example write (a.k.a. WordPad) exists in the c:\\winnt\\system32 path on my system.  The //p becomes /p which tells write to print the document.  And mydocs/msys-rocks converts to c:\\msys\\1.0\\mydocs\\msys-rocks so that write can find it.  
\par \plain\f2\fs20\b\i 
\par STARTING Msys:
\par \plain\f2\fs20 Starting Msys should just be a matter of clicking on the MSYS icon on your desktop or Start menu.  If you have the File Manager window open, you may now click on it and have it start also.  Doing these presents you with a console window within which you may enter commands.
\par 
\par \plain\f2\fs20\b\i Working with MinGW:
\par \plain\f2\fs20 If you already have MinGW installed then simply bind the path to MinGW to the /mingw mount point in the /etc/fstab as described above.  If you don't have MinGW installed already then simply unarchive the MinGW tar.gz file in the /mingw directory.  \plain\f2\fs20\b\ul DO NOT\plain\f2\fs20  unarchive the MinGW tar.gz file in the / directory.
\par \plain\f2\fs20\b\i 
\par Working with other products:
\par \plain\f2\fs20 I find that the easiest thing for working with other products, such as Microsoft Office, is to create a script pointing to the executable.  An example of a script for Microsoft Word on my system looks like the example in Table 3.  I have this stored in my /usr/local/bin directory with a filename of word.  Now all I need to do to edit a word document is `word /mydoc/proposal.doc' and voila up pops a Microsoft Word window with my document in it.
\par 
\par \plain\f2\fs20\b\i Table 3 - Script to execute MS Word from the command line:
\par \plain\f4\fs16 + ---------------------------------------------------------------------------- +
\par + #!/bin/sh                                                                    +
\par + start '/c/Program\\ Files/Microsoft\\ Office/Office/WINWORD' $@                +
\par + ---------------------------------------------------------------------------- +
\par \plain\f2\fs20\b\i 
\par Other documentation:\plain\f2\fs20 
\par Be sure to read the MSYS_ series.  I have tried to document how I'm changing the cygwin code to allow us to use it with MSYS.  These can be found in the /doc/msys directory, or you can find them in the /usr/doc/msys directory.
\par 
\par \plain\f2\fs20\b\i Using binaries with different runtimes:\plain\f2\fs20 
\par You can't use Cygwin binaries at all and if you try you'll most likely just cause the processes to "hang".  You can use Win32 native binaries but you should put them into the /mingw/bin or your /usr/local/bin directory tree.  If you wish to replace an MSYS binary with a native win32 version then delete or rename the /bin version.
\par 
\par \plain\f2\fs20\b\i Effective use of the clipboard:
\par \plain\f2\fs20 You may use the clipboard with MSYS.  When using rxvt (the default installation) as the terminal, just selecting with data with click and drag of the mouse, copies the data to the clipboard.  To paste the clipboard data in the rxvt terminal you can Shift and Left Click or press both mouse buttons if 3 button mouse emulation is on or press the mouse wheel.  To copy the highlighted data to your favorite windows email client the you use the paste options for that program, typically Ctrl-V.  You can also use interesting bash shell commands such as `cat /dev/clipboard > /tmp/foo' or `less -f /dev/clipboard'.  Data entered into the clipboard by non-MSYS programs can also be used by MSYS programs and vice versa.\plain\f2\fs20\b\i 
\par 
\par Bug Reports:\plain\f2\fs20 
\par Send your bug reports to MinGW-msys@lists.sf.net.
\par 
\par \plain\f2\fs20\b\i User Posts:\plain\f2\fs20 
\par MinGW-msys@lists.sf.net
\par 
\par \plain\f2\fs20\b\i Disclaimer:
\par \plain\f2\fs20 Products mentioned in this and other documents are solely owned by their trademark owners.  We claim no rights to those trademarks and any mention of those products are for example only.  Your uses of those products are your responsibility and no endorsement of any mentioned product is being given.
\par 
\par \plain\f2\fs20\b\i Change History:
\par \plain\f2\fs20 Version 1.0.3 added checks for paths following an `=' and `-X' where X
\par is a program switch.
\par 
\par Version 1.0.4 added symlink resolution, removed the dependancy that the pathmust begin with a / and removed bash.exe since sh.exe is bash.exe anyway.  Also added diff, diff3 and head to the distribution.  An MSYS icon exists in the rxvt binary.
\par 
\par Version 1.0.5 is a bug fix release that filters out the conversion of quoted relative paths.  So that -DSOME_CONSTANT=\\"1.0.5\\" can be properly input into gcc.  Also fixed the problem with sh.exe reading /etc/profile with \\r\\n line endings.  Added the binaries true.exe, false.exe, tail.exe and fold.exe.  Updated the gmake binary to the Cygwin version including the --win32 switch.  I am suggesting to use this version of make and have copied /bin/gmake.exe to /bin/make (yes without the .exe).  If you wish to go back to the "native" version of make typing make.exe will get you there.
\par 
\par Version 1.0.6 through current: See the appropriate MSYS-<version>-changes.rtf document.
\par }
 This README file is copied into the directory for GCC-only header files
when fixincludes is run by the makefile for GCC.

Many of the files in this directory were automatically edited from the
standard system header files by the fixincludes process.  They are
system-specific, and will not work on any other kind of system.  They
are also not part of GCC.  The reason we have to do this is because
GCC requires ANSI C headers and many vendors supply ANSI-incompatible
headers.

Because this is an automated process, sometimes headers get "fixed"
that do not, strictly speaking, need a fix.  As long as nothing is broken
by the process, it is just an unfortunate collateral inconvenience.
We would like to rectify it, if it is not "too inconvenient".
This README file is copied into the directory for GCC-only header files
when fixincludes is run by the makefile for GCC.

Many of the files in this directory were automatically edited from the
standard system header files by the fixincludes process.  They are
system-specific, and will not work on any other kind of system.  They
are also not part of GCC.  The reason we have to do this is because
GCC requires ANSI C headers and many vendors supply ANSI-incompatible
headers.

Because this is an automated process, sometimes headers get "fixed"
that do not, strictly speaking, need a fix.  As long as nothing is broken
by the process, it is just an unfortunate collateral inconvenience.
We would like to rectify it, if it is not "too inconvenient".
		   README for GNU development tools

This directory contains various GNU compilers, assemblers, linkers, 
debuggers, etc., plus their support routines, definitions, and documentation.

If you are receiving this as part of a GDB release, see the file gdb/README.
If with a binutils release, see binutils/README;  if with a libg++ release,
see libg++/README, etc.  That'll give you info about this
package -- supported targets, how to use it, how to report bugs, etc.

It is now possible to automatically configure and build a variety of
tools with one command.  To build all of the tools contained herein,
run the ``configure'' script here, e.g.:

	./configure 
	make

To install them (by default in /usr/local/bin, /usr/local/lib, etc),
then do:
	make install

(If the configure script can't determine your type of computer, give it
the name as an argument, for instance ``./configure sun4''.  You can
use the script ``config.sub'' to test whether a name is recognized; if
it is, config.sub translates it to a triplet specifying CPU, vendor,
and OS.)

If you have more than one compiler on your system, it is often best to
explicitly set CC in the environment before running configure, and to
also set CC when running make.  For example (assuming sh/bash/ksh):

	CC=gcc ./configure
	make

A similar example using csh:

	setenv CC gcc
	./configure
	make

Much of the code and documentation enclosed is copyright by
the Free Software Foundation, Inc.  See the file COPYING or
COPYING.LIB in the various directories, for a description of the
GNU General Public License terms under which you can copy the files.

REPORTING BUGS: Again, see gdb/README, binutils/README, etc., for info
on where and how to report problems.

                        Expat, Release 2.0.1

This is Expat, a C library for parsing XML, written by James Clark.
Expat is a stream-oriented XML parser.  This means that you register
handlers with the parser before starting the parse.  These handlers
are called when the parser discovers the associated structures in the
document being parsed.  A start tag is an example of the kind of
structures for which you may register handlers.

Windows users should use the expat_win32bin package, which includes
both precompiled libraries and executables, and source code for
developers.

Expat is free software.  You may copy, distribute, and modify it under
the terms of the License contained in the file COPYING distributed
with this package.  This license is the same as the MIT/X Consortium
license.

Versions of Expat that have an odd minor version (the middle number in
the release above), are development releases and should be considered
as beta software.  Releases with even minor version numbers are
intended to be production grade software.

If you are building Expat from a check-out from the CVS repository,
you need to run a script that generates the configure script using the
GNU autoconf and libtool tools.  To do this, you need to have
autoconf 2.52 or newer and libtool 1.4 or newer (1.5 or newer preferred).
Run the script like this:

        ./buildconf.sh

Once this has been done, follow the same instructions as for building
from a source distribution.

To build Expat from a source distribution, you first run the
configuration shell script in the top level distribution directory:

        ./configure

There are many options which you may provide to configure (which you
can discover by running configure with the --help option).  But the
one of most interest is the one that sets the installation directory.
By default, the configure script will set things up to install
libexpat into /usr/local/lib, expat.h into /usr/local/include, and
xmlwf into /usr/local/bin.  If, for example, you'd prefer to install
into /home/me/mystuff/lib, /home/me/mystuff/include, and
/home/me/mystuff/bin, you can tell configure about that with:

        ./configure --prefix=/home/me/mystuff
        
Another interesting option is to enable 64-bit integer support for
line and column numbers and the over-all byte index:

        ./configure CPPFLAGS=-DXML_LARGE_SIZE
        
However, such a modification would be a breaking change to the ABI
and is therefore not recommended for general use - e.g. as part of
a Linux distribution - but rather for builds with special requirements.

After running the configure script, the "make" command will build
things and "make install" will install things into their proper
location.  Have a look at the "Makefile" to learn about additional
"make" options.  Note that you need to have write permission into
the directories into which things will be installed.

If you are interested in building Expat to provide document
information in UTF-16 rather than the default UTF-8, follow these
instructions (after having run "make distclean"):

        1. For UTF-16 output as unsigned short (and version/error
           strings as char), run:

               ./configure CPPFLAGS=-DXML_UNICODE

           For UTF-16 output as wchar_t (incl. version/error strings),
           run:

               ./configure CFLAGS="-g -O2 -fshort-wchar" \
                           CPPFLAGS=-DXML_UNICODE_WCHAR_T

        2. Edit the MakeFile, changing:

               LIBRARY = libexpat.la

           to:

               LIBRARY = libexpatw.la

           (Note the additional "w" in the library name.)

        3. Run "make buildlib" (which builds the library only).
           Or, to save step 2, run "make buildlib LIBRARY=libexpatw.la".

        4. Run "make installlib" (which installs the library only).
           Or, if step 2 was omitted, run "make installlib LIBRARY=libexpatw.la".
           
Using DESTDIR or INSTALL_ROOT is enabled, with INSTALL_ROOT being the default
value for DESTDIR, and the rest of the make file using only DESTDIR.
It works as follows:
   $ make install DESTDIR=/path/to/image
overrides the in-makefile set DESTDIR, while both
   $ INSTALL_ROOT=/path/to/image make install
   $ make install INSTALL_ROOT=/path/to/image
use DESTDIR=$(INSTALL_ROOT), even if DESTDIR eventually is defined in the
environment, because variable-setting priority is
1) commandline
2) in-makefile
3) environment           

Note for Solaris users:  The "ar" command is usually located in
"/usr/ccs/bin", which is not in the default PATH.  You will need to
add this to your path for the "make" command, and probably also switch
to GNU make (the "make" found in /usr/ccs/bin does not seem to work
properly -- appearantly it does not understand .PHONY directives).  If
you're using ksh or bash, use this command to build:

        PATH=/usr/ccs/bin:$PATH make

When using Expat with a project using autoconf for configuration, you
can use the probing macro in conftools/expat.m4 to determine how to
include Expat.  See the comments at the top of that file for more
information.

A reference manual is available in the file doc/reference.html in this
distribution.

The homepage for this project is http://www.libexpat.org/.  There
are links there to connect you to the bug reports page.  If you need
to report a bug when you don't have access to a browser, you may also
send a bug report by email to expat-bugs@mail.libexpat.org.

Discussion related to the direction of future expat development takes
place on expat-discuss@mail.libexpat.org.  Archives of this list and
other Expat-related lists may be found at:

        http://mail.libexpat.org/mailman/listinfo/
            GNU LIBICONV - character set conversion library

This library provides an iconv() implementation, for use on systems which
don't have one, or whose implementation cannot convert from/to Unicode.

It provides support for the encodings:

    European languages
        ASCII, ISO-8859-{1,2,3,4,5,7,9,10,13,14,15,16},
        KOI8-R, KOI8-U, KOI8-RU,
        CP{1250,1251,1252,1253,1254,1257}, CP{850,866,1131},
        Mac{Roman,CentralEurope,Iceland,Croatian,Romania},
        Mac{Cyrillic,Ukraine,Greek,Turkish},
        Macintosh
    Semitic languages
        ISO-8859-{6,8}, CP{1255,1256}, CP862, Mac{Hebrew,Arabic}
    Japanese
        EUC-JP, SHIFT_JIS, CP932, ISO-2022-JP, ISO-2022-JP-2, ISO-2022-JP-1
    Chinese
        EUC-CN, HZ, GBK, CP936, GB18030, EUC-TW, BIG5, CP950, BIG5-HKSCS,
        BIG5-HKSCS:2001, BIG5-HKSCS:1999, ISO-2022-CN, ISO-2022-CN-EXT
    Korean
        EUC-KR, CP949, ISO-2022-KR, JOHAB
    Armenian
        ARMSCII-8
    Georgian
        Georgian-Academy, Georgian-PS
    Tajik
        KOI8-T
    Kazakh
        PT154, RK1048
    Thai
        ISO-8859-11, TIS-620, CP874, MacThai
    Laotian
        MuleLao-1, CP1133
    Vietnamese
        VISCII, TCVN, CP1258
    Platform specifics
        HP-ROMAN8, NEXTSTEP
    Full Unicode
        UTF-8
        UCS-2, UCS-2BE, UCS-2LE
        UCS-4, UCS-4BE, UCS-4LE
        UTF-16, UTF-16BE, UTF-16LE
        UTF-32, UTF-32BE, UTF-32LE
        UTF-7
        C99, JAVA
    Full Unicode, in terms of `uint16_t' or `uint32_t'
        (with machine dependent endianness and alignment)
        UCS-2-INTERNAL, UCS-4-INTERNAL
    Locale dependent, in terms of `char' or `wchar_t'
        (with machine dependent endianness and alignment, and with OS and
        locale dependent semantics)
        char, wchar_t
        The empty encoding name "" is equivalent to "char": it denotes the
        locale dependent character encoding.

When configured with the option --enable-extra-encodings, it also provides
support for a few extra encodings:

    European languages
        CP{437,737,775,852,853,855,857,858,860,861,863,865,869,1125}
    Semitic languages
        CP864
    Japanese
        EUC-JISX0213, Shift_JISX0213, ISO-2022-JP-3
    Chinese
        BIG5-2003 (experimental)
    Turkmen
        TDS565
    Platform specifics
        ATARIST, RISCOS-LATIN1

It can convert from any of these encodings to any other, through Unicode
conversion.

It has also some limited support for transliteration, i.e. when a character
cannot be represented in the target character set, it can be approximated
through one or several similarly looking characters. Transliteration is
activated when "//TRANSLIT" is appended to the target encoding name.

libiconv is for you if your application needs to support multiple character
encodings, but that support lacks from your system.


Installation
------------

As usual for GNU packages:

    $ ./configure --prefix=/usr/local
    $ make
    $ make install

After installing GNU libiconv for the first time, it is recommended to
recompile and reinstall GNU gettext, so that it can take advantage of
libiconv.

On systems other than GNU/Linux, the iconv program will be internationalized
only if GNU gettext has been built and installed before GNU libiconv. This
means that the first time GNU libiconv is installed, we have a circular
dependency between the GNU libiconv and GNU gettext packages, which can be
resolved by building and installing either
  - first libiconv, then gettext, then libiconv again,
or (on systems supporting shared libraries, excluding AIX)
  - first gettext, then libiconv, then gettext again.
Recall that before building a package for the second time, you need to erase
the traces of the first build by running "make distclean".

This library can be built and installed in two variants:

  - The library mode. This works on all systems, and uses a library
    `libiconv.so' and a header file `<iconv.h>'. (Both are installed
    through "make install".)

    To use it, simply #include <iconv.h> and use the functions.

    To use it in an autoconfiguring package:
    - If you don't use automake, append m4/iconv.m4 to your aclocal.m4
      file.
    - If you do use automake, add m4/iconv.m4 to your m4 macro repository.
    - Add to the link command line of libraries and executables that use
      the functions the placeholder @LIBICONV@ (or, if using libtool for
      the link, @LTLIBICONV@). If you use automake, the right place for
      these additions are the *_LDADD variables.
    Note that 'iconv.m4' is also part of the GNU gettext package, which
    installs it in /usr/local/share/aclocal/iconv.m4.

  - The libc plug/override mode. This works on GNU/Linux, Solaris and OSF/1
    systems only. It is a way to get good iconv support without having
    glibc-2.1.
    It installs a library `preloadable_libiconv.so'. This library can be used
    with LD_PRELOAD, to override the iconv* functions present in the C library.

    On GNU/Linux and Solaris:
        $ export LD_PRELOAD=/usr/local/lib/preloadable_libiconv.so

    On OSF/1:
        $ export _RLD_LIST=/usr/local/lib/preloadable_libiconv.so:DEFAULT

    A program's source need not be modified, the program need not even be
    recompiled. Just set the LD_PRELOAD environment variable, that's it!


Copyright
---------

The libiconv and libcharset _libraries_ and their header files are under LGPL,
see file COPYING.LIB.

The iconv _program_ and the documentation are under GPL, see file COPYING.


Download
--------

    http://ftp.gnu.org/gnu/libiconv/libiconv-1.13.1.tar.gz

Homepage
--------

    http://www.gnu.org/software/libiconv/

Bug reports to
--------------

    <bug-gnu-libiconv@gnu.org>


Bruno Haible <bruno@clisp.org>
Copyright 1991, 1996, 1999, 2000, 2007 Free Software Foundation, Inc.

This file is part of the GNU MP Library.

The GNU MP Library is free software; you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation; either version 3 of the License, or (at your
option) any later version.

The GNU MP Library is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public
License for more details.

You should have received a copy of the GNU Lesser General Public License
along with the GNU MP Library.  If not, see http://www.gnu.org/licenses/.






			THE GNU MP LIBRARY


GNU MP is a library for arbitrary precision arithmetic, operating on signed
integers, rational numbers, and floating point numbers.  It has a rich set of
functions, and the functions have a regular interface.

GNU MP is designed to be as fast as possible, both for small operands and huge
operands.  The speed is achieved by using fullwords as the basic arithmetic
type, by using fast algorithms, with carefully optimized assembly code for the
most common inner loops for lots of CPUs, and by a general emphasis on speed
(instead of simplicity or elegance).

GNU MP is believed to be faster than any other similar library.  Its advantage
increases with operand sizes for certain operations, since GNU MP in many
cases has asymptotically faster algorithms.

GNU MP is free software and may be freely copied on the terms contained in the
files COPYING.LIB and COPYING (most of GNU MP is under the former, some under
the latter).



			OVERVIEW OF GNU MP

There are five classes of functions in GNU MP.

 1. Signed integer arithmetic functions (mpz).  These functions are intended
    to be easy to use, with their regular interface.  The associated type is
    `mpz_t'.

 2. Rational arithmetic functions (mpq).  For now, just a small set of
    functions necessary for basic rational arithmetics.  The associated type
    is `mpq_t'.

 3. Floating-point arithmetic functions (mpf).  If the C type `double'
    doesn't give enough precision for your application, declare your
    variables as `mpf_t' instead, set the precision to any number desired,
    and call the functions in the mpf class for the arithmetic operations.

 4. Positive-integer, hard-to-use, very low overhead functions are in the
    mpn class.  No memory management is performed.  The caller must ensure
    enough space is available for the results.  The set of functions is not
    regular, nor is the calling interface.  These functions accept input
    arguments in the form of pairs consisting of a pointer to the least
    significant word, and an integral size telling how many limbs (= words)
    the pointer points to.

    Almost all calculations, in the entire package, are made by calling these
    low-level functions.

 5. Berkeley MP compatible functions.

    To use these functions, include the file "mp.h".  You can test if you are
    using the GNU version by testing if the symbol __GNU_MP__ is defined.

For more information on how to use GNU MP, please refer to the documentation.
It is composed from the file doc/gmp.texi, and can be displayed on the screen
or printed.  How to do that, as well how to build the library, is described in
the INSTALL file in this directory.



			REPORTING BUGS

If you find a bug in the library, please make sure to tell us about it!

You should first check the GNU MP web pages at http://gmplib.org/, under
"Status of the current release".  There will be patches for all known serious
bugs there.

Report bugs to gmp-bugs@gmplib.org.  What information is needed in a useful bug
report is described in the manual.  The same address can be used for suggesting
modifications and enhancements.




----------------
Local variables:
mode: text
fill-column: 78
End:
		   README for GNU development tools

This directory contains various GNU compilers, assemblers, linkers, 
debuggers, etc., plus their support routines, definitions, and documentation.

If you are receiving this as part of a GDB release, see the file gdb/README.
If with a binutils release, see binutils/README;  if with a libg++ release,
see libg++/README, etc.  That'll give you info about this
package -- supported targets, how to use it, how to report bugs, etc.

It is now possible to automatically configure and build a variety of
tools with one command.  To build all of the tools contained herein,
run the ``configure'' script here, e.g.:

	./configure 
	make

To install them (by default in /usr/local/bin, /usr/local/lib, etc),
then do:
	make install

(If the configure script can't determine your type of computer, give it
the name as an argument, for instance ``./configure sun4''.  You can
use the script ``config.sub'' to test whether a name is recognized; if
it is, config.sub translates it to a triplet specifying CPU, vendor,
and OS.)

If you have more than one compiler on your system, it is often best to
explicitly set CC in the environment before running configure, and to
also set CC when running make.  For example (assuming sh/bash/ksh):

	CC=gcc ./configure
	make

A similar example using csh:

	setenv CC gcc
	./configure
	make

Much of the code and documentation enclosed is copyright by
the Free Software Foundation, Inc.  See the file COPYING or
COPYING.LIB in the various directories, for a description of the
GNU General Public License terms under which you can copy the files.

REPORTING BUGS: Again, see gdb/README, binutils/README, etc., for info
on where and how to report problems.
mpc is a complex floating-point library with exact rounding.
It is based on the GNU MPFR floating-point library (http://www.mpfr.org/),
which is itself based on the GNU MP library (http://gmplib.org/).
{\rtf1\ansi\ansicpg1252\deff0\deftab720{\fonttbl{\f0\fswiss MS Sans Serif;}{\f1\froman\fcharset2 Symbol;}{\f2\fmodern\fprq1 Courier New;}{\f3\froman Times New Roman;}{\f4\fmodern\fprq1 Lucida Console;}}
{\colortbl\red0\green0\blue0;}
\deflang1033\horzdoc{\*\fchars }{\*\lchars }\pard\tx2610\plain\f2\fs20\b\i File:\plain\f2\fs20\i \tab \plain\f2\fs20 README
\par \plain\f2\fs20\b\i Copyright (C):\plain\f2\fs20 \tab 2001, 2002  Earnie Boyd  <earnie@users.sf.net>
\par \plain\f2\fs20\b\i Distribution:\plain\f2\fs20 \tab See MSYS_LICENSE
\par \plain\f2\fs20\b\i MSYS Revision:\plain\f2\fs20 \tab 1.0.10
\par \plain\f2\fs20\b\i MSYS Revision date:\plain\f2\fs20\i \tab \plain\lang1024\f2\fs20 October 31, 2002\plain\f2\fs20 
\par \pard\qc\tx2610\plain\f2\fs20\i 
\par \pard\plain\f2\fs20\b\i Preface:\plain\f2\fs20 
\par Ok, you have installed msys and now you're reading this to understand how to get started.  However, I must first explain some important facts about Msys.  Msys file system bindings (mounts) are automatic and happens as described in table 1.  These automatic file system bindings are not changable by the user.  User defined file system bindings can be created by specifying them in the /etc/fstab directory as explained in table 2.
\par 
\par \plain\f2\fs20\b\i TABLE 1 - Automatic file system maps:\plain\f2\fs20 
\par \plain\f4\fs16 + ---------------------------------------------------------------------------- +
\par | The automatic mounts are relative to where the msys-1.0.dll (DLL) is located |
\par | such that the following is true:                                             |
\par |                                                                              |
\par | / - is the parent directory of the directory containing the DLL              |
\par | /bin - the direcotry containing the DLL                                      |
\par | /usr - the parent directory of the directory containing the DLL              |
\par | /usr/bin - the directory containing the DLL                                  |
\par | /tmp - the value of the TMP environment variable                             |
\par | /c - C:\\                                                                     |
\par | /d - D:\\                                                                     |
\par | . . .                                                                        |
\par | /z - Z:\\                                                                     |
\par |                                                                              |
\par + ---------------------------------------------------------------------------- +
\par \plain\f2\fs20 
\par \plain\f2\fs20\b\i TABLE 2 - /etc/fstab layout:\plain\f2\fs20 
\par \plain\f4\fs16 + ---------------------------------------------------------------------------- +
\par | The record format for the /etc/fstab is current a simple one.  I need to     |
\par | work on the syntax parsing more so that things like embedded spaces work.    |
\par | If you wish to map a path with spaces you must use the DOS style name.       |
\par |                                                                              |
\par | The record format is as follows:                                             |
\par | d:/some/foo/path /bar                                                        |
\par |                                                                              |
\par | As you can see this is simply the Win32 path mapped to a mount point.  It is |
\par | unix practice to have the /bar created as an empty directory before it can   |
\par | mount the mount point.  Msys doesn't force this but it will be to advantage  |
\par | if you do.  Some programs, e.g. find, and some operations, e.g. tab          |
\par | operate better if the physical directory is present for those mount points.  |
\par |                                                                              |
\par | If you create a /etc/fstab record that maps to an automatic mount point Msys |
\par | will remove it when it adds the automatic point.  This means that at some    |
\par | small moment in time your mount point actually exists.  However it doesn't   |
\par | exist long enough to be of any use to you.                                   |
\par |                                                                              |
\par + ---------------------------------------------------------------------------- +
\par \plain\f2\fs20 
\par Msys will convert POSIX paths that are used as arguments to Win32 paths.  This is done for any executable not in /bin and /usr/bin.  If the executable is dependant on the msys-1.0.dll then it must be located in the /bin or /usr/bin directory.  This means that you now have a POSIX environment that will automagically do the right thing w.r.t. changing the paths passed as arguments.  Arguments beginning with a // are considered to be Win32 style switches and will be passed to the program with // converted to / to allow for the command.com/cmd.exe (Win32) style switch.  An example of a Win32 style switch is `write //p /mydocs/msys-rocks.'  In this example write (a.k.a. WordPad) exists in the c:\\winnt\\system32 path on my system.  The //p becomes /p which tells write to print the document.  And mydocs/msys-rocks converts to c:\\msys\\1.0\\mydocs\\msys-rocks so that write can find it.  
\par \plain\f2\fs20\b\i 
\par STARTING Msys:
\par \plain\f2\fs20 Starting Msys should just be a matter of clicking on the MSYS icon on your desktop or Start menu.  If you have the File Manager window open, you may now click on it and have it start also.  Doing these presents you with a console window within which you may enter commands.
\par 
\par \plain\f2\fs20\b\i Working with MinGW:
\par \plain\f2\fs20 If you already have MinGW installed then simply bind the path to MinGW to the /mingw mount point in the /etc/fstab as described above.  If you don't have MinGW installed already then simply unarchive the MinGW tar.gz file in the /mingw directory.  \plain\f2\fs20\b\ul DO NOT\plain\f2\fs20  unarchive the MinGW tar.gz file in the / directory.
\par \plain\f2\fs20\b\i 
\par Working with other products:
\par \plain\f2\fs20 I find that the easiest thing for working with other products, such as Microsoft Office, is to create a script pointing to the executable.  An example of a script for Microsoft Word on my system looks like the example in Table 3.  I have this stored in my /usr/local/bin directory with a filename of word.  Now all I need to do to edit a word document is `word /mydoc/proposal.doc' and voila up pops a Microsoft Word window with my document in it.
\par 
\par \plain\f2\fs20\b\i Table 3 - Script to execute MS Word from the command line:
\par \plain\f4\fs16 + ---------------------------------------------------------------------------- +
\par + #!/bin/sh                                                                    +
\par + start '/c/Program\\ Files/Microsoft\\ Office/Office/WINWORD' $@                +
\par + ---------------------------------------------------------------------------- +
\par \plain\f2\fs20\b\i 
\par Other documentation:\plain\f2\fs20 
\par Be sure to read the MSYS_ series.  I have tried to document how I'm changing the cygwin code to allow us to use it with MSYS.  These can be found in the /doc/msys directory, or you can find them in the /usr/doc/msys directory.
\par 
\par \plain\f2\fs20\b\i Using binaries with different runtimes:\plain\f2\fs20 
\par You can't use Cygwin binaries at all and if you try you'll most likely just cause the processes to "hang".  You can use Win32 native binaries but you should put them into the /mingw/bin or your /usr/local/bin directory tree.  If you wish to replace an MSYS binary with a native win32 version then delete or rename the /bin version.
\par 
\par \plain\f2\fs20\b\i Effective use of the clipboard:
\par \plain\f2\fs20 You may use the clipboard with MSYS.  When using rxvt (the default installation) as the terminal, just selecting with data with click and drag of the mouse, copies the data to the clipboard.  To paste the clipboard data in the rxvt terminal you can Shift and Left Click or press both mouse buttons if 3 button mouse emulation is on or press the mouse wheel.  To copy the highlighted data to your favorite windows email client the you use the paste options for that program, typically Ctrl-V.  You can also use interesting bash shell commands such as `cat /dev/clipboard > /tmp/foo' or `less -f /dev/clipboard'.  Data entered into the clipboard by non-MSYS programs can also be used by MSYS programs and vice versa.\plain\f2\fs20\b\i 
\par 
\par Bug Reports:\plain\f2\fs20 
\par Send your bug reports to MinGW-msys@lists.sf.net.
\par 
\par \plain\f2\fs20\b\i User Posts:\plain\f2\fs20 
\par MinGW-msys@lists.sf.net
\par 
\par \plain\f2\fs20\b\i Disclaimer:
\par \plain\f2\fs20 Products mentioned in this and other documents are solely owned by their trademark owners.  We claim no rights to those trademarks and any mention of those products are for example only.  Your uses of those products are your responsibility and no endorsement of any mentioned product is being given.
\par 
\par \plain\f2\fs20\b\i Change History:
\par \plain\f2\fs20 Version 1.0.3 added checks for paths following an `=' and `-X' where X
\par is a program switch.
\par 
\par Version 1.0.4 added symlink resolution, removed the dependancy that the pathmust begin with a / and removed bash.exe since sh.exe is bash.exe anyway.  Also added diff, diff3 and head to the distribution.  An MSYS icon exists in the rxvt binary.
\par 
\par Version 1.0.5 is a bug fix release that filters out the conversion of quoted relative paths.  So that -DSOME_CONSTANT=\\"1.0.5\\" can be properly input into gcc.  Also fixed the problem with sh.exe reading /etc/profile with \\r\\n line endings.  Added the binaries true.exe, false.exe, tail.exe and fold.exe.  Updated the gmake binary to the Cygwin version including the --win32 switch.  I am suggesting to use this version of make and have copied /bin/gmake.exe to /bin/make (yes without the .exe).  If you wish to go back to the "native" version of make typing make.exe will get you there.
\par 
\par Version 1.0.6 through current: See the appropriate MSYS-<version>-changes.rtf document.
\par }
 Compatibility Notice:  ** No leading underscore **
------------------------------------------------------------------------
Unlike the other builds from mingw-w64 up to 2010-04-27, these new win64
targetting toolchains do *not* prepend an undersocore to the symbols and
follows the MSVC x64 convention.  Therefore, any of the link libraries
from previous toolchains are incompatible with the ones created by these
new builds.

This README file is copied into the directory for GCC-only header files
when fixincludes is run by the makefile for GCC.

Many of the files in this directory were automatically edited from the
standard system header files by the fixincludes process.  They are
system-specific, and will not work on any other kind of system.  They
are also not part of GCC.  The reason we have to do this is because
GCC requires ANSI C headers and many vendors supply ANSI-incompatible
headers.

Because this is an automated process, sometimes headers get "fixed"
that do not, strictly speaking, need a fix.  As long as nothing is broken
by the process, it is just an unfortunate collateral inconvenience.
We would like to rectify it, if it is not "too inconvenient".
This README file is copied into the directory for GCC-only header files
when fixincludes is run by the makefile for GCC.

Many of the files in this directory were automatically edited from the
standard system header files by the fixincludes process.  They are
system-specific, and will not work on any other kind of system.  They
are also not part of GCC.  The reason we have to do this is because
GCC requires ANSI C headers and many vendors supply ANSI-incompatible
headers.

Because this is an automated process, sometimes headers get "fixed"
that do not, strictly speaking, need a fix.  As long as nothing is broken
by the process, it is just an unfortunate collateral inconvenience.
We would like to rectify it, if it is not "too inconvenient".
		   README for GNU development tools

This directory contains various GNU compilers, assemblers, linkers, 
debuggers, etc., plus their support routines, definitions, and documentation.

If you are receiving this as part of a GDB release, see the file gdb/README.
If with a binutils release, see binutils/README;  if with a libg++ release,
see libg++/README, etc.  That'll give you info about this
package -- supported targets, how to use it, how to report bugs, etc.

It is now possible to automatically configure and build a variety of
tools with one command.  To build all of the tools contained herein,
run the ``configure'' script here, e.g.:

	./configure 
	make

To install them (by default in /usr/local/bin, /usr/local/lib, etc),
then do:
	make install

(If the configure script can't determine your type of computer, give it
the name as an argument, for instance ``./configure sun4''.  You can
use the script ``config.sub'' to test whether a name is recognized; if
it is, config.sub translates it to a triplet specifying CPU, vendor,
and OS.)

If you have more than one compiler on your system, it is often best to
explicitly set CC in the environment before running configure, and to
also set CC when running make.  For example (assuming sh/bash/ksh):

	CC=gcc ./configure
	make

A similar example using csh:

	setenv CC gcc
	./configure
	make

Much of the code and documentation enclosed is copyright by
the Free Software Foundation, Inc.  See the file COPYING or
COPYING.LIB in the various directories, for a description of the
GNU General Public License terms under which you can copy the files.

REPORTING BUGS: Again, see gdb/README, binutils/README, etc., for info
on where and how to report problems.

                        Expat, Release 2.0.1

This is Expat, a C library for parsing XML, written by James Clark.
Expat is a stream-oriented XML parser.  This means that you register
handlers with the parser before starting the parse.  These handlers
are called when the parser discovers the associated structures in the
document being parsed.  A start tag is an example of the kind of
structures for which you may register handlers.

Windows users should use the expat_win32bin package, which includes
both precompiled libraries and executables, and source code for
developers.

Expat is free software.  You may copy, distribute, and modify it under
the terms of the License contained in the file COPYING distributed
with this package.  This license is the same as the MIT/X Consortium
license.

Versions of Expat that have an odd minor version (the middle number in
the release above), are development releases and should be considered
as beta software.  Releases with even minor version numbers are
intended to be production grade software.

If you are building Expat from a check-out from the CVS repository,
you need to run a script that generates the configure script using the
GNU autoconf and libtool tools.  To do this, you need to have
autoconf 2.52 or newer and libtool 1.4 or newer (1.5 or newer preferred).
Run the script like this:

        ./buildconf.sh

Once this has been done, follow the same instructions as for building
from a source distribution.

To build Expat from a source distribution, you first run the
configuration shell script in the top level distribution directory:

        ./configure

There are many options which you may provide to configure (which you
can discover by running configure with the --help option).  But the
one of most interest is the one that sets the installation directory.
By default, the configure script will set things up to install
libexpat into /usr/local/lib, expat.h into /usr/local/include, and
xmlwf into /usr/local/bin.  If, for example, you'd prefer to install
into /home/me/mystuff/lib, /home/me/mystuff/include, and
/home/me/mystuff/bin, you can tell configure about that with:

        ./configure --prefix=/home/me/mystuff
        
Another interesting option is to enable 64-bit integer support for
line and column numbers and the over-all byte index:

        ./configure CPPFLAGS=-DXML_LARGE_SIZE
        
However, such a modification would be a breaking change to the ABI
and is therefore not recommended for general use - e.g. as part of
a Linux distribution - but rather for builds with special requirements.

After running the configure script, the "make" command will build
things and "make install" will install things into their proper
location.  Have a look at the "Makefile" to learn about additional
"make" options.  Note that you need to have write permission into
the directories into which things will be installed.

If you are interested in building Expat to provide document
information in UTF-16 rather than the default UTF-8, follow these
instructions (after having run "make distclean"):

        1. For UTF-16 output as unsigned short (and version/error
           strings as char), run:

               ./configure CPPFLAGS=-DXML_UNICODE

           For UTF-16 output as wchar_t (incl. version/error strings),
           run:

               ./configure CFLAGS="-g -O2 -fshort-wchar" \
                           CPPFLAGS=-DXML_UNICODE_WCHAR_T

        2. Edit the MakeFile, changing:

               LIBRARY = libexpat.la

           to:

               LIBRARY = libexpatw.la

           (Note the additional "w" in the library name.)

        3. Run "make buildlib" (which builds the library only).
           Or, to save step 2, run "make buildlib LIBRARY=libexpatw.la".

        4. Run "make installlib" (which installs the library only).
           Or, if step 2 was omitted, run "make installlib LIBRARY=libexpatw.la".
           
Using DESTDIR or INSTALL_ROOT is enabled, with INSTALL_ROOT being the default
value for DESTDIR, and the rest of the make file using only DESTDIR.
It works as follows:
   $ make install DESTDIR=/path/to/image
overrides the in-makefile set DESTDIR, while both
   $ INSTALL_ROOT=/path/to/image make install
   $ make install INSTALL_ROOT=/path/to/image
use DESTDIR=$(INSTALL_ROOT), even if DESTDIR eventually is defined in the
environment, because variable-setting priority is
1) commandline
2) in-makefile
3) environment           

Note for Solaris users:  The "ar" command is usually located in
"/usr/ccs/bin", which is not in the default PATH.  You will need to
add this to your path for the "make" command, and probably also switch
to GNU make (the "make" found in /usr/ccs/bin does not seem to work
properly -- appearantly it does not understand .PHONY directives).  If
you're using ksh or bash, use this command to build:

        PATH=/usr/ccs/bin:$PATH make

When using Expat with a project using autoconf for configuration, you
can use the probing macro in conftools/expat.m4 to determine how to
include Expat.  See the comments at the top of that file for more
information.

A reference manual is available in the file doc/reference.html in this
distribution.

The homepage for this project is http://www.libexpat.org/.  There
are links there to connect you to the bug reports page.  If you need
to report a bug when you don't have access to a browser, you may also
send a bug report by email to expat-bugs@mail.libexpat.org.

Discussion related to the direction of future expat development takes
place on expat-discuss@mail.libexpat.org.  Archives of this list and
other Expat-related lists may be found at:

        http://mail.libexpat.org/mailman/listinfo/
            GNU LIBICONV - character set conversion library

This library provides an iconv() implementation, for use on systems which
don't have one, or whose implementation cannot convert from/to Unicode.

It provides support for the encodings:

    European languages
        ASCII, ISO-8859-{1,2,3,4,5,7,9,10,13,14,15,16},
        KOI8-R, KOI8-U, KOI8-RU,
        CP{1250,1251,1252,1253,1254,1257}, CP{850,866,1131},
        Mac{Roman,CentralEurope,Iceland,Croatian,Romania},
        Mac{Cyrillic,Ukraine,Greek,Turkish},
        Macintosh
    Semitic languages
        ISO-8859-{6,8}, CP{1255,1256}, CP862, Mac{Hebrew,Arabic}
    Japanese
        EUC-JP, SHIFT_JIS, CP932, ISO-2022-JP, ISO-2022-JP-2, ISO-2022-JP-1
    Chinese
        EUC-CN, HZ, GBK, CP936, GB18030, EUC-TW, BIG5, CP950, BIG5-HKSCS,
        BIG5-HKSCS:2001, BIG5-HKSCS:1999, ISO-2022-CN, ISO-2022-CN-EXT
    Korean
        EUC-KR, CP949, ISO-2022-KR, JOHAB
    Armenian
        ARMSCII-8
    Georgian
        Georgian-Academy, Georgian-PS
    Tajik
        KOI8-T
    Kazakh
        PT154, RK1048
    Thai
        ISO-8859-11, TIS-620, CP874, MacThai
    Laotian
        MuleLao-1, CP1133
    Vietnamese
        VISCII, TCVN, CP1258
    Platform specifics
        HP-ROMAN8, NEXTSTEP
    Full Unicode
        UTF-8
        UCS-2, UCS-2BE, UCS-2LE
        UCS-4, UCS-4BE, UCS-4LE
        UTF-16, UTF-16BE, UTF-16LE
        UTF-32, UTF-32BE, UTF-32LE
        UTF-7
        C99, JAVA
    Full Unicode, in terms of `uint16_t' or `uint32_t'
        (with machine dependent endianness and alignment)
        UCS-2-INTERNAL, UCS-4-INTERNAL
    Locale dependent, in terms of `char' or `wchar_t'
        (with machine dependent endianness and alignment, and with OS and
        locale dependent semantics)
        char, wchar_t
        The empty encoding name "" is equivalent to "char": it denotes the
        locale dependent character encoding.

When configured with the option --enable-extra-encodings, it also provides
support for a few extra encodings:

    European languages
        CP{437,737,775,852,853,855,857,858,860,861,863,865,869,1125}
    Semitic languages
        CP864
    Japanese
        EUC-JISX0213, Shift_JISX0213, ISO-2022-JP-3
    Chinese
        BIG5-2003 (experimental)
    Turkmen
        TDS565
    Platform specifics
        ATARIST, RISCOS-LATIN1

It can convert from any of these encodings to any other, through Unicode
conversion.

It has also some limited support for transliteration, i.e. when a character
cannot be represented in the target character set, it can be approximated
through one or several similarly looking characters. Transliteration is
activated when "//TRANSLIT" is appended to the target encoding name.

libiconv is for you if your application needs to support multiple character
encodings, but that support lacks from your system.


Installation
------------

As usual for GNU packages:

    $ ./configure --prefix=/usr/local
    $ make
    $ make install

After installing GNU libiconv for the first time, it is recommended to
recompile and reinstall GNU gettext, so that it can take advantage of
libiconv.

On systems other than GNU/Linux, the iconv program will be internationalized
only if GNU gettext has been built and installed before GNU libiconv. This
means that the first time GNU libiconv is installed, we have a circular
dependency between the GNU libiconv and GNU gettext packages, which can be
resolved by building and installing either
  - first libiconv, then gettext, then libiconv again,
or (on systems supporting shared libraries, excluding AIX)
  - first gettext, then libiconv, then gettext again.
Recall that before building a package for the second time, you need to erase
the traces of the first build by running "make distclean".

This library can be built and installed in two variants:

  - The library mode. This works on all systems, and uses a library
    `libiconv.so' and a header file `<iconv.h>'. (Both are installed
    through "make install".)

    To use it, simply #include <iconv.h> and use the functions.

    To use it in an autoconfiguring package:
    - If you don't use automake, append m4/iconv.m4 to your aclocal.m4
      file.
    - If you do use automake, add m4/iconv.m4 to your m4 macro repository.
    - Add to the link command line of libraries and executables that use
      the functions the placeholder @LIBICONV@ (or, if using libtool for
      the link, @LTLIBICONV@). If you use automake, the right place for
      these additions are the *_LDADD variables.
    Note that 'iconv.m4' is also part of the GNU gettext package, which
    installs it in /usr/local/share/aclocal/iconv.m4.

  - The libc plug/override mode. This works on GNU/Linux, Solaris and OSF/1
    systems only. It is a way to get good iconv support without having
    glibc-2.1.
    It installs a library `preloadable_libiconv.so'. This library can be used
    with LD_PRELOAD, to override the iconv* functions present in the C library.

    On GNU/Linux and Solaris:
        $ export LD_PRELOAD=/usr/local/lib/preloadable_libiconv.so

    On OSF/1:
        $ export _RLD_LIST=/usr/local/lib/preloadable_libiconv.so:DEFAULT

    A program's source need not be modified, the program need not even be
    recompiled. Just set the LD_PRELOAD environment variable, that's it!


Copyright
---------

The libiconv and libcharset _libraries_ and their header files are under LGPL,
see file COPYING.LIB.

The iconv _program_ and the documentation are under GPL, see file COPYING.


Download
--------

    http://ftp.gnu.org/gnu/libiconv/libiconv-1.13.1.tar.gz

Homepage
--------

    http://www.gnu.org/software/libiconv/

Bug reports to
--------------

    <bug-gnu-libiconv@gnu.org>


Bruno Haible <bruno@clisp.org>
Copyright 1991, 1996, 1999, 2000, 2007 Free Software Foundation, Inc.

This file is part of the GNU MP Library.

The GNU MP Library is free software; you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation; either version 3 of the License, or (at your
option) any later version.

The GNU MP Library is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public
License for more details.

You should have received a copy of the GNU Lesser General Public License
along with the GNU MP Library.  If not, see http://www.gnu.org/licenses/.






			THE GNU MP LIBRARY


GNU MP is a library for arbitrary precision arithmetic, operating on signed
integers, rational numbers, and floating point numbers.  It has a rich set of
functions, and the functions have a regular interface.

GNU MP is designed to be as fast as possible, both for small operands and huge
operands.  The speed is achieved by using fullwords as the basic arithmetic
type, by using fast algorithms, with carefully optimized assembly code for the
most common inner loops for lots of CPUs, and by a general emphasis on speed
(instead of simplicity or elegance).

GNU MP is believed to be faster than any other similar library.  Its advantage
increases with operand sizes for certain operations, since GNU MP in many
cases has asymptotically faster algorithms.

GNU MP is free software and may be freely copied on the terms contained in the
files COPYING.LIB and COPYING (most of GNU MP is under the former, some under
the latter).



			OVERVIEW OF GNU MP

There are five classes of functions in GNU MP.

 1. Signed integer arithmetic functions (mpz).  These functions are intended
    to be easy to use, with their regular interface.  The associated type is
    `mpz_t'.

 2. Rational arithmetic functions (mpq).  For now, just a small set of
    functions necessary for basic rational arithmetics.  The associated type
    is `mpq_t'.

 3. Floating-point arithmetic functions (mpf).  If the C type `double'
    doesn't give enough precision for your application, declare your
    variables as `mpf_t' instead, set the precision to any number desired,
    and call the functions in the mpf class for the arithmetic operations.

 4. Positive-integer, hard-to-use, very low overhead functions are in the
    mpn class.  No memory management is performed.  The caller must ensure
    enough space is available for the results.  The set of functions is not
    regular, nor is the calling interface.  These functions accept input
    arguments in the form of pairs consisting of a pointer to the least
    significant word, and an integral size telling how many limbs (= words)
    the pointer points to.

    Almost all calculations, in the entire package, are made by calling these
    low-level functions.

 5. Berkeley MP compatible functions.

    To use these functions, include the file "mp.h".  You can test if you are
    using the GNU version by testing if the symbol __GNU_MP__ is defined.

For more information on how to use GNU MP, please refer to the documentation.
It is composed from the file doc/gmp.texi, and can be displayed on the screen
or printed.  How to do that, as well how to build the library, is described in
the INSTALL file in this directory.



			REPORTING BUGS

If you find a bug in the library, please make sure to tell us about it!

You should first check the GNU MP web pages at http://gmplib.org/, under
"Status of the current release".  There will be patches for all known serious
bugs there.

Report bugs to gmp-bugs@gmplib.org.  What information is needed in a useful bug
report is described in the manual.  The same address can be used for suggesting
modifications and enhancements.




----------------
Local variables:
mode: text
fill-column: 78
End:
		   README for GNU development tools

This directory contains various GNU compilers, assemblers, linkers, 
debuggers, etc., plus their support routines, definitions, and documentation.

If you are receiving this as part of a GDB release, see the file gdb/README.
If with a binutils release, see binutils/README;  if with a libg++ release,
see libg++/README, etc.  That'll give you info about this
package -- supported targets, how to use it, how to report bugs, etc.

It is now possible to automatically configure and build a variety of
tools with one command.  To build all of the tools contained herein,
run the ``configure'' script here, e.g.:

	./configure 
	make

To install them (by default in /usr/local/bin, /usr/local/lib, etc),
then do:
	make install

(If the configure script can't determine your type of computer, give it
the name as an argument, for instance ``./configure sun4''.  You can
use the script ``config.sub'' to test whether a name is recognized; if
it is, config.sub translates it to a triplet specifying CPU, vendor,
and OS.)

If you have more than one compiler on your system, it is often best to
explicitly set CC in the environment before running configure, and to
also set CC when running make.  For example (assuming sh/bash/ksh):

	CC=gcc ./configure
	make

A similar example using csh:

	setenv CC gcc
	./configure
	make

Much of the code and documentation enclosed is copyright by
the Free Software Foundation, Inc.  See the file COPYING or
COPYING.LIB in the various directories, for a description of the
GNU General Public License terms under which you can copy the files.

REPORTING BUGS: Again, see gdb/README, binutils/README, etc., for info
on where and how to report problems.
mpc is a complex floating-point library with exact rounding.
It is based on the GNU MPFR floating-point library (http://www.mpfr.org/),
which is itself based on the GNU MP library (http://gmplib.org/).
--| Copyright (c) 1993-2006 University of Southern California and contributors.
--| All rights reserved.
--| Your use of this work is governed under the terms of the GNU General Public
--| License version 2.

This directory is the distribution directory for the EiffelWeasel
automatic tester.  It has the following subdirectories with the
indicated contents:

	bin		Executables for platform-independent shell scripts
	compilation	Scripts and files need for compiling EiffelWeasel
	control		Include files, test suite catalogs for operation
	doc		Documentation
	spec		One subdirectory per supported platform with
			platform-dependent stuff (lib, bin, project dirs)
	source		Source code to build EiffelWeasel
	tests		Contains subdirectories which each have one test

Before proceeding, please read:

	This README file
	BUGS file in this directory
	CHANGES file in this directory
	INSTALL file in this directory
	doc/eweasel.doc

Typical usage of eweasel (on Solaris)

	setenv EWEASEL <EiffelWeasel_install_dir>
	set path = ($EWEASEL/bin $path)
	rehash
	alias ew 'eweasel -d HOME <your_home_dir> -d INCLUDE $EWEASEL/control -d ISE_EIFFEL <Eiffel_install_dir> -d ISE_PLATFORM solaris-2.5+ -d VERSION 5.0 \!* $EWEASEL/control/init $EWEASEL/control/catalog <test suite output directory>'

To show usage:

	eweasel -h	


Suggestions for improvement and bug reports should be sent to the
technical support address listed below.

The file BUGS in this directory contains a list of known bugs and
deficiencies in the EiffelWeasel tester.

The file CHANGES in this directory contains a list of changes to
EiffelWeasel since the previous release.

For technical support, contact:

	David Hollenberg
	Email:  dhollen@mosis.org
	Phone:  (310) 448-8704

To install EiffelWeasel
=======================

In the following UNPACK_DIR is the directory where you put the
distribution file eweasel.tar.gz.  INSTALL_DIR is the directory
where you want to install EiffelWeasel.

1. Unpack the distribution:

	[Put eweasel.tar.gz in UNPACK_DIR]
	
	cd UNPACK_DIR
	gunzip eweasel.tar.gz
	cd INSTALL_DIR
	tar xvf UNPACK_DIR/eweasel.tar

   Creates eweasel directory tree in INSTALL_DIR.

2. Set EWEASEL environment variable:

	setenv EWEASEL INSTALL_DIR/eweasel

   eweasel is the main EiffelWeasel directory that has sub-directories
   source, bin, and so forth.
   
   For me, this is

	setenv EWEASEL /marten/eweasel

3. Repeat this step once for each platform on which you want to
   install EiffelWeasel:

   Make sure ISE_EIFFEL and ISE_PLATFORM environment variables
   are set correctly for the platform.
   
   Execute the eweasel compilation shell script:

	$EWEASEL/compilation/install_eweasel  [-keep]

   This compiles all C code needed by EiffelWeasel, builds library
   eweasel.a in platform-specific directory, compiles EiffelWeasel
   itself (finalizes it) in platform-specific directory, compiles the
   generated C code and copies the executable to:

	$EWEASEL/spec/$ISE_PLATFORM/bin/eweasel

   If you do not specify the "-keep" option, all *.o files and the
   entire EIFGEN tree from compiling eweasel are deleted at the end.



To run EiffelWeasel
===================

Make sure the following environment variables are correctly set:
	
	EWEASEL
	ISE_EIFFEL
	ISE_PLATFORM

Set the following csh alias (or equivalent in another shell):

	alias ew '$EWEASEL/spec/$ISE_PLATFORM/bin/eweasel -d HOME /home/dhollen -d INCLUDE $EWEASEL/control -d EWEASEL $EWEASEL -d ISE_EIFFEL $ISE_EIFFEL -d ISE_PLATFORM $ISE_PLATFORM -d VERSION 5.2 \!* $EWEASEL/control/init $EWEASEL/control/catalog /marten/test'

In the above alias, you'll need to change "/home/dhollen" to your home
directory (not sure if this is used for anything).  You must also
change "/marten/test" to the output directory you want to use
(directory where tests are executed).

If you want to use a different version of the compiler, just change
the value of the $ISE_EIFFEL and/or $ISE_PLATFORM environment variables.
   
You can then run tests with commands like:

	ew -f 'test generic-zero-parms'		Run test generic-zero-parms
	ew -k -f 'test generic-zero-parms'	Also keep output directory
	ew -f 'kw pass'			Run all tests with keyword "pass"
	ew 				Run all tests

Before running any of the tests, you'll need a precompiled EiffelBase.
You should create it by copying the file eiffelbase_precomp.ace in
this directory to $ISE_EIFFEL/precomp/spec/$ISE_PLATFORM/base/Ace.ace
and then precompiling EiffelBase.

Please contact me if you have any problems or if you have any
questions about how EiffelWeasel works.

-- Dave
This directory is kept as it represents the state of EiffelBase before it was moved over the
  FreeELKS project on SoureForge. It is not compilable.
ABOUT ZEN CLASSIC

  The Zen Classic theme contains the old stylesheets from Zen 5.x-0.7. It was
  made a sub-theme of Zen because, while the theme looked good as-is, everyone
  was tired of undoing all that CSS when using it to develop a new theme. See
  http://groups.drupal.org/node/6353 and http://drupal.org/node/171464

SUPPORT

  The Zen Classic theme is left as-is for historical purposes and as a reference
  for people who used Zen 5.x-0.7 and earlier and have gotten used to themeing
  with it.

  However, since most developers dislike using it as a starting point for theme
  development, fewer people will be available to help with themeing issues you
  may encounter.
To get mediawiki filter
svn co
https://svn.origo.ethz.ch/origo/web/trunk/drupal/sites/all/modules/mediawiki_filter mediawiki_filter

To apply the mediawiki filter

cd mediawiki_filter
patch -p0 -i ../mediawiki_filter.patch

INSTALL)
sudo apt-get install subversion cvs p7zip-full unzip
sudo apt-get install patch indent
sudo apt-get install apache2
sudo apt-get install php5
sudo apt-get install libapache2-mod-php5
sudo apt-get install php5-gd 
sudo apt-get install mysql-server mysql-client php5-mysql
sudo a2enmod rewrite
#sudo a2enmod ssl
sudo /etc/init.d/apache2 restart

cd ~/
svn co https://svn.eiffel.com/eiffelstudio/trunk/Documentation/tools/web/trunk eiffeldoc
cd /var/wwww
ln -s ~/eiffeldoc/drupal/ p
cd ~/
cd eiffeldoc/bin
#edit etc/init_vars.sh  to set adapted values
sh ./eiffeldoc_install.sh

# then restore backup if available
# there is no initial settings yet ... (use the backup)


1) backup and restore
You should execute the eiffeldoc_backup and eiffeldoc_restore scripts using sudo
  in order to preserver the permissions and then the ownership.

2)...

Those scripts should be run as
sudo -u www-data
This tool is a temporary tool to convert the ISE's xmldoc format documentation
into a wikitext format, in order to import it into the next to be EiffelStudio documentation web application (online doc editing based on drupal)EiffelStudio extensions
=======================

This directory contains research extensions to offical EiffelStudio. They are independent and can be used to build a custom EiffelStudio with some additional tools.

Disclaimer
----------

The extensions are used mostly for reseach and are not intended for production use. There are no guarantees or official support for them.----------------------------------------------------------
:Status: in progress
:Description: quick help to use the build.eant script
:Date: 2008-Jan-31
:Categories: ec,compilation,build,scripts
----------------------------------------------------------

The geant's script  $EIFFEL_SRC/scripts/deliv.eant can be used to make a
developper delivery for "ec"
and other product from EiffelStudio open source project.

1) First you need to checkout the source.
for instance
* svn checkout https://svn.eiffel.com/eiffelstudio/trunk/Src ESdev_src
* set the EIFFEL_SRC environment variable to this path

Note: the whole trunk or branches is checkouted into a single folder

2) go to your compilation directory
for instance
cd $HOME/compile

3) You must be sure to have valid environment variables: $ISE_EIFFEL, EIFFEL_SRC, (and for Windows ISE_C_COMPILER)

4) using geant 
* To check if your environment fulfills the requirement
	geant -b $EIFFEL_SRC/build.eant check_setup

* To prepare 'ec' compilation, you need to compile various C libraries 
	geant -b $EIFFEL_SRC/build.eant prepare

* To finalize 'ec' bench
	geant -b $EIFFEL_SRC/build.eant compile

* To compile (workbench) 'ec' bench
	geant -b $EIFFEL_SRC/build.eant compile_workbench

* To make a EiffelStudio delivery  (developper)
	geant -b $EIFFEL_SRC/build.eant make_delivery

Those scripts are in progress for now.
Please report any issue on the forum: https://forum.eiffel.com/

-------------------------------------------
 Web: https://dev.eiffel.com/
 Web: https://svn.eiffel.com/eiffelstudio/
-------------------------------------------
Those binaries except `rt_convert.exe' are extracted from the MSYS distribution for MinGW.
See http://www.mingw.org for more details.
Since it is using .rc file to include resources, as it is using precompilation, you need to freeze the application to link the executable with this resource. This is needed in order to execute the example as expected.
To compile this example, first compile the C++ code.

On UNIX this can be done by doing something like

make mystring.o

ON Windows with Microsoft C compiler with something like

nmake mystring.obj
Usage: 
	process

Description:
Prompts for the name of a file with a polynomial description (see below),
reads a polynomial from the given file, prompts for integer values of the
variables, and evaluates the polynomial.

POLYNOMIAL DESCRIPTION 
      Grammar:
		LINE 			=  VARIABLES ":" SUM 
		VARIABLES	 	=  VAR .. ";" 
		SUM 			=  DIFF .. "+" 
		DIFF 			=  PRODUCT .. "-" 
		PRODUCT 		=  TERM .. "*" 
		TERM			=  SIMPLE_VAR | INT_CONSTANT | NESTED
		NESTED			=  "(" SUM ")" 

	Example: 
		x;y: x*(y+8-(2*x))

See the "Introduction to the Parsing Library" chapter of
EIFFEL: THE LIBRARIES for more information.
Set of small examples showing how to
use different EiffelStore capabilities

The following examples have been successfully tested with ODBC, Oracle 8.04 and Oracle 8i.

The suggested order of examples use is
the following:


0) esql
	Very useful to test your Database connection.

1) select
	The basic example for a query of your Database.

2) insert
	The basic example for an insert in your Database

3) nesting
	An Example of Nested queries.

4) rm2oom
	From a Relational Model to an Object Oriented Model.

5) oom2rm
	From an Object Oriented Model to a Relational Model.

6) convert 
	to exercise the flat file conversion utilities.


Don't forget to check the Readme file of each example before testing them.

Note: If ever you copy an example directory to another location, make sure to also copy the "Utilities" directory to be in the parent of the new location.


Object Oriented Model To Relational Model (OOM2RM)

This example illustrates how to dynamically generate
the description of a relational schema (with SQL statements) 
from the traversal of a network of Eiffel objects.

One Eiffel model sample is given in subdirectory Model1
and serves as the sample to use to generate the relational schema.

To apply the example on a model of your choice, replace
in the Ace file reference to the cluster Model1 with a reference
to your customized cluster.



CAVEAT
Some problems have been encountered when using generic containers classes
derived with simple type.
To overcome this problem, rather use ARRAY [INTEGER_REF] instead of 
ARRAY [INTEGER].

This example illustrates how RDBS tables can be
translated into Eiffel class definitions where
features are simply attributes matching the DB table fields.
Class descriptions are printed on standard output.
 
A specific repository is referred to by a name that should
match a RDB table name for which an Eiffel class equivalent
is requested.
This example create a stored procedure that may result more than one result sets, and retrieves data from the first available result sets.This examples illustrates the use of stored procedure with Unicode argument.The example shows EiffelStore maps ODBC SQL_GUID to STRING_8.
The example uses SQL Server 2010 as database which supports `uniqueidentifier' type. The type is used when creating demo data.

Before running the sample on Unix, one must do
link a specific file to data.sql as follows:

With ODBC:

	ln data.sql.odbc data.sql

The example demonstrates the way to use transaction with dbms that support it.

Note:
Only ODBC and MySQL (InnoDB engine) are tested supporting transaction.





This example illustrates how to customize actions
when retrieved selection results.

For ODBC, we have a better example in ..\nesting2.


Before running `book_select' sample, one must do
link a specific file to data.sql as follows:

With Oracle:

	ln data.sql.oracle data.sql

With Sybase:

	ln data.sql.sybase data.sql

With Ingres:

	ln data.sql.ingres data.sql

With ODBC:

	ln data.sql.odbc data.sql


Classes describing Eiffel objects to be used in various 
EiffelStore examples. BOOK, BOOK2, COUNTRY, HUMAN

Handles to be linked with generic examples (Oracle, Sybase, Ingres, ODBC)
This examples illustrates the use of stored procedure.

ODBC does not support creating stored procedure, so in order to run the
example on ODBC, you should use the host DBMS to create a stored procedure
"sel_proc" which should expect three parameters:
* new_date
* new_price
* new_author
and execute the following SQL statement:
UPDATE DB_BOOK SET price = :new_price, date = :new_date WHERE author = :new_author
Note: Only ODBC multiple connections are supported and tested.
This example illustrates the way one can convert
Unix flat files into class instances.

Changing a field (it's type or format) in an 
example.dat file, highlights the parser error 
detection mechanism.

When the example has been compiled, put the two
files "example1.dat" and "example2.dat" in the
directory "EIFGENs/W_CODE" or in "EIFGENs/F_code"
directory depending on your type of Eiffel
compilation.
Before running `dynamic_sql' sample, one must do
link a specific file to data.sql as follows:

With Oracle:

	ln data.sql.oracle data.sql

With MySQL:
	
	ln data.sql.mysql data.sql

With ODBC:

	ln data.sql.odbc data.sql



Before running `book_select' sample, one must do
link a specific file to data.sql as follows:

With Oracle:

	ln data.sql.oracle data.sql

With Sybase:

	ln data.sql.sybase data.sql

With Ingres:

	ln data.sql.ingres data.sql

With ODBC:

	ln data.sql.odbc data.sql



Usage:
	esql
	
This example illustrates how to access database information. 
SQL statements are filtered through a monitor and sent to the RDBMS.


Before running `numeric_types' sample, one must do
link a specific file to data.sql as follows:

With Oracle:

	ln data.sql.oracle data.sql

With Sybase:

	ln data.sql.sybase data.sql

With Ingres:

	ln data.sql.ingres data.sql

With ODBC:

	ln data.sql.odbc data.sql


EiffelStore Examples
--------------------

Usage:
	book_insert

This example illustrates how Eiffel users may access their selected DB
to insert or modify objects in existing tables.

An Eiffel object, say ``a book'', described by class BOOK, is inserted
into a repository (instance of class REPOSITORY) defined 
with `db_book' access key for instance. The repository name
should match an external RDB table named `db_book'.
In example, session terminates on inexisting RDB table.

Class DB_CHANGE encapsulates features supporting
insertion statements.
SQL insert statements insert new objects into existing repositories
(i.e existing RDM tables).

Class DB_CONTROL provides facilities to manage the session,
control the DB status, and query the results.
Usage:
	calculator

Description:
Basic calculator in reverse Polish form.  

Usage:
	structures

Description:
Allows the user to build a variety of data structures interactively
from a menu, call the viewer on them, and use the facilities of 
classes STORE and RETRIEVE to save/retrieve the state of the object.

In response to the "Please enter parameter 'item'" prompt, an 
integer is expected.
Producer-consumer example using the EiffelThread library.
---------------------------------------------------------

A proposition of Eiffel code for implementing
the famous Producer-Consumer example.

Implementation notes
--------------------

Condition variables are used to synchronize consumers and
producers access to the shared buffer.
A mutex synchronized the output.
race: simple example using EiffelThreads (ISE Eiffel 4.2)

DESCRIPTION:
This example consists in launching several racers, performing n iterations 
(number of racers and iterations are defined by the user). For instance,
you can try to launch 10 racers, running during 10 iterations.

Each racer is an EiffelThread: the number of racers and iterations can be 
as big as you want provided your system resource can manage it. 

race use threads and mutex but the Eiffelthreads library also provides
condition variables, semaphore, policy scheduling, thread control mechanisms.

Compilation:
In most case, you just need to melt the code and run the example.

Compatibility with Eiffel 4.1:
To compile this example with ISE Eiffel 4.1, you need to modify the Eiffel
code: the PROXY class was expanded in Eiffel 4.1, then you have to remove
the '!!' before any call to feature 'put' on a PROXY object. 

The use of proxy object: 
This example put into a proxy the mutex of
synchronisation, but in general you do not have to put any MUTEX, SEMAPHORE
or CONDITION_VARIABLE into it. All other shared object needs to be put into
a proxy. In the future releases, the proxies are bound to be obsolete and
Eiffel will manage internally every shared object.

info/            inspector/       read_and_write/  repository/      selections/      simple/

delivery/info: Information on Matisse database.
Ace.ace      get_info.e

delivery/inspector: Relationships of objects.
Ace.ace                  relationships_viewer.e

delivery/read_and_write: Read and write in database.
Ace.ace            read_and_write.e

delivery/repository: Using DB_REPOSITORY with matisse.
Ace.ace                  db_repository_tester.e   example.e

delivery/selections: 
with_container/     without_container/

delivery/selections/with_container: Using a structure.
class_stream/         object_stream/        relationship_stream/

delivery/selections/with_container/class_stream: OCS example.
Ace.ace     example.e

delivery/selections/with_container/object_stream: OOAS example.
Ace.ace      example.e    example.e%

delivery/selections/with_container/relationship_stream: ORS example.

delivery/selections/without_container: Using inheritance.
class_stream/

delivery/selections/without_container/class_stream: OCS example.
Ace.ace            control_action.e   example.e          shared_cursor.e

delivery/simple: A minimal application.
Ace.ace    simple.e
info/            inspector/       read_and_write/  repository/      selections/      simple/

delivery/info: Information on Matisse database.
Ace.ace      get_info.e

delivery/inspector: Relationships of objects.
Ace.ace                  relationships_viewer.e

delivery/read_and_write: Read and write in database.
Ace.ace            read_and_write.e

delivery/repository: Using DB_REPOSITORY with matisse.
Ace.ace                  db_repository_tester.e   example.e

delivery/selections: 
with_container/     without_container/

delivery/selections/with_container: Using a structure.
class_stream/         object_stream/        relationship_stream/

delivery/selections/with_container/class_stream: OCS example.
Ace.ace     example.e

delivery/selections/with_container/object_stream: OOAS example.
Ace.ace      example.e    example.e%

delivery/selections/with_container/relationship_stream: ORS example.

delivery/selections/without_container: Using inheritance.
class_stream/

delivery/selections/without_container/class_stream: OCS example.
Ace.ace            control_action.e   example.e          shared_cursor.e

delivery/simple: A minimal application.
Ace.ace    simple.e
See the README of the Eiffel2Java library ($ISE_LIBRARY/Eiffel2Java/README) for setup needed to compile.
This example shows how to change the cursor in an application and how to pick
and drop (PND) a list item using a dedicated cursor which changes according to
the area the pointer is over. 

The text field is the only widget which accepts to receive something (a string)
by the PND mechanim. When the pointer comes over that text field the cursor
appears with a shape corresponding to the selected list item. A right click will
write the cursor name in the field.
Usage:
	eiffel_scan eiffel_file_name

	For example:
		eiffel_scan sample_file.e

Description:
Example of a lexical analyzer for Eiffel.

If not previously built and stored, a stored lexical analyzer
object is created according to regular expressions described by the
file `eiffel_regular' and stored in `eiffel_lex' for doing lexical
analysis of Eiffel code.  (This may take a few moments.)  This object is
then used to analyze the file named by the argument.  Once the analyzer
has been built, subsequent calls will be much faster.

See the "Introduction to the Lexical Library" chapter of EIFFEL: THE
LIBRARIES for more information.
This folder is used to include projects in development but likely to have interface changes in the future.
The resources are provided as they are, use at your own risk.


Eiffel CMS Library
===============

Eiffel CMS library is build with [EWF](http://eiffelwebframework.github.io/EWF/) and inspired by [Drupal](https://www.drupal.org/).

The goal of the library is to provide the following features.

    - content type
    - user management
    - module design
    - theme
    - API


**Directory Structure**

 - library --Library
	 - layout -- application layout library.
	 - model -- domain model library.
	 - persistence -- persistence layer library.
	 - src -- cms source code.
 - example
	 - demo -- example using the cms library.
 - doc  -- Documentation. 	 

**Documentation**

 >[CMS concepts](/doc/concepts.md).
 
 >[CMS design](/doc/design.md).

 >[CMS tutorial](/doc/tutorial.md).
	 
This directory can be used to keep emails sent by the CMS.
Location for contributed CMS modules.
2017-03-03: (Breaking change) added notion of editor vs author. The table nodes and node_revisions have an extra "editor" field.
Collection of ROC CMS launcher ready to use.

- Include any-safe.ecf to use any of cgi, libfcgi or standalone connector.
- Include standalone-safe.ecf to use standalone connector.
- Include libfcgi-safe.ecf to use libfcgi connector.
- Include cgi-safe.ecf to use cgi connector.

In application, the root class need to inherit from ROC_CMS_LAUNCHER with adapted CMS_EXECUTION
descendant.

# OpenSSL support for EiffelNet #

Status: working on Windows and Linux

Contributors:
- Guus Leeuw jr. (itpassion.com)
- Jocelyn Fiat (eiffel.com)
- Javier Velilla (eiffel.com)


Supported Version
=================
OpenSSL version 1.1.1a.


Check OpenSSL library to more information.

# Criteria library

This library provides an implementation for the Filter|Criteria pattern.

(note: it is using the term "criteria" instead of more correct term "criterion", mainly to match existing known criteria pattern interfaces.)

Useful to filter a list.
Via a Criteria factory, it provides expression evaluation based on
binary operators and labels, such as "name:foo or tag:test" which
keeps items satisfying criteria "name=foo" and has tag "test".
But it is also possible to use directly the CRITERIA [G] objects, and combines them with operators like "and, or, not".

For advanced usage, see examples folder.
Eiffel SQLite wrapper for http://www.sqlite.org/ library.
This provides a statically linked sqlite, based in SQLite 3.7.8

Note: the extension loading feature is DISABLED.
  The amalgamation sqlite3.c file is compiled with flag -DSQLITE_OMIT_LOAD_EXTENSION=1 
  If you want to use the extension loading, you will need to modify a few files
   - have a look at Clib/Makefile.SH (and on Windows Clib/Makefile-win.sh)
   - and add in the sqlite(-safe).ecf files the code
		<external_library location="`$(ISE_LIBRARY)/library/api_wrapper/implementation/unix/Clib/dl-config --library`">
			<description>Required for linking SQLite</description>
			<condition>
				<platform excluded_value="windows"/>
			</condition>
		</external_library>
   - Then you might have to solve local issues related to undefined dlopen and similar


To edit sqlite database 
- https://addons.mozilla.org/en-US/firefox/addon/5817 for a free Firefox SQLite database manager.
- or even http://www.dbsoftlab.com/database-editors/database-browser/overview.html
- or http://sqlitestudio.pl/ 


Default implementation of memory and mysql controllers. To copy in the framework subfolder.
This folder is used to include external projects developped and maintained by
the other than Eiffel Software
This example is a simple demo to login with github.
Please get your github api key and secret into github.ini   (copy github.ini-dist as github.ini).
See https://github.com/settings/developers and be sure to set the correct callback URL.


Examples
========

This folder contains a few examples demonstrating the EiffelWeb framework solution.


## tutorial
This is a step by step tutorial to discover the EiffelWeb framework (EWF). 
How to build your first service, access the request data and send the response, also how to use the router to dispatch url easily.

## simple
This is a very simple system that can be executed as standalone, or hosted as CGI or libFCGI application on Apache, IIS, ...
You will learn how to customize the launcher (port number for standalone, ...), and how to use the interface of `WSF_RESPONSE` to send the response. 
(note: in this example, you have to deal with the Content-Type and Content-Length http header, this requires basic knowledge about the http protocol).
[learn more](./simple/README.md)

## simple_ssl
Almost the same as `simple` example, except this `simple_ssl` example is using only the `standalone` connector, and is supporting `https://` request. You will learn how to configure the .ecf file to add ssl support (see `<variable name="ssl_enabled" value="true"/>`), and how to enable it for instance via the `simple.ini` file (imported from the class `APPLICATION`).
[learn more](./simple_ssl/README.md)

## simple_file
This demonstrates how to return a file to the client. In this example you will learn how to dispatch manually the URL thanks to the `request.path_info` value.
You will also learn how to use the `WSF_RESPONSE.send (message)` interface that does not require you to know that much about http protocol since you will build `WSF_FILE_RESPONSE` and `WSF_NOT_FOUND_MESSAGE` objects.
[learn more](./simple_file/README.md)

## upload_image
This example shows how to handle file uploading, and also how to use the `WSF_FILE_SYSTEM_HANDLER` to serve local files (i.e a file server component).
It also uses the `WSF_ROUTER` component to route URL based on URI-template declaration.
[learn more](./upload_image/README.md)

## form
The EiffelWeb framework provides the `wsf_html` library, it is a set of classes to make it easier to generate html using Eiffel code. This includes web form generation, but also web form handling as it analyzes the request data to fill the web form response. 
This example shows a simple web form asking for name, birthday, and other radio,checkboxes,combo,file ... input data, and store the result in local directory.
[learn more](./form/README.md)

## desktop_app
Using the EiffelVision2 embedded web browser component, you will learn how to embed a web server in your GUI application. This way you can run locally a web server and display html pages in the GUI application itself.
[learn more](./desktop_app/README.md)

## proxy
Via the `wsf_proxy` library, it is possible to implement a simple reverse proxy service. 
Note: you need to edit the `application_execution.e` file to use proper remote service.
[learn more](./proxy/README.md)

## websocket
The EiffelWeb framework provides a websocket server and websocket client solution. This example demonstrates how to build a simple websocket service and consume it from a html+javascript page. This is a very simple chat application.
[learn more](./websocket/README.md)

## rest
### restbuck CRUD system
Restbuck Eiffel Implementation based on the book of REST in Practice.
This is an implementation of CRUD pattern for manipulate resources, this is the first step to use the HTTP protocol as an application protocol instead of a transport protocol.
[learn more](./rest/restbucks_CRUD/readme.md)

## debug
This example is a simple service that analyze the request and return a formatted output of the request data (query parameters, form parameters, environment variables, and so on). It could be used to debug client, or to experiment the EiffelWeb behavior on various connectors (standalone, apache, iis, ...).
[learn more](./debug/README.md)

## obsolete
A set of example using the old interface of EiffelWeb  (i.e version v0). We keep them as example for people having existing project based on EWF v0, but willing to compile with latest EiffelStudio, and latest EWF source code.
[learn more](./obsolete/README.md)

## _update_needed
This folder contains set of examples that need to be reviewed and updated for various reason.
[learn more](./_update_needed/README.md)
This example demonstrates the use of the `wsf_html` library for web form handling.

To simplify the code, it is also using the `WSF_RESPONSE.send (WSF_RESPONSE_MESSAGE)`,
thus no need to write the expected http header here.

The current code is a web interface form, returning html page as response.
		
notes:
* It is not using the `WSF_ROUTER` component to keep the example as simple as possible.
* It is also possible to use the `WSF_REQUEST.form_parameter (...)` directly, 
	  but WSF_FORM provides advanced processing.
* For a CRUD REST API, you can also use `WSF_FORM` to analyze the incoming POST values, 
	  however the html generation may be too verbose for a simple REST api.
	  
warning: depending on your system and connector, you may need to use `WSF_REQUEST.set_uploaded_file_path (...)`
		to tell the server where to store the temporary uploaded files.
		(this should be a directory with write permission for the server).
		For that
			- inherit from WSF_REQUEST_EXPORTER
			- in `execute` add at the beginning the call `request.set_uploaded_file_path (path-to-wanted-directory)` 
Uploading file example
======================

This example shows how to handle file uploading, and also how to use the `WSF_FILE_SYSTEM_HANDLER` to serve local files (i.e a file server component).
It also uses the `WSF_ROUTER` component to route URL based on URI-template declaration.

Examples to update
==================

This folder contains a few examples that needs to be updated.
It could be for many reason
- using obsolete components
- bad style
- not using latest EiffelWeb features
- issue in SCOOP concurrency mode
- ...

## filter
It demonstrates how to use the `WSF_FILTER` components. It can be used for authentication, and various usage (logging, setting specific http header such as CORS related settings, ...).

The current example has a main target for the server: "restbucks"
But we also provide "policy_driven_restbucks" target which is using the
policy-driven framework than help coder fulfill HTTP expectations.
Make sure to have the Clib generated in the related cURL library

- if you use EiffelStudio >= 7.0
  check %ISE_LIBRARY%\library\cURL\spec\%ISE_C_COMPILER%\$ISE_PLATFORM
  or    $ISE_LIBRARY/library/cURL/spec/$ISE_PLATFORM

- otherwise if you use earlier version
  check under ext/ise_library/curl/spec/...

And on Windows, be sure to get the libcurl.dll from  %ISE_LIBRARY%\studio\spec\%ISE_PLATFORM%\bin\libcurl.dll

= EiffelWeb Framework =

== Why would you use the Eiffel Web Framework ? ==

To enjoy the advantage of the Eiffel technology (language, DbC, methods, tools)
To write once and run on any web server, on any platforms thanks to the notion of connector.

== What is a connector? ==

A connector is the layer between the underlying httpd server, and your application based on EiffelWeb.
Currently, 4 connectors are available within EiffelWeb (but others are available outside).
* CGI: the common CGI application (apache, iis, ...)
* FastCGI: on any server supporting libfcgi handling (apache, iis, ...)
* Standalone: a standalone Eiffel Web server, it can be run anywhere easily, and debug simply with EiffelStudio's debugger. It supports all concurrency modes, and require EiffelStudio >= 16.05

Supporting a new connector is fairly simple, it just has to support the simple EWSGI specification which is really small. Then EiffelWeb will bring the power on top of it.

So you can build your application and be sure you will be able to run it ... anywhere thanks to the concept of connectors.

== EWSGI specification ==

EiffelWeb relies on a small core specification, named EWSGI (Eiffel Web Server Gateway Interface). 
It is very limited on purpose to allow building new connector very easily.

For now, you just need to know EiffelWeb is compliant with EWSGI specification.

= Tutorial =

Now let's discover the Eiffel Web Framework with this tutorial:

# [[step_1.wiki|Step #1]]: You will learn first, how to get and install EiffelWeb.
# [[step_2.wiki|Step #2]]: build a simple Hello World application
# [[step_3.wiki|Step #3]]: use the parameter to build dynamic service
# [[step_4.wiki|Step #4]]: And you will learn how to dispatch URL


This folder contains 2 alternatives code

1) "message" using the WSF_MESSAGE_EXECUTION interface, i.e
	message: WSF_RESPONSE_MESSAGE
		do
			...
		end


2) "launcher" using the WSF_RESPONSE_SERVICE interface, but it uses a launcher to start the service, instead of inheriting from WSF_DEFAULT_SERVICE

SSL support with Standalone connector
=====================================

Almost the same as `simple` example, except this `simple_ssl` example is using only the `standalone` connector, and is supporting `https://` request. You will learn how to configure the .ecf file to add ssl support (see `<variable name="ssl_enabled" value="true"/>`), and how to enable it for instance via the `simple.ini` file (imported from the class `APPLICATION`).

Proxy example
=============

Via the `wsf_proxy` library, it is possible to implement a simple reverse proxy service. 
Note: you need to edit the `application_execution.e` file to use proper remote service.
(You can use for instance any of the EWF examples as remote server, or also existing public server).
This example demonstrates the use of embedded Vision2 web browser component, and embedded EWF server (using standalone).

Simple example
==============

This is a very simple system that can be executed as standalone, or hosted as CGI or libFCGI application on Apache, IIS, ...
You will learn how to customize the launcher (port number for standalone, ...), and how to use the interface of `WSF_RESPONSE` to send the response. 
(note: in this example, you have to deal with the Content-Type and Content-Length http header, this requires basic knowledge about the http protocol).

File response example
=====================

This demonstrates how to return a file to the client. In this example you will learn how to dispatch manually the URL thanks to the `request.path_info` value.
You will also learn how to use the `WSF_RESPONSE.send (message)` interface that does not require you to know that much about http protocol since you will build `WSF_FILE_RESPONSE` and `WSF_NOT_FOUND_MESSAGE` objects.

This example is a simple service that analyze the request and return a formatted output of the request data (query parameters, form parameters, environment variables, and so on). It could be used to debug client, or to experiment the EiffelWeb behavior on various connectors (standalone, apache, iis, ...).
Docker container for EiffelWeb debug example with apache2+libfcgi.
==================================================================

This example demonstrates the use of EiffelWeb with Apache2, using the libfcgi connector.
For that, it is using the Docker solution to show the compilation and configuration steps.

To build the docker image:

```
	docker build -t local/ewf-debug-httpd .
```

To run the docker image in a self-destroyed container:
```
	docker run --rm -dit -p 8080:80 --name my-ewf-debug local/ewf-debug-httpd
```

Notes:
	- `--rm` : to remove the container after the execution
	- `-p 8080:80` : to map internal listening port 80 to localhost port 8080.
	- on Linux, you may need to use `sudo` to be able to use `docker`
	- depending on the docker installation, you may need to add an extra `-e ISE_PLATFORM=linux-x86` to force execution in 32bits.
	- This docker example is simple on purpose. For production it should be improved and optimized to keep the image smaller and more customizable.
	- For more advanced Docker usage, please refer to official https://www.docker.com/ website.

The EiffelWeb framework provides a websocket server and websocket client solution. This example demonstrates how to build a simple websocket service and consume it from a html+javascript page. This is a very simple chat application.
An encryption library in Eiffel

Contribution from Colin LeMahieu
see original source: https://github.com/clemahieu/eelGoal: library to parse wikitext
Goal 2: wikitext to xhtml rendering tool


copyright: "2011-2014, Jocelyn Fiat and Eiffel Software"
license: "Eiffel Forum License v2 (see http://www.eiffel.com/licensing/forum.txt)"
source: "[
		Jocelyn Fiat
		Contact: http://about.jocelynfiat.net/
	]"
﻿[![Build Status](https://travis-ci.org/eiffelhub/json.svg?branch=master)](https://travis-ci.org/eiffelhub/json)

Readme file for eJSON
=====================

- team: "Jocelyn Fiat, Javier Velilla"
- previous contributors: "Paul Cohen"
- date: "2018-sept-19"

## Introduction

eJSON stands for Eiffel JSON library and is a small Eiffel library for dealing
with the JSON format. This library provides a JSON parser and visitors,
including a pretty printer.

The "serialization" interfaces replace the obsolete converters interfaces.

## Legal stuff

eJSON is copyrighted by the authors Jocelyn Fiat, Javier Velilla, and others. It is licensed under the MIT License. See the file license.txt in the same directory as this readme file.

## Versioning scheme

eJSON version numbers has the form: `"major number"."minor number"."patch level" `

eJSON will retain the major number 0 as long as it has beta status. A change in major number indicates that a release is not backward compatible. A change in minor number indicates that a release is backward compatible (within that major
number) but that new useful features may have been added. A change in patch level simply indicates that the release contains bug fixes for the previous release. Note that as long as eJSON is in beta status (0.Y.Z) backward compatibility is not guranteed for changes in minor numbers!

## Documentation

Currently the only documentation on eJSON is available at: `https://github.com/eiffelhub/json/blob/master/doc/user_guide.md`

## Requirements and installation

EJSON requires that you have:

One of the following compiler combinations installed:
   * ISE Eiffel 17.05 or later.
   * gec [try to test]

eJSON probably works fine with other versions of the above compilers.
There are no known platform dependencies (Windows, Linux).

To install eJSON simply extract the ejson-X.Y.Z.zip file to some appropriate place on your hard disk. There are no requirements on environment variables or registry variables. 
Note eJSON is also delivered within EiffelStudio release, under `$ISE_LIBRARY/contrib/library/text/parser/json`

To verify that everything works you should compile the example programs and/or
the test program.

## Contents of eJSON

All directory names below are relative to the root directory of your ejson installation. 

- doc:         Contains documentation file.
- examples:    Contains example codes.
- library:     Contains the actual eJSON library classes.
- test:        Contains test suite for eJSON.

## Contacting the Team

Contact the team: https://github.com/eiffelhub/json/issues

## Releases

```
Version Date            Description
------- ----            -----------
0.10.0 2018-11-14	Improved parsing performance (speed and memory).
					Allow to change default size for json array and object created during parsing.
0.9.0  2018-09-19	Added basic serialization
					Updated the serialization example to demonstrate the use of custom (de)serializers.
					Added JSON_VALUE.chained_item (a_key): JSON_VALUE to be able to access
					  `json@"person"@"address"@"city"` and return associated JSON value if any, 
					   otherwise JSON_NULL.

0.8.0  2018-09-13	Ensure the `JSON_STRING`.item is really UTF-8 encoded (even for characters between 128 and 255)!
					Properly encode null character as \u0000 .
					Unescape escaped unicode in unescape_to_string_8 when it represents a valid `CHARACTER_8` value.
					Fixed parsing of integer 64 value
0.7.1   2017-03-20	Added `JSON_VALUE.is_string` ... `is_null` boolean query for convenience.
0.7.1   2017-03-20	Added `JSON_VALUE.is_string` ... `is_null` boolean query for convenience.
0.7.0   2016-08-01	New JSON serialization implementation (to replace the obsolete converters).
0.6.0   2014-11-17	Fixed various issue with parsing string (such as \t and related),
					Implemented escaping of slash '/' only in case of '</' to avoid 
					  potential issue with javascript and </script>
					Many feature renaming to match Eiffel style and naming convention, 
					  kept previous feature as obsolete.
					Restructured the library to make easy extraction of "converter" 
					classes if needed in the future.
					Marked converters classes as obsolete.
0.5.0   2013-11-31	Added `JSON_ITERATOR`, simplified `JSON_OBJECT`
0.4.0   2012-12-12	Updated documentation URI
0.3.0   2011-07-06	JSON Factory Converters
0.2.0   2010-02-07	Adapted to EiffelStudio 6.4 or later, supports void-safety
0.1.0   2010-02-07	First release, Adapted to SmartEiffel 1.2r7 and EiffelStudio 6.2 or previous
```

# URI Template

## Overview
Implement URI Template as described at http://tools.ietf.org/rfc/rfc6570.txt

Support for URI template string expansion
But also partial URI Template matching

## Usage

## Examples

HTML5 and microdata

This library provides a way to extract MicroData from HTML5 content.

As currently this is implemented redefining the implementation of the XML parser, this is not compliant with all kind of html.
It accepts attribute without value (hopefully to support itemscope ...).
It accepts attribute value with single quote, double quote or no quote at all.
It may have trouble with tag without end-tag such as <dd>...<dd>... and so on.

This will be improved progressively, but for now, this could be used with html5 code you generate yourself.

# Smarty template engine for Eiffel

# Overview
This smarty library is a template engine inspired by smarty php template engine.
It provides a parser and the engine execution itself in order to generate for instance html output.
However it can be used to generate any kind of output (xml, json, html, ...).

The syntax is similar to http://www.smarty.net/ , so for now have a look at their documentation, but as quick documentation, please see following documentation by example.

As any template engine, the input includes 
- the template files themselves.
- and data, the data are mainly Eiffel objects associated with name, then it is possible to access the attributes value, and additional functions (see the "inspector" section).

# Quick documentation
## Instructions and related syntax
### Current implementation:
* actions: assign, include, if, unless, foreach, nl2br, htmlentities, literal
* condition: condition, isempty, isset
See below for details

### How to use a value associated with name "foo"?
>   {$foo/}

### How to use expression foo.bar ?
>   {$foo.bar/}

note: `bar' has to be an attribute, or declared via the "inspector" mechanism (see related section)

### How to assign a variable named "title" with a value? (or associate a value with a name "title")
>   {assign name="title" value="a new title"/}

### How to assign a variable named "title" with an expression $foo.bar?
>   {assign name="title" expression="$foo.bar"/}

### What about if, then, else, end conditional instructions?
####**keyword: if**
  - pseudo code using a variable:
     `if var_enabled then blockA end`
>    {if condition="$var_enabled"}blockA{/if}

  - pseudo code using an expression: 
     `if foo.is_valid then blockA end`
>    {if condition="$foo.is_valid"}blockA{/if}

  - pseudo code testing if expression is set (i.e registered or not Void):
     `if foo.bar /= Void then blockA end`
>    {if isset="$foo.bar"}blockA{/if}

  - pseudo code testing if expression is empty:
     `if foo.bar.is_empty then blockA end`
>    {if isempty="$foo.bar"}blockA{/if}

####**keyword: unless**
  - pseudo code using the negation of expression: 
     `if not foo.is_valid then blockA end`
>    {unless condition="$foo.is_valid"}blockA{/unless}

####**keywords: if,unless to mimic if then else end**
 - pseudo code with else part:
     `if foo.is_valid then blockA else blockB end`
     (note: there is no "else" implementation yet)
>    {if isempty="$foo.is_valid"}blockA{/if}
>    {unless isempty="$foo.is_valid"}blockB{/unless}

     for performance, one can use a variable
>    {assign name="condition_foo_is_valid" expression="$foo.is_valid"/}
>    {if condition="$condition_foo_is_valid"}blockA{/if}
>    {unless isempty="$condition_foo_is_valid"}blockB{/unless}

### How to process an instruction for each item of a collection?
  **keyword: foreach**
  - traversing an iterable structure (as a LIST)
>     {foreach item="the_value" from="$list"}{$the_value/}{/foreach}

  - traversing an iterable table (as a HASH_TABLE)
>     {foreach item="the_value" key="the_name" from="$table"}{$the_name/}={$the_value/} , {/foreach}

### How to include another template file?
  **keyword: include**
  - include template file "bar.tpl"
>    {include file="bar.tpl" /}

  - include template file, and assign variable valid only in the scope of the included file
>    {include file="bar.tpl"}{assign name="data" expression="foo-$index" /}{/include}

  - include the content of a file without processing it as template
>    {include file="bar.tpl" literal="true" /}

### How to easily encode text for html output?
  **keyword: htmlentities**
>    {htmlentities}5 > 3{/htmlentities}

     This will generate  `"5 &gt; 3"`

### How to easily convert space into html space?
  **keyword: nl2br**
  - Convert new lines into <br/> html tags
>    {nl2br}line 1 %Nline 2 %Nline 3{/nl2br}

     This will generate  `"line 1 <br/>line 2 <br/>line 3"`

  - Convert new lines into <br/> html tags, and tabs with 4 spaces &nbsp;
>    {nl2br}line%T1 %Nline%T2{/nl2br}
	 
     This will generate  `"line&nbsp;&nbsp;&nbsp;&nbsp;1 <br/>line&nbsp;&nbsp;&nbsp;&nbsp;2"`

### How to exclude text from template processing?
  **keyword: literal**
  - Keep the following text "{$abc/}" unchanged
>    {literal}{$abc/}{/literal}
	 
     This will generate "{$abc/}" unchanged. This can be useful to display text that has curly braces.

## Expression and inspector
### Definition  The expressions can be
  - manifest string as  `this is a text`
  - manifest string with variable  `this is a text, var={$var/}`
  - a variable `{$var/}`
  - an expression related to call foo.bar.var `{$foo.bar.var/}`

### Restrictions
  - when an expression can not be evaluated (due to unknown variable or call), `${abc.out.bad}` will be converted as an error message displayed usually like `{!! Invalid name !!}`
  - by default, the calls in expression can only access attribute value, for instance `{$foo.out.count/}` will not be what could be expected, since `out` for instance is not an attribute.

### Solutions for attribute restrictions
  - If ever, you want to be able to call `${foo.new_bar}` where `class FOO feature new_bar: BAR do .. end end`, by default this will not be accepted, but using the mechanism of the `TEMPLATE_INSPECTOR`, this is now possible. This is pretty simple:
  * create for instance a new class FOO_TEMPLATE_INSPECTOR
>  class FOO_TEMPLATE_INSPECTOR 
>  inherit
>      TEMPLATE_INSPECTOR 
>         redefine internal_data end
>  
>  create register
>  
>  feature -- Internal data
>	internal_data (fn: STRING; obj: detachable FOO): detachable CELL [detachable ANY]
>		local
>			l_fn: STRING
>		do
>			if obj /= Void then
>				if fn.is_case_insensitive_equal ("new_bar") then
>					Result := obj.new_bar
>				end
>			end
>		end
>  end

  * Register this inspector in the code, before executing the template execution with
>   local inspector: TEMPLATE_INSPECTOR do
>   create {FOO_TEMPLATE_INSPECTOR} inspector.register (({detachable FOO}).out)

## How to use this template engine ?
 - Examples: check the examples folder to learn from the code. (The tests folder can also be helpful)
 - otherwise, below a simple code

>  class 
>  	APP
>  
>  inherit 
>  	SHARED_TEMPLATE_CONTEXT
>  
>  create
>  	make
>  
>  feature -- Initialization
>  	make
>  		local
>  			l_foo_object: FOO
>  			template: TEMPLATE_FILE
>  			l_inspector: TEMPLATE_INSPECTOR
>  		do
>  				-- Initialize data
>  			create l_foo_object.make ("An object FOO")
>  
>  				-- The template files are inside folder "tpl"
>  			template_context.set_template_folder ("tpl")
>  
>  				-- Register the eventual template inspectors (see related section for help)
>  			create {FOO_TEMPLATE_INSPECTOR} l_inspector.register ("detachable FOO")
>  
>  				-- The template file to process is "test.tpl"
>  			create template.make_from_file ("test.tpl")
>  
>  				-- Associate data with name
>  			template.add_value (l_foo_object, "foo")
>  			template.add_value ("A nice title", "title")
>  
>  				-- Then analyze and generate output as expected
>  			template.analyze
>  			template.get_output
>  
>  				-- Print the result
>  			print (template.output)
>  		end
>  
>  end

## Future evolutions
  - Allow  `${foo}`  without the ending slash, for now it is required to write `${foo/}`
  - Add implementation for `{else}`
  - Add other instructions if needed.
  - separate the template representation from the template execution
  - inspector:
    - review the inspector design, and use TYPE instead of string for registration
    - avoid use of once functions, so that templates do not share the same inspector for the whole application

# Project Status

- **Status**: NEED-IMPROVEMENT, NEED-CLEANING
- **Goal**: build template library inspired by the php smarty template engine
- **reference**: http://www.smarty.net/
- **project**: https://github.com/eiffelhub/template-smarty

    copyright: "2011-2013, Jocelyn Fiat, Javier Velilla and EiffelSoftware"
    
    license: "Eiffel Forum License v2 (see http://www.eiffel.com/licensing/forum.txt)"
    
    source: "[
                 Jocelyn Fiat
                 Contact: http://about.jocelynfiat.net/
         ]"

# collection of Encoders

## Overview

## Requirements
* Eiffel encoding libraries

## Usage

## Examples


# Web Server Framework

User friendly framework to build Eiffel Web server applications.
It is built on top of [EWSGI](../ewsgi/) to benefit from the various EWSGI connectors.

## Requirements
* [EWSGI](../ewsgi)
* [HTTP](../../protocol/http)
* [URI template](../../protocol/uri_template)

## Content
* Core classes for the Web Server Framework
* [Router](router) library

## Overview

## Usage

## Examples
# Router 

## Requirements
* [URI Template](../../../protocol/uri_template)

## Overview

## Usage

# Introduction

The basic idea of a filter is to pre-process incoming data and post-process outgoing data.
Filters are part of a filter chain, thus following the [chain of responsability design pattern](http://en.wikipedia.org/wiki/Chain-of-responsibility_pattern).

Each filter decides to call the next filter or not.

# Levels

In EWF, there are two levels of filters.

## WSF_FILTER

Typical examples of such filters are: logging, compression, routing (WSF_ROUTING_FILTER), ...

## WSF_FILTER_HANDLER

Handler that can also play the role of a filter.

Typical examples of such filters are: authentication, ...

# References

Filters (also called middelwares) in other environments:
* in Python: http://www.wsgi.org/en/latest/libraries.html
* in Node.js: http://expressjs.com/guide.html#middleware
* in Apache: http://httpd.apache.org/docs/2.2/en/filter.html
# Eiffel Web Server Gateway Interface 

## Overview
The main goal of this library is to provide a common layer on top of many different connectors.
A connector is a library used for the integration of Eiffel web server application with an underlying httpd server technology such as CGI, libFCGI, or even standalone Eiffel Web Standalone (which is a httpd server written in Eiffel).

Then one can build an Eiffel web service compliant with EWSGI specification, and thus with the same code (or almost), this could be compiled to run on any available connectors.

## Usage


## 
# Eiffel libFCGI wrapper library

This Eiffel library wraps the libFCGI devkit from http://www.fastcgi.com/devkit/libfcgi/

## Windows
To compile your own binaries .lib and .dll on __Windows__: [read more](Clib/README.md)

## Others

### Debian based system (ubuntu, ...)
To install the fcgi lib on Ubuntu (or any Debian based system), you can use
> sudo apt-get install libfcgi-dev

### Mac OS X
To install the fcgi lib on Mac OS X, you can use [MacPorts](http://www.macports.org/)
> sudo port install fcgi
# libFCGI for Eiffel libFCGI wrapper library

## On Windows

The Eiffel libFCGI wrapper needs a modified version of libFCGI (provided by http://www.fastcgi.com/devkit/libfcgi/)

To get the full source code:
  rd /q/s libfcgi
  git clone https://github.com/EiffelSoftware/libfcgi libfcgi

And then to build the needed .dll and .lib file, use either:
  build_win32.bat 
  or build_win64.bat

## On other platorms

You can use the original version of libfcgi

### Debian based system (Ubuntu, ...)
On Ubuntu (or any Debian based system):
> sudo apt-get install libfcgi-dev


### Mac OS X
On Mac OS X:
> sudo port install fcgi
== libFCGI source code for the libFCGI Eiffel wrapper ==

This folder contains the source code required to compile the Windows versions of libfcgi

It is a __modified__ version to enable us to compile libfcgi on __Windows 64bits__

We used the patch located under doc\fcgi-2.4.0-x64.patch applied against the original version of libFCGI from http://www.fastcgi.com/devkit/libfcgi/

This folder contains only the files related to libfcgi on Windows.

You can get the full source code at https://github.com/EiffelSoftware/libfcgi


SEE ALSO in the folder "doc" the original README files
ChangeLog from 2.4.0 to 2.4.0-x64:

* Fixed to support 64bit build of library and sample executables for Windows.
* Fixed socklen_t detection failure problem in configure script for Linux.


What we've done to support 64bit build:

* Converted Win32/*.{dsw,dsp} files to Win32/*.{sln,vcproj} files
  (Visual Studio 2008 solution/project files).
* Added platform "x64" for Visual Studio solution.
* Fixed type size problem (pointer, size_t, etc.)
  to support both 32/64 bit build
  using intptr_t, uintptr_t, and so on.
* Fixed to check range of each numeric variable with ASSERT()
  before using type cast for demotion(narrowing).
* Replaced several standard functions to recommended ones.
  getpid() --> _getpid(), and so on.
* Fixed several functions to support both 32/64 bit build.
  AlignInt8(), AlignPtr8(), and so on.
* Removed almost all build warnings on Visual Studio 2008.
  with PreprocessorDefinitions:
  _SCL_SECURE_NO_WARNINGS and _CRT_SECURE_NO_WARNINGS.
* Removed almost all build warnings on Linux.


Current status:

* Tested the patch on Windows Server 2008 SP1 (64bit).
  with apache httpd 2.2.10 (32bit) and mod_fastcgi-SNAP-0811090952.
  Both 32/64 bit sample executables are working.
  We could not build and test two samples: threaded and log-dump.
* Tested the patch on CentOS 5.3 (64bit) with gcc-4.3.3.
  For 32bit build, we used gcc -m32 option.
  Both 32/64 bit sample executables are working except log-dump.
  We could not find out the usage of log-dump
  so that we could not test it.


How to build:

1. For Windows

1-1. Extract fastcgi-2.4.0.tar.gz

> tar xzf fastcgi-2.4.0.tar.gz

1-2. Apply this fastcgi-2.4.0-x64.patch

> cd fastcgi-2.4.0
> patch -p1 < ../fastcgi-2.4.0-x64.patch

1-3. Open fastcgi-2.4.0/Win32/FastCGI.sln with Visual Studio 2008 and build.

Debug and Release build on Win32 and x64 are supported.

Build with 'nmake' is not supported, since we could not find out
suitable project converter and we can use 'devenv' command line instead.


2. For Linux

2-1. Do the same process as (1-1).
2-2. Do the same process as (1-2).

2-3. Remake configure script.

> libtoolize -c -f
> aclocal
> autoheader
> automake -a -c -f
> autoconf

2-4. Configure and make

> ./configure
> make
> make install

If you need, NDEBUG preprocessor definition should be specified
to eliminate ASSERT check for release build.


FastCGI Developer's Kit README
------------------------------

    $Id: README,v 1.21 2003/01/19 17:19:41 robs Exp $
    Copyright (c) 1996 Open Market, Inc.
    See the file "LICENSE.TERMS" for information on usage and redistribution
    of this file, and for a DISCLAIMER OF ALL WARRANTIES.

Basic Directions
----------------

Unix:

    ./configure
    make
    make install

Win32:

    nmake -f Makefile.nt

    (or use the MSVC++ project files in the Win32 directory)


CHANGES
-------

For more detail regarding changes, please consult the cvs log available 
on http://fastcgi.com/.


2.4.0
-----

 *) When closing connections, shutdown() the send side of TCP sockets to 
    prevent a TCP RST from trashing the reciept of data on the client (when
    the client continues to send data to the application).

 *) [WIN32] force an exit from the ShutdownRequestThread when a shutdown is
    signaled and NamedPipes are in use.

 *) Use streamsize and char_type in the C++ API.

 *) [WIN32] Eliminate the (partial and broken) use of OverlappedIO - this 
    was causing a loose spin in acceptNamedPipe().

 *) Fix a bug that caused an assert to pop when an async file descriptor was
    numbered greater than 16. Kevin Eye [eye@buffalo.edu]

 *) Update the echo-cpp example to show the restoral of the original
    streambufs.  Trub, Vladimir [vtrub@purolator.com]

 *) Fix a bug a that caused the lib to crash under certain circumstances
    when an error occured on a read

 *) Test for iostreams that support a streambuf assigment operator

 *) (WIN32) Fixed initialization of the accept mutex when OpenSocket() was used.
    Niklas Bergh [niklas.bergh@tific.com]


2.2.2  
-----

 *) Added support for shared libraries.

 *) Added support for a graceful shutdown via an event under Win32.

 *) Added default signal handlers for PIPE, USR1, and TERM.

 *) Fix some minor bugs in the 0S_ layer.

 *) Fixed the C++ streambuf implementation.


Changes with devkit 2.1.1 
-------------------------

 *) Fixed an unintentional sign extension during promotion  in Java's
    FCGIInputStream.read(). Takayuki Tachikawa <tachi@po.ntts.co.jp>

 *) Cleaned up warnings in examples (mostly main() complaints).

 *) Removed examples/tiny-cgi.c (it wasn't a FastCGI application?!).

 *) Remove some debugging code and clean up some gcc warnings in cgi-fcgi.c.

 *) Add multithread support to the fcgiapp lib and an example multithreaded
    application, threaded.c.  Based on work by Dennis Payne
    <dpayne@softscape.com> and Gene Sokolov <hook@aktrad.ru>.

 *) Remove the printf() and #include of stdio.h from examples/echo2.c.

 *) Remove the static initialization of _fcgi_sF[] because on glibc 2.x based
    systems stdin/stdout/stderr are no longer static.

 *) Flush FastCGI buffers at application exit.  <eichin@fastengines.com>

 << INSERT OTHER STUFF HERE >>


What's New: Version 2.0b2, 04 April 1997
--------------------------------------

Some additional bug fixes, mostly on NT port.  The following list
of the bugs that have been and fixed:
  1. Updated build_no_shell.bat to create a FcgiBin directory under the
     top level of the FastCGI kit and copy all executables and the
     FastCGI dll there.  This makes it easier to use.
  2. Corrected the Unix version of OS_SpawnChild so that it didn't close
     the listenFd when forking off child processes.  This code would
     affect the cgi-fcgi application on Unix.  The problem is that it
     could only start one fastcgi process.  Any other processes would not
     get the listen file descriptor and they would die.
  3. Corrected cgi-fcgi.c so that it properly handled large posts.  The
     bug was introduced with the asynchronous I/O model implemented for
     the Windows NT port.  The problem was not clearing a bit indicating
     that a read had completed.  This caused the application to stall.
  4. Corrected OS_DoIo, the function used for scheduling I/O for cgi-fcgi.
     It had a bug where it wasn't creating a copy of the file descriptors
     used for I/O.  This would cause the master list of FDs to watch to be
     reset and thus would hang the application because we would no longer
     watch for I/O on those file descriptors. (This problem was specific to
     Unix and only happened with the cgi-fcgi application.)
  5. Cleaned up several compilation warnings present on OSF.


What's New: Version 2.0b1, 24 March 1997
--------------------------------------

This "beta" release adds the functionality of "cgi-fcgi" to the
Windows NT platform and allows for creation of FastCGI applications
running in Win32 environment.  There is almost no new documentation
provided, but will become part of this kit in the official release.
  1. Added FastCGI libraries running on Windows NT 3.51+
  2. Rename errno to FCGI_errno in the FCGX_Stream, which was causing
     problems on some Linux platforms and NT.
  3. Fixed a parenthesis problem in FCGI_gets


What's New: Version 1.5.1, 12 December 1996
--------------------------------------

This release introduces mostly bug fixes, without any additional
functionality to the kit.
  1. Conditional compilation for the hp-ux compiler.
  2. Loop around the accept() call to eliminate "OS Error: Interrupted
     System Call" message from appearing in the error logs.
  3. Casting of the FCGI_Header to (char *), which eliminates the
     assertion failure "bufPtr->size>0".


What's New: Version 1.5, 12 June 1996
--------------------------------------

General:

  Added a white paper on FastCGI application performance to the
  doc directory.  Generally brought the other docs up to date.

  Rearranged the kit to put more emphasis on running FastCGI-capable
  servers and less on running cgi-fcgi.  Added
  examples/conf/om-httpd.config, a config file that demonstrates all
  of the example apps.  (Would like to have similar configs for NCSA
  and Apache.)

  Added the tiny-authorizer and sample-store applications to
  the examples.  These are explained in the index.html.

    In addition to everything else it does, sample-store demonstrates
    a bug in the Open Market WebServer 2.0: When an Authorizer
    application denies access, the server tacks some extra junk onto
    the end of the page the application returns.  A little ugly but
    not fatal.

C libraries:

  Added the functions FCGX_Finish and FCGI_Finish.  These functions
  finish the current request from the HTTP server but do not begin a
  new request.  These functions make it possible for applications to
  perform other processing between requests.  An application must not
  use its stdin, stdout, stderr, or environ between calling
  FCGI_Finish and calling FCGI_Accept.  See doc/FCGI_Finish.3 for
  more information.  The application examples/sample-store.c demonstrates
  the use of FCGI_Finish.

  Added conditional 'extern "C"' stuff to the .h files fcgi_stdio.h,
  fcgiapp.h, and fcgiappmisc.h for the benefit of C++ applications
  (suggested by Jim McCarthy).

  Fixed two bugs in FCGX_VFPrintF (reported by Ben Laurie).  These
  bugs affected processing of %f format specifiers and of all format
  specifiers containing a precision spec (e.g "%12.4g").

  Fixed a bug in FCGX_Accept in which the environment variable
  FCGI_WEBSERVER_ADDRS was being read rather than the specified
  FCGI_WEB_SERVER_ADDRS.  Fixed a bug in FCGX_Accept in which the
  wrong storage was freed when FCGI_WEB_SERVER_ADDRS contained more
  than one address or if the address check failed.

  Changed FCGX_Accept to avoid depending upon accept(2) returning the
  correct value of sin_family in the socketaddr structure for an
  AF_UNIX connection (SCO returns the wrong value, as reported by Paul
  Mahoney).

  Changed the error retry logic in FCGX_Accept.  FCGX_Accept now
  returns -1 only in case of operating system errors that occur while
  accepting a connection (e.g. out of file descriptors).  Other errors
  cause the current connection to be dropped and a new connection to
  be attempted.

Perl:

  Changed FCGI.xs to make it insensitive to Perl's treatment of
  environ (we hope).  Changed FCGI::accept so the initial environment
  variables are not unset on the first call to FCGI::accept (or on
  subsequent calls either).  Added the echo-perl example
  program.  Added a workaround for the "empty initial environment bug"
  to tiny-perl-fcgi.  Changed the example Perl scripts to use a new
  symbolic link ./perl, avoiding the HP-UX 32 character limit on the
  first line of a command interpreter file.

  Because the FastCGI-enabled Perl interpreter uses the C fcgi_stdio
  library, it picks up all the changes listed above for C.  There's
  a new Perl subroutine FCGI::finish.

Tcl:

  Fixed a bug in tclFCGI.c that caused the request environment
  variables to be lost.  Changed FCGI_Accept so the initial
  environment variables are not unset on the first call to FCGI_Accept
  (or on subsequent calls either).  Added the echo-tcl example
  program.  Fixed another bug that caused Tcl to become confused by
  file opens; as a side effect of this change, writes to stdout/stderr
  that occur in an app running as FastCGI before FCGI_Accept is called
  are no-ops rather than crashing Tcl.  Changed the example Tcl
  scripts to use a new symbolic link ./tclsh, avoiding the HP-UX 32
  character limit on the first line of a command interpreter file.

  Because the FastCGI-enabled Tcl interpreter uses the C fcgi_stdio
  library, it picks up all the changes listed above for C; there's
  a new Tcl command FCGI_Finish.

Java:

  Fixed a sign-extension bug in FCGIMessage.java that caused bad encodings
  of names and values in name-value pairs for lengths in [128..255].
  Made small cleanups in the Java example programs to make them more
  consistent with the other examples.



What's New: Version 1.4, 10 May 1996
--------------------------------------

Includes Java classes and Java examples.



What's New: Version 1.3.1, 6 May 1996
--------------------------------------

New, simplified, license terms.  Includes an expanded whitepaper that
describes FastCGI support in Open Market's Secure WebServer 2.0.
Includes Open Market FastCGI 1.0 Programmer's Guide.  Includes
"FastCGI: A High-Performance Gateway Interface", a position paper
presented at the workshop "Programming the Web - a search for APIs",
Fifth International World Wide Web Conference, 6 May 1996, Paris,
France.



What's New: Version 1.3, 29 April 1996
--------------------------------------

First public release; new license terms on all files.

Changed cgi-fcgi.c to use SO_REUSEADDR when creating the listening socket;
this avoids the need to wait through the TIME_WAIT state on all the TCP
connections made by the previous instance of an external application
you are restarting.



What's New: Version 1.2.2, 15 April 1996
----------------------------------------

Partially fixed a bug in Perl's FCGI::accept (source file FCGI.xs).
The per-request environment variables were being lost.  Now the
per-request environment variables show up correctly, except that if
the Perl application has an empty initial environment, the environment
variables associated with the *first* request are lost.  Therefore,
when starting Perl, always set some environment variable using the
AppClass -initial-env option, or by running cgi-fcgi in a non-empty
environment.



What's New: Version 1.2.1, 22 March 1996
----------------------------------------

Fixed a bug in FCGI_Accept.  If your application running as FastCGI
opened a file before calling FCGI_Accept, it would decide that it
was really running as CGI.  Things went downhill quickly after that!

Also added advisory locking to serialize calls to accept on shared
listening sockets on Solaris and IRIX, to work around problems
with concurrent accept calls on these platforms.



What's New: Version 1.2, 20 March 1996
--------------------------------------

1. This version of the kit implements the most recent draft
of the protocol spec.  Enhancements to the protocol include
a BEGIN_REQUEST record that simplifies request ID management
and transmits role and keep-alive information, and a simplified
end-of-stream indication.

The protocol spec has been revised to describe exactly what's
been implemented, leaving out the features that we hope to
introduce in later releases.

At the application level, the visible change is the FCGI_ROLE
variable that's available to applications.  This allows an application
to check that it has been invoked in the expected role.  A single
application can be written to respond in several roles.  The
FCGI_Accept.3 manpage contains more information.

2.  We introduced the new "module" prefix FCGX in order to simplify
the relationship between fcgi_stdio and fcgiapp.

A growing number of functions are provided in both fcgi_stdio and
fcgiapp versions.  Rather than inventing an ad hoc solution for each
naming conflict (as we did with FCGI_accept and FCGI_Accept), we've
bitten the bullet and systematically renamed *all* the fcgapp
primitives with the prefix FCGX_.  In fcgi_stdio, we've renamed
FCGI_accept to FCGI_Accept.  So all functions that are common in the
two libraries have the same name modulo the different prefixes.

The Accept function visible in Tcl is now called FCGI_Accept, not
FCGI_accept.

The Accept function visible in Perl is now FCGI::accept.  All
lower case names for functions and all upper case names for
modules appears to be a Perl convention, so we conform.

3. The kit now fully supports the Responder, Authorizer,
and Filter roles.

The Filter role required a new function, FCGI_StartFilterData.
FCGI_StartFilterData changes the input stream from reading
FCGI_STDIN data to reading FCGI_DATA data.  The manpage
gives full details.

Another new function, FCGI_SetExitStatus, is primarily for
the Responder role but is available to all.  FCGI_SetExitStatus
allows an application to set a nonzero "exit" status
before completing a request and calling FCGI_Accept again.
The manpage gives full details.

These two new functions are provided at both the fcgi_stdio interface
and the basic fcgiapp interface.  Naturally, the fcgiapp versions are
called FCGX_StartFilterData and FCGX_SetExitStatus.

4. The fcgiapp interface changed slightly in order to treat
the streams and environment data more symmetrically.

FCGX_Accept now returns an environment pointer, rather than requiring
a call to FCGX_GetAllParams to retrieve an environment pointer.
FCGX_GetParam takes an explicit environment pointer argument.
FCGX_GetAllParams is eliminated.  See the documentation in the header
file for complete information.

fcgiapp also added the procedure FCGX_IsCGI, providing a standardized
test of whether the app was started as CGI or FastCGI.

5. We've ported the kits to vendor-supported ANSI C compilers
on Sun (Solaris 2.X), HP, and Digital platforms.  GCC can be
selected on these platforms by performing SETENV CC gcc before
running configure.



What's New: Version 1.1, 30 Jan 1996
------------------------------------

1. More platforms: Digital UNIX, IBM AIX, Silicon Graphics IRIX,
Sun SunOS 4.1.4.

2. Perl and Tcl: Simple recipes for producing Perl and Tcl
interpreters that run as FastCGI applications.  No source
code changes are needed to Perl and Tcl.  Documented
in separate documents, accessible via the index page.



Version 1.0, 10 Jan 1996
------------------------
OpenID 

http://en.wikipedia.org/wiki/Openid

Anyone wanting to contribute is welcome
OpenID  consumer

http://en.wikipedia.org/wiki/Openid

Anyone wanting to contribute is welcome
Cypress
=======

Is an OAuth protocol implementation in Eiffel.

- Consumer: the client library and support OAtuh1.0a and 2.0.
- Server: is not done.


Note: This is a work in progress, and the API could change in a future.

## SSL/https concerns

Cypress is using the `http_client` library, and by default it uses the libcurl implementation. But if you use the EiffelNet implementation of the `http_client`, be sure to have `<variable name="ssl_enabled" value="true"/>` in your ecf file.
When using the libcurl implementation on Windows, make sue the associated .dll files are in accessible by the application.


OAuth consumer library
======================

Warning: 
	this is experimental code, shared for collaboration purpose. 
	It is likely to change a lot in the future.
    
Requirements:
JSON, eel, http client.
    

OAuth 1.0
* [RFC5849](http://tools.ietf.org/html/rfc5849)

OAuth 2.0
* [RFC6749](http://tools.ietf.org/html/rfc6749)

Anyone wanting to contribute is welcome


[Getting Started] (https://github.com/EiffelWebFramework/cypress/wiki/Getting-Started) 
JSON Web Token (JWT)

http://jwt.io/

Note: supporting only HS256 and none algorithm for signature, but could be extend with your own algorithm via `JWT_ALGORITHMS` (see `JWT.algorithms`, and `JWT_LOADER.algorithms`).

# How to use
```eiffel

	example
		local
			jwt: JWS
			tok: STRING
			l_loader: JWT_LOADER
		do
			create jwt.make_with_json_payload ("[
					{"iss":"joe", "exp":1200819380,"http://example.com/is_root":true}
					]")
			jwt.set_algorithm_to_hs256
			tok := jwt.encoded_string ("my-secret")

			create l_loader
			if
				attached l_loader.token (tok, Void, "my-secret", Void) as l_tok and then
				not l_tok.has_error
			then
				print (l_tok.claimset.string)
				check verified: not l_tok.has_unverified_token_error end
				check no_error: not l_tok.has_error end
			end
		end
	end
```

Eiffel Collection+json is a library to work with  Collection+JSON - Hypermedia Type,  http://www.amundsen.com/media-types/collection/

Project page: https://github.com/eiffelwebframework/collection_json

The current CJ implementation does not implement the [extensions][1] proposals,  
The google group is here [discussion group][2]

[1]: https://github.com/mamund/collection-json/tree/master/extensions "extensions"
[2]: https://groups.google.com/forum/?fromgroups#!forum/collectionjson "discussion group"
[![Build Status](https://travis-ci.org/EiffelWebFramework/HAL.svg?branch=master)](https://travis-ci.org/EiffelWebFramework/HAL/)
[![AppVeyor status](https://ci.appveyor.com/api/projects/status/01094sp8soowwpku?svg=true)](https://ci.appveyor.com/project/jvelilla/hal-gahly)

Eiffel HAL is a library to work with  http://stateless.co/hal_specification.html#json

HAL is used for exposing RESTful hypermedia APIs. Right now the current implementation only support 
JSON_HAL

References
http://tools.ietf.org/html/draft-kelly-json-hal-08
http://stateless.co/hal_specification.html#json
Eiffel HAL is a library to work with  http://stateless.co/hal_specification.html#json

HAL is used for exposing RESTful hypermedia APIs. Right now the current implementation only support 
JSON_HAL

References
http://tools.ietf.org/html/draft-kelly-json-hal-06
http://stateless.co/hal_specification.html#json
This library is a simplified version of ESpec without the GUI facilities.

After adding the espec library (see below) the following class will run a test "t1".

---------------------------------
class ROOT inherit ES_TEST create
	make
feature {NONE} -- Initialization
	make
		do
			add_boolean_case (agent t1)
			show_browser; show_errors; run_espec
		end
feature --tests
	t1: BOOLEAN
		local
			a: ARRAY[INTEGER]
		do
			comment("t1: test array count query")
			a := <<10, 9, 8>>
			Result := a.count = 3
		end
end
---------------------------------

Sample projects are included in the "tests" folder. For more instructions on how to use ESpec (e.g. for suits of tests) please compile the "demo" project included in the "tests" folder. This project will provide information on howto setup and run the tests.

The "show_browser" command (inserted before the "run_espec" command) will bring up the test results in the default browser (i.e. iexplorer for Windows and firefox on Linux). 

The "show_errors" command (inserted before the "run_espec" command) will show the full trace of contract violations in the generated output.

The user can change the default browser (see {ES_TEST_SUITE}.check_browser" in the library).

FOLLOW THESE STEPS BEFORE USING ESPEC:

1- Install Eiffel Studio from eiffel.com

TO ADD THE LIBRARY TO AN EXISTING PROJECT:
1- Open "project settings window" from Eiffel Studio
2- Click on groups
3- Click on libraries
4- Click on "add library"
5- In the name field type "espec" in the location type:
"$ISE_LIBRARY\contrib\library\testing\framework\espec\library\espec-safe.ecf"/>"

Or, add the following to the ecf file:
"<library name="espec" location="$ISE_LIBRARY\contrib\library\testing\framework\espec\library\espec-safe.ecf"/>"

TO RUN TESTS
1- Freeze the system (by pressing crl-f7) and wait for the C compilation to complete.
2- press the little down arrow next to the run button (crl-alt-F5 in windows), and invoke "run workbench system", that will bring a
browser window with the results of your tests .



Oct 28 2011
Faraz Torshizi
Jonathan Ostroff
Software Engineering Lab
York University, Toronto

Revision History
================

17 April 2012
Renamed the folder to espec (from espec-simple).
Fixed obsolete assignment attempts in routines
{ES_VIOLATION_CLASS} write_passed_case
{ES_VIOLATION_CLASS} write_failed_case
Fixed obsolete calls in tests:dictionary.

9 January 2014
--------------

Fixed some errors reported by new void safe checks
Added MacOs as supported system for browser report
Added features: assert_equal, assert_not_equal, assert and sub_comment

See 
  * https://wiki.eecs.yorku.ca/project/eiffel/getting_started:
  * https://wiki.eecs.yorku.ca/project/eiffel/getting_started:espec for new features
CONNEG is a library that provides utilities to select the best repesentation of a resource for a client where there are multiple representations available.

Using this library you can retrieve the best variant for media type, language preference, charset, and enconding/compression.

Take into account that the library is under development so is expected that the API change.

The library contains utilities that deal with content negotiation (server driven negotiation).This utility class
is based on ideas taken from the Book Restful WebServices Cookbook

The class SERVER_CONTENT_NEGOTIATION contains several features that helps to write different types of negotiation (media type, language,
charset and compression).
So for each of the following questions, you will have a corresponding method to help in the solution.

-  How to implement Media type negotiation?
	Hint: Use SERVER_CONTENT_NEGOTIATION.media_type_preference 
	       or SERVER_MEDIA_TYPE_NEGOTIATION.preference 

-  How to implement Language Negotiation?
	Hint: Use SERVER_CONTENT_NEGOTIATION.language_preference
	       or SERVER_LANGUAGE_NEGOTIATION.preference 

-  How to implement Character Negotiation?
	Hint: Use SERVER_CONTENT_NEGOTIATION.charset_preference
	       or SERVER_CHARSET_NEGOTIATION.preference 

-  How to implement Encoding Negotiation?
	Hint: Use SERVER_CONTENT_NEGOTIATION.encoding_preference
	       or SERVER_ENCODING_NEGOTIATION.preference 

There is also a  [test case](test/conneg_server_side_test.e "conneg_server_side_test") where you can check how to use this class.

# Eiffel IMAP Library

Eiffel IMAP library is an open source library to use the IMAP protocol in Eiffel

## Contents
At the moment, only the client part of the library is available. The client part of the library is used to connect to an IMAP server.
# HTTP library

## Overview

## Usage

## Examples

# simple HTTP client

## Overview
It provides simple routine to perform http requests, and get response.

## Requirements
* One of the following
	- Eiffel cURL library
		- cURL dynamic libraries in the PATH or the current directory (.dll or .so)
	- Eiffel Net library 
		- and optionally Eiffel NetSSL library to support `https://...`

* Note: set ciphers setting is supported only with libcurl implementation for now, net implementation
set all the ciphers as part of the OpenSSL initialization.

This means on Windows, do not forget to copy the libcurl.dll (and related) either in the same directory of the executable, or ensure the .dll are in the PATH environment.

It is possible to exclude the libcurl implementation xor the Eiffel Net implementation:
	In the .ecf configuration file of your project, you can use the following custom variables:

	* Disable the libcurl implementation
```
		<variable name="libcurl_http_client_disabled" value="True"/>
```

	* Disable the net implementation
```
		<variable name="net_http_client_disabled" value="True"/>
```

	* If you disabled both, the http client will not work as expected.

For the net implementation (using EiffelNet), if you need https:// support, you need to enabled the ssl support with the custom variables :
```
		<variable name="ssl_enabled" value="True"/>
```
	* By default, SSL is not included (mostly because it is sometime a pain to get the needed dynamic libraries .dll or .so)

## Usage
* To build code that is portable across the libcurl or net implementation of `http_client` library, use the `DEFAULT_HTTP_CLIENT`

```
	cl: DEFAULT_HTTP_CLIENT
	sess: HTTP_CLIENT_SESSION
	create cl
	sess := cl.new_session ("http://example.com")
	if attached sess.get ("/path-to-test") as l_response then
		if not l_response.error_occurred then
			if attached l_response.body as l_body then
				print (l_body)
			end
		end
	end
```

## Examples
* See the `tests/test-safe.ecf` project to see how to use.
* Examples will come in the future.

Eiffel Web Nino is and HTTPD server. It's a work in progress, so maybe it will be refactored.
The goal of is to provide a simple web server for development (like Java, Python and Ruby provide)



Eiffel Arbitrary Precision Mathematics Library

Contribution from Colin LeMahieu
see original source: https://github.com/clemahieu/eapmlDecimal library.
Use decimal.ecf or decimal-safe.ecf to include as library
Based on http://speleotrove.com/decimal/
Only some of the official tests have been implemented.
See folder "tests".
Class {FAST} has some basic tests, e.g:

t1: BOOLEAN
	local
		d1,d2,d3: DECIMAL
		r1 : REAL_64
	do
		comment("t1: test 0.1 + 0.1 + 0.1 = 0.3")
		r1 := 0.1
		d1 := "0.1"
		d3 := "0.3"
		d2 := d1 + d1 + d1
		check d1.out ~ "0.1" end
		Result := d2.out ~ "0.3"
	end

January 25, 2012
======================


-----------------------
Working infrastructure
-----------------------

-- Basic operators +. -, *, \, abs, floor, ceiling etc.
-- Default precision set to 28
-- Default roundoff is round-half-up
-- See {FAST} test cases

-- By default contracts (e.g. 4/0) are turned off
To turn on contracts, d1.default_context.enable_exception_on_trap.
This will cause 4/0 to generate a precondition exception.

-- d1.round_to(2) will round to 2 decimal places. As in Excel.

-- Approximately equal: d1.approximately_equal(d2) or "d1 |~ d2" 
Feature d1.no_digit_after_point returns the number of digits after the decimal point
(which we abbreviate as d1.ndap).
Let ndap = max(d1.ndap, d2.ndap), then
d1 |~ d2 iff |d1-d2| <= 5E-ndap
There is also a function to specify a specific epsilion, default = 5.

-- d1.log10, d1.log2, d1.sqrt and d1.nth_root(n:INT) have been added
(and appear to be working, although not yet efficient)


--------------------
EXPERIMENTAL
--------------------

--d1.sin, d1.cos, d1.tan, t1.cot, d1.sec, d1.csc are working but not well tested.
Degrees (not radians)

--d1.exp(x) fails on large numbers (e.g. x=500) can be very inaccurate
e.g. to 10 ULP (units in the last place).
d1.pow(x) also fails as it depends on exp(x)


==========================
LICENSE
==========================
note
	description:
		"DECIMAL numbers. Following the 'General Decimal Arithmetic Specification'."
	copyright: "Copyright (c) 2004, Paul G. Crismer and others."
	copyright: "Copyright (c) 2011, SEL, York University, Toronto and others."
	license: "MIT License"
	date: "$Date: 2012-01-02 22:26:29 -0500 (Mon, 02 Jan 2012) $"
	revision: "$Revision: 359 $"
README.txt - Intro to the AEL_PRINTF cluster

The Amalasoft Eiffel Printf Cluster is a collection of classes that implements
a printf facility for the Eiffel language.  It depends on the Eiffel base 
libraries (available in open source or commercial form from Eiffel 
Software www.eiffel.com) and is, like other Eiffel code, portable across 
platforms.

The printf cluster does not include an equivalent to scanf at this time.

The printf cluster does not support internationalization at this time.

     ------------------------------------------------------------

The cluster includes the following classes:

  AEL_PRINTF
    The "face" of the cluster; the class to be inherited or instantiated
    by classes needing the facility.
    AEL_PRINTF offers the key client features including printf, sprintf,
    fprintf and aprintf ("append" printf, that returns a formatted string),
    and features for generating hexadecimal dumps, as well as the key error
    handling routines.
    There is typically no need for clients to access directly any other
    class from the cluster.

    printf-like features presented by AEL_PRINTF include:

      aprintf - "append printf"
        Accepts a format specifier and arg list, and returns
        the formatted string result

      fprintf - "file printf"
        Accepts an opened file, a format specifier and arg list,
        and writes the formatted string to the file

      printf  - "printf"
        Accepts a format specifier and arg list, and writes the
        formatted string result to default output

      sprintf - "string printf"
        Accepts a destination STRING, a format specifier and arg list,
        and writes the formatted string into the destination string.

      axdump  - "hex dump"
        Accepts a source buffer, an options string and range/sequencing
        arguments, and returns as result a hexadecimal dump of the source
        buffer as a formatted string

      amemdump - "memory dump"
        Accepts  POINTER to a memory location, the size of memory
        to be processed, an options string, an effective starting address
        (for presentation) and a line spacing specifier, and returns
        a hexadecimal dump of the memory provided address given as
        a formatted string

      lxdump   - "list dump"
        Accepts a source buffer, options string, start/end sequence numbers
        and effective start address (for presentation) and returns a
        hexadecimal dump of the source buffer as a list of (rows of) strings

      amemdump - "memory dump"
        Accepts  POINTER to a memory location, the size of memory
        to be processed, an options string, an effective starting address
        (for presentation) and a line spacing specifier, and returns
        a hexadecimal dump of the memory provided address given as
        a list of (rows of) strings

      print_line, printline
        Accepts a detachable ANY as argument and writes it to default
        output (using) print, appending a newline character

    Additional features usable by clients/descendents include those by
    which to set global printf paramers.  These include:

      set_default_printf_fill_char
        Sets the character to be used for filling space in formatted strings
        to the given value (blank by default)

      reset_default_printf_fill_char
        Sets the character to be used for filling space in formatted strings
        to default value (blank)

      set_default_printf_decimal_separator
        Sets the character used by printf to denote the decimal (radix)
        point to the given value ('.' by default)

      reset_default_printf_decimal_separator
        Resets the character used by printf to denote the decimal (radix)
        point to the default value ('.')

      set_default_printf_list_delimiter
        Sets the string used by printf to denote the delimit items
        in a formatted list to the given value (", " by default)

      reset_default_printf_list_delimiter
        Resets the string used by printf to denote the delimit items
        in a formatted list to the default value (", ")

      set_default_printf_thousands_delimiter
        Sets the string used by printf to denote the delimit digit groups
        of thousands (3 decimal digits) in a formatted decimal to the given
        value ("," by default)

      reset_default_printf_thousands_delimiter
        Resets the string used by printf to denote the delimit digit groups
        of thousands (3 decimal digits) in a formatted decimal to the default
        value (",")

      set_printf_client_error_agent
        Sets the procedure to call when printf encounters a format error.
        Errors encountered are always recorded in last_printf_errors, whether
        the value for this agent is defined or not.

  AEL_PF_FORMATTING_CONSTANTS
    Provides constant values used by the other members of the cluster
    It holds the shared error list (last_printf_errors) and provides a
    shared (onced) instance of AEL_PF_FORMATTING_ROUTINES.

  AEL_PF_FORMATTING_ROUTINES
    Provides the core formatting routines used by the front-end routines
    in AEL_PRINTF.

  AEL_PF_FORMAT_ERROR
    Encapsulation of a single error instance (for when a run-time error
    occurs, due to mismatched parameters and such)

  AEL_PF_FORMAT_ERROR_SUPPORT
    Provides routines to interface with the shared error list

  AEL_PF_FORMAT_PARAM
    The heart of the cluster.  Provides format string parsing and
    interpretation, argument coordination and output routines

  AEL_PF_FORMAT_TOKEN
    A simple class representing a token within the format string
    argument.

     ------------------------------------------------------------

 The printf.ecf and printf-safe.ecf files define the library form of
 the cluster.

 Check the HISTORY.txt file for latest changes

     ------------------------------------------------------------

 Refer to AEL_Printf.pdf for a detailed description of the options, syntax
 and examples.

     ------------------------------------------------------------
# etar
Eiffel archiving library based on tar.

The etar adds archiving support to the Eiffel programming language. It was
developed as a project within the scope of the course "Software Engineering
Laboratory: Open-Source EiffelStudio" at ETH Zurich in autumn semester 2015.

For more information you are invited to visit the
[documentation](doc/README.md).

## Provided archives
The archive folder contains some archives. For a detailed description, view
[archives/README.md](archives/README.md).

Since some of these archives are rather large, they use git lfs.

## Current limitation
* Symbolic links are not supported for now.

## License
etar is licensed under the Eiffel Forum License, version 2 (see [LICENSE](LICENSE)).
For copyright information see [license.lic](license.lic).

## Development:
* Project page: https://github.com/eiffelhub/etar
* Contribution:
	- main contributor: Nicolas Trüssel
	- other contributor: Jocelyn Fiat (jfiat@eiffel.com)

# Example usages of the etar library
## tar_ls
tar_ls lists the contents of one or more tar archives.

```
Usage:
	tar_ls archive...
```

## minipax
minipax is a tiny version of pax (the posix replacement for tar). It can be used
to list archive contents, create and extract archives. Calling just minipax from
a terminal will cause it to show the usage text which is:

```
Usage: 
    - minipax [-A] -f archive
        List mode: minipax prints the contents of the specified archive
    - minipax [-A] -r -f archive
        Read mode: minipax unarchives the contents of the specified archive
    - minipax [-A] -w -f archive file...
        Write mode: minipax archives the given list of files, creating the
                    archive if it does not exist, overriding it otherwise
Options
    -A      Allow absolute paths and parent directory identifiers in filenames
```
# ETAR
Eiffel compression library based on tar.
Welcome to the etar wiki!

Project page: https://github.com/eiffelhub/etar

### Introduction
The etar library was developed as a project within the scope of the course "Software Engineering Laboratory: Open-Source EiffelStudio" at ETH Zurich, attended by Nicolas Trüssel and supervised by Jocelyn Fiat. The goal of the project was to add archiving support to the Eiffel programming language through a library. During the initial project discussion it was then decided to use the tar archive format and that the library should be written in pure Eiffel (no wrapping of existing solutions). The etar library was written and designed from scratch, since I (Nicolas Trüssel) did not find any existing archiving solutions for Eiffel.

### Functionality
etar supports creating and extracting archives using tar-family formats. Currently the ustar and pax archive formats are supported (specification linked below) and only plain files and directories can be added/extracted. Additionally the only storage possibility is an uncompressed file on disk.

However, etar was designed to be as extensible as possible, allowing both contributors and users to add support for new archive formats, payload types (e.g. symlinks and hardlinks), and storage backends (e.g. in-memory, compressed files) quite easily. For further information check the pages [ARCHIVABLE](interfaces/ARCHIVABLE.md) and [UNARCHIVER](interfaces/UNARCHIVER.md) for new payload types,  [TAR_HEADER_PARSER](interfaces/TAR_HEADER_PARSER.md) and [TAR_HEADER_WRITER](interfaces/TAR_HEADER_WRITER.md) for new archive formats, and [STORAGE_BACKEND](interfaces/STORAGE_BACKEND.md) for new storage possibilities.

### Documentation
Use the [Index](index.md) to easily navigate to different topics. 
A good starting point would be [Getting Started](Getting-Started.md) or [ARCHIVE](interfaces/ARCHIVE.md). 
[General Information about Archives](General-Information-about-Archives.md) and [Header Formats](Header-Formats.md) contains more background information, in case you want to learn more about tar in general.

Topics:
* [General Information about Archives](General-Information-about-Archives.md)
* [Header Formats](Header-Formats.md)
* [Getting Started](Getting-Started.md)
* [Interfaces](interfaces/README.md)

### Issues
- Improve test coverage
- Improve test style:
  Currently most tests nearly have the same code, so there is a lot of code duplication within the testcases.
- `ARCHIVABLE` tests use machine dependent metadata:
  Tests for `DIRECTORY_ARCHIVABLE` and `FILE_ARCHIVABLE` use hard-coded metadata which causes them to fail if cloned from GitHub and executed on different machines than the one the tests were written on.
- Unicode support is not fully tested.
-  `USTAR_HEADER_WRITER` allows UTF-8 strings (as opposed to [ISO/IEC 646:1991](https://en.wikipedia.org/wiki/ISO/IEC_646) only).
- Metadata restoring uses uid -> username lookup instead of username -> uid. There is a partial solution to this problem on the branch [externals](../../../tree/externals), but it only compiles on machines that have the `pwd.h` and `grp.h` headers (in particular it does not compile on Windows).
- When an archive named archive.tar contains an entry of a file named archive.tar and minipax is used to extract this file, the archive file is overwritten with the archived version (the entry) before it is fully extracted and therefore only parts of the original file are extracted.
  
### Future Work
Possible library extensions could be:
- Add append mode to `ARCHIVE` that allows to append new entries to an existing archive.
- Add support for more entry types (like links, sockets ...)
- Add more storage backends (e.g. compressed files, in-memory ...)

In case you want to work on some of these proposals (or something different) feel free to add an issue and/or submit PR.

### Resources
- pax specification: http://pubs.opengroup.org/onlinepubs/9699919799/utilities/pax.html

**[Home](../README.md) | [Interfaces](README.md) | [Index](../index.md)**
***

# Interfaces
* [ARCHIVE](ARCHIVE.md)
* [ERROR](ERROR.md)
* [TAR_HEADER](TAR_HEADER.md)
* [TAR_HEADER_PARSER](TAR_HEADER_PARSER.md)
* [TAR_HEADER_WRITER](TAR_HEADER_WRITER.md)
* [STORAGE_BACKEND](STORAGE_BACKEND.md)
* [ARCHIVABLE](ARCHIVABLE.md)
* [UNARCHIVER](UNARCHIVER.md)
* [TAR_UTILS](TAR_UTILS.md)
* [OCTAL_UTILS](OCTAL_UTILS.md)
Status: Work in Progress

Web documentation services, based on /src/tools/wdocs.
# Google-code-prettify : Eiffel language plugin #

## Introduction ##

[Google-code-prettify] (https://code.google.com/p/google-code-prettify/) is 
a Javascript module and CSS file that allows syntax highlighting of source code snippets in an html page.

This plugin adds syntax highlighting for the [Eiffel](http://en.wikipedia.org/wiki/Eiffel_\(programming_language\)) language.

*status*: beta

## Content ##

	- Readme.md		this file
	+ src
		- lang-eiffel.js	prettify module, defining lexeme classes
	+ examples
		- eiffel.html		a sample file
	+ styles
		- lang-eiffel.css	sample stylesheet
		
## Using this module in your html ##

1. In the \<head\> portion, reference
	- your stylesheet, e.g: \<script src="http://mysite.com/styles/lang-eiffel.js"\>\</script\>
	- the prettify.js module e.g: \<script src="https://google-code-prettify.googlecode.com/svn/loader/prettify.js"\>\</script\>
	- the lang-eiffel.js module e.g: \<script src="http://mysite.com/scripts/lang-eiffel.js"\>\</script\>
	
2. Initialize the prettify module by calling 'prettyPrint()'
	- e.g: \<body onload="prettyPrint()"\>

3. Trigger pretty printing in your \<pre\> nodes
	- e.g: \<pre class="prettyprint lang-eiffel"\>
	- or with line numbering: \<pre class="prettyprint lang-eiffel linenums"\>
    
Externals libraries included here for convenience.

cms comes from a modified version of EWF CMS library with added support for smarty template.
See https://github.com/EiffelWebFramework/cms/tree/smarty_template_supported

(note this changes should be included into master EWF/CMS library soon or later).

date:2014-09-01This folder should contain reusable classes for any system.
So please don't have any dependencies on the "ec" system.
Iron: the Eiffel library repository 
This library was inspired by GoboEiffel's xml library (http://www.gobosoft.com/)

This `gobo' library is mainly used to ease the replacement of the Gobo's XML library
with the current .. xml library.

One can use this code in .ecf to include and replace gobo XM_ classes with XML_ classes from those libraries ...
if equivalent interface exists.


		<library name="xml_tree" location="$ISE_LIBRARY\framework\xml\tree\xml_tree.ecf">
			<renaming old_name="XML_ATTRIBUTE" new_name="XM_ATTRIBUTE"/>
			<renaming old_name="XML_CHARACTER_DATA" new_name="XM_CHARACTER_DATA"/>
			<renaming old_name="XML_COMMENT" new_name="XM_COMMENT"/>
			<renaming old_name="XML_COMPOSITE" new_name="XM_COMPOSITE"/>
			<renaming old_name="XML_DOCUMENT" new_name="XM_DOCUMENT"/>
			<renaming old_name="XML_ELEMENT" new_name="XM_ELEMENT"/>
			<renaming old_name="XML_NAMESPACE" new_name="XM_NAMESPACE"/>
			<renaming old_name="XML_CALLBACKS_TREE" new_name="XM_CALLBACKS_TREE"/>
			<renaming old_name="XML_DOCUMENT_NODE" new_name="XM_DOCUMENT_NODE"/>
			<renaming old_name="XML_ELEMENT_NODE" new_name="XM_ELEMENT_NODE"/>
			<renaming old_name="XML_NAMED_NODE" new_name="XM_NAMED_NODE"/>
			<renaming old_name="XML_NODE" new_name="XM_NODE"/>
			<renaming old_name="XML_TREE_TO_EVENTS" new_name="XM_TREE_TO_EVENTS"/>
			<renaming old_name="XML_NODE_VISITOR_NULL" new_name="XM_NODE_PROCESSOR"/>
			<renaming old_name="XML_NODE_VISITOR_NULL" new_name="XM_NODE_VISITOR_NULL"/>
			<renaming old_name="XML_NODE_VISITOR_PRINT" new_name="XM_NODE_VISITOR_PRINT"/>
			<renaming old_name="XML_PROCESSING_INSTRUCTION" new_name="XM_PROCESSING_INSTRUCTION"/>
		</library>
		<library name="xml_parser" location="$ISE_LIBRARY\framework\xml\parser\xml_parser.ecf">
			<renaming old_name="XML_PARSER_FACTORY" new_name="XM_PARSER_FACTORY"/>
			<renaming old_name="XML_CALLBACKS" new_name="XM_CALLBACKS"/>
			<renaming old_name="XML_CALLBACKS_FILTER" new_name="XM_CALLBACKS_FILTER"/>
			<renaming old_name="XML_CALLBACKS_NULL" new_name="XM_CALLBACKS_NULL"/>
			<renaming old_name="XML_CALLBACKS_SOURCE" new_name="XM_CALLBACKS_SOURCE"/>
			<renaming old_name="XML_FORWARD_CALLBACKS" new_name="XM_FORWARD_CALLBACKS"/>
			<renaming old_name="XML_NAMESPACE_RESOLVER" new_name="XM_NAMESPACE_RESOLVER"/>
			<renaming old_name="XML_NAMESPACE_RESOLVER_CONTEXT" new_name="XM_NAMESPACE_RESOLVER_CONTEXT"/>
		</library>
		<library name="xml_gobo" location="$ISE_LIBRARY\framework\xml\gobo\xml_gobo.ecf" readonly="false">
			<renaming old_name="XML_CALLBACKS_FILTER_FACTORY" new_name="XM_CALLBACKS_FILTER_FACTORY"/>
			<renaming old_name="XML_TREE_CALLBACKS_PIPE" new_name="XM_TREE_CALLBACKS_PIPE"/>
			<renaming old_name="XML_CONTENT_CONCATENATOR" new_name="XM_CONTENT_CONCATENATOR"/>
			<renaming old_name="XML_CALLBACKS_TO_TREE_FILTER" new_name="XM_CALLBACKS_TO_TREE_FILTER"/>
			<renaming old_name="XML_STOP_ON_ERROR_FILTER" new_name="XM_STOP_ON_ERROR_FILTER"/>
			<renaming old_name="XML_POSITION_TABLE" new_name="XM_POSITION_TABLE"/>
			<renaming old_name="XML_MARKUP_CONSTANTS" new_name="XM_MARKUP_CONSTANTS"/>
		</library>

Actually you might not have to rename all those classes ...
that depends how you use the Gobo's xml library.To generate the IDL file for using the .NET consumer as a .NET component. Use:

  tlbexp /oldnames EiffelSoftware.MetadataConsumer.dll

Then do

  oleview EiffelSoftware.MetadataConsumer.tlb

Then compare with the previous version of the IDL to ensure it corresponds to your changes.
In order to use the library you need set the
concurrency settings to either EiffelThread or SCOOP.
XML v2 libraries

= Description =
- XML parser: parser and callbacks components
- XML tree: document, elements, and nodes (and related visitors)

= What is the difference with previous set of XML libraries =
This set of libraries is a fork of previous set.
It adds unicode support.
As a consequence it manipulates instances of STRING_32, and not just STRING_8.
The various features signature uses (*)_STRING_32.

This is the main breaking change with previous XML libraries.
Users are encouraged to migrate to this new version, since previous version was handling only ASCII, and had trouble to unescape entities such as &#12345;  (which represents a unicode character).

In addition, it does not make sense to restrict XML to ASCII, and the XML specification is all about unicode.

= How to migrate to XML v2 =
- Update your configuration files  ( .ecf ) to use the new xml_*.ecf paths.
- Make sure the various descendant of XML_CALLBACKS uses the adapted signature. And thus manipulate STRING_32 and not just STRING_8.
- XML_nodes returns READABLE_STRING_32 objects, and not anymore just STRING_8
- check any implicit conversion from STRING_32 to STRING_8 that might truncate and break the semantic of your XML data.

= Future changes =

= Misc =

-- Date: 2012/oct/25
This library was inspired by GoboEiffel's xml library (http://www.gobosoft.com/)This library was inspired by GoboEiffel's xml library (http://www.gobosoft.com/)To build libevent, type

$ ./configure && make

     (If you got libevent from the subversion repository, you will
      first need to run the included "autogen.sh" script in order to
      generate the configure script.)

Install as root via

# make install

You can run the regression tests by

$ make verify

Before, reporting any problems, please run the regression tests.

To enable the low-level tracing build the library as:

CFLAGS=-DUSE_DEBUG ./configure [...]

Acknowledgements:
-----------------

The following people have helped with suggestions, ideas, code or
fixing bugs:

  Alejo
  Weston Andros Adamson
  William Ahern
  Stas Bekman
  Andrew Danforth
  Mike Davis
  Shie Erlich
  Alexander von Gernler
  Artur Grabowski
  Aaron Hopkins
  Claudio Jeker
  Scott Lamb
  Adam Langley
  Philip Lewis
  David Libenzi
  Nick Mathewson
  Andrey Matveev
  Richard Nyberg
  Jon Oberheide
  Phil Oleson
  Dave Pacheco
  Tassilo von Parseval
  Pierre Phaneuf
  Jon Poland
  Bert JW Regeer
  Dug Song
  Taral

If I have forgotten your name, please contact me.
Eiffel internationalisation (i18n) library, version 1.0

BLABLA

This library is distributed under the Eiffel Forum License v2; a copy of this license can be found in the file "forum.txt" or at http://www.eiffel-nice.org/license/eiffel-forum-license-2.txt .  

INSTALLATION

You will have to set an environment variable called EIFFEL_I18N that points to the directory that you installed the library into - that is, the directory containing the library's .ecf file.
You will also have to compile the library's C-code.

Linux:

	From the root directory of the library execute the following commands: 
	
	cd Clib/
	finish-freezing -library
	
Under Windows for use without .NET:

	Please make sure you have the environment variables ISE_EIFFEL and ISE_C_COMPILER defined.
	This should have been done during installation of EiffelStudio; if not please refer to it's documentation.  ISE_EIFFEL should point to your EiffelStudio installation and ISE_C_COMPILER should indicate your C compiler ('msc' or 'bcb').
	If you are using the Borland compiler, you just need to run the 'make_bcb.bat' file in the Clib\ directory.
	
	If you are using Microsoft Visual Studio, you'll have to play with environment variables for a bit longer.
	You can follow the instructions given at http://dev.eiffel.com/Windows_32-bit_C_compiler , or you can try doing it yourself.
	In our case this involved:
		1. Making sure ISE_EIFFEL, ISE_C_COMPILER and ISE_PLATFORM were set.
		2. Changing the INCLUDE variable to contain something like
			C:\Program Files\Microsoft Visual Studio .NET 2003\SDK\v1.1\include\;
			C:\Program Files\Microsoft Visual Studio .NET 2003\Vc7\PlatformSDK\Include;
			C:\Program Files\Microsoft Visual Studio .NET 2003\Vc7\include;
		3. Changing the PATH variable to contain something like
			C:\Program Files\Microsoft Visual Studio .NET 2003\SDK\v1.1\Bin\;
			C:\Program Files\Microsoft Visual Studio .NET 2003\Vc7\bin;
			C:\Program Files\Microsoft Visual Studio .NET 2003\Common7\IDE;
	Once the enviroment variables are set correctly you should be able to run 'make_msc.bat'.
	Alternatively I suggest using the Borland compiler, as it does not require making sure utilities dispersed across half your hard drive are pointer to in $PATH.
		
	
Under Windows with .NET:

	No extra compilation required.

DOCUMENTATION

Both a user guide and a developer guide can be found in the "doc" directory. As the names indicate, the user guide explains how to use the library and documents it's features, whereas the developer guide is intended for people who want to extend or modify the library. 
HTML and text formats are available. 

Up-to-date and/or prettier versions can be found at the following two URLS:
http://dev.eiffel.com/Internationalization/User_guide
http://dev.eiffel.com/Internationalization/Developer_guide

HISTORY

1.0: initial release
Welcome to the distribution of Gobo from EiffelSoftware.

Here are some information on this distribution:

 * The Gobo binaries are located in spec/$ISE_PLATFORM/bin.

 * The documentation is available from http://www.gobosoft.com

 * The samples can be compiled using the gobo_sample.ecf file and replacing the
   THE_ROOT_CLASS_HERE by the actual name of the root class for the sample you chose.

Happy Eiffeling,
The EiffelSoftware Team	
The EiffelStore library provides a consistent set of 
classes for writing object oriented Eiffel applications that need 
to handle persistent objects.

The library interface consists of two sets:

1) A set of general purpose classes designed regardless of any data 
 management system used, to be found in directory 
 $ISE_LIBRARY/library/store/interface, and that you always need in your universe

2) Specific classes, referred to by the interface classes, bridging
  the application to selected data management systems called ``handles''. 
  The set of handles may be found:

   * in directory $ISE_LIBRARY/library/store/dbms

   * in the directory $ISE_LIBRARY/library/store/dbms/rdbms/{server_name}   
   with {server_name} corresponding to a selected relational database 
   management system.

   The best way to use them is to include the corresponding configuration file
   $ISE_LIBRARY/library/store/dbms/rdbms/{server_name}/{server_name.ecf}

   Additional support classes are also needed in your universe
   regardless of the selected handle. They are located in:
   
   * directory $ISE_LIBRARY/library/store/support and 
      $ISE_LIBRARY/library/store/dbms/support

Example classes are located in $ISE_EIFFEL/examples/store

EiffelStore has currently only been tested with:
		EiffelStudio 5.7
   		Oracle8 8.0.4
		ODBC 3.0

Documentation
-------------
   The user's manual is in Postscript format in directory /doc
   (cover page + content in US LTR format)

Then, to install EiffelStore external libraries, go to directory 
$ISE_EIFFEL/library/store/install (a README file provides full instructions).
One needs to setup database and modify test.config to fit database settings before running the tests.
# Eiffel Store test cases 
==========================
* support NULL values with SQL queries and Store Procedures.
* DB_PROC.store example.
* EiffelStore safe queries examples
* EiffelStore unsafe queries examples
* Eiffel SQL injection



This directory contains the upper level classes of EiffelStore



1. DB_CONTROL
-------------
This class provides session control and management primivites: 
connect, disconnect, commit, rollback, and database status flags.

It uses classes from the $ISE_EIFFEL/library/store/support directory.


2. DB_CHANGE
------------
This class allows an Eiffel user to modify persistent objects
(made persistent in DB repository from Eiffel or from any other source).
Objects can be referred to directly, or through a mapping table. 


3. DB_STORE
-----------
This class performs standard store operations on Eiffel objects. 
The way objects are stored varies according to EiffelStore layer used.


4. DB_SELECTION
---------------
This class performs standard retrieve operations on Eiffel objects.
The way objects are stored varies according to the EiffelStore layer used.


5. DB_REPOSITORY
----------------
This class captures the notion of data repository implemented in
different ways according to the selected data base handle.


6. DB_RESULT
------------
This class represents the notion of query result, in different
formats depending on the data base handle used.

7. DB_BYN_CHANGE
----------------
This class is quite the same class as DB_CHANGE but with dynamic sql.

8. DB_DYN_STORE
---------------
This class is quite the same class as DB_STORE but with dynamic sql.

EiffelStore
-----------

Installation 

1. Make sure the environment variables ISE_EIFFEL and ISE_PLATFORM are set.

2. Configure your setup for the database

3. Install the C-libraries:

	Start your databases kernels if needed (most of the C-libraries are based
	on DBMS libraries, but some of them use a precompiler which needs to access
	the database kernel).

	Go in the directory specific to the handle you are using and perform the
	following actions. For instance, for the ODBC handle:

	* Windows:
		cd %ISE_EIFFEL%\library\store\dbms\rdbms\odbc\Clib
		finish_freezing -library

	* Unix:
		cd $ISE_EIFFEL/library/store/dbms/rdbms/odbc/Clib
		finish_freezing -library

Collection of classes that help testing some facility of EiffelBase.
Eiffel Event Library (EEL)
(C) ISE 1999

This is the beginings of some hopefully generaly useful event handling stuff.
This library was inspired by GoboEiffel's xml library (http://www.gobosoft.com/)This library was inspired by GoboEiffel's xml library (http://www.gobosoft.com/)Before using the vision libraries you must compile
the C libraries in the Clib directory.
There is a Makefile.SH in each subdirectory.

You will need to make sure that the parent directory
for X11/includes is defined or included in the make file.

Then place the archive produced in each subdirectory in the
directory $EIFFEL4/library/mel/spec/$PLATFORM/lib.

This will need to be done on for each platform you will
be running mel on.

A documentation for EiffelTest still has to be written. It will appear 
web site as soon as possible. For the meantime, looking at the supplied
examples gives a good overview on how to work with this library.
The following classes have been made obsolete from 
version 3.3.7:

Kernel classe:
IO_HANDLER

Oui widget classes:
LABEL_G, PUSH_BG, SEPARATOR_G, TOGGLE_BG, SCROLL_LIST
LIST_MAN, MESSAGE, PROMPT

Context data classes:
CIRCNOT_DATA, FOCSOUT_DATA, MAPREQ_DATA, SELCLR_DATA
CIRCREQ_DATA, FOCUSIN_DATA, MESSAGE_DATA, SELNOT_DATA
CLRMAP_DATA, GRAPEXP_DATA, MULTIPL_DATA, SELREQ_DATA
CONFNOT_DATA, GRAVNOT_DATA, NOEXP_DATA, TOGGLE_DATA
CONFREQ_DATA, KEYMAP_DATA, PROPERT_DATA, UNMAP_DATA
CREATE_DATA, LEAVE_DATA, REPAREN_DATA, VISIBLE_DATA
DESTROY_DATA, MAPNOT_DATA, RESIZE_DATA, ENTER_DATA     
MAPPING_DATA, SCALE_DATA

To include these obsolete classes into your application
you must follow these steps:

1. If you are using MOTIF, change the declaration of the toolkit 
   initialization from MOTIF to OBSOLETE_MOTIF (for windows, change 
   the declaration from MS_WINDOWS to OBSOLETE_MS_WINDOWS)
2. Include the following clusters into your Ace file:
   obsolete_oui:    "$ISE_EIFFEL/library/vision/obsolete/oui";
   obsolete_toolkit:"$ISE_EIFFEL/library/vision/obsolete/toolkit";
   obsolete_motif:  "$ISE_EIFFEL/library/vision/obsolete/motif";
Eiffel2Java interface library.

This library needs the include files for JNI and the JVM library to be found by the compiler.
On UNIX this can normally be done by doing something like

export JAVA_HOME="/usr/lib/j2sdk1.5-sun"
export CPATH=$CPATH:"$JAVA_HOME/include;$JAVA_HOME/include/linux"
export LIBRARY_PATH=$LIBRARY_PATH:"$JAVA_HOME/jre/lib/amd64/server"
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:"$JAVA_HOME/jre/lib/amd64/server"

JAVA_HOME and the path to the libjvm.so library may have to be changed to fit the local installation.

On windows with Microsoft C compiler this can be done by adding the paths to environment variables, e.g.:

INCLUDE: C:\Program Files\Java\jdk1.5.0_06\include;C:\Program Files\Java\jdk1.5.0_06\include\win32 (directories where the jni.h and jni_md.h are)
LIB: C:\Program Files\Java\jdk1.5.0_06\lib (directory where the jvm.lib is)
PATH: C:\Program Files\Java\jre1.5.0_06\bin\client (directory where the jvm.dll is, needed to run the compiled program)

Creating packages for Linux distributions
-----------------------------------------

If you want to create a Debian/RPM packge of EiffelStudio, use one of these scripts:

  * make_debian_package
  * make_rpm_package

For details see http://dev.eiffel.com/Linux_Packages


Instructions to build a delivery with a Unix layout
---------------------------------------------------

Motivation
----------
-consistent file layout
-no environment setup needed
-multiple versions can be installed and used at the same time

Before building
---------------
If the default base directory (/usr/local) or the name of the lib dir (lib) should be changed,
adjust set_aliases.

Building
--------
A normal build should be created, e.g. with make_all

After building
--------------
To get a delivery in the unix layout, use the make_unix_layout script

make_unix_layout platform source destination

e.g. under Delivery/scripts/unix where a linux-x86-64 delivery has been generated

./make_unix_layout linux-x86-64 PorterPackage/Eiffel_19.01 unix_layout

will generate a delivery in the unix_layout directory.

At the end, the precompiles should be built using the freshly built delivery.
Instructions to build a delivery:

0 - Setting up the environment:

Make sure that "." must be in your PATH or else add it in any
script that calls `set_aliases'. Otherwise, it won't work because
`set_aliases' won't be found or some scripts used by `set_aliases'
won't be found too.

Make sure you have `pax' installed (See http://www.odi.ch/weblog/posting.php?posting=458) for more details on why we use it versus GNU tar).

1 - Preparing a delivery:

Make sure that ISE_EIFFEL and ISE_PLATFORM are correctly defined, ie
they point to an existing Eiffel installation.

Edit `set_aliases' to reflect your environment.

Launch `make_delivery' from the Delivery/scripts/unix directory as otherwise
it won't work.

2 - Producing a library for a given platform:

Launch `compile_exes $ISE_PLATFORM' where $ISE_PLATFORM is the value for
your platform.

Then `make_images $ISE_PLATFORM'.

At the end you have an ISO.bz2 and a tar.bz2 package of your delivery in the directory
where the 2 above scripts where launched.
docker-compose build
docker-compose up
see inside var/deliv-output/ folder for the .tar.bz2 file (and also the PorterPackage.tgz).
Note: if you leave the PorterPackage.tgz, it will be reused by the docker execution.


For 32bits, quite similar:
docker-compose -f docker-compose-32bits.yml build
docker-compose -f docker-compose-32bits.yml up

This is the location of the template license files.

License files are located at $ISE_EIFFEL/studio/templates/licenses/*.lic, and user license
files at $ISE_USER_FILES/studio/templates/licenses/*.lic. The * represents the license name.

License files must contain the note/indexing clause text and nothing more. They will be validated
using a parse and invalid licenses will not be merged into the associated class.

The license name is extracted using the following exclusive methods:
  - From the source text under an indexing term 'licence_name'.
  - Using a license reference in a neighboring license file to a project's ECF.

From the Source:
--------------------
Assigning a license to a particular class can be accomplished by adding the `license_name' term with
a string value representing the license name used to look for a license file. See below:

    note
        licence_name: "my_license"
    class
        MY_CLASS
    ....

The license_name term should be placed in the top note/indexing clause of a class. Placing it at the
bottom will cause it to be removed when replacing a class' license.

In the case of a license_name using the license name 'my_license' the following will be attempted to
be loaded, in order or priority:		
  - $ISE_USER_FILES/studio/templates/licenses/my_license.lic
  - $ISE_EIFFEL/studio/templates/licenses/my_license.lic
    
From a License File:
--------------------
For libraries and projects with an associated ECF, a license file or a license reference file may be
used to class all classes belonging to that library or project with a particular license. The
sources do not have to be modified to accomplish this, only a license file added at the same level 
as the ECF.

A license file should use the same file name as the ECF, for a project or library, except should
used a ".lic" extension instead of one used for the ECF. The file can contain a license similar to
those in $ISE_EIFFEL/studio/templates/licenses or can contain a reference string to point to a
installed license file using a license name. For this, create the license file next to the ECF with
the contents:

    reference:name
    
where 'name' is the name of the license in $ISE_EIFFEL/studio/templates/licenses/ or
$ISE_USER_FILES/studio/templates/licenses/ you wish to apply to the project/library. For instance

   reference:my_ref_license

In the case of a reference name using the license name 'my_license' the following will be attempted
to be loaded, in order or priority:
  - $ISE_USER_FILES/studio/templates/licenses/my_ref_license.lic
  - $ISE_EIFFEL/studio/templates/licenses/my_ref_license.lic

Using the Default License:
--------------------------
Where no license name in the source or license file neighbored to an ECF is found, you have one fall
back option, which will license all other classes in all projects and libraries in this way - the
default license.

A default license is installed with EiffelStudio under
$ISE_EIFFEL/studio/templates/licenses/default.lic and is blank. This file should not be modified
unless there is good reason to do so. Instead add a user file at
$ISE_USER_FILES/studio/templates/licenses/default.lic with the license you wish to use as the
default for all other classes.

C libraries needed for various Eiffel Libraries: Eiffel Vision2, Eiffel cURL
and also the delivery of EiffelStudio.

This is only for Windows

openssl
=======
	copy libeay32.dll $(EIFFEL_SRC)\Delivery\studio\spec\$(ISE_PLATFORM)\bin  
	copy ssleay32.dll $(EIFFEL_SRC)\Delivery\studio\spec\$(ISE_PLATFORM)\bin  

curl
====
- includes:
	$(EIFFEL_SRC)\C_library\openssl\include
	$(EIFFEL_SRC)\C_library\openssl\include\openssl
- actions:
	cp libcurl_imp.lib ..\..\library\cURL\spec\$(ISE_C_COMPILER)\$(ISE_PLATFORM)\lib
	copy libcurl.dll $(EIFFEL_SRC)\Delivery\studio\spec\$(ISE_PLATFORM)\bin

libpng
======
	copy libpng\libpng.lib to ..\library\vision2\spec\$(ISE_C_COMPILER)\$(ISE_PLATFORM)\lib
	copy libpng\libpng.lib to ..\compatible\library\vision2\spec\$(ISE_C_COMPILER)\$(ISE_PLATFORM)\lib

zlib
====
	copy zlib\zlib.lib to ..\library\vision2\spec\$(ISE_C_COMPILER)\$(ISE_PLATFORM)\lib
	copy zlib\zlib.lib to ..\compatible\library\vision2\spec\$(ISE_C_COMPILER)\$(ISE_PLATFORM)\lib
	
	
README for libpng version 1.6.32 - August 24, 2017 (shared library 16.0)
See the note about version numbers near the top of png.h

See INSTALL for instructions on how to install libpng.

Libpng comes in several distribution formats.  Get libpng-*.tar.gz or
libpng-*.tar.xz or if you want UNIX-style line endings in the text files,
or lpng*.7z or lpng*.zip if you want DOS-style line endings.

Version 0.89 was the first official release of libpng.  Don't let the
fact that it's the first release fool you.  The libpng library has been in
extensive use and testing since mid-1995.  By late 1997 it had
finally gotten to the stage where there hadn't been significant
changes to the API in some time, and people have a bad feeling about
libraries with versions < 1.0.  Version 1.0.0 was released in
March 1998.

****
Note that some of the changes to the png_info structure render this
version of the library binary incompatible with libpng-0.89 or
earlier versions if you are using a shared library.  The type of the
"filler" parameter for png_set_filler() has changed from png_byte to
png_uint_32, which will affect shared-library applications that use
this function.

To avoid problems with changes to the internals of the png info_struct,
new APIs have been made available in 0.95 to avoid direct application
access to info_ptr.  These functions are the png_set_<chunk> and
png_get_<chunk> functions.  These functions should be used when
accessing/storing the info_struct data, rather than manipulating it
directly, to avoid such problems in the future.

It is important to note that the APIs did not make current programs
that access the info struct directly incompatible with the new
library, through libpng-1.2.x.  In libpng-1.4.x, which was meant to
be a transitional release, members of the png_struct and the
info_struct can still be accessed, but the compiler will issue a
warning about deprecated usage.  Since libpng-1.5.0, direct access
to these structs is not allowed, and the definitions of the structs
reside in private pngstruct.h and pnginfo.h header files that are not
accessible to applications.  It is strongly suggested that new
programs use the new APIs (as shown in example.c and pngtest.c), and
older programs be converted to the new format, to facilitate upgrades
in the future.
****

Additions since 0.90 include the ability to compile libpng as a
Windows DLL, and new APIs for accessing data in the info struct.
Experimental functions include the ability to set weighting and cost
factors for row filter selection, direct reads of integers from buffers
on big-endian processors that support misaligned data access, faster
methods of doing alpha composition, and more accurate 16->8 bit color
conversion.

The additions since 0.89 include the ability to read from a PNG stream
which has had some (or all) of the signature bytes read by the calling
application.  This also allows the reading of embedded PNG streams that
do not have the PNG file signature.  As well, it is now possible to set
the library action on the detection of chunk CRC errors.  It is possible
to set different actions based on whether the CRC error occurred in a
critical or an ancillary chunk.

The changes made to the library, and bugs fixed are based on discussions
on the PNG-implement mailing list and not on material submitted
privately to Guy, Andreas, or Glenn.  They will forward any good
suggestions to the list.

For a detailed description on using libpng, read libpng-manual.txt.  For
examples of libpng in a program, see example.c and pngtest.c.  For usage
information and restrictions (what little they are) on libpng, see
png.h.  For a description on using zlib (the compression library used by
libpng) and zlib's restrictions, see zlib.h

I have included a general makefile, as well as several machine and
compiler specific ones, but you may have to modify one for your own needs.

You should use zlib 1.0.4 or later to run this, but it MAY work with
versions as old as zlib 0.95.  Even so, there are bugs in older zlib
versions which can cause the output of invalid compression streams for
some images.  You will definitely need zlib 1.0.4 or later if you are
taking advantage of the MS-DOS "far" structure allocation for the small
and medium memory models.  You should also note that zlib is a
compression library that is useful for more things than just PNG files.
You can use zlib as a drop-in replacement for fread() and fwrite() if
you are so inclined.

zlib should be available at the same place that libpng is, or at zlib.net.

You may also want a copy of the PNG specification.  It is available
as an RFC, a W3C Recommendation, and an ISO/IEC Standard.  You can find
these at http://www.libpng.org/pub/png/pngdocs.html .

This code is currently being archived at libpng.sourceforge.io in the
[DOWNLOAD] area, and at http://libpng.download/src .  If you
can't find it in any of those places, e-mail me, and I'll help you find it.

I am not a lawyer, but I believe that the Export Control Classification
Number (ECCN) for libpng is EAR99, which means not subject to export
controls or International Traffic in Arms Regulations (ITAR) because it
is open source, publicly available software, that does not contain any
encryption software.  See the EAR, paragraphs 734.3(b)(3) and 734.7(b).

If you have any code changes, requests, problems, etc., please e-mail
them to me.  Also, I'd appreciate any make files or project files,
and any modifications you needed to make to get libpng to compile,
along with a #define variable to tell what compiler/system you are on.
If you needed to add transformations to libpng, or wish libpng would
provide the image in a different way, drop me a note (and code, if
possible), so I can consider supporting the transformation.
Finally, if you get any warning messages when compiling libpng
(note: not zlib), and they are easy to fix, I'd appreciate the
fix.  Please mention "libpng" somewhere in the subject line.  Thanks.

This release was created and will be supported by myself (of course
based in a large way on Guy's and Andreas' earlier work), and the PNG
development group.

Send comments/corrections/commendations to png-mng-implement at
lists.sourceforge.net (subscription required; visit
https://lists.sourceforge.net/lists/listinfo/png-mng-implement
to subscribe) or to glennrp at users.sourceforge.net

You can't reach Guy, the original libpng author, at the addresses
given in previous versions of this document.  He and Andreas will
read mail addressed to the png-implement list, however.

Please do not send general questions about PNG.  Send them to
png-mng-misc at lists.sf.net (subscription required; visit
https://lists.sourceforge.net/lists/listinfo/png-mng-misc to
subscribe).  If you have a question about something
in the PNG specification that is related to using libpng, send it
to me.  Send me any questions that start with "I was using libpng,
and ...".  If in doubt, send questions to me.  I'll bounce them
to others, if necessary.

Please do not send suggestions on how to change PNG.  We have
been discussing PNG for twenty years now, and it is official and
finished.  If you have suggestions for libpng, however, I'll
gladly listen.  Even if your suggestion is not used immediately,
it may be used later.

Files in this distribution:

      ANNOUNCE      =>  Announcement of this version, with recent changes
      CHANGES       =>  Description of changes between libpng versions
      KNOWNBUG      =>  List of known bugs and deficiencies
      LICENSE       =>  License to use and redistribute libpng
      README        =>  This file
      TODO          =>  Things not implemented in the current library
      Y2KINFO       =>  Statement of Y2K compliance
      example.c     =>  Example code for using libpng functions
      libpng.3      =>  manual page for libpng (includes libpng-manual.txt)
      libpng-manual.txt  =>  Description of libpng and its functions
      libpngpf.3    =>  manual page for libpng's private functions
      png.5         =>  manual page for the PNG format
      png.c         =>  Basic interface functions common to library
      png.h         =>  Library function and interface declarations (public)
      pngpriv.h     =>  Library function and interface declarations (private)
      pngconf.h     =>  System specific library configuration (public)
      pngstruct.h   =>  png_struct declaration (private)
      pnginfo.h     =>  png_info struct declaration (private)
      pngdebug.h    =>  debugging macros (private)
      pngerror.c    =>  Error/warning message I/O functions
      pngget.c      =>  Functions for retrieving info from struct
      pngmem.c      =>  Memory handling functions
      pngbar.png    =>  PNG logo, 88x31
      pngnow.png    =>  PNG logo, 98x31
      pngpread.c    =>  Progressive reading functions
      pngread.c     =>  Read data/helper high-level functions
      pngrio.c      =>  Lowest-level data read I/O functions
      pngrtran.c    =>  Read data transformation functions
      pngrutil.c    =>  Read data utility functions
      pngset.c      =>  Functions for storing data into the info_struct
      pngtest.c     =>  Library test program
      pngtest.png   =>  Library test sample image
      pngtrans.c    =>  Common data transformation functions
      pngwio.c      =>  Lowest-level write I/O functions
      pngwrite.c    =>  High-level write functions
      pngwtran.c    =>  Write data transformations
      pngwutil.c    =>  Write utility functions
      arm           =>  Contains optimized code for the ARM platform
      powerpc       =>  Contains optimized code for the PowerPC platform
      contrib       =>  Contributions
       arm-neon         =>  Optimized code for ARM-NEON platform
       powerpc-vsx      =>  Optimized code for POWERPC-VSX platform
       examples         =>  Example programs
       gregbook         =>  source code for PNG reading and writing, from
                            Greg Roelofs' "PNG: The Definitive Guide",
                            O'Reilly, 1999
       libtests         =>  Test programs
       mips-msa         =>  Optimized code for MIPS-MSA platform
       pngminim         =>  Minimal decoder, encoder, and progressive decoder
                            programs demonstrating use of pngusr.dfa
       pngminus         =>  Simple pnm2png and png2pnm programs
       pngsuite         =>  Test images
       testpngs
       tools            =>  Various tools
       visupng          =>  Contains a MSVC workspace for VisualPng
      intel             =>  Optimized code for INTEL-SSE2 platform
      mips              =>  Optimized code for MIPS platform
      projects      =>  Contains project files and workspaces for
                        building a DLL
       owatcom          =>  Contains a WATCOM project for building libpng
       visualc71        =>  Contains a Microsoft Visual C++ (MSVC)
                            workspace for building libpng and zlib
       vstudio          =>  Contains a Microsoft Visual C++ (MSVC)
                            workspace for building libpng and zlib
      scripts       =>  Directory containing scripts for building libpng:
                            (see scripts/README.txt for the list of scripts)

Good luck, and happy coding.

-Glenn Randers-Pehrson (current maintainer, since 1998)
 Internet: glennrp at users.sourceforge.net

-Andreas Eric Dilger (former maintainer, 1996-1997)
 Internet: adilger at enel.ucalgary.ca
 Web: http://www-mddsp.enel.ucalgary.ca/People/adilger/

-Guy Eric Schalnat (original author and former maintainer, 1995-1996)
 (formerly of Group 42, Inc)
 Internet: gschal at infinet.com

Makefiles for  libpng version 1.6.32 - August 24, 2017

pnglibconf.h.prebuilt       =>  Stores configuration settings
 makefile.linux    =>  Linux/ELF makefile
                       (gcc, creates libpng16.so.16.1.6.32)
 makefile.linux-opt=>  Linux/ELF makefile with hardware optimizations on
                       (gcc, creates libpng16.so.16.1.6.32)
 makefile.gcc      =>  Generic makefile (gcc, creates static libpng.a)
 makefile.knr      =>  Archaic UNIX Makefile that converts files with
                       ansi2knr (Requires ansi2knr.c from
                       ftp://ftp.cs.wisc.edu/ghost)
 makefile.acorn    =>  Acorn makefile
 makefile.aix      =>  AIX/gcc makefile
 makefile.amiga    =>  Amiga makefile
 makefile.atari    =>  Atari makefile
 makefile.bc32     =>  32-bit Borland C++ (all modules compiled in C mode)
 makefile.beos     =>  beos makefile
 makefile.bor      =>  Borland makefile (uses bcc)
 makefile.cegcc    =>  minge32ce for Windows CE makefile
 makefile.darwin   =>  Darwin makefile, can use on MacosX
 makefile.dec      =>  DEC Alpha UNIX makefile
 makefile.dj2      =>  DJGPP 2 makefile
 makefile.freebsd  =>  FreeBSD makefile
 makefile.gcc      =>  Generic gcc makefile
 makefile.hpgcc    =>  HPUX makefile using gcc
 makefile.hpux     =>  HPUX (10.20 and 11.00) makefile
 makefile.hp64     =>  HPUX (10.20 and 11.00) makefile, 64-bit
 makefile.ibmc     =>  IBM C/C++ version 3.x for Win32 and OS/2 (static)
 makefile.intel    =>  Intel C/C++ version 4.0 and later
 makefile.mips     =>  MIPS makefile
 makefile.msc      =>  Microsoft C makefile
 makefile.netbsd   =>  NetBSD/cc makefile, makes libpng.so.
 makefile.openbsd  =>  OpenBSD makefile
 makefile.os2      =>  OS/2 Makefile (gcc and emx, requires libpng.def)
 makefile.sco      =>  For SCO OSr5  ELF and Unixware 7 with Native cc
 makefile.sggcc    =>  Silicon Graphics (gcc,
                       creates libpng16.so.16.1.6.32)
 makefile.sgi      =>  Silicon Graphics IRIX makefile (cc, creates static lib)
 makefile.solaris  =>  Solaris 2.X makefile (gcc,
                       creates libpng16.so.16.1.6.32)
 makefile.so9      =>  Solaris 9 makefile (gcc,
                       creates libpng16.so.16.1.6.32)
 makefile.std      =>  Generic UNIX makefile (cc, creates static libpng.a)
 makefile.sunos    =>  Sun makefile
 makefile.32sunu   =>  Sun Ultra 32-bit makefile
 makefile.64sunu   =>  Sun Ultra 64-bit makefile
 makefile.tc3      =>  Turbo C 3.0 makefile
 makefile.vcwin32  =>  makefile for Microsoft Visual C++ 4.0 and later
 makevms.com       =>  VMS build script
 smakefile.ppc     =>  AMIGA smakefile for SAS C V6.58/7.00 PPC compiler
                       (Requires SCOPTIONS, copied from scripts/SCOPTIONS.ppc)

Other supporting scripts:
 README.txt        =>  This file
 descrip.mms       =>  VMS makefile for MMS or MMK
 libpng-config-body.in => used by several makefiles to create libpng-config
 libpng-config-head.in => used by several makefiles to create libpng-config
 libpng.pc.in      =>  Used by several makefiles to create libpng.pc
 pngwin.rc         =>  Used by the visualc71 project.
 pngwin.def        =>  Used by makefile.os2
 pngwin.dfn        =>  Used to maintain pngwin.def
 SCOPTIONS.ppc     =>  Used with smakefile.ppc

 checksym.awk       =>  Used for maintaining pnglibconf.h
 def.dfn            =>  Used for maintaining pnglibconf.h
 options.awk        =>  Used for maintaining pnglibconf.h
 pnglibconf.dfa     =>  Used for maintaining pnglibconf.h
 pnglibconf.mak     =>  Used for maintaining pnglibconf.h
 sym.dfn            =>  Used for symbol versioning
 symbols.def        =>  Used for symbol versioning
 symbols.dfn        =>  Used for symbol versioning
 vers.dfn           =>  Used for symbol versioning

 libtool.m4        =>  Used by autoconf tools
 ltoptions.m4      =>  Used by autoconf tools
 ltsugar.m4        =>  Used by autoconf tools
 ltversion.m4      =>  Used by autoconf tools
 lt~obsolete.m4    =>  Used by autoconf tools

 intprefix.dfn     =>  Used by autoconf tools
 macro.lst         =>  Used by autoconf tools
 prefix.dfn        =>  Used by autoconf tools


Further information can be found in comments in the individual makefiles.

This "contrib" directory contains contributions which are not necessarily under
the libpng license, although all are open source.  They are not part of
libpng proper and are not used for building the library, although some are used
for testing the library via "make check".

This directory (contrib/examples) contains examples of libpng usage.

NO COPYRIGHT RIGHTS ARE CLAIMED TO ANY OF THE FILES IN THIS DIRECTORY.

To the extent possible under law, the authors have waived all copyright and
related or neighboring rights to this work.  This work is published from:
United States.

The files may be used freely in any way.  The intention is that appropriate
parts of the files be used in other libpng-using programs without any need for
the authors of the using code to seek copyright or license from the original
authors.

The source code and comments in this directory are the original work of the
people named below.  No other person or organization has made contributions to
the work in this directory.

ORIGINAL AUTHORS
    The following people have contributed to the code in this directory.  None
    of the people below claim any rights with regard to the contents of this
    directory.

    John Bowler <jbowler at acm.org>
PngMinus
--------
(copyright Willem van Schaik, 1999)


License
-------

Permission to use, copy, modify, and distribute this software and
its documentation for any purpose and without fee is hereby granted,
provided that the above copyright notice appear in all copies and
that both that copyright notice and this permission notice appear in
supporting documentation. This software is provided "as is" without
express or implied warranty.


Some history
------------
Soon after the creation of PNG in 1995, the need was felt for a set of
pnmtopng / pngtopnm utilities. Independantly Alexander Lehmann and I
(Willem van Schaik) started such a project. Luckily we discovered this
and merged the two together into pnmtopng.tar.gz, which is available
from a/o ftp://ftp.simplesystems.org/pub/libpng/png/.

These two utilities have many, many options and make use of most of the
features of PNG, like gamma, alpha, sbit, text-chunks, etc. This makes
the utilities quite complex and by now not anymore very maintainable.
When we wrote these programs, libpng was still in an early stage.
Therefore, lots of the functionality that we put in our software can now
be done using transform-functions in libpng.

Finally, to compile these programs, you need to have installed and
compiled three libraries: libpng, zlib and netpbm. Especially the latter
makes the whole setup a bit bulky. But that's unavoidable given the many
features of pnmtopng.


What now
--------
At this moment libpng is in a very stable state and can do much of the
work done in pnmtopng. Also, pnmtopng needs to be upgraded to the new
interface of libpng. Hence, it is time for a rewrite from the ground up
of pnmtopng and pngtopnm. This will happen in the near future (stay
tuned). The new package will get a different name to distinguish it from
the old one: PngPlus.

To experiment a bit with the new interface of libpng, I started off with
a small prototype that contains only the basic functionality. It doesn't
have any of the options to read or write special chunks and it will do
no gamma correction. But this makes it also a simple program that is
quite easy to understand and can serve well as a template for other
software developments. (By now there are of course a couple of programs,
like Greg Roelofs' rpng/wpng, that can be used just as good.)


Can and can not
---------------
As this is the small brother of the future PngPlus, I called this fellow
PngMinus. Because I started this development in good-old Turbo-C, I
avoided the use the netpbm library, which requires DOS extenders. Again,
another reason to call it PngMinus (minus netpbm :-). So, part of the
program are some elementary routines to read / write pgm- and ppm-files.
It does not read b&w pbm-files.

The downside of this approach is that you can not use them on images
that require blocks of memory bigger than 64k (the DOS version). For
larger images you will get an out-of-memory error.

As said before, PngMinus doesn't correct for gamma. When reading
png-files you can do this just as well by piping the output of png2pnm
to pnmgamma, one of the standard PbmPlus tools. This same scenario will
most probably also be followed in the full-blown future PngPlus, with
the addition of course of the possibility to create gamma-chunks when
writing png-files.

On the other hand it supports alpha-channels. When reading a png-image
you can write the alpha-channel into a pgm-file. And when creating an
RGB+A png-image, you just combine a ppm-file with a corresponding
pgm-file containing the alpha-channel. When reading, transparency chunks
are converted into an alpha-channel and from there on treated the same
way.

Finally you can opt for writing ascii or binary pgm- and ppm-files. When
the bit-depth is 16, the format will always be ascii.


Using it
--------
To distinguish them from pnmtopng and PngPlus, the utilities are named
png2pnm and pnm2png (2 instead of to). The input- and output-files can
be given as parameters or through redirection. Therefore the programs
can be part of a pipe.

To list the options type "png2pnm -h" or "pnm2png -h".


Just like Scandinavian furniture
--------------------------------
You have to put it together yourself. I did test the software under
MS-DOS with Turbo-C 3.0 and under RedHat Linux 4.2 with gcc. In both
cases I used libpng-1.0.4 and zlib-1.1.3. Later versions should be OK,
however some older libpng versions have a bug in pngmem.c when using
Turbo-C 3.0 (see below).

You can build it using one of the two makefiles (make -f makefile.###)
or use the batch/script files pngminus.bat / pngminus.sh. This assumes
that you have built the libraries in ../libpng and ../zlib. Using Linux,
make sure that you have built libpng with makefile.std and not
makefile.linux (also called .lnx in earlier versions of libpng). The
latter creates a .so shared-library, while the PngMinus makefile assumes
a normal .a static library.

If you create a ../pngsuite directory and then store the basn####.png
files from PngSuite (http://www.schaik.com/pngsuite/) in there, you can
test in one go the proper functioning of PngMinus, see png2pnm.bat and
pnm2png.bat (or the .sh versions).


Warranty
-------
Please, remember that this was just a small experiment to learn a few
things. It will have many unforeseen features <vbg>. Who said bugs? Use
it when you are in need for something simple or when you want to start
developing your own stuff.


The Turbo bug
-------------
** pngmem.old
          hptr = (png_byte huge *)((long)(hptr) & 0xfffffff0L);
          hptr += 16L;
** pngmem.c
          hptr = (png_byte huge *)((long)(hptr) & 0xfffffff0L);
          hptr = hptr + 16L;
**

** pngmem.old
          png_ptr->offset_table_ptr[i] = (png_bytep)hptr;
          hptr += (png_uint_32)65536L;
** pngmem.c
          png_ptr->offset_table_ptr[i] = (png_bytep)hptr;
          hptr = hptr + 65536L;
**


The end
-------
Willem van Schaik
mailto:willem at schaik.com
http://www.schaik.com/png/
-------
Oct 1999

OPERATING SYSTEM SPECIFIC ARM NEON DETECTION
--------------------------------------------

Detection of the ability to execute ARM NEON on an ARM processor requires
operating system support.  (The information is not available in user mode.)

HOW TO USE THIS
---------------

This directory contains C code fragments that can be included in arm/arm_init.c
by setting the macro PNG_ARM_NEON_FILE to the file name in "" or <> at build
time.  This setting is not recorded in pnglibconf.h and can be changed simply by
rebuilding arm/arm_init.o with the required macro definition.

For any of this code to be used the ARM NEON code must be enabled and run time
checks must be supported.  I.e.:

#if PNG_ARM_NEON_OPT > 0
#ifdef PNG_ARM_NEON_CHECK_SUPPORTED

This is done in a 'configure' build by passing configure the argument:

   --enable-arm-neon=check

Apart from the basic Linux implementation in contrib/arm-neon/linux.c this code
is unsupported.  That means that it is not even compiled on a regular basis and
may be broken in any given minor release.

FILE FORMAT
-----------

Each file documents its testing status as of the last time it was tested (which
may have been a long time ago):

STATUS: one of:
   SUPPORTED: This indicates that the file is included in the regularly
         performed test builds and bugs are fixed when discovered.
   COMPILED: This indicates that the code did compile at least once.  See the
         more detailed description for the extent to which the result was
         successful.
   TESTED: This means the code was fully compiled into the libpng test programs
         and these were run at least once.

BUG REPORTS: an email address to which to send reports of problems

The file is a fragment of C code. It should not define any 'extern' symbols;
everything should be static.  It must define the function:

static int png_have_neon(png_structp png_ptr);

That function must return 1 if ARM NEON instructions are supported, 0 if not.
It must not execute png_error unless it detects a bug.  A png_error will prevent
the reading of the PNG and in the future, writing too.

BUG REPORTS
-----------

If you mail a bug report for any file that is not SUPPORTED there may only be
limited response.  Consider fixing it and sending a patch to fix the problem -
this is more likely to result in action.

CONTRIBUTIONS
-------------

You may send contributions of new implementations to
png-mng-implement@sourceforge.net.  Please write code in strict C90 C where
possible.  Obviously OS dependencies are to be expected.  If you submit code you
must have the authors permission and it must have a license that is acceptable
to the current maintainer; in particular that license must permit modification
and redistribution.

Please try to make the contribution a single file and give the file a clear and
unambiguous name that identifies the target OS.  If multiple files really are
required put them all in a sub-directory.

You must also be prepared to handle bug reports from users of the code, either
by joining the png-mng-implement mailing list or by providing an email for the
"BUG REPORTS" entry or both.  Please make sure that the header of the file
contains the STATUS and BUG REPORTS fields as above.

Please list the OS requirements as precisely as possible.  Ideally you should
also list the environment in which the code has been tested and certainly list
any environments where you suspect it might not work.
OPERATING SYSTEM SPECIFIC MIPS MSA DETECTION
--------------------------------------------

Detection of the ability to execute MIPS MSA on an MIPS processor requires
operating system support.  (The information is not available in user mode.)

HOW TO USE THIS
---------------

This directory contains C code fragments that can be included in mips/mips_init.c
by setting the macro PNG_MIPS_MSA_FILE to the file name in "" or <> at build
time.  This setting is not recorded in pnglibconf.h and can be changed simply by
rebuilding mips/msa_init.o with the required macro definition.

For any of this code to be used the MIPS MSA code must be enabled and run time
checks must be supported.  I.e.:

#if PNG_MIPS_MSA_OPT > 0
#ifdef PNG_MIPS_MSA_CHECK_SUPPORTED

This is done in a 'configure' build by passing configure the argument:

   --enable-mips-msa=check

Apart from the basic Linux implementation in contrib/mips-msa/linux.c this code
is unsupported.  That means that it is not even compiled on a regular basis and
may be broken in any given minor release.

FILE FORMAT
-----------

Each file documents its testing status as of the last time it was tested (which
may have been a long time ago):

STATUS: one of:
   SUPPORTED: This indicates that the file is included in the regularly
         performed test builds and bugs are fixed when discovered.
   COMPILED: This indicates that the code did compile at least once.  See the
         more detailed description for the extent to which the result was
         successful.
   TESTED: This means the code was fully compiled into the libpng test programs
         and these were run at least once.

BUG REPORTS: an email address to which to send reports of problems

The file is a fragment of C code. It should not define any 'extern' symbols;
everything should be static.  It must define the function:

static int png_have_msa(png_structp png_ptr);

That function must return 1 if MIPS MSA instructions are supported, 0 if not.
It must not execute png_error unless it detects a bug.  A png_error will prevent
the reading of the PNG and in the future, writing too.

BUG REPORTS
-----------

If you mail a bug report for any file that is not SUPPORTED there may only be
limited response.  Consider fixing it and sending a patch to fix the problem -
this is more likely to result in action.

CONTRIBUTIONS
-------------

You may send contributions of new implementations to
png-mng-implement@sourceforge.net.  Please write code in strict C90 C where
possible.  Obviously OS dependencies are to be expected.  If you submit code you
must have the authors permission and it must have a license that is acceptable
to the current maintainer; in particular that license must permit modification
and redistribution.

Please try to make the contribution a single file and give the file a clear and
unambiguous name that identifies the target OS.  If multiple files really are
required put them all in a sub-directory.

You must also be prepared to handle bug reports from users of the code, either
by joining the png-mng-implement mailing list or by providing an email for the
"BUG REPORTS" entry or both.  Please make sure that the header of the file
contains the STATUS and BUG REPORTS fields as above.

Please list the OS requirements as precisely as possible.  Ideally you should
also list the environment in which the code has been tested and certainly list
any environments where you suspect it might not work.

pngsuite
--------
Copyright (c) Willem van Schaik, 1999, 2011, 2012
Two images (ftbbn0g01.png and ftbbn0g02.png) are by Glenn Randers-Pehrson, 2012

Permission to use, copy, modify, and distribute these images for any
purpose and without fee is hereby granted.

The 15 "bas*.png" images are part of the much larger PngSuite test-set of
images, available for developers of PNG supporting software. The
complete set, available at http:/www.schaik.com/pngsuite/, contains
a variety of images to test interlacing, gamma settings, ancillary
chunks, etc.

The "ft*.png" images are "free/libre" replacements for the transparent
corresponding t*.png images in the PngSuite.

The images in this directory represent the basic PNG color-types:
grayscale (1-16 bit deep), full color (8 or 16 bit), paletted
(1-8 bit) and grayscale or color images with alpha channel. You
can use them to test the proper functioning of PNG software.

    filename       depth type
    ------------ ------ --------------
    basn0g01.png   1-bit grayscale
    basn0g02.png   2-bit grayscale
    basn0g04.png   4-bit grayscale
    basn0g08.png   8-bit grayscale
    basn0g16.png  16-bit grayscale
    basn2c08.png   8-bit truecolor
    basn2c16.png  16-bit truecolor
    basn3p01.png   1-bit paletted
    basn3p02.png   2-bit paletted
    basn3p04.png   4-bit paletted
    basn3p08.png   8-bit paletted
    basn4a08.png   8-bit gray with alpha
    basn4a16.png  16-bit gray with alpha
    basn6a08.png   8-bit RGBA
    basn6a16.png  16-bit RGBA

    ftbbn0g01.png  1-bit grayscale, black bKGD
    ftbbn0g02.png  2-bit grayscale, black bKGD
    ftbbn0g04.png  4-bit grayscale, black bKGD
    ftbbn2c16.png 16-bit truecolor, black bKGD
    ftbbn3p08.png  8-bit paletted, black bKGD
    ftbgn2c16.png 16-bit truecolor, gray bKGD
    ftbgn3p08.png  8-bit paletted, gray bKGD
    ftbrn2c08.png  8-bit truecolor, red bKGD
    ftbwn0g16.png 16-bit gray, white bKGD
    ftbwn3p08.png  8-bit paletted, white bKGD
    ftbyn3p08.png  8-bit paletted, yellow bKGD
    ftp0n0g08.png  8-bit grayscale, opaque
    ftp0n2c08.png  8-bit truecolor, opaque
    ftp0n3p08.png  8-bit paletted, opaque
    ftp1n3p08.png  8-bit paletted, no bKGD

Here is the correct result of typing "pngtest -m bas*.png" in
this directory:

Testing basn0g01.png: PASS (524 zero samples)
 Filter 0 was used 32 times
Testing basn0g02.png: PASS (448 zero samples)
 Filter 0 was used 32 times
Testing basn0g04.png: PASS (520 zero samples)
 Filter 0 was used 32 times
Testing basn0g08.png: PASS (3 zero samples)
 Filter 1 was used 9 times
 Filter 4 was used 23 times
Testing basn0g16.png: PASS (1 zero samples)
 Filter 1 was used 1 times
 Filter 2 was used 31 times
Testing basn2c08.png: PASS (6 zero samples)
 Filter 1 was used 5 times
 Filter 4 was used 27 times
Testing basn2c16.png: PASS (592 zero samples)
 Filter 1 was used 1 times
 Filter 4 was used 31 times
Testing basn3p01.png: PASS (512 zero samples)
 Filter 0 was used 32 times
Testing basn3p02.png: PASS (448 zero samples)
 Filter 0 was used 32 times
Testing basn3p04.png: PASS (544 zero samples)
 Filter 0 was used 32 times
Testing basn3p08.png: PASS (4 zero samples)
 Filter 0 was used 32 times
Testing basn4a08.png: PASS (32 zero samples)
 Filter 1 was used 1 times
 Filter 4 was used 31 times
Testing basn4a16.png: PASS (64 zero samples)
 Filter 0 was used 1 times
 Filter 1 was used 2 times
 Filter 2 was used 1 times
 Filter 4 was used 28 times
Testing basn6a08.png: PASS (160 zero samples)
 Filter 1 was used 1 times
 Filter 4 was used 31 times
Testing basn6a16.png: PASS (1072 zero samples)
 Filter 1 was used 4 times
 Filter 4 was used 28 times
libpng passes test

Willem van Schaik
<willem at schaik.com>
October 1999
Microsoft Developer Studio Build File, Format Version 6.00 for VisualPng
------------------------------------------------------------------------

Copyright 2000, Willem van Schaik.

This code is released under the libpng license.
For conditions of distribution and use, see the disclaimer
and license in png.h

As a PNG .dll demo VisualPng is finished. More features would only hinder
the program's objective. However, further extensions (like support for other
graphics formats) are in development. To get these, or for pre-compiled
binaries, go to "http://www.schaik.com/png/visualpng.html".

------------------------------------------------------------------------

Assumes that

   libpng DLLs and LIBs are in ..\..\projects\msvc\win32\libpng
   zlib DLLs and LIBs are in   ..\..\projects\msvc\win32\zlib
   libpng header files are in  ..\..\..\libpng
   zlib header files are in    ..\..\..\zlib
   the pngsuite images are in  ..\pngsuite

To build:

1) On the main menu Select "Build|Set Active configuration".
   Choose the configuration that corresponds to the library you want to test.
   This library must have been built using the libpng MS project located in
   the "..\..\mscv" subdirectory.

2) Select "Build|Clean"

3) Select "Build|Rebuild All"

4) After compiling and linking VisualPng will be started to view an image
   from the PngSuite directory.  Press Ctrl-N (and Ctrl-V) for other images.


To install:

When distributing VisualPng (or a further development) the following options
are available:

1) Build the program with the configuration "Win32 LIB" and you only need to
   include the executable from the ./lib directory in your distribution.

2) Build the program with the configuration "Win32 DLL" and you need to put
   in your distribution the executable from the ./dll directory and the dll's
   libpng1.dll, zlib.dll and msvcrt.dll.  These need to be in the user's PATH.


Willem van Schaik
Calgary, June 6th 2000

P.S. VisualPng was written based on preliminary work of:

    - Simon-Pierre Cadieux
    - Glenn Randers-Pehrson
    - Greg Roelofs

This directory contains test configuration files, currently always '.dfa' files
intended to be used in the build by setting the make macro DFA_XTRA to the name
of the file.

These files are used in release validation of the 'configure' builds of libpng
by building 'make check', or 'make all-am' for cross-builds, with each .dfa
file.

The files in this directory may change between minor releases, however
contributions describing specific builds of libpng are welcomed.  There is no
guarantee that libpng will continue to build with such configurations; support
for given configurations can be, and has been, dropped between successive minor
releases.  However if a .dfa file describing a configuration is not in this
directory it is very unlikely that it will be tested before a minor release!

You can use these .dfa files as the basis of new configurations.  Files in this
directory should not have any use restrictions or restrictive licenses.

This directory is not included in the .zip and .7z distributions, which do
not contain 'configure' scripts.

DOCUMENTATION
=============

Examples:
   ${srcdir}/pngusr.dfa
   ${srcdir}/contrib/pngminim/*/pngusr.dfa

Documentation of the options:
   ${srcdir}/scripts/pnglibconf.dfa

Documentation of the file format:
   ${srcdir}/scripts/options.awk

FILE NAMING
===========

File names in this directory may NOT contain any of the five characters:

   - , + * ?

Neither may they contain any space character.

While other characters may be used it is strongly suggested that file names be
limited to lower case Latiin alphabetic characters (a-z), digits (0-9) and, if
necessary the underscore (_) character.  File names should be about 8 characters
long (excluding the .dfa extension).  Submitted .dfa files should have names
between 7 and 16 characters long, shorter names (6 characters or less) are
reserved for standard tests.

This demonstrates the use of PNG_USER_CONFIG, pngusr.h and pngusr.dfa
to build minimal decoder, encoder, and progressive reader applications.

See the individual README and pngusr.dfa files for more explanation.
This demonstrates the use of PNG_USER_CONFIG, pngusr.h and pngusr.dfa

The makefile builds a minimal read-only decoder with embedded libpng
and zlib.

Specify the location of the zlib source (1.2.1 or later) as ZLIBSRC
on the make command line.

If you prefer to use the shared libraries, go to contrib/pngminus
and build the png2pnm application there.
This demonstrates the use of PNG_USER_CONFIG and pngusr.h

The makefile builds a minimal read-only progressive decoder with
embedded libpng, zlib and your system's X library.

Specify the location of the zlib source (1.2.1 or later) as ZLIBSRC
on the make command line.

Edit makefile if required, to find your X library and include files,
then

    make ZLIBSRC=directory

If you prefer to use the shared libraries, go to contrib/gregbook
and build the rpng2-x application there.
This demonstrates the use of PNG_USER_CONFIG and pngusr.h

The makefile builds a minimal write-only encoder with embedded libpng
and zlib.

Specify the location of the zlib source (1.2.1 or later) as ZLIBSRC
on the make command line.

If you prefer to use the shared libraries, go to contrib/pngminus
and build the pnm2png application there.
                     ===========================
                      PNG: The Definitive Guide
                     ===========================

                             Source Code

Chapters 13, 14 and 15 of "PNG: The Definitive Guide" discuss three free,
cross-platform demo programs that show how to use the libpng reference
library:  rpng, rpng2 and wpng.  rpng and rpng2 are viewers; the first is
a very simple example that that shows how a standard file-viewer might use
libpng, while the second is designed to process streaming data and shows
how a web browser might be written.  wpng is a simple command-line program
that reads binary PGM and PPM files (the ``raw'' grayscale and RGB subsets
of PBMPLUS/NetPBM) and converts them to PNG.

The source code for all three demo programs currently compiles under
Unix, OpenVMS, and 32-bit Windows.  (Special thanks to Martin Zinser,
zinser at decus.de, for making the necessary changes for OpenVMS and for
providing an appropriate build script.)  Build instructions can be found
below.

Files:

   README             this file
   LICENSE            terms of distribution and reuse (BSD-like or GNU GPL)
   COPYING            GNU General Public License (GPL)

   Makefile.unx       Unix makefile
   Makefile.w32       Windows (MSVC) makefile
   makevms.com        OpenVMS build script

   rpng-win.c         Windows front end for the basic viewer
   rpng-x.c           X Window System (Unix, OpenVMS) front end
   readpng.c          generic back end for the basic viewer
   readpng.h          header file for the basic viewer

   rpng2-win.c        Windows front end for the progressive viewer
   rpng2-x.c          X front end for the progressive viewer
   readpng2.c         generic back end for the progressive viewer
   readpng2.h         header file for the progressive viewer

   wpng.c             generic (text) front end for the converter
   writepng.c         generic back end for the converter
   writepng.h         header file for the converter

   toucan.png         transparent PNG for testing (by Stefan Schneider)

Note that, although the programs are designed to be functional, their
primary purpose is to illustrate how to use libpng to add PNG support to
other programs.  As such, their user interfaces are crude and definitely
are not intended for everyday use.

Please see http://www.libpng.org/pub/png/pngbook.html for further infor-
mation and links to the latest version of the source code, and Chapters
13-15 of the book for detailed discussion of the three programs.

Greg Roelofs
https://pobox.com/~newt/greg_contact.html
16 March 2008


BUILD INSTRUCTIONS

 - Prerequisites (in order of compilation):

      - zlib            https://zlib.net/
      - libpng          http://www.libpng.org/pub/png/libpng.html
      - pngbook         http://www.libpng.org/pub/png/book/sources.html

     The pngbook demo programs are explicitly designed to demonstrate proper
     coding techniques for using the libpng reference library.  As a result,
     you need to download and build both zlib (on which libpng depends) and
     libpng.  A common build setup is to place the zlib, libpng and pngbook
     subdirectory trees ("folders") in the same parent directory.  Then the
     libpng build can refer to files in ../zlib (or ..\zlib or [-.zlib]),
     and similarly for the pngbook build.

     Note that all three packages are designed to be built from a command
     line by default; those who wish to use a graphical or other integrated
     development environments are on their own.


 - Unix:

     Unpack the latest pngbook sources (which should correspond to this
     README file) into a directory and change into that directory.

     Copy Makefile.unx to Makefile and edit the PNG* and Z* variables
     appropriately (possibly also the X* variables if necessary).

     make

     There is no "install" target, so copy the three executables somewhere
     in your path or run them from the current directory.  All three will
     print a basic usage screen when run without any command-line arguments;
     see the book for more details.


 - Windows:

     Unpack the latest pngbook sources (which should correspond to this
     README file) into a folder, open a "DOS shell" or "command prompt"
     or equivalent command-line window, and cd into the folder where you
     unpacked the source code.

     For MSVC, set up the necessary environment variables by invoking

        %devstudio%\vc\bin\vcvars32.bat

     where where %devstudio% is the installation directory for MSVC /
     DevStudio.  If you get "environment out of space" errors under 95/98,
     create a desktop shortcut with "c:\windows\command.com /e:4096" as
     the program command line and set the working directory to the pngbook
     directory.  Then double-click to open the new DOS-prompt window with
     a bigger environment and retry the commands above.

     Copy Makefile.w32 to Makefile and edit the PNGPATH and ZPATH variables
     appropriately (possibly also the "INC" and "LIB" variables if needed).
     Note that the names of the dynamic and static libpng and zlib libraries
     used in the makefile may change in later releases of the libraries.
     Also note that, as of libpng version 1.0.5, MSVC DLL builds do not work.
     This makefile therefore builds statically linked executables, but if
     the DLL problems ever get fixed, uncommenting the appropriate PNGLIB
     and ZLIB lines will build dynamically linked executables instead.

     Do the build by typing

        nmake

     The result should be three executables:  rpng-win.exe, rpng2-win.exe,
     and wpng.exe.  Copy them somewhere in your PATH or run them from the
     current folder.  Like the Unix versions, the two windowed programs
     (rpng and rpng2) now display a usage screen in a console window when
     invoked without command-line arguments; this is new behavior as of
     the June 2001 release.  Note that the programs use the Unix-style "-"
     character to specify options, instead of the more common DOS/Windows
     "/" character.  (For example:  "rpng2-win -bgpat 4 foo.png", not
     "rpng2-win /bgpat 4 foo.png")


 - OpenVMS:

     Unpack the pngbook sources into a subdirectory and change into that
     subdirectory.

     Edit makevms.com appropriately, specifically the zpath and pngpath
     variables.

     @makevms

     To run the programs, they probably first need to be set up as "foreign
     symbols," with "disk" and "dir" set appropriately:

     $ rpng  == "$disk:[dir]rpng-x.exe"
     $ rpng2 == "$disk:[dir]rpng2-x.exe"
     $ wpng  == "$disk:[dir]wpng.exe"

     All three will print a basic usage screen when run without any command-
     line arguments; see the book for more details.  Note that the options
     style is Unix-like, i.e., preceded by "-" rather than "/".


RUNNING THE PROGRAMS:  (VERY) BRIEF INTRO

     rpng is a simple PNG viewer that can display transparent PNGs with a
     specified background color; for example,

        rpng -bgcolor \#ff0000 toucan.png

     would display the image with a red background.  rpng2 is a progressive
     viewer that simulates a web browser in some respects; it can display
     images against either a background color or a dynamically generated
     background image.  For example:

        rpng2 -bgpat 16 toucan.png

     wpng is a purely command-line image converter from binary PBMPLUS/NetPBM
     format (.pgm or .ppm) to PNG; for example,

        wpng -time < toucan-notrans.ppm > toucan-notrans.png

     would convert the specified PPM file (using redirection) to PNG, auto-
     matically setting the PNG modification-time chunk.

     All options can be abbreviated to the shortest unique value; for example,
     "-bgc" for -bgcolor (versus "-bgp" for -bgpat), or "-g" for -gamma.
This directory (contrib/tools) contains tools used by the authors of libpng.

Code and data placed in this directory is not required to build libpng,
however the code in this directory has been used to generate data or code in
the body of the libpng source.  The source code identifies where this has
been done.  Code in this directory may not compile on all operating systems
that libpng supports.

NO COPYRIGHT RIGHTS ARE CLAIMED TO ANY OF THE FILES IN THIS DIRECTORY.

To the extent possible under law, the authors have waived all copyright and
related or neighboring rights to this work.  This work is published from:
United States.

The files may be used freely in any way.

The source code and comments in this directory are the original work of the
people named below.  No other person or organization has made contributions to
the work in this directory.

ORIGINAL AUTHORS
    The following people have contributed to the code in this directory.  None
    of the people below claim any rights with regard to the contents of this
    directory.

    John Bowler <jbowler at acm.org>
    Glenn Randers-Pehrson <glennrp at users.sourceforge.net>
Microsoft Developer Studio Project File, Format Version 7.10 for libpng.

Copyright (C) 2004 Simon-Pierre Cadieux.

This code is released under the libpng license.
For conditions of distribution and use, see copyright notice in png.h

NOTE: This project will be removed from libpng-1.5.0.  It has
been replaced with the "vstudio" project.

Assumptions:
* The libpng source files are in ..\..
* The zlib source files are in ..\..\..\zlib
* The zlib project file is in . /* Warning: This is until the zlib project
  files get intergrated into the next zlib release. The final zlib project
  directory will then be ..\..\..\zlib\projects\visualc71. */

To use:

1) On the main menu, select "File | Open Solution".
   Open "libpng.sln".

2) Display the Solution Explorer view (Ctrl+Alt+L)

3) Set one of the project as the StartUp project. If you just want to build the
   binaries set "libpng" as the startup project (Select "libpng" tree view
   item + Project | Set as StartUp project). If you want to build and test the
   binaries set it to "pngtest" (Select "pngtest" tree view item +
   Project | Set as StartUp project)

4) Select "Build | Configuration Manager...".
   Choose the configuration you wish to build.

5) Select "Build | Clean Solution".

6) Select "Build | Build Solution (Ctrl-Shift-B)"

This project builds the libpng binaries as follows:

* Win32_DLL_Release\libpng16.dll      DLL build
* Win32_DLL_Debug\libpng16d.dll       DLL build (debug version)
* Win32_DLL_VB\libpng16vb.dll         DLL build for Visual Basic, using stdcall
* Win32_LIB_Release\libpng.lib        static build
* Win32_LIB_Debug\libpngd.lib         static build (debug version)

Notes:

If you change anything in the source files, or select different compiler
settings, please change the DLL name to something different than any of
the above names. Also, make sure that in your "pngusr.h" you define
PNG_USER_PRIVATEBUILD and PNG_USER_DLLFNAME_POSTFIX according to the
instructions provided in "pngconf.h".

All DLLs built by this project use the Microsoft dynamic C runtime library
MSVCR71.DLL (MSVCR71D.DLL for debug versions).  If you distribute any of the
above mentioned libraries you may have to include this DLL in your package.
For a list of files that are redistributable in Visual Studio see
$(VCINSTALLDIR)\redist.txt.
/* WARNING: This file was put in the LibPNG distribution for convenience only.
            It is expected to be part of the next zlib release under
            "projects\visualc71\README.txt." */

Microsoft Developer Studio Project File, Format Version 7.10 for zlib.

Copyright (C) 2004 Simon-Pierre Cadieux.
Copyright (C) 2004 Cosmin Truta.

This code is released under the libpng license.
For conditions of distribution and use, see copyright notice in zlib.h.

NOTE: This project will be removed from libpng-1.5.0.  It has
been replaced with the "vstudio" project.

To use:

1) On the main menu, select "File | Open Solution".
   Open "zlib.sln".

2) Display the Solution Explorer view (Ctrl+Alt+L)

3) Set one of the project as the StartUp project. If you just want to build the
   binaries set "zlib" as the startup project (Select "zlib" tree view item +
   Project | Set as StartUp project). If you want to build and test the
   binaries set it to "example" (Select "example" tree view item + Project |
   Set as StartUp project), If you want to build the minigzip utility set it to
   "minigzip" (Select "minigzip" tree view item + Project | Set as StartUp
   project

4) Select "Build | Configuration Manager...".
   Choose the configuration you wish to build.

5) Select "Build | Clean Solution".

6) Select "Build | Build Solution (Ctrl-Shift-B)"

This project builds the zlib binaries as follows:

* Win32_DLL_Release\zlib1.dll       DLL build
* Win32_DLL_Debug\zlib1d.dll        DLL build (debug version)
* Win32_LIB_Release\zlib.lib        static build
* Win32_LIB_Debug\zlibd.lib         static build (debug version)


VisualStudio instructions

libpng version 1.6.32 - August 24, 2017

Copyright (c) 2010,2013,2015 Glenn Randers-Pehrson

This code is released under the libpng license.
For conditions of distribution and use, see the disclaimer
and license in png.h

This directory  contains support for building libpng under MicroSoft
VisualStudio 2010.  It may also work under later versions of VisualStudio.
You should be familiar with VisualStudio before using this directory.

Initial preparations
====================
You must enter some information in zlib.props before attempting to build
with this 'solution'.  Please read and edit zlib.props first.  You will
probably not be familiar with the contents of zlib.props - do not worry,
it is mostly harmless.

This is all you need to do to build the 'release' and 'release library'
configurations.

Debugging
=========
The release configurations default to /Ox optimization.  Full debugging
information is produced (in the .pdb), but if you encounter a problem the
optimization may make it difficult to debug.  Simply rebuild with a lower
optimization level (e.g. /Od.)

Linking your application
========================
Normally you should link against the 'release' configuration.  This builds a
DLL for libpng with the default runtime options used by Visual Studio 2010.
In particular the runtime library is the "MultiThreaded DLL" version.
If you use Visual Studio defaults to build your application you will have no
problems.

If you don't use the Visual Studio defaults your application must still be
built with the default runtime option (/MD).  If, for some reason, it is not
then your application will crash inside libpng16.dll as soon as libpng
tries to read from a file handle you pass in.

If you do not want to use the DLL, for example for a very small application,
the 'release library' configuration may be more appropriate.  This is built
with a non-standard runtime library - the "MultiThreaded" version.  When you
build your application it must be compiled with this option (/MT), otherwise
it will not build (if you are lucky) or crash (if you are not.) See the
WARNING file that is distributed along with this readme.txt.

Stop reading here
=================
You have enough information to build a working application.

Debug versions have limited support
===================================
This solution includes limited support for debug versions of libpng.  You
do not need these unless your own solution itself uses debug builds (it is
far more effective to debug on the release builds, there is no point building
a special debug build unless you have heap corruption problems that you can't
track down.)

The debug build of libpng is minimally supported.  Support for debug builds of
zlib is also minimal.  You really don't want to do this.

WARNING
=======
Libpng 1.6.x does not use the default run-time library when building static
library builds of libpng; instead of the shared DLL runtime it uses a static
runtime.  If you need to change this make sure to change the setting on all the
relevant projects:

    libpng
    zlib
    all the test programs

The runtime library settings for each build are as follows:

               Release        Debug
    DLL         /MD            /MDd
    Library     /MT            /MTd

NOTICE that libpng 1.5.x erroneously used /MD for Debug DLL builds; if you used
the debug builds in your app and you changed your app to use /MD you will need
to change it back to /MDd for libpng 1.6.0 and later.

The Visual Studio 2010 defaults for a Win32 DLL or Static Library project are
as follows:

                     Release     Debug
    DLL               /MD         /MDd
    Static Library    /MD         /MDd

Also, be sure to build libpng, zlib, and your project all for the same
platform (e.g., 32-bit or 64-bit).
ZLIB DATA COMPRESSION LIBRARY

zlib 1.2.11 is a general purpose data compression library.  All the code is
thread safe.  The data format used by the zlib library is described by RFCs
(Request for Comments) 1950 to 1952 in the files
http://tools.ietf.org/html/rfc1950 (zlib format), rfc1951 (deflate format) and
rfc1952 (gzip format).

All functions of the compression library are documented in the file zlib.h
(volunteer to write man pages welcome, contact zlib@gzip.org).  A usage example
of the library is given in the file test/example.c which also tests that
the library is working correctly.  Another example is given in the file
test/minigzip.c.  The compression library itself is composed of all source
files in the root directory.

To compile all files and run the test program, follow the instructions given at
the top of Makefile.in.  In short "./configure; make test", and if that goes
well, "make install" should work for most flavors of Unix.  For Windows, use
one of the special makefiles in win32/ or contrib/vstudio/ .  For VMS, use
make_vms.com.

Questions about zlib should be sent to <zlib@gzip.org>, or to Gilles Vollant
<info@winimage.com> for the Windows DLL version.  The zlib home page is
http://zlib.net/ .  Before reporting a problem, please check this site to
verify that you have the latest version of zlib; otherwise get the latest
version and check whether the problem still exists or not.

PLEASE read the zlib FAQ http://zlib.net/zlib_faq.html before asking for help.

Mark Nelson <markn@ieee.org> wrote an article about zlib for the Jan.  1997
issue of Dr.  Dobb's Journal; a copy of the article is available at
http://marknelson.us/1997/01/01/zlib-engine/ .

The changes made in version 1.2.11 are documented in the file ChangeLog.

Unsupported third party contributions are provided in directory contrib/ .

zlib is available in Java using the java.util.zip package, documented at
http://java.sun.com/developer/technicalArticles/Programming/compression/ .

A Perl interface to zlib written by Paul Marquess <pmqs@cpan.org> is available
at CPAN (Comprehensive Perl Archive Network) sites, including
http://search.cpan.org/~pmqs/IO-Compress-Zlib/ .

A Python interface to zlib written by A.M. Kuchling <amk@amk.ca> is
available in Python 1.5 and later versions, see
http://docs.python.org/library/zlib.html .

zlib is built into tcl: http://wiki.tcl.tk/4610 .

An experimental package to read and write files in .zip format, written on top
of zlib by Gilles Vollant <info@winimage.com>, is available in the
contrib/minizip directory of zlib.


Notes for some targets:

- For Windows DLL versions, please see win32/DLL_FAQ.txt

- For 64-bit Irix, deflate.c must be compiled without any optimization. With
  -O, one libpng test fails. The test works in 32 bit mode (with the -n32
  compiler flag). The compiler bug has been reported to SGI.

- zlib doesn't work with gcc 2.6.3 on a DEC 3000/300LX under OSF/1 2.1 it works
  when compiled with cc.

- On Digital Unix 4.0D (formely OSF/1) on AlphaServer, the cc option -std1 is
  necessary to get gzprintf working correctly. This is done by configure.

- zlib doesn't work on HP-UX 9.05 with some versions of /bin/cc. It works with
  other compilers. Use "make test" to check your compiler.

- gzdopen is not supported on RISCOS or BEOS.

- For PalmOs, see http://palmzlib.sourceforge.net/


Acknowledgments:

  The deflate format used by zlib was defined by Phil Katz.  The deflate and
  zlib specifications were written by L.  Peter Deutsch.  Thanks to all the
  people who reported problems and suggested various improvements in zlib; they
  are too numerous to cite here.

Copyright notice:

 (C) 1995-2017 Jean-loup Gailly and Mark Adler

  This software is provided 'as-is', without any express or implied
  warranty.  In no event will the authors be held liable for any damages
  arising from the use of this software.

  Permission is granted to anyone to use this software for any purpose,
  including commercial applications, and to alter it and redistribute it
  freely, subject to the following restrictions:

  1. The origin of this software must not be misrepresented; you must not
     claim that you wrote the original software. If you use this software
     in a product, an acknowledgment in the product documentation would be
     appreciated but is not required.
  2. Altered source versions must be plainly marked as such, and must not be
     misrepresented as being the original software.
  3. This notice may not be removed or altered from any source distribution.

  Jean-loup Gailly        Mark Adler
  jloup@gzip.org          madler@alumni.caltech.edu

If you use the zlib library in a product, we would appreciate *not* receiving
lengthy legal documents to sign.  The sources are provided for free but without
warranty of any kind.  The library has been entirely written by Jean-loup
Gailly and Mark Adler; it does not include third-party code.

If you redistribute modified sources, we would appreciate that you include in
the file ChangeLog history information documenting your changes.  Please read
the FAQ for more information on the distribution of modified source versions.
This directory contains examples of the use of zlib and other relevant
programs and documentation.

enough.c
    calculation and justification of ENOUGH parameter in inftrees.h
    - calculates the maximum table space used in inflate tree
      construction over all possible Huffman codes

fitblk.c
    compress just enough input to nearly fill a requested output size
    - zlib isn't designed to do this, but fitblk does it anyway

gun.c
    uncompress a gzip file
    - illustrates the use of inflateBack() for high speed file-to-file
      decompression using call-back functions
    - is approximately twice as fast as gzip -d
    - also provides Unix uncompress functionality, again twice as fast

gzappend.c
    append to a gzip file
    - illustrates the use of the Z_BLOCK flush parameter for inflate()
    - illustrates the use of deflatePrime() to start at any bit

gzjoin.c
    join gzip files without recalculating the crc or recompressing
    - illustrates the use of the Z_BLOCK flush parameter for inflate()
    - illustrates the use of crc32_combine()

gzlog.c
gzlog.h
    efficiently and robustly maintain a message log file in gzip format
    - illustrates use of raw deflate, Z_PARTIAL_FLUSH, deflatePrime(),
      and deflateSetDictionary()
    - illustrates use of a gzip header extra field

zlib_how.html
    painfully comprehensive description of zpipe.c (see below)
    - describes in excruciating detail the use of deflate() and inflate()

zpipe.c
    reads and writes zlib streams from stdin to stdout
    - illustrates the proper use of deflate() and inflate()
    - deeply commented in zlib_how.html (see above)

zran.c
    index a zlib or gzip stream and randomly access it
    - illustrates the use of Z_BLOCK, inflatePrime(), and
      inflateSetDictionary() to provide random access
All files under this contrib directory are UNSUPPORTED. There were
provided by users of zlib and were not tested by the authors of zlib.
Use at your own risk. Please contact the authors of the contributions
for help about these, not the zlib authors. Thanks.


ada/        by Dmitriy Anisimkov <anisimkov@yahoo.com>
        Support for Ada
        See http://zlib-ada.sourceforge.net/

amd64/      by Mikhail Teterin <mi@ALDAN.algebra.com>
        asm code for AMD64
        See patch at http://www.freebsd.org/cgi/query-pr.cgi?pr=bin/96393

asm686/     by Brian Raiter <breadbox@muppetlabs.com>
        asm code for Pentium and PPro/PII, using the AT&T (GNU as) syntax
        See http://www.muppetlabs.com/~breadbox/software/assembly.html

blast/      by Mark Adler <madler@alumni.caltech.edu>
        Decompressor for output of PKWare Data Compression Library (DCL)

delphi/     by Cosmin Truta <cosmint@cs.ubbcluj.ro>
        Support for Delphi and C++ Builder

dotzlib/    by Henrik Ravn <henrik@ravn.com>
        Support for Microsoft .Net and Visual C++ .Net

gcc_gvmat64/by Gilles Vollant <info@winimage.com>
        GCC Version of x86 64-bit (AMD64 and Intel EM64t) code for x64
        assembler to replace longest_match() and inflate_fast()

infback9/   by Mark Adler <madler@alumni.caltech.edu>
        Unsupported diffs to infback to decode the deflate64 format

inflate86/  by Chris Anderson <christop@charm.net>
        Tuned x86 gcc asm code to replace inflate_fast()

iostream/   by Kevin Ruland <kevin@rodin.wustl.edu>
        A C++ I/O streams interface to the zlib gz* functions

iostream2/  by Tyge Løvset <Tyge.Lovset@cmr.no>
        Another C++ I/O streams interface

iostream3/  by Ludwig Schwardt <schwardt@sun.ac.za>
            and Kevin Ruland <kevin@rodin.wustl.edu>
        Yet another C++ I/O streams interface

masmx64/    by Gilles Vollant <info@winimage.com>
        x86 64-bit (AMD64 and Intel EM64t) code for x64 assembler to
        replace longest_match() and inflate_fast(),  also masm x86
        64-bits translation of Chris Anderson inflate_fast()

masmx86/    by Gilles Vollant <info@winimage.com>
        x86 asm code to replace longest_match() and inflate_fast(),
        for Visual C++ and MASM (32 bits).
        Based on Brian Raiter (asm686) and Chris Anderson (inflate86)

minizip/    by Gilles Vollant <info@winimage.com>
        Mini zip and unzip based on zlib
        Includes Zip64 support by Mathias Svensson <mathias@result42.com>
        See http://www.winimage.com/zLibDll/minizip.html

pascal/     by Bob Dellaca <bobdl@xtra.co.nz> et al.
        Support for Pascal

puff/       by Mark Adler <madler@alumni.caltech.edu>
        Small, low memory usage inflate.  Also serves to provide an
        unambiguous description of the deflate format.

testzlib/   by Gilles Vollant <info@winimage.com>
        Example of the use of zlib

untgz/      by Pedro A. Aranda Gutierrez <paag@tid.es>
        A very simple tar.gz file extractor using zlib

vstudio/    by Gilles Vollant <info@winimage.com>
        Building a minizip-enhanced zlib with Microsoft Visual Studio
        Includes vc11 from kreuzerkrieg and vc12 from davispuh
Puff -- A Simple Inflate
3 Mar 2003
Mark Adler
madler@alumni.caltech.edu

What this is --

puff.c provides the routine puff() to decompress the deflate data format.  It
does so more slowly than zlib, but the code is about one-fifth the size of the
inflate code in zlib, and written to be very easy to read.

Why I wrote this --

puff.c was written to document the deflate format unambiguously, by virtue of
being working C code.  It is meant to supplement RFC 1951, which formally
describes the deflate format.  I have received many questions on details of the
deflate format, and I hope that reading this code will answer those questions.
puff.c is heavily commented with details of the deflate format, especially
those little nooks and cranies of the format that might not be obvious from a
specification.

puff.c may also be useful in applications where code size or memory usage is a
very limited resource, and speed is not as important.

How to use it --

Well, most likely you should just be reading puff.c and using zlib for actual
applications, but if you must ...

Include puff.h in your code, which provides this prototype:

int puff(unsigned char *dest,           /* pointer to destination pointer */
         unsigned long *destlen,        /* amount of output space */
         unsigned char *source,         /* pointer to source data pointer */
         unsigned long *sourcelen);     /* amount of input available */

Then you can call puff() to decompress a deflate stream that is in memory in
its entirety at source, to a sufficiently sized block of memory for the
decompressed data at dest.  puff() is the only external symbol in puff.c  The
only C library functions that puff.c needs are setjmp() and longjmp(), which
are used to simplify error checking in the code to improve readabilty.  puff.c
does no memory allocation, and uses less than 2K bytes off of the stack.

If destlen is not enough space for the uncompressed data, then inflate will
return an error without writing more than destlen bytes.  Note that this means
that in order to decompress the deflate data successfully, you need to know
the size of the uncompressed data ahead of time.

If needed, puff() can determine the size of the uncompressed data with no
output space.  This is done by passing dest equal to (unsigned char *)0.  Then
the initial value of *destlen is ignored and *destlen is set to the length of
the uncompressed data.  So if the size of the uncompressed data is not known,
then two passes of puff() can be used--first to determine the size, and second
to do the actual inflation after allocating the appropriate memory.  Not
pretty, but it works.  (This is one of the reasons you should be using zlib.)

The deflate format is self-terminating.  If the deflate stream does not end
in *sourcelen bytes, puff() will return an error without reading at or past
endsource.

On return, *sourcelen is updated to the amount of input data consumed, and
*destlen is updated to the size of the uncompressed data.  See the comments
in puff.c for the possible return codes for puff().
These classes provide a C++ stream interface to the zlib library. It allows you
to do things like:

  gzofstream outf("blah.gz");
  outf << "These go into the gzip file " << 123 << endl;

It does this by deriving a specialized stream buffer for gzipped files, which is
the way Stroustrup would have done it. :->

The gzifstream and gzofstream classes were originally written by Kevin Ruland
and made available in the zlib contrib/iostream directory. The older version still
compiles under gcc 2.xx, but not under gcc 3.xx, which sparked the development of
this version.

The new classes are as standard-compliant as possible, closely following the
approach of the standard library's fstream classes. It compiles under gcc versions
3.2 and 3.3, but not under gcc 2.xx. This is mainly due to changes in the standard
library naming scheme. The new version of gzifstream/gzofstream/gzfilebuf differs
from the previous one in the following respects:
- added showmanyc
- added setbuf, with support for unbuffered output via setbuf(0,0)
- a few bug fixes of stream behavior
- gzipped output file opened with default compression level instead of maximum level
- setcompressionlevel()/strategy() members replaced by single setcompression()

The code is provided "as is", with the permission to use, copy, modify, distribute
and sell it for any purpose without fee.

Ludwig Schwardt
<schwardt@sun.ac.za>

DSP Lab
Electrical & Electronic Engineering Department
University of Stellenbosch
South Africa
This is a patched version of zlib, modified to use
Pentium-Pro-optimized assembly code in the deflation algorithm. The
files changed/added by this patch are:

README.686
match.S

The speedup that this patch provides varies, depending on whether the
compiler used to build the original version of zlib falls afoul of the
PPro's speed traps. My own tests show a speedup of around 10-20% at
the default compression level, and 20-30% using -9, against a version
compiled using gcc 2.7.2.3. Your mileage may vary.

Note that this code has been tailored for the PPro/PII in particular,
and will not perform particuarly well on a Pentium.

If you are using an assembler other than GNU as, you will have to
translate match.S to use your assembler's syntax. (Have fun.)

Brian Raiter
breadbox@muppetlabs.com
April, 1998


Added for zlib 1.1.3:

The patches come from
http://www.muppetlabs.com/~breadbox/software/assembly.html

To compile zlib with this asm file, copy match.S to the zlib directory
then do:

CFLAGS="-O3 -DASMV" ./configure
make OBJA=match.o


Update:

I've been ignoring these assembly routines for years, believing that
gcc's generated code had caught up with it sometime around gcc 2.95
and the major rearchitecting of the Pentium 4. However, I recently
learned that, despite what I believed, this code still has some life
in it. On the Pentium 4 and AMD64 chips, it continues to run about 8%
faster than the code produced by gcc 4.1.

In acknowledgement of its continuing usefulness, I've altered the
license to match that of the rest of zlib. Share and Enjoy!

Brian Raiter
breadbox@muppetlabs.com
April, 2007
Read blast.h for purpose and usage.

Mark Adler
madler@alumni.caltech.edu
See infback9.h for what this is and how to use it.
        ZLIB version 1.2.11 for OS/400 installation instructions

1) Download and unpack the zlib tarball to some IFS directory.
   (i.e.: /path/to/the/zlib/ifs/source/directory)

   If the installed IFS command suppors gzip format, this is straightforward,
else you have to unpack first to some directory on a system supporting it,
then move the whole directory to the IFS via the network (via SMB or FTP).

2) Edit the configuration parameters in the compilation script.

        EDTF STMF('/path/to/the/zlib/ifs/source/directory/os400/make.sh')

Tune the parameters according to your needs if not matching the defaults.
Save the file and exit after edition.

3) Enter qshell, then work in the zlib OS/400 specific directory.

        QSH
        cd /path/to/the/zlib/ifs/source/directory/os400

4) Compile and install

        sh make.sh

The script will:
- create the libraries, objects and IFS directories for the zlib environment,
- compile all modules,
- create a service program,
- create a static and a dynamic binding directory,
- install header files for C/C++ and for ILE/RPG, both for compilation in
  DB2 and IFS environments.

That's all. 


Notes:  For OS/400 ILE RPG programmers, a /copy member defining the ZLIB
                API prototypes for ILE RPG can be found in ZLIB/H(ZLIB.INC).
                In the ILE environment, the same definitions are available from
                file zlib.inc located in the same IFS include directory as the
                C/C++ header files.
                Please read comments in this member for more information.

        Remember that most foreign textual data are ASCII coded: this
                implementation does not handle conversion from/to ASCII, so
                text data code conversions must be done explicitely.

        Mainly for the reason above, always open zipped files in binary mode.
This directory contains files that have not been updated for zlib 1.2.x

(Volunteers are encouraged to help clean this up.  Thanks.)
This Makefile requires devkitARM (http://www.devkitpro.org/category/devkitarm/) and works inside "contrib/nds". It is based on a devkitARM template.

Eduardo Costa <eduardo.m.costa@gmail.com>
January 3, 2009

ZLIB DATA COMPRESSION LIBRARY

zlib 1.2.11 is a general purpose data compression library.  All the code is
thread safe.  The data format used by the zlib library is described by RFCs
(Request for Comments) 1950 to 1952 in the files
http://www.ietf.org/rfc/rfc1950.txt (zlib format), rfc1951.txt (deflate format)
and rfc1952.txt (gzip format).

All functions of the compression library are documented in the file zlib.h
(volunteer to write man pages welcome, contact zlib@gzip.org).  Two compiled
examples are distributed in this package, example and minigzip.  The example_d
and minigzip_d flavors validate that the zlib1.dll file is working correctly.

Questions about zlib should be sent to <zlib@gzip.org>.  The zlib home page
is http://zlib.net/ .  Before reporting a problem, please check this site to
verify that you have the latest version of zlib; otherwise get the latest
version and check whether the problem still exists or not.

PLEASE read DLL_FAQ.txt, and the the zlib FAQ http://zlib.net/zlib_faq.html
before asking for help.


Manifest:

The package zlib-1.2.11-win32-x86.zip will contain the following files:

  README-WIN32.txt This document
  ChangeLog        Changes since previous zlib packages
  DLL_FAQ.txt      Frequently asked questions about zlib1.dll
  zlib.3.pdf       Documentation of this library in Adobe Acrobat format

  example.exe      A statically-bound example (using zlib.lib, not the dll)
  example.pdb      Symbolic information for debugging example.exe

  example_d.exe    A zlib1.dll bound example (using zdll.lib)
  example_d.pdb    Symbolic information for debugging example_d.exe

  minigzip.exe     A statically-bound test program (using zlib.lib, not the dll)
  minigzip.pdb     Symbolic information for debugging minigzip.exe

  minigzip_d.exe   A zlib1.dll bound test program (using zdll.lib)
  minigzip_d.pdb   Symbolic information for debugging minigzip_d.exe

  zlib.h           Install these files into the compilers' INCLUDE path to
  zconf.h          compile programs which use zlib.lib or zdll.lib

  zdll.lib         Install these files into the compilers' LIB path if linking
  zdll.exp         a compiled program to the zlib1.dll binary

  zlib.lib         Install these files into the compilers' LIB path to link zlib
  zlib.pdb         into compiled programs, without zlib1.dll runtime dependency
                   (zlib.pdb provides debugging info to the compile time linker)

  zlib1.dll        Install this binary shared library into the system PATH, or
                   the program's runtime directory (where the .exe resides)
  zlib1.pdb        Install in the same directory as zlib1.dll, in order to debug
                   an application crash using WinDbg or similar tools.

All .pdb files above are entirely optional, but are very useful to a developer
attempting to diagnose program misbehavior or a crash.  Many additional
important files for developers can be found in the zlib127.zip source package
available from http://zlib.net/ - review that package's README file for details.


Acknowledgments:

The deflate format used by zlib was defined by Phil Katz.  The deflate and
zlib specifications were written by L.  Peter Deutsch.  Thanks to all the
people who reported problems and suggested various improvements in zlib; they
are too numerous to cite here.


Copyright notice:

  (C) 1995-2017 Jean-loup Gailly and Mark Adler

  This software is provided 'as-is', without any express or implied
  warranty.  In no event will the authors be held liable for any damages
  arising from the use of this software.

  Permission is granted to anyone to use this software for any purpose,
  including commercial applications, and to alter it and redistribute it
  freely, subject to the following restrictions:

  1. The origin of this software must not be misrepresented; you must not
     claim that you wrote the original software. If you use this software
     in a product, an acknowledgment in the product documentation would be
     appreciated but is not required.
  2. Altered source versions must be plainly marked as such, and must not be
     misrepresented as being the original software.
  3. This notice may not be removed or altered from any source distribution.

  Jean-loup Gailly        Mark Adler
  jloup@gzip.org          madler@alumni.caltech.edu

If you use the zlib library in a product, we would appreciate *not* receiving
lengthy legal documents to sign.  The sources are provided for free but without
warranty of any kind.  The library has been entirely written by Jean-loup
Gailly and Mark Adler; it does not include third-party code.

If you redistribute modified sources, we would appreciate that you include in
the file ChangeLog history information documenting your changes.  Please read
the FAQ for more information on the distribution of modified source versions.
                                  _   _ ____  _
                              ___| | | |  _ \| |
                             / __| | | | |_) | |
                            | (__| |_| |  _ <| |___
                             \___|\___/|_| \_\_____|

README

  Curl is a command line tool for transferring data specified with URL
  syntax. Find out how to use curl by reading the curl.1 man page or the
  MANUAL document. Find out how to install Curl by reading the INSTALL
  document.

  libcurl is the library curl is using to do its job. It is readily
  available to be used by your software. Read the libcurl.3 man page to
  learn how!

  You find answers to the most frequent questions we get in the FAQ document.

  Study the COPYING file for distribution terms and similar. If you distribute
  curl binaries or other binaries that involve libcurl, you might enjoy the
  LICENSE-MIXING document.

CONTACT

  If you have problems, questions, ideas or suggestions, please contact us
  by posting to a suitable mailing list. See https://curl.haxx.se/mail/

  All contributors to the project are listed in the THANKS document.

WEB SITE

  Visit the curl web site for the latest news and downloads:

        https://curl.haxx.se/

GIT

  To download the very latest source off the GIT server do this:

    git clone https://github.com/curl/curl.git

  (you'll get a directory named curl created, filled with the source code)

NOTICE

  Curl contains pieces of source code that is Copyright (c) 1998, 1999
  Kungliga Tekniska Högskolan. This notice is included here to comply with the
  distribution terms.
                                  _   _ ____  _
                              ___| | | |  _ \| |
                             / __| | | | |_) | |
                            | (__| |_| |  _ <| |___
                             \___|\___/|_| \_\_____|

Include files for libcurl, external users.

They're all placed in the curl subdirectory here for better fit in any kind
of environment. You must include files from here using...

        #include <curl/curl.h>

... style and point the compiler's include path to the directory holding the
curl subdirectory. It makes it more likely to survive future modifications.

NOTE FOR LIBCURL HACKERS

* If you check out from git on a non-configure platform, you must run the
  appropriate buildconf* script to set up files before being able of compiling
  the library.

* We cannot assume anything else but very basic compiler features being
  present. While libcurl requires an ANSI C compiler to build, some of the
  earlier ANSI compilers clearly can't deal with some preprocessor operators.

* Newlines must remain unix-style for older compilers' sake.

* Comments must be written in the old-style /* unnested C-fashion */

To figure out how to do good and portable checks for features, operating
systems or specific hardwarare, a very good resource is Bjorn Reese's
collection at https://sourceforge.net/p/predef/wiki/
Building via IDE Project Files
==============================

   This document describes how to compile, build and install curl and libcurl
   from sources using an IDE based development tool such as Visual Studio.

   Project files are currently available for Visual C++ v6.0 to v14.0. The
   following directory structure has been used to cater for this:

   somedirectory\
    |_curl
      |_projects
        |_<platform>
          |_<ide>
            |_lib
            |_src

   This structure allows for side-by-side compilation of curl on the same
   machine using different versions of a given compiler (for example VC8, VC9
   and VC10) and allows for your own application or product to be compiled
   against those variants of libcurl for example.

   Note: Typically this side-by-side compilation is generally only required
   when a library is being compiled against dynamic runtime libraries.

Dependencies
============

   The projects files also support build configurations that require third
   party dependencies such as OpenSSL, wolfSSL and SSH2. If you wish to support
   these, you will also need to download and compile those libraries as well.

   To support compilation of these libraries using different versions of
   compilers, the following directory structure has been used for both the
   output of curl and libcurl as well as these dependencies.

   somedirectory\
    |_curl
    | |_ build
    |    |_<architecture>
    |      |_<ide>
    |        |_<configuration>
    |          |_lib
    |          |_src
    |
    |_openssl
    | |_ build
    |    |_<architecture>
    |      |_VC <version>
    |        |_<configuration>
    |
    |_libssh2
      |_ build
         |_<architecture>
           |_VC <version>
             |_<configuration>

   As OpenSSL and wolfSSL don't support side-by-side compilation when using
   different versions of Visual Studio, build helper batch files have been
   provided to assist with this. Please run "build-openssl -help" and/or
   "build-wolfssl -help" for usage details.

Building with Visual C++
========================

   To build with VC++, you will of course have to first install VC++ which is
   part of Visual Studio.

   If you are building with VC6 then you will also need the February 2003
   Edition of the Windows Platform SDK which can be downloaded from:

    https://www.microsoft.com/en-us/download/details.aspx?id=12261

   If you require support for Internationalized Domain Names via Windows IDN
   then you will need either:

    * Microsoft Internationalized Domain Name (IDN) Mitigation APIs:
      https://www.microsoft.com/en-us/download/details.aspx?id=734

    * Microsoft Windows SDK Update for Windows Vista:
      https://www.microsoft.com/en-us/download/details.aspx?id=23719

    * Microsoft Visual Studio 2010 or above

   Once you have VC++ installed you should launch the application and open one
   of the solution or workspace files.

   Whilst files are provided for both libcurl and the curl command line tool as
   well as a configuration that includes both, it is recommend that you use the
   all-in-one configuration.

Running DLL based configurations
================================

   If you are a developer and plan to run the curl tool from Visual Studio (eg
   you are debugging) with any third-party libraries (such as OpenSSL, wolfSSL
   or LibSSH2) then you will need to add the search path of these DLLs to the
   configuration's PATH environment. To do that:

    * Open the 'curl-all.sln' or 'curl.sln' solutions

    * Right-click on the 'curl' project and select Properties

    * Navigate to 'Configuration Properties > Debugging > Environment'

    * Add PATH='Path to DLL';C:\Windows\system32;C:\Windows;
               C:\Windows\System32\Wbem

   ... where 'Path to DLL` is the configuration specific path. For example the
   following configurations in Visual Studio 2010 might be:
   
   DLL Debug - DLL OpenSSL (Win32):
   PATH=..\..\..\..\..\openssl\build\Win32\VC10\DLL Debug;C:\Windows\system32;
        C:\Windows;C:\Windows\System32\Wbem

   DLL Debug - DLL OpenSSL (x64):
   PATH=..\..\..\..\..\openssl\build\Win64\VC10\DLL Debug;C:\Windows\system32;
        C:\Windows;C:\Windows\System32\Wbem

   DLL Debug - DLL wolfSSL (Win32):
   PATH=..\..\..\..\..\wolfssl\build\Win32\VC10\DLL Debug;C:\Windows\system32;
        C:\Windows;C:\Windows\System32\Wbem

   DLL Debug - DLL wolfSSL (x64):
   PATH=..\..\..\..\..\wolfssl\build\Win64\VC10\DLL Debug;C:\Windows\system32;
        C:\Windows;C:\Windows\System32\Wbem

   If you are using a configuration that uses multiple third-party library DLLs
   (such as DLL Debug - DLL OpenSSL - DLL LibSSH2) then 'Path to DLL' will need
   to contain the path to both of these.

Notes
=====

   The following keywords have been used in the directory hierarchy:
   
   <platform>      - The platform (For example: Windows)
   <ide>           - The IDE (For example: VC6, VC10, BCC5)
   <architecture>  - The platform architecture (For example: Win32, Win64)
   <configuration> - The target configuration (For example: DLL Debug,
                     LIB Release - LIB OpenSSL)

   If you are using the source code from the git repository, rather than a
   release archive or nightly build, you will need to generate the project
   files. Please run "generate -help" for usage details. 

   Should you wish to help out with some of the items on the TODO list, or
   find bugs in the project files that need correcting, and would like to
   submit updated files back then please note that, whilst the solution files
   can be edited directly, the templates for the project files (which are 
   stored in the git repositoty) will need to be modified rather than the
   generated project files that Visual Studio uses.

Legacy Windows and SSL
======================

   Some of the project configurations allow the use of WinSSL (specifically
   SChannel from Windows SSPI), the native SSL library in Windows. However,
   WinSSL in Windows <= XP is unable to connect to servers that no longer
   support the legacy handshakes and algorithms used by those versions. If
   you will be using curl in one of those earlier versions of Windows you
   should choose another SSL backend such as OpenSSL.
                                  _   _ ____  _
                              ___| | | |  _ \| |
                             / __| | | | |_) | |
                            | (__| |_| |  _ <| |___
                             \___|\___/|_| \_\_____|

PACKAGES

 This directory and all its subdirectories are for special package
information, template, scripts and docs. The files herein should be of use for
those of you who want to package curl in a binary or source format using one
of those custom formats.

 The hierarchy for these directories is something like this:

   packages/[OS]/[FORMAT]/

 Currently, we have Win32 and Linux for [OS]. There might be different formats
for the same OS so for Linux we have RPM as format.

 We might need to add some differentiation for CPU as well, as there is
Linux-RPMs for several CPUs. However, it might not be necessary since the
packaging should be pretty much the same no matter what CPU that is used.

 For each unique OS-FORMAT pair, there's a directory to "fill"! I'd like to
see a single README with as much details as possible, and then I'd like some
template files for the package process.

Implementation notes:

  This is a true OS/400 implementation, not a PASE implementation (for PASE,
use AIX implementation).

  The biggest problem with OS/400 is EBCDIC. Libcurl implements an internal
conversion mechanism, but it has been designed for computers that have a
single native character set. OS/400 default native character set varies
depending on the country for which it has been localized. And more, a job
may dynamically alter its "native" character set.
  Several characters that do not have fixed code in EBCDIC variants are
used in libcurl strings. As a consequence, using the existing conversion
mechanism would have lead in a localized binary library - not portable across
countries.
  For this reason, and because libcurl was originally designed for ASCII based
operating systems, the current OS/400 implementation uses ASCII as internal
character set. This has been accomplished using the QADRT library and
include files, a C and system procedures ASCII wrapper library. See IBM QADRT
description for more information.
  This then results in libcurl being an ASCII library: any function string
argument is taken/returned in ASCII and a C/C++ calling program built around
QADRT may use libcurl functions as on any other platform.
  QADRT does not define ASCII wrappers for all C/system procedures: the
OS/400 configuration header file and an additional module (os400sys.c) define
some more of them, that are used by libcurl and that QADRT left out.
  To support all the different variants of EBCDIC, non-standard wrapper
procedures have been added to libcurl on OS/400: they provide an additional
CCSID (numeric Coded Character Set ID specific to OS/400) parameter for each
string argument. String values passed to callback procedures are NOT converted,
so text gathered this way is (probably !) ASCII.

  Another OS/400 problem comes from the fact that the last fixed argument of a
vararg procedure may not be of type char, unsigned char, short or unsigned
short. Enums that are internally implemented by the C compiler as one of these
types are also forbidden. Libcurl uses enums as vararg procedure tagfields...
Happily, there is a pragma forcing enums to type "int". The original libcurl
header files are thus altered during build process to use this pragma, in
order to force libcurl enums of being type int (the pragma disposition in use
before inclusion is restored before resuming the including unit compilation).

  Secure socket layer is provided by the IBM GSKit API: unlike other SSL
implementations, GSKit is based on "certificate stores" or keyrings
rather than individual certificate/key files. Certificate stores, as well as
"certificate labels" are managed by external IBM-defined applications.
  There are two ways to specify an SSL context:
- By an application identifier.
- By a keyring file pathname and (optionally) certificate label.
  To identify an SSL context by application identifier, use option
SETOPT_SSLCERT to specify the application identifier.
  To address an SSL context by keyring and certificate label, use CURLOPT_CAINFO
to set-up the keyring pathname, CURLOPT_SSLCERT to define the certificate label
(omitting it will cause the default certificate in keyring to be used) and
CURLOPT_KEYPASSWD to give the keyring password. If SSL is used without
defining any of these options, the default (i.e.: system) keyring is used for
server certificate validation.

  Non-standard EBCDIC wrapper prototypes are defined in an additional header
file: ccsidcurl.h. These should be self-explanatory to an OS/400-aware
designer. CCSID 0 can be used to select the current job's CCSID.
  Wrapper procedures with variable arguments are described below:

_ curl_easy_setopt_ccsid()
  Variable arguments are a string pointer and a CCSID (unsigned int) for
options:
        CURLOPT_ABSTRACT_UNIX_SOCKET
        CURLOPT_CAINFO
        CURLOPT_CAPATH
        CURLOPT_COOKIE
        CURLOPT_COOKIEFILE
        CURLOPT_COOKIEJAR
        CURLOPT_COOKIELIST
        CURLOPT_COPYPOSTFIELDS
        CURLOPT_CRLFILE
        CURLOPT_CUSTOMREQUEST
        CURLOPT_DEFAULT_PROTOCOL
        CURLOPT_DNS_SERVERS
        CURLOPT_EGDSOCKET
        CURLOPT_ENCODING
        CURLOPT_FTPPORT
        CURLOPT_FTP_ACCOUNT
        CURLOPT_FTP_ALTERNATIVE_TO_USER
        CURLOPT_INTERFACE
        CURLOPT_ISSUERCERT
        CURLOPT_KEYPASSWD
        CURLOPT_KRBLEVEL
        CURLOPT_LOGIN_OPTIONS
        CURLOPT_MAIL_AUTH
        CURLOPT_MAIL_FROM
        CURLOPT_NETRC_FILE
        CURLOPT_NOPROXY
        CURLOPT_PASSWORD
        CURLOPT_PINNEDPUBLICKEY
        CURLOPT_PRE_PROXY
        CURLOPT_PROXY
        CURLOPT_PROXYPASSWORD
        CURLOPT_PROXYUSERNAME
        CURLOPT_PROXYUSERPWD
        CURLOPT_PROXY_CAINFO
        CURLOPT_PROXY_CAPATH
        CURLOPT_PROXY_CRLFILE
        CURLOPT_PROXY_KEYPASSWD
        CURLOPT_PROXY_PINNEDPUBLICKEY
        CURLOPT_PROXY_SERVICE_NAME
        CURLOPT_PROXY_SSLCERT
        CURLOPT_PROXY_SSLCERTTYPE
        CURLOPT_PROXY_SSLKEY
        CURLOPT_PROXY_SSLKEYTYPE
        CURLOPT_PROXY_SSL_CIPHER_LIST
        CURLOPT_PROXY_TLSAUTH_PASSWORD
        CURLOPT_PROXY_TLSAUTH_TYPE
        CURLOPT_PROXY_TLSAUTH_USERNAME
        CURLOPT_RANDOM_FILE
        CURLOPT_RANGE
        CURLOPT_REFERER
        CURLOPT_RTSP_SESSION_UID
        CURLOPT_RTSP_STREAM_URI
        CURLOPT_RTSP_TRANSPORT
        CURLOPT_SERVICE_NAME
        CURLOPT_SOCKS5_GSSAPI_SERVICE
        CURLOPT_SSH_HOST_PUBLIC_KEY_MD5
        CURLOPT_SSH_KNOWNHOSTS
        CURLOPT_SSH_PRIVATE_KEYFILE
        CURLOPT_SSH_PUBLIC_KEYFILE
        CURLOPT_SSLCERT
        CURLOPT_SSLCERTTYPE
        CURLOPT_SSLENGINE
        CURLOPT_SSLKEY
        CURLOPT_SSLKEYTYPE
        CURLOPT_SSL_CIPHER_LIST
        CURLOPT_TLSAUTH_PASSWORD
        CURLOPT_TLSAUTH_TYPE
        CURLOPT_TLSAUTH_USERNAME
        CURLOPT_UNIX_SOCKET_PATH
        CURLOPT_URL
        CURLOPT_USERAGENT
        CURLOPT_USERNAME
        CURLOPT_USERPWD
        CURLOPT_XOAUTH2_BEARER
  Else it is the same as for curl_easy_setopt().
  Note that CURLOPT_ERRORBUFFER is not in the list above, since it gives the
address of an (empty) character buffer, not the address of a string.
CURLOPT_POSTFIELDS stores the address of static binary data (of type void *) and
thus is not converted. If CURLOPT_COPYPOSTFIELDS is issued after
CURLOPT_POSTFIELDSIZE != -1, the data size is adjusted according to the
CCSID conversion result length.

_ curl_formadd_ccsid()
  In the variable argument list, string pointers should be followed by a (long)
CCSID for the following options:
        CURLFORM_FILENAME
        CURLFORM_CONTENTTYPE
        CURLFORM_BUFFER
        CURLFORM_FILE
        CURLFORM_FILECONTENT
        CURLFORM_COPYCONTENTS
        CURLFORM_COPYNAME
        CURLFORM_PTRNAME
  If taken from an argument array, an additional array entry must follow each
entry containing one of the above option. This additional entry holds the CCSID
in its value field, and the option field is meaningless.
  It is not possible to have a string pointer and its CCSID across a function
parameter/array boundary.
  Please note that CURLFORM_PTRCONTENTS and CURLFORM_BUFFERPTR are considered
unconvertible strings and thus are NOT followed by a CCSID.

_ curl_easy_getinfo_ccsid()
  The following options are followed by a 'char * *' and a CCSID. Unlike
curl_easy_getinfo(), the value returned in the pointer should be freed after
use:
        CURLINFO_EFFECTIVE_URL
        CURLINFO_CONTENT_TYPE
        CURLINFO_FTP_ENTRY_PATH
        CURLINFO_REDIRECT_URL
        CURLINFO_PRIMARY_IP
        CURLINFO_RTSP_SESSION_ID
        CURLINFO_LOCAL_IP
        CURLINFO_SCHEME
  Likewise, the following options are followed by a struct curl_slist * * and a
CCSID.
        CURLINFO_SSL_ENGINES
        CURLINFO_COOKIELIST
Lists returned should be released with curl_slist_free_all() after use.
  Option CURLINFO_CERTINFO is followed by a struct curl_certinfo * * and a
CCSID. Returned structures sould be free'ed using curl_certinfo_free_all() after
use.
  Other options are processed like in curl_easy_getinfo().

_ curl_pushheader_bynum_cssid() and curl_pushheader_byname_ccsid()
  Although the prototypes are self-explanatory, the returned string pointer
should be freed after use, as opposite to the non-ccsid versions of these
procedures.
  Please note that HTTP2 is not (yet) implemented on OS/400, thus these
functions will always return NULL.


  Standard compilation environment does support neither autotools nor make;
in fact, very few common utilities are available. As a consequence, the
config-os400.h has been coded manually and the compilation scripts are
a set of shell scripts stored in subdirectory packages/OS400.

  The "curl" command and the test environment are currently not supported on
OS/400.


Protocols currently implemented on OS/400:
_ DICT
_ FILE
_ FTP
_ FTPS
_ FTP with secure transmission
_ GOPHER
_ HTTP
_ HTTPS
_ IMAP
_ IMAPS
_ IMAP with secure transmission
_ LDAP
_ POP3
_ POP3S
_ POP3 with secure transmission
_ RTSP
_ SCP if libssh2 is enabled
_ SFTP if libssh2 is enabled
_ SMTP
_ SMTPS
_ SMTP with secure transmission
_ TELNET
_ TFTP



Compiling on OS/400:

  These instructions targets people who knows about OS/400, compiling, IFS and
archive extraction. Do not ask questions about these subjects if you're not
familiar with.

_ As a prerequisite, QADRT development environment must be installed.
_ If data compression has to be supported, ZLIB development environment must
  be installed.
_ Likewise, if SCP and SFTP protocols have to be compiled in, LIBSSH2
  developent environment must be installed.
_ Install the curl source directory in IFS. Do NOT install it in the
  installation target directory (wich defaults to /curl).
_ Enter shell (QSH)
_ Change current directory to the curl installation directory
_ Change current directory to ./packages/OS400
_ Edit file iniscript.sh. You may want to change tunable configuration
  parameters, like debug info generation, optimisation level, listing option,
  target library, ZLIB/LIBSSH2 availability and location, etc.
_ Copy any file in the current directory to makelog (i.e.:
  cp initscript.sh makelog): this is intended to create the makelog file with
  an ASCII CCSID!
_ Enter the command "sh makefile.sh > makelog 2>&1'
_ Examine the makelog file to check for compilation errors.

  Leaving file initscript.sh unchanged, this will produce the following OS/400
objects:
_ Library CURL. All other objects will be stored in this library.
_ Modules for all libcurl units.
_ Binding directory CURL_A, to be used at calling program link time for
  statically binding the modules (specify BNDSRVPGM(QADRTTS QGLDCLNT QGLDBRDR)
  when creating a program using CURL_A).
_ Service program CURL.<soname>, where <soname> is extracted from the
  lib/Makefile.am VERSION variable. To be used at calling program run-time
  when this program has dynamically bound curl at link time.
_ Binding directory CURL. To be used to dynamically bind libcurl when linking a
  calling program.
_ Source file H. It contains all the include members needed to compile a C/C++
  module using libcurl, and an ILE/RPG /copy member for support in this
  language.
_ Standard C/C++ libcurl include members in file H.
_ CCSIDCURL member in file H. This defines the non-standard EBCDIC wrappers for
  C and C++.
_ CURL.INC member in file H. This defines everything needed by an ILE/RPG
  program using libcurl.
_ LIBxxx modules and programs. Although the test environment is not supported
  on OS/400, the libcurl test programs are compiled for manual tests.
_ IFS directory /curl/include/curl containing the C header files for IFS source
  C/C++ compilation and curl.inc.rpgle for IFS source ILE/RPG compilation.



Special programming consideration:

QADRT being used, the following points must be considered:
_ If static binding is used, service program QADRTTS must be linked too.
_ The EBCDIC CCSID used by QADRT is 37 by default, NOT THE JOB'S CCSID. If
  another EBCDIC CCSID is required, it must be set via a locale through a call
  to setlocale_a (QADRT's setlocale() ASCII wrapper) with category LC_ALL or
  LC_CTYPE, or by setting environment variable QADRT_ENV_LOCALE to the locale
  object path before executing the program.
_ Do not use original source include files unless you know what you are doing.
  Use the installed members instead (in /QSYS.LIB/CURL.LIB/H.FILE and
  /curl/include/curl).



ILE/RPG support:

  Since 95% of the OS/400 programmers use ILE/RPG exclusively, a definition
  /INCLUDE member is provided for this language. To include all libcurl
  definitions in an ILE/RPG module, line

     h bnddir('CURL/CURL')

must figure in the program header, and line

     d/include curl/h,curl.inc

in the global data section of the module's source code.

  No vararg procedure support exists in ILE/RPG: for this reason, the following
considerations apply:
_ Procedures curl_easy_setopt_long(), curl_easy_setopt_object(),
  curl_easy_setopt_function() and curl_easy_setopt_offset() are all alias
  prototypes to curl_easy_setopt(), but with different parameter lists.
_ Procedures curl_easy_getinfo_string(), curl_easy_getinfo_long(),
  curl_easy_getinfo_double() and curl_easy_getinfo_slist() are all alias
  prototypes to curl_easy_getinfo(), but with different parameter lists.
_ Procedures curl_multi_setopt_long(), curl_multi_setopt_object(),
  curl_multi_setopt_function() and curl_multi_setopt_offset() are all alias
  prototypes to curl_multi_setopt(), but with different parameter lists.
_ The prototype of procedure curl_formadd() allows specifying a pointer option
  and the CURLFORM_END option. This makes possible to use an option array
  without any additional definition. If some specific incompatible argument
  list is used in the ILE/RPG program, the latter must define a specialised
  alias. The same applies to curl_formadd_ccsid() too.

  Since RPG cannot cast a long to a pointer, procedure curl_form_long_value()
is provided for that purpose: this allows storing a long value in the curl_forms
array.
EPM is a free Unix software/file packaging program that generates distribution
archives from a list of files. EPM Can:

 * Generate portable script-based distribution packages complete with
   installation and removal scripts.
 * Generate vendor distributions in AIX, BSD, Compaq Tru64, Debian, HP-UX,
   IRIX, Red Hat, and Solaris formats.
 * Provide a complete, cross-platform software distribution solution for your
   applications.

http://www.easysw.com/epm/

                             _   _ ____  _
                         ___| | | |  _ \| |
                        / __| | | | |_) | |
                       ( (__| |_| |  _ <| |___
                        \___|\___/|_| \_\_____|
                            for AIX Toolbox

Author: Tor Arntsen

The spec file in this directory is based on the Linux ssl and non-ssl
curl spec files, plus additions to make it AIX Toolbox compatible.

The AIX Toolbox setup (installs into /opt/freeware, with symlinks in
/usr/bin,/usr/lib,/usr/include) are based on IBM's aixtoolbox spec
file written by David Clissold <cliss@austin.ibm.com>, see

ftp://ftp.software.ibm.com/aixtoolbox/SPECS/curl-7.9.3-2.spec

This spec file is designed to be a drop-in replacement for the
old spec file found at the above link. Thus, like the old spec file
this version is also a unified ssl/non-ssl  version. To get non-ssl
RPMs just pass --define 'nossl 1' to the command line when building
the RPM, e.g.

rpm -bb --define 'nossl 1' curl.spec

Default is to build with ssl support.

Lastly, the spec file expects the Curl source distribution file to be
in .tar.bz2 format.

The nifty curl header of this README is a ripoff of the vms/readme file.

Curl is a tool for transferring files with URL syntax, supporting
  FTP, FTPS, HTTP, HTTPS, TELNET, DICT, FILE and LDAP.
  Curl supports HTTPS certificates, HTTP POST, HTTP PUT,
  FTP uploading, kerberos, HTTP form based upload, proxies,
  cookies, user+password authentication, file transfer resume,
  http proxy tunneling and a busload of other useful tricks.

See /usr/doc/curl-$(VERSION)/FEATURES for more info.


Dependencies:
  - Cygwin
  - OpenSSL 0.9.6b-2+ (*)

  (*) curl can be built without SSL support, see below for details


Canonical Homepage and Downloads:
  https://curl.haxx.se/
  https://curl.haxx.se/download.html


Cygwin specific source files (a .README template and a Makefile
  for building binary tarballs) are maintained in the upstream
  CVS at: <srctop>/packages/Win32/cygwin/


Build Instructions (to recompile from the cygwin source tarball):
  ---STANDARD (with SSL) RELEASE---
  Download the source (either the official release or the cygwin version),
  unpack it (done for you if using setup.exe), then:

  $ ./configure --prefix=/usr --mandir=/usr/share/man  # (*)
  $ make
  $ make test    # optional
  $ make install # (**)

  (*) The Cygwin project now (as of sometime in 2003) prefers man pages
      within /usr/share/man, as opposed to the default /usr/man.

  (**) LibTool 1.4.2 had a bug related to cygwin's use of ".exe" extensions,
      such that "make install" blew up at curl.exe. See this URL for details:
         https://lists.gnu.org/archive/html/libtool/2001-09/msg00101.html
      The copy of ltmain.sh that is distributed with curl includes this patch.

  As of curl 7.9.1, the official source compiles (under Cygwin) and tests
    100% cleanly OOTB (Out Of The Box)

  ---NO SSL RELEASE---
  Same as standard, except for the configure step, which changes to:

  $ ./configure --prefix=/usr --mandir=/usr/share/man --without-ssl

  NOTE: the standard release is what is available via Cygwin's setup.exe;
    the no-ssl release is only available from the curl website


Packaging Instructions:
  ---BINARY---
  Compile cleanly as described above, then:

  $ make cygwinbin CYGBUILD=n

  where n is the cygwin release number (e.g. the "1" in curl-7.9-1),
  and "CYGBUILD=n" is optional (n defaults to 1 if not specified)

  Assuming everything worked, you'll find your binary tarballs in
   $(buildtop)/packages/Win32/cygwin/

  ---SOURCE---
  1. download & unpack the pristine source
  2. rename the source dir to add the "-$(REL)" suffix, e.g.:
     $ mv curl-7.9 curl-7.9-1
  3. unpack the pristine source once more, so you'll end up
     with 2 directories: "curl-7.9" and "curl-7.9-1" in this example
  3. add a CYGWIN-PATCHES directory, and add this readme to it
     $ cd curl-7.9-1; mkdir CYGWIN-PATCHES
     $ cp packages/Win32/cygwin/README CYGWIN-PATCHES/curl-7.9-1.README
  4. if applicable, document any changes in the README file
  5. create a patch which, when applied
     (using `patch -p1 < curl-7.9-$(REL).patch`)
     will remove any changes you've made to the pristine source:
     $ cd ..
     $ diff -Nrup curl-7.9-1 curl-7.9 > curl-7.9-1.patch
     and then move it into the CYGWIN-PATCHES directory
     $ mv curl-7.9-1.patch curl-7.9-1/CYGWIN-PATCHES
  6. pack the new source dir into a tar.bz2 file:
     $ tar cfj curl-7.9-1-src.tar.bz2 curl-7.9-1

  ---SETUP.HINT---
  @ curl
  sdesc: "a client that groks URLs"
  ldesc: "Curl is a tool for transferring files with URL syntax,
  supporting FTP, FTPS, HTTP, HTTPS, TELNET, DICT, FILE
  and LDAP. Curl supports HTTPS certificates, HTTP POST, HTTP PUT,
  FTP uploading, kerberos, HTTP form based upload, proxies,
  cookies, user+password authentication, file transfer resume,
  http proxy tunneling and a busload of other useful tricks."
  category: Web Libs
  requires: cygwin openssl

  @ curl-devel
  sdesc: "(lib)curl headers, static libraries, developer docs and samples"
  ldesc: "curl-devel is the developer-oriented (non-run-time) parts
  of the curl package. It includes header files, static libraries,
  example source code snippets, and the libcurl man pages."
  category: Web Libs Devel
  requires: cygwin openssl curl


Cygwin port maintained by:
  Kevin Roth <kproth @ users . sourceforge . net>
  Questions about curl should be directed to curl-users@cool.haxx.se.
  Questions about this cygwin package go to cygwin@cygwin.com.
Author: Daniel (I'm not trustworthy, replace this!)

Paul Marquis's 'make_curl_rpm' script is a fine example on how to automate the
jobs. You need to fill in your own name and email at least.

Gisle Vanem made curl build fine on DOS (and MingW) with djgpp, OpenSSL and his
Watt-32 stack.

'make djgpp' in the root curl dir should build it fine.

Note 1: djgpp 2.04 beta has a sscanf() bug so the URL parsing isn't
        done proberly. Use djgpp 2.03 until they fix it.

Note 2: Compile Watt-32 (and OpenSSL) with the same version of djgpp.
        Otherwise things go wrong because things like FS-extensions and
        errnos have been changed between releases.
  ENGINE
  ======

  With OpenSSL 0.9.6, a new component was added to support alternative
  cryptography implementations, most commonly for interfacing with external
  crypto devices (eg. accelerator cards). This component is called ENGINE,
  and its presence in OpenSSL 0.9.6 (and subsequent bug-fix releases)
  caused a little confusion as 0.9.6** releases were rolled in two
  versions, a "standard" and an "engine" version. In development for 0.9.7,
  the ENGINE code has been merged into the main branch and will be present
  in the standard releases from 0.9.7 forwards.

  There are currently built-in ENGINE implementations for the following
  crypto devices:

      o Microsoft CryptoAPI
      o VIA Padlock
      o nCipher CHIL

  In addition, dynamic binding to external ENGINE implementations is now
  provided by a special ENGINE called "dynamic". See the "DYNAMIC ENGINE"
  section below for details.

  At this stage, a number of things are still needed and are being worked on:

      1 Integration of EVP support.
      2 Configuration support.
      3 Documentation!

1 With respect to EVP, this relates to support for ciphers and digests in
  the ENGINE model so that alternative implementations of existing
  algorithms/modes (or previously unimplemented ones) can be provided by
  ENGINE implementations.

2 Configuration support currently exists in the ENGINE API itself, in the
  form of "control commands". These allow an application to expose to the
  user/admin the set of commands and parameter types a given ENGINE
  implementation supports, and for an application to directly feed string
  based input to those ENGINEs, in the form of name-value pairs. This is an
  extensible way for ENGINEs to define their own "configuration" mechanisms
  that are specific to a given ENGINE (eg. for a particular hardware
  device) but that should be consistent across *all* OpenSSL-based
  applications when they use that ENGINE. Work is in progress (or at least
  in planning) for supporting these control commands from the CONF (or
  NCONF) code so that applications using OpenSSL's existing configuration
  file format can have ENGINE settings specified in much the same way.
  Presently however, applications must use the ENGINE API itself to provide
  such functionality. To see first hand the types of commands available
  with the various compiled-in ENGINEs (see further down for dynamic
  ENGINEs), use the "engine" openssl utility with full verbosity, ie;
       openssl engine -vvvv

3 Documentation? Volunteers welcome! The source code is reasonably well
  self-documenting, but some summaries and usage instructions are needed -
  moreover, they are needed in the same POD format the existing OpenSSL
  documentation is provided in. Any complete or incomplete contributions
  would help make this happen.

  STABILITY & BUG-REPORTS
  =======================

  What already exists is fairly stable as far as it has been tested, but
  the test base has been a bit small most of the time. For the most part,
  the vendors of the devices these ENGINEs support have contributed to the
  development and/or testing of the implementations, and *usually* (with no
  guarantees) have experience in using the ENGINE support to drive their
  devices from common OpenSSL-based applications. Bugs and/or inexplicable
  behaviour in using a specific ENGINE implementation should be sent to the
  author of that implementation (if it is mentioned in the corresponding C
  file), and in the case of implementations for commercial hardware
  devices, also through whatever vendor support channels are available.  If
  none of this is possible, or the problem seems to be something about the
  ENGINE API itself (ie. not necessarily specific to a particular ENGINE
  implementation) then you should mail complete details to the relevant
  OpenSSL mailing list. For a definition of "complete details", refer to
  the OpenSSL "README" file. As for which list to send it to;

     openssl-users: if you are *using* the ENGINE abstraction, either in an
          pre-compiled application or in your own application code.

     openssl-dev: if you are discussing problems with OpenSSL source code.

  USAGE
  =====

  The default "openssl" ENGINE is always chosen when performing crypto
  operations unless you specify otherwise. You must actively tell the
  openssl utility commands to use anything else through a new command line
  switch called "-engine". Also, if you want to use the ENGINE support in
  your own code to do something similar, you must likewise explicitly
  select the ENGINE implementation you want.

  Depending on the type of hardware, system, and configuration, "settings"
  may need to be applied to an ENGINE for it to function as expected/hoped.
  The recommended way of doing this is for the application to support
  ENGINE "control commands" so that each ENGINE implementation can provide
  whatever configuration primitives it might require and the application
  can allow the user/admin (and thus the hardware vendor's support desk
  also) to provide any such input directly to the ENGINE implementation.
  This way, applications do not need to know anything specific to any
  device, they only need to provide the means to carry such user/admin
  input through to the ENGINE in question. Ie. this connects *you* (and
  your helpdesk) to the specific ENGINE implementation (and device), and
  allows application authors to not get buried in hassle supporting
  arbitrary devices they know (and care) nothing about.

  A new "openssl" utility, "openssl engine", has been added in that allows
  for testing and examination of ENGINE implementations. Basic usage
  instructions are available by specifying the "-?" command line switch.

  DYNAMIC ENGINES
  ===============

  The new "dynamic" ENGINE provides a low-overhead way to support ENGINE
  implementations that aren't pre-compiled and linked into OpenSSL-based
  applications. This could be because existing compiled-in implementations
  have known problems and you wish to use a newer version with an existing
  application. It could equally be because the application (or OpenSSL
  library) you are using simply doesn't have support for the ENGINE you
  wish to use, and the ENGINE provider (eg. hardware vendor) is providing
  you with a self-contained implementation in the form of a shared-library.
  The other use-case for "dynamic" is with applications that wish to
  maintain the smallest foot-print possible and so do not link in various
  ENGINE implementations from OpenSSL, but instead leaves you to provide
  them, if you want them, in the form of "dynamic"-loadable
  shared-libraries. It should be possible for hardware vendors to provide
  their own shared-libraries to support arbitrary hardware to work with
  applications based on OpenSSL 0.9.7 or later. If you're using an
  application based on 0.9.7 (or later) and the support you desire is only
  announced for versions later than the one you need, ask the vendor to
  backport their ENGINE to the version you need.

  How does "dynamic" work?
  ------------------------
    The dynamic ENGINE has a special flag in its implementation such that
    every time application code asks for the 'dynamic' ENGINE, it in fact
    gets its own copy of it. As such, multi-threaded code (or code that
    multiplexes multiple uses of 'dynamic' in a single application in any
    way at all) does not get confused by 'dynamic' being used to do many
    independent things. Other ENGINEs typically don't do this so there is
    only ever 1 ENGINE structure of its type (and reference counts are used
    to keep order). The dynamic ENGINE itself provides absolutely no
    cryptographic functionality, and any attempt to "initialise" the ENGINE
    automatically fails. All it does provide are a few "control commands"
    that can be used to control how it will load an external ENGINE
    implementation from a shared-library. To see these control commands,
    use the command-line;

       openssl engine -vvvv dynamic

    The "SO_PATH" control command should be used to identify the
    shared-library that contains the ENGINE implementation, and "NO_VCHECK"
    might possibly be useful if there is a minor version conflict and you
    (or a vendor helpdesk) is convinced you can safely ignore it.
    "ID" is probably only needed if a shared-library implements
    multiple ENGINEs, but if you know the engine id you expect to be using,
    it doesn't hurt to specify it (and this provides a sanity check if
    nothing else). "LIST_ADD" is only required if you actually wish the
    loaded ENGINE to be discoverable by application code later on using the
    ENGINE's "id". For most applications, this isn't necessary - but some
    application authors may have nifty reasons for using it. The "LOAD"
    command is the only one that takes no parameters and is the command
    that uses the settings from any previous commands to actually *load*
    the shared-library ENGINE implementation. If this command succeeds, the
    (copy of the) 'dynamic' ENGINE will magically morph into the ENGINE
    that has been loaded from the shared-library. As such, any control
    commands supported by the loaded ENGINE could then be executed as per
    normal. Eg. if ENGINE "foo" is implemented in the shared-library
    "libfoo.so" and it supports some special control command "CMD_FOO", the
    following code would load and use it (NB: obviously this code has no
    error checking);

       ENGINE *e = ENGINE_by_id("dynamic");
       ENGINE_ctrl_cmd_string(e, "SO_PATH", "/lib/libfoo.so", 0);
       ENGINE_ctrl_cmd_string(e, "ID", "foo", 0);
       ENGINE_ctrl_cmd_string(e, "LOAD", NULL, 0);
       ENGINE_ctrl_cmd_string(e, "CMD_FOO", "some input data", 0);

    For testing, the "openssl engine" utility can be useful for this sort
    of thing. For example the above code excerpt would achieve much the
    same result as;

       openssl engine dynamic \
                 -pre SO_PATH:/lib/libfoo.so \
                 -pre ID:foo \
                 -pre LOAD \
                 -pre "CMD_FOO:some input data"

    Or to simply see the list of commands supported by the "foo" ENGINE;

       openssl engine -vvvv dynamic \
                 -pre SO_PATH:/lib/libfoo.so \
                 -pre ID:foo \
                 -pre LOAD

    Applications that support the ENGINE API and more specifically, the
    "control commands" mechanism, will provide some way for you to pass
    such commands through to ENGINEs. As such, you would select "dynamic"
    as the ENGINE to use, and the parameters/commands you pass would
    control the *actual* ENGINE used. Each command is actually a name-value
    pair and the value can sometimes be omitted (eg. the "LOAD" command).
    Whilst the syntax demonstrated in "openssl engine" uses a colon to
    separate the command name from the value, applications may provide
    their own syntax for making that separation (eg. a win32 registry
    key-value pair may be used by some applications). The reason for the
    "-pre" syntax in the "openssl engine" utility is that some commands
    might be issued to an ENGINE *after* it has been initialised for use.
    Eg. if an ENGINE implementation requires a smart-card to be inserted
    during initialisation (or a PIN to be typed, or whatever), there may be
    a control command you can issue afterwards to "forget" the smart-card
    so that additional initialisation is no longer possible. In
    applications such as web-servers, where potentially volatile code may
    run on the same host system, this may provide some arguable security
    value. In such a case, the command would be passed to the ENGINE after
    it has been initialised for use, and so the "-post" switch would be
    used instead. Applications may provide a different syntax for
    supporting this distinction, and some may simply not provide it at all
    ("-pre" is almost always what you're after, in reality).

  How do I build a "dynamic" ENGINE?
  ----------------------------------
    This question is trickier - currently OpenSSL bundles various ENGINE
    implementations that are statically built in, and any application that
    calls the "ENGINE_load_builtin_engines()" function will automatically
    have all such ENGINEs available (and occupying memory). Applications
    that don't call that function have no ENGINEs available like that and
    would have to use "dynamic" to load any such ENGINE - but on the other
    hand such applications would only have the memory footprint of any
    ENGINEs explicitly loaded using user/admin provided control commands.
    The main advantage of not statically linking ENGINEs and only using
    "dynamic" for hardware support is that any installation using no
    "external" ENGINE suffers no unnecessary memory footprint from unused
    ENGINEs. Likewise, installations that do require an ENGINE incur the
    overheads from only *that* ENGINE once it has been loaded.

    Sounds good? Maybe, but currently building an ENGINE implementation as
    a shared-library that can be loaded by "dynamic" isn't automated in
    OpenSSL's build process. It can be done manually quite easily however.
    Such a shared-library can either be built with any OpenSSL code it
    needs statically linked in, or it can link dynamically against OpenSSL
    if OpenSSL itself is built as a shared library. The instructions are
    the same in each case, but in the former (statically linked any
    dependencies on OpenSSL) you must ensure OpenSSL is built with
    position-independent code ("PIC"). The default OpenSSL compilation may
    already specify the relevant flags to do this, but you should consult
    with your compiler documentation if you are in any doubt.

    This example will show building the "atalla" ENGINE in the
    crypto/engine/ directory as a shared-library for use via the "dynamic"
    ENGINE.
    1) "cd" to the crypto/engine/ directory of a pre-compiled OpenSSL
       source tree.
    2) Recompile at least one source file so you can see all the compiler
       flags (and syntax) being used to build normally. Eg;
           touch hw_atalla.c ; make
       will rebuild "hw_atalla.o" using all such flags.
    3) Manually enter the same compilation line to compile the
       "hw_atalla.c" file but with the following two changes;
         (a) add "-DENGINE_DYNAMIC_SUPPORT" to the command line switches,
	 (b) change the output file from "hw_atalla.o" to something new,
             eg. "tmp_atalla.o"
    4) Link "tmp_atalla.o" into a shared-library using the top-level
       OpenSSL libraries to resolve any dependencies. The syntax for doing
       this depends heavily on your system/compiler and is a nightmare
       known well to anyone who has worked with shared-library portability
       before. 'gcc' on Linux, for example, would use the following syntax;
          gcc -shared -o dyn_atalla.so tmp_atalla.o -L../.. -lcrypto
    5) Test your shared library using "openssl engine" as explained in the
       previous section. Eg. from the top-level directory, you might try;
          apps/openssl engine -vvvv dynamic \
              -pre SO_PATH:./crypto/engine/dyn_atalla.so -pre LOAD
       If the shared-library loads successfully, you will see both "-pre"
       commands marked as "SUCCESS" and the list of control commands
       displayed (because of "-vvvv") will be the control commands for the
       *atalla* ENGINE (ie. *not* the 'dynamic' ENGINE). You can also add
       the "-t" switch to the utility if you want it to try and initialise
       the atalla ENGINE for use to test any possible hardware/driver
       issues.

  PROBLEMS
  ========

  It seems like the ENGINE part doesn't work too well with CryptoSwift on Win32.
  A quick test done right before the release showed that trying "openssl speed
  -engine cswift" generated errors. If the DSO gets enabled, an attempt is made
  to write at memory address 0x00000002.


 OpenSSL 1.1.1a 20 Nov 2018

 Copyright (c) 1998-2018 The OpenSSL Project
 Copyright (c) 1995-1998 Eric A. Young, Tim J. Hudson
 All rights reserved.

 DESCRIPTION
 -----------

 The OpenSSL Project is a collaborative effort to develop a robust,
 commercial-grade, fully featured, and Open Source toolkit implementing the
 Transport Layer Security (TLS) protocols (including SSLv3) as well as a
 full-strength general purpose cryptographic library.

 OpenSSL is descended from the SSLeay library developed by Eric A. Young
 and Tim J. Hudson.  The OpenSSL toolkit is licensed under a dual-license (the
 OpenSSL license plus the SSLeay license), which means that you are free to
 get and use it for commercial and non-commercial purposes as long as you
 fulfill the conditions of both licenses.

 OVERVIEW
 --------

 The OpenSSL toolkit includes:

 libssl (with platform specific naming):
     Provides the client and server-side implementations for SSLv3 and TLS.

 libcrypto (with platform specific naming):
     Provides general cryptographic and X.509 support needed by SSL/TLS but
     not logically part of it.

 openssl:
     A command line tool that can be used for:
        Creation of key parameters
        Creation of X.509 certificates, CSRs and CRLs
        Calculation of message digests
        Encryption and decryption
        SSL/TLS client and server tests
        Handling of S/MIME signed or encrypted mail
        And more...

 INSTALLATION
 ------------

 See the appropriate file:
        INSTALL         Linux, Unix, Windows, OpenVMS, ...
        NOTES.*         INSTALL addendums for different platforms

 SUPPORT
 -------

 See the OpenSSL website www.openssl.org for details on how to obtain
 commercial technical support. Free community support is available through the
 openssl-users email list (see
 https://www.openssl.org/community/mailinglists.html for further details).

 If you have any problems with OpenSSL then please take the following steps
 first:

    - Download the latest version from the repository
      to see if the problem has already been addressed
    - Configure with no-asm
    - Remove compiler optimization flags

 If you wish to report a bug then please include the following information
 and create an issue on GitHub:

    - OpenSSL version: output of 'openssl version -a'
    - Configuration data: output of 'perl configdata.pm --dump'
    - OS Name, Version, Hardware platform
    - Compiler Details (name, version)
    - Application Details (name, version)
    - Problem Description (steps that will reproduce the problem, if known)
    - Stack Traceback (if the application dumps core)

 Just because something doesn't work the way you expect does not mean it
 is necessarily a bug in OpenSSL. Use the openssl-users email list for this type
 of query.

 HOW TO CONTRIBUTE TO OpenSSL
 ----------------------------

 See CONTRIBUTING

 LEGALITIES
 ----------

 A number of nations restrict the use or export of cryptography. If you
 are potentially subject to such restrictions you should seek competent
 professional legal advice before attempting to develop or distribute
 cryptographic code.
This release does not support a FIPS 140-2 validated module.

Text::Template v1.46

This is a library for generating form letters, building HTML pages, or
filling in templates generally.  A `template' is a piece of text that
has little Perl programs embedded in it here and there.  When you
`fill in' a template, you evaluate the little programs and replace
them with their values.  

Here's an example of a template:

	Dear {$title} {$lastname},

	It has come to our attention that you are delinquent in your
	{$monthname[$last_paid_month]} payment.  Please remit
	${sprintf("%.2f", $amount)} immediately, or your patellae may
	be needlessly endangered.

			Love,

			Mark "{nickname(rand 20)}" Dominus


The result of filling in this template is a string, which might look
something like this:

	Dear Mr. Gates,

	It has come to our attention that you are delinquent in your
	February payment.  Please remit
	$392.12 immediately, or your patellae may
	be needlessly endangered.


			Love,

			Mark "Vizopteryx" Dominus

You can store a template in a file outside your program.  People can
modify the template without modifying the program.  You can separate
the formatting details from the main code, and put the formatting
parts of the program into the template.  That prevents code bloat and
encourages functional separation.

You can fill in the template in a `Safe' compartment.  This means that
if you don't trust the person who wrote the code in the template, you
won't have to worry that they are tampering with your program when you
execute it.  

----------------------------------------------------------------

Text::Template was originally released some time in late 1995 or early
1996.  After three years of study and investigation, I rewrote it from
scratch in January 1999.  The new version, 1.0, was much faster,
delivered better functionality and was almost 100% backward-compatible
with the previous beta versions.

I have added a number of useful features and conveniences since the
1.0 release, while still retaining backward compatibility.  With one
merely cosmetic change, the current version of Text::Template passes
the test suite that the old beta versions passed.

Questions or comments should be addressed to
mjd-perl-template+@plover.com.  This address goes directly to me, and
not to anyone else; it is not a mailing list address.

To receive occasional announcements of new versions of T::T, send an
empty note to mjd-perl-template-request@plover.com.  This mailing list
is not for discussion; it is for announcements only.  Therefore, there
is no address for sending messages to the list.

You can get the most recent version of Text::Template, news, comments,
and other collateral information from
<URL:http://www.plover.com/~mjd/perl/Template/>.

----------------------------------------------------------------

What's new in v1.46 since v1.44:

        Thanks to Rik Signes, there is a new
        Text::Template->append_text_to_output method, which
        Text::Template always uses whenever it wants to emit output.
        You can subclass this to get control over the output, for
        example for postprocessing.

        A spurious warning is no longer emitted when the TYPE
        parameter to ->new is omitted.

----------------------------------------------------------------
What's new in v1.44 since v1.43: 

This is a maintentance release.  There are no feature changes.

        _scrubpkg, which was responsible for eptying out temporary
        packages after the module had done with them, wasn't always
        working; the result was memory-leaks in long-running
        applications.  This should be fixed now, and there is a test
        in the test suite for it.

        Minor changes to the test suite to prevent spurious errors.

        Minor documentation changes.

----------------------------------------------------------------
What's new in v1.43 since v1.42:

        The ->new method now fails immediately and sets
        $Text::Template::ERROR if the file that is named by a filename
        argument does not exist or cannot be opened for some other
        reason.  Formerly, the constructor would succeed and the
        ->fill_in call would fail.

----------------------------------------------------------------

What's new in v1.42 since v1.41:

This is a maintentance release.  There are no feature changes.

        Fixed a bug relating to use of UNTAINT under perl 5.005_03 and
        possibly other versions.

        Taint-related tests are now more comprehensive.
----------------------------------------------------------------

What's new in v1.41 since v1.40:

This is a maintentance release.  There are no feature changes.

        Tests now work correctly on Windows systems and possibly on
        other non-unix systems.

----------------------------------------------------------------

What's new in v1.40 since v1.31:

        New UNTAINT option tells the module that it is safe to 'eval'
        code even though it has come from a file or filehandle.

        Code added to prevent memory leaks when filling many
        templates.  Thanks to Itamar Almeida de Carvalho.

        Bug fix:  $OUT was not correctly initialized when used in
        conjunction with SAFE.

        You may now use a glob ref when passing a filehandle to the
        ->new funcion.  Formerly, a glob was reuqired.

        New subclass:  Text::Template::Preprocess.  Just like
        Text::Template, but you may supply a PREPROCESS option in the
        constructor or the fill_in call; this is a function which
        receives each code fragment prior to evaluation, and which may
        modify and return the fragment; the modified fragment is what
        is evaluated.

        Error messages passed to BROKEN subroutines will now report
        the correct line number of the template at which the error
        occurred:

                Illegal division by zero at template line 37.

        If the template comes from a file, the filename will be
        reported as well:

                Illegal division by zero at catalog.tmpl line 37.


        INCOMPATIBLE CHANGE:

        The format of the default error message has changed.  It used
        to look like:

                Program fragment at line 30 delivered error ``Illegal division by zero''

        It now looks like:

                Program fragment delivered error ``Illegal division by zero at catalog.tmpl line 37''

        Note that the default message used to report the line number
        at which the program fragment began; it now reports the line
        number at which the error actually occurred.

----------------------------------------------------------------
What's new in v1.31 since v1.23:

	Just bug fixes---fill_in_string was failing.  Thanks to 
        Donald L. Greer Jr. for the test case.

----------------------------------------------------------------
What's new in v1.23 since v1.22:

	Small bug fix:  DELIMITER and other arguments were being
	ignored in calls to fill_in_file and fill_this_in.  (Thanks to
	Jonathan Roy for reporting this.)

----------------------------------------------------------------
What's new in v1.22 since v1.20:

	You can now specify that certain Perl statements be prepended
	to the beginning of every program fragment in a template,
	either per template, or for all templates, or for the duration
	of only one call to fill_in.  This is useful, for example, if
	you want to enable `strict' checks in your templates but you
	don't want to manually add `use strict' to the front of every
	program fragment everywhere.

----------------------------------------------------------------
What's new in v1.20 since v1.12:

	You can now specify that the program fragment delimiters are
	strings other than { and }.  This has three interesting
	effects: First, it changes the delimiter strings.  Second, it
	disables the special meaning of \, so you have to be really,
	really sure that the delimiters will not appear in your
	templates.  And third, because of the simplifications
	introduced by the elimination of \ processing, template
	parsing is 20-25% faster.

	See the manual section on `Alternative Delimiters'.

	Fixed bug having to do with undefined values in HASH options.
	In particular, Text::Template no longer generates a warning if
	you try to give a variable an undefined value.

----------------------------------------------------------------

What's new in v1.12 since v1.11:

	I forgot to say that Text::Template ISA Exporter, so the
	exported functions never got exported.  Duhhh!

	Template TYPEs are now case-insensitive.  The `new' method now
	diagnoses attempts to use an invalid TYPE.

	More tests for these things.

----------------------------------------------------------------

What's new in v1.11 since v1.10:

	Fixed a bug in the way backslashes were processed.  The 1.10
	behavior was incompatible with the beta versions and was also
	inconvenient.  (`\n' in templates was replaced with `n' before
	it was given to Perl for evaluation.)  The new behavior is
	also incompatible with the beta versions, but it is only a
	little bit incompatible, and it is probbaly better.

	Documentation for the new behavior, and tests for the bug.

----------------------------------------------------------------

What's new in v1.10 since v1.03:

	New OUTPUT option delivers template results directly to a
	filehandle instead of making them into a string.  Saves space
	and time. 

	PACKAGE and HASH now work intelligently with SAFE.

	Fragments may now output data directly to the template, rather
	than having to arrange to return it as a return value at the
	end.  This means that where you used to have to write this:

			{ my $blist = '';
		          foreach $i (@items) {
		            $blist .= qq{  * $i\n};
		          }    
		          $blist;
		        } 

	You can now write this instead, because $OUT is special.

			{ foreach $i (@items) {
		            $OUT.= "  * $i\n";
		          }    
		        } 

	(`A spoonful of sugar makes the medicine go down.')

	Fixed some small bugs.  Worked around a bug in Perl that does
	the wrong thing with $x = <Y> when $x contains a glob.

	More documentation.  Errors fixed.

	Lots more tests.  

----------------------------------------------------------------

What's new in v1.03 since v1.0:

	Code added to support HASH option to fill_in.
	(Incl. `_gensym' function.)
	
	Documentation for HASH.
	
	New test file for HASH.
	
	Note about failure of lexical variables to propagate into
 	templates.  Why does this surprise people?
	
	Bug fix: program fragments are evaluated in an environment with
 	`no strict' by default.  Otherwise, you get a lot of `Global
 	symbol "$v" requires explicit package name' failures.  Why didn't
 	the test program pick this up?  Because the only variable the test
 	program ever used was `$a', which is exempt.  Duhhhhh.
	
	Fixed the test program.
	
	Various minor documentation fixes.



----------------------------------------------------------------

Improvements of 1.0 over the old 0.1beta:

New features:

      At least twice as fast 

      Better support for filling out the same template more than once 

      Now supports evaluation of program fragments in Safe
      compartments. (Thanks, Jonathan!)  

      Better argument syntax 

      More convenience functions 

      The parser is much better and simpler. 

      Once a template is parsed, the parsed version is stored so that
      it needn't be parsed again.  

      BROKEN function behavior is rationalized. You can now pass an
      arbitrary argument to your BROKEN function, or return a value
      from it to the main program.  

      Documentation overhauled. 

objects.txt syntax
------------------

To cover all the naming hacks that were previously in objects.h needed some
kind of hacks in objects.txt.

The basic syntax for adding an object is as follows:

	1 2 3 4		: shortName	: Long Name

		If Long Name contains only word characters and hyphen-minus
		(0x2D) or full stop (0x2E) then Long Name is used as basis
		for the base name in C. Otherwise, the shortName is used.

		The base name (let's call it 'base') will then be used to
		create the C macros SN_base, LN_base, NID_base and OBJ_base.

		Note that if the base name contains spaces, dashes or periods,
		those will be converted to underscore.

Then there are some extra commands:

	!Alias foo 1 2 3 4

		This just makes a name foo for an OID.  The C macro
		OBJ_foo will be created as a result.

	!Cname foo

		This makes sure that the name foo will be used as base name
		in C.

	!module foo
	1 2 3 4		: shortName	: Long Name
	!global

		The !module command was meant to define a kind of modularity.
		What it does is to make sure the module name is prepended
		to the base name.  !global turns this off.  This construction
		is not recursive.

Lines starting with # are treated as comments, as well as any line starting
with ! and not matching the commands above.

Notes: 2001-09-24
-----------------

This "description" (if one chooses to call it that) needed some major updating
so here goes. This update addresses a change being made at the same time to
OpenSSL, and it pretty much completely restructures the underlying mechanics of
the "ENGINE" code. So it serves a double purpose of being a "ENGINE internals
for masochists" document *and* a rather extensive commit log message. (I'd get
lynched for sticking all this in CHANGES or the commit mails :-).

ENGINE_TABLE underlies this restructuring, as described in the internal header
"eng_int.h", implemented in eng_table.c, and used in each of the "class" files;
tb_rsa.c, tb_dsa.c, etc.

However, "EVP_CIPHER" underlies the motivation and design of ENGINE_TABLE so
I'll mention a bit about that first. EVP_CIPHER (and most of this applies
equally to EVP_MD for digests) is both a "method" and a algorithm/mode
identifier that, in the current API, "lingers". These cipher description +
implementation structures can be defined or obtained directly by applications,
or can be loaded "en masse" into EVP storage so that they can be catalogued and
searched in various ways, ie. two ways of encrypting with the "des_cbc"
algorithm/mode pair are;

(i) directly;
     const EVP_CIPHER *cipher = EVP_des_cbc();
     EVP_EncryptInit(&ctx, cipher, key, iv);
     [ ... use EVP_EncryptUpdate() and EVP_EncryptFinal() ...]

(ii) indirectly; 
     OpenSSL_add_all_ciphers();
     cipher = EVP_get_cipherbyname("des_cbc");
     EVP_EncryptInit(&ctx, cipher, key, iv);
     [ ... etc ... ]

The latter is more generally used because it also allows ciphers/digests to be
looked up based on other identifiers which can be useful for automatic cipher
selection, eg. in SSL/TLS, or by user-controllable configuration.

The important point about this is that EVP_CIPHER definitions and structures are
passed around with impunity and there is no safe way, without requiring massive
rewrites of many applications, to assume that EVP_CIPHERs can be reference
counted. One an EVP_CIPHER is exposed to the caller, neither it nor anything it
comes from can "safely" be destroyed. Unless of course the way of getting to
such ciphers is via entirely distinct API calls that didn't exist before.
However existing API usage cannot be made to understand when an EVP_CIPHER
pointer, that has been passed to the caller, is no longer being used.

The other problem with the existing API w.r.t. to hooking EVP_CIPHER support
into ENGINE is storage - the OBJ_NAME-based storage used by EVP to register
ciphers simultaneously registers cipher *types* and cipher *implementations* -
they are effectively the same thing, an "EVP_CIPHER" pointer. The problem with
hooking in ENGINEs is that multiple ENGINEs may implement the same ciphers. The
solution is necessarily that ENGINE-provided ciphers simply are not registered,
stored, or exposed to the caller in the same manner as existing ciphers. This is
especially necessary considering the fact ENGINE uses reference counts to allow
for cleanup, modularity, and DSO support - yet EVP_CIPHERs, as exposed to
callers in the current API, support no such controls.

Another sticking point for integrating cipher support into ENGINE is linkage.
Already there is a problem with the way ENGINE supports RSA, DSA, etc whereby
they are available *because* they're part of a giant ENGINE called "openssl".
Ie. all implementations *have* to come from an ENGINE, but we get round that by
having a giant ENGINE with all the software support encapsulated. This creates
linker hassles if nothing else - linking a 1-line application that calls 2 basic
RSA functions (eg. "RSA_free(RSA_new());") will result in large quantities of
ENGINE code being linked in *and* because of that DSA, DH, and RAND also. If we
continue with this approach for EVP_CIPHER support (even if it *was* possible)
we would lose our ability to link selectively by selectively loading certain
implementations of certain functionality. Touching any part of any kind of
crypto would result in massive static linkage of everything else. So the
solution is to change the way ENGINE feeds existing "classes", ie. how the
hooking to ENGINE works from RSA, DSA, DH, RAND, as well as adding new hooking
for EVP_CIPHER, and EVP_MD.

The way this is now being done is by mostly reverting back to how things used to
work prior to ENGINE :-). Ie. RSA now has a "RSA_METHOD" pointer again - this
was previously replaced by an "ENGINE" pointer and all RSA code that required
the RSA_METHOD would call ENGINE_get_RSA() each time on its ENGINE handle to
temporarily get and use the ENGINE's RSA implementation. Apart from being more
efficient, switching back to each RSA having an RSA_METHOD pointer also allows
us to conceivably operate with *no* ENGINE. As we'll see, this removes any need
for a fallback ENGINE that encapsulates default implementations - we can simply
have our RSA structure pointing its RSA_METHOD pointer to the software
implementation and have its ENGINE pointer set to NULL.

A look at the EVP_CIPHER hooking is most explanatory, the RSA, DSA (etc) cases
turn out to be degenerate forms of the same thing. The EVP storage of ciphers,
and the existing EVP API functions that return "software" implementations and
descriptions remain untouched. However, the storage takes more meaning in terms
of "cipher description" and less meaning in terms of "implementation". When an
EVP_CIPHER_CTX is actually initialised with an EVP_CIPHER method and is about to
begin en/decryption, the hooking to ENGINE comes into play. What happens is that
cipher-specific ENGINE code is asked for an ENGINE pointer (a functional
reference) for any ENGINE that is registered to perform the algo/mode that the
provided EVP_CIPHER structure represents. Under normal circumstances, that
ENGINE code will return NULL because no ENGINEs will have had any cipher
implementations *registered*. As such, a NULL ENGINE pointer is stored in the
EVP_CIPHER_CTX context, and the EVP_CIPHER structure is left hooked into the
context and so is used as the implementation. Pretty much how things work now
except we'd have a redundant ENGINE pointer set to NULL and doing nothing.

Conversely, if an ENGINE *has* been registered to perform the algorithm/mode
combination represented by the provided EVP_CIPHER, then a functional reference
to that ENGINE will be returned to the EVP_CIPHER_CTX during initialisation.
That functional reference will be stored in the context (and released on
cleanup) - and having that reference provides a *safe* way to use an EVP_CIPHER
definition that is private to the ENGINE. Ie. the EVP_CIPHER provided by the
application will actually be replaced by an EVP_CIPHER from the registered
ENGINE - it will support the same algorithm/mode as the original but will be a
completely different implementation. Because this EVP_CIPHER isn't stored in the
EVP storage, nor is it returned to applications from traditional API functions,
there is no associated problem with it not having reference counts. And of
course, when one of these "private" cipher implementations is hooked into
EVP_CIPHER_CTX, it is done whilst the EVP_CIPHER_CTX holds a functional
reference to the ENGINE that owns it, thus the use of the ENGINE's EVP_CIPHER is
safe.

The "cipher-specific ENGINE code" I mentioned is implemented in tb_cipher.c but
in essence it is simply an instantiation of "ENGINE_TABLE" code for use by
EVP_CIPHER code. tb_digest.c is virtually identical but, of course, it is for
use by EVP_MD code. Ditto for tb_rsa.c, tb_dsa.c, etc. These instantiations of
ENGINE_TABLE essentially provide linker-separation of the classes so that even
if ENGINEs implement *all* possible algorithms, an application using only
EVP_CIPHER code will link at most code relating to EVP_CIPHER, tb_cipher.c, core
ENGINE code that is independent of class, and of course the ENGINE
implementation that the application loaded. It will *not* however link any
class-specific ENGINE code for digests, RSA, etc nor will it bleed over into
other APIs, such as the RSA/DSA/etc library code.

ENGINE_TABLE is a little more complicated than may seem necessary but this is
mostly to avoid a lot of "init()"-thrashing on ENGINEs (that may have to load
DSOs, and other expensive setup that shouldn't be thrashed unnecessarily) *and*
to duplicate "default" behaviour. Basically an ENGINE_TABLE instantiation, for
example tb_cipher.c, implements a hash-table keyed by integer "nid" values.
These nids provide the uniquenness of an algorithm/mode - and each nid will hash
to a potentially NULL "ENGINE_PILE". An ENGINE_PILE is essentially a list of
pointers to ENGINEs that implement that particular 'nid'. Each "pile" uses some
caching tricks such that requests on that 'nid' will be cached and all future
requests will return immediately (well, at least with minimal operation) unless
a change is made to the pile, eg. perhaps an ENGINE was unloaded. The reason is
that an application could have support for 10 ENGINEs statically linked
in, and the machine in question may not have any of the hardware those 10
ENGINEs support. If each of those ENGINEs has a "des_cbc" implementation, we
want to avoid every EVP_CIPHER_CTX setup from trying (and failing) to initialise
each of those 10 ENGINEs. Instead, the first such request will try to do that
and will either return (and cache) a NULL ENGINE pointer or will return a
functional reference to the first that successfully initialised. In the latter
case it will also cache an extra functional reference to the ENGINE as a
"default" for that 'nid'. The caching is acknowledged by a 'uptodate' variable
that is unset only if un/registration takes place on that pile. Ie. if
implementations of "des_cbc" are added or removed. This behaviour can be
tweaked; the ENGINE_TABLE_FLAG_NOINIT value can be passed to
ENGINE_set_table_flags(), in which case the only ENGINEs that tb_cipher.c will
try to initialise from the "pile" will be those that are already initialised
(ie. it's simply an increment of the functional reference count, and no real
"initialisation" will take place).

RSA, DSA, DH, and RAND all have their own ENGINE_TABLE code as well, and the
difference is that they all use an implicit 'nid' of 1. Whereas EVP_CIPHERs are
actually qualitatively different depending on 'nid' (the "des_cbc" EVP_CIPHER is
not an interoperable implementation of "aes_256_cbc"), RSA_METHODs are
necessarily interoperable and don't have different flavours, only different
implementations. In other words, the ENGINE_TABLE for RSA will either be empty,
or will have a single ENGINE_PILE hashed to by the 'nid' 1 and that pile
represents ENGINEs that implement the single "type" of RSA there is.

Cleanup - the registration and unregistration may pose questions about how
cleanup works with the ENGINE_PILE doing all this caching nonsense (ie. when the
application or EVP_CIPHER code releases its last reference to an ENGINE, the
ENGINE_PILE code may still have references and thus those ENGINEs will stay
hooked in forever). The way this is handled is via "unregistration". With these
new ENGINE changes, an abstract ENGINE can be loaded and initialised, but that
is an algorithm-agnostic process. Even if initialised, it will not have
registered any of its implementations (to do so would link all class "table"
code despite the fact the application may use only ciphers, for example). This
is deliberately a distinct step. Moreover, registration and unregistration has
nothing to do with whether an ENGINE is *functional* or not (ie. you can even
register an ENGINE and its implementations without it being operational, you may
not even have the drivers to make it operate). What actually happens with
respect to cleanup is managed inside eng_lib.c with the "engine_cleanup_***"
functions. These functions are internal-only and each part of ENGINE code that
could require cleanup will, upon performing its first allocation, register a
callback with the "engine_cleanup" code. The other part of this that makes it
tick is that the ENGINE_TABLE instantiations (tb_***.c) use NULL as their
initialised state. So if RSA code asks for an ENGINE and no ENGINE has
registered an implementation, the code will simply return NULL and the tb_rsa.c
state will be unchanged. Thus, no cleanup is required unless registration takes
place. ENGINE_cleanup() will simply iterate across a list of registered cleanup
callbacks calling each in turn, and will then internally delete its own storage
(a STACK). When a cleanup callback is next registered (eg. if the cleanup() is
part of a graceful restart and the application wants to cleanup all state then
start again), the internal STACK storage will be freshly allocated. This is much
the same as the situation in the ENGINE_TABLE instantiations ... NULL is the
initialised state, so only modification operations (not queries) will cause that
code to have to register a cleanup.

What else? The bignum callbacks and associated ENGINE functions have been
removed for two obvious reasons; (i) there was no way to generalise them to the
mechanism now used by RSA/DSA/..., because there's no such thing as a BIGNUM
method, and (ii) because of (i), there was no meaningful way for library or
application code to automatically hook and use ENGINE supplied bignum functions
anyway. Also, ENGINE_cpy() has been removed (although an internal-only version
exists) - the idea of providing an ENGINE_cpy() function probably wasn't a good
one and now certainly doesn't make sense in any generalised way. Some of the
RSA, DSA, DH, and RAND functions that were fiddled during the original ENGINE
changes have now, as a consequence, been reverted back. This is because the
hooking of ENGINE is now automatic (and passive, it can internally use a NULL
ENGINE pointer to simply ignore ENGINE from then on).

Hell, that should be enough for now ... comments welcome.

Adding new libraries
--------------------

When adding a new sub-library to OpenSSL, assign it a library number
ERR_LIB_XXX, define a macro XXXerr() (both in err.h), add its
name to ERR_str_libraries[] (in crypto/err/err.c), and add
ERR_load_XXX_strings() to the ERR_load_crypto_strings() function
(in crypto/err/err_all.c). Finally, add an entry:

    L      XXX     xxx.h   xxx_err.c

to crypto/err/openssl.ec, and add xxx_err.c to the Makefile.
Running make errors will then generate a file xxx_err.c, and
add all error codes used in the library to xxx.h.

Additionally the library include file must have a certain form.
Typically it will initially look like this:

    #ifndef HEADER_XXX_H
    #define HEADER_XXX_H

    #ifdef __cplusplus
    extern "C" {
    #endif

    /* Include files */

    #include <openssl/bio.h>
    #include <openssl/x509.h>

    /* Macros, structures and function prototypes */


    /* BEGIN ERROR CODES */

The BEGIN ERROR CODES sequence is used by the error code
generation script as the point to place new error codes, any text
after this point will be overwritten when make errors is run.
The closing #endif etc will be automatically added by the script.

The generated C error code file xxx_err.c will load the header
files stdio.h, openssl/err.h and openssl/xxx.h so the
header file must load any additional header files containing any
definitions it uses.
=pod

=head1 NAME

bn_mul_words, bn_mul_add_words, bn_sqr_words, bn_div_words,
bn_add_words, bn_sub_words, bn_mul_comba4, bn_mul_comba8,
bn_sqr_comba4, bn_sqr_comba8, bn_cmp_words, bn_mul_normal,
bn_mul_low_normal, bn_mul_recursive, bn_mul_part_recursive,
bn_mul_low_recursive, bn_sqr_normal, bn_sqr_recursive,
bn_expand, bn_wexpand, bn_expand2, bn_fix_top, bn_check_top,
bn_print, bn_dump, bn_set_max, bn_set_high, bn_set_low - BIGNUM
library internal functions

=head1 SYNOPSIS

 #include <openssl/bn.h>

 BN_ULONG bn_mul_words(BN_ULONG *rp, BN_ULONG *ap, int num, BN_ULONG w);
 BN_ULONG bn_mul_add_words(BN_ULONG *rp, BN_ULONG *ap, int num,
   BN_ULONG w);
 void     bn_sqr_words(BN_ULONG *rp, BN_ULONG *ap, int num);
 BN_ULONG bn_div_words(BN_ULONG h, BN_ULONG l, BN_ULONG d);
 BN_ULONG bn_add_words(BN_ULONG *rp, BN_ULONG *ap, BN_ULONG *bp,
   int num);
 BN_ULONG bn_sub_words(BN_ULONG *rp, BN_ULONG *ap, BN_ULONG *bp,
   int num);

 void bn_mul_comba4(BN_ULONG *r, BN_ULONG *a, BN_ULONG *b);
 void bn_mul_comba8(BN_ULONG *r, BN_ULONG *a, BN_ULONG *b);
 void bn_sqr_comba4(BN_ULONG *r, BN_ULONG *a);
 void bn_sqr_comba8(BN_ULONG *r, BN_ULONG *a);

 int bn_cmp_words(BN_ULONG *a, BN_ULONG *b, int n);

 void bn_mul_normal(BN_ULONG *r, BN_ULONG *a, int na, BN_ULONG *b,
   int nb);
 void bn_mul_low_normal(BN_ULONG *r, BN_ULONG *a, BN_ULONG *b, int n);
 void bn_mul_recursive(BN_ULONG *r, BN_ULONG *a, BN_ULONG *b, int n2,
   int dna, int dnb, BN_ULONG *tmp);
 void bn_mul_part_recursive(BN_ULONG *r, BN_ULONG *a, BN_ULONG *b,
   int n, int tna, int tnb, BN_ULONG *tmp);
 void bn_mul_low_recursive(BN_ULONG *r, BN_ULONG *a, BN_ULONG *b,
   int n2, BN_ULONG *tmp);

 void bn_sqr_normal(BN_ULONG *r, BN_ULONG *a, int n, BN_ULONG *tmp);
 void bn_sqr_recursive(BN_ULONG *r, BN_ULONG *a, int n2, BN_ULONG *tmp);

 void mul(BN_ULONG r, BN_ULONG a, BN_ULONG w, BN_ULONG c);
 void mul_add(BN_ULONG r, BN_ULONG a, BN_ULONG w, BN_ULONG c);
 void sqr(BN_ULONG r0, BN_ULONG r1, BN_ULONG a);

 BIGNUM *bn_expand(BIGNUM *a, int bits);
 BIGNUM *bn_wexpand(BIGNUM *a, int n);
 BIGNUM *bn_expand2(BIGNUM *a, int n);
 void bn_fix_top(BIGNUM *a);

 void bn_check_top(BIGNUM *a);
 void bn_print(BIGNUM *a);
 void bn_dump(BN_ULONG *d, int n);
 void bn_set_max(BIGNUM *a);
 void bn_set_high(BIGNUM *r, BIGNUM *a, int n);
 void bn_set_low(BIGNUM *r, BIGNUM *a, int n);

=head1 DESCRIPTION

This page documents the internal functions used by the OpenSSL
B<BIGNUM> implementation. They are described here to facilitate
debugging and extending the library. They are I<not> to be used by
applications.

=head2 The BIGNUM structure

 typedef struct bignum_st BIGNUM;

 struct bignum_st
        {
        BN_ULONG *d;    /* Pointer to an array of 'BN_BITS2' bit chunks. */
        int top;        /* Index of last used d +1. */
        /* The next are internal book keeping for bn_expand. */
        int dmax;       /* Size of the d array. */
        int neg;        /* one if the number is negative */
        int flags;
        };


The integer value is stored in B<d>, a malloc()ed array of words (B<BN_ULONG>),
least significant word first. A B<BN_ULONG> can be either 16, 32 or 64 bits
in size, depending on the 'number of bits' (B<BITS2>) specified in
C<openssl/bn.h>.

B<dmax> is the size of the B<d> array that has been allocated.  B<top>
is the number of words being used, so for a value of 4, bn.d[0]=4 and
bn.top=1.  B<neg> is 1 if the number is negative.  When a B<BIGNUM> is
B<0>, the B<d> field can be B<NULL> and B<top> == B<0>.

B<flags> is a bit field of flags which are defined in C<openssl/bn.h>. The
flags begin with B<BN_FLG_>. The macros BN_set_flags(b, n) and
BN_get_flags(b, n) exist to enable or fetch flag(s) B<n> from B<BIGNUM>
structure B<b>.

Various routines in this library require the use of temporary
B<BIGNUM> variables during their execution.  Since dynamic memory
allocation to create B<BIGNUM>s is rather expensive when used in
conjunction with repeated subroutine calls, the B<BN_CTX> structure is
used.  This structure contains B<BN_CTX_NUM> B<BIGNUM>s, see
L<BN_CTX_start(3)>.

=head2 Low-level arithmetic operations

These functions are implemented in C and for several platforms in
assembly language:

bn_mul_words(B<rp>, B<ap>, B<num>, B<w>) operates on the B<num> word
arrays B<rp> and B<ap>.  It computes B<ap> * B<w>, places the result
in B<rp>, and returns the high word (carry).

bn_mul_add_words(B<rp>, B<ap>, B<num>, B<w>) operates on the B<num>
word arrays B<rp> and B<ap>.  It computes B<ap> * B<w> + B<rp>, places
the result in B<rp>, and returns the high word (carry).

bn_sqr_words(B<rp>, B<ap>, B<n>) operates on the B<num> word array
B<ap> and the 2*B<num> word array B<ap>.  It computes B<ap> * B<ap>
word-wise, and places the low and high bytes of the result in B<rp>.

bn_div_words(B<h>, B<l>, B<d>) divides the two word number (B<h>, B<l>)
by B<d> and returns the result.

bn_add_words(B<rp>, B<ap>, B<bp>, B<num>) operates on the B<num> word
arrays B<ap>, B<bp> and B<rp>.  It computes B<ap> + B<bp>, places the
result in B<rp>, and returns the high word (carry).

bn_sub_words(B<rp>, B<ap>, B<bp>, B<num>) operates on the B<num> word
arrays B<ap>, B<bp> and B<rp>.  It computes B<ap> - B<bp>, places the
result in B<rp>, and returns the carry (1 if B<bp> E<gt> B<ap>, 0
otherwise).

bn_mul_comba4(B<r>, B<a>, B<b>) operates on the 4 word arrays B<a> and
B<b> and the 8 word array B<r>.  It computes B<a>*B<b> and places the
result in B<r>.

bn_mul_comba8(B<r>, B<a>, B<b>) operates on the 8 word arrays B<a> and
B<b> and the 16 word array B<r>.  It computes B<a>*B<b> and places the
result in B<r>.

bn_sqr_comba4(B<r>, B<a>, B<b>) operates on the 4 word arrays B<a> and
B<b> and the 8 word array B<r>.

bn_sqr_comba8(B<r>, B<a>, B<b>) operates on the 8 word arrays B<a> and
B<b> and the 16 word array B<r>.

The following functions are implemented in C:

bn_cmp_words(B<a>, B<b>, B<n>) operates on the B<n> word arrays B<a>
and B<b>.  It returns 1, 0 and -1 if B<a> is greater than, equal and
less than B<b>.

bn_mul_normal(B<r>, B<a>, B<na>, B<b>, B<nb>) operates on the B<na>
word array B<a>, the B<nb> word array B<b> and the B<na>+B<nb> word
array B<r>.  It computes B<a>*B<b> and places the result in B<r>.

bn_mul_low_normal(B<r>, B<a>, B<b>, B<n>) operates on the B<n> word
arrays B<r>, B<a> and B<b>.  It computes the B<n> low words of
B<a>*B<b> and places the result in B<r>.

bn_mul_recursive(B<r>, B<a>, B<b>, B<n2>, B<dna>, B<dnb>, B<t>) operates
on the word arrays B<a> and B<b> of length B<n2>+B<dna> and B<n2>+B<dnb>
(B<dna> and B<dnb> are currently allowed to be 0 or negative) and the 2*B<n2>
word arrays B<r> and B<t>.  B<n2> must be a power of 2.  It computes
B<a>*B<b> and places the result in B<r>.

bn_mul_part_recursive(B<r>, B<a>, B<b>, B<n>, B<tna>, B<tnb>, B<tmp>)
operates on the word arrays B<a> and B<b> of length B<n>+B<tna> and
B<n>+B<tnb> and the 4*B<n> word arrays B<r> and B<tmp>.

bn_mul_low_recursive(B<r>, B<a>, B<b>, B<n2>, B<tmp>) operates on the
B<n2> word arrays B<r> and B<tmp> and the B<n2>/2 word arrays B<a>
and B<b>.

BN_mul() calls bn_mul_normal(), or an optimized implementation if the
factors have the same size: bn_mul_comba8() is used if they are 8
words long, bn_mul_recursive() if they are larger than
B<BN_MULL_SIZE_NORMAL> and the size is an exact multiple of the word
size, and bn_mul_part_recursive() for others that are larger than
B<BN_MULL_SIZE_NORMAL>.

bn_sqr_normal(B<r>, B<a>, B<n>, B<tmp>) operates on the B<n> word array
B<a> and the 2*B<n> word arrays B<tmp> and B<r>.

The implementations use the following macros which, depending on the
architecture, may use "long long" C operations or inline assembler.
They are defined in C<bn_lcl.h>.

mul(B<r>, B<a>, B<w>, B<c>) computes B<w>*B<a>+B<c> and places the
low word of the result in B<r> and the high word in B<c>.

mul_add(B<r>, B<a>, B<w>, B<c>) computes B<w>*B<a>+B<r>+B<c> and
places the low word of the result in B<r> and the high word in B<c>.

sqr(B<r0>, B<r1>, B<a>) computes B<a>*B<a> and places the low word
of the result in B<r0> and the high word in B<r1>.

=head2 Size changes

bn_expand() ensures that B<b> has enough space for a B<bits> bit
number.  bn_wexpand() ensures that B<b> has enough space for an
B<n> word number.  If the number has to be expanded, both macros
call bn_expand2(), which allocates a new B<d> array and copies the
data.  They return B<NULL> on error, B<b> otherwise.

The bn_fix_top() macro reduces B<a-E<gt>top> to point to the most
significant non-zero word plus one when B<a> has shrunk.

=head2 Debugging

bn_check_top() verifies that C<((a)-E<gt>top E<gt>= 0 && (a)-E<gt>top
E<lt>= (a)-E<gt>dmax)>.  A violation will cause the program to abort.

bn_print() prints B<a> to stderr. bn_dump() prints B<n> words at B<d>
(in reverse order, i.e. most significant word first) to stderr.

bn_set_max() makes B<a> a static number with a B<dmax> of its current size.
This is used by bn_set_low() and bn_set_high() to make B<r> a read-only
B<BIGNUM> that contains the B<n> low or high words of B<a>.

If B<BN_DEBUG> is not defined, bn_check_top(), bn_print(), bn_dump()
and bn_set_max() are defined as empty macros.

=head1 SEE ALSO

L<bn(3)>

=head1 COPYRIGHT

Copyright 2000-2016 The OpenSSL Project Authors. All Rights Reserved.

Licensed under the OpenSSL license (the "License").  You may not use
this file except in compliance with the License.  You can obtain a copy
in the file LICENSE in the source distribution or at
L<https://www.openssl.org/source/license.html>.

=cut
State Machine Design
====================

This file provides some guidance on the thinking behind the design of the
state machine code to aid future maintenance.

The state machine code replaces an older state machine present in OpenSSL
versions 1.0.2 and below. The new state machine has the following objectives:
    - Remove duplication of state code between client and server
    - Remove duplication of state code between TLS and DTLS
    - Simplify transitions and bring the logic together in a single location
      so that it is easier to validate
    - Remove duplication of code between each of the message handling functions
    - Receive a message first and then work out whether that is a valid
      transition - not the other way around (the other way causes lots of issues
      where we are expecting one type of message next but actually get something
      else)
    - Separate message flow state from handshake state (in order to better
      understand each)
      - message flow state = when to flush buffers; handling restarts in the
        event of NBIO events; handling the common flow of steps for reading a
        message and the common flow of steps for writing a message etc
      - handshake state = what handshake message are we working on now
    - Control complexity: only the state machine can change state: keep all
      the state changes local to the state machine component

The message flow state machine is divided into a reading sub-state machine and a
writing sub-state machine. See the source comments in statem.c for a more
detailed description of the various states and transitions possible.

Conceptually the state machine component is designed as follows:

                        libssl
                           |
---------------------------|-----statem.h--------------------------------------
                           |
                    _______V____________________
                   |                            |
                   |    statem.c                |
                   |                            |
                   |    Core state machine code |
                   |____________________________|
        statem_locl.h     ^          ^
                 _________|          |_______
                |                            |
   _____________|____________   _____________|____________
  |                          | |                          |
  | statem_clnt.c            | | statem_srvr.c            |
  |                          | |                          |
  | TLS/DTLS client specific | | TLS/DTLS server specific |
  | state machine code       | | state machine code       |
  |__________________________| |__________________________|
               |        |_______________|__       |
               |        ________________|  |      |
               |       |                   |      |
   ____________V_______V________   ________V______V_______________
  |                             | |                               |
  | statem_both.c               | | statem_dtls.c                 |
  |                             | |                               |
  | Non core functions common   | | Non core functions common to  |
  | to both servers and clients | | both DTLS servers and clients |
  |_____________________________| |_______________________________|

Record Layer Design
===================

This file provides some guidance on the thinking behind the design of the
record layer code to aid future maintenance.

The record layer is divided into a number of components. At the time of writing
there are four: SSL3_RECORD, SSL3_BUFFER, DLTS1_BITMAP and RECORD_LAYER. Each
of these components is defined by:
1) A struct definition of the same name as the component
2) A set of source files that define the functions for that component
3) A set of accessor macros

All struct definitions are in record.h. The functions and macros are either
defined in record.h or record_locl.h dependent on whether they are intended to
be private to the record layer, or whether they form part of the API to the rest
of libssl.

The source files map to components as follows:

dtls1_bitmap.c                                   -> DTLS1_BITMAP component
ssl3_buffer.c                                    -> SSL3_BUFFER component
ssl3_record.c                                    -> SSL3_RECORD component
rec_layer_s3.c, rec_layer_d1.c                   -> RECORD_LAYER component

The RECORD_LAYER component is a facade pattern, i.e. it provides a simplified
interface to the record layer for the rest of libssl. The other 3 components are
entirely private to the record layer and therefore should never be accessed
directly by libssl.

Any component can directly access its own members - they are private to that
component, e.g. ssl3_buffer.c can access members of the SSL3_BUFFER struct
without using a macro. No component can directly access the members of another
component, e.g. ssl3_buffer cannot reach inside the RECORD_LAYER component to
directly access its members. Instead components use accessor macros, so if code
in ssl3_buffer.c wants to access the members of the RECORD_LAYER it uses the
RECORD_LAYER_* macros.

Conceptually it looks like this:

                        libssl
                           |
---------------------------|-----record.h--------------------------------------
                           |
                    _______V______________
                   |                      |
                   |    RECORD_LAYER      |
                   |                      |
                   |    rec_layer_s3.c    |
                   |          ^           |
                   | _________|__________ |
                   ||                    ||
                   || DTLS1_RECORD_LAYER ||
                   ||                    ||
                   || rec_layer_d1.c     ||
                   ||____________________||
                   |______________________|
        record_locl.h     ^   ^   ^
         _________________|   |   |_________________
        |                     |                     |
   _____V_________      ______V________      _______V________
  |               |    |               |    |                |
  | SSL3_BUFFER   |    | SSL3_RECORD   |    | DTLS1_BITMAP   |
  |               |--->|               |    |                |
  | ssl3_buffer.c |    | ssl3_record.c |    | dtls1_bitmap.c |
  |_______________|    |_______________|    |________________|


The two RECORD_LAYER source files build on each other, i.e.
the main one is rec_layer_s3.c which provides the core SSL/TLS layer. The second
one is rec_layer_d1.c which builds off of the SSL/TLS code to provide DTLS
specific capabilities. It uses some DTLS specific RECORD_LAYER component members
which should only be accessed from rec_layer_d1.c. These are held in the
DTLS1_RECORD_LAYER struct.
Please checkout the most recent version of metaconfig from:
  svn co https://dist.svn.sourceforge.net/svnroot/dist/trunk/dist
                             dist 3.0

                   Copyright (c) 1988, Larry Wall
                Copyright (c) 1990-1992, Harlan Stenn
              Copyright (c) 1991-1997, Raphael Manfredi

------------------------------------------------------------------------
    This program is free software; you can redistribute it and/or modify
    it under the terms of the Artistic License, a copy of which can be
    found with this package.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Artistic License for more details.
------------------------------------------------------------------------

This version of dist requires you to have at least perl 4.0 PL36.
It has also been ported to work with perl 5.0 PL0, provided you have
at least integrated patches 0a-0h, issued by Andy Dougherty and made
available at the following ftp sites:

	ftp.demon.co.uk:/pub/perl/db/perl5.000-p0a-p0h.tar.gz
	ftp.funet.fi:/pub/languages/perl/ports/perl5/perl5.000-p0a-p0h.tar.gz

Please read all the directions below before you proceed any further, and
then follow them carefully.

After you have unpacked your kit, you should have all the files listed
in MANIFEST.

========================================================================
                           It's not the way I wrote it, but the
                           way you play it makes it sound a lot better.
                                -- Camille Saint-Saens (French composer)

The dist package consists of four parts:

    1) The Configure generator (metaconfig) and its supporting files.
    2) The distribution kit maker (makedist) and its supporting files.
    3) The patch distribution system (pat*) and its supporting files.
    4) The Makefile generator (jmake) and its supporting files.

Each of these can be used separately from the others.  Before you can
use any of those, however, the directory containing your package (not this
package) must be initialized by putting a .package file into it.  This
can be done by running packinit in that directory.

There is a mailing list hosted in Japan and set up by Shigeya Suzuki
<shigeya@foretune.co.jp>, for discussion about the dist package as a
whole. It's a good place to ask questions (or answer them) and to
send your patches. I will post official patches to the net, as well
as to the dist-users list.

To send a mail to the list, address it to <dist-users@foretune.co.jp>.
To subscribe, send a mail to <majordomo@foretune.co.jp>. If you don't
know how to use majordomo, the syntax of the subscribe command is:

	subscribe dist-users [address]

where the address part is optional. You may unsubscribe automatically
at any time by sending:

	unsubscribe dist-users

If you have a problem with this version of dist, it is recommended that
you subscribe to the list, then send a description of your problem to it.
If you send mail to me personally, I may not be able to answer in a
timely fashion.

This mailing list has low traffic (a few articles per week, typically),
and it is expected to remain so, with a high signal/noise ratio.

Notes:

    If you are running on a system with <= 14 char filenames, don't
    distribute any files with filenames longer than 12 chars (with the
    exception of patchlevel.h), so that there will be room for a
    2-digit extension indicating patch number in your bugs direcory.
    This includes .SH files, so any shell script built by a .SH file
    should be 9 characters or less.  On systems with flexfilenames you
    don't have to worry about it.

    This package has been designed on top of dist 2.0, which has been
    written by Larry Wall <lwall@netlabs.com>.
========================================================================

INSTALLATION

1) Run Configure. This will figure out various things about your
system. After it has completed, it will produce config.h and config.sh.

You might possibly have to trim # comments from the front of Configure
if your shell doesn't handle them, but all other comments will be taken
care of.

2) Run make.

3) If make succeeded, you may wish to do "make install install.man". Be
sure your rights are correct (if you install manual pages, you may need
super-user privileges). By not running "make install.man", you avoid the
installation of the manual pages.

4) Read the manual entry before running.

5) IMPORTANT!  Communicate any problem and suggested patches to me,
ram@hptnos02.grenoble.hp.com (Raphael Manfredi), so we can keep this
distribution in sync.  If you have a problem, there will be someone else
who had it or will have it too...

If possible, send me patches such that the patch program will apply
them.  Context diffs are the best, then normal diffs.  Do not send ed
scripts, I have probably changed my copy since the version you got.

6) After everything is installed, you can do make clobber. This will
clean up everything and let you re-distribute this kit, without
carrying useless files. You should keep this distribution intact, so
that future patches will be applyable.

7) I have an automatic patch sender. Send me the following mail:

	Subject: Command
	@SH mailhelp PATH

and you'll get instructions (PATH stands for YOUR e-mail address, either
in INTERNET or in bang notation). I would recommend you to get all the
issued patches before you start making some modifications on this
package.

8) If you wish to deinstall the package, you may run "make deinstall".
A separate "make deinstall.man" will remove the manual pages. Be sure
the makefiles are correctly set before running any deinstall target.
On USG systems, some executable have a chance to remain despite the
deinstall (text file busy...).

	Raphael Manfredi <Raphael_Manfredi@grenoble.hp.com>
This is the root directory for metaconfig.

If you are new to metaconfig, you may wish to have a look at the INTRO
file, which gives a quick introduction.

The metaconfig you have here is a modified version of Larry Wall's 2.0
release.  The units themselves have been ripped off from some Configure
scripts (perl 4.0, elm 2.3).  They all carry a copyright from me, which
is not true, but it was automatically produced and I had no time yet to
set the proper copyrights for each unit.

Although metaconfig, as being part of dist, is covered by the Artistic
License, a Configure script is not copyrighted and belongs to the
public domain. Units can be copyrighted, and credits for each unit may
appear in the generated Configure script, at the author's request.

The manual page for metaconfig is not up-to-date.  The built-in
interpreter and the changes are documented in NOTES.

The units that come from dist 2.0 need to be changed. A script should be
provided in the final release to do an automatic conversion, which will
be fine 90% of the time. If you want to see how new features can be used,
I would recommend you to have a look at Oldconfig.U, d_gethname.U and
voidflags.U.
This directory contains unit templates.

It is hoped metaconfig will have a tool to generate "standard" units based
on some well-known templates.

For now, it has a documentary-only value.
This directory contains a rudimentary kit maker.

N.B.: This must not be confused with the kit package, which is a set of shell
scripts for sending arbitrary files and directories by mail and unpacking them.
One could call kit a binary tarmailer. The kit package has been released
separately from dist (posted on comp.sources.unix in 1991).

Larry Wall said:

	Depending on where you are going to send your kits you might prefer
	to use Rich $alz's kit maker instead--it makes more robust kits
	but assumes more about the target system.

I say:

	If you are using RCS 4.3, be sure to use makedist instead of your
	own shell archiver, unless you do not use $Id, $Header or $Locker
	markers. Moreover, makedist will take the latest checked in
	revision intead of the working file, so that you archive a coherent
	package even if you made some mods since the last patch.

You run makedist in the top level directory of your package and it uses
the MANIFEST.new file to generate shar scripts of about 50000 bytes each.

Just make sure MANIFEST.new contains everything you want, including any
Configure, config.h.SH, or patchlevel.h files. A prototype patchlevel.h
may be found in ../gen/patchlevel.h. See the manpage for more details.

If you do not wish to build up shell archives but an up-to-date copy of
your source tree, run someting like:

	makedist -c dir

to build an up-to-date source tree in dir, which you can then archive using
your own shell archiver.
This is the root directory for jmake.

The jmake program is a Makefile generator. It comes from 'imake' one
may find in the X11R4 distribution, but it produces a Makefile.SH
instead of a Makefile. Jmake has a template which knows some metaconfig
symbols and has built-in commands which make it more powerful than imake.

The jmkmf script may be used to produce the Makefile.SH from a Jmakefile.
Once the bootstrap is done, you can run 'make Makefile.SH' to rebuild the
Makefile.SH in the current directory, or 'make Makefiles.SH' to build the
Makefiles in a recursive manner.

All the rules used by jmake are listed in an automatically built index.
The jmake's cryptic syntax is documented in file NOTES. You may also
have a look at the sample Jmakefiles that come with this package.
Usually, you do not include them in the release, but I kept them so
that you may have a real example and see how things are organized.

If you choose to use jmake, then you will have to use metaconfig, in
order to get a meaningful value for all the needed symbol. Thus, each
time you change your Jmakefiles, it may be necessary to update the
Configure script.

Here is how to use jmake...

First, you have to write a Jmakefile for each directory where you want
to put a Makefile. Be sure to declare all the sub-directories with the
SetSubdirs rule. Usually, the order of the rules is not significant,
but you should make sure the Makefile begins with an 'all::' target,
so that a default 'make' does not run a clean for instance.

Then, if this is the first time, you have to bootstrap. Go to the main
directory of your package and run:

	jmkmf
	make Makefiles.SH

which will first produce the main makefile and then recursively build
all the makefiles.

Once you have bootstrapped once, you can edit a Jmakefile and rebuild
the local makefile with

	make Makefile

or all the hierachy below with:

	make Makefiles.SH

If you want to extract all the makefiles, you may run

	sh Makefile.SH
	make Makefiles

in the top-level directory. Finally, if you only want to test the
generated Makefile.SH without disturbing the Makefile, run

	make Makefile.SH

which will stop before running the produced file through sh.


CAUTION:

On machines whose cpp eats up tabs in macro expansion, the Makefile.SH
produced might not be indented properly inside rules.

Perl 4.0 PL10 sometimes dumps core, while PL3 does not. Thus, perl 4.0
PL10 should NOT be used with jmake, at least on a MIPS.

This is the root directory for pat tools.

This directory contains an automatic patch generator.  You must have RCS
to use this.  You must also have run packinit in the top level directory
of your package to create a .package file.

When you've modified a file in your package, the pat program is used to
control the whole process.  The other programs can be called by hand, but
usually needn't be.  Run pat from the top level directory of your package.

The pat, patcil, patdiff, and patbase programs take a list of filenames as
arguments.  Alternately, a -a means all files listed in MANIFEST.

Patcil will create an RCS directory if necessary.  However, it may not check in
things which require special initializaton properly.  For example, if you
want to check in a shell script, you'd better make your RCS directory yourself
and then say

	rcs -i -c'# ' blurfl.xsh

before running pat or patcil.  Otherwise the RCS log may not be commented
properly.  Unless of course you are using a standard extension (like .c for
a C file) or have placed the proper comments in front of the $Log marker
within the file itself--patcil will then correctly guess the type of
comment required.

Patdiff will create a bugs directory in your top level directory, and will want
to find a patchlevel.h file in that same directory.  Everything is done from
that top level directory--don't put any patchlevel.h or bugs directories in
your subdirectories.  Each subdirectory has its own RCS directory though.

Patpost, patsend and patftp may be used to post to Usenet, mail to someone,
or copy patches to your ftp directory.  They take a destination and a list
of patches to process.

Those pat tools are an hopefully enhanced version of the tools that
came with Larry Wall's dist 2.0. There are however a few new scripts:

    - patclean, which checks in the mods and removes the working files.
    - patcol, which restores the files removed by a patclean.
    - patname, which sets a symbolic version number.

Here is the way I am using the pat tools...

First, I set up a MANIFEST.new file. If you are converting an existing
distribution to use dist, the manifake script will convert a MANIFEST
into a MANIFEST.new (removing the possible archive number column).

Then I run packinit to modify the version number and set up things
correctly. The package is then ready to be placed under pat control.
I make sure the file patchlevel.h is correctly set and I run:

	patcil -f -a -s
	touch patchlevel.h
	find . -name "*~" -exec /bin/rm -f {} \; -print

There is a prototypical patchlevel.h file in this directory, so you
might want to have a look at it.

[If you are planning on using the mailagent to send the patches (and sort
your mail -- that's its primary goal now), the you must make sure
the patchelevel.h file is locatated in the root directory of your package.
The mailagent program is available separately, and was posted on the
comp.sources.misc newsgroup]

Now everything is ready. The distribution is frozen, the bugs directory
has been created. I issue a makedist -v to create the distribution kits.
Eventually I set up the mailagent so that people can request for the
distribution automatically. If I want to create a directory containing
the lattest sources (to be able to `kit' them to someone using the kit
program -- posted to comp.sources.unix), I use:

	makedist -c <package>-<version>@<patchlevel>

for instance, for dist 2.9 at PL26

	makedist -c dist-2.9@26

which I can then send to people directly with kit (which is NOT part
of this release).

As I receive patches or find some bugs, I edit the files and make the
modifications. When I want to issue an official patch, I run:

	pat -n

and one or more patches are issued. You can compress the patches in the
bugs subdirectory, since the mailpatch program knows about that. Also
patindex will correctly uncompress them.

When I need to clean up the distribution directory, I use:

	patclean -a

which checks in every changes and removes the working files. The whole
set of working files can then be restored by:

	patcol -a

Sometimes, I made a couple of modification and I don't want to issue
a patch right now. I then run:

	patcil -a

which checks in the changes. You can run this as many times as you want,
because patcil will skip unchanged file and remembers the last time you
issued a patch.

If you are still using RCS 4.3, be sure you use makedist and not your
own shell archiver, as the $Locker symbol has an annoying expansion
which makes patch to fail when applyed. I'm not sure this was correctly
fixed with RCS 5.5 as I am not using it yet for various reasons.

In any case, if you are using the copyright expansion feature (i.e. the
stuffing of the COPYRIGHT token surrounded by '@' -- can't do it here
or it will get expanded...), then you must use makedist to make sure
the copyright is properly written in all your files. Distributing files
with an un-expanded COPYRIGHT token in them would be a disaster, since
the patching system will also expand them before building a patch and
some of your hunks may not apply correctly.
Iron: the Eiffel library repository 
The folder "iron" should be installed on $ISE_EIFFEL/tools/iron
Note the spec/*/ should be renamed accordingly to the platform.

To upload iron packages, please edit the iron.cfg with good credential, and
repository info, then execute inside "upload" folder

> python ./ise_upload_version.py iron.cfg
About
=====

The command-line tool to install packages, and manage local repositories.
Eiffel Iron Server

This library_indexer tool index ecf files from folders
and provides queries
such as find the libraries providing a specific class

Example:

> library_indexer -v -r --update $ISE_LIBRARY

this will create a "library.db" in current working directory

then you can query 

> library_indexer --search STRING_TABLE
Libraries containing {STRING_TABLE} ->
  base @ C:\_dev\trunk\Src\library\base\base-safe.ecf

> library_indexer --search ZMQ*
Libraries containing {ZMQ*} ->
  zmq @ C:\_dev\trunk\Src\library\zeromq\zmq.ecf
    - ZMQ
    - ZMQ_CONSTANTS
    - ZMQ_BROKER
    - ZMQ_CONTEXT
    - ZMQ_ERROR_CODES
    - ZMQ_MESSAGE
    - ZMQ_POLLER
    - ZMQ_SOCKET

> library_indexer -h
for help
Tool to create ecf redirection

usage: ecf_redirection <subcommand> [options] [args]
Type 'ecf_redirection help <subcommand> for help on a specific subcommand.
Available subcommands:
   help
   create <redirection_ecf> <target_ecf>
   delete <redirection_ecf>
   check  <redirection_ecf> {target_ecf}

Global options:
   -v|--verbose: verbose output

This tool is only a kind of front-end for the tools located in Src/C/bench.
At the moment resource bench does not compile due to the fact that in EiffelLex/EiffelParse they are some undefined routines that needs to be implemented but we haven't spent the time doing that yet.

To compile rename rb.ecf-not_compilable into rb.ecf
== Compile-All tool ==

=== Description ===
This tool can be used to check if all targets in a directory compile.
It recursively scans all directories and looks for files with a .ecf extension.
For each configuration file all targets are processed by actions declared in the command line (could melt, freeze, finalize, ...), and it reports the result as Ok or Failed (or Skipped, Ignored).

=== Command line options ===
To see the list of available command-line options and their help information, use the '/?' switch.

	USAGE:
	   compile_all.exe [-l <directory>] [-compdir <directory>] [-eifgen <directory>]
	 [-logdir <directory>] [-ignore <ignore.ini>] [-log_verbose] [-list_failures] 
	 [-ecb] [-experiment] [-compat] [-clean] [-keep[ <status>]] [-c_compile]
	 [-melt] [-freeze] [-finalize] [-options <key=value> [-options...]] 
	 [-interface <key=value> [-interface...]] 
	 [-version] [-nologo]

	OPTIONS:
	   Options should be prefixed with: '-' or '/'

	   -l            : Directory where to look for configuration files. (Optional)
					   <directory>: A directory to look for ecf files
	   -compdir      : Directory where projects will be compiled. (Optional)
					   <directory>: A directory where the projects will be compiled
	   -eifgen       : Obsolete: see "compdir" option. (Optional)
					   <directory>: ...
	   -logdir       : Directory where logs will be stored (if verbose logging is
					   enabled). (Optional)
					   <directory>: A directory where the logs will be stored
	   -ignore       : Ignore file with files/targets to ignore. (Optional)
					   <ignore.ini>: INI file with the ignores.
	   -log_verbose  : Verbose logging of actions? (Optional)
	   -list_failures: Display a list of failed compilation(s) with associated log filename if
					   available. (Optional)
	   -ecb          : Use ecb instead of ec? (Optional)
	   -experiment   : Use experimental library during compilation? (Optional)
	   -compat       : Use compatible library during compilation? (Optional)
	   -c_compile    : Compile generated C code? (Optional)
	   -melt         : Melt the project? (Optional)
	   -freeze       : Freeze the project? (Optional)
	   -finalize     : Finalize the project? (Optional)
	   -clean        : Clean before compilation? (Optional)
	   -keep         : Keep EIFGENs related data after compilation? (by default
					   they are removed) (Optional)
					   <status>: (Optional) {all | passed | failed}
	   -options      : Comma separated option(s) (Optional)
					   <key=value>: dotnet=(true|false)
									...
	   -interface    : Comma separated option(s) to customize the output (Optional)
					   <key=value>: for instance key "template": using any of
									#action, #target, #uuid, #system, #ecf ,
									#absolute_ecf variables
									...
	   -?            : Display usage information. (Optional)
	   -version      : Displays version information. (Optional)
	   -nologo       : Supresses copyright information. (Optional)

=== Information ===
Online short documentation: https://svn.eiffel.com/eiffelstudio/trunk/Src/tools/compile_all

=== Examples ===
To check if every target in the trunk EIFFEL_SRC folder still compiles, use the following setup
# create a directory which will contain the compilation data (EIFGENs, ...) such as C:\compdir
# compile_all -l %EIFFEL_SRC% -compdir C:\compdir -ignore %EIFFEL_SRC%\tools\compile_all\baseline\trunk.ini -melt -output_template "#ecf #system.#target : "

=== Using -ignore ===
* You can list in an .ini file, the .ecf files or folder to ignore, such as 
	[$EIFFEL_SRC\foo\foo.ecf]
	[$EIFFEL_SRC\foo\bar]

* You can also use regexp  such as

	[regexp=(\\|\/).(svn|git)$]
	[regexp=(\\|\/).*GENs*$]

=== Output progress ===
* During execution of compile_all tool, the default output is for instance
	"Melting test from test (C:\tests\test.ecf)...Ok"

* It is possible to use another output for instance by using 
	-output_template "[#action] #ecf #system.#target : "

* The available variables are #action, #system, #target, #uuid, #ecf, #absolute_ecf and #log_filename

=== Output folders ===
* You can specify the folder that will contains all the compilation data (EIFGENs...) by using "-compdir directory"  (same as obsolete  -eifgen flag). By default this uses the ".ecf" folder.

* You can specify where goes the log files, by using "-logdir directory". By default this uses the ".ecf" folder.

=== Cleaning ===
* By using "-clean" , any compilation will start by cleaning any previous compilation for the target. (i.e: ec -clean ....)

* By default, once the compilation is done, 'compile_all' tool will remove the compilation data (EIFGENs ...). But you decide to keep :
  - all of them by using  "-keep" or "-keep all"
  - only the failed ones by using "-keep failed"
  - only the passed ones by using "-keep passed"

=== Optimization ===
Compling using 'ecb' is slightly faster than just using 'ec' , by default 'compile_all' is using 'ec', but you can decide to use 'ecb' by using flag  " -ecb "

=== Specific -interface .. ===

With release 7.0 the output uses  "passed", "failed", (and others), instead of "Ok",
"Failed" (and others).

However in order to get same output as previous versions of 'compile_all', you
can use:
	-interface "template=#action #target from #system (#ecf)..."
	-interface "text.passed=Ok,text.failed=Failed"

The current possible usage of -interface are:
	-interface text.{id}={new_id}
		where {id} can be: 
			passed, failed, skipped, ignored, error
			target, Parsing, Melting, Freezing, Finalizing
		and {new_id} the value of the wanted text

Note: if ever you want to use comma "," in the template, 
      you can change the non alpha separator by putting the wanted separator char as first character
      For instance, to use ";" as separator
      	-interface ";template=#action, #system, #target, (#ecf), "
	  This way, you can use "," in your value, and here the ";" is used as separator, 
	  Another example:
		-interface ";text.passed=OK;text.failed=Failure, try again later"

=== Specific -options .. ===

This is possible to exclude all dotnet target by using
	-options dotnet=false

The current possible usage of -options are:
	-options dotnet={true|false}
	-options "ec={flags}" and -options "ec.{mode}={flags}"
		where {mode} can be:
			melt, freeze, finalize
		where {flags} is flags for the compiler "ec" such as "-full -verbose" 
		An usage could be:
			-options "ec.finalize=-keep"

Note: in the same way as "-interface", you can choose another separator
		-options "|ec.finalize=-keep|ec.freeze=-c_compile"

Note:
In the future, this "-options" flag will be use for additional purpose such as simulation a specific platform, and so on ...

# Goal:

 update the value of the library's location inside the ecf
 this is useful when the location of library changes (especially with relative path).
 It can also be used to transform relative path to absolute path using an environment variable for instance

# Usage:

ecf_updater - Version: 0.1
Copyright Eiffel Software 2011-2012. All Rights Reserved.

USAGE:
   ecf_updater [<path>[ <path>, ...]] [-r <r|root>] [-f] [-base <base>] [-base_variable <base_variable>] [-ise_library] [-eiffel_library] [-r <r|replace> [-r...
]] [-v] [-b] [-n] [-d] [-v] [-nologo]

OPTIONS:
   Options should be prefixed with: '-' or '/'

   -r --root          : Root directory (Optional)
                        <r|root>: Root directory
   -f --force         : Force execution without any confirmation (Optional)
      --base          : Base name (Optional)
                        <base>: Could be $ISE_LIBRARY
      --base_variable : Base variable name (Optional)
                        <base_variable>: Could be ISE_LIBRARY
      --ise_library   : Use $ISE_LIBRARY for 'base' (Optional)
      --eiffel_library: Use $EIFFEL_LIBRARY for 'base' (Optional)
   -r --replace       : Replace  (Optional)
                        <r|replace>: use FOO=BAR to replace FOO with BAR (case sensitive)
   -v --verbose       : Verbose output (Optional)
   -b --backup        : Backup modified files (Optional)
   -n --simulation    : Simulation mode (Optional)
   -d --diff          : Display diff (Optional)
   -? --help          : Display usage information. (Optional)
   -v --version       : Displays version information. (Optional)
      --nologo        : Supresses copyright information. (Optional)

NON-SWITCHED ARGUMENTS:
   <path>: Eiffel configuration file or directory


# Examples
- Update all ecf files located under . (and recursively in sub directories), and update relative path with absolute path using $ISE_LIBRARY

	ecf_updater --simulation --verbose --diff --ise_library .

- If you have a collection of libraries, and that you use relative path to reference .ecf, whenever you want to move a folder to another, you can easily update your .ecf using ecf_updater
	ecf_updater  --simulation --verbose --diff  .

- Now if you want to "release" your libs and use an environment variable to use absolute path, you can do
	ecf_updater --simulation --verbose --diff  --base_variable MY_EIFFEL_LIBS .

- If you want to update only a subfolder, for instance your examples just do
	ecf_updater --simulation --verbose --diff  examples

# Future potential evolutions
- Handle non relative path, and being able to update ecf file using for instance $EIFFEL_LIBRARY , when a folder is moved.


                           Welcome to PCCTS 1.33

                              October 5, 1995


                          Parr Research Corporation
                                    with
                  Purdue University Electrical Engineering
                                    and
                       University of Minnesota, AHPCRC

                                Terence Parr
                                Russell Quong
                                 Will Cohen
                                 Hank Dietz

[The "NOTES for new users" by Tom Moog is available now via web
 browser at http:www.mcs.net/~tmoog and via anonymous ftp at
 ftp.mcs.net/mcsnet.users/tmoog.]

[We've removed PCCTS.FUTURE from the distribution and added file SERVICES,
 which describes the services of Parr Research Corporation.]


                                INSTALLATION

     This document describes the installation of PCCTS 1.33 on UNIX
and non-UNIX machines.  The UNIX installation is trivial while the
non-UNIX folks have a bit more work to do as an install script
explicitly for there machine will not exist--they will have to
interpret the install script.

     PCCTS 1.33 includes a number of different programs and examples
in the software release package -- most of which like to live in their
own directories.  The install script will build a standard hierarchy.
Or, if you get the tar file off the ftp site, the hierarchy will be
constructed automatically by tar.

     The PCCTS executables (antlr, dlg) may be placed anywhere the user
wishes but the install script places them in the bin directory created
during installation.

1.0.  UNIX USERS

This section is for UNIX users and describes the most convenient
installation procedure.

1.1.  FORMAT: pccts.tar

To begin installation, place the pccts.tar file into the directory
where you want to place a pccts subdirectory.  Untar the file with

     tar xvf pccts.tar

and cd into it.  To install PCCTS, simply type
 
     make

which will build the standard PCCTS directory hierarchy (under the
directory where you ran the install script) and build executable
versions of antlr and dlg.

1.2.  FORMAT: pccts.bag

     To begin installation, the user should create a directory (usually
called pccts) where the PCCTS source subtree is to be created.  Place
the pccts.bag file and the install script into this directory and cd
into it.  To install PCCTS, simply type
 
     sh install

which will build the standard PCCTS directory hierarchy (under the
directory where you ran the install script), "unbag" all of the files
and build executable versions of antlr and dlg.

If you do not have the 'sh' shell, you'll need the install.unbag.reqd
file.

NOTE: If you are using the later SGI C++ compilers, use -woff 3262 to
get rid of a bunch of noise by the compiler (warnings).


2.0.  NON-UNIX USERS

     ANTLR was written using portable (we hope), vanilla K&R-style C,
ANSI C, and C++.  It has been successfully ported to a variety of
environments.  We do not provide an installation script explicitly for
non-Unix users.  You must interpret the install script and perform the
analogous operations on your machine.  There is an install script,
install.mpw, for Macintosh programmers.

IMPORTANT NOTE:  For PC users:  You must create the parser.dlg and
		 "touch" scan.c in antlr and dlg directories or the
		 makefiles will try to execute antlr and dlg, which
		 don't exist yet.  The first time, you want only to
		 compile the C files in order to obtain an executable
		 for antlr and dlg.  From this point, a change in
		 antlr.g or dlg_p.g will force antlr/dlg to regenerate
		 themselves.

		 You must define symbol PC if you want things to work
		 out right for use on a DOS, OS/2, Windows machine.
		 This affects the config.h file, which you can change
		 as you wish.

     For Mac programmers using MPW (Macintosh Programmer's Workshop),
define symbol MPW to get the correct config.h stuff included.

3.0.  EMAIL VERSION RECIPIENTS

     If you received PCCTS via email response from
pccts@ecn.purdue.edu you have one additional installation step to
perform over the ftp folks (and pccts.tar is unavailable).  You will
have received a number of bite-size chunks of pccts which are small
enough to be emailed (~1500 lines each).  You must reconstruct the
PCCTS files before you can begin installation.  In order to rebuild an
original file, you must have "one.c" which will take the chunks and
pack them together.  If you are a non-UNIX type, you must have the
"unbag.c" file which unbags the bags created by our mail archiver.
UNIX folks use the shell to unbag as they would for shar files (this
will be done automatically by the install script).

     To install PCCTS, place all PCCTS mail messages into a pccts
directory, remove the mail headers from one.c.  Then compile one.c
with:

     cc -o one one.c

and then type:

     ./one f1 f2 ... fn

where f1..fn are the parts of PCCTS source sent as chunks (i.e. these
files will be all the files you received NOT including one.c, unbag.c,
README, install and the request acknowledge banner).  There is no need
to remove mail headers from the chunk files and they may appear in any
order.  The subject line of the mail will identify it as a chunk and a
chunk of what file.  The "one" program should be used to put pccts.bag
back together.  You are now in a position to begin normal PCCTS
installation.  All files you receive should go into a pccts directory.

     Note that all files which arrive in "chunks" must be put back
together using "one".  Beware that you do not mix chunks from more
than one original file.  For instance, do not specify all chunks that
you collect from the PCCTS mailbot on the "one" command line unless
you have requested only one original file that was split into multiple
files.  Each chunk knows which original file it is a part of, where it
goes in that file and how many total chunks are required to rebuild
that original.

4.0.  WORD SIZE AND PC USERS

     The config.h file now sets up the word size for your compiler
automatically.


                                TUTORIAL

     The advanced tutorial should be placed in a directory at the
same level as antlr, dlg, support etc...  Do a

     sh advtut.bag

to unbag (or use the unbag program) and then type

     make -s all

which will create executables called tut1-tut4.  Naturally, if you got
the tutorials from the ftp site, the tar format of the tutorials can
be obtained for easier installation.

Unfortunately, the tutorials have changed little since the 1.06
release.  With luck, these will be enhanced and an AST tutorial will
appear.

                         MACHINE COMPATIBILITY

PCCTS is known to compile "out of the box" on the following machines
and/or operating systems:  [didn't have time to retest on all these
machines, but seems to be highly portable still].

o  DECSTATION 5000

o  SGI; use "-woff 3262" in your CFLAGS make variable

o  Sun SparcStation (cc, gcc, g++, Cfront, acc)

o  VAX C under VMS

o  Linux SLS 0.99, gcc/g++

o  386 PC, NetBSD 0.9, gcc 2.4.5

o  HP 9000/755, HP-UX 9.01, HP cc

o  486 PC, OS/2 2.1 (w/long filenames), IBM C Set++ 2.1

o  NeXTStep 3.2 running g++/gcc 2.6.3 (pentium-90)


                           INCOMPATIBILITIES

Please see the release notes.


                                CREDITS

Please see the history.ps or history.txt.
                            ANTLR 1.33

This directory contains the files necessary to build ANTLR.

If you do a "make scrub", ANTLR will have to run on antlr.g and DLG
will have to run on parser.dlg.  Either

(1)     ANTLR uses the previous antlr in that directory to rebuild itself
(2)     Needs to find antlr on the search path

You will find that running "antlr -gh antlr.g" will result in about
10 ambiguity warnings.  These are normal.  Don't worry.

If you do a "make clean" right after installation, ANTLR and DLG should
not need to run; only the C files will compile.

Don't forget to go into the makefile to uncomment the appropriate
definitions for your OS/architecture/compiler or see the appropriate
NOTES.?? file.
Eiffel script-like execution
============================

#Overview
The purpose of this `eiffel` tool, is to execute an Eiffel project by providing the .ecf file.

`Usage:  eiffel prog.ecf arg1 arg2 ...`

The first time, it compiles `prog.ecf` in finalized mode, and on success it launchs the generated executable with arguments `arg1 arg2 ...`.

Then the next time, `eiffel` reuses the executable previously compiled (if any). The (re)compilation is triggered only if the `prog.ecf` is changed, or if required by the `eiffel` command using specific options `-b or --build`.
(TODO: find better way to detect changes that would trigger a new compilation).

# Build instruction

The `eiffel` can also be used to compile the `prog.ecf` and save the generated file at given location.
`eiffel (--target targetname) build prog.ecf path-to-prog.exe`

# Usage:

```
USAGE:
  eiffel (-v|--verbose) (-h|--help) (-b|--build) (--check class,project) (--target ecf_target_name) (--resource file_name)* <project.ecf> ...
  eiffel build (-v|--verbose) (--target ecf_target_name) (--resource file_name)* <project.ecf> <output_executable_path> ...

COMMANDS:
  <project.ecf> ...   : build once and launch <project.ecf> execution.
  build               : build project and save executable as <output_executable_path>.

OPTIONS:
  --target <ecf-target-name>    : optional target name.
  --resource <file-name>        : optional resource file name to copy in the parent directory of the EIFGENs
                                : such as *.rc files (multiple occurrences allowed).
  --check <level>               : check level for recompilation, either class (default), or project.
                                : class   = check timestamp of system class files,
                                :           and ecf files for included libraries
                                :          (ignoring classes from libraries).
                                : project = only check the timestamp of main project ecf file.

  -b --build                    : force a fresh system build.
  -o --executable-output <path> : build and save executable as <path>.
                                : without any execution.!

  -v --verbose                  : verbose output.
  -h --help                     : display this help.
  ...                           : arguments for the <project.ecf> execution.

Note: you can overwrite default value, using
  EIFFEL_SCRIPT_DIR       : root directory for eiffel script app (default under Eiffel user files/.apps)
  EIFFEL_SCRIPT_CACHE_DIR : directory caching the compiled executables ($EIFFEL_SCRIPT_DIR/cache)
  EIFFEL_SCRIPT_COMP_DIR : directory caching the EIFGENs compilation ($EIFFEL_SCRIPT_DIR/comp)
```

# Status

* status:experimental

For now, this is an experimentation.

Description

Running Eweasel, people may have to disable those intempestive dialogs that shows up when test crashes asking if one wants to debug it. One may follow Dr Watson (http://dev.eiffel.com/Dr_Watson) to disable them, But sometimes it doesn't work for some reasons. This tool is made as another choice to close those annoying windows.

The tool is functionally simple, and easy to use. Simply start it before or after launching eweasel tests with few settings:

    * Top Window Title - The window where the button to click is.
    * Button Text - The text on the button to be clicked. Note that one need to add a "&" before the shortcut character. 
    * Scan interval - Interval between each scanning for the button, in seconds.

One can use this tool to automatically click buttons raised by applications that may break smooth processes. For example, a tool unconfigurably needs confirmation on certain behaviors (Deleting, Ignoring and so on).

Dependencies

    * EiffelBase
    * EiffelVision2
    * WEL
    * EiffelStudio

Supported Platforms

    * Windows

== "ecf_tool create" command ==

This command helps the user to create an ecf file for either a library, an application or a testing suite.

== Examples ==

* New application ecf
>  ecf_tool create --application APPLICATION.make --add_cluster src --add_library base --add_library diff
>  ecf_tool create --application APPLICATION.make --console -c src -l base -l diff -l c:\my_libs\foo.ecf

* New library ecf
>  ecf_tool create --library -c src -l base -l diff


== Usage ==

create - Version: 14.11
Copyright Eiffel Software 1985-2014. All Rights Reserved.

USAGE:
   ecf_tool.exe create [-l <l|add_library> [-l...]] [-c <c|add_cluster> [-c...]] [-t <t|add_test> [-t...]] 
	[-uuid <uuid>] [-n <n|name>] [-syntax <syntax>] [-library] [-application[ <Entry point>]] [-testing]
	[-executable_name <executable_name>] [-console] [-concurrency <concurrency>] [-thread] [-scoop] 
	[-f] [-v] [-v] [-nologo] [<path>]

OPTIONS:
   Options should be prefixed with: '-' or '/'

   -l --add_library    : Libraries (Optional)
                         <l|add_library>: Library to include
   -c --add_cluster    : Clusters (Optional)
                         <c|add_cluster>: Cluster to include
   -t --add_test       : Tests clusters (Optional)
                         <t|add_test>: Tests cluster to include
      --uuid           : UUID (Optional)
                         <uuid>: UUID value
   -n --name           : Target name (Optional)
                         <n|name>: Eiffel target name
      --syntax         : Syntax mode (Optional)
                         <syntax>: Syntax mode: obsolete, transitional, default=standard, provisional
      --library        : This is a library configuration file (Optional)
      --application    : This is an application configuration file (Optional)
                         <Entry point>: (Optional) Root cluster.CLASS_NAME.creation_name information (cluster is
                                        optional)
      --testing        : This is an testing configuration file (Optional)
      --executable_name: Executable name (Optional)
                         <executable_name>: Executable name (without extension)
      --console        : Console application mode (Optional)
      --concurrency    : Concurrency mode (Optional)
                         <concurrency>: Concurrency mode: default=none, thread, scoop
      --thread         : Concurrency mode = thread (Optional)
      --scoop          : Concurrency mode = SCOOP (Optional)
   -f --force          : Force execution without any confirmation (Optional)
   -v --verbose        : Verbose output (Optional)
   -? --help           : Display usage information. (Optional)
   -v --version        : Displays version information. (Optional)
      --nologo         : Supresses copyright information. (Optional)

NON-SWITCHED ARGUMENTS:
   <path>: directory for target

NON-SWITCHED ARGUMENTS:
   <path>: directory for target

== "ecf_tool resave" command ==

Resave an Eiffel Configuration File (or all ecf from a directory), so that it uses latest .ecf schema.

== Examples ==

>  ecf_tool resave my_project.ecf


== Usage ==


resave - Version: 14.11
Copyright Eiffel Software 1985-2014. All Rights Reserved.

USAGE: 
   ecf_tool.exe resave [-r] [-version] [-nologo] [<path> [<path>, ...]]

OPTIONS:
   Options should be prefixed with: '-' or '/'

   -r      : Recursive scan any directories for *.ecf (Optional)
   -?      : Display usage information. (Optional)
   -version: Displays version information. (Optional)
   -nologo : Supresses copyright information. (Optional)

NON-SWITCHED ARGUMENTS:
   <path>: An Eiffel configuration file or a directory
== "ecf_tool integration" command ==

This command will create an Eiffel Configuration File (ecf) that includes a collection of .ecf files.
Such generated ecf can be used during integration/testing to compile many ecf projects at once,
and then, for instance this can help refactorying operations across many projects.

== Examples ==

>  ecf_tool integration -o all.ecf path-to-libs


== Usage ==

integration - Version: 14.11
Copyright Eiffel Software 1985-2014. All Rights Reserved.

USAGE: 
   ecf_tool.exe integration [-r <folder>] -o <ecf_file> [-f] [-v] [-x <path> [-x...]] [-v] [-nologo] [<path>]

OPTIONS:
   Options should be prefixed with: '-' or '/'

   -r --root   : Root directory (Optional)
                 <folder>: Root directory
   -o --output : Output config file
                 <ecf_file>: output config file
   -f --force  : Force execution without any confirmation (Optional)
   -v --verbose: Verbose output (Optional)
   -x --exclude: Excluded directories (Optional)
                 <path>: directory
   -? --help   : Display usage information. (Optional)
   -v --version: Displays version information. (Optional)
      --nologo : Supresses copyright information. (Optional)

NON-SWITCHED ARGUMENTS:
   <path>: folder to look Eiffel configuration files
# Goal:
	ecf_tool groups a collection of tools related to ecf manipulation.
	For now, there are 5 commands, execute "ecf_tool help" to get information

# Help:
 - updater: Update ecf files content for location and various data according to given parameters.
 - integration: Include all scanned ecf files into a unique integration file to be able to compile all at once.
 - resave: Update ecf files content for location and various data according to given parameters.
 - create: Create Eiffel ecf project file accordingly to user input.
 - redirection: Create an Eiffel Configuration File redirection.

# Usage:

	ecf_tool help

	ecf_tool updater --help
	ecf_tool integration --help
	ecf_tool resave --help
	ecf_tool create --help
	ecf_tool redirection --help
== "ecf_tool updater" command ==

For a collection of ecf files, update the library location to reflect existing project.
This can be used when moving a library from a location to another, and update all existing ecf that uses this.

== Examples ==

* update ecf files from $ISE_LIBRARY, for instance if a library is moved or renamed.
> ecf_tool updater --simulation --force --diff --root $ISE_LIBRARY/library $ISE_LIBRARY/library 

* update ecf files from $MY_PROJECTS, in case libraries were renamed or moved in $ISE_LIBRARY
> ecf_tool updater --simulation --force --diff --root $ISE_LIBRARY/library $MY_PROJECTS

* Replace $ISE_LIBRARY by $EIFFEL_LIBRARY
> ecf_tool updater --simulation --force --diff --replace ISE_LIBRARY=EIFFEL_LIBRARY --root $ISE_LIBRARY/library $ISE_LIBRARY/library 

* Update ecfs, but only with library locations from $ISE_LIBRARY/library and $ISE_LIBRARY/contrib
> ecf_tool updater --simulation --force --diff --root $ISE_LIBRARY/library --include $ISE_LIBRARY/library --include $ISE_LIBRARY/contrib $MY_PROJECTS

It is also possible to exclude directories from being scanned (and associated ecfs included) thanks to the --exclude option.


== Usage ==

updater - Version: 16.5
Copyright Eiffel Software 1985-2016. All Rights Reserved.

USAGE:
   ecf_tool.exe updater [-r <r|root>] [--include <include> [-include...]] [--exclude <exclude> [-exclude...]] [--avoid <avoid> [-avoid...]] [-f] [--base <base>] [--base_variable <base_variable>] [--ise_library] [--eiffel_library] [--replace <replace> [-replace...]] [-x <replace> [-x...]] [-v] [-b] [-n] [-d] [-v] [--nologo] [<path> [<path>, ...]]

OPTIONS:
   Options should be prefixed with: '-' or '/'

   -r --root                : Root directory (Optional)
                              <r|root>: Root directory
      --include             : Include <directory> (Optional)
                              <include>: directory
      --exclude             : Exclude <directory> (Optional)
                              <exclude>: directory
      --avoid               : Avoid to select new ecf location from <directory> (Optional)
                              <avoid>: directory
   -f --force               : Force execution without any confirmation (Optional)
      --base                : Base name (Optional)
                              <base>: Could be $ISE_LIBRARY
      --base_variable       : Base variable name (Optional)
                              <base_variable>: Could be ISE_LIBRARY
      --ise_library         : Use $ISE_LIBRARY for 'base' (Optional)
      --eiffel_library      : Use $EIFFEL_LIBRARY for 'base' (Optional)
      --replace             : Replace  (Optional)
                              <replace>: use FOO=BAR to replace FOO with BAR (case sensitive)
   -x --expand-variable-with: Expand variable VAR with value (Optional)
                              <replace>: use VAR=value to expand VAR environment variable with 'value'
   -v --verbose             : Verbose output (Optional)
   -b --backup              : Backup modified files (Optional)
   -n --simulation          : Simulation mode (Optional)
   -d --diff                : Display diff (Optional)
   -? --help                : Display usage information. (Optional)
   -v --version             : Displays version information. (Optional)
      --nologo              : Supresses copyright information. (Optional)

NON-SWITCHED ARGUMENTS:
   <path>: Eiffel configuration file or directory

== "ecf_tool redirection" command ==

Create an ecf redirection, similar to symbolic link but using .ecf files.


== Examples ==

If a library is moved from old\location\lib.ecf to new\location\new_lib.ecf, a redirection could be created to avoid breaking existing project looking for the lib.ecf at the former location.

> ecf_tool redirection create old\location\lib.ecf new\location\new_lib.ecf

== Usage ==


usage: ecf_tool redirection <subcommand> [options] [args]
Type 'ecf_tool redirection help <subcommand> for help on a specific subcommand.
Available subcommands:
   help
   create <redirection_ecf> <target_ecf>
   delete <redirection_ecf>
   check  <redirection_ecf> {target_ecf}
   shadow/unshadow  <redirection_ecf> {target_ecf}

Global options:
   -v|--verbose: verbose output


=== ecf_tool redirection help create ===

usage: ecf_tool redirection create [options] <redirection_ecf> <target_ecf>
   <redirection_ecf> : redirection ecf file
   <target_ecf>      : target ecf file
Create a redirection from <redirection_ecf> to <target_ecf>.

Options:
   -f|--force: force operation

Global options:
   -v|--verbose: verbose output


Description

The tool was designed to replace the compile_all tool. With SCOOP equiped, it fully utilizes all CPUs on a machine, which make the compilation work much faster. In additional, a new function of running Auto-test in a batch is also added.

To use the tool, execute with -? option to check in details.XML v2 libraries

= Description =
- XML parser: parser and callbacks components
- XML tree: document, elements, and nodes (and related visitors)

= What is the difference with previous set of XML libraries =
This set of libraries is a fork of previous set.
It adds unicode support.
As a consequence it manipulates instances of STRING_32, and not just STRING_8.
The various features signature uses (*)_STRING_32.

This is the main breaking change with previous XML libraries.
Users are encouraged to migrate to this new version, since previous version was handling only ASCII, and had trouble to unescape entities such as &#12345;  (which represents a unicode character).

In addition, it does not make sense to restrict XML to ASCII, and the XML specification is all about unicode.

= How to migrate to XML v2 =
- Update your configuration files  ( .ecf ) to use the new xml_*.ecf paths.
- Make sure the various descendant of XML_CALLBACKS uses the adapted signature. And thus manipulate STRING_32 and not just STRING_8.
- XML_nodes returns READABLE_STRING_32 objects, and not anymore just STRING_8
- check any implicit conversion from STRING_32 to STRING_8 that might truncate and break the semantic of your XML data.

= Future changes =

= Misc =

-- Date: 2012/oct/25
This library was inspired by GoboEiffel's xml library (http://www.gobosoft.com/)This library was inspired by GoboEiffel's xml library (http://www.gobosoft.com/)To build libevent, type

$ ./configure && make

     (If you got libevent from the subversion repository, you will
      first need to run the included "autogen.sh" script in order to
      generate the configure script.)

Install as root via

# make install

You can run the regression tests by

$ make verify

Before, reporting any problems, please run the regression tests.

To enable the low-level tracing build the library as:

CFLAGS=-DUSE_DEBUG ./configure [...]

Acknowledgements:
-----------------

The following people have helped with suggestions, ideas, code or
fixing bugs:

  Alejo
  Weston Andros Adamson
  William Ahern
  Stas Bekman
  Andrew Danforth
  Mike Davis
  Shie Erlich
  Alexander von Gernler
  Artur Grabowski
  Aaron Hopkins
  Claudio Jeker
  Scott Lamb
  Adam Langley
  Philip Lewis
  David Libenzi
  Nick Mathewson
  Andrey Matveev
  Richard Nyberg
  Jon Oberheide
  Phil Oleson
  Dave Pacheco
  Tassilo von Parseval
  Pierre Phaneuf
  Jon Poland
  Bert JW Regeer
  Dug Song
  Taral

If I have forgotten your name, please contact me.
Eiffel internationalisation (i18n) library, version 1.0

BLABLA

This library is distributed under the Eiffel Forum License v2; a copy of this license can be found in the file "forum.txt" or at http://www.eiffel-nice.org/license/eiffel-forum-license-2.txt .  

INSTALLATION

You will have to set an environment variable called EIFFEL_I18N that points to the directory that you installed the library into - that is, the directory containing the library's .ecf file.
You will also have to compile the library's C-code.

Linux:

	From the root directory of the library execute the following commands: 
	
	cd Clib/
	finish-freezing -library
	
Under Windows for use without .NET:

	Please make sure you have the environment variables ISE_EIFFEL and ISE_C_COMPILER defined.
	This should have been done during installation of EiffelStudio; if not please refer to it's documentation.  ISE_EIFFEL should point to your EiffelStudio installation and ISE_C_COMPILER should indicate your C compiler ('msc' or 'bcb').
	If you are using the Borland compiler, you just need to run the 'make_bcb.bat' file in the Clib\ directory.
	
	If you are using Microsoft Visual Studio, you'll have to play with environment variables for a bit longer.
	You can follow the instructions given at http://dev.eiffel.com/Windows_32-bit_C_compiler , or you can try doing it yourself.
	In our case this involved:
		1. Making sure ISE_EIFFEL, ISE_C_COMPILER and ISE_PLATFORM were set.
		2. Changing the INCLUDE variable to contain something like
			C:\Program Files\Microsoft Visual Studio .NET 2003\SDK\v1.1\include\;
			C:\Program Files\Microsoft Visual Studio .NET 2003\Vc7\PlatformSDK\Include;
			C:\Program Files\Microsoft Visual Studio .NET 2003\Vc7\include;
		3. Changing the PATH variable to contain something like
			C:\Program Files\Microsoft Visual Studio .NET 2003\SDK\v1.1\Bin\;
			C:\Program Files\Microsoft Visual Studio .NET 2003\Vc7\bin;
			C:\Program Files\Microsoft Visual Studio .NET 2003\Common7\IDE;
	Once the enviroment variables are set correctly you should be able to run 'make_msc.bat'.
	Alternatively I suggest using the Borland compiler, as it does not require making sure utilities dispersed across half your hard drive are pointer to in $PATH.
		
	
Under Windows with .NET:

	No extra compilation required.

DOCUMENTATION

Both a user guide and a developer guide can be found in the "doc" directory. As the names indicate, the user guide explains how to use the library and documents it's features, whereas the developer guide is intended for people who want to extend or modify the library. 
HTML and text formats are available. 

Up-to-date and/or prettier versions can be found at the following two URLS:
http://dev.eiffel.com/Internationalization/User_guide
http://dev.eiffel.com/Internationalization/Developer_guide

HISTORY

1.0: initial release
Welcome to the distribution of Gobo from EiffelSoftware.

Here are some information on this distribution:

 * The Gobo binaries are located in spec/$ISE_PLATFORM/bin.

 * The documentation is available from http://www.gobosoft.com

 * The samples can be compiled using the gobo_sample.ecf file and replacing the
   THE_ROOT_CLASS_HERE by the actual name of the root class for the sample you chose.

Happy Eiffeling,
The EiffelSoftware Team	
This folder contains generated (unversioned) Eiffel file from the svn checkout.


note: leave this file so that git-svn also create the folder.
This folder contains generated (unversioned) Eiffel file from the svn checkout.


note: leave this file so that git also creates the folder.
This folder contains generated (unversioned) Eiffel file from the svn checkout.


note: leave this file so that git also creates the folder.
This folder contains generated (unversioned) Eiffel file from the svn checkout.


note: leave this file so that git also creates the folder.
This folder contains generated (unversioned) Eiffel file from the svn checkout.


note: leave this file so that git also creates the folder.
This folder contains generated (unversioned) Eiffel file from the svn checkout.


note: leave this file so that git also creates the folder.
This folder contains generated (unversioned) Eiffel file from the svn checkout.


note: leave this file so that git also creates the folder.
This folder contains generated (unversioned) Eiffel file from the svn checkout.


note: leave this file so that git also creates the folder.
The EiffelStore library provides a consistent set of 
classes for writing object oriented Eiffel applications that need 
to handle persistent objects.

The library interface consists of two sets:

1) A set of general purpose classes designed regardless of any data 
 management system used, to be found in directory 
 $ISE_LIBRARY/library/store/interface, and that you always need in your universe

2) Specific classes, referred to by the interface classes, bridging
  the application to selected data management systems called ``handles''. 
  The set of handles may be found:

   * in directory $ISE_LIBRARY/library/store/dbms

   * in the directory $ISE_LIBRARY/library/store/dbms/rdbms/{server_name}   
   with {server_name} corresponding to a selected relational database 
   management system.

   The best way to use them is to include the corresponding configuration file
   $ISE_LIBRARY/library/store/dbms/rdbms/{server_name}/{server_name.ecf}

   Additional support classes are also needed in your universe
   regardless of the selected handle. They are located in:
   
   * directory $ISE_LIBRARY/library/store/support and 
      $ISE_LIBRARY/library/store/dbms/support

Example classes are located in $ISE_EIFFEL/examples/store

EiffelStore has currently only been tested with:
		EiffelStudio 5.7
   		Oracle8 8.0.4
		ODBC 3.0

Documentation
-------------
   The user's manual is in Postscript format in directory /doc
   (cover page + content in US LTR format)

Then, to install EiffelStore external libraries, go to directory 
$ISE_EIFFEL/library/store/install (a README file provides full instructions).
One needs to setup database and modify test.config to fit database settings before running the tests.
# Eiffel Store test cases 
==========================
* support NULL values with SQL queries and Store Procedures.
* DB_PROC.store example.
* EiffelStore safe queries examples
* EiffelStore unsafe queries examples
* Eiffel SQL injection



This directory contains the upper level classes of EiffelStore



1. DB_CONTROL
-------------
This class provides session control and management primivites: 
connect, disconnect, commit, rollback, and database status flags.

It uses classes from the $ISE_EIFFEL/library/store/support directory.


2. DB_CHANGE
------------
This class allows an Eiffel user to modify persistent objects
(made persistent in DB repository from Eiffel or from any other source).
Objects can be referred to directly, or through a mapping table. 


3. DB_STORE
-----------
This class performs standard store operations on Eiffel objects. 
The way objects are stored varies according to EiffelStore layer used.


4. DB_SELECTION
---------------
This class performs standard retrieve operations on Eiffel objects.
The way objects are stored varies according to the EiffelStore layer used.


5. DB_REPOSITORY
----------------
This class captures the notion of data repository implemented in
different ways according to the selected data base handle.


6. DB_RESULT
------------
This class represents the notion of query result, in different
formats depending on the data base handle used.

7. DB_BYN_CHANGE
----------------
This class is quite the same class as DB_CHANGE but with dynamic sql.

8. DB_DYN_STORE
---------------
This class is quite the same class as DB_STORE but with dynamic sql.

EiffelStore
-----------

Installation 

1. Make sure the environment variables ISE_EIFFEL and ISE_PLATFORM are set.

2. Configure your setup for the database

3. Install the C-libraries:

	Start your databases kernels if needed (most of the C-libraries are based
	on DBMS libraries, but some of them use a precompiler which needs to access
	the database kernel).

	Go in the directory specific to the handle you are using and perform the
	following actions. For instance, for the ODBC handle:

	* Windows:
		cd %ISE_EIFFEL%\library\store\dbms\rdbms\odbc\Clib
		finish_freezing -library

	* Unix:
		cd $ISE_EIFFEL/library/store/dbms/rdbms/odbc/Clib
		finish_freezing -library

Collection of classes that help testing some facility of EiffelBase.
Eiffel Event Library (EEL)
(C) ISE 1999

This is the beginings of some hopefully generaly useful event handling stuff.
This library was inspired by GoboEiffel's xml library (http://www.gobosoft.com/)This library was inspired by GoboEiffel's xml library (http://www.gobosoft.com/)Before using the vision libraries you must compile
the C libraries in the Clib directory.
There is a Makefile.SH in each subdirectory.

You will need to make sure that the parent directory
for X11/includes is defined or included in the make file.

Then place the archive produced in each subdirectory in the
directory $EIFFEL4/library/mel/spec/$PLATFORM/lib.

This will need to be done on for each platform you will
be running mel on.

A documentation for EiffelTest still has to be written. It will appear 
web site as soon as possible. For the meantime, looking at the supplied
examples gives a good overview on how to work with this library.
The following classes have been made obsolete from 
version 3.3.7:

Kernel classe:
IO_HANDLER

Oui widget classes:
LABEL_G, PUSH_BG, SEPARATOR_G, TOGGLE_BG, SCROLL_LIST
LIST_MAN, MESSAGE, PROMPT

Context data classes:
CIRCNOT_DATA, FOCSOUT_DATA, MAPREQ_DATA, SELCLR_DATA
CIRCREQ_DATA, FOCUSIN_DATA, MESSAGE_DATA, SELNOT_DATA
CLRMAP_DATA, GRAPEXP_DATA, MULTIPL_DATA, SELREQ_DATA
CONFNOT_DATA, GRAVNOT_DATA, NOEXP_DATA, TOGGLE_DATA
CONFREQ_DATA, KEYMAP_DATA, PROPERT_DATA, UNMAP_DATA
CREATE_DATA, LEAVE_DATA, REPAREN_DATA, VISIBLE_DATA
DESTROY_DATA, MAPNOT_DATA, RESIZE_DATA, ENTER_DATA     
MAPPING_DATA, SCALE_DATA

To include these obsolete classes into your application
you must follow these steps:

1. If you are using MOTIF, change the declaration of the toolkit 
   initialization from MOTIF to OBSOLETE_MOTIF (for windows, change 
   the declaration from MS_WINDOWS to OBSOLETE_MS_WINDOWS)
2. Include the following clusters into your Ace file:
   obsolete_oui:    "$ISE_EIFFEL/library/vision/obsolete/oui";
   obsolete_toolkit:"$ISE_EIFFEL/library/vision/obsolete/toolkit";
   obsolete_motif:  "$ISE_EIFFEL/library/vision/obsolete/motif";
Eiffel2Java interface library.

This library needs the include files for JNI and the JVM library to be found by the compiler.
On UNIX this can normally be done by doing something like

export JAVA_HOME="/usr/lib/j2sdk1.5-sun"
export CPATH=$CPATH:"$JAVA_HOME/include;$JAVA_HOME/include/linux"
export LIBRARY_PATH=$LIBRARY_PATH:"$JAVA_HOME/jre/lib/amd64/server"
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:"$JAVA_HOME/jre/lib/amd64/server"

JAVA_HOME and the path to the libjvm.so library may have to be changed to fit the local installation.

On windows with Microsoft C compiler this can be done by adding the paths to environment variables, e.g.:

INCLUDE: C:\Program Files\Java\jdk1.5.0_06\include;C:\Program Files\Java\jdk1.5.0_06\include\win32 (directories where the jni.h and jni_md.h are)
LIB: C:\Program Files\Java\jdk1.5.0_06\lib (directory where the jvm.lib is)
PATH: C:\Program Files\Java\jre1.5.0_06\bin\client (directory where the jvm.dll is, needed to run the compiled program)
