= How to build and blog on in.relation.to
ifdef::env-github[:outfilesuffix: .adoc]
ifndef::env-github[:outfilesuffix: /]
:toc:
:toc-placement: preamble

A bit of Git, a bit of Ruby and you will get your local in.relation.to served.

== Prerequisites

* Get http://git-scm.com[Git]
* Get https://www.ruby-lang.org/en/[Ruby] > 1.9

== Installation

=== Ensure Rake is installed

Make sure https://github.com/jimweirich/rake[Rake] is available. It is often installed per default.

[source]
----
> rake --version
----

If you get "_command not found_":

[source]
----
> gem install rake
----

=== Ensure Bundler is installed

Make sure http://bundler.io/[Bundler] (version >= 1.10) is available. It manages your Ruby gems
locally to the project and prevents version conflicts between different Ruby projects.
Quoting from the website:

____
Bundler provides a consistent environment for Ruby projects by tracking and installing the exact
gems and versions that are needed.
____

[source]
----
> bundle -v
----

If you get "_command not found_" or a version < 1.10:

[source]
----
> gem install bundler
----

[[get-the-source]]
=== Get the source

[source]
----
> git clone git@github.com:hibernate/in.relation.to.git
> cd in.relation.to
----

[[awestruct-setup]]
=== Setup awestruct

[source]
----
> rake setup
----

=== Serve the site locally

[source]
----
rake preview
----

Point your browser to http://localhost:4242. Per default the site is generated with
the _editor_ profile enabled.
In this profile, posts per tag and author are not
generated and only the last 12 months of blog entries are used.
The main purpose of this mode is to generate a new blog entry.

If you are developing the blog, you might want to use the _development_ profile.
It creates tags and author pages and only considers the last 12 months of blog entries.

[source]
----
rake preview[development]
----

If you want the full site generated for example to see the full list of tags or authors,
you should use:

[source]
----
rake preview[staging]
----

== Write a blog

Blogs are written in http://asciidoctor.org[Asciidoctor].

Create a file in the directory named after you: for example `posts/Emmanuel`.
The file should be named as followed: `yyyy-mm-dd-your-lowercase-dash-separated-slug.adoc`.
For example `2015-06-30-multitenancy-and-current-session.adoc`.

Here is a sample blog template you can start with:

[source]
.An Asciidoctor blog post
....
= Let me tell you about...
Emmanuel Bernard
:awestruct-tags: ["Discussions", "Off topic"]
:awestruct-layout: blog-post

Today let's discuss blogging.

== Metadata

You can see that the metadata is made of:

* the title in the first line: it starts with `=`
* the author in the second line: put your first and lastname
* `awestruct-tags`: a list of tags
* `awestruct-layout`: don't change this one

=== Tags

Here is a curated list of tags that you can look at http://in.relation.to/tags/.
Try to use that list, we do not want tag proliferation.
In particular, the general rule is to have tags representing:

* projects, products and podcasts: e.g. `Hibernate ORM`
* specifications: e.g. `CDI` or `Bean Validation`
* a tag representing a release announcement: `Releases`
* a tag representing conferences, JUGs etc: `Events`
* a tag representing discussions: `Discussions`. This one covers development methods, dev tooling, build, etc.
* a tag representing off topic: `Off topic`

== Headers

Sections of a blog post start at level 2 i.e. `==`.
Level 1 is the blog post title.

== Code samples

Code can be highlighted

[source,java]
----
public class Test {
    public String name;
}
----

== More info

You can read more on the Asciidoctor syntax at http://asciidoctor.org.

Happy blogging.
....

=== Metadata

You can see that the metadata is made of:

* the title in the first line: it starts with `=`
* the author in the second line: put your first and lastname
* `awestruct-tags`: a list of tags
* `awestruct-layout`: don't change this one

==== Tags

Here is a curated list of tags that you can look at http://in.relation.to/tags/.
Try to use that list, we do not want tag proliferation.
In particular, the general rule is to have tags representing:

* projects, products and podcasts: e.g. `Hibernate ORM`
* specifications: e.g. `CDI` or `Bean Validation`
* a tag representing a release announcement: `Releases`
* a tag representing conferences, JUGs etc: `Events`
* a tag representing discussions: `Discussions`. This one covers development methods, dev tooling, build, etc.
* a tag representing off topic: `Off topic`

