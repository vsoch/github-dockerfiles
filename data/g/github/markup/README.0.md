* One
* Two
* One
* Two
<ul>
	<li>One</li>
	<li>Two</li>
</ul><div>
<p>Contents</p>
<ul>
<li>
<a href="#introduction">1   Introduction</a><ul>
<li><a href="#what-is-pycparser">1.1   What is pycparser?</a></li>
<li><a href="#what-is-it-good-for">1.2   What is it good for?</a></li>
</ul>
</li>
</ul>
</div>
<a name="introduction"></a>
<h2>1   Introduction</h2>
<a name="what-is-pycparser"></a>
<h3>1.1   What is pycparser?</h3>
<p><strong>pycparser</strong> is a parser for the C language, written in pure Python. It is a
module designed to be easily integrated into applications that need to parse
C source code.</p>
<a name="what-is-it-good-for"></a>
<h3>1.2   What is it good for?</h3>
<p>Anything that needs C code to be parsed. The following are some uses for
<strong>pycparser</strong>, taken from real user reports:</p>
<ul>
<li>C code obfuscator</li>
<li>Front-end for various specialized C compilers</li>
<li>Static code checker</li>
<li>Automatic unit-test discovery</li>
<li>Adding specialized extensions to the C language</li>
</ul>
<p><strong>pycparser</strong> is unique in the sense that it's written in pure Python - a very
high level language that's easy to experiment with and tweak. To people familiar
with Lex and Yacc, <strong>pycparser</strong>'s code will be simple to understand.</p>
* One
* Two

