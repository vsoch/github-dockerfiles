These tests test integration of 3scale with external (remote) services. For example payment gateways, and so on.
These configuration files will set up an Nginx instance as an API
Gateway that will use 3scale to authenticate incoming API calls.
* Getting started

  These are the basic changes you need to do in order to get your
  configuration up and running.

  #. drop these files into your Nginx configuration directory
     (e.g. /opt/openresty/nginx/conf).

  #. modify the server_name statement in your nginx.conf file to be
  the domain of your Nginx proxy (this step is only stricly necessary if
  you have more than one service in 3scale)

  #. start Nginx or reload Nginx (see Nginx on-premises setup guide in
  the Resources section)

* Detailed walkthrough

** Nginx.conf

*** upstreams

    These are the backend servers to which Nginx will be sending
    requests. There will always be:

    - One for each service you have in 3scale (your API backend servers)
    - An additional one pointing to the 3scale service management API

*** server sections

    There is one server section for each service that you configure in
    your 3scale admin portal. Each server section acts as a different
    virtual host, allowing you to expose multiple domains/subdomains with
    one instance of Nginx.

    - server_name : Domain name of the virtual host. It is only
      required when there are more than one server sections.

*** location sections

    Within each server section you will find multiple location sections.

**** location /
     This is the main location and it is the point of entry for all
     incoming API requests. This section calls the Lua code in the
     nginx.lua file to authenticate the request and, if the
     authentication is successful, allows it to go through to the API
     backend.

     Some important configurations within the main location section:


     - access_by_lua: 'requires' your Lua configuration file in your
       server (e.g.  /opt/openresty/nginx/conf/nginx_12345.lua) and
       call the function 'access'.

     - proxy_pass: If the authentication performed during the
       *access_by_lua* step has been successful then this
       instruction will perform a pass through. The variable
       *$proxy_pass* will have been set to point to the correct
       upstream in the Lua code.

**** location /threescale_authrep
     This and any other location sections different than the main one
     (i.e. the one with the "/" path) are only used internally by
     Nginx itself when calling 3scale.

*** Nginx.lua

This file contains the code that performs the authentication for all
incoming API calls. This includes validations against what you have
configured in your 3scale admin portal:

- check that the request carries credentials in the expected location defined in 3scale
- check that the URL path matches at least one of those defined in 3scale
- call 3scale to authorize the request
- if the response is successful, keep the authorization result in a local cache and let the request go through
- if the response is unsuccessful, block the request and return the appropriate error code to the client

From all the code sections there are only a few you really need to
know about. These parts are the only ones impacted when you modify
your configuration options in the 3scale admin portal.

1.**Error parameters**: These are the status code and error messages
that a client will get in response in case their API call was
unsuccessful. These parameters are configured from the proxy
integration page for each one of your services.

2.**Mappings**: For each one of your services there will also be a
function in extract_usage key.

This function is the output of the mapping rules section of the proxy
integration page in the 3scale admin portal. It will parse the URL
path of the incoming request and attempt to match it against the ones
previously defined by you. For each successful match the corresponding
method/metric will be added to the transaction that will be reported
to 3scale.

3.**Extracting credentials**

Near the end of the nginx.lua file, there will be a snippet of code like the following for each one of your services:

#+BEGIN_SRC lua
if ngx.var.service_id == '2555417709352' then
	local parameters = get_auth_params("headers", string.split(ngx.var.request, " ")[1] )
    service = service_2555417709352
    ngx.var.secret_token = service.secret_token
    params.user_key = parameters["user_key"]
    get_credentials_user_key(params , service_2555417709352)
    ngx.var.cached_key = "2555417709352" .. ":" .. params.user_key
    auth_strat = "1"
    ngx.var.service_id = "2555417709352"
    ngx.var.proxy_pass = "https://example.com"
    usage, matched_patterns = service:extract_usage(ngx.var.request)
 end
#+END_SRC

This is the entry point of the code in this file, where the service
will be identified by its **id** and then the corresponding helper
functions will be called to perform the key verification and the URL
matching.


** Common edits

*** Multiple services under same domain
By default, when you have multiple services in 3scale these are translated into multiple **server** sections in the nginx.conf file. Since in Nginx a server section is equivalent to a virtual host, this means that each server will require a different domain name to be set up (using the **server_name** statement).

