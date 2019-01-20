
So you've made changes that you want to push to the world.
Congratulations!

There are three basic steps to taking what you've done and making it
into an actual official CLL release:

1.  Make everything correct in your own tree, and in particular
    under official/
2.  Make everything correct on github
3.  Releasing the results to the public

Step 1: Finishing Up Your Changes
=================================

The goal here is to finalize everything.  Most of the actual work
here is in the various chunks of the official/ directory, as
explained below.

It is also *VERY IMPORTANT* that you update the CHANGELOG!

DO THAT FIRST!

Updating XHTML official/
------------------------

Run scripts/diff_official (but see the next paragraph first!);
confirm that nothing has changed except what you want to change.

(Note that when the build asks "Would you like to diff the new
output against the last official/ build?", it is running
scripts/diff_official; so if you've already done that, you've done
this step.

scripts/diff_official makes copies of both the relevant build/ dir
and the relevant official/ dir, and massages them to make the output
easier to review.  In particular, it removes all build-time ID
numbers, that otherwise would lead to hundreds of thousands of
apparent changes.

If you have made a complicated change that is hard for a human to
review, but you can simplify the review process with a script, put
that script at scripts/diff_official-special ; if that script
exists, it will be run against every file on *both* sides of the
diff.

As an example, this mini-script finds anything that looks like a
navgiation header and removes any newlines inside it; I used this
when I changed all the nav headers so that each file had ~5 lines of
changes (easy to review) vs. ~30 lines (not so much).

    ruby -e 'puts ARGF.read.encode("UTF-8", "binary", invalid: :replace, undef: :replace, replace: "").gsub(%r{<div[^>]*(navheader|navfooter|toc-link|back-to-info-link).*?</div>}m) { |x| x.gsub(%r{\s+}," ") }' "$@"

When you're satisfied that the changes you made are the changes you
want, put the changes you want in official/ with something like
this:

    $ cp -r build/xhtml_section_chunks official/cll_v1.1_xhtml-section-chunks_2016-05-25
    $ cd official

Now you need to fix the links; you can get a list of all the links like so:

    $ find . -type l \! -name dtd

Fixing looks like this:

    $ rm cll_v1.1_xhtml-section-chunks
    $ ln -s cll_v1.1_xhtml-section-chunks_2016-05-25 cll_v1.1_xhtml-section-chunks

(Obviously, update that if we're not on version 1.1 anymore!)

(Repeat for the other 2 chunk types.)

The goal here is to make it so that every currently-relevant
file/directory has a symlink to it, and that that symlink's name
only changes when we change CLL versions.

NOTE: The - and _ in the build/ dir do not match what's in the
official/ dir.  Sorry about that.

Updating EPUB & MOBI official/
------------------------------

We check the EPUB's format with both epubchecker and kindlegen.
Since it's generated from the same xhtml as everything else (more or
less), if it passes all those tests it's probably fine.

However, it's now part of diff_official, too, since it's just a zip.

When done, copy and update symlinks as with XHTML.

Copy and update the MOBI as well; it's generated directly from the
EPUB via kindlegen.

Updating PDF official/
----------------------

Get a PDF diff viewer for your OS and compare them visually.  I'm
using https://github.com/vslavik/diff-pdf on Windows.

When done, copy and update symlinks as with XHTML.

Step 2: Updating github
=======================

The forever home of this data is the docbook-prince branch of https://github.com/lojban/cll/

Before you push, though, there are some things to do.

Make *certain* that everything is done completely (all the work
above, the CHANGELOG, etc).  Commit your changes (ideally in a very
few, very semantically distinct commits).  Rebase from the
docbook-prince branch of https://github.com/lojban/cll/ .  In other
words, get all the usual git ducks in a row.

Then you *MUST* tag your release!

The following is the complete list of tags to make, assuming you
have updated everything and intend to push the result everywhere;
modify as appropriate:

    $ git tag v1.1-[date]-mobi
    $ git tag v1.1-[date]-pdf
    $ git tag v1.1-[date]-html
    $ git tag v1.1-[date]-epub
    $ git tag v1.1-[date]-print

where "date" is the release date, i.e. something like "2017-07-13".
Obviously you can increment the release number too if appropriate.

You will then need to run:

    $ git push --all
    $ git push --tags

and confirm that it worked at https://github.com/lojban/cll/releases
and https://github.com/lojban/cll/commits/docbook-prince

Step 3: Releasing To The World
==============================

Pushing official/ To www.lojban.org
-----------------------------------

In your git directory after you've made official/ look how you want,
the following script will look for any symlinks under official/ and
tar up the symlinks and their referents:

    $ scripts/tar_official

Then check it:

    $ tar -tvf official_cll.tar | less

Then copy it over:

    $ scp official_cll.tar jukni:/tmp/

Then on the webserver (currently (Jun 2016) this is jukni):

    $ sudo -u apache mv /srv/lojban/static/publications/cll /srv/lojban/static/publications/cll.before-$(date +%Y%m%d)
    $ sudo -u apache mkdir /srv/lojban/static/publications/cll
    $ sudo -u apache tar -xvf /tmp/official_cll.tar -C /srv/lojban/static/publications/cll/
    $ ls -lZd /srv/lojban/static/publications/cll
    drwxr-xr-x. 5 apache apache staff_u:object_r:httpd_user_content_t:s0 4096 Aug 27 01:09 /srv/lojban/static/publications/cll/
    $ ls -lZ /srv/lojban/static/publications/cll
    total 16444
    -rw-r--r--. 1 apache apache staff_u:object_r:httpd_user_content_t:s0    3173 Aug 27 01:08 CHANGELOG
    lrwxrwxrwx. 1 apache apache staff_u:object_r:httpd_user_content_t:s0      24 Aug 27 00:47 cll_v1.1.epub -> cll_v1.1_2016-08-26.epub
    lrwxrwxrwx. 1 apache apache staff_u:object_r:httpd_user_content_t:s0      24 Aug 27 00:54 cll_v1.1.mobi -> cll_v1.1_2016-08-26.mobi
    -rw-r--r--. 1 apache apache staff_u:object_r:httpd_user_content_t:s0  491834 Apr 19 01:12 cll_v1.1_2016-04-13_cover.pdf
    -rw-r--r--. 1 apache apache staff_u:object_r:httpd_user_content_t:s0  369822 Jun 14 01:48 cll_v1.1_2016-06-12_epub-cover.jpg
    -rw-r--r--. 1 apache apache staff_u:object_r:httpd_user_content_t:s0 1661232 Aug 26 19:37 cll_v1.1_2016-08-26.epub
    -rw-r--r--. 1 apache apache staff_u:object_r:httpd_user_content_t:s0 7990646 Aug 26 19:37 cll_v1.1_2016-08-26.mobi
    -rw-r--r--. 1 apache apache staff_u:object_r:httpd_user_content_t:s0 6282332 Aug 26 19:23 cll_v1.1_2016-08-26.pdf
    lrwxrwxrwx. 1 apache apache staff_u:object_r:httpd_user_content_t:s0      23 Aug 27 00:53 cll_v1.1_book.pdf -> cll_v1.1_2016-08-26.pdf
    lrwxrwxrwx. 1 apache apache staff_u:object_r:httpd_user_content_t:s0      29 May 19 23:52 cll_v1.1_cover.pdf -> cll_v1.1_2016-04-13_cover.pdf
    lrwxrwxrwx. 1 apache apache staff_u:object_r:httpd_user_content_t:s0      34 Jun 14 06:12 cll_v1.1_epub-cover.jpg -> cll_v1.1_2016-06-12_epub-cover.jpg
    lrwxrwxrwx. 1 apache apache staff_u:object_r:httpd_user_content_t:s0      40 Aug 27 00:49 cll_v1.1_xhtml-chapter-chunks -> cll_v1.1_xhtml-chapter-chunks_2016-08-26/
    drwxr-xr-x. 3 apache apache staff_u:object_r:httpd_user_content_t:s0    4096 Aug 26 18:53 cll_v1.1_xhtml-chapter-chunks_2016-08-26/
    lrwxrwxrwx. 1 apache apache staff_u:object_r:httpd_user_content_t:s0      35 Aug 27 00:25 cll_v1.1_xhtml-no-chunks -> cll_v1.1_xhtml-no-chunks_2016-08-26/
    drwxr-xr-x. 3 apache apache staff_u:object_r:httpd_user_content_t:s0    4096 Aug 26 19:11 cll_v1.1_xhtml-no-chunks_2016-08-26/
    lrwxrwxrwx. 1 apache apache staff_u:object_r:httpd_user_content_t:s0      40 Aug 27 00:52 cll_v1.1_xhtml-section-chunks -> cll_v1.1_xhtml-section-chunks_2016-08-26/
    drwxr-xr-x. 3 apache apache staff_u:object_r:httpd_user_content_t:s0   20480 Aug 26 19:04 cll_v1.1_xhtml-section-chunks_2016-08-26/

Note that the selinux stuff there is important.

Then confirm that all of the following addresses work:

http://lojban.org/publications/cll/cll_v1.1.epub
http://lojban.org/publications/cll/cll_v1.1_epub-cover.jpg
http://lojban.org/publications/cll/cll_v1.1.mobi
http://lojban.org/publications/cll/cll_v1.1_book.pdf
http://lojban.org/publications/cll/cll_v1.1_cover.pdf
http://lojban.org/publications/cll/cll_v1.1_xhtml-chapter-chunks/
http://lojban.org/publications/cll/cll_v1.1_xhtml-no-chunks/
http://lojban.org/publications/cll/cll_v1.1_xhtml-section-chunks/

(Obviously, update that if we're not on version 1.1 anymore!)

Pushing official/ To Dead Tree Books
------------------------------------

Go to https://myaccount.ingramspark.com/Titles/TitleInfo/CSS1956560
using the LLG's account (Riley or Robin or Bob should have access).

Click "Upload New Files".  Upload the files.

Errors about transparency and color profiles that say "The good news
is that we can correct the file error(s) for you at no charge." can
be ignored (i.e. you should ask Ingram to fix them) (although if you
can figure out how to make the automation *not* cause those errors,
you should totally do that).

When the fixes are done and the version is approved and so on, go
back to the Title Details (same link as above) and update the
Edition Description.

Pushing official/ To Kindle Direct Publishing E-Books
-----------------------------------------------------
Note that this is the *MORE* important of the two e-book
destinations.

Go to https://kdp.amazon.com/en_US/title-setup/kindle/A31M4HTHVJGEWW/details
using the LLG's account (Riley or Robin or Bob should have access).

Update the Edition Number and anything else that seems relevant;
click Save And Continue.

Upload the new files; click Save And Continue.

Update pricing info if needed; click Publish.

Pushing official/ To Ingram Spark E-Books
-----------------------------------------

Note that this is the *LESS* important of the two e-book
destinations.

Go to https://myaccount.ingramspark.com/Titles/TitleInfo/CSS2977442
using the LLG's account (Riley or Robin or Bob should have access).

Click "Upload New Files".  Upload the files.

When the fixes are done and the version is approved and so on, go
back to the Title Details (same link as above) and update the
Edition Description.

This is about the <anchor.../> tags in the text, which (except for
bits in chapters 20 and 21) are SOLELY A BACKWARDS COMPATIBILITY
MEASURE.

As such, the <anchor.../> tags should NEVER be updated, even when
things are moved.

The below is how our anchors used to work, and how they map to the
new system, and was originally copied from https://github.com/lojban/cll/issues/82

- ---------

Old CLL html Chapter 5 Example 2.3 is:

    http://www.lojban.org/publications/reference_grammar/chapter5.html#e2d3

github.io/dag-cll Chapter 5 Example 2.3 is:

    https://lojban.github.io/cll/5/2/#e3

These are both terrible as they rely on the chunking behaviour selected! That is: if the file is one big chunk, neither of these methods can possibly work.

I don't know what that means in terms of our ability to generate such anchors.

Section URLs:

    old: http://www.lojban.org/publications/reference_grammar/chapter5.html#s2
    dag-cll: https://lojban.github.io/cll/5/2/

So the thing is that pre-CLLv1.1 URLs are reliably convertible to CLLv1.1 URLs, just not at the anchor level. In particular, this:

    http://vrici.lojban.org/~rlpowell/media/public/cll_build/cll-xhtml-nochunks/#c5e2d3

is the equivalent of both of the example URLs above, and this:

    http://vrici.lojban.org/~rlpowell/media/public/cll_build/cll-xhtml-nochunks/#c5s2

Notice that these conversions can easily be achieved by Apache mod_rewrite, but there is no sane/obvious way to do it at any other level.

If, for some reason, it is really important to make it so that, say, the chapter-chunked output of CLLv1.1 responds to [url]/chapter5.html#e2d3 , this could be done by:

    1. cp or mv chapter-selbri.html to chapter5.html

    2. Something like: sed -r -i 's;a id="c5e([0-9]+)d([0-9]+)">;&\n;' (untested)

I don't see baking that replacement into the build process as adding significant value, much easier to have whatever system is hosting CLLv1.1's output do it at the mod rewrite level.

      ============
      Introduction
      ============

The docbook for the CLL uses a lot of our own custom/homebrew xml tags.

No really.  A *lot*.

These are all auto-converted to basic docbook.  Our customization of
docbook itself is very minor; just the usual CSS and
docbook2html_config.xsl stuff.

The basic point of all the custom tags is to make it easy to enter
our own special-case stuff, and also to maintain semantic
distinctions that we might want to mark up later, whether we want to
mark them up specially right now or not.  The actual markup is done
with the "role" attribute and CSS, basically.

The following is a list of the custom tags and when to use them.
Mostly it's just in the form of examples; ask rlpowell/camgusmis if
you want more detail.

IMPORTANT: These tags (both name and structure) are not sacred; if
you can see a better way to do things, please let rlpowell/camgusmis
know.

      Simple Phrase Markup
      ====================

These are used to markup inline phrases, mostly in Lojban.

  jbophrase
  ---------

Example: "a man biting a dog at a specified place and time. But
Lojbanic events may be much more <quote>spread out</quote> than
that: <jbophrase>mi vasxu</jbophrase> (I breathe) is something
which is true during the whole of my life"

This is used for any sequence of Lojban words that is simply present
inline as normal text.  There is currently no glossary of these
phrases, although there certainly could be.

  jbophrase validity
  ------------------

A <jbophrase> that contains invalid Lojban should be <jbophrase
valid="false">, and one that contains strange or surprising Lojban
should be <jbophrase valid="iffy">, to give us the option of marking
them up with special colours or other indicators later.


  valsi
  -----

Example: "It is also possible to put the tense somewhere else in the
bridi by adding <valsi>ku</valsi> after it."

This is used for a single Lojban word when it is referenced in the
text (that is, when discussing the word, not when using its actual
meaning).  This results in a link from the Lojban glossary.

NB: This means that anything wrapped in valsi must be findable in
jbovlaste.

A special case here is compound cmavo.  Where the compound has its
own meaning that isn't necessarily composable from the parts, use a
single tag, like so:

  <valsi>.uinai</valsi>

Where it is decomposable, use two adjacent, like so:

  <valsi>je</valsi><valsi>nai</valsi>

  valsi validity
  --------------

<valsi valid="false">ro'irre'o</valsi> should be used where an
example morphologically illegal word is given, as in that example.
  
  cmevla
  ------

Like "valsi" (including validity) but with no expectation that it
can be found in a dictionary.

  diphthong
  ---------

Example: "(for example, <diphthong>io</diphthong> is pronounced
<quote>yo</quote>)"

Used to markup diphthong in discussion of morphology.

  letteral
  --------

Example: "they all end in the letter <letteral>o</letteral>, which
is otherwise a rare letter in Lojban gismu."

Used to markup individual letters when their use in Lojban is being
referred to by the text.
  
  rafsi
  -----

Example: "<para>In making a lujvo that contains <rafsi>jax-</rafsi>
for a selbri that contains <valsi>jai</valsi>,"

Used to markup a rafsi when referred to as such.
  
  morphology
  ----------

Example: "As a result, <morphology>bf</morphology> is forbidden, and
so is <morphology>sd</morphology>"

Used to markup any morphological examples not otherwise covered.
  
  inlinemath
  ----------

Example: <inlinemath>(1000 * 6) - (500 * 0) + (100 * 0) - (10 * 15) - 3 = 5847</inlinemath>

Used to wrap math that appears inline; just shorthand for docbook's
<inlineequation><mathphrase>
  
  math
  ----
  
Example: <math>(1000 * L) - (500 * A) + (100 * H) - (10 * R) - V</math>

Used to wrap math that appears as its own paragrah; just shorthand
for docbook's <informalequation><mathphrase>

  grammar-template
  ----------------

Example:

  The syntax of jeks is:</para>
  <grammar-template>
    [na] [se] JA [nai]
  </grammar-template>
  <para>parallel to eks and giheks.</para>

Used to show (usually very simplified versions of) the Lojban formal
grammatical productions.

  definition
  ----------

Example:

  <definition>
    <valsi>bridi</valsi> <content>x1 is a predicate relationship with relation x2 (abstraction) among arguments (sequence/set) x3</content>
  </definition>

Used to denote a free-standing definition for a Lojban word (as opposed to the
cmavo-list sections).

      The cmavo Lists
      ===============

At the top of most sections, and sometimes embedded throughout, is a list of
cmavo, with (at least) the cmavo, a selmaho, and a description.

Basic Example:

    <cmavo-list>
      <cmavo-entry>
        <cmavo>bo</cmavo>
        <selmaho>BO</selmaho>
        <description>closest scope grouping</description>
      </cmavo-entry>
    </cmavo-list>

Example that covers the attitudinal version:

    <cmavo-entry>
      <cmavo>.u'i</cmavo>
      <attitudinal-scale point="sai">amusement</attitudinal-scale>
      <attitudinal-scale point="nai">weariness</attitudinal-scale>
    </cmavo-entry>
    
Example that covers the sumtcita version:

    <cmavo-entry>
      <cmavo>bai</cmavo>
      <gismu>bapli</gismu>
      <modal-place>compelled by</modal-place>
      <modal-place se="se">compelling</modal-place>
    </cmavo-entry>

THere's also a <cmavo-list-head> which works just like a normal
table/list head, and only actually occurs once so far.

      Examples
      ========

A truly staggering percentage of the CLL consists of what it calls
"examples" (they usually aren't examples of anything really, but
that's neither here nor there).  These come in a few set patterns,
which we've codified.  Each of these comes with a bunch of sub-tags,
as well, that are only valid inside examples.

VERY IMPORTANT:

  <example role="interlinear-gloss-example" xml:id="random-id-jig0">

the id is a random string to be used for anchors only, i.e. not for
humans.  It should never be changed or removed.  It should follow
the example around forever (unless the example itself is removed, of
course).

Note that the <jbo> tags here can also take valid="false" and
valid="iffy", like <jbophrase>.

  interlinear-gloss-example
  -------------------------

(This is a technical linguistics term for word-by-word
pseudo-translations; see
http://www.eva.mpg.de/lingua/resources/glossing-rules.php )

Example:

    <example role="interlinear-gloss-example" xml:id="example-do-mamta-mi">
      <title>
        <anchor xml:id="c5e1d1"/>
      </title>
      <interlinear-gloss>
        <jbo>do mamta mi</jbo>
        <gloss>You are-a-mother-of me</gloss>
        <natlang>You are my mother</natlang>
      </interlinear-gloss>
    </example>

Inside the <interlinear-gloss>, <jbo> marks raw Lojban, <gloss> marks natural
language text (normally English) that matches the Lojban word for word, and
<natlang> marks natural language text (normally English) that more
loosely/colloquially translates the Lojban.

  pronunciation-example
  ---------------------

Example:

    <example role="pronunciation-example" xml:id="example-random-id-k2B4">
      <title>
        <anchor xml:id="c3e3d1"/>
      </title>
      <pronunciation>
        <jbo>.i.ai.i.ai.o</jbo>
        <ipa><phrase role="IPA">[ʔi ʔaj ʔi ʔaj ʔo]</phrase></ipa>
        <natlang>Ee! Eye! Ee! Eye! Oh!</natlang>
      </pronunciation>
    </example>

Similar in concept, but the <ipa> section matches the <jbo> section
in terms of sounds rather than words.

  lojbanization-example
  ---------------------

Example:

    <example role="lojbanization-example" xml:id="example-random-id-DQju">
      <title>
        <indexterm type="example-imported"><primary>cobra</primary><secondary>example</secondary></indexterm>
        <anchor xml:id="c4e7d6"/>
      </title>
      <lojbanization>
        <natlang>cobra</natlang>
        <jbo>kobra <comment>Lojbanize</comment></jbo>
        <jbo>sinc,r,kobra <comment>prefix rafsi</comment></jbo>
      </lojbanization>
    </example>

Used for demonstration of conversion of a natural language word or
name into a Lojban word.  Note the <comment> tag that can be
associated with particular lines.

  lujvo-example
  -------------

Example:

    <example xml:id="example-random-id-qjbP" role="lujvo-example">
      <title>
        <indexterm type="example-imported"><primary>supper</primary><secondary>example</secondary></indexterm>
        <anchor xml:id="c4e6d5"/>
      </title>
      <lujvo-making>
        <jbo>vancysanmi</jbo>
        <veljvo>vanci sanmi</veljvo>
        <gloss><quote>evening meal</quote></gloss>
        <natlang>or <quote>supper</quote></natlang>
      </lujvo-making>
    </example>

Used to show conversion between a lujvo and the words used to make
it, and its meaning; note the new <veljvo> internal tag.

  compound-cmavo-example
  ----------------------

Example:

    <example xml:id="example-random-id-qIYK" role="compound-cmavo-example">
      <title>
        <anchor xml:id="c4e2d2"/>
      </title>
      <compound-cmavo>
        <jbo>punaijecanai</jbo>
        <jbo>pu nai je ca nai</jbo>
      </compound-cmavo>
    </example>

Used to show the breakup of compound cmavo.

      Special Cases
      =============

<phrase role="logical-vowel">A</phrase> denotes one of the A, E, O
or U vowels associated with Lojbanic logic operations.

<lujvo-making>
  <jbo>zbasai</jbo>
  <rafsi>zba + sai</rafsi>
  <score><inlinemath>(1000 * 6) - (500 * 0) + (100 * 0) - (10 * 15) - 3 = 5847</inlinemath></score>
</lujvo-making>

  landscape orientation
  ---------------------

Here's how to do a table with rows instead of columns:

<informaltable class="rotated">
      <tbody>
      <tr>
        <td><simplelist type="vert"><member>'</member><member><valsi>.y'y.</valsi></member></simplelist></td>
        <td><simplelist type="vert"><member>a</member><member><valsi>.abu</valsi></member></simplelist></td><F29>

That's from chapter 17.  The class="rotated" just sets some CSS
stuff so it doesn't get so spread out.
TO USE DOCKER:

Instead of ./cll_build below, use the same commands with:

  ./run_docker.sh

Note that it expects to need sudo to run docker commands; if that
causes a problem for you let me (rlpowell) know and we'll figure out
a fix, but needing sudo for docker is pretty common.

You don't *need* to use docker, but if you don't you'll have to put
together all the requirements yourself, and they'll need to match
versions, and so on.  I really strongly suggest using the Docker
version.

- ---

To make all the versions do:

  ./cll_build

The final results will end up under the build/ directory, scattered
about in various places.  If you would like the final outputs only
to be copied to another directory, you can use the -a option, so for example:

  ./cll_build -a output/

would put all the outputs in the output/ directory, whereas

  ./cll_build -a ~/public_html/cll_build/

would put them in your personal webspace.

Running a complete build takes quite a while (like probably at least
an hour).  To do it for just one chapter for faster testing:

  ./cll_build -t chapters/05.xml 

This does the whole book but is also much faster:

  ./cll_build -t

There are many possible sub-targets as well, which are specified
with -T, such as:

  ./cll_build -t -T pdf

You can get a complete list of targets via:

  ./cll_build -h

Requirements
------------

Getting this all working is actually a pretty huge undertaking;
you're almost certainly better off asking Robin Lee Powell for an
account on the appropriate server.

  General/HTML
  ------------

    xsltproc

    xmlto

    Normal linux tools probably like tar.  You definitely need wget,
    in particular.

    The actual docbook packages (i.e. the docbook 5.0 XSLT stuff)

    Ruby

    All the Ruby gems mentioned in Gemfile; in fact the normal way to
    do this sort of thing is:

      $ gem install bundler
      $ bundle install

    and that should get all the dependencies for you (although I
    (rlpowell) don't do it that way myself, so this is untested by me
    and you might have to do "bundle exec ..." with your build
    commands or something; regardless, there's only like 3 gem
    dependencies).

  PDF Generation
  --------------

    prince ( http://www.princexml.com/ )


  MOBI / EPUB
  -----------

    ebook-convert (from calibre, but the yum package doesn't really
    work; use the binary install at
    https://calibre-ebook.com/download_linux )

    Xvfb and xvfb-run (fake X for calibre) or a running X server
    session -- MAYBE NOT ACTUALLY NEEDED
