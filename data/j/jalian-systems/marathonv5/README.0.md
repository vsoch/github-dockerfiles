Hello,
this is the Login demo!
 
Scenario
========
1) Open the Demo project in NetBeans.
2) Run the project.
3) In the logging window log as user: demo  password: demo
Any other name will be rejected.
4) In the Profile window, you can set the phone/email/subscription.
5) Click on Update to update the model with the typed values. 
You should observe an animated test to warn that profile has been updated.
6) Click on logout to go back to login window.
7) Log again as done in step 3).
8) You will observe an updated profile.
9) Close the Window.

Adding new user
===============
- Edit the class demo.security.Authenticator
- To add Joe with password barteam add USERS.put("Joe", "barteam");
- Then re-run the project

Known issues
============
- Do not resize the windows, you will observe wrong background resizing.
- TextBox font is a bit too small.

Workaround put in place
=======================
- Styleclass has been set on Profile and Login controllers in order to set 
a background on both screen. Style class should be set thanks to the VT.

Difficulties and issues encountered in the VT when making the demo
==================================================================
- Difficult to align properly elements.
- Spacing of dynamic content is difficult to handle.
- Double values. too much digits. Makes very difficult to compare values.
- Project Panel, background is useless. We should get ridoff it.
- FileChooser has no memory. Tedious to select FXML files.
- Inline Editor is not working well.
- No visual feedback when moving elements in StageView (at least on mac)
- Tedious to set colors/Font properties on multiple element. CSS would help there.
- Button disabled should be in Type info panel.
- Need static edit to switch from code <==> UI layout. Otherwise NPE....
- Resizing the background issues.<?xml version='1.0' encoding='utf-8' ?><!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/></head><body><h1 id="Marathon">Marathon</h1><p>Marathon &#8211; Java GUI Testing Tool.</p><h2 id="WhatisMarathon">What is Marathon?</h2><p>Marathon is a tool for recording, replaying, refactoring test cases for Java GUI programs developed using Swing components. Marathon consists of an editor, a recorder and a player. Marathon records the test cases in an easy to read and maintainable format using Jython, or JRuby that can be selected at the time of project creation. The test cases can be run either through the UI or in batch mode.</p><h2 id="BuildingMarathon">Building Marathon</h2><p>You need to clone this repository as well update submodule to compile Marathon.</p><p><pre><code><br/>$ git clone git://github.com/jalian-systems/Marathon.git<br/>$ cd Marathon<br/>$ git submodule update --init<br/>$ ant<br/></code></pre></p><p>Should generate marathon-{version}.zip.</p><h3 id="UsingEclipse">Using Eclipse</h3><p>Clone the repository.</p><p>Install egit/jgit plugins. Import the projects from the cloned repository. There is an EclipseFormatting.xml file in the repository &#8211; set eclipse formatting preferences to use these preferences.</p><p>Build All. Enjoy.</p><p>Note: The build might fail first time (Version class not found). Just use Build All again.</p><h2 id="MoreInformation">More Information </h2><p>You can get more information about Marathon and documentation/support from:</p><p>http://www.marathontesting.com/</p></body></html>Hello,
this is the Login demo!
 
Scenario
========
1) Open the Demo project in NetBeans.
2) Run the project.
3) In the logging window log as user: demo  password: demo
Any other name will be rejected.
4) In the Profile window, you can set the phone/email/subscription.
5) Click on Update to update the model with the typed values. 
You should observe an animated test to warn that profile has been updated.
6) Click on logout to go back to login window.
7) Log again as done in step 3).
8) You will observe an updated profile.
9) Close the Window.

Adding new user
===============
- Edit the class demo.security.Authenticator
- To add Joe with password barteam add USERS.put("Joe", "barteam");
- Then re-run the project

Known issues
============
- Do not resize the windows, you will observe wrong background resizing.
- TextBox font is a bit too small.

Workaround put in place
=======================
- Styleclass has been set on Profile and Login controllers in order to set 
a background on both screen. Style class should be set thanks to the VT.

