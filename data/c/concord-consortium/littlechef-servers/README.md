To use this repository you need two tools: littlechef and librarian-chef

### Setup your environment

Install littlechef

    pip install littlechef

Configure Ruby

    source ./.rvmrc
    bundle install --binstubs


Run initial librarian install

    librarian-chef install

Setup your .ssh/config file. It needs to know the correct identify file (pem) to use with the servers.
Mine looks like this

	Host *.compute-1.amazonaws.com
	  User ubuntu
	  IdentityFile /Users/scytacki/Development/ec2/genigames.pem

This repository uses a submodule for the data_bags folder. It is a private repository named: chef-databags. If you are permitted to access this repository run this command

    git submodule update --init

### Setup a new Production portal Server ###

0. Setup your environment, as per the direction at the top.
0. Create a new aws config in `aws-config/<projectname>.json`
0. run `bundle exec ./script/create_ec2.rb --stage production --project <project name>`
0. Using the AWS web console, create a DNS entry for your host using Route 53.
0. `echo '{"id": "<projectname>"}' >> data_bags/sites/<projectname>.json`
0. Create the S3 Bins for your project `./script/create_s3_bucket.rb --stage production --project <projectname>`
0. Using the information from the output of the S3 bucket creation script, create a new databag for your site in `data_bags/sites/<projectname>.json`
0. Add `db_username` and `db_password` to `data_bags/sites/<projectname>.json`
0. Create a Roles for your project in `roles/<projectname>.json`, `roles/<projectname>-production.json` and `roles/<projectname>-staging.json`. The roles should include a reference to the rails portal role. See `roles/interactions-portal.json` for example. eg `"role[rails-portal-server]"`.
0. Create the databases for your project `./script/create_db.rb --stage production --project <projectname>`
0. make sure you specify the correct ssh_id and pem file in your
   `.ssh/config` file. Add the following to your ~/.ssh/config file (TODO: we could do this
   in `config.cfg`) :

        Host <project-name>.*.concord.org
          User ubuntu
          IdentityFile ~/.ssh/genigames.pem

0. run fix on your node `fix node:<projectname>.concord.org role:<projectname>-production`
    NOTE: currently this will fail because of the SSL cert files need to manually copied to /etc/apache2/ssl
0. checkout the rigse project, create new entries in `deploy.rb` and add `deploy/<projectname>-staging.rb` and `deploy/<projectname>-production.rb`
0. add a new theme for your project by copying and editing an existing
   theme eg: `cp -r ./app/assets/themes/interactions ./app/assets/themes/newthemename` and `cp -r ./themes/interactions ./themes/newthemename`.  You will also have to modify app.scss to add a new `.project-header h1` background image for your project.
0. Deploy: `bundle exec cap projectname-production deploy`
0. Setup the default project: `bundle exec cap projectname-production setup:init_database`
0. OPTIONAL: Load in some NCES districts.
  0. Check config/settings.yml, add or remove states from the entry "states_and_provinces:" (all is valid) 
     NOTE: `config/settings.yml` is managed by chef and is usually specificed in the roles/<projectname>.json
  0. Run the cap task to setup districts (this will take a while if you use 'all' or have a lot of states): `bundle exec cap <site> setup:districts`
  0. TBD: You might consider using a mysql databse dump of just the
     district data, using 'Sequel Pro' and the included
0140425portal-districts-and-schools.sql.zip file (password protected) 
0. Run the cap task `bundle exec cap <site> solr:hard_reindex` to get the solr
   materials listings to work.
0. Create a SSO client for LARA: ssh to server and run `RAILS_ENV=production bundle exec rake sso:add_client`
0. Add the client_id and secret to `data_bags/sites/lara.json`, follow the pattern there
0. This might be a good time to create a new staging server (maybe)
   using `./script/create_staging.rb --project <project-name>`


### Adding a New Cookbook

There are 2 types of cookbooks supported: cookbooks and site-cookbooks.

*Cookbooks* are managed by librarian-chef. These are pulled from remote source. The source can be a github
repository, or a chef repository

You add a new one by modifying the Chefile so librarian-chef knows about the new cookbook. Then
you run

    librarian-chef install

*Site-cookbooks* are local to this repository. In littlechef terms this "repository" is called a kitchen.
Add a folder to the site-cookbooks folder. The folder needs the standard Chef cookbook format.


### MISC BUGS

Sometimes, I have found (especially when trying to install PhantomJS) an error message returned by
chef like this: `uninitialized constant Chef::Mixin::PowershellOut` and `Recipe Compile Error in /tmp/chef-solo/cookbooks/powershell/libraries/windows_architecture_helper.rb`.

I am not sure why this happens, but the fix for me is to `rm -rf ./cookbooks/powershell` and then `librarian-chef install`.

### TODO

When starting without ruby installed passenger doesn't install correctly because it is using the an ohai
key for the location of ruby: :languages/ruby/ruby_bin, and that won't be configured correctly unless chef
is restarted. A couple of options are to make that be more dynamic, switch to rvm_passenger setup, or change the
bootstrap scripts to build ruby from source

Improve the Indentify file managment. If we are going to use a single kitchen for all of our servers then we'll probably
want to have several pem files, and then all the developers would need to manage the mapping of all of those files.

Fix the way nodejs is installing the apt repository so we don't need to run apt-get update ourselves

Separate out the couchdb from package installation code into its own recipe, look around for other couch
cookbooks to see if anyone wants this as an option.

Make base image that contains the parts that are common when spinning up a new instance or testing code. This ought to
contain:

- chef-solo
- ruby 1.9.3
- apache
- passenger
- git
