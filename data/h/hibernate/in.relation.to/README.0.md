# Importing in.relation.to

The scripts in this directory allow you to create required input files to migrate
the exiting in.relation.to blog to awestruct.
The scripts will crawl the site and save all *.lace urls into a Ruby PStore.
From there erb files for the awestruct site can be created. Besides of this the scripts
generate a input file to migrate comments to Disqus as well as redirect files for
old to new URLs.

## How to run the scripts

### Quickstart

    # install bundler
    > gem install bundler

    # get your dependencies via bundler
    > bundle install

    # run the crawler
    > bundle exec ./crawler.rb -u http://in.relation.to -p ".*\.lace" -o posts.pstore | tee crawl.log

    # run the importer (creates erb files, Apache redirects and Disqus WXR import file)
    > bundle exec ./importer.rb -s posts.pstore -o ../posts -rf ../redirects/.htaccess_posts -wxr wxr.xml

    # for experiments when you don't want to download images (-ni) and assets (-na)
    > bundle exec ./importer.rb -s posts.pstore -o ../posts -ni -na


### Crawling in.relation.to

That's the first step in the in.relation.to migration. We crawl the site to extract
the HTML for the blog posts and use it to run through an importer to create the
awestruct files. The data is stored in a [PStore](http://ruby-doc.org/stdlib-2.1.2/libdoc/pstore/rdoc/PStore.html) file.

    > bundle exec ./crawler.rb -u http://in.relation.to -p ".*\.lace" -o posts.pstore | tee crawl.log

The version used for creating the awestruct site is added to this directory and
called [posts.pstore.bz2](./posts.pstore.bz2). It is BZIP2 compressed and can be
uncompressed via

    > bunzip2 posts.pstore.bz2

### Creating ERB files

Once you have the PStore file you can run the importer to create the [ERB](http://www.stuartellis.eu/articles/erb/) files. Using ERB we can keep the original HTML and don't
have to parse it to for example create Markdown.

    > bundle exec ./importer.rb -s posts.pstore -o ../posts

### Creating Disqus WXR import file

Blog comments are also part of the data stored in the PStore file. The comments can be extracted into a XML file which is suited for
[importing into Disqus](https://help.disqus.com/customer/portal/articles/472150-custom-xml-import-format).

    > bundle exec ./importer.rb -s posts.pstore -o ../posts -wxr wxr.xml -e

#### Disqus

Some information around Disqus.

* The JavaScript needed to integrate Disqus is described here - https://help.disqus.com/customer/portal/articles/472097-universal-embed-code
* Import of the generated WXR XML file is via https://\<disqus-id\>.disqus.com/admin/discussions/import/platform/wordpress/, where `disqus-id` is the unique identifier
used to integrate the Disqus threads into the blog posts. The `disqus-id` is configured
in `_config/site.yml` and must match the one generated via the Disqus admin tool.
* Imports can be checked after the completed under the URL - https://import.disqus.com.
* Under https://\<disqus-id\>.disqus.com/admin/settings/advanced/ the trusted domains need to be configured. The entry should look like:

        in.relation.to
        staging.in.relation.to
        localhost

### Creating Apache re-directs

The scripts also generates redirect instructions for Apache to map old URLs to new ones.
There are three parts to this (all these fragments are committed under "redirects"):

* Redirects for blog posts and tags; Generated by importer.rb:

    > bundle exec ./importer.rb -s posts.pstore -o ../posts -rf ../redirects/.htaccess_posts

* Redirects for blogger homes; Generated by user_redirect_creator.rb:

    > bundle exec ./user_redirect_creator.rb -s users.pstore -o ../redirects/.htaccess_bloggers

* Additional manually created redirects in ../redirects/.htaccess_misc

To merge the fragments into one .htaccess or include file for the main HTTPD config run:

    > cat ../redirects/.htaccess_misc ../redirects/.htaccess_bloggers ../redirects/.htaccess_posts > .htaccess

The users.pstore file used for creating the awestruct site is added to this directory and
called [users.pstore.bz2](./users.pstore.bz2). It is BZIP2 compressed and can be
uncompressed via

    > bunzip2 users.pstore.bz2

To re-create the file from the existing blog, run the crawler like so:

    bundle exec ./crawler.rb -u "http://in.relation.to/Bloggers/Ales, \
    http://in.relation.to/Bloggers/Aslak, \
    http://in.relation.to/Bloggers/Brett, \
    http://in.relation.to/Bloggers/Christian, \
    http://in.relation.to/Bloggers/Dan, \
    http://in.relation.to/Bloggers/Daniel, \
    http://in.relation.to/Bloggers/David, \
    http://in.relation.to/Bloggers/Davide, \
    http://in.relation.to/Bloggers/Emmanuel, \
    http://in.relation.to/Bloggers/Gail, \
    http://in.relation.to/Bloggers/Gavin, \
    http://in.relation.to/Bloggers/Gleb, \
    http://in.relation.to/Bloggers/Greg, \
    http://in.relation.to/Bloggers/Gunnar, \
    http://in.relation.to/Bloggers/Hardy, \
    http://in.relation.to/Bloggers/Ilya, \
    http://in.relation.to/Bloggers/Jason, \
    http://in.relation.to/Bloggers/JasonP, \
    http://in.relation.to/Bloggers/Jay, \
    http://in.relation.to/Bloggers/Jesper, \
    http://in.relation.to/Bloggers/John, \
    http://in.relation.to/Bloggers/Jozef, \
    http://in.relation.to/Bloggers/Ken, \
    http://in.relation.to/Bloggers/Lincoln, \
    http://in.relation.to/Bloggers/Luksa, \
    http://in.relation.to/Bloggers/Marek, \
    http://in.relation.to/Bloggers/Marius, \
    http://in.relation.to/Bloggers/Marko, \
    http://in.relation.to/Bloggers/Martin, \
    http://in.relation.to/Bloggers/Max, \
    http://in.relation.to/Bloggers/Michael, \
    http://in.relation.to/Bloggers/Nicklas, \
    http://in.relation.to/Bloggers/Norman, \
    http://in.relation.to/Bloggers/Pete, \
    http://in.relation.to/Bloggers/Robb, \
    http://in.relation.to/Bloggers/Sanne, \
    http://in.relation.to/Bloggers/Scott, \
    http://in.relation.to/Bloggers/Sergey, \
    http://in.relation.to/Bloggers/Shane, \
    http://in.relation.to/Bloggers/Snjezana, \
    http://in.relation.to/Bloggers/Steve, \
    http://in.relation.to/Bloggers/StrongLiu, \
    http://in.relation.to/Bloggers/Stuart, \
    http://in.relation.to/Bloggers/Tihomir" \
    -p ".*" -o users.pstore -d 0

## Tips & Tricks

* To nicely format the generated WXR XML file you can use

        xmllint --format --recover <export-file-name>.xml

* When experimenting with the importer it is often nice to start from a clean state. Just run to reset your checkout:

        git clean -f -d

* To list all available script options use '-h'

        > ./crawler.rb -h
        Usage: crawler.rb [-upoh]
        Application options:
        Required:
          -u, --url=<file>                 The base url
          -p, --pattern=<regexp>           Regular expression to limit the discovered pages
          -o, --out=<file>                 The name of the output-file
        Common:
          -h, --help                       Show this message.

        > ./importer.rb -h
        Usage: importer.rb [-sorfwxrelnninah]
        Application options:

            -s, --store=<file>               The PStore file containing the spidered HTML
            -o, --out=<dir>                  The name of the output directory

           -rf, --redirects-file=<file>      The name of file to which write HTTP redirect rules
          -wxr, --wxr-export-file=<file>     The name of WXR XML file. If specified comments are exported, otherwise not

            -e, --log-errors                 Whether failed imports should be logged with stacktrace
            -l, --lace=<lace-url>            Runs the importer only for the given lace url
            -n, --limit=<n>                  Limit the imported posts (for debugging purposes)
           -ni, --no-images                  Wether image processing should be skipped
           -na, --no-assets                  Wether asset processing should be skipped

            -h, --help                       Show this message.

## Resources

* [Bundler](http://gembundler.com/)
*  If you see the error message below:

        incompatible character encodings: ASCII-8BIT and UTF-8

   You might be dealing with [encoding problems](http://talk-archive.awestruct.org/Stumbling-onto-an-encoding-problem-right-from-the-start-td39.html)

When making changes to the redirect rules or other Apache HTTPD configuration files,
these are not applied automatically by the Jenkins build job which
normally publishes new blog posts.

You have to invoke the deploy script to upload and restart HTTPD:

 > source ./deploy.sh

You can invoke this locally - from your workstation - but it assumes
that you have SSH console credentials in place to get a shell on `ci.hibernate.org`.

Your private key needs to be used in combination with user "ec2-user".

A typical .ssh/config file would look like:

Host ci.hibernate.org
   User ec2-user
   VerifyHostKeyDNS no
   IdentityFile ~/.ssh/id_rsa # Possibly change to your key!
   IdentitiesOnly yes
   AddressFamily inet
   Compression yes
   ForwardAgent no
   ForwardX11 no
= Running in.relation.to within Docker
:toc:
:toc-placement: preamble

The following instructions allow you to run in.relation.to within
a docker container while still being able to edit your sources locally.
This is not a Docker introduction. At least you will need a running
Docker daemon. If you want an intro into Docker - link:http://docs.docker.com/[start here].

== The short version

The short version. If you are lucky all you need is:

[source]
----
> cd docker
> docker build -t hibernate/in.relation.to .
> docker run -t -i -p 4242:4242 -v `pwd | xargs dirname`:/home/dev/in.relation.to hibernate/in.relation.to
----

Once you have a bash into the running container you can use the various Rake task to
drive awestruct.

[TIP]
====
The first time you use the Docker approach make sure that you don't have any changes
in your local checkout of in.relation.to, in particular temp files generated by
Bundler. You can for example run `git clean -fxd`, but make sure you have no
outstanding changes.
====

[TIP]
====
On Linux you might need to use _sudo_ to execute docker commands. If you want to
avoid that have a look at link:https://docs.docker.com/installation/ubuntulinux/#create-a-docker-group[create a docker group].
====

[NOTE]
====
`pwd | xargs dirname` tries to determine the full path to the root directory of your
in.relation.to checkout. It assumes you are in the _docker_ sub-directory when you
execute it. If you replace `pwd | xargs dirname` with your specific root directory
path, you can run this command from anywhere.
====

== The long version

=== Building the Docker image

First step is to build the Docker image containing your awestruct setup.
This step could eventually be replaced by a automatically build image made
available via a Docker repository. For now, however, we build this image locally.

[source]
----
> docker build -t hibernate/in.relation.to .
----

Whenever the gem dependencies change, you will need to rebuild the image to make sure
you get a working environment out of the box.

Below you see the used Dockerfile with some comments:

[source]
.Dockerfile for Awestruct setup based on Fedora 22
----
FROM       fedora:22

# install the required dependencies to complile natice extensions
RUN        dnf -y install gcc-c++ make ruby-devel libxml2-devel libxslt-devel findutils git ruby // <1>

RUN        groupadd -r dev && useradd  -g dev -u 1000 dev // <2>
RUN        mkdir -p /home/dev
RUN        chown dev:dev /home/dev

# From here we run everything as dev user
USER       dev

# Setup all the env variables needed for ruby
ENV        HOME /home/dev
ENV        GEM_HOME $HOME/.gems
ENV        GEM_PATH $HOME/.gems
ENV        PATH $PATH:$GEM_HOME/bin
ENV        LC_ALL en_US.UTF-8
ENV        LANG en_US.UTF-8
RUN        mkdir $HOME/.gems

# Install Rake and Bundler for driving the Awestruct build & site
RUN        gem install -N rake bundler

# Clone in.relation.to in order to run the setup task
RUN        git clone https://github.com/hibernate/in.relation.to.git
RUN        cd $HOME/in.relation.to && git checkout production && rake setup

# We need to patch awestruct to make auto generation work. On mounted volumes file
# change montoring will only work with polling
RUN        gem contents awestruct | grep auto.rb | xargs sed -i "s/^\(.*force_polling =\).*/\1 true/" // <4>

EXPOSE     4242
VOLUME     $HOME/in.relation.to
WORKDIR    $HOME/in.relation.to

CMD [ "/bin/bash" ]
----

. Install all dependencies, especially the ones needed to compile native
extensions. After changes to the gem dependencies this might need to be updated.
Otherwise we rely on the default ruby version available via _dnf_.

. In order for the container to be able to modify files in your mounted volume,
we need to make sure that the created _dev_ user gets the same user id as the files
have on the host machine. In many cases 1000 is a good guess, but in case you are
getting file permission errors when running `rake preview` you want to check which
user id the files have when mounted into the container. Use this user id as part of
the `useradd` command and re-build the image.

. We need the checkout to setup the awestruct environment. At runtime the checkout
will be overridden by the mounted volume

. An awestruct hack. Awestruct uses live-reload to determine file changes in order
to trigger re-generation of pages. live-reload allows to configure how changes are
detected, but awestruct does not expose this option. When mounting your checkout as
a volume, the default detection fails (at least on Mac using boot2docker) and polling
needs to be used. This sed command will patch the awestruct version we use. Obviously
this is very fragile to changes in awestruct version

=== Running the container

Once you have your image you can run the docker container and use it to drive your
awestruct site. The site can be previewed under http://localhost:4242 on Linux or
http://<docker-ip>:4242 with boot2docker, where _docker-ip_ can be retrieved via
`boot2docker ip`.

[source]
----
> docker run -t -i -p 4242:4242 -v <path to root directry of in.relation.to checkout>:/home/dev/in.relation.to hibernate/in.relation.to
----


