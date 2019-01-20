# Ionicons


The premium icon font for [Ionic](http://ionicframework.com/). Designed by [@benjsperry](https://twitter.com/benjsperry).

Note: All brand icons are trademarks of their respective owners. The use of these trademarks does not indicate endorsement of the trademark holder by Drifty, nor vice versa.

Visit [ionicons.com](http://ionicons.com) and  check out the search feature, which has keywords identifying common icon names and styles. For example, if you search for “arrow” we call up every icon that could possibly be used as an arrow. We’ve also included each icon’s class name for easy copy/pasting when you’re developing!

We intend for this icon pack to be used with [Ionic](http://ionicframework.com/), but it’s by no means limited to it. Use them wherever you see fit, personal or commercial. They are free to use and licensed under [MIT](http://opensource.org/licenses/MIT).


## Getting Started

 1. Download and extract the font pack
 2. Copy the `ionicons.css` to your project
 3. Copy the `fonts` folder to your project
 4. Ensure the font urls within `ionicons.css` properly reference the `fonts` path within your project.
 5. Include a reference to the `ionicons.css` file from every webpage you need to use it.

Or install with [component](https://github.com/component/component):

    $ component install driftyco/ionicons
    
Or perhaps you're known to use [bower](http://bower.io/)?
   
    $ bower install ionicons


## HTML Example

You can use [ionicons.com](http://ionicons.com) to easily find the icon you want to use. Once you've copied the desired icon's CSS classname, simply add the `icon` and icon's classname, such as `ion-home` to an HTML element.

    <i class="icon ion-home"></i>


## Build Instructions

This repo already comes with all the files built and ready to go, but can also build the fonts from the source. Requires Python, FontForge and Sass:

1) Install FontForge, which is the program that creates the font files from the SVG files:

    $ brew install fontforge ttfautohint

2) Install [Sass](http://sass-lang.com/)

    $ gem install sass

3) Add or subtract files from the `src/` folder you'd like to be apart of the font files.

4) Modify any settings in the `builder/manifest.json` file. You can change the name of the font-family and CSS classname prefix.

5) Run the build command:

    python ./builder/generate.py


## License

Ionicons is licensed under the [MIT license](http://opensource.org/licenses/MIT).
Acceptance Tests
==============

Chime supports basic acceptance tests. Acceptance tests use
[fabric](https://fabric-docs.readthedocs.org) and
[selenium](https://selenium-python.readthedocs.org/)'s Firefox driver.

The simplest way to run an acceptance test is to run `fab test_chime`.

### Requirements:

**AWS IAM Setup**:

In order to run these acceptance tests, you are first going to have to
get setup on Amazon with an [IAM account](http://aws.amazon.com/iam/):

1. Create an IAM and generate a key. This should give you values to use
  to fill in the required `AWS_ACCESS_KEY` and `AWS_SECRET_KEY`
  environmental variables below.
2. Ensure either that the user or a group the user belongs to has
  `AmazonEC2FullAccess`.
3. Create a keypair and download the .pem file. This is essentially
  interchangable with an .id-rsa file. After you download the file,
  make sure that SSH can discover it, or manually set fabric to use
  it by setting the `SSH_PRIVATE_KEY_PATH` below.

**Environmental Variables for Fabric**:

+ `AWS_ACCESS_KEY`: The access ID that accompanies your Amazon IAM
  account.
+ `AWS_SECRET_KEY`: The secret key that accompanies your Amazon IAM
  account.
+ `EC2_KEY_PAIR`: The name of the keypair on AWS. This defaults to
  'cfa-chime-keypair'
+ `AWS_SECURITY_GROUPS`: The name of your AWS Security Group. This
  defaults to 'default'
+ `SSH_PRIVATE_KEY_PATH`: This is optional. If you haven't added
  all of your keys via [ssh-add](http://linux.die.net/man/1/ssh-add)
  or another way of configuring SSH, you can use this variable to 
  describe the absolute location of the SSH keypair that you are using
  to connect to EC2.

**Environmental Variables for Acceptance Tests**:

+ `TESTING_EMAIL`: Your persona email.
+ `TESTING_PASSWORD`: Your persona password.

**Python libraries**:

+ Fabric and selenium must be installed:
  `pip install -r fabfile/requirements.txt`

**Other**:

+ [Firefox](https://www.mozilla.org/en-US/firefox/new/)

### Available fab commands

More information about any individual fab command can be viewed by
running `fab -d <command>`. You can view all fab commands with `fab -l`

+ `fab spawn_instance`: Creates a new EC2 instance and writes the
  public DNS to the hosts.txt file.
+ `fab despawn_instance`: Destroys an EC2 instance. Takes an optional
 DNS argument. If no argument is given, it will use the DNS found in
 the hosts.txt file.
+ `fab boot`: Spawns a new EC2 instance, writes the DNS to the
  hosts.txt file, and then installs the necessary requirements to start
  Chime running on the new instance. This can only deploy the master
  branch.
+ `fab test_chime`: Spawns a new EC2 instance, installs Chime, runs the
  tests found in `./test/acceptance`, and then terminates the instance.
  Takes three arguments: setup, despawn, and branch (Example:
  `fab test_chime:setup=f,despawn=f`):
    + setup: Flag for running the setup scraccipts on the instance.
      Defaults to True. NOTE: passing any value that is not True,
      true, t, or y will cause the setup script not to run.
    + despawn: Flag for despawning the instance after the tests pass.
      Defaults to True. NOTE: passing any value that is not True, true,
      t, or y will keep the instance around.
    + branch: Takes a string of a branch name. If provided, it will
      attempt to checkout to that branch before running the tests.

**Testing Locally**

To run acceptance tests locally:

+ Download and install the [ChromeDriver tool](https://sites.google.com/a/chromium.org/chromedriver/)
+ Start the application running with **ACCEPTANCE_TEST_MODE** set to **True**: `env ACCEPTANCE_TEST_MODE=True foreman run python run.py`
+ Make sure the address in `hosts.txt` is that of your local server, i.e. `127.0.0.1:5000`
+ Run the acceptance tests with test email and password env variables: `env TESTING_EMAIL='erica@example.com' TESTING_PASSWORD='12345' nosetests test/acceptance/`
Jekyll Install
=============

This is our installation of jekyll, which we use to preview and render
pages. Eventually this should happen automatically, but for now there's
a manual process to get it set up for development. This assumes rbenv
for managing ruby versions, but if you already have rvm, go ahead and
keep using that. (You can't use both; they conflict.)

It goes something like this:

* Install rbenv
  + Ubuntu: `apt-get install rbenv`
  + MacOS: `brew install rbenv ruby-build` or `brew upgrade rbenv ruby-build` (using [Homebrew](http://brew.sh/))
* activate rbenv temporarily or permanently
  + temporary: `eval "$(rbenv init -)"`
  + permanent: `echo 'eval "$(rbenv init -)"' >> ~/.bash_profile` (restart shell after)
* Install rvm-download
  + `git clone https://github.com/garnieretienne/rvm-download.git ~/.rbenv/plugins/rvm-download`
* Install and use the right ruby
  + `rbenv download 2.2.0`
  + `rbenv shell 2.2.0`
* Install bundler
  + `gem install bundler`
  + `rbenv rehash`
* Install the gems (using the *Gemfile* in the *jekyll/* directory)
  + `cd jekyll`
  + `bundle install`
  + `rbenv rehash`
* Check jekyll
  + `cd ..`
  + `jekyll/run-jekyll.sh --help`
  + Should produce the jekyll help, not error messages



