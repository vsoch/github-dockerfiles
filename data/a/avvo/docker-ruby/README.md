# Ruby Docker images from Avvo

These Dockerfiles are used to build docker images we use for various Ruby 
containers at Avvo.

## Development

1. Clone this repo
2. Edit the Dockerfile you want to update
3. Build the image (for instance the `rails-mysql` image): 
   `docker build -t avvo/avvo-rails-mysql:latest .`
4. Push the image: `docker push avvo/avvo-rails-mysql:latest`

Two notes:

a. You need permissions to write the images on dockerhub. If you're not an 
Avvo person, you probably don't have access. You can push it up to your own 
namespace.
b. Test out your changes on a tag before committing and pushing to latest.

## Images
alpine-phantomjs-builder  Dockerfile  rails  rails-5  rails-mysql  
rails-mysql-ci  README.md  ruby  ruby-libv8  ruby-libv8-phantomjs

### rails
An alpine image with ruby included.  Also includes the openssl-dev system 
package for compiling gems/software that uses SSL.

### rails-mysql
Same as rails, but includes mariadb-dev instead of openssl-dev

### rails-mysql-ci
Uses rails-mysql as the base, and includes aspell, libffi, git client, 
openssh client, ruby-irb, and a few other utilities.  Also includes 
/etc/timezone which is set to Los_Angeles.

### rails-5
Same as rails, but explicitly pulls ruby2.3 from the ruby:2.3-alpine image.

### ruby
A simple alpine image that includes ruby

### ruby-libv8
An image that includes ruby and the libv8, mini_racer, and nokogiri gems 
pre-built.  Includes working dockerfiles for alpine and ubuntu.

### ruby-libv8-phantomjs
Same as above, but includes a phantomjs binary.  Also, there's no dockerfile 
for alpine since the phantomjs binary doesn't work in alpine as of this 
writing (phantomjs hangs).  The ubuntu image works though.

### alpine-phantomjs-builder
Meant to be a simple way to build a phantomjs binary compatible with alpine 
(for the above libv8-phantomjs) but phantomjs still doesn't seem to work in 
alpine.  Included in this repo since its output a direct dependency of the 
libv8-phantomjs image above.

## License

MIT License. Do what you want, this is just configuration, nothing special.
