Instead of making style sheets, make sass files.

This project uses [themes_for_rails](https://github.com/lucasefe/themes_for_rails) and the 
[rails 3 asset pipeline](http://guides.rubyonrails.org/asset_pipeline.html).

Read the rails guide for more information on the asset pipeline.

Images, Javascripts, and stylesheets for this theme go in `app/assets/themes/<theme-name>/stylesheets/*.sass`
The file `app/assets/themes/<theme-name>/stylesheets/application.sass` should include the 'main' stylesheet references.

    /*
    * =require application
    */

You can then add any other local theme-specific requires using addtional ` =require `  statments. Note: to take advantage
of scss variables &etc, instead use the @import directive (not in comments.)

themes_for_rails is configured in an initialization block under ` config/intializers `

Basically it's doing this:

    config.themes_dir = ":root/app/assets/themes"
    config.assets_dir = ":root/app/assets/themes/:name"
    config.themes_routes_dir = "assets"

  Instead of making style sheets, make sass files.

This project uses [themes_for_rails](https://github.com/lucasefe/themes_for_rails) and the 
[rails 3 asset pipeline](http://guides.rubyonrails.org/asset_pipeline.html).

Read the rails guide for more information on the asset pipeline.

Images, Javascripts, and stylesheets for this theme go in `app/assets/themes/<theme-name>/stylesheets/*.sass`
The file `app/assets/themes/<theme-name>/stylesheets/application.sass` should include the 'main' stylesheet references.

    /*
    * =require application
    */

You can then add any other local theme-specific requires using addtional ` =require `  statments. Note to take advantage
of scss variables &etc, instead use the @improt directive (not in comments.)

themes_for_rails is configured in an initialization block under ` config/intializers `

basically its doing this:

    config.themes_dir = ":root/app/assets/themes"
    config.assets_dir = ":root/app/assets/themes/:name"
    config.themes_routes_dir = "assets"

  Instead of making style sheets, make sass files.

This project uses [themes_for_rails](https://github.com/lucasefe/themes_for_rails) and the 
[rails 3 asset pipeline](http://guides.rubyonrails.org/asset_pipeline.html).

Read the rails guide for more information on the asset pipeline.

Images, Javascripts, and stylesheets for this theme go in `app/assets/themes/<theme-name>/stylesheets/*.sass`
The file `app/assets/themes/<theme-name>/stylesheets/application.sass` should include the 'main' stylesheet references.

    /*
    * =require application
    */

You can then add any other local theme-specific requires using addtional ` =require `  statments. Note to take advantage
of scss variables &etc, instead use the @improt directive (not in comments.)

themes_for_rails is configured in an initialization block under ` config/intializers `

basically its doing this:

    config.themes_dir = ":root/app/assets/themes"
    config.assets_dir = ":root/app/assets/themes/:name"
    config.themes_routes_dir = "assets"

  Instead of making style sheets, make sass files.

This project uses [themes_for_rails](https://github.com/lucasefe/themes_for_rails) and the 
[rails 3 asset pipeline](http://guides.rubyonrails.org/asset_pipeline.html).

Read the rails guide for more information on the asset pipeline.

Images, Javascripts, and stylesheets for this theme go in `app/assets/themes/<theme-name>/stylesheets/*.sass`
The file `app/assets/themes/<theme-name>/stylesheets/application.sass` should include the 'main' stylesheet references.

    /*
    * =require application
    */

You can then add any other local theme-specific requires using addtional ` =require `  statments. Note to take advantage
of scss variables &etc, instead use the @improt directive (not in comments.)

themes_for_rails is configured in an initialization block under ` config/intializers `

basically its doing this:

    config.themes_dir = ":root/app/assets/themes"
    config.assets_dir = ":root/app/assets/themes/:name"
    config.themes_routes_dir = "assets"

  Instead of making style sheets, make sass files.

This project uses [themes_for_rails](https://github.com/lucasefe/themes_for_rails) and the 
[rails 3 asset pipeline](http://guides.rubyonrails.org/asset_pipeline.html).

Read the rails guide for more information on the asset pipeline.

Images, Javascripts, and stylesheets for this theme go in `app/assets/themes/<theme-name>/stylesheets/*.sass`
The file `app/assets/themes/<theme-name>/stylesheets/application.sass` should include the 'main' stylesheet references.

    /*
    * =require application
    */

You can then add any other local theme-specific requires using addtional ` =require `  statments. Note: to take advantage
of scss variables &etc, instead use the @import directive (not in comments.)

themes_for_rails is configured in an initialization block under ` config/intializers `

Basically it's doing this:

    config.themes_dir = ":root/app/assets/themes"
    config.assets_dir = ":root/app/assets/themes/:name"
    config.themes_routes_dir = "assets"

  Instead of making style sheets, make sass files.

This project uses [themes_for_rails](https://github.com/lucasefe/themes_for_rails) and the 
[rails 3 asset pipeline](http://guides.rubyonrails.org/asset_pipeline.html).

Read the rails guide for more information on the asset pipeline.

Images, Javascripts, and stylesheets for this theme go in `app/assets/themes/<theme-name>/stylesheets/*.sass`
The file `app/assets/themes/<theme-name>/stylesheets/application.sass` should include the 'main' stylesheet references.

    /*
    * =require application
    */

You can then add any other local theme-specific requires using addtional ` =require `  statments. Note: to take advantage
of scss variables &etc, instead use the @import directive (not in comments.)

themes_for_rails is configured in an initialization block under ` config/intializers `

Basically it's doing this:

    config.themes_dir = ":root/app/assets/themes"
    config.assets_dir = ":root/app/assets/themes/:name"
    config.themes_routes_dir = "assets"

  #main
  %h3= "#{APP_CONFIG[:site_name]}: Technical Documentation"
  = @readme.html
body {
  padding: 5px 20px 5px 20px;
  background: {
    image: image-url("rites-bg.jpg");
    repeat: repeat; };
  margin: 10px {
    bottom: 0px; }; }

#main {
  background-color: #f2f8fc;
  color: #00233a;
  border: 1px solid;
  display: inline;
  float: left;
  padding: 10px;
  height: auto;
  margin-right: 0;
  min-height: 600px;
  width: 900px; }

h1 {
  font-size: 170%;
  border-top: 4px solid #aaaaaa;
  padding-top: 0.5em;
  margin-top: 1.5em;
  &:first-child {
    margin-top: 0;
    padding-top: 0.25em;
    border-top: none; } }

h2 {
  font-size: 150%;
  margin-top: 1.5em;
  border-top: 4px solid #e0e0e0;
  padding-top: 0.5em; }

h3 {
  margin-top: 1em; }

p {
  margin: 1em 0;
  line-height: 1.5em; }

ul {
  margin: 1em 0 1em 1.3em;
  margin-top: 0;
  margin-bottom: 0; }

ol {
  margin: 1em 0 1em 1.5em;
  ol {
    margin-top: 0;
    margin-bottom: 0; } }

blockquote {
  margin: 1em 0;
  border-left: 5px solid #dddddd;
  padding-left: 0.6em;
  color: #555555; }

dt {
  font-weight: bold;
  margin-left: 1em; }

dd {
  margin-left: 2em;
  margin-bottom: 1em; }

table {
  margin: 1em 0;
  th {
    border-bottom: 1px solid #bbbbbb;
    padding: 0.2em 1em; }
  td {
    border-bottom: 1px solid #dddddd;
    padding: 0.2em 1em; } }

pre {
  margin: 1em 0;
  font-size: 90%;
  background-color: #f8f8ff;
  border: 1px solid #dedede;
  padding: 0.5em;
  line-height: 1.5em;
  color: #444444;
  overflow: auto;
  code {
    padding: 0;
    font-size: 100%;
    background-color: #f8f8ff;
    border: none; } }

code {
  font-size: 90%;
  background-color: #f8f8ff;
  color: #444444;
  padding: 0 0.2em;
  border: 1px solid #dedede; }

pre.console {
  margin: 1em 0;
  font-size: 90%;
  background-color: black;
  padding: 0.5em;
  line-height: 1.5em;
  color: white;
  code {
    padding: 0;
    font-size: 100%;
    background-color: black;
    border: none;
    color: white; } }
## Gource visualization of work on the application

[Gource](https://github.com/acaudwell/Gource) is a C++ OpenGL application that interactively renders a visualization showing how developers interact with source code in a repository over time.

Here's a 4 1/2 minute [Gource](https://github.com/acaudwell/Gource) visualization of 5777 commits (over 2 1/2 years) to this codebase.

<iframe width="560" height="345" src="http://www.youtube.com/embed/AFrLpHRRgv8" frameborder="0"><a href="http://www.youtube.com/watch?v=AFrLpHRRgv8">Jan 27, 2009 ... Sep 3, 2011</a></iframe>

What's happening in the visualization ...

- The connections between active directories are represented by splines, colored by the contents of the directories they connect to. 
- When directories and files have not been modified for some time they slowly fade from view.
- Files are represented as colored spheres (the color generated by a hash of the file extension) which are laid out in a spiral pattern around the center of the directory the files belong to.
- Developers who are currently contributing to the project are floating near the files they are modifying.
- Developers illuminate the file they are modifying with colored beams: (green adding, orange modifying, red deleting).

### Installing Gource on a Mac with [Homebrew](http://mxcl.github.com/homebrew/):

    brew install gource

### Install [ffmpeg](http://ffmpeg.org/) if you want to be able to generate movies from the Gource visualizations:

*Basic ffmpeg install plus mpeg4 and webm codecs:*

    brew install x264 libvpx ffmpeg

*Complete ffmpeg install (if you want to use ffmpeg for all-around general transcoding and processing):*

    brew install x264 libvpx faac theora libvorbis libogg libogg xvid ffmpeg

### Creating a Gource Visualization

Create a local cache of gravatar images of the developers in .git/avatar http://code.google.com/p/gource/wiki/GravatarExample

From the root directory of this application:

    $ perl docs/gource/get_gravatar_images.pl

To interactively play with a gource visualization (hiding the directories in vendor and public/javascript/):

    $ ./docs/gource/interactive.sh

See: the [Gource readme](http://github.com/acaudwell/Gource/blob/master/README) for more information about these parameters and the commands available while the rendering is running.

Generating an mpeg4 video of the gource output (*ffmpeg required*):

    $ ./docs/gource/generate-mp4.sh

Generating an webm video of the gource output (*ffmpeg required*):

    $ ./docs/gource/generate-webm.sh


Running bundle posting load tests on rails-portal running in production mode.

Install httperf with your favorite package manager (mine is brew):

    $ brew install httperf

screencast on Rack and Metal in Rails 2.3:

* http://railslab.newrelic.com/2009/06/05/episode-14-rack-metal

load-testing and httperf references:

* http://railslab.newrelic.com/2009/06/23/episode-15-load-testing-part-1
* http://railslab.newrelic.com/2009/06/23/episode-16-load-testing-part-2
* http://www.comlore.com/httperf/httperf-quickstart-guide.pdf

Blog post and github repo for generating load tests for httperf from server logs:

* http://www.igvita.com/2008/09/30/load-testing-with-log-replay/
* https://github.com/igrigorik/autoperf

## Setup xproject.local as an apache virtual host to run the rails-portal

I use a reverse proxy below because I use Passenger with Ruby 1.9.2 and the rails-portal runs on Ruby 1.8.7.

Add to /etc/hosts:

    127.0.0.1       xproject.local

Add to: /etc/apache2/extra/httpd-vhosts.conf

    # Proxying to passenger-standalone running under Ruby 1.8.7                                                                                                                                             
    # http://blog.phusion.nl/2010/09/21/phusion-passenger-running-multiple-ruby-versions/                                                                                                                   
    # /Users/stephen/dev/test/xproject-git                                                                                                                                                                  
    # passenger start -a 127.0.0.1 -p 3003 -d                                                                                                                                                               

    <VirtualHost xproject.local:80>
       ServerName xproject.local
       DocumentRoot /Users/stephen/dev/test/xproject-git/public
       PassengerEnabled off
       AllowEncodedSlashes On
       ProxyRequests Off
       KeepAlive Off
       <Proxy *>
          Order deny,allow
          Allow from all
       </Proxy>
       ProxyPass / http://127.0.0.1:3003/  retry=0
       ProxyPassReverse / http://127.0.0.1:3003/
       ErrorLog "/Users/stephen/dev/test/xproject-git/log/assessments.localhost-error_log"
       CustomLog "/Users/stephen/dev/test/xproject-git/log/assessments.localhost-access_log" common
    </VirtualHost>
  
    # after making changes ...                                                                                                                                                                              
    # testing the config: apachectl configtest                                                                                                                                                              
    # restarting apache: sudo apachectl restart                                                                                                                                                             
    # or tailing the general apache2 error log                                                                                                                                                              
    # tail -n 200 -f /var/log/apache2/error_log

Test the apache config and restart.

Start passenger stand-alone in production mode on port 3003:

    $ cd xproject
    $ passenger start -e production -a 127.0.0.1 -p 3003 -d

Confirm that the app is responding: http://xproject.local/

We'll be adding a bunch of records into the database, save a dump of your current database into db/development_data.sql to easily restore the initial state:

    $ rake db:dump

Check to see how many Dataservice::BundleContent models you are starting with:

    $ bin/rails runner "puts Dataservice::BundleContent.count"
    => 2

cd to the httperf dir:

    $ cd benchmarks/httperf

Check the os settings for maximum number of open files -- httperf uses select() and uses a new file descriptor for each connection it opens concurrently. I was getting this warning running httperf:

    httperf: warning: open file limit > FD_SETSIZE; limiting max. # of open files to FD_SETSIZE

On my Mac the maximum open files descriptors was set to 256

    $ ulimit -acore 
    file size          (blocks, -c) 0
    data seg size           (kbytes, -d) unlimited
    file size               (blocks, -f) unlimited
    max locked memory       (kbytes, -l) unlimited
    max memory size         (kbytes, -m) unlimited
    open files                      (-n) 256
    pipe size            (512 bytes, -p) 1
    stack size              (kbytes, -s) 8192
    cpu time               (seconds, -t) unlimited
    max user processes              (-u) 266
    virtual memory          (kbytes, -v) unlimited

Increase the maximum number of file descriptors to 1024:

    $ ulimit -n 1024



    curl -i --header "Content-Type: application/xml" --header "Content-Encoding: b64gzip" --header "Content-md5: 2f90a99d87961e3ffdf585cd0c523b42 --cookie _rails_portal_session=520923139d1eb51aea3715a82ad94cba; --data @curl-data/dataservice_bundle_loggers_1_bundle_contents.bundle.med.txt" http://xproject3.local/dataservice/bundle_loggers/1/bundle_contents.bundle


This measures the time to post 100 OTrunk session bundles:

    $ httperf --hog --server xproject.local --add-header="Content-Type: application/xml\nContent-Encoding: b64gzip\nContent-md5: 2f90a99d87961e3ffdf585cd0c523b42\n" --wsesslog 100,0,sessions/dataservice_bundle_loggers_1_bundle_contents.bundle.med.txt

The results running both httperf and the rails-portal server on the same machine:

    Maximum connect burst length: 1

    Total: connections 100 requests 100 replies 100 test-duration 23.803 s

    Connection rate: 4.2 conn/s (238.0 ms/conn, <=2 concurrent connections)
    Connection time [ms]: min 76.6 avg 238.0 max 930.9 median 326.5 stddev 142.6
    Connection time [ms]: connect 0.1
    Connection length [replies/conn]: 1.000

    Request rate: 4.2 req/s (238.0 ms/req)
    Request size [B]: 7192.0

    Reply rate [replies/s]: min 4.2 avg 4.3 max 4.4 stddev 0.1 (4 samples)
    Reply time [ms]: response 237.9 transfer 0.0
    Reply size [B]: header 357.0 content 0.0 footer 0.0 (total 357.0)
    Reply status: 1xx=0 2xx=100 3xx=0 4xx=0 5xx=0

    CPU time [s]: user 4.77 system 18.97 (user 20.0% system 79.7% total 99.7%)
    Net I/O: 31.0 KB/s (0.3*10^6 bps)

    Errors: total 0 client-timo 0 socket-timo 0 connrefused 0 connreset 0
    Errors: fd-unavail 0 addrunavail 0 ftab-full 0 other 0

    Session rate [sess/s]: min 4.20 avg 4.20 max 4.40 stddev 0.12 (100/100)
    Session: avg 1.00 connections/session
    Session lifetime [s]: 0.2
    Session failtime [s]: 0.0
    Session length histogram: 0 100

If you ran the previous test once you should have 100 more Dataservice::BundleContent models than you starting with:

    $ bin/rails runner "puts Dataservice::BundleContent.count"
    => 102

When you are done restore the previous state of the database:

    $ rake db:load

JRuby is about 33% times faster running this test than MRI Ruby v1.8.7

Install and setup JRuby for running the rails-portal:

    $ rvm install jruby-head
    $ rvm use jruby-head
    $ rvm use gemset global
    $ gem install ruby-debug bundler
    $ rvm use jruby@xproject
    $ bundle install

Start the server in production mode using mongrel:

    $ script/server -e production

Run the same bundle post tests specifying localhost as the server and port 3000:

    $ httperf --hog --server localhost --port 3000 --add-header="Content-Type: application/xml\nContent-Encoding: b64gzip\nContent-md5: 2f90a99d87961e3ffdf585cd0c523b42\n" --wsesslog 100,0,sessions/dataservice_bundle_loggers_1_bundle_contents.bundle.med.txt

JRuby starts at about 5 bundle posts a second but after warming up hotspot by the third run of httperf the rate is up to 9.9:

    Maximum connect burst length: 1

    Total: connections 100 requests 100 replies 100 test-duration 11.087 s

    Connection rate: 9.0 conn/s (110.9 ms/conn, <=2 concurrent connections)
    Connection time [ms]: min 91.4 avg 110.9 max 527.8 median 105.5 stddev 42.9
    Connection time [ms]: connect 0.2
    Connection length [replies/conn]: 1.000

    Request rate: 9.0 req/s (110.9 ms/req)
    Request size [B]: 7187.0

    Reply rate [replies/s]: min 8.4 avg 8.9 max 9.4 stddev 0.7 (2 samples)
    Reply time [ms]: response 110.5 transfer 0.2
    Reply size [B]: header 216.0 content 0.0 footer 0.0 (total 216.0)
    Reply status: 1xx=0 2xx=100 3xx=0 4xx=0 5xx=0

    CPU time [s]: user 2.23 system 8.76 (user 20.1% system 79.0% total 99.1%)
    Net I/O: 65.2 KB/s (0.5*10^6 bps)

    Errors: total 0 client-timo 0 socket-timo 0 connrefused 0 connreset 0
    Errors: fd-unavail 0 addrunavail 0 ftab-full 0 other 0

    Session rate [sess/s]: min 8.40 avg 9.02 max 9.40 stddev 0.71 (100/100)
    Session: avg 1.00 connections/session
    Session lifetime [s]: 0.1
    Session failtime [s]: 0.0
    Session length histogram: 0 100

If instead you start the server with JRuby with hotspot optimized for server operation:

        $ jruby --server script/server -e production

After running the httperf test several times the server is now processing bundle posts at over 11/s:

    Maximum connect burst length: 1

    Total: connections 100 requests 100 replies 100 test-duration 9.031 s

    Connection rate: 11.1 conn/s (90.3 ms/conn, <=2 concurrent connections)
    Connection time [ms]: min 79.5 avg 90.3 max 134.3 median 89.5 stddev 7.1
    Connection time [ms]: connect 0.1
    Connection length [replies/conn]: 1.000

    Request rate: 11.1 req/s (90.3 ms/req)
    Request size [B]: 7187.0

    Reply rate [replies/s]: min 10.8 avg 10.8 max 10.8 stddev 0.0 (1 samples)
    Reply time [ms]: response 90.0 transfer 0.2
    Reply size [B]: header 216.0 content 0.0 footer 0.0 (total 216.0)
    Reply status: 1xx=0 2xx=100 3xx=0 4xx=0 5xx=0

    CPU time [s]: user 1.82 system 7.19 (user 20.2% system 79.6% total 99.8%)
    Net I/O: 80.0 KB/s (0.7*10^6 bps)

    Errors: total 0 client-timo 0 socket-timo 0 connrefused 0 connreset 0
    Errors: fd-unavail 0 addrunavail 0 ftab-full 0 other 0

    Session rate [sess/s]: min 10.80 avg 11.07 max 10.80 stddev 0.00 (100/100)
    Session: avg 1.00 connections/session
    Session lifetime [s]: 0.1
    Session failtime [s]: 0.0
    Session length histogram: 0 100
    This is a customized docker image for running logstash.
It is based on the official logstash image just with the configuration
changed.

It reads data from a mysql database and outputs it to either a local ES
or a Amazon ES instance.

There are three configuration files.
logstash.conf - this contains the mysql input config and the filter config
logstash-output.conf - this contains the aws elasticsearch output config
logstash-output-dev.conf - this contains the local elasticsearch output config

logstash.conf and logstash-output.conf are built into image made by the Dockerfile.
The docker-compose file at the top level of this repo then overrides logstash-output
when docker-compose is used to run this locally.

The config files uses these environment variables:

DB_HOST - portal database hostname
DB_PORT - portal database port default 3306
DB_NAME - portal database name
DB_USER - portal database user
DB_PASSWORD - portal database password
ES_HOST - hostname of the elasticsearch domain
AWS_REGION - aws region of the aws es server
Files in this directory are automatically generated from your plugins.
They are copied from the 'assets' directories of each plugin into this directory
each time Rails starts (script/server, script/console... and so on).
Any edits you make will NOT persist across the next server restart; instead you
should edit the files within the <plugin_name>/assets/ directory itself.
this is the default directory for saving locally cached jar filesActsAsReplicatable
==================

Specify this act if you want to be able to replicate models from one instance of this web application to another.
But ... so far all this plugin does is create and save a uuid for model instances.

Example
=======

You need to add a uuid attribute (string, limit=36) to the models you use this plugin with.

  t.column :uuid, :string, :limit => 36

Then in the model definition add:

  acts_as_replicatable

Copyright (c) 2008 Concord Consortium, released under the MIT license
Written by Stephen Bannasch= Deep Cloning Plugin

This has been modified quite a bit by the Concord Consortium

This plugin gives every ActiveRecord::Base object the possibility to do a deep clone.

The original repository is on github: http://github.com/DefV/deep_cloning

There used to be a nice set of tests that came with the plugin but they haven't been runnable
in a long time so they have been removed. There is some tests in specs/models/deep_cloning_spec.rb

== Example

=== Cloning a model without an attribute
   pirate.clone :except => :name
 
=== Cloning a model without multiple attributes
   pirate.clone :except => [:name, :nick_name]
=== Cloning one single association
   pirate.clone :include => :mateys

=== Cloning multiple associations
   pirate.clone :include => [:mateys, :treasures]

=== Cloning really deep
   pirate.clone :include => {:treasures => :gold_pieces}

=== Cloning really deep with multiple associations
   pirate.clone :include => [:mateys, {:treasures => :gold_pieces}]
Copyright (c) 2008 Jan De Poorter, released under the MIT license
# IcoMoon Font/Icons

We use IcoMoon font files for rendering various icons (e.g. arrows, checkmarks, social media logos, etc.).

Icon glyphs are applied to HTML elements by using classes with corresponding CSS rules.

Example: <p><i class="icon icon-email"></i> Email</p>

CSS rules and class names for icons are specified in /app/assets/stylesheets/web/app.scss.

## Adding Icons

To add new icons to the IcoMoon font files, use the IcoMoon app at icomoon.io/app.

First, create a project, then import icomoon.svg using the Import Icons button and select all the icons imported.

Next, add additional icons by selecting from the default IcoMoon set or importing custom icons in SVG format.

Finally, download the font package and update the icomoon font files in /app/assets/fonts
Use this README file to introduce your application and point to useful places in the API for learning more.
Run "rake doc:app" to generate API documentation for your models, controllers, helpers, and libraries.