It is sometimes desirable to expose multiple 3scale services through a single domain (e.g. api.mycompany.com) and then use a path fragment to distinguish between them:

- api.mycompany.com/firstapi/
- api.mycompany.com/secondapi/

This can be easily achieved by converting your configuration to have a single **server** section and one **location /apipath** section within it for each service. The steps to achieve this starting from a default configuration with two services would be:

- copy the **location /** section from one server section to the other one
- delete one server section so you only keep the one that now has  two **location /** sections
- you can tell apart both services by looking at its **$service_id** variable which is the id for that service in 3scale.
- modify the paths of these root locations to be **location /service1** and **location /service2**


*** Using user_key as basic auth

If you want your API to require the credentials to be sent following the [Basic Auth](http://tools.ietf.org/html/rfc2617#section-2) format you can do so with a very simple change.

Before downloading your Nginx configuration files you should have set your authentication mode to **user_key** and the credentials location to **headers** in your 3scale admin portal. If that is not the case, you just need to change those settings and download the files again.

Once the required settings are in place, you just need to replace one function from your **nginx.lua** configuration file.

- locate the function named get_auth_params
- replace it by the one in [this snippet](http://codehub.3scale.net/nginx/lua/authentication/2014/08/11/ExtractingBasicAuthtoken/)

Now you will be able to call your API by sending the credentials in the authorization headers:

#+BEGIN_SRC lua
Authorization: Basic <user_key>
#+END_SRC

** Customizations
   Apicast offers a way to modify its behaviour through an external
   file that will be evaluated as lua code. The behaviour of the
   authorization and matching of mapping rules can be modified using
   this method.

*** Activate customization
    In the beginning of the file, change the value of custom_config to
    the filename to require.
    #+BEGIN_SRC lua
    local custom_config = false
    #+END_SRC

    #+BEGIN_SRC lua
    local custom_config = "config"
    #+END_SRC

    should load "config.lua"

*** Format of config.lua
    The configuration file should be a module which exports a function
    called setup.

    This 'setup' method will be called with the 'access' module as a
    parameter, allowing to get to the service configs, or overwriting
    the matching functions.

    - All request increments hits in 1. superseeds any proxy rule:
    #+BEGIN_SRC lua
    return { setup = function(_M)  _M.extract_usage = function() return {hits = 1}, "hits" end }
    #+END_SRC

    - Add a custom metric to all hits. appart from the normal ones
    #+BEGIN_SRC lua
return {
  setup = function(_M)
    ngx.log(0, "SETTING UP")

    for id, definition in pairs(_M.services) do
        local old_extract_usage = definition.extract_usage

        local new_one = function(service, request)
          local usage, log = old_extract_usage(service, request)
          usage.my_new_metric = 1
          return usage, log .. ", my_new_metric"
        end

        definition.extract_usage = new_one
      end
    end

    ngx.log(0, "SETUP FINISHED")
  end
}
       #+END_SRC

    - Add optional slash to exact maching endpoints that end with dollar
    #+BEGIN_SRC lua
return {
  setup = function(_M)
    ngx.log(0, "SETTING UP")

    for id, definition in pairs(_M.services) do
      for i,r in ipairs(definition.rules) do
        r.pattern = r.pattern:gsub("%$", '\\/*$')
      end
    end
    ngx.log(0, "SETUP FINISHED")
  end
}
    #+END_SRC

** Deployment and maintenance

How to start Nginx:

#+BEGIN_SRC lua
  sudo /opt/openresty/nginx/sbin/nginx -p /opt/openresty/nginx/ -c /opt/openresty/nginx/conf/YOUR-CONFIG-FILE.conf
#+END_SRC

How to stop it:

#+BEGIN_SRC lua
sudo /opt/openresty/nginx/sbin/nginx -p /opt/openresty/nginx/ -c /opt/openresty/nginx/conf/YOUR-CONFIG-FILE.conf -s stop
#+END_SRC

Reload (for example, after a change to the configuration):
#+BEGIN_SRC lua
  sudo /opt/openresty/nginx/sbin/nginx -p /opt/openresty/nginx/ -c /opt/openresty/nginx/conf/YOUR-CONFIG-FILE.conf -s reload
#+END_SRC

**Note:** these commands assume that you installed the Openresty bundle to the `/opt/openresty/` directory.

You can always get a new version of your Nginx configuration from your the proxy integration page in your 3scale admin portal.
A quicker alternative is to get it through an API call:

#+BEGIN_SRC lua
curl -X GET "https://MYCOMPANY-admin.3scale.net/admin/api/nginx.zip?provider_key=PROVIDERKEY"
#+END_SRC

If you are using the 3scale AWS AMI there is a built-in tool that makes this more convenient. You just need to run:

#+BEGIN_SRC lua
download-3scale-config
#+END_SRC

Check in the the resources section for a document with more information about deploying Nginx on your own server.

* Resources
- [[https://support.3scale.net/docs/deployment-options/apicast-self-managed][NGINX self-managed setup]]
- [[https://support.3scale.net/docs/deployment-options/advanced-nginx][Advanced settings for NGINX in 3scale]]
- [[https://support.3scale.net/docs/api-devops/production-tips][Useful tips for running the 3scale API gateway in production]]
Raimon Grau


Table of Contents
_________________

1 Getting started
2 Detailed walkthrough
.. 2.1 Nginx.conf
..... 2.1.1 upstreams
..... 2.1.2 server sections
..... 2.1.3 location sections
..... 2.1.4 Nginx.lua
.. 2.2 Common edits
..... 2.2.1 Multiple services under same domain
..... 2.2.2 Using user_key as basic auth
.. 2.3 Customizations
..... 2.3.1 Activate customization
..... 2.3.2 Format of config.lua
.. 2.4 Deployment and maintenance
3 Resources


These configuration files will set up an Nginx instance as an API
Gateway that will use 3scale to authenticate incoming API calls.


1 Getting started
=================

  These are the basic changes you need to do in order to get your
  configuration up and running.

  #. drop these files into your Nginx configuration directory
     (e.g. /opt/openresty/nginx/conf).

  #. modify the server_name statement in your nginx.conf file to be the
  domain of your Nginx proxy (this step is only stricly necessary if you
  have more than one service in 3scale)

  #. start Nginx or reload Nginx (see Nginx on-premises setup guide in
  the Resources section)


2 Detailed walkthrough
======================

2.1 Nginx.conf
~~~~~~~~~~~~~~

2.1.1 upstreams
---------------

  These are the backend servers to which Nginx will be sending
  requests. There will always be:

  - One for each service you have in 3scale (your API backend servers)
  - An additional one pointing to the 3scale service management API


2.1.2 server sections
---------------------

  There is one server section for each service that you configure in
  your 3scale admin portal. Each server section acts as a different
  virtual host, allowing you to expose multiple domains/subdomains with
  one instance of Nginx.

  - server_name : Domain name of the virtual host. It is only required
    when there are more than one server sections.


2.1.3 location sections
-----------------------

  Within each server section you will find multiple location sections.


* 2.1.3.1 location /

  This is the main location and it is the point of entry for all
  incoming API requests. This section calls the Lua code in the
  nginx.lua file to authenticate the request and, if the authentication
  is successful, allows it to go through to the API backend.

  Some important configurations within the main location section:


  - access_by_lua: 'requires' your Lua configuration file in your server
    (e.g.  /opt/openresty/nginx/conf/nginx_12345.lua) and call the
    function 'access'.

  - proxy_pass: If the authentication performed during the
    *access_by_lua* step has been successful then this instruction will
    perform a pass through. The variable *$proxy_pass* will have been
    set to point to the correct upstream in the Lua code.


* 2.1.3.2 location /threescale_authrep

  This and any other location sections different than the main one
  (i.e. the one with the "/" path) are only used internally by Nginx
  itself when calling 3scale.


2.1.4 Nginx.lua
---------------

  This file contains the code that performs the authentication for all
  incoming API calls. This includes validations against what you have
  configured in your 3scale admin portal:

  - check that the request carries credentials in the expected location
    defined in 3scale
  - check that the URL path matches at least one of those defined in
    3scale
  - call 3scale to authorize the request
  - if the response is successful, keep the authorization result in a
    local cache and let the request go through
  - if the response is unsuccessful, block the request and return the
    appropriate error code to the client

  From all the code sections there are only a few you really need to
  know about. These parts are the only ones impacted when you modify
  your configuration options in the 3scale admin portal.

  1.**Error parameters**: These are the status code and error messages
  that a client will get in response in case their API call was
  unsuccessful. These parameters are configured from the proxy
  integration page for each one of your services.

  2.**Mappings**: For each one of your services there will also be a
  function in extract_usage key.

  This function is the output of the mapping rules section of the proxy
  integration page in the 3scale admin portal. It will parse the URL
  path of the incoming request and attempt to match it against the ones
  previously defined by you. For each successful match the corresponding
  method/metric will be added to the transaction that will be reported
  to 3scale.

  3.**Extracting credentials**

  Near the end of the nginx.lua file, there will be a snippet of code
  like the following for each one of your services:

  ,----
  | if ngx.var.service_id == '2555417709352' then
  |   local parameters = get_auth_params("headers", string.split(ngx.var.request, " ")[1] )
  |     service = service_2555417709352
  |     ngx.var.secret_token = service.secret_token
  |     params.user_key = parameters["user_key"]
  |     get_credentials_user_key(params , service_2555417709352)
  |     ngx.var.cached_key = "2555417709352" .. ":" .. params.user_key
  |     auth_strat = "1"
  |     ngx.var.service_id = "2555417709352"
  |     ngx.var.proxy_pass = "https://example.com"
  |     usage, matched_patterns = service:extract_usage(ngx.var.request)
  |  end
  `----

  This is the entry point of the code in this file, where the service
  will be identified by its **id** and then the corresponding helper
  functions will be called to perform the key verification and the URL
  matching.


2.2 Common edits
~~~~~~~~~~~~~~~~

2.2.1 Multiple services under same domain
-----------------------------------------

  By default, when you have multiple services in 3scale these are
  translated into multiple **server** sections in the nginx.conf
  file. Since in Nginx a server section is equivalent to a virtual host,
  this means that each server will require a different domain name to be
  set up (using the **server_name** statement).

  It is sometimes desirable to expose multiple 3scale services through a
  single domain (e.g. api.mycompany.com) and then use a path fragment to
  distinguish between them:

  - api.mycompany.com/firstapi/
  - api.mycompany.com/secondapi/

  This can be easily achieved by converting your configuration to have a
  single **server** section and one **location /apipath** section within
  it for each service. The steps to achieve this starting from a default
  configuration with two services would be:

  - copy the **location /** section from one server section to the other
    one
  - delete one server section so you only keep the one that now has two
    **location /** sections
  - you can tell apart both services by looking at its **$service_id**
    variable which is the id for that service in 3scale.
  - modify the paths of these root locations to be **location
    /service1** and **location /service2**


2.2.2 Using user_key as basic auth
----------------------------------

  If you want your API to require the credentials to be sent following
  the [Basic Auth]([http://tools.ietf.org/html/rfc2617#section-2])
  format you can do so with a very simple change.

  Before downloading your Nginx configuration files you should have set
  your authentication mode to **user_key** and the credentials location
  to **headers** in your 3scale admin portal. If that is not the case,
  you just need to change those settings and download the files again.

  Once the required settings are in place, you just need to replace one
  function from your **nginx.lua** configuration file.

  - locate the function named get_auth_params
  - replace it by the one in [this
    snippet]([http://codehub.3scale.net/nginx/lua/authentication/2014/08/11/ExtractingBasicAuthtoken/])

  Now you will be able to call your API by sending the credentials in
  the authorization headers:

  ,----
  | Authorization: Basic <user_key>
  `----


2.3 Customizations
~~~~~~~~~~~~~~~~~~

  Apicast offers a way to modify its behaviour through an external file
  that will be evaluated as lua code. The behaviour of the authorization
  and matching of mapping rules can be modified using this method.


2.3.1 Activate customization
----------------------------

  In the beginning of the file, change the value of custom_config to the
  filename to require.
  ,----
  | local custom_config = false
  `----

  ,----
  | local custom_config = "config"
  `----

  should load "config.lua"


2.3.2 Format of config.lua
--------------------------

  The configuration file should be a module which exports a function
  called setup.

  This 'setup' method will be called with the 'access' module as a
  parameter, allowing to get to the service configs, or overwriting the
  matching functions.

  - All request increments hits in 1. superceeds any proxy rule:
  ,----
  | return { setup = function(_M)  _M.extract_usage = function() return {hits = 1}, "hits" end }
  `----

  - Add a custom metric to all hits. appart from the normal ones
  ,----
  | return {
  |   setup = function(_M)
  |     ngx.log(0, "SETUPPING")
  |
  |     for k, v in pairs(_M) do
  |       if k:match('service_') then
  |
  |         local old_extract_usage =  _M[k].extract_usage
  |
  |         local new_one = function(service, request)
  |           local usage, log = old_extract_usage(service, request)
  |           usage.my_new_metric = 1
  |           return usage, log .. ", my_new_metric"
  |         end
  |
  |         _M[k].extract_usage = new_one
  |       end
  |     end
  |
  |     ngx.log(0, "SETUP FINISHED")
  |   end
  | }
  `----

  - Add optional slash to exact maching endpoints that end with dollar
  ,----
  | return {
  |   setup = function(_M)
  |     ngx.log(0, "SETUPPING")
  |
  |     for k, v in pairs(_M) do
  |       if k:match('service_') then
  |         for i,r in ipairs(v.rules) do
  |           r.pattern = r.pattern:gsub("%$", '\\/*$')
  |         end
  |       end
  |     end
  |     ngx.log(0, "SETUP FINISHED")
  |   end
  | }
  `----


2.4 Deployment and maintenance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  How to start Nginx:

  ,----
  | sudo /opt/openresty/nginx/sbin/nginx -p /opt/openresty/nginx/ -c /opt/openresty/nginx/conf/YOUR-CONFIG-FILE.conf
  `----

  How to stop it:

  ,----
  | sudo /opt/openresty/nginx/sbin/nginx -p /opt/openresty/nginx/ -c /opt/openresty/nginx/conf/YOUR-CONFIG-FILE.conf -s stop
  `----

  Reload (for example, after a change to the configuration):
  ,----
  | sudo /opt/openresty/nginx/sbin/nginx -p /opt/openresty/nginx/ -c /opt/openresty/nginx/conf/YOUR-CONFIG-FILE.conf -s reload
  `----

  **Note:** these commands assume that you installed the Openresty
    bundle to the `/opt/openresty/` directory.

  You can always get a new version of your Nginx configuration from your
  the proxy integration page in your 3scale admin portal.  A quicker
  alternative is to get it through an API call:

  ,----
  | curl -X GET "https://MYCOMPANY-admin.3scale.net/admin/api/nginx.zip?provider_key=PROVIDERKEY"
  `----

  If you are using the 3scale AWS AMI there is a built-in tool that
  makes this more convenient. You just need to run:

  ,----
  | download-3scale-config
  `----

  Check in the the resources section for a document with more
  information about deploying Nginx on your own server.


3 Resources
===========

  - [Nginx on-premises setup]
  - [Advanced settings for Nginx in 3scale]
  - [Useful tips for running the 3scale API gateway in production]


  [Nginx on-premises setup]
  https://support.3scale.net/docs/deployment-options/apicast-self-managed

  [Advanced settings for Nginx in 3scale]
  https://support.3scale.net/howtos/api-configuration#apicast-advanced-config

  [Useful tips for running the 3scale API gateway in production]
  https://support.3scale.net/howtos/api-configuration#production-tips-gateway
# Working with Oracle

Save the 3 Oracle binaries in this directory (vendor/oracle):

- instantclient-basiclite-linux.x64-12.2.0.1.0.zip
- instantclient-sdk-linux.x64-12.2.0.1.0.zip
- instantclient-odbc-linux.x64-12.2.0.1.0-2.zip


Then run `DB=oracle make build`== Welcome to Rails

Rails is a web-application framework that includes everything needed to create
database-backed web applications according to the Model-View-Control pattern.

This pattern splits the view (also called the presentation) into "dumb"
templates that are primarily responsible for inserting pre-built data in between
HTML tags. The model contains the "smart" domain objects (such as Account,
Product, Person, Post) that holds all the business logic and knows how to
persist themselves to a database. The controller handles the incoming requests
(such as Save New Account, Update Product, Show Post) by manipulating the model
and directing data to the view.

In Rails, the model is handled by what's called an object-relational mapping
layer entitled Active Record. This layer allows you to present the data from
database rows as objects and embellish these data objects with business logic
methods. You can read more about Active Record in
link:files/vendor/rails/activerecord/README.html.

The controller and view are handled by the Action Pack, which handles both
layers by its two parts: Action View and Action Controller. These two layers
are bundled in a single package due to their heavy interdependence. This is
unlike the relationship between the Active Record and Action Pack that is much
more separate. Each of these packages can be used independently outside of
Rails. You can read more about Action Pack in
link:files/vendor/rails/actionpack/README.html.


== Getting Started

1. At the command prompt, create a new Rails application:
       <tt>rails new myapp</tt> (where <tt>myapp</tt> is the application name)

2. Change directory to <tt>myapp</tt> and start the web server:
       <tt>cd myapp; rails server</tt> (run with --help for options)

3. Go to http://localhost:3000/ and you'll see:
       "Welcome aboard: You're riding Ruby on Rails!"

4. Follow the guidelines to start developing your application. You can find
the following resources handy:

* The Getting Started Guide: http://guides.rubyonrails.org/getting_started.html
* Ruby on Rails Tutorial Book: http://www.railstutorial.org/


== Debugging Rails

Sometimes your application goes wrong. Fortunately there are a lot of tools that
will help you debug it and get it back on the rails.

First area to check is the application log files. Have "tail -f" commands
running on the server.log and development.log. Rails will automatically display
debugging and runtime information to these files. Debugging info will also be
shown in the browser on requests from 127.0.0.1.

You can also log your own messages directly into the log file from your code
using the Ruby logger class from inside your controllers. Example:

  class WeblogController < ActionController::Base
    def destroy
      @weblog = Weblog.find(params[:id])
      @weblog.destroy
      logger.info("#{Time.now} Destroyed Weblog ID ##{@weblog.id}!")
    end
  end

The result will be a message in your log file along the lines of:

  Mon Oct 08 14:22:29 +1000 2007 Destroyed Weblog ID #1!

More information on how to use the logger is at http://www.ruby-doc.org/core/

Also, Ruby documentation can be found at http://www.ruby-lang.org/. There are
several books available online as well:

* Programming Ruby: http://www.ruby-doc.org/docs/ProgrammingRuby/ (Pickaxe)
* Learn to Program: http://pine.fm/LearnToProgram/ (a beginners guide)

These two books will bring you up to speed on the Ruby language and also on
programming in general.


== Debugger

Debugger support is available through the debugger command when you start your
Mongrel or WEBrick server with --debugger. This means that you can break out of
execution at any point in the code, investigate and change the model, and then,
resume execution! You need to install ruby-debug to run the server in debugging
mode. With gems, use <tt>sudo gem install ruby-debug</tt>. Example:

  class WeblogController < ActionController::Base
    def index
      @posts = Post.all
      debugger
    end
  end

So the controller will accept the action, run the first line, then present you
with a IRB prompt in the server window. Here you can do things like:

  >> @posts.inspect
  => "[#<Post:0x14a6be8
          @attributes={"title"=>nil, "body"=>nil, "id"=>"1"}>,
       #<Post:0x14a6620
          @attributes={"title"=>"Rails", "body"=>"Only ten..", "id"=>"2"}>]"
  >> @posts.first.title = "hello from a debugger"
  => "hello from a debugger"

...and even better, you can examine how your runtime objects actually work:

  >> f = @posts.first
  => #<Post:0x13630c4 @attributes={"title"=>nil, "body"=>nil, "id"=>"1"}>
  >> f.
  Display all 152 possibilities? (y or n)

Finally, when you're ready to resume execution, you can enter "cont".


== Console

The console is a Ruby shell, which allows you to interact with your
application's domain model. Here you'll have all parts of the application
configured, just like it is when the application is running. You can inspect
domain models, change values, and save to the database. Starting the script
without arguments will launch it in the development environment.

To start the console, run <tt>rails console</tt> from the application
directory.

Options:

* Passing the <tt>-s, --sandbox</tt> argument will rollback any modifications
  made to the database.
* Passing an environment name as an argument will load the corresponding
  environment. Example: <tt>rails console production</tt>.

To reload your controllers and models after launching the console run
<tt>reload!</tt>

More information about irb can be found at:
link:http://www.rubycentral.org/pickaxe/irb.html


== dbconsole

You can go to the command line of your database directly through <tt>rails
dbconsole</tt>. You would be connected to the database with the credentials
defined in database.yml. Starting the script without arguments will connect you
to the development database. Passing an argument will connect you to a different
database, like <tt>rails dbconsole production</tt>. Currently works for MySQL,
PostgreSQL and SQLite 3.

== Description of Contents

The default directory structure of a generated Ruby on Rails application:

  |-- app
  |   |-- assets
  |   |   |-- images
  |   |   |-- javascripts
  |   |   `-- stylesheets
  |   |-- controllers
  |   |-- helpers
  |   |-- mailers
  |   |-- models
  |   `-- views
  |       `-- layouts
  |-- config
  |   |-- environments
  |   |-- initializers
  |   `-- locales
  |-- db
  |-- doc
  |-- lib
  |   |-- assets
  |   `-- tasks
  |-- log
  |-- public
  |-- script
  |-- test
  |   |-- fixtures
  |   |-- functional
  |   |-- integration
  |   |-- performance
  |   `-- unit
  |-- tmp
  |   `-- cache
  |       `-- assets
  `-- vendor
      |-- assets
      |   |-- javascripts
      |   `-- stylesheets
      `-- plugins

app
  Holds all the code that's specific to this particular application.

app/assets
  Contains subdirectories for images, stylesheets, and JavaScript files.

app/controllers
  Holds controllers that should be named like weblogs_controller.rb for
  automated URL mapping. All controllers should descend from
  ApplicationController which itself descends from ActionController::Base.

app/models
  Holds models that should be named like post.rb. Models descend from
  ActiveRecord::Base by default.

app/views
  Holds the template files for the view that should be named like
  weblogs/index.html.erb for the WeblogsController#index action. All views use
  eRuby syntax by default.

app/views/layouts
  Holds the template files for layouts to be used with views. This models the
  common header/footer method of wrapping views. In your views, define a layout
  using the <tt>layout :default</tt> and create a file named default.html.erb.
  Inside default.html.erb, call <% yield %> to render the view using this
  layout.

app/helpers
  Holds view helpers that should be named like weblogs_helper.rb. These are
  generated for you automatically when using generators for controllers.
  Helpers can be used to wrap functionality for your views into methods.

config
  Configuration files for the Rails environment, the routing map, the database,
  and other dependencies.

db
  Contains the database schema in schema.rb. db/migrate contains all the
  sequence of Migrations for your schema.

doc
  This directory is where your application documentation will be stored when
  generated using <tt>rake doc:app</tt>

lib
  Application specific libraries. Basically, any kind of custom code that
  doesn't belong under controllers, models, or helpers. This directory is in
  the load path.

public
  The directory available for the web server. Also contains the dispatchers and the
  default HTML files. This should be set as the DOCUMENT_ROOT of your web
  server.

script
  Helper scripts for automation and generation.

test
  Unit and functional tests along with fixtures. When using the rails generate
  command, template test files will be generated for you and placed in this
  directory.

vendor
  External libraries that the application depends on. Also includes the plugins
  subdirectory. If the app has frozen rails, those gems also go here, under
  vendor/rails/. This directory is in the load path.
Put here scripts for profiler (script/performance/request).


Run them in staging enviroment like this:
RAILS_ENV=staging script/performance/request lib/profiler_scripts/whatever.rb
# cdn
3scale Assets CDN
# OpenShift deployment

Follow the instructions in openshift templates repository:

https://github.com/3scale/openshift-templates/tree/master/system

```shell
cd 3scale
git clone git@github.com:3scale/openshift-templates.git
cd openshift-templates/system
cat README.md
```

# System Release as a part of AMP

1. Build the image

   ```shell
   make build DOCKERFILE=Dockerfile.on_prem NAME=amp VERSION=system-er2-pre1
   ```

2. Test the image

   ```shell
   make test NAME=amp VERSION=system-er2-pre1
   ```

3. Tag the image

   ```shell
   make tag NAME=amp VERSION=system-er2-pre1
   ```

4. Push the image

   ```shell
   make push NAME=amp VERSION=system-er2-pre1
   ```