=== Sections

Sections of a blog post start at level 2 i.e. `==`.
Level 1 is the blog post title.

=== Code samples

Code can be highlighted

[source,java]
----
public class Test {
    public String name;
}
----

=== More info

You can read more on the Asciidoctor syntax at http://asciidoctor.org.

Happy blogging.

== Preview changes on staging.in.relation.to

Use git to push on the _staging_ branch on GitHub.
You might need to use "git push --force" to overwrite previous experiments;
possibly check when doing so to not interfere with someone else also looking to publish a preview.

Pushing on this branch will trigger a build at http://ci.hibernate.org/view/Website/job/staging.in.relation.to/[the CI Server],
if the build is successful your changes should be visible on http://staging.in.relation.to/[the staging website].

== Publish changes to production

Use git to push on the _production_ branch on GitHub.

In this case, never use "--force" !
If you have a push error, please rebase first, and possibly repeat the staging phase.

Also in this case a build is triggered on http://ci.hibernate.org/view/Website/job/in.relation.to/[the CI Server],
and if successful the content is then visible on http://in.relation.to/[the public blog].

[NOTE]
====
If you change any of the `.htaccess` files under `server-config`, you need to execute `deploy.sh`.
Changes will be applied to the CI server.

You need to have access to the CI machine via SSH.
Ask you know who.

More info link:server-config/README[in the server-config readme file].
====

== Tips & Tricks

=== Which other tasks exist in the Rake build file?

[source]
----
> rake -T
> rake -D
----

The '-T' version will list the available tasks with short description whereas the '-D'
version gives the long description.

=== If your changes are not visible...

Panic! Then completely regenerate the site via:

[source]
----
> rake clean preview
----

=== I am getting errors when trying to execute *awestruct* directly

You need to use `bundle exec <command>` to make sure you get all required Gems. Check the *Rakefile*
to see how the different awestruct calls are wrapped.

=== Fedora 22 setup

Make sure the user is in the sudo group and install required dependencies for
compilation of native extensions:

[source]
----
> sudo dnf -y install gcc-c++ make ruby-devel libxml2-devel libxslt-devel
----

[NOTE]
====
This is required regardless how you proceed from here (provided Ruby version ns RVM)
====

==== Using Ruby version provided by the Fedora packages

[source]
----
> sudo dnf -y install ruby
> gem install rake bundler
----

Continue <<get-the-source,here>>

==== Using RVM

How to Integrating RVM with gnome-terminal: http://rvm.io/integration/gnome-terminal

How to install RVM (http://rvm.io/rvm/install)

Install the GPG key:

[source]
----
gpg2 --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
----

Install a stable Ruby version:

[source]
----
curl -sSL https://get.rvm.io | bash -s stable --ruby
git clone in.relation.to
cd in.relation.to
echo "rvm ruby-2.2@global” > .rvmrc
----

Load the .rvmrc file:

[source]
----
cd ../in.relation.to
----

Say yes to .rvmrc execution.

Continue <<awestruct-setup, here>>

=== Bugger that,...

I cannot get the enviroment up and running. Use Docker! Read link:/docker/README{outfilesuffix}[how]!

=== [Linux] Problem with character encodings during execution of awestruct

[source]
----
An error occurred: /in.relation.to/in.relation.to/README.adoc is not valid US-ASCII
----

Make sure you have the right locale set:
[source]
----
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
----

== License

The articles, blog posts and other content of this repository are released under the link:http://creativecommons.org/licenses/by-sa/3.0/[Creative Commons Attribution Share-Alike 3.0 Unported (CC BY-SA 3.0)] license.

All sample code available on these blog posts is released under the link:http://www.apache.org/licenses/LICENSE-2.0.html[Apache Software License 2.0].
All source code available in this repository to build the website is also released under the link:http://www.apache.org/licenses/LICENSE-2.0.html[Apache Software License 2.0].

By submitting a "pull request" or otherwise contributing to this repository, you
agree to license your contribution under the respective licenses mentioned above.

== Acknowledgements

This website uses https://github.com/jbossorg/bootstrap-community[JBoss Community Bootstrap].
