Redbox
======

Redbox is a very simple lightbox library, which is a way of display a model popup window which may contain any html, while the rest
of the page is faded out behind it. There are already many such libraries around for this, but:

 - Often they do a little more than I wanted
 - Many of them require a large javascript library that isn't prototype/scriptaculous. While I don't really have an opinion on which library
   is better, prototype is generally the one that we're using for rails, so I wanted a lightbox that took advantage of that,
   rather than forcing me to include another library which might class.
 - Many of them where not compatible with rails' ajax system. I wanted to be able to do multi-page forms within a lightbox,
   using form_remote_tag, or any other means of reloading the lightbox div using ajax.

And of course, I wanted it all packaged as a nice rails plugin with handy helpers to use it. 


Credits
=======

Much of the design, and some of the javascript and css are shamelessly ripped from the Thickbox library, by Cody Lindley. 

This library should be considered to be a derivative work of Thickbox, and is also released under the MIT licence.

http://jquery.com/demo/thickbox/

Redbox Rails plugin development by Craig Ambrose

http://www.craigambrose.com

Additional code submissions, testing and bugfixes by:
- Brandon Keepers
- Niko Dittmann
- Randy Parker
- Julien Coupard
- Erin Staniland
(and many more)

Licence
=======

MIT License

http://www.opensource.org/licenses/mit-license.php

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so.


Usage
=====

Examine the public methods of redbox_helper.rb. They will all look familiar, much like the existing link helpers, except that they work with redboxes. You should not need to interact with the javascript directly.

Redbox provides three helpers which are used instead of a regular “link_to” helper when linking to a redbox.

link_to_redbox(name, id, html_options = {})

This is used if you already have an HTML element in your page (presumably hidden, but it doesn’t have to be) and you wish to use it for your redbox. Specify it by it’s id, and you’re in business.

link_to_component_redbox(name, url_options = {}, html_options = {})

This serves essentially the same purpose, but it uses the url_options supplied to load another page from your app into a hidden div on page load. This saves you having to do it yourself, but beware that there are definite performance implications to using components.

link_to_remote_redbox(name, link_to_remote_options = {}, html_options = {})

This waits until the link is clicked on to load the redbox using ajax, and displays loading graphics while it’s waiting.

link_to_close_redbox(name, html_options = {})

Allows you to put a link (presumably inside the redbox) to close it. Other way to close it is to refresh the entire page, but obviously closing it with javascript is spiffier.

More Info
=========

A static page is maintained for this plugin at:

	http://www.craigambrose.com/projects/redbox

Updates are always posted at:

	http://blog.craigambrose.com
	
Bugs, once you have tracked down the exact problem and can reproduce a failure case, can be reported to:

	craig@craigambrose.com

If you find this plugin useful, you can give something back to the community by examining your own code and seeing
what bits of functionality are generic enough to be useful as a rails plugin. Releasing rails plugins is dead
simple, and helps us all do better work.

DynamicForm
===========

DynamicForm holds a few helpers method to help you deal with your models, they are:

* input(record, method, options = {})
* form(record, options = {})
* error_message_on(object, method, options={})
* error_messages_for(record, options={})

It also adds f.error_messages and f.error_messages_on to your form builders.

Copyright (c) 2010 David Heinemeier Hansson, released under the MIT license
{<img src="https://travis-ci.org/sikachu/verification.png" />}[https://travis-ci.org/sikachu/verification]

This module provides a class-level method for specifying that certain
actions are guarded against being called without certain prerequisites
being met. This is essentially a special kind of before_filter.

An action may be guarded against being invoked without certain request
parameters being set, or without certain session values existing.

When a verification is violated, values may be inserted into the flash, and
a specified redirection is triggered. If no specific action is configured,
verification failures will by default result in a 400 Bad Request response.

Usage:

  class GlobalController < ActionController::Base
    # Prevent the #update_settings action from being invoked unless
    # the 'admin_privileges' request parameter exists. The
    # settings action will be redirected to in current controller
    # if verification fails.
    verify :params => "admin_privileges", :only => :update_post,
           :redirect_to => { :action => "settings" }

    # Disallow a post from being updated if there was no information
    # submitted with the post, and if there is no active post in the
    # session, and if there is no "note" key in the flash. The route
    # named category_url will be redirected to if verification fails.

    verify :params => "post", :session => "post", "flash" => "note",
           :only => :update_post,
           :add_flash => { "alert" => "Failed to create your message" },
           :redirect_to => :category_url

Note that these prerequisites are not business rules. They do not examine
the content of the session or the parameters. That level of validation should
be encapsulated by your domain model or helper methods in the controller.## Expertiza Installation using Docker

### Operating Systems: 

* Mac
* Linux

### Prerequisites:

* [Docker](https://www.docker.com/)
* [Docker-Compose](https://docs.docker.com/compose/install/)
* Make sure that you place the **'scrubbed_db'** in the scrubbed_db folder.
   * Download the scrubbed database from: https://goo.gl/60RnWx


### Installation steps: 

1. Mac:

  * Clone your forked Expertiza github repository: `git clone YOUR_REPO_LINK.git` 
  * Go to the expertiza/docker folder: `cd expertiza/docker`
  * Run the `setup_mac.sh` script : `bash setup_mac.sh`

2. Linux: 

  * Clone your forked Expertiza github repository: `git clone YOUR_REPO_LINK.git` 
  * Go to the expertiza/docker folder: `cd expertiza/docker`
  * Run the `setup_linux.sh` script: `bash setup_linux.sh`

#### After you run the script you need to do the following: 

* You will be required to fill in your MY SQL PASSWORD. Put any password for you MySQL Database.
* After some time open up your browser and go to the `localhost:3000` 
* If you see the following error, it means the script ran successfully and you just need to do the database migration.
![migration_error](https://i.stack.imgur.com/Om4yH.png)

#### Database Migration

* Once you see the above error, open up a new terminal.
* List all the active containers by typing `sudo docker ps -a`
* Look for the CONTAINER ID of the IMAGE `winbobob/expertiza:ruby-2.2.7`
* And run the following command: `sudo docker exec -it <CONTAINER ID> bin/rake db:migrate RAILS_ENV=development`
* For example: 

   ```
   vivekbhat$ sudo docker ps -a 
   CONTAINER ID        IMAGE                           COMMAND                  CREATED             STATUS                        PORTS                    NAMES
   2a63f480521f        winbobob/expertiza:ruby-2.2.7   "bundle exec thin ..."   12 hours ago        Exited (255) 3 hours ago      0.0.0.0:3000->3000/tcp   expertiza_expertiza_1
   017b6688d44c        redis:alpine                    "docker-entrypoint..."   12 hours ago        Exited (255) 3 hours ago      6379/tcp                 expertiza_redis_1
   7c9e5c30de7c        mysql:5.7                       "docker-entrypoint..."   12 hours ago        Exited (255) 3 hours ago      3306/tcp                 expertiza_scrubbed_db_1

   vivekbhat$ sudo docker exec -it 2a63f480521f bin/rake db:migrate RAILS_ENV=development
   ```
* Wait for the program to finish the database migration
* Once completed go to `localhost:3000` and Expertiza should be up and running :) 

## Scrubbed DB Folder

Place the scrubbed_db here

### How to get the scrubbed_db: 

Download the scrubbed database from: https://goo.gl/60RnWx

Use this README file to introduce your application and point to useful places in the API for learning more.
Run "rake doc:app" to generate API documentation for your models, controllers, helpers, and libraries.