Difficulties and issues encountered in the VT when making the demo
==================================================================
- Difficult to align properly elements.
- Spacing of dynamic content is difficult to handle.
- Double values. too much digits. Makes very difficult to compare values.
- Project Panel, background is useless. We should get ridoff it.
- FileChooser has no memory. Tedious to select FXML files.
- Inline Editor is not working well.
- No visual feedback when moving elements in StageView (at least on mac)
- Tedious to set colors/Font properties on multiple element. CSS would help there.
- Button disabled should be in Type info panel.
- Need static edit to switch from code <==> UI layout. Otherwise NPE....
- Resizing the background issues.========================
BUILD OUTPUT DESCRIPTION
========================

When you build an Java application project that has a main class, the IDE
automatically copies all of the JAR
files on the projects classpath to your projects dist/lib folder. The IDE
also adds each of the JAR files to the Class-Path element in the application
JAR files manifest file (MANIFEST.MF).

To run the project from the command line, go to the dist folder and
type the following:

java -jar "SwingSet3.jar" 

To distribute this project, zip up the dist folder (including the lib folder)
and distribute the ZIP file.

Notes:

* If two JAR files on the project classpath have the same name, only the first
JAR file is copied to the lib folder.
* Only JAR files are copied to the lib folder.
If the classpath contains other types of files or folders, none of the
classpath elements are copied to the lib folder. In such a case,
you need to copy the classpath elements to the lib folder manually after the build.
* If a library on the projects classpath also has a Class-Path element
specified in the manifest,the content of the Class-Path element has to be on
the projects runtime path.
* To set a main class in a standard Java project, right-click the project node
in the Projects window and choose Properties. Then click Run and enter the
class name in the Main Class field. Alternatively, you can manually type the
class name in the manifest Main-Class element.
<?xml version='1.0' encoding='utf-8' ?><!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/></head><body><h1 id="Marathon">Marathon</h1><p>Marathon &#8211; Java GUI Testing Tool.</p><h2 id="WhatisMarathon">What is Marathon?</h2><p>Marathon is a tool for recording, replaying, refactoring test cases for Java GUI programs developed using Swing components. Marathon consists of an editor, a recorder and a player. Marathon records the test cases in an easy to read and maintainable format using Jython, or JRuby that can be selected at the time of project creation. The test cases can be run either through the UI or in batch mode.</p><h2 id="BuildingMarathon">Building Marathon</h2><p>You need to clone this repository as well update submodule to compile Marathon.</p><p><pre><code><br/>$ git clone git://github.com/jalian-systems/Marathon.git<br/>$ cd Marathon<br/>$ git submodule update --init<br/>$ ant<br/></code></pre></p><p>Should generate marathon-{version}.zip.</p><h3 id="UsingEclipse">Using Eclipse</h3><p>Clone the repository.</p><p>Install egit/jgit plugins. Import the projects from the cloned repository. There is an EclipseFormatting.xml file in the repository &#8211; set eclipse formatting preferences to use these preferences.</p><p>Build All. Enjoy.</p><p>Note: The build might fail first time (Version class not found). Just use Build All again.</p><h2 id="MoreInformation">More Information </h2><p>You can get more information about Marathon and documentation/support from:</p><p>http://www.marathontesting.com/</p></body></html>1. Building the GEM
   Run `gem build marathon-javadriver.gemspec`. This should build the gem in the current folder.
2. Installing the GEM
   Run `gem install ./<gem-name>`.
3. Running the tests
   a. set MARATHON_HOME to the marathon installation folder. Alternatively set MARATHON_AGENT to point to the marathon-java-agent jar file.
   b. run `rspec`. This command should run all tests from the spec folder.

========================
BUILD OUTPUT DESCRIPTION
========================

When you build an Java application project that has a main class, the IDE
automatically copies all of the JAR
files on the projects classpath to your projects dist/lib folder. The IDE
also adds each of the JAR files to the Class-Path element in the application
JAR files manifest file (MANIFEST.MF).

To run the project from the command line, go to the dist folder and
type the following:

java -jar "SwingSet3.jar" 