This is an {absolute link}[http://github.com].  So is this: http://github.com

This is a {relative link}[link:rawr.html].  So is this: link:rawr.html<ul>
<li>
<p>One</p>
</li>
<li>
<p>Two</p>
</li>
</ul>

<p>This is an <a href="http://github.com">absolute link</a>.  So is this: <a href="http://github.com">github.com</a></p>

<p>This is a <a href="rawr.html">relative link</a>.  So is this: <a href="rawr.html">rawr.html</a></p>* One
* Two
<ul>
<li>One</li>
<li>Two</li>
</ul>==================================================
restructuredText (rst) directives and comments
==================================================

Introduction
=================

An rst directive starts with two periods, and has a keyword
followed by two colons, like this::

    .. MyDirective::

The rst parser is quite flexible and configurable.  Directives
may be added for specialized operations.  Sphinx is a system
that was designed for writing documentation, and, for example,
readthedocs.org uses sphinx.

Display of rst files at github needs to cover two distinct
use-cases:

- The github display is the primary method for displaying
  the file (e.g. for README.rst files)

- The github display is incidental to the primary method
  for displaying the file (e.g. for readthedocs documentation)

Currently, github handles the first case fine, but could
confuse viewers for the second case, because sometimes
content is missing from the github display.

It would seem that one possibility for distinguishing these
two cases is to add a github directive to control the display.

Unfortunately, this would place a burden on every other rst
parser to ignore the github directive (some of them will error
on unknown directives).

Instead, we can assign semantic content to specific comments.

This is a fairly ugly hack, but it has the benefit of not
requiring any document changes that would create problems with
any conformant parser.


The proposed special comment is::

  .. github display [on | off]


If you pass this the "on" value, then all unknown directives
will be displayed as literal code blocks.  If you pass this
the "off" value, then unknown directives will not be displayed.

In addition to controlling the display of literal code blocks,
this also allows you to show comments specifically for github.

For example, somebody could place this at the top of their file::

  .. github display

    This file was designed to be viewed at readthedocs.  Some
    content will not display properly when viewing using the
    github browser.

Tests
==========

By default, unknown directives should be displayed.

.. UnknownDirective::  This is an unknown directive

      it has a lot of stuff underneath it

But we can turn this off, and the next directive should
not be displayed.

.. github display off

.. UnknownDirective::  This is an unknown directive

      it has a lot of stuff underneath it

Or we can turn it back on...

.. github display on

.. UnknownDirective::  This is an unknown directive (3)

      it has a lot of stuff underneath it

Here is a comment that should display at github

.. github display

    YOU SHOULD SEE THIS!

And here is a comment that should not display at github

.. foobar

    YOU SHOULD NOT SEE THIS!

This concludes the tests.
* One
* Two<h1>Header 1</h1>
<p>Example text.</p>
<a name="header-2"></a>
<h2>Header 2</h2>
<ol>
<li>Blah blah <code>code</code> blah</li>
<li>More <code>code</code>, hooray</li>
<li>Somé UTF-8°</li>
</ol>
<table>




<tbody valign="top">
<tr>
<td>Travis</td>
<td><a href="http://travis-ci.org/tony/pullv">http://travis-ci.org/tony/pullv</a></td>
</tr>
<tr>
<td>Docs</td>
<td><a href="http://pullv.rtfd.org">http://pullv.rtfd.org</a></td>
</tr>
<tr>
<td>API</td>
<td><a href="http://pullv.readthedocs.org/en/latest/api.html">http://pullv.readthedocs.org/en/latest/api.html</a></td>
</tr>
<tr>
<td>Issues</td>
<td><a href="https://github.com/tony/pullv/issues">https://github.com/tony/pullv/issues</a></td>
</tr>
<tr>
<td>Source</td>
<td><a href="https://github.com/tony/pullv">https://github.com/tony/pullv</a></td>
</tr>
</tbody>
</table>Header 1
========

Example text.

Header 2
--------

1. Blah blah ``code`` blah

2. More ``code``, hooray

3. Somé UTF-8°

==============  ==========================================================
Travis          http://travis-ci.org/tony/pullv
Docs            http://pullv.rtfd.org
API             http://pullv.readthedocs.org/en/latest/api.html
Issues          https://github.com/tony/pullv/issues
Source          https://github.com/tony/pullv
==============  ==========================================================
<h1>H1</h1><h2>H2</h2><p>paragraph of text that will be turned into a paragraph element. It can go over several lines with line breaks, it will be turned into a contiguous paragraph element.</p><p>You can force a linebreak in your paragraph text<br>thusly.</p><ul>
<li>a list element<ul><li>sub list element</li></ul>
</li>
<li>2nd list element</li>
</ul><pre>pre formatted text

$ ls -la
total 56
drwxr-xr-x   6 nferrier users  4096 Jul  5 23:10 .
drwxr-x--- 120 nferrier users 12288 Jul  5 19:36 ..
drwxr-xr-x   2 nferrier users  4096 Jul  5 18:19 bin
-rw-r--r--   1 nferrier users     6 Jul  5 18:19 .gitignore
drwxr-xr-x   4 nferrier users  4096 Jul  5 23:10 .hg
-rw-r--r--   1 nferrier users  1182 Jul  5 18:19 HISTORY.md
-rw-r--r--   1 nferrier users   562 Jul  5 18:19 .kick
drwxr-xr-x   3 nferrier users  4096 Jul  5 18:19 lib
-rw-r--r--   1 nferrier users  1050 Jul  5 18:19 LICENSE
-rw-r--r--   1 nferrier users  1312 Jul  5 18:19 Rakefile
-rw-r--r--   1 nferrier users  3390 Jul  5 18:19 README.md
drwxr-xr-x   3 nferrier users  4096 Jul  5 18:19 test</pre><p><a href="Home">» JRuby Project Wiki Home Page</a>
</p><h1>Embedding JRuby</h1>
Using Java from Ruby is JRuby's best-known feature---but you can also go in the other direction, and use Ruby from Java.  There are several different ways to do this. You can execute entire Ruby scripts, call individual Ruby methods, or even implement a Java interface in Ruby (thus allowing you to treat Ruby objects like Java ones).  We refer to all these techniques generically as "embedding."  This section will explain how to embed JRuby in your Java project.

<p></p><table summary="Contents"><tr><td>
<div><h2>Table of Contents</h2></div>
<ul>
<li>
<a href="#Red_Bridge_JRuby_Embed">Red Bridge (JRuby Embed)</a><ul><li><a href="#Features_of_Red_Bridge">Features of Red Bridge</a></li></ul>
</li>
<li><a href="#Previous_Embedding_JRuby_Page">Previous Embedding JRuby Page</a></li>
<li><a href="#References">References</a></li>
</ul>
</td></tr></table>


<h1>
<a name="Red_Bridge_JRuby_Embed"></a>Red Bridge (JRuby Embed)</h1>


<p><tt>one-&lt;two</tt>
</p><pre>a-b</pre>


<p>JRuby has long had a private embedding API, which was closely tied to the runtime's internals and therefore changed frequently as JRuby evolved. Since version 1.4, however, we have also provided a more stable public API, known as Red Bridge or JRuby Embed. Existing Java programs written to the <a href="DirectJRubyEmbedding">legacy API</a> should still work, but we strongly recommend Red Bridge for all new projects.
</p>

<h2>
<a name="Features_of_Red_Bridge"></a>Features of Red Bridge</h2>


<p>Red Bridge consists of two layers: Embed Core on the bottom, and implementations of <a href="http://www.jcp.org/en/jsr/detail?id=223" target="_blank">JSR223</a> and <a href="http://jakarta.apache.org/bsf/" target="_blank">BSF</a> on top. Embed Core is JRuby-specific, and can take advantage of much of JRuby's power. JSR223 and BSF are more general interfaces that provide a common ground across scripting languages.
</p>
<p>Which API should you use? For projects where Ruby is the only scripting language involved, we recommend Embed Core for the following reasons:
</p>



<p></p><ol>
<li>With Embed Core, you can create several Ruby environments in one JVM, and configure them individually (via <code>org.jruby.RubyInstanceConfig</code>. With the other APIs, configuration options can only be set globally, via the <code>System</code> properties.</li>
<li>Embed Core offers several shortcuts, such as loading scripts from a <code>java.io.InputStream</code>, or returning Java-friendly objects from Ruby code. These allow you to skip a lot of boilerplate.</li>
</ol>
For projects requiring multiple scripting languages, JSR223 is a good fit. Though the API is language-independent, JRuby's implementation of it allows you to set some Ruby-specific options. In particular, you can control the threading model of the scripting engine, the lifetime of local variables, compilation mode, and how line numbers are displayed.

<p>The full <a href="http://jruby-embed.kenai.com/docs/" target="_blank">API documentation</a> has all the gory details. It's worth talking about a couple of the finer points here.
</p>

<h1>
<a name="Previous_Embedding_JRuby_Page"></a>Previous Embedding JRuby Page</h1>


<p>We recommend using Embed Core; however, if you're maintaining code that uses the old API, you can find its documentation on the <a href="JavaIntegration">legacy embedding</a><sup>[<a href="#cite_note-1">1</a>]</sup> page.
</p>

<h1>
<a name="References"></a>References</h1>


<p></p><ol><li>
<b><a href="#cite_ref-1-0">^</a> </b> This link goes nowhere.</li></ol>* One
* Two#+TITLE:     org-ruby
#+AUTHOR:    Brian Dewey
#+EMAIL:     bdewey@gmail.com
#+DATE:      2009-12-21
#+DESCRIPTION: 
#+KEYWORDS: 
#+LANGUAGE:  en
#+OPTIONS:   H:3 num:t toc:nil \n:nil @:t ::t |:t ^:t -:t f:t *:t <:t
#+OPTIONS:   TeX:t LaTeX:nil skip:nil d:nil todo:nil pri:nil tags:not-in-toc
#+EXPORT_EXCLUDE_TAGS: exclude
#+STARTUP:    showall

 | Status:   | Under Development                 |
 | Location: | [[http://github.com/wallyqs/org-ruby]] |
 | Version:  | 0.9.0                             |

* Description

  Helpful Ruby routines for parsing orgmode files. The most
  significant thing this library does today is convert orgmode files
  to textile. Currently, you cannot do much to customize the
  conversion. The supplied textile conversion is optimized for
  extracting "content" from the orgfile as opposed to "metadata."

* History

** 2014-02-08: Version 0.9.0

   - Let's make sure =#+INCLUDE:= is not supported

#+INCLUDE: "./README.txt" src text

   - And confirm that syntax highlight is supported

#+begin_src ruby
module GitHub
  module Markup
    VERSION = 'test'
    Version = VERSION
  end
end
#+end_src

** 2009-12-30: Version 0.5.1

   - Minor enhancement: Recognize lines starting with ":" as examples.
   - Minor enhancement: Recognize #+BEGIN_SRC as source blocks
   - Minor enhancement: Add "src" and "example" classes to <pre> blocks.


** 2009-12-30: Version 0.5.0

   - Parse (but not necessarily *use*) in-buffer settings. The following
     in-buffer settings *are* used:
     - Understand the #+TITLE: directive.
     - Exporting todo keywords (option todo:t)
     - Numbering headlines (option num:t)
     - Skipping text before the first headline (option skip:t)
     - Skipping tables (option |:nil)
     - Custom todo keywords
     - EXPORT_SELECT_TAGS and EXPORT_EXLUDE_TAGS for controlling parts of
       the tree to export
   - Rewrite "file:(blah).org" links to "http:(blah).html" links. This
     makes the inter-links to other org-mode files work.
   - Uses <th> tags inside table rows that precede table separators.
   - Bugfixes:
     - Headings now have HTML escaped.

** 2009-12-29: Version 0.4.2

   - Got rid of the extraneous newline at the start of code blocks.
   - Everything now shows up in code blocks, even org-mode metadata.
   - Fixed bugs:
     - Regressed smart double quotes with HTML escaping. Added a test
       case and fixed the regression.

** 2009-12-29: Version 0.4.1
   - HTML is now escaped by default
   - org-mode comments will show up in a code block.

** 2009-12-29: Version 0.4

   - The first thing output in HTML gets the class "title"
   - HTML output is now indented
   - Proper support for multi-paragraph list items.

     See? This paragraph is part of the last bullet.
     
   - Fixed bugs:
     - "rake spec" wouldn't work on Linux. Needed "require 'rubygems'".

** 2009-12-27: Version 0.3

   - Uses rubypants to get better typography (smart quotes, ellipses, etc...).
   - Fixed bugs:
     - Tables and lists did not get properly closed at the end of file
     - You couldn't do inline formatting inside table cells
     - Characters in PRE blocks were not HTML escaped.
   
** 2009-12-26: Version 0.2

   - Added =to_html= output on the parser.
   - Added support for the full range of inline markup: *bold*,
     /italic/, =code=, ~verbatim~, _underline_, +strikethrough+.
   - Lots of refactoring to make the code more maintainable.

** 2009-12-23: Version 0.1

   - Added support for block code, like this:

     #+BEGIN_EXAMPLE
     def flush!
     @logger.debug "FLUSH ==========> #{@output_type}"
     if (@output_type == :blank) then
       @output << "\n"
     elsif (@buffer.length > 0) then
       if @cancel_modifier then
         @output << "p. " if @output_type == :paragraph
         @cancel_modifier = false
       end
       @output << @paragraph_modifier if (@paragraph_modifier and not sticky_modifier?)
       @output << @buffer.textile_substitution << "\n"
     end
     @buffer = ""
   end
   #+END_EXAMPLE

   - Major code cleanup: Created the =OutputBuffer= class that
     greatly simplified a lot of the messiness of =textile=
     conversion.
   - Added support for line breaks within list items.
<h1>Document Title</h1>
<div>
<h2>First Section</h2>
<div>
<div>
<ul>
<li>
<p>One</p>
</li>
<li>
<p>Two</p>
</li>
</ul>
</div>
<div>
<p>Refer to <a href="#another-section">Another Section</a> or <a href="#another-section-1">Another Section</a>.</p>
</div>
<div>
<p>Navigate from README.asciidoc to <a href="another-document.asciidoc">another document</a>.</p>
</div>
</div>
</div>
<div>
<h2>Another Section</h2>
<div>
<div>
<table>
<tr>
<td>
<div>Note</div>
</td>
<td>
Here is some source code.
</td>
</tr>
</table>
</div>
<div>
<div>
<pre lang="ruby"><code>puts "Hello, World!"</code></pre>
</div>
</div>
<div>
<ul>
<li>
<p>❏ todo</p>
</li>
<li>
<p>✓ done</p>
</li>
</ul>
</div>
</div>
</div>
<div>
<h2>Another Section</h2>
<div>
<div>
<p>content</p>
</div>
</div>
</div>
<h2>Literate CoffeeScript Test</h2>
<blockquote>
<p>Taken from <a href="https://github.com/jashkenas/coffee-script/blob/master/test/literate.litcoffee">https://github.com/jashkenas/coffee-script/blob/master/test/literate.litcoffee</a></p>
</blockquote>
<p>comment comment</p>
<pre><code>test "basic literate CoffeeScript parsing", -&gt;
  ok yes
</code></pre>
<p>now with a...</p>
<pre><code>test "broken up indentation", -&gt;
</code></pre>
<p>... broken up ...</p>
<pre><code>  do -&gt;
</code></pre>
<p>... nested block.</p>
<pre><code>    ok yes
</code></pre>
<p>Code must be separated from text by a blank line.</p>
<pre><code>test "code blocks must be preceded by a blank line", -&gt;
</code></pre>
<p>The next line is part of the text and will not be executed.
fail()</p>
<pre><code>  ok yes
</code></pre>
<p>Code in <code>backticks is not parsed</code> and...</p>
<pre><code>test "comments in indented blocks work", -&gt;
  do -&gt;
    do -&gt;
      # Regular comment.

      ###
        Block comment.
      ###

      ok yes
</code></pre>
<p>Regular <a href="http://example.com/markdown">Markdown</a> features,
like links and unordered lists, are fine:</p>
<ul>
<li>
<p>I</p>
</li>
<li>
<p>Am</p>
</li>
<li>
<p>A</p>
</li>
<li>
<p>List</p>
</li>
</ul>
<p>Tabs work too:</p>
<p>test "tabbed code", -&gt;
ok yes</p>
<h1>Matrixy</h1>

<h2>INTRODUCTION</h2>

<p>This is a port of the MATLAB/Octave programming language to Parrot. See the ROADMAP file for more information on the status of this project, and what else needs to be done.</p>

<h2>ABOUT</h2>

<p>Primary goals are:</p>

<ul>

<li><p>Create a working compiler that understands the majority of the MATLAB/Octave programming language.</p>

</li>
</ul>

<h2>IMPLEMENTATION</h2>

<p>This project is broken into three primary components:</p>

<ul>

<li><p>The first is the parser, located in the <code>src/parser/</code> directory. The parser proper is composed of three source files, <i>grammar.pg</i> which is a Perl6Grammar file, and <i>actions.pm</i> which is the associated actions file written in NQP, and <i>grammar-oper.pm</i> which is the operator precedence parser. In addition, several helper functions used by the parser are located in <code>src/internals</code>.</p>

</li>
<li><p>The second component is the library of builtin functions in the <code>src/builtins/</code> directory. These functions are, currently, written primarily in PIR. Function names prefixed with an underscore are &quot;private&quot; functions for use with the parser. Other functions should have names which are the same as names for regular MATLAB or Octave functions, since they will be available to the HLL. These are also separated into different namespaces depending on visibility and utility.</p>

</li>
<li><p>A number of library functions are written in M, or mostly M with some inline PIR code in <code>toolbox/</code>.</p>

</li>
</ul>

<h2>DEPENDENCIES</h2>

<p>Matrixy depends on these dependencies:</p>

<h3>Parrot</h3>

<p>To get a proper version of Parrot to build Matrixy, you will need to check out and build Parrot from source:</p>

<pre><code>svn co http://svn.parrot.org/parrot/trunk parrot
cd parrot
perl Configure.pl
make &amp;&amp; make test &amp;&amp; make install-dev</code></pre>

<h3>Parrot-Linear-Algebra</h3>

<p>The linear algebra package for Parrot is available separately and provides functionality required by Matrixy. This includes matrix data types and matrix manipulation libraries</p>

<h2>BUILDING</h2>

<p>Once all dependencies are in place, you can build Matrixy using this sequence of commands:</p>

<pre><code>perl Configure.pl
nmake test</code></pre>

<h2>TODO</h2>

<pre><code>* Parser
* Standard Builtins
* Test against Octave Test Suite.</code></pre>

<h2>BUGS</h2>

<p>Lots!</p>

<h2>CONTACT</h2>

<p>If you need to contact the Matrixy team, go to the project home page at:</p>

<p>www.github.com\Whiteknight\matrixy</p><h1>org-ruby</h1>
<table>
  <tr>
<td>Status:</td>
<td>Under Development</td>
</tr>
  <tr>
<td>Location:</td>
<td><a href="http://github.com/wallyqs/org-ruby">http://github.com/wallyqs/org-ruby</a></td>
</tr>
  <tr>
<td>Version:</td>
<td>0.9.0</td>
</tr>
</table>
<h1>1 Description</h1>
<p>Helpful Ruby routines for parsing orgmode files. The most
  significant thing this library does today is convert orgmode files
  to textile. Currently, you cannot do much to customize the
  conversion. The supplied textile conversion is optimized for
  extracting “content” from the orgfile as opposed to “metadata.”</p>
<h1>2 History</h1>
<h2>2.1 2014-02-08: Version 0.9.0</h2>
<ul>
  <li>Let’s make sure <code>#+INCLUDE:</code> is not supported</li>
</ul>
<ul>
  <li>And confirm that syntax highlight is supported</li>
</ul>
<pre lang="ruby">
module GitHub
  module Markup
    VERSION = 'test'
    Version = VERSION
  end
end
</pre>
<h2>2.2 2009-12-30: Version 0.5.1</h2>
<ul>
  <li>Minor enhancement: Recognize lines starting with “:” as examples.</li>
  <li>Minor enhancement: Recognize #+BEGIN_SRC as source blocks</li>
  <li>Minor enhancement: Add “src” and “example” classes to &lt;pre&gt; blocks.</li>
</ul>
<h2>2.3 2009-12-30: Version 0.5.0</h2>
<ul>
  <li>Parse (but not necessarily <b>use</b>) in-buffer settings. The following
    in-buffer settings <b>are</b> used:
    <ul>
      <li>Understand the #+TITLE: directive.</li>
      <li>Exporting todo keywords (option todo:t)</li>
      <li>Numbering headlines (option num:t)</li>
      <li>Skipping text before the first headline (option skip:t)</li>
      <li>Skipping tables (option |:nil)</li>
      <li>Custom todo keywords</li>
      <li>EXPORT_SELECT_TAGS and EXPORT_EXLUDE_TAGS for controlling parts of
        the tree to export</li>
    </ul>
  </li>
  <li>Rewrite “file:(blah).org” links to “http:(blah).html” links. This
    makes the inter-links to other org-mode files work.</li>
  <li>Uses &lt;th&gt; tags inside table rows that precede table separators.</li>
  <li>Bugfixes:
    <ul>
      <li>Headings now have HTML escaped.</li>
    </ul>
  </li>
</ul>
<h2>2.4 2009-12-29: Version 0.4.2</h2>
<ul>
  <li>Got rid of the extraneous newline at the start of code blocks.</li>
  <li>Everything now shows up in code blocks, even org-mode metadata.</li>
  <li>Fixed bugs:
    <ul>
      <li>Regressed smart double quotes with HTML escaping. Added a test
        case and fixed the regression.</li>
    </ul>
  </li>
</ul>
<h2>2.5 2009-12-29: Version 0.4.1</h2>
<ul>
  <li>HTML is now escaped by default</li>
  <li>org-mode comments will show up in a code block.</li>
</ul>
<h2>2.6 2009-12-29: Version 0.4</h2>
<ul>
  <li>The first thing output in HTML gets the class “title”</li>
  <li>HTML output is now indented</li>
  <li>Proper support for multi-paragraph list items.
    <p>See? This paragraph is part of the last bullet.</p>
  </li>
  <li>Fixed bugs:
    <ul>
      <li>“rake spec” wouldn’t work on Linux. Needed “require ‘rubygems’”.</li>
    </ul>
  </li>
</ul>
<h2>2.7 2009-12-27: Version 0.3</h2>
<ul>
  <li>Uses rubypants to get better typography (smart quotes, ellipses, etc…).</li>
  <li>Fixed bugs:
    <ul>
      <li>Tables and lists did not get properly closed at the end of file</li>
      <li>You couldn’t do inline formatting inside table cells</li>
      <li>Characters in PRE blocks were not HTML escaped.</li>
    </ul>
  </li>
</ul>
<h2>2.8 2009-12-26: Version 0.2</h2>
<ul>
  <li>Added <code>to_html</code> output on the parser.</li>
  <li>Added support for the full range of inline markup: <b>bold</b>,
    <i>italic</i>, <code>code</code>, <code>verbatim</code>, underline, <del>strikethrough</del>.</li>
  <li>Lots of refactoring to make the code more maintainable.</li>
</ul>
<h2>2.9 2009-12-23: Version 0.1</h2>
<ul>
  <li>Added support for block code, like this:
    <pre>
  def flush!
  @logger.debug "FLUSH ==========&gt; #{@output_type}"
  if (@output_type == :blank) then
    @output &lt;&lt; "\n"
  elsif (@buffer.length &gt; 0) then
    if @cancel_modifier then
      @output &lt;&lt; "p. " if @output_type == :paragraph
      @cancel_modifier = false
    end
    @output &lt;&lt; @paragraph_modifier if (@paragraph_modifier and not sticky_modifier?)
    @output &lt;&lt; @buffer.textile_substitution &lt;&lt; "\n"
  end
  @buffer = ""
end
    </pre>
  </li>
  <li>Major code cleanup: Created the <code>OutputBuffer</code> class that
    greatly simplified a lot of the messiness of <code>textile</code>
    conversion.</li>
  <li>Added support for line breaks within list items.</li>
</ul>Header 1
========
--------
Subtitle
--------

Example text.

.. contents:: Table of Contents

Header 2
--------

1. Blah blah ``code`` blah

2. More ``code``, hooray

3. Somé UTF-8°

The UTF-8 quote character in this table used to cause python to go boom. Now docutils just silently ignores it.

.. csv-table:: Things that are Awesome (on a scale of 1-11)
	:quote: ”

	Thing,Awesomeness
	Icecream, 7
	Honey Badgers, 10.5
	Nickelback, -2
	Iron Man, 10
	Iron Man 2, 3
	Tabular Data, 5
	Made up ratings, 11

.. code::

	A block of code

.. code:: python

	python.code('hooray')

.. doctest:: ignored

	>>> some_function()
	'result'

>>> some_function()
'result'

==============  ==========================================================
Travis          http://travis-ci.org/tony/pullv
Docs            http://pullv.rtfd.org
API             http://pullv.readthedocs.org/en/latest/api.html
Issues          https://github.com/tony/pullv/issues
Source          https://github.com/tony/pullv
==============  ==========================================================


.. image:: https://scan.coverity.com/projects/621/badge.svg
	:target: https://scan.coverity.com/projects/621
	:alt: Coverity Scan Build Status

.. image:: https://scan.coverity.com/projects/621/badge.svg
	:alt: Coverity Scan Build Status

Field list
----------

:123456789 123456789 123456789 123456789 123456789 1: Uh-oh! This name is too long!
:123456789 123456789 123456789 123456789 1234567890: this is a long name,
	but no problem!
:123456789 12345: this is not so long, but long enough for the default!
:123456789 1234: this should work even with the default :)

someone@somewhere.org

Press :kbd:`Ctrl+C` to quit


.. raw:: html

    <p><strong>RAW HTML!</strong></p><style> p {color:blue;} </style>
* One
* Two
[[Home|&raquo; JRuby Project Wiki Home Page]]
<h1>Embedding JRuby</h1>
Using Java from Ruby is JRuby's best-known feature---but you can also go in the other direction, and use Ruby from Java.  There are several different ways to do this. You can execute entire Ruby scripts, call individual Ruby methods, or even implement a Java interface in Ruby (thus allowing you to treat Ruby objects like Java ones).  We refer to all these techniques generically as "embedding."  This section will explain how to embed JRuby in your Java project.

__TOC__

= Red Bridge (JRuby Embed) =

<tt>one-<two</tt>
<pre>a-b</pre>

JRuby has long had a private embedding API, which was closely tied to the runtime's internals and therefore changed frequently as JRuby evolved. Since version 1.4, however, we have also provided a more stable public API, known as Red Bridge or JRuby Embed. Existing Java programs written to the [[DirectJRubyEmbedding|legacy API]] should still work, but we strongly recommend Red Bridge for all new projects.

== Features of Red Bridge ==
Red Bridge consists of two layers: Embed Core on the bottom, and implementations of [http://www.jcp.org/en/jsr/detail?id=223 JSR223] and [http://jakarta.apache.org/bsf/ BSF] on top. Embed Core is JRuby-specific, and can take advantage of much of JRuby's power. JSR223 and BSF are more general interfaces that provide a common ground across scripting languages.

Which API should you use? For projects where Ruby is the only scripting language involved, we recommend Embed Core for the following reasons:

# With Embed Core, you can create several Ruby environments in one JVM, and configure them individually (via <code>org.jruby.RubyInstanceConfig</code>. With the other APIs, configuration options can only be set globally, via the <code>System</code> properties.
# Embed Core offers several shortcuts, such as loading scripts from a <code>java.io.InputStream</code>, or returning Java-friendly objects from Ruby code. These allow you to skip a lot of boilerplate.

For projects requiring multiple scripting languages, JSR223 is a good fit. Though the API is language-independent, JRuby's implementation of it allows you to set some Ruby-specific options. In particular, you can control the threading model of the scripting engine, the lifetime of local variables, compilation mode, and how line numbers are displayed.

The full [http://jruby-embed.kenai.com/docs/ API documentation] has all the gory details. It's worth talking about a couple of the finer points here.

= Previous Embedding JRuby Page=
We recommend using Embed Core; however, if you're maintaining code that uses the old API, you can find its documentation on the [[JavaIntegration|legacy embedding]]<ref>This link goes nowhere.</ref> page.

= References =
<references/>
<h1>restructuredText (rst) directives and comments</h1>
<a name="introduction"></a>
<h2>Introduction</h2>
<p>An rst directive starts with two periods, and has a keyword
followed by two colons, like this:</p>
<pre>
.. MyDirective::
</pre>
<p>The rst parser is quite flexible and configurable.  Directives
may be added for specialized operations.  Sphinx is a system
that was designed for writing documentation, and, for example,
readthedocs.org uses sphinx.</p>
<p>Display of rst files at github needs to cover two distinct
use-cases:</p>
<ul>
<li>The github display is the primary method for displaying
the file (e.g. for README.rst files)</li>
<li>The github display is incidental to the primary method
for displaying the file (e.g. for readthedocs documentation)</li>
</ul>
<p>Currently, github handles the first case fine, but could
confuse viewers for the second case, because sometimes
content is missing from the github display.</p>
<p>It would seem that one possibility for distinguishing these
two cases is to add a github directive to control the display.</p>
<p>Unfortunately, this would place a burden on every other rst
parser to ignore the github directive (some of them will error
on unknown directives).</p>
<p>Instead, we can assign semantic content to specific comments.</p>
<p>This is a fairly ugly hack, but it has the benefit of not
requiring any document changes that would create problems with
any conformant parser.</p>
<p>The proposed special comment is:</p>
<pre>
.. github display [on | off]
</pre>
<p>If you pass this the "on" value, then all unknown directives
will be displayed as literal code blocks.  If you pass this
the "off" value, then unknown directives will not be displayed.</p>
<p>In addition to controlling the display of literal code blocks,
this also allows you to show comments specifically for github.</p>
<p>For example, somebody could place this at the top of their file:</p>
<pre>
.. github display

  This file was designed to be viewed at readthedocs.  Some
  content will not display properly when viewing using the
  github browser.
</pre>
<a name="tests"></a>
<h2>Tests</h2>
<p>By default, unknown directives should be displayed.</p>
<pre>
.. UnknownDirective::  This is an unknown directive

      it has a lot of stuff underneath it

</pre>
<p>But we can turn this off, and the next directive should
not be displayed.</p>
<p>Or we can turn it back on...</p>
<pre>
.. UnknownDirective::  This is an unknown directive (3)

      it has a lot of stuff underneath it

</pre>
<p>Here is a comment that should display at github</p>
<pre>

YOU SHOULD SEE THIS!
</pre>
<p>And here is a comment that should not display at github</p>
<p>This concludes the tests.</p>Literate CoffeeScript Test
--------------------------

> Taken from https://github.com/jashkenas/coffee-script/blob/master/test/literate.litcoffee

comment comment

    test "basic literate CoffeeScript parsing", ->
      ok yes

now with a...

    test "broken up indentation", ->

... broken up ...

      do ->

... nested block.

        ok yes

Code must be separated from text by a blank line.

    test "code blocks must be preceded by a blank line", ->

The next line is part of the text and will not be executed.
      fail()

      ok yes

Code in `backticks is not parsed` and...

    test "comments in indented blocks work", ->
      do ->
        do ->
          # Regular comment.

          ###
            Block comment.
          ###

          ok yes

Regular [Markdown](http://example.com/markdown) features,
like links and unordered lists, are fine:

  * I

  * Am

  * A

  * List

Tabs work too:

  test "tabbed code", ->
    ok yes
= Document Title

== First Section

* One
* Two

Refer to <<another-section>> or <<another-section-1>>.

Navigate from {docname}{outfilesuffix} to <<another-document#,another document>>.

== Another Section

NOTE: Here is some source code.

```ruby
puts "Hello, World!"
```

* [ ] todo
* [x] done

== Another Section

content
.. contents::
    :backlinks: none

.. sectnum::

Introduction
============

What is pycparser?
------------------

**pycparser** is a parser for the C language, written in pure Python. It is a
module designed to be easily integrated into applications that need to parse
C source code.

What is it good for?
--------------------

Anything that needs C code to be parsed. The following are some uses for
**pycparser**, taken from real user reports:

* C code obfuscator
* Front-end for various specialized C compilers
* Static code checker
* Automatic unit-test discovery
* Adding specialized extensions to the C language

**pycparser** is unique in the sense that it's written in pure Python - a very
high level language that's easy to experiment with and tweak. To people familiar
with Lex and Yacc, **pycparser**'s code will be simple to understand.
=head1 Matrixy

=head2 INTRODUCTION

This is a port of the MATLAB/Octave programming language to Parrot. See the
ROADMAP file for more information on the status of this project, and what else
needs to be done.

=head2 ABOUT

Primary goals are:

=over 4

=item * Create a working compiler that understands the majority of the
MATLAB/Octave programming language.

=back

=head2 IMPLEMENTATION

This project is broken into three primary components:

=over 4

=item * The first is the parser, located in the C<src/parser/> directory. The
parser proper is composed of three source files, F<grammar.pg> which is a
Perl6Grammar file, and F<actions.pm> which is the associated actions file
written in NQP, and F<grammar-oper.pm> which is the operator precedence parser.
In addition, several helper functions used by the parser are located in
C<src/internals>.

=item * The second component is the library of builtin functions in the
C<src/builtins/> directory. These functions are, currently, written primarily in
PIR. Function names prefixed with an underscore are "private" functions for use
with the parser. Other functions should have names which are the same as names
for regular MATLAB or Octave functions, since they will be available to the
HLL. These are also separated into different namespaces depending on visibility
and utility.

=item * A number of library functions are written in M, or mostly M with some
inline PIR code in C<toolbox/>.

=back

=head2 DEPENDENCIES

Matrixy depends on these dependencies:

=head3 Parrot

To get a proper version of Parrot to build Matrixy, you will need to check out
and build Parrot from source:

    svn co http://svn.parrot.org/parrot/trunk parrot
    cd parrot
    perl Configure.pl
    make && make test && make install-dev

=head3 Parrot-Linear-Algebra

The linear algebra package for Parrot is available separately and provides
functionality required by Matrixy. This includes matrix data types and matrix
manipulation libraries

=head2 BUILDING

Once all dependencies are in place, you can build Matrixy using this sequence of
commands:

    perl Configure.pl
    nmake test

=head2 TODO

    * Parser
    * Standard Builtins
    * Test against Octave Test Suite.

=head2 BUGS

Lots!

=head2 CONTACT

If you need to contact the Matrixy team, go to the project home page at:

www.github.com\Whiteknight\matrixy

<h1>Header 1</h1>
<h2>Subtitle</h2>
<p>Example text.</p>
<div>
<p>Table of Contents</p>
<ul>
<li><a href="#header-2">Header 2</a></li>
<li><a href="#field-list">Field list</a></li>
</ul>
</div>
<a name="header-2"></a>
<h2><a href="#id1">Header 2</a></h2>
<ol>
<li>Blah blah <code>code</code> blah</li>
<li>More <code>code</code>, hooray</li>
<li>Somé UTF-8°</li>
</ol>
<p>The UTF-8 quote character in this table used to cause python to go boom. Now docutils just silently ignores it.</p>
<pre>
A block of code
</pre>
<pre lang="python">
python.code('hooray')
</pre>
<pre lang="python">
&gt;&gt;&gt; some_function()
'result'
</pre>
<pre lang="pycon">
&gt;&gt;&gt; some_function()
'result'
</pre>
<table>




<tbody valign="top">
<tr>
<td>Travis</td>
<td><a href="http://travis-ci.org/tony/pullv">http://travis-ci.org/tony/pullv</a></td>
</tr>
<tr>
<td>Docs</td>
<td><a href="http://pullv.rtfd.org">http://pullv.rtfd.org</a></td>
</tr>
<tr>
<td>API</td>
<td><a href="http://pullv.readthedocs.org/en/latest/api.html">http://pullv.readthedocs.org/en/latest/api.html</a></td>
</tr>
<tr>
<td>Issues</td>
<td><a href="https://github.com/tony/pullv/issues">https://github.com/tony/pullv/issues</a></td>
</tr>
<tr>
<td>Source</td>
<td><a href="https://github.com/tony/pullv">https://github.com/tony/pullv</a></td>
</tr>
</tbody>
</table>
<a href="https://scan.coverity.com/projects/621"><img alt="Coverity Scan Build Status" src="https://scan.coverity.com/projects/621/badge.svg">
</a>
<img alt="Coverity Scan Build Status" src="https://scan.coverity.com/projects/621/badge.svg">
<a name="field-list"></a>
<h2><a href="#id2">Field list</a></h2>
<table frame="void" rules="none">


<tbody valign="top">
<tr><th colspan="2">123456789 123456789 123456789 123456789 123456789 1:</th></tr>
<tr>
<td> </td>
<td>Uh-oh! This name is too long!</td>
</tr>
<tr>
<th>123456789 123456789 123456789 123456789 1234567890:</th>
<td>this is a long name,
but no problem!</td>
</tr>
<tr>
<th>123456789 12345:</th>
<td>this is not so long, but long enough for the default!</td>
</tr>
<tr>
<th>123456789 1234:</th>
<td>this should work even with the default :)</td>
</tr>
</tbody>
</table>

<p><a href="mailto:someone@somewhere.org">someone@somewhere.org</a></p>

<p>Press <kbd>Ctrl+C</kbd> to quit</p>

<p><strong>RAW HTML!</strong></p> p {color:blue;}
= H1 =

== H2 ==

paragraph of text that will be turned into a paragraph element. It can
go over several lines with line breaks, it will be turned into a
contiguous paragraph element.

You can force a linebreak in your paragraph text\\thusly.


 * a list element
 ** sub list element
 * 2nd list element

{{{
pre formatted text

$ ls -la
total 56
drwxr-xr-x   6 nferrier users  4096 Jul  5 23:10 .
drwxr-x--- 120 nferrier users 12288 Jul  5 19:36 ..
drwxr-xr-x   2 nferrier users  4096 Jul  5 18:19 bin
-rw-r--r--   1 nferrier users     6 Jul  5 18:19 .gitignore
drwxr-xr-x   4 nferrier users  4096 Jul  5 23:10 .hg
-rw-r--r--   1 nferrier users  1182 Jul  5 18:19 HISTORY.md
-rw-r--r--   1 nferrier users   562 Jul  5 18:19 .kick
drwxr-xr-x   3 nferrier users  4096 Jul  5 18:19 lib
-rw-r--r--   1 nferrier users  1050 Jul  5 18:19 LICENSE
-rw-r--r--   1 nferrier users  1312 Jul  5 18:19 Rakefile
-rw-r--r--   1 nferrier users  3390 Jul  5 18:19 README.md
drwxr-xr-x   3 nferrier users  4096 Jul  5 18:19 test
}}}