To distribute this project, zip up the dist folder (including the lib folder)
and distribute the ZIP file.

Notes:

* If two JAR files on the project classpath have the same name, only the first
JAR file is copied to the lib folder.
* Only JAR files are copied to the lib folder.
If the classpath contains other types of files or folders, none of the
classpath elements are copied to the lib folder. In such a case,
you need to copy the classpath elements to the lib folder manually after the build.
* If a library on the projects classpath also has a Class-Path element
specified in the manifest,the content of the Class-Path element has to be on
the projects runtime path.
* To set a main class in a standard Java project, right-click the project node
in the Projects window and choose Properties. Then click Run and enter the
class name in the Main Class field. Alternatively, you can manually type the
class name in the manifest Main-Class element.
When using batch file, any files in this folder will be added to the classpath and available to access from ruby scripts.
Ace (Ajax.org Cloud9 Editor)
============================

Ace is a code editor written in JavaScript.

This repository has only generated files.
If you want to work on ace please go to https://github.com/ajaxorg/ace instead.


here you can find pre-built files for convenience of embedding.
it contains 4 versions
 * [src](https://github.com/ajaxorg/ace-builds/tree/master/src)              concatenated but not minified
 * [src-min](https://github.com/ajaxorg/ace-builds/tree/master/src-min)      concatenated and minified with uglify.js
 * [src-noconflict](https://github.com/ajaxorg/ace-builds/tree/master/src-noconflict)      uses ace.require instead of require
 * [src-min-noconflict](https://github.com/ajaxorg/ace-builds/tree/master/src-min-noconflict)      -


For a simple way of embedding ace into webpage see [editor.html](https://github.com/ajaxorg/ace-builds/blob/master/editor.html) or list of other [simple examples](https://github.com/ajaxorg/ace-builds/tree/master/demo)
To see ace in action go to [kitchen-sink-demo](http://ajaxorg.github.com/ace-builds/kitchen-sink.html), [scrollable-page-demo](http://ajaxorg.github.com/ace-builds/demo/scrollable-page.html) or [minimal demo](http://ajaxorg.github.com/ace-builds/editor.html),


# childprocess

This gem aims at being a simple and reliable solution for controlling
external programs running in the background on any Ruby / OS combination.

The code originated in the [selenium-webdriver](https://rubygems.org/gems/selenium-webdriver) gem, but should prove useful as
a standalone library.

[![Build Status](https://secure.travis-ci.org/enkessler/childprocess.svg)](http://travis-ci.org/enkessler/childprocess)
[![Build status](https://ci.appveyor.com/api/projects/status/fn2snbcd7kku5myk/branch/dev?svg=true)](https://ci.appveyor.com/project/enkessler/childprocess/branch/dev)
[![Gem Version](https://badge.fury.io/rb/childprocess.svg)](http://badge.fury.io/rb/childprocess)
[![Code Climate](https://codeclimate.com/github/enkessler/childprocess.svg)](https://codeclimate.com/github/enkessler/childprocess)
[![Coverage Status](https://coveralls.io/repos/enkessler/childprocess/badge.svg?branch=master)](https://coveralls.io/r/enkessler/childprocess?branch=master)

# Usage

The object returned from `ChildProcess.build` will implement `ChildProcess::AbstractProcess`.

### Basic examples

```ruby
process = ChildProcess.build("ruby", "-e", "sleep")

# inherit stdout/stderr from parent...
process.io.inherit!

# ...or pass an IO
process.io.stdout = Tempfile.new("child-output")

# modify the environment for the child
process.environment["a"] = "b"
process.environment["c"] = nil

# set the child's working directory
process.cwd = '/some/path'

# start the process
process.start

# check process status
process.alive?    #=> true
process.exited?   #=> false

# wait indefinitely for process to exit...
process.wait
process.exited?   #=> true

# get the exit code
process.exit_code #=> 0

# ...or poll for exit + force quit
begin
  process.poll_for_exit(10)
rescue ChildProcess::TimeoutError
  process.stop # tries increasingly harsher methods to kill the process.
end
```

### Advanced examples

#### Output to pipe

```ruby
r, w = IO.pipe

proc = ChildProcess.build("echo", "foo")
proc.io.stdout = proc.io.stderr = w
proc.start
w.close

begin
  loop { print r.readpartial(8192) }
rescue EOFError
end

proc.wait
```

Note that if you just want to get the output of a command, the backtick method on Kernel may be a better fit.

#### Write to stdin

```ruby
process = ChildProcess.build("cat")

out      = Tempfile.new("duplex")
out.sync = true

process.io.stdout = process.io.stderr = out
process.duplex    = true # sets up pipe so process.io.stdin will be available after .start

process.start
process.io.stdin.puts "hello world"
process.io.stdin.close

process.poll_for_exit(exit_timeout_in_seconds)

out.rewind
out.read #=> "hello world\n"
```

#### Pipe output to another ChildProcess

```ruby
search           = ChildProcess.build("grep", '-E', %w(redis memcached).join('|'))
search.duplex    = true # sets up pipe so search.io.stdin will be available after .start
search.io.stdout = $stdout
search.start

listing           = ChildProcess.build("ps", "aux")
listing.io.stdout = search.io.stdin
listing.start
listing.wait

search.io.stdin.close
search.wait
```

#### Prefer posix_spawn on *nix

If the parent process is using a lot of memory, `fork+exec` can be very expensive. The `posix_spawn()` API removes this overhead.

```ruby
ChildProcess.posix_spawn = true
process = ChildProcess.build(*args)
```

### Ensure entire process tree dies

By default, the child process does not create a new process group. This means there's no guarantee that the entire process tree will die when the child process is killed. To solve this:

```ruby
process = ChildProcess.build(*args)
process.leader = true
process.start
```

#### Detach from parent

```ruby
process = ChildProcess.build("sleep", "10")
process.detach = true
process.start
```

#### Invoking a shell

As opposed to `Kernel#system`, `Kernel#exec` et al., ChildProcess will not automatically execute your command in a shell (like `/bin/sh` or `cmd.exe`) depending on the arguments.
This means that if you try to execute e.g. gem executables (like `bundle` or `gem`) or Windows executables (with `.com` or `.bat` extensions) you may see a `ChildProcess::LaunchError`.
You can work around this by being explicit about what interpreter to invoke:

```ruby
ChildProcess.build("cmd.exe", "/c", "bundle")
ChildProcess.build("ruby", "-S", "bundle")
```

#### Log to file

Errors and debugging information are logged to `$stderr` by default but a custom logger can be used instead. 

```ruby
logger = Logger.new('logfile.log')
logger.level = Logger::DEBUG
ChildProcess.logger = logger
```

## Caveats

* With JRuby on Unix, modifying `ENV["PATH"]` before using childprocess could lead to 'Command not found' errors, since JRuby is unable to modify the environemnt used for PATH searches in `java.lang.ProcessBuilder`. This can be avoided by setting `ChildProcess.posix_spawn = true`.

# Implementation

How the process is launched and killed depends on the platform:

* Unix     : `fork + exec` (or `posix_spawn` if enabled)
* Windows  : `CreateProcess()` and friends
* JRuby    : `java.lang.{Process,ProcessBuilder}`

# Note on Patches/Pull Requests

1. Fork it
2. Create your feature branch (off of the development branch)
   `git checkout -b my-new-feature dev`
3. Commit your changes
   `git commit -am 'Add some feature'`
4. Push to the branch
   `git push origin my-new-feature`
5. Create new Pull Request

# Copyright

Copyright (c) 2010-2015 Jari Bakken. See LICENSE for details.
# selenium-webdriver

This gem provides Ruby bindings for WebDriver
and has been tested to work on MRI (2.0 through 2.2),

## Install

    gem install selenium-webdriver

## Links

* http://rubygems.org/gems/selenium-webdriver
* http://seleniumhq.github.io/selenium/docs/api/rb/index.html
* https://github.com/SeleniumHQ/selenium/wiki/Ruby-Bindings
* https://github.com/SeleniumHQ/selenium/issues

## License

Copyright 2009-2017 Software Freedom Conservancy

Licensed to the Software Freedom Conservancy (SFC) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The SFC licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
# rubyzip
[![Gem Version](https://badge.fury.io/rb/rubyzip.svg)](http://badge.fury.io/rb/rubyzip)
[![Build Status](https://secure.travis-ci.org/rubyzip/rubyzip.svg)](http://travis-ci.org/rubyzip/rubyzip)
[![Code Climate](https://codeclimate.com/github/rubyzip/rubyzip.svg)](https://codeclimate.com/github/rubyzip/rubyzip)
[![Coverage Status](https://img.shields.io/coveralls/rubyzip/rubyzip.svg)](https://coveralls.io/r/rubyzip/rubyzip?branch=master)

Rubyzip is a ruby library for reading and writing zip files.

## Important note

The Rubyzip interface has changed!!! No need to do `require "zip/zip"` and `Zip` prefix in class names removed.

If you have issues with any third-party gems that require an old version of rubyzip, you can use this workaround:

```ruby
gem 'rubyzip', '>= 1.0.0' # will load new rubyzip version
gem 'zip-zip' # will load compatibility for old rubyzip API.
```

## Requirements

* Ruby 1.9.2 or greater

## Installation
Rubyzip is available on RubyGems:

```
gem install rubyzip
```

Or in your Gemfile:

```ruby
gem 'rubyzip'
```

## Usage

### Basic zip archive creation

```ruby
require 'rubygems'
require 'zip'

folder = "Users/me/Desktop/stuff_to_zip"
input_filenames = ['image.jpg', 'description.txt', 'stats.csv']

zipfile_name = "/Users/me/Desktop/archive.zip"

Zip::File.open(zipfile_name, Zip::File::CREATE) do |zipfile|
  input_filenames.each do |filename|
    # Two arguments:
    # - The name of the file as it will appear in the archive
    # - The original file, including the path to find it
    zipfile.add(filename, folder + '/' + filename)
  end
  zipfile.get_output_stream("myFile") { |os| os.write "myFile contains just this" }
end
```

### Zipping a directory recursively
Copy from [here](https://github.com/rubyzip/rubyzip/blob/05916bf89181e1955118fd3ea059f18acac28cc8/samples/example_recursive.rb )

```ruby
require 'zip'

# This is a simple example which uses rubyzip to
# recursively generate a zip file from the contents of
# a specified directory. The directory itself is not
# included in the archive, rather just its contents.
#
# Usage:
#   directory_to_zip = "/tmp/input"
#   output_file = "/tmp/out.zip"
#   zf = ZipFileGenerator.new(directory_to_zip, output_file)
#   zf.write()
class ZipFileGenerator
  # Initialize with the directory to zip and the location of the output archive.
  def initialize(input_dir, output_file)
    @input_dir = input_dir
    @output_file = output_file
  end

  # Zip the input directory.
  def write
    entries = Dir.entries(@input_dir) - %w(. ..)

    ::Zip::File.open(@output_file, ::Zip::File::CREATE) do |io|
      write_entries entries, '', io
    end
  end

  private

  # A helper method to make the recursion work.
  def write_entries(entries, path, io)
    entries.each do |e|
      zip_file_path = path == '' ? e : File.join(path, e)
      disk_file_path = File.join(@input_dir, zip_file_path)
      puts "Deflating #{disk_file_path}"

      if File.directory? disk_file_path
        recursively_deflate_directory(disk_file_path, io, zip_file_path)
      else
        put_into_archive(disk_file_path, io, zip_file_path)
      end
    end
  end

  def recursively_deflate_directory(disk_file_path, io, zip_file_path)
    io.mkdir zip_file_path
    subdir = Dir.entries(disk_file_path) - %w(. ..)
    write_entries subdir, zip_file_path, io
  end

  def put_into_archive(disk_file_path, io, zip_file_path)
    io.get_output_stream(zip_file_path) do |f|
      f.write(File.open(disk_file_path, 'rb').read)
    end
  end
end
```

### Save zip archive entries in sorted by name state

To save zip archives in sorted order like below, you need to set `::Zip.sort_entries` to `true`

```
Vegetable/
Vegetable/bean
Vegetable/carrot
Vegetable/celery
fruit/
fruit/apple
fruit/kiwi
fruit/mango
fruit/orange
```

After this, entries in the zip archive will be saved in ordered state.

### Default permissions of zip archives

On Posix file systems the default file permissions applied to a new archive
are (0666 - umask), which mimics the behavior of standard tools such as `touch`.

On Windows the default file permissions are set to 0644 as suggested by the
[Ruby File documentation](http://ruby-doc.org/core-2.2.2/File.html).

When modifying a zip archive the file permissions of the archive are preserved.

### Reading a Zip file

```ruby
Zip::File.open('foo.zip') do |zip_file|
  # Handle entries one by one
  zip_file.each do |entry|
    # Extract to file/directory/symlink
    puts "Extracting #{entry.name}"
    entry.extract(dest_file)

    # Read into memory
    content = entry.get_input_stream.read
  end

  # Find specific entry
  entry = zip_file.glob('*.csv').first
  puts entry.get_input_stream.read
end
```

#### Notice about ::Zip::InputStream

`::Zip::InputStream` usable for fast reading zip file content because it not read Central directory.

But there is one exception when it is not working - General Purpose Flag Bit 3.

```
If bit 3 (0x08) of the general-purpose flags field is set, then the CRC-32 and file sizes are not known when the header is written. The fields in the local header are filled with zero, and the CRC-32 and size are appended in a 12-byte structure (optionally preceded by a 4-byte signature) immediately after the compressed data
```

If `::Zip::InputStream` finds such entry in the zip archive it will raise an exception.

### Password Protection (Experimental)

Rubyzip supports reading/writing zip files with traditional zip encryption (a.k.a. "ZipCrypto"). AES encryption is not yet supported. It can be used with buffer streams, e.g.:

```ruby
Zip::OutputStream.write_buffer(::StringIO.new(''), Zip::TraditionalEncrypter.new('password')) do |out|
  out.put_next_entry("my_file.txt")
  out.write my_data
end.string
```

This is an experimental feature and the interface for encryption may change in future versions.

## Known issues

### Modify docx file with rubyzip

Use `write_buffer` instead `open`. Thanks to @jondruse

```ruby
buffer = Zip::OutputStream.write_buffer do |out|
  @zip_file.entries.each do |e|
    unless [DOCUMENT_FILE_PATH, RELS_FILE_PATH].include?(e.name)
      out.put_next_entry(e.name)
      out.write e.get_input_stream.read
     end
  end

  out.put_next_entry(DOCUMENT_FILE_PATH)
  out.write xml_doc.to_xml(:indent => 0).gsub("\n","")

  out.put_next_entry(RELS_FILE_PATH)
  out.write rels.to_xml(:indent => 0).gsub("\n","")
end

File.open(new_path, "wb") {|f| f.write(buffer.string) }
```

## Configuration

By default, rubyzip will not overwrite files if they already exist inside of the extracted path.  To change this behavior, you may specify a configuration option like so:

```ruby
Zip.on_exists_proc = true
```

If you're using rubyzip with rails, consider placing this snippet of code in an initializer file such as `config/initializers/rubyzip.rb`

Additionally, if you want to configure rubyzip to overwrite existing files while creating a .zip file, you can do so with the following:

```ruby
Zip.continue_on_exists_proc = true
```

If you want to store non-english names and want to open them on Windows(pre 7) you need to set this option:

```ruby
Zip.unicode_names = true
```

Some zip files might have an invalid date format, which will raise a warning. You can hide this warning with the following setting:

```ruby
Zip.warn_invalid_date = false
```

You can set the default compression level like so:

```ruby
Zip.default_compression = Zlib::DEFAULT_COMPRESSION
```
It defaults to `Zlib::DEFAULT_COMPRESSION`. Possible values are `Zlib::BEST_COMPRESSION`, `Zlib::DEFAULT_COMPRESSION` and `Zlib::NO_COMPRESSION`

You can set multiple settings at the same time by using a block:

```ruby
  Zip.setup do |c|
    c.on_exists_proc = true
    c.continue_on_exists_proc = true
    c.unicode_names = true
    c.default_compression = Zlib::BEST_COMPRESSION
  end
```

By default, Zip64 support is disabled for writing. To enable it do this:

```ruby
Zip.write_zip64_support = true
```

_NOTE_: If you will enable Zip64 writing then you will need zip extractor with Zip64 support to extract archive.

## Developing

To run the test you need to do this:

```
bundle install
rake
```

## Website and Project Home

http://github.com/rubyzip/rubyzip

http://rdoc.info/github/rubyzip/rubyzip/master/frames

## Authors

Alexander Simonov ( alex at simonov.me)

Alan Harper ( alan at aussiegeek.net)

Thomas Sondergaard (thomas at sondergaard.cc)

Technorama Ltd. (oss-ruby-zip at technorama.net)

extra-field support contributed by Tatsuki Sugiura (sugi at nemui.org)

## License

Rubyzip is distributed under the same license as ruby. See
http://www.ruby-lang.org/en/LICENSE.txt
# ruby-ffi https://wiki.github.com/ffi/ffi [![Build Status](https://travis-ci.org/ffi/ffi.png?branch=master)](https://travis-ci.org/ffi/ffi)

## Description

Ruby-FFI is a ruby extension for programmatically loading dynamic
libraries, binding functions within them, and calling those functions
from Ruby code. Moreover, a Ruby-FFI extension works without changes
on Ruby and JRuby. [Discover why you should write your next extension
using Ruby-FFI](https://wiki.github.com/ffi/ffi/why-use-ffi).

## Features/problems

* Intuitive DSL
* Supports all C native types
* C structs (also nested), enums and global variables
* Callbacks from C to ruby
* Automatic garbage collection of native memory

## Synopsis

```ruby
require 'ffi'

module MyLib
  extend FFI::Library
  ffi_lib 'c'
  attach_function :puts, [ :string ], :int
end

MyLib.puts 'Hello, World using libc!'
```

For less minimalistic and more sane examples you may look at:

* the samples/ folder
* the examples on the [wiki](https://wiki.github.com/ffi/ffi)
* the projects using FFI listed on this page (https://wiki.github.com/ffi/ffi/projects-using-ffi)

## Requirements

You need a sane building environment in order to compile the extension.
At a minimum, you will need:
* A C compiler (e.g. Xcode on OSX, gcc on everything else)
* libffi development library - this is commonly in the libffi-dev or libffi-devel

On Linux systems running with [PaX](https://en.wikipedia.org/wiki/PaX) (Gentoo, Alpine, etc.) FFI may trigger `mprotrect` errors. You may need to disable [mprotect](https://en.wikibooks.org/wiki/Grsecurity/Appendix/Grsecurity_and_PaX_Configuration_Options#Restrict_mprotect.28.29) for ruby (`paxctl -m [/path/to/ruby]`) for the time being until a solution is found.

## Installation

From rubygems:

    [sudo] gem install ffi

or from the git repository on github:

    git clone git://github.com/ffi/ffi.git
    cd ffi
    rake gem:install

## License

The ffi library is covered by the BSD license, also see the LICENSE file.
The specs are shared with Rubyspec and are licensed by the same license
as Rubyspec, see the LICENSE.SPECS file.

## Credits

The following people have submitted code, bug reports, or otherwise contributed to the success of this project:

* Alban Peignier <alban.peignier@free.fr>
* Aman Gupta <aman@tmm1.net>
* Andrea Fazzi <andrea.fazzi@alcacoop.it>
* Andreas Niederl <rico32@gmx.net>
* Andrew Cholakian <andrew@andrewvc.com>
* Antonio Terceiro <terceiro@softwarelivre.org>
* Brian Candler <B.Candler@pobox.com>
* Brian D. Burns <burns180@gmail.com>
* Bryan Kearney <bkearney@redhat.com>
* Charlie Savage <cfis@zerista.com>
* Chikanaga Tomoyuki <nagachika00@gmail.com>
* Hongli Lai <hongli@phusion.nl>
* Ian MacLeod <ian@nevir.net>
* Jake Douglas <jake@shiftedlabs.com>
* Jean-Dominique Morani <jdmorani@mac.com>
* Jeremy Hinegardner <jeremy@hinegardner.org>
* Jesús García Sáez <blaxter@gmail.com>
* Joe Khoobyar <joe@ankhcraft.com>
* Jurij Smakov <jurij@wooyd.org>
* KISHIMOTO, Makoto <ksmakoto@dd.iij4u.or.jp>
* Kim Burgestrand <kim@burgestrand.se>
* Lars Kanis <kanis@comcard.de>
* Luc Heinrich <luc@honk-honk.com>
* Luis Lavena <luislavena@gmail.com>
* Matijs van Zuijlen <matijs@matijs.net>
* Matthew King <automatthew@gmail.com>
* Mike Dalessio <mike.dalessio@gmail.com>
* NARUSE, Yui <naruse@airemix.jp>
* Park Heesob <phasis@gmail.com>
* Shin Yee <shinyee@speedgocomputing.com>
* Stephen Bannasch <stephen.bannasch@gmail.com>
* Suraj N. Kurapati <sunaku@gmail.com>
* Sylvain Daubert <sylvain.daubert@laposte.net>
* Victor Costan
* beoran@gmail.com
* ctide <christide@christide.com>
* emboss <Martin.Bosslet@googlemail.com>
* hobophobe <unusualtears@gmail.com>
* meh <meh@paranoici.org>
* postmodern <postmodern.mod3@gmail.com>
* wycats@gmail.com <wycats@gmail.com>
* Wayne Meissner <wmeissner@gmail.com>
JSON in Java [package org.json]

Douglas Crockford
douglas@crockford.com

2011-02-02


JSON is a light-weight, language independent, data interchange format.
See http://www.JSON.org/

The files in this package implement JSON encoders/decoders in Java.
It also includes the capability to convert between JSON and XML, HTTP
headers, Cookies, and CDL.

This is a reference implementation. There is a large number of JSON packages
in Java. Perhaps someday the Java community will standardize on one. Until
then, choose carefully.

The license includes this restriction: "The software shall be used for good,
not evil." If your conscience cannot live with that, then choose a different
package.

The package compiles on Java 1.2 thru Java 1.4.


JSONObject.java: The JSONObject can parse text from a String or a JSONTokener
to produce a map-like object. The object provides methods for manipulating its
contents, and for producing a JSON compliant object serialization.

JSONArray.java: The JSONObject can parse text from a String or a JSONTokener
to produce a vector-like object. The object provides methods for manipulating
its contents, and for producing a JSON compliant array serialization.

JSONTokener.java: The JSONTokener breaks a text into a sequence of individual
tokens. It can be constructed from a String, Reader, or InputStream.

JSONException.java: The JSONException is the standard exception type thrown
by this package.


JSONString.java: The JSONString interface requires a toJSONString method,
allowing an object to provide its own serialization.

JSONStringer.java: The JSONStringer provides a convenient facility for
building JSON strings.

JSONWriter.java: The JSONWriter provides a convenient facility for building
JSON text through a writer.


CDL.java: CDL provides support for converting between JSON and comma
delimited lists.

Cookie.java: Cookie provides support for converting between JSON and cookies.

CookieList.java: CookieList provides support for converting between JSON and
cookie lists.

HTTP.java: HTTP provides support for converting between JSON and HTTP headers.

HTTPTokener.java: HTTPTokener extends JSONTokener for parsing HTTP headers.

XML.java: XML provides support for converting between JSON and XML.

JSONML.java: JSONML provides support for converting between JSONML and XML.

XMLTokener.java: XMLTokener extends JSONTokener for parsing XML text.
FOR EVALUATION PURPOSES ONLY. THIS PACKAGE HAS NOT BEEN TESTED ADEQUATELY FOR
PRODUCTION USE.
