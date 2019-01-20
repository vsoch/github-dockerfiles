<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<html lang="en-US" xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-US">
  <head>
    <title>ReadMe for ICU 57.1</title>
    <meta name="COPYRIGHT" content=
    "Copyright (c) 1997-2016 IBM Corporation and others. All Rights Reserved." />
    <meta name="KEYWORDS" content=
    "ICU; International Components for Unicode; ICU4C; what's new; readme; read me; introduction; downloads; downloading; building; installation;" />
    <meta name="DESCRIPTION" content=
    "The introduction to the International Components for Unicode with instructions on building, installation, usage and other information about ICU." />
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
	<link type="text/css" href="./icu4c.css" rel="stylesheet"/>
  </head>

<!--
    classes to use with the "body" -
        draft - if the release note is itself a draft (May be combined with the other two)
        rc  - if the release note is a release candidate
        milestone - if the release note is a milestone release
-->

  <!-- <body class="rc"> -->
  <body>
    <p class="only-draft"><b>Note:</b> This is a draft readme.</p>

    <h1>
      <span class="only-draft">DRAFT</span>
      International Components for Unicode<br/>
      <span class="only-rc">Release Candidate</span>
      <span class="only-milestone">(Milestone Release)</span>
      <abbr title="International Components for Unicode">ICU</abbr> 57.1 ReadMe
    </h1>

    <!-- Shouldn't need to comment/uncomment this paragraph, just change the body class -->
    <p class="note only-milestone">This is a development milestone release of ICU
      This milestone is intended for those wishing to get an early look at new features and API changes.
      It is not recommended for production use.</p>

    <!-- Shouldn't need to comment/uncomment this paragraph, just change the body class -->
    <p class="note only-rc">This is a release candidate version of ICU4C.
      It is not recommended for production use.</p>

    <p>Last updated: 2016-Mar-21<br />
      Copyright &copy; 1997-2016 International Business Machines Corporation and
      others. All Rights Reserved.</p>
    <!-- Remember that there is a copyright at the end too -->
    <hr/>

    <h2 class="TOC">Table of Contents</h2>

    <ul class="TOC">
      <li><a href="#Introduction">Introduction</a></li>

      <li><a href="#GettingStarted">Getting Started</a></li>

      <li><a href="#News">What Is New In This release?</a></li>

      <li><a href="#Download">How To Download the Source Code</a></li>

      <li><a href="#SourceCode">ICU Source Code Organization</a></li>

      <li>
        <a href="#HowToBuild">How To Build And Install ICU</a>

        <ul >
          <li><a href="#RecBuild">Recommended Build Options</a></li>

          <li><a href="#UserConfig">User-Configurable Settings</a></li>

          <li><a href="#HowToBuildWindows">Windows</a></li>

          <li><a href="#HowToBuildCygwin">Cygwin</a></li>

          <li><a href="#HowToBuildUNIX">UNIX</a></li>

          <li><a href="#HowToBuildZOS">z/OS (os/390)</a></li>

          <li><a href="#HowToBuildOS400">IBM i family (IBM i, i5/OS, OS/400)</a></li>

		  <li><a href="#HowToCrossCompileICU">How to Cross Compile ICU</a></li>
        </ul>
      </li>


      <li><a href="#HowToPackage">How To Package ICU</a></li>

      <li>
        <a href="#ImportantNotes">Important Notes About Using ICU</a>

        <ul >
          <li><a href="#ImportantNotesMultithreaded">Using ICU in a Multithreaded
          Environment</a></li>

          <li><a href="#ImportantNotesWindows">Windows Platform</a></li>

          <li><a href="#ImportantNotesUNIX">UNIX Type Platforms</a></li>
        </ul>
      </li>

      <li>
        <a href="#PlatformDependencies">Platform Dependencies</a>

        <ul >
          <li><a href="#PlatformDependenciesNew">Porting To A New
          Platform</a></li>

          <li><a href="#PlatformDependenciesImpl">Platform Dependent
          Implementations</a></li>
        </ul>
      </li>
    </ul>
    <hr />

    <h2><a name="Introduction" href="#Introduction" id=
    "Introduction">Introduction</a></h2>

    <p>Today's software market is a global one in which it is desirable to
    develop and maintain one application (single source/single binary) that
    supports a wide variety of languages. The International Components for
    Unicode (ICU) libraries provide robust and full-featured Unicode services on
    a wide variety of platforms to help this design goal. The ICU libraries
    provide support for:</p>

    <ul>
      <li>The latest version of the Unicode standard</li>

      <li>Character set conversions with support for over 220 codepages</li>

      <li>Locale data for more than 300 locales</li>

      <li>Language sensitive text collation (sorting) and searching based on the
      Unicode Collation Algorithm (=ISO 14651)</li>

      <li>Regular expression matching and Unicode sets</li>

      <li>Transformations for normalization, upper/lowercase, script
      transliterations (50+ pairs)</li>

      <li>Resource bundles for storing and accessing localized information</li>

      <li>Date/Number/Message formatting and parsing of culture specific
      input/output formats</li>

      <li>Calendar specific date and time manipulation</li>

      <li>Complex text layout for Arabic, Hebrew, Indic and Thai</li>

      <li>Text boundary analysis for finding characters, word and sentence
      boundaries</li>
    </ul>

    <p>ICU has a sister project ICU4J that extends the internationalization
    capabilities of Java to a level similar to ICU. The ICU C/C++ project is also
    called ICU4C when a distinction is necessary.</p>

    <h2><a name="GettingStarted" href="#GettingStarted" id=
    "GettingStarted">Getting started</a></h2>

    <p>This document describes how to build and install ICU on your machine. For
    other information about ICU please see the following table of links.<br />
     The ICU homepage also links to related information about writing
    internationalized software.</p>

    <table class="docTable" summary="These are some useful links regarding ICU and internationalization in general.">
      <caption>
        Here are some useful links regarding ICU and internationalization in
        general.
      </caption>

      <tr>
        <td>ICU, ICU4C &amp; ICU4J Homepage</td>

        <td><a href=
        "http://icu-project.org/">http://icu-project.org/</a></td>
      </tr>

      <tr>
        <td>FAQ - Frequently Asked Questions about ICU</td>

        <td><a href=
        "http://userguide.icu-project.org/icufaq">http://userguide.icu-project.org/icufaq</a></td>
      </tr>

      <tr>
        <td>ICU User's Guide</td>

        <td><a href=
        "http://userguide.icu-project.org/">http://userguide.icu-project.org/</a></td>
      </tr>

      <tr>
        <td>How To Use ICU</td>

        <td><a href="http://userguide.icu-project.org/howtouseicu">http://userguide.icu-project.org/howtouseicu</a></td>
      </tr>

      <tr>
        <td>Download ICU Releases</td>

        <td><a href=
        "http://site.icu-project.org/download">http://site.icu-project.org/download</a></td>
      </tr>

      <tr>
        <td>ICU4C API Documentation Online</td>

        <td><a href=
        "http://icu-project.org/apiref/icu4c/">http://icu-project.org/apiref/icu4c/</a></td>
      </tr>

      <tr>
        <td>Online ICU Demos</td>

        <td><a href=
        "http://demo.icu-project.org/icu-bin/icudemos">http://demo.icu-project.org/icu-bin/icudemos</a></td>
      </tr>

      <tr>
        <td>Contacts and Bug Reports/Feature Requests</td>

        <td><a href=
        "http://site.icu-project.org/contacts">http://site.icu-project.org/contacts</a></td>
      </tr>
    </table>

    <p><strong>Important:</strong> Please make sure you understand the <a href=
    "http://source.icu-project.org/repos/icu/icu/trunk/LICENSE">Copyright and License Information</a>.</p>

    <h2><a name="News" href="#News" id="News">What is new in this
    release?</a></h2>

    <h3>API Changes</h3>
    <p>See the <a href="APIChangeReport.html">API Change Report</a> for a complete
      list of APIs added, removed, or changed in this release.</p>

    <!-- ICU 57 items -->
    <h3>ICU 57: Changes related to new CLDR data and specifications</h3>
    <ul>
    	<li>Time formats may include the new day period characters b, B, and
    	these may produced in response to the new skeleton character C used
    	with DateTimePatternGenerator.</li>
    	<li>In day period rules, the use of "after" has been deprecated.</li>
    	<li>The measurement unit "proportion-karat" has been renamed to
    	"concentr-karat".</li>
    </ul>

    <!-- ICU 56 items -->
    <h3>ICU 56: COLON withdrawn as date/time pattern character</h3>
    <p>In ICU 55, COLON was introduced as a date/time pattern character
      to be replaced by the value of the timeSeparator for the number
      system being used; a corresponding new UDateFormatField
      UDAT_TIME_SEPARATOR_FIELD was added. Use of COLON caused some
      backwards compatibility problems, so it is being withdrawn as a
      pattern character. However, UDAT_TIME_SEPARATOR_FIELD remains
      as does the mechanism for replacing a pattern character with the
      value of the timeSeparator; a new pattern character may be
      assigned in the future.</p>

    <h3>ICU 56: ICU Plugins are disabled by default</h3>
    <p>ICU Plugins are now disabled by default. They may be enabled
      with the configure option
      <tt>--enable-plugins</tt> or by means of
      <tt>#define UCONFIG_ENABLE_PLUGINS</tt>.
	</p>

    <!-- ICU 55 items -->
    <h3>ICU 55: Layout Engine breaking API change</h3>
    <p>The LayoutEngine (already deprecated) has had the function
      <tt>LEFontInstance::getFontTable(LETag, size_t &amp;length)</tt>
      since ICU 52. Its implementation was optional. In ICU 55, this
      version
      of <tt>getFontTable</tt> has been made pure virtual, and the
      version without a length (<tt>getFontTable(LETag)</tt>) has been
      completely removed. This is a breaking change for users who have
      not implemented the two-argument <tt>getFontTable()</tt>
      function in their <tt>LEFontInstance</tt> subclasses.
      The break is intentional, as the one-argument version cannot be
      made secure. See <tt>LEFontInstance</tt> api docs for more detail.
    </p>

    <h3>ICU 55: Deprecations in PluralRules (plurrule.h)</h3>
    <p>The following PluralRules methods never had an implementation
      but were inadvertently marked @stable; they have now been
      deprecated. [#<a href="http://bugs.icu-project.org/trac/ticket/10759">10759</a>]</p>
    <ul>
      <li><tt>double icu::PluralRules::getUniqueKeywordValue(const UnicodeString&amp;)</tt></li>
      <li><tt>int32_t icu::PluralRules::getAllKeywordValues(const UnicodeString&amp;, double*, int32_t, UErrorCode&amp;)</tt></li>
    </ul>

    <h3>ICU 55: Deprecate uidna.h functions for IDNA2003 support</h3>
    <p>The IDNA2003 API has been deprecated; use the API for IDNA2008 / UTS #46 instead via
      uidna_openUTS46() or class IDNA [#<a href="http://bugs.icu-project.org/trac/ticket/8477">8477</a>].
      This applies to the following:</p>
    <ul>
      <li><tt>enum  value UIDNA_ALLOW_UNASSIGNED</tt></li>
      <li><tt>uidna_IDNToASCII</tt></li>
      <li><tt>uidna_IDNToUnicode</tt></li>
      <li><tt>uidna_compare</tt></li>
      <li><tt>uidna_toASCII</tt></li>
      <li><tt>uidna_toUnicode</tt></li>
    </ul>

    <!-- ICU 54 items -->
    <h3>ICU 54: Deprecation of Layout Engine</h3>
    <p>The LayoutEngine is now deprecated. Please
    see <a href='http://userguide.icu-project.org/layoutengine'>the
    User's Guide</a> for more details and migration recommendations.
      In the future, passing "<tt>--enable-layout</tt>" to configure
      will be required to
     enable the layout engine.</p>
    <p>
      Note that the ParagraphLayout (layoutex) library is not deprecated.
      There is a new option, <tt>--enable-layoutex</tt> which will build
      the ParagraphLayout library using <a href="http://harfbuzz.org">HarfBuzz</a>
      instead of ICU as the layout engine. See <a href="http://userguide.icu-project.org/layoutengine">
        the users' guide</a> for more information about how to build.
    </p>
    <h3>ICU 54: Deprecation of Collation Short Strings</h3>
    <p>The collation short naming scheme and its API functions are deprecated.
    Use ucol_open() with language tag collation keywords instead (see <a href="http://userguide.icu-project.org/collation/api">Collation API Details</a>). For example, <code>ucol_open("de-u-co-phonebk-ka-shifted", &amp;errorCode)</code>
     for German Phonebook order with "ignore punctuation" mode.</p>

    <h3>ICU 54: Deprecation of UCOL_TAILORINGS_VERSION</h3>
    <p>This was originally intended to be the version of collation tailorings,
    but that information is actually in the tailorings data and this
    constant has always been (and now will continue to be) 1.</p>

    <!-- ICU 53 items -->
    <h3>ICU 53: Deprecation of TimeUnitFormat</h3>
    <p>The TimeUnitFormat and its methods were actually deprecated in ICU 53 and the
    class as a whole was tagged as deprecated in that release, but the status tags for
    the individual methods did not correctly indicate the deprecated status; they
    do as of ICU 54. Use the MeasureFormat class and its methods instead.</p>

    <!-- standing item -->
    <h3>Full release notes and the latest updates</h3>
    <p>The previous list concentrates on <em>changes that affect existing
    applications migrating from previous ICU releases</em>.
    For more news about this release, as well as late-breaking news, see the
    <a href="http://site.icu-project.org/download/57">ICU download page</a>.</p>

    <!-- end of What's New items -->

    <h2><a name="Download" href="#Download" id="Download">How To Download the
    Source Code</a></h2>

    <p>There are two ways to download ICU releases:</p>

    <ul>
      <li><strong>Official Release Snapshot:</strong><br />
       If you want to use ICU (as opposed to developing it), you should download
      an official packaged version of the ICU source code. These versions are
      tested more thoroughly than day-to-day development builds of the system,
      and they are packaged in zip and tar files for convenient download. These
      packaged files can be found at <a href=
      "http://site.icu-project.org/download">http://site.icu-project.org/download</a>.<br />
       The packaged snapshots are named <strong>icu-nnnn.zip</strong> or
      <strong>icu-nnnn.tgz</strong>, where nnnn is the version number. The .zip
      file is used for Windows platforms, while the .tgz file is preferred on
      most other platforms.<br />
       Please unzip this file. </li>

      <li><strong>Subversion Source Repository:</strong><br />
       If you are interested in developing features, patches, or bug fixes for
      ICU, you should probably be working with the latest version of the ICU
      source code. You will need to check the code out of our Subversion repository to
      ensure that you have the most recent version of all of the files. See our
      <a href="http://site.icu-project.org/repository">source
      repository</a> for details.</li>
    </ul>

    <h2><a name="SourceCode" href="#SourceCode" id="SourceCode">ICU Source Code
    Organization</a></h2>

    <p>In the descriptions below, <strong><i>&lt;ICU&gt;</i></strong> is the full
    path name of the ICU directory (the top level directory from the distribution
    archives) in your file system. You can also view the <a href=
    "http://userguide.icu-project.org/design">ICU Architectural
    Design</a> section of the User's Guide to see which libraries you need for
    your software product. You need at least the data (<code>[lib]icudt</code>)
    and the common (<code>[lib]icuuc</code>) libraries in order to use ICU.</p>

    <table class="docTable" summary="The following files describe the code drop.">
      <caption>
        The following files describe the code drop.
      </caption>

      <tr>
        <th scope="col">File</th>

        <th scope="col">Description</th>
      </tr>

      <tr>
        <td>readme.html</td>

        <td>Describes the International Components for Unicode (this file)</td>
      </tr>

      <tr>
        <td>LICENSE</td>

        <td>Contains the text of the ICU license</td>
      </tr>
    </table>

    <p><br />
    </p>

    <table class="docTable" summary=
    "The following directories contain source code and data files.">
      <caption>
        The following directories contain source code and data files.
      </caption>

      <tr>
        <th scope="col">Directory</th>

        <th scope="col">Description</th>
      </tr>

      <tr>
        <td><i>&lt;ICU&gt;</i>/source/<b>common</b>/</td>

        <td>The core Unicode and support functionality, such as resource bundles,
        character properties, locales, codepage conversion, normalization,
        Unicode properties, Locale, and UnicodeString.</td>
      </tr>

      <tr>
        <td><i>&lt;ICU&gt;</i>/source/<b>i18n</b>/</td>

        <td>Modules in i18n are generally the more data-driven, that is to say
        resource bundle driven, components. These deal with higher-level
        internationalization issues such as formatting, collation, text break
        analysis, and transliteration.</td>
      </tr>

      <tr>
        <td><i>&lt;ICU&gt;</i>/source/<b>layout</b>/</td>

        <td>Contains the ICU complex text layout engine. (Deprecated)</td>
      </tr>
      <tr>
        <td><i>&lt;ICU&gt;</i>/source/<b>layoutex</b>/</td>

        <td>Contains the ICU paragraph layout engine.</td>
      </tr>

      <tr>
        <td><i>&lt;ICU&gt;</i>/source/<b>io</b>/</td>

        <td>Contains the ICU I/O library.</td>
      </tr>

      <tr>
        <td><i>&lt;ICU&gt;</i>/source/<b>data</b>/</td>

        <td>
          <p>This directory contains the source data in text format, which is
          compiled into binary form during the ICU build process. It contains
          several subdirectories, in which the data files are grouped by
          function. Note that the build process must be run again after any
          changes are made to this directory.</p>

          <p>If some of the following directories are missing, it's probably
          because you got an official download. If you need the data source files
          for customization, then please download the ICU source code from <a
          href="http://site.icu-project.org/repository">subversion</a>.</p>

          <ul>
            <li><b>in/</b> A directory that contains a pre-built data library for
            ICU. A standard source code package will contain this file without
            several of the following directories. This is to simplify the build
            process for the majority of users and to reduce platform porting
            issues.</li>

            <li><b>brkitr/</b> Data files for character, word, sentence, title
            casing and line boundary analysis.</li>

            <li><b>locales/</b> These .txt files contain ICU language and
            culture-specific localization data. Two special bundles are
            <b>root</b>, which is the fallback data and parent of other bundles,
            and <b>index</b>, which contains a list of installed bundles. The
            makefile <b>resfiles.mk</b> contains the list of resource bundle
            files.</li>

            <li><b>mappings/</b> Here are the code page converter tables. These
            .ucm files contain mappings to and from Unicode. These are compiled
            into .cnv files. <b>convrtrs.txt</b> is the alias mapping table from
            various converter name formats to ICU internal format and vice versa.
            It produces cnvalias.icu. The makefiles <b>ucmfiles.mk,
            ucmcore.mk,</b> and <b>ucmebcdic.mk</b> contain the list of
            converters to be built.</li>

            <li><b>translit/</b> This directory contains transliterator rules as
            resource bundles, a makefile <b>trnsfiles.mk</b> containing the list
            of installed system translitaration files, and as well the special
            bundle <b>translit_index</b> which lists the system transliterator
            aliases.</li>

            <li><b>unidata/</b> This directory contains the Unicode data files.
            Please see <a href=
            "http://www.unicode.org/">http://www.unicode.org/</a> for more
            information.</li>

            <li><b>misc/</b> The misc directory contains other data files which
            did not fit into the above categories. Currently it only contains
            time zone information, and a name preperation file for <a href=
            "http://www.ietf.org/rfc/rfc3490.txt">IDNA</a>.</li>

            <li><b>out/</b> This directory contains the assembled memory mapped
            files.</li>

            <li><b>out/build/</b> This directory contains intermediate (compiled)
            files, such as .cnv, .res, etc.</li>
          </ul>

          <p>If you are creating a special ICU build, you can set the ICU_DATA
          environment variable to the out/ or the out/build/ directories, but
          this is generally discouraged because most people set it incorrectly.
          You can view the <a href=
          "http://userguide.icu-project.org/icudata">ICU Data
          Management</a> section of the ICU User's Guide for details.</p>
        </td>
      </tr>

      <tr>
        <td><i>&lt;ICU&gt;</i>/source/test/<b>intltest</b>/</td>

        <td>A test suite including all C++ APIs. For information about running
        the test suite, see the build instructions specific to your platform
        later in this document.</td>
      </tr>

      <tr>
        <td><i>&lt;ICU&gt;</i>/source/test/<b>cintltst</b>/</td>

        <td>A test suite written in C, including all C APIs. For information
        about running the test suite, see the build instructions specific to your
        platform later in this document.</td>
      </tr>

      <tr>
        <td><i>&lt;ICU&gt;</i>/source/test/<b>iotest</b>/</td>

        <td>A test suite written in C and C++ to test the icuio library. For
        information about running the test suite, see the build instructions
        specific to your platform later in this document.</td>
      </tr>

      <tr>
        <td><i>&lt;ICU&gt;</i>/source/test/<b>testdata</b>/</td>

        <td>Source text files for data, which are read by the tests. It contains
        the subdirectories <b>out/build/</b> which is used for intermediate
        files, and <b>out/</b> which contains <b>testdata.dat.</b></td>
      </tr>

      <tr>
        <td><i>&lt;ICU&gt;</i>/source/<b>tools</b>/</td>

        <td>Tools for generating the data files. Data files are generated by
        invoking <i>&lt;ICU&gt;</i>/source/data/build/makedata.bat on Win32 or
        <i>&lt;ICU&gt;</i>/source/make on UNIX.</td>
      </tr>

      <tr>
        <td><i>&lt;ICU&gt;</i>/source/<b>samples</b>/</td>

        <td>Various sample programs that use ICU</td>
      </tr>

      <tr>
        <td><i>&lt;ICU&gt;</i>/source/<b>extra</b>/</td>

        <td>Non-supported API additions. Currently, it contains the 'uconv' tool
        to perform codepage conversion on files.</td>
      </tr>

      <tr>
        <td><i>&lt;ICU&gt;</i>/<b>packaging</b>/</td>

        <td>This directory contain scripts and tools for packaging the final
        ICU build for various release platforms.</td>
      </tr>

      <tr>
        <td><i>&lt;ICU&gt;</i>/source/<b>config</b>/</td>

        <td>Contains helper makefiles for platform specific build commands. Used
        by 'configure'.</td>
      </tr>

      <tr>
        <td><i>&lt;ICU&gt;</i>/source/<b>allinone</b>/</td>

        <td>Contains top-level ICU workspace and project files, for instance to
        build all of ICU under one MSVC project.</td>
      </tr>

      <tr>
        <td><i>&lt;ICU&gt;</i>/<b>include</b>/</td>

        <td>Contains the headers needed for developing software that uses ICU on
        Windows.</td>
      </tr>

      <tr>
        <td><i>&lt;ICU&gt;</i>/<b>lib</b>/</td>

        <td>Contains the import libraries for linking ICU into your Windows
        application.</td>
      </tr>

      <tr>
        <td><i>&lt;ICU&gt;</i>/<b>bin</b>/</td>

        <td>Contains the libraries and executables for using ICU on Windows.</td>
      </tr>
    </table>
    <!-- end of ICU structure ==================================== -->

    <h2><a name="HowToBuild" href="#HowToBuild" id="HowToBuild">How To Build And
    Install ICU</a></h2>

    <h3><a name="RecBuild" href="#RecBuild" id=
    "RecBuild">Recommended Build Options</a></h3>

    <p>Depending on the platform and the type of installation,
    we recommend a small number of modifications and build options.
    Note that C99 compatibility is now required.</p>
    <ul>
      <li><b>Namespace:</b> By default, unicode/uversion.h has
        "using namespace icu;" which defeats much of the purpose of the namespace.
        (This is for historical reasons: Originally, ICU4C did not use namespaces,
        and some compilers did not support them. The default "using" statement
        preserves source code compatibility.)<br />
        If this compatibility is not an issue, we recommend you turn this off
         via <code>-DU_USING_ICU_NAMESPACE=0</code>
        or by modifying unicode/uversion.h:
<pre>Index: source/common/unicode/uversion.h
===================================================================
--- source/common/unicode/uversion.h    (revision 26606)
+++ source/common/unicode/uversion.h    (working copy)
@@ -180,7 +180,8 @@
 #   define U_NAMESPACE_QUALIFIER U_ICU_NAMESPACE::

 #   ifndef U_USING_ICU_NAMESPACE
-#       define U_USING_ICU_NAMESPACE 1
+        // Set to 0 to force namespace declarations in ICU usage.
+#       define U_USING_ICU_NAMESPACE 0
 #   endif
 #   if U_USING_ICU_NAMESPACE
         U_NAMESPACE_USE
</pre>
        ICU call sites then either qualify ICU types explicitly,
        for example <code>icu::UnicodeString</code>,
        or do <code>using icu::UnicodeString;</code> where appropriate.</li>
      <li><b>Hardcode the default charset to UTF-8:</b> On platforms where
        the default charset is always UTF-8,
        like MacOS X and some Linux distributions,
        we recommend hardcoding ICU's default charset to UTF-8.
        This means that some implementation code becomes simpler and faster,
        and statically linked ICU libraries become smaller.
        (See the <a href="http://icu-project.org/apiref/icu4c/utypes_8h.html#0a33e1edf3cd23d9e9c972b63c9f7943">U_CHARSET_IS_UTF8</a>
        API documentation for more details.)<br />
        You can <code>-DU_CHARSET_IS_UTF8=1</code> or
        modify unicode/utypes.h (in ICU 4.8 and below)
        or modify unicode/platform.h (in ICU 49 and higher):
<pre>Index: source/common/unicode/utypes.h
===================================================================
--- source/common/unicode/utypes.h      (revision 26606)
+++ source/common/unicode/utypes.h      (working copy)
@@ -160,7 +160,7 @@
  * @see UCONFIG_NO_CONVERSION
  */
 #ifndef U_CHARSET_IS_UTF8
-#   define U_CHARSET_IS_UTF8 0
+#   define U_CHARSET_IS_UTF8 1
 #endif

 /*===========================================================================*/
</pre></li>
      <li><b>UnicodeString constructors:</b> The UnicodeString class has
        several single-argument constructors that are not marked "explicit"
        for historical reasons.
        This can lead to inadvertent construction of a <code>UnicodeString</code>
        with a single character by using an integer,
        and it can lead to inadvertent dependency on the conversion framework
        by using a C string literal.<br />
        Beginning with ICU 49, you should do the following:
        <ul>
          <li>Consider marking the from-<code>UChar</code>
            and from-<code>UChar32</code> constructors explicit via
            <code>-DUNISTR_FROM_CHAR_EXPLICIT=explicit</code> or similar.</li>
          <li>Consider marking the from-<code>const char*</code> and
            from-<code>const UChar*</code> constructors explicit via
            <code>-DUNISTR_FROM_STRING_EXPLICIT=explicit</code> or similar.</li>
        </ul>
        Note: The ICU test suites cannot be compiled with these settings.
      </li>
      <li><b>utf.h, utf8.h, utf16.h, utf_old.h:</b>
        By default, utypes.h (and thus almost every public ICU header)
        includes all of these header files.
        Often, none of them are needed, or only one or two of them.
        All of utf_old.h is deprecated or obsolete.<br />
        Beginning with ICU 49,
        you should define <code>U_NO_DEFAULT_INCLUDE_UTF_HEADERS</code> to 1
        (via -D or uconfig.h, as above)
        and include those header files explicitly that you actually need.<br />
        Note: The ICU test suites cannot be compiled with this setting.</li>
      <li><b>.dat file:</b> By default, the ICU data is built into
        a shared library (DLL). This is convenient because it requires no
        install-time or runtime configuration,
        but the library is platform-specific and cannot be modified.
        A .dat package file makes the opposite trade-off:
        Platform-portable (except for endianness and charset family, which
        can be changed with the icupkg tool)
        and modifiable (also with the icupkg tool).
        If a path is set, then single data files (e.g., .res files)
        can be copied to that location to provide new locale data
        or conversion tables etc.<br />
        The only drawback with a .dat package file is that the application
        needs to provide ICU with the file system path to the package file
        (e.g., by calling <code>u_setDataDirectory()</code>)
        or with a pointer to the data (<code>udata_setCommonData()</code>)
        before other ICU API calls.
        This is usually easy if ICU is used from an application where
        <code>main()</code> takes care of such initialization.
        It may be hard if ICU is shipped with
        another shared library (such as the Xerces-C++ XML parser)
        which does not control <code>main()</code>.<br />
        See the <a href="http://userguide.icu-project.org/icudata">User Guide ICU Data</a>
        chapter for more details.<br />
        If possible, we recommend building the .dat package.
        Specify <code>--with-data-packaging=archive</code>
        on the configure command line, as in<br />
        <code>runConfigureICU Linux --with-data-packaging=archive</code><br />
        (Read the configure script's output for further instructions.
        On Windows, the Visual Studio build generates both the .dat package
        and the data DLL.)<br />
        Be sure to install and use the tiny stubdata library
        rather than the large data DLL.</li>
      <li><b>Static libraries:</b> It may make sense to build the ICU code
        into static libraries (.a) rather than shared libraries (.so/.dll).
        Static linking reduces the overall size of the binary by removing
        code that is never called.<br />
        Example configure command line:<br />
        <code>runConfigureICU Linux --enable-static --disable-shared</code></li>
      <li><b>Out-of-source build:</b> It is usually desirable to keep the ICU
        source file tree clean and have build output files written to
        a different location. This is called an "out-of-source build".
        Simply invoke the configure script from the target location:
<pre>~/icu$ svn export http://source.icu-project.org/repos/icu/icu/trunk
~/icu$ mkdir trunk-dev
~/icu$ cd trunk-dev
~/icu/trunk-dev$ ../trunk/source/runConfigureICU Linux
~/icu/trunk-dev$ make check</pre><br/>
        (Note: this example shows a relative path to
         <code>runConfigureICU</code>. If you experience difficulty,
         try using an absolute path to <code>runConfigureICU</code>
         instead.)
      </li>
    </ul>
    <h4>ICU as a System-Level Library</h4>
    <p>If ICU is installed as a system-level library, there are further
      opportunities and restrictions to consider.
      For details, see the <em>Using ICU as an Operating System Level Library</em>
      section of the <a href="http://userguide.icu-project.org/design">User Guide ICU Architectural Design</a> chapter.</p>
    <ul>
      <li><b>Data path:</b> For a system-level library, it is best to load
        ICU data from the .dat package file because the file system path
        to the .dat package file can be hardcoded. ICU will automatically set
        the path to the final install location using U_ICU_DATA_DEFAULT_DIR.
        Alternatively, you can set <code>-DICU_DATA_DIR=/path/to/icu/data</code>
        when building the ICU code. (Used by source/common/putil.c.)<br/>
        Consider also setting <code>-DICU_NO_USER_DATA_OVERRIDE</code>
        if you do not want the "ICU_DATA" environment variable to be used.
        (An application can still override the data path via
        <code>u_setDataDirectory()</code> or
        <code>udata_setCommonData()</code>.</li>
      <li><b>Hide draft API:</b> API marked with <code>@draft</code>
        is new and not yet stable. Applications must not rely on unstable
        APIs from a system-level library.
        Define <code>U_HIDE_DRAFT_API</code>, <code>U_HIDE_INTERNAL_API</code>
        and <code>U_HIDE_SYSTEM_API</code>
        by modifying unicode/utypes.h before installing it.</li>
      <li><b>Only C APIs:</b> Applications must not rely on C++ APIs from a
        system-level library because binary C++ compatibility
        across library and compiler versions is very hard to achieve.
        Most ICU C++ APIs are in header files that contain a comment with
        <code>\brief C++ API</code>.
        Consider not installing these header files.</li>
      <li><b>Disable renaming:</b> By default, ICU library entry point names
        have an ICU version suffix. Turn this off for a system-level installation,
        to enable upgrading ICU without breaking applications. For example:<br />
        <code>runConfigureICU Linux --disable-renaming</code><br />
        The public header files from this configuration must be installed
        for applications to include and get the correct entry point names.</li>
    </ul>

    <h3><a name="UserConfig" href="#UserConfig" id="UserConfig">User-Configurable Settings</a></h3>
    <p>ICU4C can be customized via a number of user-configurable settings.
    Many of them are controlled by preprocessor macros which are
    defined in the <code>source/common/unicode/uconfig.h</code> header file.
    Some turn off parts of ICU, for example conversion or collation,
    trading off a smaller library for reduced functionality.
    Other settings are recommended (see previous section)
    but their default values are set for better source code compatibility.</p>

    <p>In order to change such user-configurable settings, you can
    either modify the <code>uconfig.h</code> header file by adding
    a specific <code>#define ...</code> for one or more of the macros
    before they are first tested,
    or set the compiler's preprocessor flags (<code>CPPFLAGS</code>) to include
    an equivalent <code>-D</code> macro definition.</p>

    <h3><a name="HowToBuildWindows" href="#HowToBuildWindows" id=
    "HowToBuildWindows">How To Build And Install On Windows</a></h3>

    <p>Building International Components for Unicode requires:</p>

    <ul>
      <li>Microsoft Windows</li>

      <li>Microsoft Visual C++ (see the ICU download page for the currently compatible version)</li>
    </ul>
        <p class="note"><a href="#HowToBuildCygwin">Cygwin</a> is required if using a version of MSVC other than the one
        compatible with the supplied project files or if other compilers are used to build ICU. (e.g. GCC)</p>

    <p>The steps are:</p>

    <ol>
      <li>Unzip the icu-XXXX.zip file into any convenient location. Using command
      line zip, type "unzip -a icu-XXXX.zip -d drive:\directory", or just use
      WinZip.</li>

      <li>Be sure that the ICU binary directory, <i>&lt;ICU&gt;</i>\bin\, is
      included in the <strong>PATH</strong> environment variable. The tests will
      not work without the location of the ICU DLL files in the path.</li>

      <li>Open the "<i>&lt;ICU&gt;</i>\source\allinone\allinone.sln" workspace
      file in Microsoft Visual Studio. (This solution includes all the
      International Components for Unicode libraries, necessary ICU building
      tools, and the test suite projects). Please see the <a href=
      "#HowToBuildWindowsCommandLine">command line note below</a> if you want to
      build from the command line instead.</li>

      <li>Set the active platform to "Win32" or "x64" (See <a href="#HowToBuildWindowsPlatform">Windows platform note</a> below)
      and configuration to "Debug" or "Release" (See <a href="#HowToBuildWindowsConfig">Windows configuration note</a> below).</li>

      <li>Choose the "Build" menu and select "Rebuild Solution". If you want to
      build the Debug and Release at the same time, see the <a href=
      "#HowToBuildWindowsBatch">batch configuration note</a> below.</li>


      <li>Run the tests. They can be run from the command line or from within Visual Studio.

	 <h4>Running the Tests from the Windows Command Line (cmd)</h4>
	<ul>
	   <li>For x86 (32 bit) and Debug, use: <br />

	<tt><i>&lt;ICU&gt;</i>\source\allinone\icucheck.bat  <i>Platform</i> <i>Configuration</i>
		</tt> <br />
       </li>
	<li>So, for example:
				 <br />
		<samp><i>&lt;ICU&gt;</i>\source\allinone\icucheck.bat  <b>x86</b> <b>Debug</b></samp>
				or
		<samp><i>&lt;ICU&gt;</i>\source\allinone\icucheck.bat  <b>x86</b> <b>Release</b></samp>
				or
		<samp><i>&lt;ICU&gt;</i>\source\allinone\icucheck.bat  <b>x64</b> <b>Release</b></samp></li>
	</ul>

         <h4>Running the Tests from within Visual Studio</h4>

	<ol>
      <li>Run the C++ test suite, "intltest". To do this: set the active startup
      project to "intltest", and press Ctrl+F5 to run it. Make sure that it
      passes without any errors.</li>

      <li>Run the C test suite, "cintltst". To do this: set the active startup
      project to "cintltst", and press Ctrl+F5 to run it. Make sure that it
      passes without any errors.</li>

      <li>Run the I/O test suite, "iotest". To do this: set the active startup
      project to "iotest", and press Ctrl+F5 to run it. Make sure that it passes
      without any errors.</li>

	</ol>

	</li>

      <li>You are now able to develop applications with ICU by using the
      libraries and tools in <i>&lt;ICU&gt;</i>\bin\. The headers are in
      <i>&lt;ICU&gt;</i>\include\ and the link libraries are in
      <i>&lt;ICU&gt;</i>\lib\. To install the ICU runtime on a machine, or ship
      it with your application, copy the needed components from
      <i>&lt;ICU&gt;</i>\bin\ to a location on the system PATH or to your
      application directory.</li>
    </ol>

    <p><a name="HowToBuildWindowsCommandLine" id=
    "HowToBuildWindowsCommandLine"><strong>Using MSDEV At The Command Line
    Note:</strong></a> You can build ICU from the command line. Assuming that you
    have properly installed Microsoft Visual C++ to support command line
    execution, you can run the following command, 'devenv.com
    <i>&lt;ICU&gt;</i>\source\allinone\allinone.sln /build "Win32|Release"'. You can also
    use Cygwin with this compiler to build ICU, and you can refer to the <a href=
    "#HowToBuildCygwin">How To Build And Install On Windows with Cygwin</a>
    section for more details.</p>

    <p><a name="HowToBuildWindowsPlatform" id=
    "HowToBuildWindowsPlatform"><strong>Setting Active Platform
    Note:</strong></a> Even though you are able to select "x64" as the active platform, if your operating system is
    not a 64 bit version of Windows, the build will fail. To set the active platform, two different possibilities are:</p>

    <ul>
      <li>Choose "Build" menu, select "Configuration Manager...", and select
      "Win32" or "x64" for the Active Platform Solution.</li>

      <li>Another way is to select the desired build configuration from "Solution
      Platforms" dropdown menu from the standard toolbar. It will say
      "Win32" or "x64" in the dropdown list.</li>
    </ul>

    <p><a name="HowToBuildWindowsConfig" id=
    "HowToBuildWindowsConfig"><strong>Setting Active Configuration
    Note:</strong></a> To set the active configuration, two different
    possibilities are:</p>

    <ul>
      <li>Choose "Build" menu, select "Configuration Manager...", and select
      "Release" or "Debug" for the Active Configuration Solution.</li>

      <li>Another way is to select the desired build configuration from "Solution
      Configurations" dropdown menu from the standard toolbar. It will say
      "Release" or "Debug" in the dropdown list.</li>
    </ul>

    <p><a name="HowToBuildWindowsBatch" id="HowToBuildWindowsBatch"><strong>Batch
    Configuration Note:</strong></a> If you want to build the Win32 and x64 platforms and
    Debug and Release configurations at the same time, choose "Build" menu, and select "Batch
    Build...". Click the "Select All" button, and then click the "Rebuild"
    button.</p>

    <h3><a name="HowToBuildCygwin" href="#HowToBuildCygwin" id=
    "HowToBuildCygwin">How To Build And Install On Windows with Cygwin</a></h3>

    <p>Building International Components for Unicode with this configuration
    requires:</p>

    <ul>
      <li>Microsoft Windows</li>

      <li>Microsoft Visual C++ (when gcc isn't used).</li>

      <li>
        Cygwin with the following installed:

        <ul>
          <li>bash</li>

          <li>GNU make</li>

          <li>ar</li>

          <li>ranlib</li>

          <li>man (if you plan to look at the man pages)</li>
        </ul>
      </li>
    </ul>

    <p>There are two ways you can build ICU with Cygwin. You can build with gcc
    or Microsoft Visual C++. If you use gcc, the resulting libraries and tools
    will depend on the Cygwin environment. If you use Microsoft Visual C++, the
    resulting libraries and tools do not depend on Cygwin and can be more easily
    distributed to other Windows computers (the generated man pages and shell
    scripts still need Cygwin). To build with gcc, please follow the "<a href=
    "#HowToBuildUNIX">How To Build And Install On UNIX</a>" instructions, while
    you are inside a Cygwin bash shell. To build with Microsoft Visual C++,
    please use the following instructions:</p>

    <ol>
      <li>Start the Windows "Command Prompt" window. This is different from the
      gcc build, which requires the Cygwin Bash command prompt. The Microsoft
      Visual C++ compiler will not work with a bash command prompt.</li>

      <li>If the computer isn't set up to use Visual C++ from the command line,
      you need to run vcvars32.bat.<br />For example:<br />"<tt>C:\Program Files\Microsoft
      Visual Studio 8\VC\bin\vcvars32.bat</tt>" can be used for 32-bit builds
      <strong>or</strong> <br />"<tt>C:\Program Files (x86)\Microsoft Visual Studio
      8\VC\bin\amd64\vcvarsamd64.bat</tt>" can be used for 64-bit builds on
      Windows x64.</li>

      <li>Unzip the icu-XXXX.zip file into any convenient location. Using command
      line zip, type "unzip -a icu-XXXX.zip -d drive:\directory", or just use
      WinZip.</li>

      <li>Change directory to "icu/source", which is where you unzipped ICU.</li>

      <li>Run "<tt>bash <a href="source/runConfigureICU">./runConfigureICU</a>
      Cygwin/MSVC</tt>" (See <a href="#HowToWindowsConfigureICU">Windows
      configuration note</a> and non-functional configure options below).</li>

      <li>Type <tt>"make"</tt> to compile the libraries and all the data files.
      This make command should be GNU make.</li>

      <li>Optionally, type <tt>"make check"</tt> to run the test suite, which
      checks for ICU's functionality integrity (See <a href=
      "#HowToTestWithoutGmake">testing note</a> below).</li>

      <li>Type <tt>"make install"</tt> to install ICU. If you used the --prefix=
      option on configure or runConfigureICU, ICU will be installed to the
      directory you specified. (See <a href="#HowToInstallICU">installation
      note</a> below).</li>
    </ol>

    <p><a name="HowToWindowsConfigureICU" id=
    "HowToWindowsConfigureICU"><strong>Configuring ICU on Windows
    NOTE:</strong></a> </p>
    <p>
    Ensure that the order of the PATH is MSVC, Cygwin, and then other PATHs. The configure
    script needs certain tools in Cygwin (e.g. grep).
    </p>
    <p>
    Also, you may need to run <tt>"dos2unix.exe"</tt> on all of the scripts (e.g. configure)
    in the top source directory of ICU. To avoid this issue, you can download
    the ICU source for Unix platforms (icu-xxx.tgz).
    </p>
    <p>In addition to the Unix <a href=
    "#HowToConfigureICU">configuration note</a> the following configure options
    currently do not work on Windows with Microsoft's compiler. Some options can
    work by manually editing <tt>icu/source/common/unicode/pwin32.h</tt>, but
    manually editing the files is not recommended.</p>

    <ul>
      <li><tt>--disable-renaming</tt></li>

      <li><tt>--enable-tracing</tt></li>

      <li><tt>--enable-rpath</tt></li>

      <li><tt>--enable-static</tt> (Requires that U_STATIC_IMPLEMENTATION be
      defined in user code that links against ICU's static libraries.)</li>

      <li><tt>--with-data-packaging=files</tt> (The pkgdata tool currently does
      not work in this mode. Manual packaging is required to use this mode.)</li>
    </ul>

    <h3><a name="HowToBuildUNIX" href="#HowToBuildUNIX" id="HowToBuildUNIX">How
    To Build And Install On UNIX</a></h3>

    <p>Building International Components for Unicode on UNIX requires:</p>

    <ul>
      <li>A C++ compiler installed on the target machine (for example: gcc, CC,
      xlC_r, aCC, cxx, etc...).</li>

      <li>An ANSI C compiler installed on the target machine (for example:
      cc).</li>

      <li>A recent version of GNU make (3.80+).</li>

      <li>For a list of z/OS tools please view the <a href="#HowToBuildZOS">z/OS
      build section</a> of this document for further details.</li>
    </ul>

    <p>Here are the steps to build ICU:</p>

    <ol>
      <li>Decompress the icu-<i>X</i>.<i>Y</i>.tgz (or
      icu-<i>X</i>.<i>Y</i>.tar.gz) file. For example, <samp>gunzip -d &lt; icu-<i>X</i>.<i>Y</i>.tgz | tar xvf -</samp></li>

      <li>Change directory to <code>icu/source</code>.
          <samp>cd icu/source</samp>
          </li>

      <li>Some files may have the wrong permissions.<samp>chmod +x runConfigureICU configure install-sh</samp></li>

      <li>Run the <span style='font-family: monospace;'><a href="source/runConfigureICU">runConfigureICU</a></span>
      script for your platform. (See <a href="#HowToConfigureICU">configuration
      note</a> below).</li>

      <li>Now build: <samp>gmake</samp> (or just <code>make</code> if GNU make is the default make on
      your platform) to compile the libraries and all the data files. The proper
      name of the GNU make command is printed at the end of the configuration
      run, as in <tt>"You must use gmake to compile ICU"</tt>.
      <br/>
      Note that the compilation command output may be simplified on your platform.  If this is the case, you will see just:
      <tt>gcc ... stubdata.c</tt>
      rather than
      <tt>gcc  -DU_NO_DEFAULT_INCLUDE_UTF_HEADERS=1 -D_REENTRANT -I../common -DU_ATTRIBUTE_DEPRECATED= -O2 -Wall -std=c99 -pedantic -Wshadow -Wpointer-arith -Wmissing-prototypes -Wwrite-strings -c -DPIC -fPIC -o stubdata.o stubdata.c</tt>
      <br/>
      If you need to see the whole compilation line,  use <span style='font-family: monospace;'>"gmake VERBOSE=1"</span>. The full compilation line will print if an error occurs.
      </li>

      <li>Optionally,<samp>gmake check</samp> will run the test suite, which
      checks for ICU's functionality integrity (See <a href=
      "#HowToTestWithoutGmake">testing note</a> below).</li>

      <li>To install, <samp>gmake install</samp> to install ICU. If you used the --prefix=
      option on configure or runConfigureICU, ICU will be installed to the
      directory you specified. (See <a href="#HowToInstallICU">installation
      note</a> below).</li>
    </ol>

    <p><a name="HowToConfigureICU" id="HowToConfigureICU"><strong>Configuring ICU
    NOTE:</strong></a> Type <tt>"./runConfigureICU --help"</tt> for help on how
    to run it and a list of supported platforms. You may also want to type
    <tt>"./configure --help"</tt> to print the available configure options that
    you may want to give runConfigureICU. If you are not using the
    runConfigureICU script, or your platform is not supported by the script, you
    may need to set your CC, CXX, CFLAGS and CXXFLAGS environment variables, and
    type <tt>"./configure"</tt>.
    HP-UX users, please see this <a href="#ImportantNotesHPUX">note regarding
    HP-UX multithreaded build issues</a> with newer compilers. Solaris users,
    please see this <a href="#ImportantNotesSolaris">note regarding Solaris
    multithreaded build issues</a>.</p>

    <p>ICU is built with strict compiler warnings enabled by default.  If this
    causes excessive numbers of warnings on your platform, use the --disable-strict
    option to configure to reduce the warning level.</p>

    <p><a name="HowToTestWithoutGmake" id="HowToTestWithoutGmake"><strong>Running
    The Tests From The Command Line NOTE:</strong></a> You may have to set
    certain variables if you with to run test programs individually, that is
    apart from "gmake check". The environment variable <strong>ICU_DATA</strong>
    can be set to the full pathname of the data directory to indicate where the
    locale data files and conversion mapping tables are when you are not using
    the shared library (e.g. by using the .dat archive or the individual data
    files). The trailing "/" is required after the directory name (e.g.
    "$Root/source/data/out/" will work, but the value "$Root/source/data/out" is
    not acceptable). You do not need to set <strong>ICU_DATA</strong> if the
    complete shared data library is in your library path.</p>

    <p><a name="HowToInstallICU" id="HowToInstallICU"><strong>Installing ICU
    NOTE:</strong></a> Some platforms use package management tools to control the
    installation and uninstallation of files on the system, as well as the
    integrity of the system configuration. You may want to check if ICU can be
    packaged for your package management tools by looking into the "packaging"
    directory. (Please note that if you are using a snapshot of ICU from Subversion, it
    is probable that the packaging scripts or related files are not up to date
    with the contents of ICU at this time, so use them with caution).</p>

    <h3><a name="HowToBuildZOS" href="#HowToBuildZOS" id="HowToBuildZOS">How To
    Build And Install On z/OS (OS/390)</a></h3>

    <p>You can install ICU on z/OS or OS/390 (the previous name of z/OS), but IBM
    tests only the z/OS installation. You install ICU in a z/OS UNIX system
    services file system such as HFS or zFS. On this platform, it is important
    that you understand a few details:</p>

    <ul>
      <li>The makedep and GNU make tools are required for building ICU. If it
      is not already installed on your system, it is available at the <a href=
      "http://www-03.ibm.com/servers/eserver/zseries/zos/unix/bpxa1toy.html">z/OS UNIX -
      Tools and Toys</a> site. The PATH environment variable should be updated to
      contain the location of this executable prior to build. Failure to add these
      tools to your PATH will cause ICU build failures or cause pkgdata to fail
      to run.</li>

      <li>Since USS does not support using the mmap() function over NFS, it is
      recommended that you build ICU on a local filesystem. Once ICU has been
      built, you should not have this problem while using ICU when the data
      library has been built as a shared library, which is this is the default
      setting.</li>

      <li>Encoding considerations: The source code assumes that it is compiled
      with codepage ibm-1047 (to be exact, the UNIX System Services variant of
      it). The pax command converts all of the source code files from ASCII to
      codepage ibm-1047 (USS) EBCDIC. However, some files are binary files and
      must not be converted, or must be converted back to their original state.
      You can use the <a href="as_is/os390/unpax-icu.sh">unpax-icu.sh</a> script
      to do this for you automatically. It will unpackage the tar file and
      convert all the necessary files for you automatically.</li>

      <li>z/OS supports both native S/390 hexadecimal floating point and (with
      OS/390 2.6 and later) IEEE 754 binary floating point. This is a compile
      time option. Applications built with IEEE should use ICU DLLs that are
      built with IEEE (and vice versa). The environment variable IEEE390=0 will
      cause the z/OS version of ICU to be built without IEEE floating point
      support and use the native hexadecimal floating point. By default ICU is
      built with IEEE 754 support. Native floating point support is sufficient
      for codepage conversion, resource bundle and UnicodeString operations, but
      the Format APIs require IEEE binary floating point.</li>

      <li>z/OS introduced the concept of Extra Performance Linkage (XPLINK) to
      bring performance improvement opportunities to call-intensive C and C++
      applications such as ICU. XPLINK is enabled on a DLL-by-DLL basis, so if
      you are considering using XPLINK in your application that uses ICU, you
      should consider building the XPLINK-enabled version of ICU. You need to
      set ICU's environment variable <code>OS390_XPLINK=1</code> prior to
      invoking the make process to produce binaries that are enabled for
      XPLINK. The XPLINK option, which is available for z/OS 1.2 and later,
      requires the PTF PQ69418 to build XPLINK enabled binaries.</li>

      <li>ICU requires XPLINK for the icuio library. If you want to use the
      rest of ICU without XPLINK, then you must use the --disable-icuio
      configure option.</li>

      <li>The latest versions of z/OS use <a
      href="http://www.ibm.com/support/docview.wss?uid=swg2120240">XPLINK
      version (C128) of the C++ standard library</a> by default. You may see <a
      href="http://www.ibm.com/support/docview.wss?uid=swg21376279">an
      error</a> when running with XPLINK disabled. To avoid this error,
      set the following environment variable or similar:

<pre><samp>export _CXX_PSYSIX="CEE.SCEELIB(C128N)":"CBC.SCLBSID(IOSTREAM,COMPLEX)"</samp></pre>
      </li>

      <li>When building ICU data, the heap size may need to be increased with the following
      environment variable:

<pre><samp>export _CEE_RUNOPTS="HEAPPOOLS(ON),HEAP(4M,1M,ANY,FREE,0K,4080)"</samp></pre>
      </li>


      <li>The rest of the instructions for building and testing ICU on z/OS with
      UNIX System Services are the same as the <a href="#HowToBuildUNIX">How To
      Build And Install On UNIX</a> section.</li>
    </ul>

    <h4>z/OS (Batch/PDS) support outside the UNIX system services
    environment</h4>

    <p>By default, ICU builds its libraries into the UNIX file system (HFS). In
    addition, there is a z/OS specific environment variable (OS390BATCH) to build
    some libraries into the z/OS native file system. This is useful, for example,
    when your application is externalized via Job Control Language (JCL).</p>

    <p>The OS390BATCH environment variable enables non-UNIX support including the
    batch environment. When OS390BATCH is set, the libicui18n<i>XX</i>.dll,
    libicuuc<i>XX</i>.dll, and libicudt<i>XX</i>e.dll binaries are built into
    data sets (the native file system). Turning on OS390BATCH does not turn off
    the normal z/OS UNIX build. This means that the z/OS UNIX (HFS) DLLs will
    always be created.</p>

    <p>Two additional environment variables indicate the names of the z/OS data
    sets to use. The LOADMOD environment variable identifies the name of the data
    set that contains the dynamic link libraries (DLLs) and the LOADEXP
    environment variable identifies the name of the data set that contains the
    side decks, which are normally the files with the .x suffix in the UNIX file
    system.</p>

    <p>A data set is roughly equivalent to a UNIX or Windows file. For most kinds
    of data sets the operating system maintains record boundaries. UNIX and
    Windows files are byte streams. Two kinds of data sets are PDS and PDSE. Each
    data set of these two types contains a directory. It is like a UNIX
    directory. Each "file" is called a "member". Each member name is limited to
    eight bytes, normally EBCDIC.</p>

    <p>Here is an example of some environment variables that you can set prior to
    building ICU:</p>
<pre>
<samp>OS390BATCH=1
LOADMOD=<i>USER</i>.ICU.LOAD
LOADEXP=<i>USER</i>.ICU.EXP</samp>
</pre>

    <p>The PDS member names for the DLL file names are as follows:</p>
<pre>
<samp>IXMI<i>XX</i>IN --&gt; libicui18n<i>XX</i>.dll
IXMI<i>XX</i>UC --&gt; libicuuc<i>XX</i>.dll
IXMI<i>XX</i>DA --&gt; libicudt<i>XX</i>e.dll</samp>
</pre>

    <p>You should point the LOADMOD environment variable at a partitioned data
    set extended (PDSE) and point the LOADEXP environment variable at a
    partitioned data set (PDS). The PDSE can be allocated with the following
    attributes:</p>
<pre>
<samp>Data Set Name . . . : <i>USER</i>.ICU.LOAD
Management class. . : <i>**None**</i>
Storage class . . . : <i>BASE</i>
Volume serial . . . : <i>TSO007</i>
Device type . . . . : <i>3390</i>
Data class. . . . . : <i>LOAD</i>
Organization  . . . : PO
Record format . . . : U
Record length . . . : 0
Block size  . . . . : <i>32760</i>
1st extent cylinders: 1
Secondary cylinders : 5
Data set name type  : LIBRARY</samp>
</pre>

    <p>The PDS can be allocated with the following attributes:</p>
<pre>
<samp>Data Set Name . . . : <i>USER</i>.ICU.EXP
Management class. . : <i>**None**</i>
Storage class . . . : <i>BASE</i>
Volume serial . . . : <i>TSO007</i>
Device type . . . . : <i>3390</i>
Data class. . . . . : <i>**None**</i>
Organization  . . . : PO
Record format . . . : FB
Record length . . . : 80
Block size  . . . . : <i>3200</i>
1st extent cylinders: 3
Secondary cylinders : 3
Data set name type  : PDS</samp>
</pre>

    <h3><a name="HowToBuildOS400" href="#HowToBuildOS400" id=
    "HowToBuildOS400">How To Build And Install On The IBM i Family (IBM i, i5/OS OS/400)</a></h3>

    <p>Before you start building ICU, ICU requires the following:</p>

    <ul>
      <li>QSHELL interpreter installed (install base option 30, operating system)
      <!--li>QShell Utilities, PRPQ 5799-XEH (not required for V4R5)</li--></li>

      <li>ILE C/C++ Compiler installed on the system</li>

      <li>The latest IBM tools for Developers for IBM i &mdash;
        <a href='http://www.ibm.com/servers/enable/site/porting/tools/'>http://www.ibm.com/servers/enable/site/porting/tools/</a>
        <!-- formerly: http://www.ibm.com/servers/enable/site/porting/iseries/overview/gnu_utilities.html -->
      </li>
    </ul>

    <p>The following describes how to setup and build ICU. For background
    information, you should look at the <a href="#HowToBuildUNIX">UNIX build
    instructions</a>.</p>

    <ol>
      <li>
        Copy the ICU source .tgz to the IBM i environment, as binary.
        Also, copy the <a href='as_is/os400/unpax-icu.sh'>unpax-icu.sh</a> script into the same directory, as a text file.
      </li>

      <li>
        Create target library. This library will be the target for the
        resulting modules, programs and service programs. You will specify this
        library on the OUTPUTDIR environment variable.
<pre>
<samp>CRTLIB LIB(<i>libraryname</i>)
ADDENVVAR ENVVAR(OUTPUTDIR) VALUE('<i>libraryname</i>') REPLACE(*YES)   </samp></pre>
      </li>

      <li>
      Set up the following environment variables and job characteristics in your build process
<pre>
<samp>ADDENVVAR ENVVAR(MAKE) VALUE('gmake') REPLACE(*YES)
CHGJOB CCSID(37)</samp></pre></li>

      <li>Fire up the QSH <i>(all subsequent commands are run inside the qsh session.)</i>
        <pre><samp>qsh</samp></pre>
      </li>

      <li>Set up the PATH: <pre><samp>export PATH=/QIBM/ProdData/DeveloperTools/qsh/bin:$PATH:/QOpenSys/usr/bin</samp></pre>
      </li>

      <li>Unpack the ICU source code archive:
        <pre><samp>gzip -d icu-<i>X</i>.<i>Y</i>.tgz</samp></pre>
          </li>

      <li>Run unpax-icu.sh on the tar file generated from the previous step.
        <pre><samp>unpax-icu.sh icu.tar</samp></pre></li>

      <li>Build the program ICULD which ICU will use for linkage.
        <pre><samp>cd icu/as_is/os400
qsh bldiculd.sh
cd ../../..</samp></pre>
        </li>

      <li>Change into the 'source' directory, and configure ICU.  (See <a href="#HowToConfigureICU">configuration
      note</a> for details). Note that --with-data-packaging=archive and setting the --prefix are recommended, building in default (dll) mode is currently not supported.
        <pre><samp>cd icu/source
./runConfigureICU IBMi --prefix=<i>/path/to/somewhere</i> --with-data-packaging=archive</samp></pre>
</li>

      <li>Build ICU. <i>(Note: Do not use the -j option)</i> <pre><samp>gmake</samp></pre></li>

      <li>Test ICU. <pre><samp>gmake check</samp></pre>
        (The <tt> QIBM_MULTI_THREADED=Y</tt> flag will be automatically applied to intltest -
          you can look at the <a href=
      "http://publib.boulder.ibm.com/infocenter/iseries/v5r3/index.jsp?topic=/apis/concept4.htm">
      iSeries Information Center</a> for more details regarding the running of multiple threads
      on IBM i.)</li>
    </ol>

      <!-- cross -->
    <h3><a name="HowToCrossCompileICU" href="#HowToCrossCompileICU" id="HowToCrossCompileICU">How To Cross Compile ICU</a></h3>
		<p>This section will explain how to build ICU on one platform, but to produce binaries intended to run on another. This is commonly known as a cross compile.</p>
		<p>Normally, in the course of a build, ICU needs to run the tools that it builds in order to generate and package data and test-data.In a cross compilation setting, ICU is built on a different system from that which it eventually runs on. An example might be, if you are building for a small/headless system (such as an embedded device), or a system where you can't easily run the ICU command line tools (any non-UNIX-like system).</p>
		<p>To reduce confusion, we will here refer to the "A" and the "B" system.System "A" is the actual system we will be running on- the only requirements on it is are it is able to build ICU from the command line targetting itself (with configure or runConfigureICU), and secondly, that it also contain the correct toolchain for compiling and linking for the resultant platform, referred to as the "B" system.</p>
		<p>The autoconf docs use the term "build" for A, and "host" for B. More details at: <a href="http://www.gnu.org/software/autoconf/manual/html_node/Specifying-Names.html#Specifying-Names">http://www.gnu.org/software/autoconf/manual/html_node/Specifying-Names.html</a></p>
		<p>Three initially-empty directories will be used in this example:</p>
		<table summary="Three directories used in this example" class="docTable">
			<tr>
				<th align="left">/icu</th><td>a copy of the ICU source</td>
			</tr>
			<tr>
				<th align="left">/buildA</th><td>an empty directory, it will contain ICU built for A<br />(MacOSX in this case)</td>
			</tr>
			<tr>
				<th align="left">/buildB</th><td>an empty directory, it will contain ICU built for B<br />(HaikuOS in this case)</td>
			</tr>
		</table>

		<ol>
		<li>Check out or unpack the ICU source code into the /icu directory.You will have the directories /icu/source, etc.</li>
		<li>Build ICU in /buildA normally (using runConfigureICU or configure):
<pre class="samp">cd /buildA
sh /icu/source/runConfigureICU <strong>MacOSX</strong>
gnumake
</pre>
		</li>
		<li>Set PATH or other variables as needed, such as CPPFLAGS.</li>
		<li>Build ICU in /buildB<br />
			<p class="note">"<code>--with-cross-build</code>" takes an absolute path.</p>
<pre class="samp">cd /buildB
sh /icu/source/configure --host=<strong>i586-pc-haiku</strong> --with-cross-build=<strong>/buildA</strong>
gnumake</pre>
		</li>
		<li>Tests and testdata can be built with "gnumake tests".</li>
	</ol>
      <!-- end cross -->

    <!-- end build environment -->

    <h2><a name="HowToPackage" href="#HowToPackage" id="HowToPackage">How To
    Package ICU</a></h2>

    <p>There are many ways that a person can package ICU with their software
    products. Usually only the libraries need to be considered for packaging.</p>

    <p>On UNIX, you should use "<tt>gmake install</tt>" to make it easier to
    develop and package ICU. The bin, lib and include directories are needed to
    develop applications that use ICU. These directories will be created relative
    to the "<tt>--prefix=</tt><i>dir</i>" configure option (See the <a href=
    "#HowToBuildUNIX">UNIX build instructions</a>). When ICU is built on Windows,
    a similar directory structure is built.</p>

    <p>When changes have been made to the standard ICU distribution, it is
    recommended that at least one of the following guidelines be followed for
    special packaging.</p>

    <ol>
      <li>Add a suffix name to the library names. This can be done with the
      --with-library-suffix configure option.</li>

      <li>The installation script should install the ICU libraries into the
      application's directory.</li>
    </ol>

    <p>Following these guidelines prevents other applications that use a standard
    ICU distribution from conflicting with any libraries that you need. On
    operating systems that do not have a standard C++ ABI (name mangling) for
    compilers, it is recommended to do this special packaging anyway. More
    details on customizing ICU are available in the <a href=
    "http://userguide.icu-project.org/">User's Guide</a>. The <a href=
    "#SourceCode">ICU Source Code Organization</a> section of this readme.html
    gives a more complete description of the libraries.</p>

    <table class="docTable" summary=
    "ICU has several libraries for you to use.">
      <caption>
        Here is an example of libraries that are frequently packaged.
      </caption>

      <tr>
        <th scope="col">Library Name</th>

        <th scope="col">Windows Filename</th>

        <th scope="col">Linux Filename</th>

        <th scope="col">Comment</th>
      </tr>

      <tr>
        <td>Data Library</td>

        <td>icudt<i>XY</i>l.dll</td>

        <td>libicudata.so.<i>XY</i>.<i>Z</i></td>

        <td>Data required by the Common and I18n libraries. There are many ways
        to package and <a href=
        "http://userguide.icu-project.org/icudata">customize this
        data</a>, but by default this is all you need.</td>
      </tr>

      <tr>
        <td>Common Library</td>

        <td>icuuc<i>XY</i>.dll</td>

        <td>libicuuc.so.<i>XY</i>.<i>Z</i></td>

        <td>Base library required by all other ICU libraries.</td>
      </tr>

      <tr>
        <td>Internationalization (i18n) Library</td>

        <td>icuin<i>XY</i>.dll</td>

        <td>libicui18n.so.<i>XY</i>.<i>Z</i></td>

        <td>A library that contains many locale based internationalization (i18n)
        functions.</td>
      </tr>

      <tr>
        <td>Layout Engine</td>

        <td>icule<i>XY</i>.dll</td>

        <td>libicule.so.<i>XY</i>.<i>Z</i></td>

        <td>An optional engine for doing font layout.</td>
      </tr>

      <tr>
        <td>Layout Extensions Engine</td>

        <td>iculx<i>XY</i>.dll</td>

        <td>libiculx.so.<i>XY</i>.<i>Z</i></td>

        <td>An optional engine for doing font layout that uses parts of ICU.</td>
      </tr>

      <tr>
        <td>ICU I/O (Unicode stdio) Library</td>

        <td>icuio<i>XY</i>.dll</td>

        <td>libicuio.so.<i>XY</i>.<i>Z</i></td>

        <td>An optional library that provides a stdio like API with Unicode
        support.</td>
      </tr>

      <tr>
        <td>Tool Utility Library</td>

        <td>icutu<i>XY</i>.dll</td>

        <td>libicutu.so.<i>XY</i>.<i>Z</i></td>

        <td>An internal library that contains internal APIs that are only used by
        ICU's tools. If you do not use ICU's tools, you do not need this
        library.</td>
      </tr>
    </table>

    <p>Normally only the above ICU libraries need to be considered for packaging.
    The versionless symbolic links to these libraries are only needed for easier
    development. The <i>X</i>, <i>Y</i> and <i>Z</i> parts of the name are the
    version numbers of ICU. For example, ICU 2.0.2 would have the name
    libicuuc.so.20.2 for the common library. The exact format of the library
    names can vary between platforms due to how each platform can handles library
    versioning.</p>

    <h2><a name="ImportantNotes" href="#ImportantNotes" id=
    "ImportantNotes">Important Notes About Using ICU</a></h2>

    <h3><a name="ImportantNotesMultithreaded" href="#ImportantNotesMultithreaded"
    id="ImportantNotesMultithreaded">Using ICU in a Multithreaded
    Environment</a></h3>

    <p>Some versions of ICU require calling the <code>u_init()</code> function
    from <code>uclean.h</code> to ensure that ICU is initialized properly. In
    those ICU versions, <code>u_init()</code> must be called before ICU is used
    from multiple threads. There is no harm in calling <code>u_init()</code> in a
    single-threaded application, on a single-CPU machine, or in other cases where
    <code>u_init()</code> is not required.</p>

    <p>In addition to ensuring thread safety, <code>u_init()</code> also attempts
    to load at least one ICU data file. Assuming that all data files are packaged
    together (or are in the same folder in files mode), a failure code from
    <code>u_init()</code> usually means that the data cannot be found. In this
    case, the data may not be installed properly, or the application may have
    failed to call <code>udata_setCommonData()</code> or
    <code>u_setDataDirectory()</code> which specify to ICU where it can find its
    data.</p>

    <p>Since <code>u_init()</code> will load only one or two data files, it
    cannot guarantee that all of the data that an application needs is available.
    It cannot check for all data files because the set of files is customizable,
    and some ICU services work without loading any data at all. An application
    should always check for error codes when opening ICU service objects (using
    <code>ucnv_open()</code>, <code>ucol_open()</code>, C++ constructors,
    etc.).</p>

    <h4>ICU 3.4 and later</h4>

    <p>ICU 3.4 self-initializes properly for multi-threaded use. It achieves this
    without performance penalty by hardcoding the core Unicode properties data,
    at the cost of some flexibility. (For details see Jitterbug 4497.)</p>

    <p><code>u_init()</code> can be used to check for data loading. It tries to
    load the converter alias table (<code>cnvalias.icu</code>).</p>

    <h4>ICU 2.6..3.2</h4>

    <p>These ICU versions require a call to <code>u_init()</code> before
    multi-threaded use. The services that are directly affected are those that
    don't have a service object and need to be fast: normalization and character
    properties.</p>

    <p><code>u_init()</code> loads and initializes the data files for
    normalization and character properties (<code>unorm.icu</code> and
    <code>uprops.icu</code>) and can therefore also be used to check for data
    loading.</p>

    <h4>ICU 2.4 and earlier</h4>

    <p>ICU 2.4 and earlier versions were not prepared for multithreaded use on
    multi-CPU platforms where the CPUs implement weak memory coherency. These
    CPUs include: Power4, Power5, Alpha, Itanium. <code>u_init()</code> was not
    defined yet.</p>

    <h4><a name="ImportantNotesHPUX" href="#ImportantNotesHPUX" id=
    "ImportantNotesHPUX">Using ICU in a Multithreaded Environment on
    HP-UX</a></h4>

    <p>When ICU is built with aCC on HP-UX, the <a
    href="http://h21007.www2.hp.com/portal/site/dspp/menuitem.863c3e4cbcdc3f3515b49c108973a801?ciid=eb08b3f1eee02110b3f1eee02110275d6e10RCRD">-AA</a>
    compiler flag is used. It is required in order to use the latest
    &lt;iostream&gt; API in a thread safe manner. This compiler flag affects the
    version of the C++ library being used. Your applications will also need to
    be compiled with -AA in order to use ICU.</p>

    <h4><a name="ImportantNotesSolaris" href="#ImportantNotesSolaris" id=
    "ImportantNotesSolaris">Using ICU in a Multithreaded Environment on
    Solaris</a></h4>

    <h5>Linking on Solaris</h5>

    <p>In order to avoid synchronization and threading issues, developers are
    <strong>suggested</strong> to strictly follow the compiling and linking
    guidelines for multithreaded applications, specified in the following
    document from Sun Microsystems. Most notably, pay strict attention to the
    following statements from Sun:</p>

    <blockquote>
      <p>To use libthread, specify -lthread before -lc on the ld command line, or
      last on the cc command line.</p>

      <p>To use libpthread, specify -lpthread before -lc on the ld command line,
      or last on the cc command line.</p>
    </blockquote>

    <p>Failure to do this may cause spurious lock conflicts, recursive mutex
    failure, and deadlock.</p>

    <p>Source: "<i>Solaris Multithreaded Programming Guide, Compiling and
    Debugging</i>", Sun Microsystems, Inc., Apr 2004<br />
     <a href=
    "http://docs.sun.com/app/docs/doc/816-5137/6mba5vpke?a=view">http://docs.sun.com/app/docs/doc/816-5137/6mba5vpke?a=view</a></p>

    <h3><a name="ImportantNotesWindows" href="#ImportantNotesWindows" id=
    "ImportantNotesWindows">Windows Platform</a></h3>

    <p>If you are building on the Win32 platform, it is important that you
    understand a few of the following build details.</p>

    <h4>DLL directories and the PATH setting</h4>

    <p>As delivered, the International Components for Unicode build as several
    DLLs, which are placed in the "<i>&lt;ICU&gt;</i>\bin" directory. You must
    add this directory to the PATH environment variable in your system, or any
    executables you build will not be able to access International Components for
    Unicode libraries. Alternatively, you can copy the DLL files into a directory
    already in your PATH, but we do not recommend this. You can wind up with
    multiple copies of the DLL and wind up using the wrong one.</p>

    <h4><a name="ImportantNotesWindowsPath" id=
    "ImportantNotesWindowsPath">Changing your PATH</a></h4>

    <p><strong>Windows 2000/XP</strong>: Use the System Icon in the Control
    Panel. Pick the "Advanced" tab. Select the "Environment Variables..."
    button. Select the variable PATH in the lower box, and select the lower
    "Edit..." button. In the "Variable Value" box, append the string
    ";<i>&lt;ICU&gt;</i>\bin" to the end of the path string. If there is
    nothing there, just type in "<i>&lt;ICU&gt;</i>\bin". Click the Set button,
    then the OK button.</p>

    <p>Note: When packaging a Windows application for distribution and
    installation on user systems, copies of the ICU DLLs should be included with
    the application, and installed for exclusive use by the application. This is
    the only way to insure that your application is running with the same version
    of ICU, built with exactly the same options, that you developed and tested
    with. Refer to Microsoft's guidelines on the usage of DLLs, or search for the
    phrase "DLL hell" on <a href=
    "http://msdn.microsoft.com/">msdn.microsoft.com</a>.</p>

    <h3><a name="ImportantNotesUNIX" href="#ImportantNotesUNIX" id=
    "ImportantNotesUNIX">UNIX Type Platform</a></h3>

    <p>If you are building on a UNIX platform, and if you are installing ICU in a
    non-standard location, you may need to add the location of your ICU libraries
    to your <strong>LD_LIBRARY_PATH</strong> or <strong>LIBPATH</strong>
    environment variable (or the equivalent runtime library path environment
    variable for your system). The ICU libraries may not link or load properly
    without doing this.</p>

    <p>Note that if you do not want to have to set this variable, you may instead
    use the --enable-rpath option at configuration time. This option will
    instruct the linker to always look for the libraries where they are
    installed. You will need to use the appropriate linker options when linking
    your own applications and libraries against ICU, too. Please refer to your
    system's linker manual for information about runtime paths. The use of rpath
    also means that when building a new version of ICU you should not have an
    older version installed in the same place as the new version's installation
    directory, as the older libraries will used during the build, instead of the
    new ones, likely leading to an incorrectly build ICU. This is the proper
    behavior of rpath.</p>

    <h2><a name="PlatformDependencies" href="#PlatformDependencies" id=
    "PlatformDependencies">Platform Dependencies</a></h2>

    <h3><a name="PlatformDependenciesNew" href="#PlatformDependenciesNew" id=
    "PlatformDependenciesNew">Porting To A New Platform</a></h3>

    <p>If you are using ICU's Makefiles to build ICU on a new platform, there are
    a few places where you will need to add or modify some files. If you need
    more help, you can always ask the <a href=
    "http://site.icu-project.org/contacts">icu-support mailing list</a>. Once
    you have finished porting ICU to a new platform, it is recommended that you
    contribute your changes back to ICU via the icu-support mailing list. This
    will make it easier for everyone to benefit from your work.</p>

    <h4>Data For a New Platform</h4>

    <p>For some people, it may not be necessary for completely build ICU. Most of
    the makefiles and build targets are for tools that are used for building
    ICU's data, and an application's data (when an application uses ICU resource
    bundles for its data).</p>

    <p>Data files can be built on a different platform when both platforms share
    the same endianness and the same charset family. This assertion does not
    include platform dependent DLLs/shared/static libraries. For details see the
    User Guide <a href="http://userguide.icu-project.org/icudata">ICU
    Data</a> chapter.</p>

    <p>ICU 3.6 removes the requirement that ICU be completely built in the native
    operating environment. It adds the icupkg tool which can be run on any
    platform to turn binary ICU data files from any one of the three formats into
    any one of the other data formats. This allows a application to use ICU data
    built anywhere to be used for any other target platform.</p>

    <p><strong>WARNING!</strong> Building ICU without running the tests is not
    recommended. The tests verify that ICU is safe to use. It is recommended that
    you try to completely port and test ICU before using the libraries for your
    own application.</p>

    <h4>Adapting Makefiles For a New Platform</h4>

    <p>Try to follow the build steps from the <a href="#HowToBuildUNIX">UNIX</a>
    build instructions. If the configure script fails, then you will need to
    modify some files. Here are the usual steps for porting to a new
    platform:<br />
    </p>

    <ol>
      <li>Create an mh file in icu/source/config/. You can use mh-linux or a
      similar mh file as your base configuration.</li>

      <li>Modify icu/source/aclocal.m4 to recognize your platform's mh file.</li>

      <li>Modify icu/source/configure.in to properly set your <b>platform</b> C
      Macro define.</li>

      <li>Run <a href="http://www.gnu.org/software/autoconf/">autoconf</a> in
      icu/source/ without any options. The autoconf tool is standard on most
      Linux systems.</li>

      <li>If you have any optimization options that you want to normally use, you
      can modify icu/source/runConfigureICU to specify those options for your
      platform.</li>

      <li>Build and test ICU on your platform. It is very important that you run
      the tests. If you don't run the tests, there is no guarentee that you have
      properly ported ICU.</li>
    </ol>

    <h3><a name="PlatformDependenciesImpl" href="#PlatformDependenciesImpl" id=
    "PlatformDependenciesImpl">Platform Dependent Implementations</a></h3>

    <p>The platform dependencies have been mostly isolated into the following
    files in the common library. This information can be useful if you are
    porting ICU to a new platform.</p>

    <ul>
      <li>
        <strong>unicode/platform.h.in</strong> (autoconf'ed platforms)<br />
         <strong>unicode/p<i>XXXX</i>.h</strong> (others: pwin32.h, ppalmos.h,
        ..): Platform-dependent typedefs and defines:<br />
        <br />


        <ul>
          <li>Generic types like UBool, int8_t, int16_t, int32_t, int64_t,
          uint64_t etc.</li>

          <li>U_EXPORT and U_IMPORT for specifying dynamic library import and
          export</li>

          <li>String handling support for the char16_t and wchar_t types.</li>
        </ul>
        <br />
      </li>

      <li>
        <strong>unicode/putil.h, putil.c</strong>: platform-dependent
        implementations of various functions that are platform dependent:<br />
        <br />


        <ul>
          <li>uprv_isNaN, uprv_isInfinite, uprv_getNaN and uprv_getInfinity for
          handling special floating point values.</li>

          <li>uprv_tzset, uprv_timezone, uprv_tzname and time for getting
          platform specific time and time zone information.</li>

          <li>u_getDataDirectory for getting the default data directory.</li>

          <li>uprv_getDefaultLocaleID for getting the default locale
          setting.</li>

          <li>uprv_getDefaultCodepage for getting the default codepage
          encoding.</li>
        </ul>
        <br />
      </li>

      <li>
        <strong>umutex.h, umutex.c</strong>: Code for doing synchronization in
        multithreaded applications. If you wish to use International Components
        for Unicode in a multithreaded application, you must provide a
        synchronization primitive that the classes can use to protect their
        global data against simultaneous modifications. We already supply working
        implementations for many platforms that ICU builds on.<br />
        <br />
      </li>

      <li><strong>umapfile.h, umapfile.c</strong>: functions for mapping or
      otherwise reading or loading files into memory. All access by ICU to data
      from files makes use of these functions.<br />
      <br />
      </li>

      <li>Using platform specific #ifdef macros are highly discouraged outside of
      the scope of these files. When the source code gets updated in the future,
      these #ifdef's can cause testing problems for your platform.</li>
    </ul>
    <hr />

    <p>Copyright &copy; 1997-2016 International Business Machines Corporation and
    others. All Rights Reserved.<br />
     IBM Globalization Center of Competency - San Jos&eacute;<br />
     4400 North First Street<br />
     San Jos&eacute;, CA 95134<br />
     USA</p>
  </body>
</html>
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

The two files vprof.h and vprof.cpp implement a simple value-profiling mechanism. By including these two files in avmplus (or any other project), you can value profile data as you wish (currently integers).

Usage:
#include "vprof.h"  // in the source file you want to use it

_vprof (value);

At the end of the execution, for each probe you'll get the data associated with the probe, such as:

File                                        line    avg     [min : max] total       count
..\..\pcre\pcre_valid_utf8.cpp  182 50222.75916 [0 :    104947] 4036955604  80381

The probe is defined at line 182 of file pcre_vali_utf8.cpp. It was called 80381 times. The min value of the probe was 0 while its max was 10497 and its average was  50222.75916. The total sum of all values of the probe is 4036955604. Later, I plan to add more options on the spectrum of data among others.

A few typical uses
------------------

To see how many times a given function gets executed do:

void f()
{
    _vprof(1);
    ...
}

void f()
{
        _vprof(1);
        ...
       if (...) {
           _vprof(1);
           ...
       } else {
           _vprof(1);
           ...
       }
}

Here are a few examples of using the value-profiling utility:

  _vprof (e);
    at the end of program execution, you'll get a dump of the source location of this probe,
    its min, max, average, the total sum of all instances of e, and the total number of times this probe was called.

  _vprof (x > 0);
    shows how many times and what percentage of the cases x was > 0,
    that is the probablitiy that x > 0.

 _vprof (n % 2 == 0);
    shows how many times n was an even number
    as well as th probablitiy of n being an even number.

 _hprof (n, 4, 1000, 5000, 5001, 10000);
    gives you the histogram of n over the given 4 bucket boundaries:
        # cases <  1000
        # cases >= 1000 and < 5000
        # cases >= 5000 and < 5001
        # cases >= 5001 and < 10000
        # cases >= 10000

 _nvprof ("event name", value);
    all instances with the same name are merged
    so, you can call _vprof with the same event name at difference places

 _vprof (e, myProbe);
    value profile e and call myProbe (void* vprofID) at the profiling point.
    inside the probe, the client has the predefined variables:
    _VAL, _COUNT, _SUM, _MIN, _MAX, and the general purpose registers
    _IVAR1, ..., IVAR4      general integer registrs
    _I64VAR1, ..., I64VAR4  general integer64 registrs
    _DVAR1, ..., _DVAR4     general double registers
    _GENPTR a generic pointer that can be used by the client
    the number of registers can be changed in vprof.h

Named Events
------------
_nvprof ("event name", value);
    all instances with the same name are merged
    so, you can call _vprof with the same event name at difference places


Custom Probes
--------------
You can call your own custom probe at the profiling point.
_vprof (v, myProbe);
   value profile v and call myProbe (void* vprofID) at the profiling point
   inside the probe, the client has the predefined variables:
   _VAL, _COUNT, _SUM, _MIN, _MAX, and the general purpose registers
   _IVAR1, ..., IVAR4   general integer registrs
   _I64VAR1, ..., I64VAR4 general integer64 registrs
   _DVAR1, ..., _DVAR4  general double registers
  the number of registers can be changed in vprof.h
  _GENPTR a generic pointer that can be used for almost anything
## On requirements (`*-requirements.txt`) files

MongoDB requires multiple pypa projects installed to build and test. To that end, we provide our own
`*-requirements.txt` files for specific domains of use. Inside each requirements file, there are
only include statements for component files. These files are the bare requirements for specific
components of our python environment. This separation allows us to avoid repetition and conflict in
our requirements across components.

For most developers, if you pip-install `dev-requirements.txt`, you have the python requirements to
lint, build, and test MongoDB.

## On the constraints (`constraints.txt`) file

Our requirements files are *minimally* constrained. For the majority of pypa projects, any
given requirements file will install the newest version of the project. For increased stability,
there is a `constraints.txt` file with explicit versions for each required project. This file
represents a _somewhat_ portable manifest of the latest acceptable pypa projects version according
to a set of local python environments. It is also used to install the site-packages in the MongoDB
internal toolchain-builder.

Please note that the `verify_pip` task in evergreen confirms that `constraints.txt` satisfies
`toolchain-requirements.txt`. If you modify the pypa project requirements, you should regenerate the
constraints file.

## How to modify a pypa project requirement in a component

The most common edit of our requirements is likely a change to the constraints on a pypa project
that we already use. For example, say that we currently require `pymongo >= 3.0, < 3.6.0` in the
component `core`. You would like to use PyMongo 3.7, so you instead modify the line in
`etc/pip/components/core.req` to read `pymongo >= 3.0, != 3.6.0`. Since this is a modification to an
existing component, you do not need to modify any requirements file. However, you do need to
regenerate the constraints file. The workflow will usually look like:

```
$ # Make your changes to the component file
$ $EDITOR etc/pip/components/core.req
$ # Regenerate the constraints file
$ bash buildscripts/generate-pip-constraints.sh -r etc/pip/toolchain-requirements.txt -o etc/pip/constraints.txt
```

## How to add a new component (`*.req`) file

Occasionally, we will require a set of pypa projects for an entirely new piece of software in our
repository. This usually implies adding a new component file. For example, say that we need to add
a logging system to both local development and evergreen. This system requires the fictional pypa
project `FooLog`. So we add a file `foolog.req` and require it from both `dev-requirements.txt` and
`evgtest-requirements.txt`. Like the majority of our components, we want it in the toolchain, so we
also add it to `toolchain-requirements.txt`. The workflow will usually look like:

```
$ # Make the component file
$ echo "FooLog" >etc/pip/components/foolog.req
$ # Require the component from the requirements files
$ echo "-r components/foolog.req" >>etc/pip/dev-requirements.txt
$ echo "-r components/foolog.req" >>etc/pip/evgtest-requirements.txt
$ echo "-r components/foolog.req" >>etc/pip/toolchain-requirements.txt
$ # Regenerate the constraints file
$ bash buildscripts/generate-pip-constraints.sh -r etc/pip/toolchain-requirements.txt -o etc/pip/constraints.txt
```

## How to add a new requirements (`*-requirements.txt`) file

Rarely, we will have an entirely new domain of requirements that is useful. In this case, we need to
at least make a new requirements file. For example, say we want to make a requirements file for
packaging our code. We would need most of the requirements for `dev-requirements.txt` but the
testing has already been done in our continuous integration. So we create a new file
`package-requirements.txt` and require a smaller subset of components. The new file at
`etc/pip/package-requirements.txt` would look like this:
```
-r components/platform.req
-r components/core.req

-r components/compile.req
-r components/lint.req
```

Notice that since we did not change any components files, we do not need to regenerate our
constraints.
--- COMPILING

This project has begun being ported to Windows, only tcmalloc_minimal
is supported at this time.  A working solution file exists in this
directory:
    gperftools.sln

You can load this solution file into VC++ 7.1 (Visual Studio 2003) or
later -- in the latter case, it will automatically convert the files
to the latest format for you.

When you build the solution, it will create a number of unittests,
which you can run by hand (or, more easily, under the Visual Studio
debugger) to make sure everything is working properly on your system.
The binaries will end up in a directory called "debug" or "release" in
the top-level directory (next to the .sln file).  It will also create
two binaries, nm-pdb and addr2line-pdb, which you should install in
the same directory you install the 'pprof' perl script.

I don't know very much about how to install DLLs on Windows, so you'll
have to figure out that part for yourself.  If you choose to just
re-use the existing .sln, make sure you set the IncludeDir's
appropriately!  Look at the properties for libtcmalloc_minimal.dll.

Note that these systems are set to build in Debug mode by default.
You may want to change them to Release mode.

To use tcmalloc_minimal in your own projects, you should only need to
build the dll and install it someplace, so you can link it into
further binaries.  To use the dll, you need to add the following to
the linker line of your executable:
   "libtcmalloc_minimal.lib" /INCLUDE:"__tcmalloc" 

Here is how to accomplish this in Visual Studio 2005 (VC8):

1) Have your executable depend on the tcmalloc library by selecting
   "Project Dependencies..." from the "Project" menu.  Your executable
   should depend on "libtcmalloc_minimal".

2) Have your executable depend on a tcmalloc symbol -- this is
   necessary so the linker doesn't "optimize out" the libtcmalloc
   dependency -- by right-clicking on your executable's project (in
   the solution explorer), selecting Properties from the pull-down
   menu, then selecting "Configuration Properties" -> "Linker" ->
   "Input".  Then, in the "Force Symbol References" field, enter the
   text "__tcmalloc" (without the quotes).  Be sure to do this for both
   debug and release modes!

You can also link tcmalloc code in statically -- see the example
project tcmalloc_minimal_unittest-static, which does this.  For this
to work, you'll need to add "/D PERFTOOLS_DLL_DECL=" to the compile
line of every perftools .cc file.  You do not need to depend on the
tcmalloc symbol in this case (that is, you don't need to do either
step 1 or step 2 from above).

An alternative to all the above is to statically link your application
with libc, and then replace its malloc with tcmalloc.  This allows you
to just build and link your program normally; the tcmalloc support
comes in a post-processing step.  This is more reliable than the above
technique (which depends on run-time patching, which is inherently
fragile), though more work to set up.  For details, see
   https://groups.google.com/group/google-perftools/browse_thread/thread/41cd3710af85e57b


--- THE HEAP-PROFILER

The heap-profiler has had a preliminary port to Windows but does not
build on Windows by default.  It has not been well tested, and
probably does not work at all when Frame Pointer Optimization (FPO) is
enabled -- that is, in release mode.  The other features of perftools,
such as the cpu-profiler and leak-checker, have not yet been ported to
Windows at all.


--- WIN64

The function-patcher has to disassemble code, and is very
x86-specific.  However, the rest of perftools should work fine for
both x86 and x64.  In particular, if you use the 'statically link with
libc, and replace its malloc with tcmalloc' approach, mentioned above,
it should be possible to use tcmalloc with 64-bit windows.

As of perftools 1.10, there is some support for disassembling x86_64
instructions, for work with win64.  This work is preliminary, but the
test file preamble_patcher_test.cc is provided to play around with
that a bit.  preamble_patcher_test will not compile on win32.


--- ISSUES

NOTE FOR WIN2K USERS: According to reports
(http://code.google.com/p/gperftools/issues/detail?id=127)
the stack-tracing necessary for the heap-profiler does not work on
Win2K.  The best workaround is, if you are building on a Win2k system
is to add "/D NO_TCMALLOC_SAMPLES=" to your build, to turn off the
stack-tracing.  You will not be able to use the heap-profiler if you
do this.

NOTE ON _MSIZE and _RECALLOC: The tcmalloc version of _msize returns
the size of the region tcmalloc allocated for you -- which is at least
as many bytes you asked for, but may be more.  (btw, these *are* bytes
you own, even if you didn't ask for all of them, so it's correct code
to access all of them if you want.)  Unfortunately, the Windows CRT
_recalloc() routine assumes that _msize returns exactly as many bytes
as were requested.  As a result, _recalloc() may not zero out new
bytes correctly.  IT'S SAFEST NOT TO USE _RECALLOC WITH TCMALLOC.
_recalloc() is a tricky routine to use in any case (it's not safe to
use with realloc, for instance).


I have little experience with Windows programming, so there may be
better ways to set this up than I've done!  If you run across any
problems, please post to the google-perftools Google Group, or report
them on the gperftools Google Code site:
   http://groups.google.com/group/google-perftools
   http://code.google.com/p/gperftools/issues/list

-- craig

Last modified: 2 February 2012
gperftools
----------
(originally Google Performance Tools)

The fastest malloc we’ve seen; works particularly well with threads
and STL. Also: thread-friendly heap-checker, heap-profiler, and
cpu-profiler.


OVERVIEW
---------

gperftools is a collection of a high-performance multi-threaded
malloc() implementation, plus some pretty nifty performance analysis
tools.

gperftools is distributed under the terms of the BSD License. Join our
mailing list at gpeftools@googlegroups.com for updates.

gperftools was original home for pprof program. But do note that
original pprof (which is still included with gerftools) is now
deprecated in favor of golang version at https://github.com/google/pprof


TCMALLOC
--------
Just link in -ltcmalloc or -ltcmalloc_minimal to get the advantages of
tcmalloc -- a replacement for malloc and new.  See below for some
environment variables you can use with tcmalloc, as well.

tcmalloc functionality is available on all systems we've tested; see
INSTALL for more details.  See README_windows.txt for instructions on
using tcmalloc on Windows.

NOTE: When compiling with programs with gcc, that you plan to link
with libtcmalloc, it's safest to pass in the flags

 -fno-builtin-malloc -fno-builtin-calloc -fno-builtin-realloc -fno-builtin-free

when compiling.  gcc makes some optimizations assuming it is using its
own, built-in malloc; that assumption obviously isn't true with
tcmalloc.  In practice, we haven't seen any problems with this, but
the expected risk is highest for users who register their own malloc
hooks with tcmalloc (using gperftools/malloc_hook.h).  The risk is
lowest for folks who use tcmalloc_minimal (or, of course, who pass in
the above flags :-) ).


HEAP PROFILER
-------------
See doc/heap-profiler.html for information about how to use tcmalloc's
heap profiler and analyze its output.

As a quick-start, do the following after installing this package:

1) Link your executable with -ltcmalloc
2) Run your executable with the HEAPPROFILE environment var set:
     $ HEAPPROFILE=/tmp/heapprof <path/to/binary> [binary args]
3) Run pprof to analyze the heap usage
     $ pprof <path/to/binary> /tmp/heapprof.0045.heap  # run 'ls' to see options
     $ pprof --gv <path/to/binary> /tmp/heapprof.0045.heap

You can also use LD_PRELOAD to heap-profile an executable that you
didn't compile.

There are other environment variables, besides HEAPPROFILE, you can
set to adjust the heap-profiler behavior; c.f. "ENVIRONMENT VARIABLES"
below.

The heap profiler is available on all unix-based systems we've tested;
see INSTALL for more details.  It is not currently available on Windows.


HEAP CHECKER
------------
See doc/heap-checker.html for information about how to use tcmalloc's
heap checker.

In order to catch all heap leaks, tcmalloc must be linked *last* into
your executable.  The heap checker may mischaracterize some memory
accesses in libraries listed after it on the link line.  For instance,
it may report these libraries as leaking memory when they're not.
(See the source code for more details.)

Here's a quick-start for how to use:

As a quick-start, do the following after installing this package:

1) Link your executable with -ltcmalloc
2) Run your executable with the HEAPCHECK environment var set:
     $ HEAPCHECK=1 <path/to/binary> [binary args]

Other values for HEAPCHECK: normal (equivalent to "1"), strict, draconian

You can also use LD_PRELOAD to heap-check an executable that you
didn't compile.

The heap checker is only available on Linux at this time; see INSTALL
for more details.


CPU PROFILER
------------
See doc/cpu-profiler.html for information about how to use the CPU
profiler and analyze its output.

As a quick-start, do the following after installing this package:

1) Link your executable with -lprofiler
2) Run your executable with the CPUPROFILE environment var set:
     $ CPUPROFILE=/tmp/prof.out <path/to/binary> [binary args]
3) Run pprof to analyze the CPU usage
     $ pprof <path/to/binary> /tmp/prof.out      # -pg-like text output
     $ pprof --gv <path/to/binary> /tmp/prof.out # really cool graphical output

There are other environment variables, besides CPUPROFILE, you can set
to adjust the cpu-profiler behavior; cf "ENVIRONMENT VARIABLES" below.

The CPU profiler is available on all unix-based systems we've tested;
see INSTALL for more details.  It is not currently available on Windows.

NOTE: CPU profiling doesn't work after fork (unless you immediately
      do an exec()-like call afterwards).  Furthermore, if you do
      fork, and the child calls exit(), it may corrupt the profile
      data.  You can use _exit() to work around this.  We hope to have
      a fix for both problems in the next release of perftools
      (hopefully perftools 1.2).


EVERYTHING IN ONE
-----------------
If you want the CPU profiler, heap profiler, and heap leak-checker to
all be available for your application, you can do:
   gcc -o myapp ... -lprofiler -ltcmalloc

However, if you have a reason to use the static versions of the
library, this two-library linking won't work:
   gcc -o myapp ... /usr/lib/libprofiler.a /usr/lib/libtcmalloc.a  # errors!

Instead, use the special libtcmalloc_and_profiler library, which we
make for just this purpose:
   gcc -o myapp ... /usr/lib/libtcmalloc_and_profiler.a


CONFIGURATION OPTIONS
---------------------
For advanced users, there are several flags you can pass to
'./configure' that tweak tcmalloc performace.  (These are in addition
to the environment variables you can set at runtime to affect
tcmalloc, described below.)  See the INSTALL file for details.


ENVIRONMENT VARIABLES
---------------------
The cpu profiler, heap checker, and heap profiler will lie dormant,
using no memory or CPU, until you turn them on.  (Thus, there's no
harm in linking -lprofiler into every application, and also -ltcmalloc
assuming you're ok using the non-libc malloc library.)

The easiest way to turn them on is by setting the appropriate
environment variables.  We have several variables that let you
enable/disable features as well as tweak parameters.

Here are some of the most important variables:

HEAPPROFILE=<pre> -- turns on heap profiling and dumps data using this prefix
HEAPCHECK=<type>  -- turns on heap checking with strictness 'type'
CPUPROFILE=<file> -- turns on cpu profiling and dumps data to this file.
PROFILESELECTED=1 -- if set, cpu-profiler will only profile regions of code
                     surrounded with ProfilerEnable()/ProfilerDisable().
CPUPROFILE_FREQUENCY=x-- how many interrupts/second the cpu-profiler samples.

TCMALLOC_DEBUG=<level> -- the higher level, the more messages malloc emits
MALLOCSTATS=<level>    -- prints memory-use stats at program-exit

For a full list of variables, see the documentation pages:
   doc/cpuprofile.html
   doc/heapprofile.html
   doc/heap_checker.html


COMPILING ON NON-LINUX SYSTEMS
------------------------------

Perftools was developed and tested on x86 Linux systems, and it works
in its full generality only on those systems.  However, we've
successfully ported much of the tcmalloc library to FreeBSD, Solaris
x86, and Darwin (Mac OS X) x86 and ppc; and we've ported the basic
functionality in tcmalloc_minimal to Windows.  See INSTALL for details.
See README_windows.txt for details on the Windows port.


PERFORMANCE
-----------

If you're interested in some third-party comparisons of tcmalloc to
other malloc libraries, here are a few web pages that have been
brought to our attention.  The first discusses the effect of using
various malloc libraries on OpenLDAP.  The second compares tcmalloc to
win32's malloc.
  http://www.highlandsun.com/hyc/malloc/
  http://gaiacrtn.free.fr/articles/win32perftools.html

It's possible to build tcmalloc in a way that trades off faster
performance (particularly for deletes) at the cost of more memory
fragmentation (that is, more unusable memory on your system).  See the
INSTALL file for details.


OLD SYSTEM ISSUES
-----------------

When compiling perftools on some old systems, like RedHat 8, you may
get an error like this:
    ___tls_get_addr: symbol not found

This means that you have a system where some parts are updated enough
to support Thread Local Storage, but others are not.  The perftools
configure script can't always detect this kind of case, leading to
that error.  To fix it, just comment out (or delete) the line
   #define HAVE_TLS 1
in your config.h file before building.


64-BIT ISSUES
-------------

There are two issues that can cause program hangs or crashes on x86_64
64-bit systems, which use the libunwind library to get stack-traces.
Neither issue should affect the core tcmalloc library; they both
affect the perftools tools such as cpu-profiler, heap-checker, and
heap-profiler.

1) Some libc's -- at least glibc 2.4 on x86_64 -- have a bug where the
libc function dl_iterate_phdr() acquires its locks in the wrong
order.  This bug should not affect tcmalloc, but may cause occasional
deadlock with the cpu-profiler, heap-profiler, and heap-checker.
Its likeliness increases the more dlopen() commands an executable has.
Most executables don't have any, though several library routines like
getgrgid() call dlopen() behind the scenes.

2) On x86-64 64-bit systems, while tcmalloc itself works fine, the
cpu-profiler tool is unreliable: it will sometimes work, but sometimes
cause a segfault.  I'll explain the problem first, and then some
workarounds.

Note that this only affects the cpu-profiler, which is a
gperftools feature you must turn on manually by setting the
CPUPROFILE environment variable.  If you do not turn on cpu-profiling,
you shouldn't see any crashes due to perftools.

The gory details: The underlying problem is in the backtrace()
function, which is a built-in function in libc.
Backtracing is fairly straightforward in the normal case, but can run
into problems when having to backtrace across a signal frame.
Unfortunately, the cpu-profiler uses signals in order to register a
profiling event, so every backtrace that the profiler does crosses a
signal frame.

In our experience, the only time there is trouble is when the signal
fires in the middle of pthread_mutex_lock.  pthread_mutex_lock is
called quite a bit from system libraries, particularly at program
startup and when creating a new thread.

The solution: The dwarf debugging format has support for 'cfi
annotations', which make it easy to recognize a signal frame.  Some OS
distributions, such as Fedora and gentoo 2007.0, already have added
cfi annotations to their libc.  A future version of libunwind should
recognize these annotations; these systems should not see any
crashses.

Workarounds: If you see problems with crashes when running the
cpu-profiler, consider inserting ProfilerStart()/ProfilerStop() into
your code, rather than setting CPUPROFILE.  This will profile only
those sections of the codebase.  Though we haven't done much testing,
in theory this should reduce the chance of crashes by limiting the
signal generation to only a small part of the codebase.  Ideally, you
would not use ProfilerStart()/ProfilerStop() around code that spawns
new threads, or is otherwise likely to cause a call to
pthread_mutex_lock!

---
17 May 2011
asio version 1.12.2
Released Sunday, 09 December 2018.

See doc/index.html for API documentation and a tutorial.
Copyright (C) 2000-2003, International Business Machines
Corporation and others.  All Rights Reserved.

This directory contains information, input files and scripts for
packaging ICU using specific packaging tools. We assume that the
packager is familiar with the tools and procedures needed to build a
package for a given packaging method (for example, how to use
dpkg-buildpackage(1) on Debian GNU/Linux, or rpm(8) on distributions that
use RPM packages).

Please read the file PACKAGES if you are interested in packaging ICU
yourself. It describes what the different packages should be, and what
their contents are.
WiredTiger 3.1.1: (July 12, 2018)

This is version 3.1.1 of WiredTiger.

WiredTiger release packages and documentation can be found at:

	http://source.wiredtiger.com/

The documentation for this specific release can be found at:

	http://source.wiredtiger.com/3.1.1/index.html

The WiredTiger source code can be found at:

	http://github.com/wiredtiger/wiredtiger

WiredTiger uses JIRA for issue management:

	http://jira.mongodb.org/browse/WT

Please do not report issues through GitHub.

WiredTiger licensing information can be found at:

	http://source.wiredtiger.com/license.html

For general questions and discussion, there's a WiredTiger group:

	http://groups.google.com/group/wiredtiger-users
This is a benchmark program for testing the performance of WiredTiger.

Scripts for running the benchmark can be found in the runners directory.
======
extras
======

extras is a set of extensions to the Python standard library, originally
written to make the code within testtools cleaner, but now split out for
general use outside of a testing context.


Documentation
-------------

pydoc extras is your friend. extras currently contains the following functions:

* try_import

* try_imports

* safe_hasattr

Which do what their name suggests.


Licensing
---------

This project is distributed under the MIT license and copyright is owned by
the extras authors. See LICENSE for details.


Required Dependencies
---------------------

 * Python 2.6+ or 3.0+


Bug reports and patches
-----------------------

Please report bugs using github issues at <https://github.com/testing-cabal/extras>.
Patches can also be submitted via github.  You can mail the authors directly
via the mailing list testtools-dev@lists.launchpad.net. (Note that Launchpad
discards email from unknown addresses - be sure to sign up for a Launchpad
account before mailing the list, or your mail will be silently discarded).


History
-------

extras used to be testtools.helpers, and was factored out when folk wanted to
use it separately.


Thanks
------

 * Martin Pool
=========
testtools
=========

testtools is a set of extensions to the Python standard library's unit testing
framework.

These extensions have been derived from years of experience with unit testing
in Python and come from many different sources.


Documentation
-------------

If you would like to learn more about testtools, consult our documentation in
the 'doc/' directory.  You might like to start at 'doc/overview.rst' or
'doc/for-test-authors.rst'.


Licensing
---------

This project is distributed under the MIT license and copyright is owned by
Jonathan M. Lange and the testtools authors. See LICENSE for details.

Some code in 'testtools/run.py' is taken from Python's unittest module, and is
copyright Steve Purcell and the Python Software Foundation, it is distributed
under the same license as Python, see LICENSE for details.


Required Dependencies
---------------------

 * Python 2.6+ or 3.0+

If you would like to use testtools for earlier Python's, please use testtools
0.9.15.

 * extras (helpers that we intend to push into Python itself in the near
   future).


Optional Dependencies
---------------------

If you would like to use our undocumented, unsupported Twisted support, then
you will need Twisted.

If you want to use ``fixtures`` then you can either install fixtures (e.g. from
https://launchpad.net/python-fixtures or http://pypi.python.org/pypi/fixtures)
or alternatively just make sure your fixture objects obey the same protocol.


Bug reports and patches
-----------------------

Please report bugs using Launchpad at <https://bugs.launchpad.net/testtools>.
Patches should be submitted as Github pull requests, or mailed to the authors.
See ``doc/hacking.rst`` for more details.

There's no mailing list for this project yet, however the testing-in-python
mailing list may be a useful resource:

 * Address: testing-in-python@lists.idyll.org
 * Subscription link: http://lists.idyll.org/listinfo/testing-in-python


History
-------

testtools used to be called 'pyunit3k'.  The name was changed to avoid
conflating the library with the Python 3.0 release (commonly referred to as
'py3k').


Thanks
------

 * Canonical Ltd
 * Bazaar
 * Twisted Matrix Labs
 * Robert Collins
 * Andrew Bennetts
 * Benjamin Peterson
 * Jamu Kakar
 * James Westby
 * Martin [gz]
 * Michael Hudson-Doyle
 * Aaron Bentley
 * Christian Kampka
 * Gavin Panella
 * Martin Pool

  subunit: A streaming protocol for test results
  Copyright (C) 2005-2013 Robert Collins <robertc@robertcollins.net>

  Licensed under either the Apache License, Version 2.0 or the BSD 3-clause
  license at the users choice. A copy of both licenses are available in the
  project source as Apache-2.0 and BSD. You may not use this file except in
  compliance with one of these two licences.

  Unless required by applicable law or agreed to in writing, software
  distributed under these licenses is distributed on an "AS IS" BASIS, WITHOUT
  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
  license you chose for the specific language governing permissions and
  limitations under that license.

  See the COPYING file for full details on the licensing of Subunit.

  subunit reuses iso8601 by Michael Twomey, distributed under an MIT style
  licence - see python/iso8601/LICENSE for details.

Subunit
-------

Subunit is a streaming protocol for test results.

There are two major revisions of the protocol. Version 1 was trivially human
readable but had significant defects as far as highly parallel testing was
concerned - it had no room for doing discovery and execution in parallel,
required substantial buffering when multiplexing and was fragile - a corrupt
byte could cause an entire stream to be misparsed. Version 1.1 added
encapsulation of binary streams which mitigated some of the issues but the
core remained.

Version 2 shares many of the good characteristics of Version 1 - it can be
embedded into a regular text stream (e.g. from a build system) and it still
models xUnit style test execution. It also fixes many of the issues with
Version 1 - Version 2 can be multiplexed without excessive buffering (in
time or space), it has a well defined recovery mechanism for dealing with
corrupted streams (e.g. where two processes write to the same stream
concurrently, or where the stream generator suffers a bug).

More details on both protocol version s can be found in the 'Protocol' section
of this document.

Subunit comes with command line filters to process a subunit stream and
language bindings for python, C, C++ and shell. Bindings are easy to write
for other languages.

A number of useful things can be done easily with subunit:
 * Test aggregation: Tests run separately can be combined and then
   reported/displayed together. For instance, tests from different languages
   can be shown as a seamless whole, and tests running on multiple machines
   can be aggregated into a single stream through a multiplexer.
 * Test archiving: A test run may be recorded and replayed later.
 * Test isolation: Tests that may crash or otherwise interact badly with each
   other can be run seperately and then aggregated, rather than interfering
   with each other or requiring an adhoc test->runner reporting protocol.
 * Grid testing: subunit can act as the necessary serialisation and
   deserialiation to get test runs on distributed machines to be reported in
   real time.

Subunit supplies the following filters:
 * tap2subunit - convert perl's TestAnythingProtocol to subunit.
 * subunit2csv - convert a subunit stream to csv.
 * subunit2pyunit - convert a subunit stream to pyunit test results.
 * subunit2gtk - show a subunit stream in GTK.
 * subunit2junitxml - convert a subunit stream to JUnit's XML format.
 * subunit-diff - compare two subunit streams.
 * subunit-filter - filter out tests from a subunit stream.
 * subunit-ls - list info about tests present in a subunit stream.
 * subunit-stats - generate a summary of a subunit stream.
 * subunit-tags - add or remove tags from a stream.

Integration with other tools
----------------------------

Subunit's language bindings act as integration with various test runners like
'check', 'cppunit', Python's 'unittest'. Beyond that a small amount of glue
(typically a few lines) will allow Subunit to be used in more sophisticated
ways.

Python
======

Subunit has excellent Python support: most of the filters and tools are written
in python and there are facilities for using Subunit to increase test isolation
seamlessly within a test suite.

The most common way is to run an existing python test suite and have it output
subunit via the ``subunit.run`` module::

  $ python -m subunit.run mypackage.tests.test_suite

For more information on the Python support Subunit offers , please see
``pydoc subunit``, or the source in ``python/subunit/``

C
=

Subunit has C bindings to emit the protocol. The 'check' C unit testing project
has included subunit support in their project for some years now. See
'c/README' for more details.

C++
===

The C library is includable and usable directly from C++. A TestListener for
CPPUnit is included in the Subunit distribution. See 'c++/README' for details.

shell
=====

There are two sets of shell tools. There are filters, which accept a subunit
stream on stdin and output processed data (or a transformed stream) on stdout.

Then there are unittest facilities similar to those for C : shell bindings
consisting of simple functions to output protocol elements, and a patch for
adding subunit output to the 'ShUnit' shell test runner. See 'shell/README' for
details.

Filter recipes
--------------

To ignore some failing tests whose root cause is already known::

  subunit-filter --without 'AttributeError.*flavor'


The xUnit test model
--------------------

Subunit implements a slightly modified xUnit test model. The stock standard
model is that there are tests, which have an id(), can be run, and when run
start, emit an outcome (like success or failure) and then finish.

Subunit extends this with the idea of test enumeration (find out about tests
a runner has without running them), tags (allow users to describe tests in
ways the test framework doesn't apply any semantic value to), file attachments
(allow arbitrary data to make analysing a failure easy) and timestamps.

The protocol
------------

Version 2, or v2 is new and still under development, but is intended to
supercede version 1 in the very near future. Subunit's bundled tools accept
only version 2 and only emit version 2, but the new filters subunit-1to2 and
subunit-2to1 can be used to interoperate with older third party libraries.

Version 2
=========

Version 2 is a binary protocol consisting of independent packets that can be
embedded in the output from tools like make - as long as each packet has no
other bytes mixed in with it (which 'make -j N>1' has a tendency of doing).
Version 2 is currently in draft form, and early adopters should be willing
to either discard stored results (if protocol changes are made), or bulk
convert them back to v1 and then to a newer edition of v2.

The protocol synchronises at the start of the stream, after a packet, or
after any 0x0A byte. That is, a subunit v2 packet starts after a newline or
directly after the end of the prior packet.

Subunit is intended to be transported over a reliable streaming protocol such
as TCP. As such it does not concern itself with out of order delivery of
packets. However, because of the possibility of corruption due to either
bugs in the sender, or due to mixed up data from concurrent writes to the same
fd when being embedded, subunit strives to recover reasonably gracefully from
damaged data.

A key design goal for Subunit version 2 is to allow processing and multiplexing
without forcing buffering for semantic correctness, as buffering tends to hide
hung or otherwise misbehaving tests. That said, limited time based buffering
for network efficiency is a good idea - this is ultimately implementator
choice. Line buffering is also discouraged for subunit streams, as dropping
into a debugger or other tool may require interactive traffic even if line
buffering would not otherwise be a problem.

In version two there are two conceptual events - a test status event and a file
attachment event. Events may have timestamps, and the path of multiplexers that
an event is routed through is recorded to permit sending actions back to the
source (such as new tests to run or stdin for driving debuggers and other
interactive input). Test status events are used to enumerate tests, to report
tests and test helpers as they run. Tests may have tags, used to allow
tunnelling extra meanings through subunit without requiring parsing of
arbitrary file attachments. Things that are not standalone tests get marked
as such by setting the 'Runnable' flag to false. (For instance, individual
assertions in TAP are not runnable tests, only the top level TAP test script
is runnable).

File attachments are used to provide rich detail about the nature of a failure.
File attachments can also be used to encapsulate stdout and stderr both during
and outside tests.

Most numbers are stored in network byte order - Most Significant Byte first
encoded using a variation of http://www.dlugosz.com/ZIP2/VLI.html. The first
byte's top 2 high order bits encode the total number of octets in the number.
This encoding can encode values from 0 to 2**30-1, enough to encode a
nanosecond. Numbers that are not variable length encoded are still stored in
MSB order.

 prefix   octets   max       max
+-------+--------+---------+------------+
| 00    |      1 |  2**6-1 |         63 |
| 01    |      2 | 2**14-1 |      16383 |
| 10    |      3 | 2**22-1 |    4194303 |
| 11    |      4 | 2**30-1 | 1073741823 |
+-------+--------+---------+------------+

All variable length elements of the packet are stored with a length prefix
number allowing them to be skipped over for consumers that don't need to
interpret them.

UTF-8 strings are with no terminating NUL and should not have any embedded NULs
(implementations SHOULD validate any such strings that they process and take
some remedial action (such as discarding the packet as corrupt).

In short the structure of a packet is:
PACKET := SIGNATURE FLAGS PACKET_LENGTH TIMESTAMP? TESTID? TAGS? MIME?
          FILECONTENT? ROUTING_CODE? CRC32

In more detail...

Packets are identified by a single byte signature - 0xB3, which is never legal
in a UTF-8 stream as the first byte of a character. 0xB3 starts with the first
bit set and the second not, which is the UTF-8 signature for a continuation
byte. 0xB3 was chosen as 0x73 ('s' in ASCII') with the top two bits replaced by
the 1 and 0 for a continuation byte.

If subunit packets are being embedded in a non-UTF-8 text stream, where 0x73 is
a legal character, consider either recoding the text to UTF-8, or using
subunit's 'file' packets to embed the text stream in subunit, rather than the
other way around.

Following the signature byte comes a 16-bit flags field, which includes a
4-bit version field - if the version is not 0x2 then the packet cannot be
read. It is recommended to signal an error at this point (e.g. by emitting
a synthetic error packet and returning to the top level loop to look for
new packets, or exiting with an error). If recovery is desired, treat the
packet signature as an opaque byte and scan for a new synchronisation point.
NB: Subunit V1 and V2 packets may legitimately included 0xB3 internally,
as they are an 8-bit safe container format, so recovery from this situation
may involve an arbitrary number of false positives until an actual packet
is encountered : and even then it may still be false, failing after passing
the version check due to coincidence.

Flags are stored in network byte order too.
+-------------------------+------------------------+
| High byte               | Low byte               |
| 15 14 13 12 11 10  9  8 | 7  6  5  4  3  2  1  0 |
| VERSION    |feature bits|                        |
+------------+------------+------------------------+

Valid version values are:
0x2 - version 2

Feature bits:
Bit 11 - mask 0x0800 - Test id present.
Bit 10 - mask 0x0400 - Routing code present.
Bit  9 - mask 0x0200 - Timestamp present.
Bit  8 - mask 0x0100 - Test is 'runnable'.
Bit  7 - mask 0x0080 - Tags are present.
Bit  6 - mask 0x0040 - File content is present.
Bit  5 - mask 0x0020 - File MIME type is present.
Bit  4 - mask 0x0010 - EOF marker.
Bit  3 - mask 0x0008 - Must be zero in version 2.

Test status gets three bits:
Bit 2 | Bit 1 | Bit 0 - mask 0x0007 - A test status enum lookup:
000 - undefined / no test
001 - Enumeration / existence
002 - In progress
003 - Success
004 - Unexpected Success
005 - Skipped
006 - Failed
007 - Expected failure

After the flags field is a number field giving the length in bytes for the
entire packet including the signature and the checksum. This length must
be less than 4MiB - 4194303 bytes. The encoding can obviously record a larger
number but one of the goals is to avoid requiring large buffers, or causing
large latency in the packet forward/processing pipeline. Larger file
attachments can be communicated in multiple packets, and the overhead in such a
4MiB packet is approximately 0.2%.

The rest of the packet is a series of optional features as specified by the set
feature bits in the flags field. When absent they are entirely absent.

Forwarding and multiplexing of packets can be done without interpreting the
remainder of the packet until the routing code and checksum (which are both at
the end of the packet). Additionally, routers can often avoid copying or moving
the bulk of the packet, as long as the routing code size increase doesn't force
the length encoding to take up a new byte (which will only happen to packets
less than or equal to 16KiB in length) - large packets are very efficient to
route.

Timestamp when present is a 32 bit unsigned integer for secnods, and a variable
length number for nanoseconds, representing UTC time since Unix Epoch in
seconds and nanoseconds.

Test id when present is a UTF-8 string. The test id should uniquely identify
runnable tests such that they can be selected individually. For tests and other
actions which cannot be individually run (such as test
fixtures/layers/subtests) uniqueness is not required (though being human
meaningful is highly recommended).

Tags when present is a length prefixed vector of UTF-8 strings, one per tag.
There are no restrictions on tag content (other than the restrictions on UTF-8
strings in subunit in general). Tags have no ordering.

When a MIME type is present, it defines the MIME type for the file across all
packets same file (routing code + testid + name uniquely identifies a file,
reset when EOF is flagged). If a file never has a MIME type set, it should be
treated as application/octet-stream.

File content when present is a UTF-8 string for the name followed by the length
in bytes of the content, and then the content octets.

If present routing code is a UTF-8 string. The routing code is used to
determine which test backend a test was running on when doing data analysis,
and to route stdin to the test process if interaction is required.

Multiplexers SHOULD add a routing code if none is present, and prefix any
existing routing code with a routing code ('/' separated) if one is already
present. For example, a multiplexer might label each stream it is multiplexing
with a simple ordinal ('0', '1' etc), and given an incoming packet with route
code '3' from stream '0' would adjust the route code when forwarding the packet
to be '0/3'.

Following the end of the packet is a CRC-32 checksum of the contents of the
packet including the signature.

Example packets
~~~~~~~~~~~~~~~

Trivial test "foo" enumeration packet, with test id, runnable set,
status=enumeration. Spaces below are to visually break up signature / flags /
length / testid / crc32

b3 2901 0c 03666f6f 08555f1b


Version 1 (and 1.1)
===================

Version 1 (and 1.1) are mostly human readable protocols.

Sample subunit wire contents
----------------------------

The following::
  test: test foo works
  success: test foo works.
  test: tar a file.
  failure: tar a file. [
  ..
   ]..  space is eaten.
  foo.c:34 WARNING foo is not defined.
  ]
  a writeln to stdout

When run through subunit2pyunit::
  .F
  a writeln to stdout

  ========================
  FAILURE: tar a file.
  -------------------
  ..
  ]..  space is eaten.
  foo.c:34 WARNING foo is not defined.


Subunit protocol description
============================

This description is being ported to an EBNF style. Currently its only partly in
that style, but should be fairly clear all the same. When in doubt, refer the
source (and ideally help fix up the description!). Generally the protocol is
line orientated and consists of either directives and their parameters, or
when outside a DETAILS region unexpected lines which are not interpreted by
the parser - they should be forwarded unaltered.

test|testing|test:|testing: test LABEL
success|success:|successful|successful: test LABEL
success|success:|successful|successful: test LABEL DETAILS
failure: test LABEL
failure: test LABEL DETAILS
error: test LABEL
error: test LABEL DETAILS
skip[:] test LABEL
skip[:] test LABEL DETAILS
xfail[:] test LABEL
xfail[:] test LABEL DETAILS
uxsuccess[:] test LABEL
uxsuccess[:] test LABEL DETAILS
progress: [+|-]X
progress: push
progress: pop
tags: [-]TAG ...
time: YYYY-MM-DD HH:MM:SSZ

LABEL: UTF8*
NAME: UTF8*
DETAILS ::= BRACKETED | MULTIPART
BRACKETED ::= '[' CR UTF8-lines ']' CR
MULTIPART ::= '[ multipart' CR PART* ']' CR
PART ::= PART_TYPE CR NAME CR PART_BYTES CR
PART_TYPE ::= Content-Type: type/sub-type(;parameter=value,parameter=value)
PART_BYTES ::= (DIGITS CR LF BYTE{DIGITS})* '0' CR LF

unexpected output on stdout -> stdout.
exit w/0 or last test completing -> error

Tags given outside a test are applied to all following tests
Tags given after a test: line and before the result line for the same test
apply only to that test, and inherit the current global tags.
A '-' before a tag is used to remove tags - e.g. to prevent a global tag
applying to a single test, or to cancel a global tag.

The progress directive is used to provide progress information about a stream
so that stream consumer can provide completion estimates, progress bars and so
on. Stream generators that know how many tests will be present in the stream
should output "progress: COUNT". Stream filters that add tests should output
"progress: +COUNT", and those that remove tests should output
"progress: -COUNT". An absolute count should reset the progress indicators in
use - it indicates that two separate streams from different generators have
been trivially concatenated together, and there is no knowledge of how many
more complete streams are incoming. Smart concatenation could scan each stream
for their count and sum them, or alternatively translate absolute counts into
relative counts inline. It is recommended that outputters avoid absolute counts
unless necessary. The push and pop directives are used to provide local regions
for progress reporting. This fits with hierarchically operating test
environments - such as those that organise tests into suites - the top-most
runner can report on the number of suites, and each suite surround its output
with a (push, pop) pair. Interpreters should interpret a pop as also advancing
the progress of the restored level by one step. Encountering progress
directives between the start and end of a test pair indicates that a previous
test was interrupted and did not cleanly terminate: it should be implicitly
closed with an error (the same as when a stream ends with no closing test
directive for the most recently started test).

The time directive acts as a clock event - it sets the time for all future
events. The value should be a valid ISO8601 time.

The skip, xfail and uxsuccess outcomes are not supported by all testing
environments. In Python the testttools (https://launchpad.net/testtools)
library is used to translate these automatically if an older Python version
that does not support them is in use. See the testtools documentation for the
translation policy.

skip is used to indicate a test was discovered but not executed. xfail is used
to indicate a test that errored in some expected fashion (also know as "TODO"
tests in some frameworks). uxsuccess is used to indicate and unexpected success
where a test though to be failing actually passes. It is complementary to
xfail.

Hacking on subunit
------------------

Releases
========

* Update versions in configure.ac and python/subunit/__init__.py.
* Make PyPI and regular tarball releases. Upload the regular one to LP, the
  PyPI one to PyPI.
* Push a tagged commit.

This is the test discovery mechanism and ``load_tests`` protocol for unittest
backported from Python 2.7 to work with Python 2.4 or more recent (including 
Python 3).

.. note::

    Test discovery is just part of what is new in unittest in Python 2.7. All
    of the new features have been backported to run on Python 2.4-2.6, including
    test discovery. This is the 
    `unittest2 package <http://pypi.python.org/pypi/unittest2>`_.

discover can be installed with pip or easy_install. After installing switch the
current directory to the top level directory of your project and run::

   python -m discover
   python discover.py
  
(If you have setuptools or `distribute <http://pypi.python.org/pypi/distribute>`_
installed you will also have a ``discover`` script available.)

This will discover all tests (with certain restrictions) from the current
directory. The discover module has several options to control its behavior (full
usage options are displayed with ``python -m discover -h``)::

    Usage: discover.py [options]

    Options:
      -v, --verbose    Verbose output
      -s directory     Directory to start discovery ('.' default)
      -p pattern       Pattern to match test files ('test*.py' default)
      -t directory     Top level directory of project (default to
                       start directory)

    For test discovery all test modules must be importable from the top
    level directory of the project.

For example to use a different pattern for matching test modules run::

    python -m discover -p '*test.py'

(For UNIX-like shells like Bash you need to put quotes around the test pattern
or the shell will attempt to expand the pattern instead of passing it through to
discover. On Windows you must *not* put quotes around the pattern as the
Windows shell will pass the quotes to discover as well.)

Test discovery is implemented in ``discover.DiscoveringTestLoader.discover``. As
well as using discover as a command line script you can import
``DiscoveringTestLoader``, which is a subclass of ``unittest.TestLoader``, and
use it in your test framework.

This method finds and returns all test modules from the specified start
directory, recursing into subdirectories to find them. Only test files that
match *pattern* will be loaded. (Using shell style pattern matching.)

All test modules must be importable from the top level of the project. If
the start directory is not the top level directory then the top level
directory must be specified separately.

The ``load_tests`` protocol allows test modules and packages to customize how
they are loaded. This is implemented in
``discover.DiscoveringTestLoader.loadTestsFromModule``. If a test module defines
a ``load_tests`` function then tests are loaded from the module by calling
``load_tests`` with three arguments: `loader`, `standard_tests`, `None`.

If a test package name (directory with `__init__.py`) matches the
pattern then the package will be checked for a ``load_tests``
function. If this exists then it will be called with *loader*, *tests*,
*pattern*.

.. note::

    The default pattern for matching tests is ``test*.py``. The '.py' means
    that it will match test files and *not* match package names. You can
    change this by changing the pattern using a command line option like
    ``-p 'test*'``.

If ``load_tests`` exists then discovery does  *not* recurse into the package,
``load_tests`` is responsible for loading all tests in the package.

The pattern is deliberately not stored as a loader attribute so that
packages can continue discovery themselves. *top_level_dir* is stored so
``load_tests`` does not need to pass this argument in to
``loader.discover()``.

discover.py is maintained in a google code project (where bugs and feature
requests should be posted): http://code.google.com/p/unittest-ext/

The latest development version of discover.py can be found at:
http://code.google.com/p/unittest-ext/source/browse/trunk/discover.py


CHANGELOG
=========


2010/06/11 0.4.0
----------------

* Addition of a setuptools compatible test collector. Set
  "test_suite = 'discover.collector'" in setup.py. "setup.py test" will start
  test discovery with default parameters from the same directory as the setup.py.
* Allow test discovery using dotted module names instead of a path.
* Addition of a setuptools compatible entrypoint for the discover script.
* A faulty load_tests function will not halt test discovery. A failing test
  is created to report the error.
* If test discovery imports a module from the wrong location (usually because
  the module is globally installed and the user is expecting to run tests
  against a development version in a different location) then discovery halts
  with an ImportError and the problem is reported.
* Matching files during test discovery is done in
  ``DiscoveringTestLoader._match_path``. This method can be overriden in
  subclasses to, for example, match on the full file path or use regular
  expressions for matching.
* Tests for discovery ported from unittest2. (The tests require unittest2 to
  run.)

Feature parity with the ``TestLoader`` in Python 2.7 RC 1.


2010/02/07 0.3.2
----------------

* If ``load_tests`` exists it is passed the standard tests as a ``TestSuite`` 
  rather than a list of tests.

2009/09/13 0.3.1
----------------

* Fixed a problem when a package directory matches the discovery pattern.

2009/08/20 0.3.0
----------------

* Failing to import a file (e.g. due to a syntax error) no longer halts
  discovery but is reported as a failure.
* Discovery will not attempt to import test files whose names are not valid Python
  identifiers, even if they match the pattern.*****************************************************************
testscenarios: extensions to python unittest to support scenarios
*****************************************************************

  Copyright (c) 2009, Robert Collins <robertc@robertcollins.net>
  
  Licensed under either the Apache License, Version 2.0 or the BSD 3-clause
  license at the users choice. A copy of both licenses are available in the
  project source as Apache-2.0 and BSD. You may not use this file except in
  compliance with one of these two licences.
  
  Unless required by applicable law or agreed to in writing, software
  distributed under these licenses is distributed on an "AS IS" BASIS, WITHOUT
  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
  license you chose for the specific language governing permissions and
  limitations under that license.


testscenarios provides clean dependency injection for python unittest style
tests. This can be used for interface testing (testing many implementations via
a single test suite) or for classic dependency injection (provide tests with
dependencies externally to the test code itself, allowing easy testing in
different situations).

Dependencies
============

* Python 2.4+
* testtools <https://launchpad.net/testtools>


Why TestScenarios
=================

Standard Python unittest.py provides on obvious method for running a single
test_foo method with two (or more) scenarios: by creating a mix-in that
provides the functions, objects or settings that make up the scenario. This is
however limited and unsatisfying. Firstly, when two projects are cooperating
on a test suite (for instance, a plugin to a larger project may want to run
the standard tests for a given interface on its implementation), then it is
easy for them to get out of sync with each other: when the list of TestCase
classes to mix-in with changes, the plugin will either fail to run some tests
or error trying to run deleted tests. Secondly, its not as easy to work with
runtime-created-subclasses (a way of dealing with the aforementioned skew)
because they require more indirection to locate the source of the test, and will
often be ignored by e.g. pyflakes pylint etc.

It is the intent of testscenarios to make dynamically running a single test
in multiple scenarios clear, easy to debug and work with even when the list
of scenarios is dynamically generated.


Defining Scenarios
==================

A **scenario** is a tuple of a string name for the scenario, and a dict of
parameters describing the scenario.  The name is appended to the test name, and
the parameters are made available to the test instance when it's run.

Scenarios are presented in **scenario lists** which are typically Python lists
but may be any iterable.


Getting Scenarios applied
=========================

At its heart the concept is simple. For a given test object with a list of
scenarios we prepare a new test object for each scenario. This involves:

* Clone the test to a new test with a new id uniquely distinguishing it.
* Apply the scenario to the test by setting each key, value in the scenario
  as attributes on the test object.

There are some complicating factors around making this happen seamlessly. These
factors are in two areas:

* Choosing what scenarios to use. (See Setting Scenarios For A Test).
* Getting the multiplication to happen. 

Subclasssing
++++++++++++

If you can subclass TestWithScenarios, then the ``run()`` method in
TestWithScenarios will take care of test multiplication. It will at test
execution act as a generator causing multiple tests to execute. For this to 
work reliably TestWithScenarios must be first in the MRO and you cannot
override run() or __call__. This is the most robust method, in the sense
that any test runner or test loader that obeys the python unittest protocol
will run all your scenarios.

Manual generation
+++++++++++++++++

If you cannot subclass TestWithScenarios (e.g. because you are using
TwistedTestCase, or TestCaseWithResources, or any one of a number of other
useful test base classes, or need to override run() or __call__ yourself) then 
you can cause scenario application to happen later by calling
``testscenarios.generate_scenarios()``. For instance::

  >>> import unittest
  >>> try:
  ...     from StringIO import StringIO
  ... except ImportError:
  ...     from io import StringIO
  >>> from testscenarios.scenarios import generate_scenarios

This can work with loaders and runners from the standard library, or possibly other
implementations::

  >>> loader = unittest.TestLoader()
  >>> test_suite = unittest.TestSuite()
  >>> runner = unittest.TextTestRunner(stream=StringIO())

  >>> mytests = loader.loadTestsFromNames(['doc.test_sample'])
  >>> test_suite.addTests(generate_scenarios(mytests))
  >>> runner.run(test_suite)
  <unittest...TextTestResult run=1 errors=0 failures=0>

Testloaders
+++++++++++

Some test loaders support hooks like ``load_tests`` and ``test_suite``.
Ensuring your tests have had scenario application done through these hooks can
be a good idea - it means that external test runners (which support these hooks
like ``nose``, ``trial``, ``tribunal``) will still run your scenarios. (Of
course, if you are using the subclassing approach this is already a surety).
With ``load_tests``::

  >>> def load_tests(standard_tests, module, loader):
  ...     result = loader.suiteClass()
  ...     result.addTests(generate_scenarios(standard_tests))
  ...     return result

as a convenience, this is available in ``load_tests_apply_scenarios``, so a
module using scenario tests need only say ::

  >>> from testscenarios import load_tests_apply_scenarios as load_tests

Python 2.7 and greater support a different calling convention for `load_tests``
<https://bugs.launchpad.net/bzr/+bug/607412>.  `load_tests_apply_scenarios`
copes with both.

With ``test_suite``::

  >>> def test_suite():
  ...     loader = TestLoader()
  ...     tests = loader.loadTestsFromName(__name__)
  ...     result = loader.suiteClass()
  ...     result.addTests(generate_scenarios(tests))
  ...     return result


Setting Scenarios for a test
============================

A sample test using scenarios can be found in the doc/ folder.

See `pydoc testscenarios` for details.

On the TestCase
+++++++++++++++

You can set a scenarios attribute on the test case::

  >>> class MyTest(unittest.TestCase):
  ...
  ...     scenarios = [
  ...         ('scenario1', dict(param=1)),
  ...         ('scenario2', dict(param=2)),]

This provides the main interface by which scenarios are found for a given test.
Subclasses will inherit the scenarios (unless they override the attribute).

After loading
+++++++++++++

Test scenarios can also be generated arbitrarily later, as long as the test has
not yet run. Simply replace (or alter, but be aware that many tests may share a
single scenarios attribute) the scenarios attribute. For instance in this
example some third party tests are extended to run with a custom scenario. ::

  >>> import testtools
  >>> class TestTransport:
  ...     """Hypothetical test case for bzrlib transport tests"""
  ...     pass
  ...
  >>> stock_library_tests = unittest.TestLoader().loadTestsFromNames(
  ...     ['doc.test_sample'])
  ...
  >>> for test in testtools.iterate_tests(stock_library_tests):
  ...     if isinstance(test, TestTransport):
  ...         test.scenarios = test.scenarios + [my_vfs_scenario]
  ...
  >>> suite = unittest.TestSuite()
  >>> suite.addTests(generate_scenarios(stock_library_tests))

Generated tests don't have a ``scenarios`` list, because they don't normally
require any more expansion.  However, you can add a ``scenarios`` list back on
to them, and then run them through ``generate_scenarios`` again to generate the
cross product of tests. ::

  >>> class CrossProductDemo(unittest.TestCase):
  ...     scenarios = [('scenario_0_0', {}),
  ...                  ('scenario_0_1', {})]
  ...     def test_foo(self):
  ...         return
  ...
  >>> suite = unittest.TestSuite()
  >>> suite.addTests(generate_scenarios(CrossProductDemo("test_foo")))
  >>> for test in testtools.iterate_tests(suite):
  ...     test.scenarios = [
  ...         ('scenario_1_0', {}), 
  ...         ('scenario_1_1', {})]
  ...
  >>> suite2 = unittest.TestSuite()
  >>> suite2.addTests(generate_scenarios(suite))
  >>> print(suite2.countTestCases())
  4

Dynamic Scenarios
+++++++++++++++++

A common use case is to have the list of scenarios be dynamic based on plugins
and available libraries. An easy way to do this is to provide a global scope
scenarios somewhere relevant to the tests that will use it, and then that can
be customised, or dynamically populate your scenarios from a registry etc.
For instance::

  >>> hash_scenarios = []
  >>> try:
  ...     from hashlib import md5
  ... except ImportError:
  ...     pass
  ... else:
  ...     hash_scenarios.append(("md5", dict(hash=md5)))
  >>> try:
  ...     from hashlib import sha1
  ... except ImportError:
  ...     pass
  ... else:
  ...     hash_scenarios.append(("sha1", dict(hash=sha1)))
  ...
  >>> class TestHashContract(unittest.TestCase):
  ...
  ...     scenarios = hash_scenarios
  ...
  >>> class TestHashPerformance(unittest.TestCase):
  ...
  ...     scenarios = hash_scenarios


Forcing Scenarios
+++++++++++++++++

The ``apply_scenarios`` function can be useful to apply scenarios to a test
that has none applied. ``apply_scenarios`` is the workhorse for
``generate_scenarios``, except it takes the scenarios passed in rather than
introspecting the test object to determine the scenarios. The
``apply_scenarios`` function does not reset the test scenarios attribute,
allowing it to be used to layer scenarios without affecting existing scenario
selection.


Generating Scenarios
====================

Some functions (currently one :-) are available to ease generation of scenario
lists for common situations.

Testing Per Implementation Module
+++++++++++++++++++++++++++++++++

It is reasonably common to have multiple Python modules that provide the same
capabilities and interface, and to want apply the same tests to all of them.

In some cases, not all of the statically defined implementations will be able
to be used in a particular testing environment.  For example, there may be both
a C and a pure-Python implementation of a module.  You want to test the C
module if it can be loaded, but also to have the tests pass if the C module has
not been compiled.

The ``per_module_scenarios`` function generates a scenario for each named
module. The module object of the imported module is set in the supplied
attribute name of the resulting scenario.
Modules which raise ``ImportError`` during import will have the
``sys.exc_info()`` of the exception set instead of the module object. Tests
can check for the attribute being a tuple to decide what to do (e.g. to skip).

Note that for the test to be valid, all access to the module under test must go
through the relevant attribute of the test object.  If one of the
implementations is also directly imported by the test module or any other,
testscenarios will not magically stop it being used.


Advice on Writing Scenarios
===========================

If a parameterised test is because of a bug run without being parameterized,
it should fail rather than running with defaults, because this can hide bugs.


Producing Scenarios
===================

The `multiply_scenarios` function produces the cross-product of the scenarios
passed in::

  >>> from testscenarios.scenarios import multiply_scenarios
  >>> 
  >>> scenarios = multiply_scenarios(
  ...      [('scenario1', dict(param1=1)), ('scenario2', dict(param1=2))],
  ...      [('scenario2', dict(param2=1))],
  ...      )
  >>> scenarios == [('scenario1,scenario2', {'param2': 1, 'param1': 1}),
  ...               ('scenario2,scenario2', {'param2': 1, 'param1': 2})]
  True
The 'test/csuite' directory includes a collection of sanity tests written in C.
They are expected to be executed as part of 'make check' testing.

Each sub directory of 'test/csuite' include source code of one csuite test, and 
should have one corresponding task in the Evergreen (CI system) configuration file. 
See 'test/evergreen.yml' for details.

When a new csuite test is introduced, a corresponding new Evergreen task should be 
crafted and put into the Evergreen configuration file. We have a utility program 
'test/evergreen/evg_cfg.py' to help with identifying and auto-generating the
Evergreen configuration for new or missing csuite tests. The program checking
has been bound into developer workflow through 'dist/s_evergreen'. 
The test/suite directory includes a collection of Python unit tests 
that are expected to be executed when code change is introduced in this repo.  

These Python tests are broken down and grouped into multiple buckets/tasks
in Evergreen (CI system) configuration. See test/evergreen.yml for details.

There is a plan to implement a mechanism to auto-group tests into buckets/tasks
based on history runtime of each test, and generate the Evergreen configuration
dynamically before each Evergreen build variant run, so that no mental overhead
is required when new tests is introduced into test/suite. (WT-4441)

Before the above mentioned mechansim is put into place, please double check
test/evergreen.yml and test run logs to make sure new test are covered.
The test/format program randomly generates WiredTiger databases with
different configurations and different size objects and then does
operations on those files.  The goal is to test the WiredTiger file
formats.

test/format should be linked with a version of Berkeley DB (which it
uses to verify format's results).  Use the configuration option
--with-berkeleydb=DIR to specify the top-level of an installed Berkeley
DB distribution directory, for example:

	--with-berkeleydb=/usr/local/BerkeleyDB.5.3
crc32-s390x
===========

A library of functions for accelerating CRC32 calculations using the
Vector Galois Field Multiply instruction family instructions introduced in
the z13. The Vector Extension Facility for z/Architecture provides two
instructions to perform a binary Galois field multiplication. Both
instructions (VGFM and VGFMA) can operate on different element sizes.
For the 32-bit CRC computation, doublewords are used throughout the
implementation.

Quick start
-----------

Type make to generate a static library libcrc32\_s390x.a.

The library provides functions to compute CRC-32 (IEEE 802.3) and
CRC-32C (Castagnoli), with optional bit reflection (with the `*_le`
versions of the functions).

Function prototypes are declared in crc32-s390x.h. A sample program
crc32-cli.c shows how the library is used.

Testing
-------

The correctness of the hardware-accelerated implementation is verified
with the pure-software Rocksoft Model CRC algorithm. There are four
variants of the test, each of which exercise one type of CRC on random
data with random alignment and buffer sizes, in an infinite loop:

    ./crc32_be_test
    ./crc32_le_test
    ./crc32c_be_test
    ./crc32c_le_test

If the hardware-accelerated algorithm ever returns a different result
than the Rocksoft Model, the test will print messages to indicate the
errors.

Performance
-----------

The performance of the hardware-accelerated implemention is compared
with the slicing-by-8 algorithm. Testing 500000 iterations of a CRC
of 32kB of data showed a 70-times speed-up:

    $ time ./crc32_sw_bench 32768 500000
    CRC: a98177aa
    
    real    0m21.862s
    user    0m21.859s
    sys     0m0.002s
    
    $ time ./crc32_vx_bench 32768 500000
    CRC: a98177aa
    
    real    0m0.323s
    user    0m0.323s
    sys     0m0.000s

crc32-vpmsum
============

A set of examples for accelerating CRC32 calculations using the vector
polynomial multiply sum (vpmsum) instructions introduced in POWER8. These
instructions implement byte, halfword, word and doubleword carryless
multiply/add.

Performance
-----------

An implementation of slice-by-8, one of the fastest lookup table methods
is included so we can compare performance against it. Testing 5000000
iterations of a CRC of 32 kB of data (to keep it L1 cache contained):

```
# time slice_by_8_bench 32768 5000000
122.220 seconds

# time crc32_bench 32768 5000000
2.937 seconds
```

The vpmsum accelerated CRC is just over 41x faster.

This test was run on a 4.1 GHz POWER8, so the algorithm sustains about
52 GiB/sec or 13.6 bytes/cycle. The theoretical limit is 16 bytes/cycle
since we can execute a maximum of one vpmsum instruction per cycle.

In another test, a version was added to the kernel and btrfs write
performance was shown to be 3.8x faster. The test was done to a ramdisk
to mitigate any I/O induced variability.

Quick start
-----------

- Modify CRC and OPTIONS in the Makefile. There are examples for the two most
  common crc32s.

- Type make to create the constants (crc32_constants.h)

- Import the code into your application (crc32.sx crc32_wrapper.c
  crc32_constants.h ppc-opcode.h) and call the CRC:

```
unsigned int crc32_vpmsum(unsigned int crc, unsigned char *p, unsigned long len);
```

CRC background
--------------

For a good background on CRCs, check out:

http://www.ross.net/crc/download/crc_v3.txt

A few key points:

- A CRC is the remainder after dividing a message by the CRC polynomial,
  ie M mod CRC_POLY
- multiply/divide is carryless
- add/subtract is an xor
- n (where n is the order of the CRC) bits of zeroes are appended to the
  end of the message.

One more important piece of information - a CRC is a linear function, so:

```
	CRC(A xor B) = CRC(A) xor CRC(B)

	CRC(A . B) = CRC(A) . CRC(B)	(remember this is carryless multiply)
```

If we take 64bits of data, represented by two 32 bit chunks (AAAAAAAA
and BBBBBBBB):

```
CRC(AAAAAAAABBBBBBBB)
	= CRC(AAAAAAAA00000000 xor BBBBBBBB)
	= CRC(AAAAAAAA00000000) xor CRC(BBBBBBBB)
```

If we operate on AAAAAAAA:

```
CRC(AAAAAAAA00000000)
	= CRC(AAAAAAAA . 100000000)
	= CRC(AAAAAAAA) . CRC(100000000)
```

And CRC(100000000) is a constant which we can pre-calculate:

```
CRC(100000000)
	= 100000000 mod CRC_POLY
	= 2^32 mod CRC_POLY
```

Finally we can add our modified AAAAAAAA to BBBBBBBB:

```
CRC(AAAAAAAABBBBBBBB)
	= ((2^32 mod CRC_POLY) . CRC(AAAAAAAA)) xor CRC(BBBBBBBB)
```

In other words, with the right constants pre-calculated we can shift the
input data around and we can also calculate the CRC in as many parallel
chunks as we want.

No matter how much shifting we do, the final result will be be 64 bits of
data (63 actually, because there is no carry into the top bit). To reduce
it further we need a another trick, and that is Barrett reduction:

http://en.wikipedia.org/wiki/Barrett_reduction

Barrett reduction is a method of calculating a mod n. The idea is to
calculate q, the multiple of our polynomial that we need to subtract. By
doing the computation 2x bits higher (ie 64 bits) and shifting the
result back down 2x bits, we round down to the nearest multiple.

```
	k = 32
	m = floor((4^k)/n) = floor((4^32))/n)
	n = 64 bits of data
	a = 32 bit CRC

	q = floor(ma/(2^64))
	result = a - qn
```

An example in the floating point domain makes it clearer how this works:

```
a mod n = a - floor(am) * n
```

Let's use it to calculate 22 mod 10:

```
	a = 22
	n = 10
	m = 1/n = 1/10 = 0.1

22 mod 10
	= 22 - floor(22*0.1) * 10
	= 22 - 2 * 10
	= 22 - 20
	= 2
```

There is one more issue left - bit reflection. Some CRCs are defined to
operate on the least significant bit first (eg CRC32c). Lets look at
how this would get laid out in a register, and lets simplify it to just
two bytes (vs a 16 byte VMX register):

    [ 8..15 ] [ 0..7 ]

Notice how the bits and bytes are out of order. Since we are doing
multi word multiplication on these values we need them to both be
in order.

The simplest way to fix this is to reflect the bits in each byte:

    [ 15..8 ] [ 7..0 ]

However shuffling bits in a byte is expensive on most CPUs. It is
however relatively cheap to shuffle bytes around. What if we load
the bytes in reversed:

    [ 0..7 ] [ 8..15 ]

Now the bits and bytes are in order, except the least significant bit
of the register is now on the left and the most significant bit is on the
right. We operate as if the register is reflected, which normally we
cannot do. The reason we get away with this is our multiplies are carryless
and our addition and subtraction is xor, so our operations never create
carries.

The only trick is we have to shift the result of multiplies left one
because the high bit of the multiply is always 0, and we want that high bit
on the right not the left.

Implementation
--------------

The vpmsum instructions on POWER8 have a 6 cycle latency and we can
execute one every cycle. In light of this the main loop has 8 parallel
streams which consume 8 x 16 B each iteration. At the completion of this
loop we have taken 32 kB of data and reduced it to 8 x 16 B (128 B).

The next step is to take this 128 B and reduce it to 8 B. At this stage
we also add 32 bits of 0 to the end.

We then apply Barrett reduction to get our CRC.

Examples
--------
- barrett_reduction: An example of Barrett reduction

- final_fold: Starting with 128 bits, add 32 bits of zeros and reduce it to
  64 bits, then apply Barrett reduction

- final_fold2: A second method of reduction

Acknowledgements
----------------

Thanks to Michael Gschwind, Jeff Derby, Lorena Pesantez and Stewart Smith
for their ideas and assistance.
Helium README.

The data structures are "Helium sources" which map to one or more physical
volumes; each Helium source supports any number of "WiredTiger sources",
where a WiredTiger source is an object similar to a Btree "file:" object.
Each WiredTiger source supports any number of WiredTiger cursors.

Each Helium source is given a logical name when first referenced, and that
logical name is subsequently used when a WiredTiger source is created.  For
example, the logical name for a Helium source might be "dev1", and it would
map to the Helium volumes /dev/sd0 and /dev/sd1; subsequent WT_SESSION.create
calls specify a URI like "table:dev1/my_table".

For each WiredTiger source, we create two namespaces on the underlying device,
a "cache" and a "primary".

The cache contains key/value pairs based on updates or changes that have been
made, and includes transactional information.  So, for example, if transaction
3 modifies key/value pair "foo/aaa", and then transaction 4 removes key "foo",
then transaction 5 inserts key/value pair "foo/bbb", the entry in the cache
will look something like:

	Key:	foo
	Value:	[transaction ID 3] [aaa]
		[transaction ID 4] [remove]
		[transaction ID 5] [bbb]

Obviously, we have to marshall/unmarshall these values to/from the cache.

In contrast, the primary contains only key/value pairs known to be committed
and visible to any reader.

When an insert, update or remove is done:
	acquire a lock
	read any matching key from the cache
	check to see if the update can proceed
	append a new value for this transaction
	release the lock

When a search is done:
	if there's a matching key/value pair in the cache {
		if there's an item visible to the reading transaction
			return it
	}
	if there's a matching key/value pair in the primary {
		return it
	}

When a next/prev is done:
	move to the next/prev visible item in the cache
	move to the next/prev visible item in the primary
	return the one closest to the starting position

Locks are not acquired for read operations, and no flushes are done for any of
these operations.

We also create one additional object, the transaction name space, which serves
all of the WiredTiger and Helium objects in a WiredTiger connection.  Whenever
a transaction involving a Helium source commits, we insert a commit record into
the transaction name space and flush the device.  When a transaction rolls back,
we insert an abort record into the txn name space, but don't flush the device.

The visibility check is slightly different than the rest of WiredTiger: we do
not reset anything when a transaction aborts, and so we have to check if the
transaction has been aborted as well as check the transaction ID for visibility.

We create a "cleanup" thread for every underlying Helium source.  The job of
this thread is to migrate rows from the cache object into the primary.  Any
committed, globally visible change in the cache can be copied into the primary
and removed from the cache:

	set BaseTxnID to the oldest transaction ID
	    not yet visible to a running transaction

	for each row in the cache:
		if all of the updates are greater than BaseTxnID
			copy the last update to the primary

	flush the primary to stable storage

	lock the cache
	for each row in the cache:
		if all of the updates are greater than BaseTxnID
			remove the row from the cache
	unlock the cache

	for each row in the transaction store:
		if the transaction ID is less than BaseTxnID
			remove the row

We only need to lock the cache when removing rows, the initial copy to the
primary does not require locks because only the cleanup thread ever writes
to the primary.

No lock is required when removing rows from the transaction store, once the
transaction ID is less than the BaseTxnID, it will never be read.

Helium recovery is almost identical to the cleanup thread, which migrates rows
from the cache into the primary.  For every cache/primary pair, migrate every
commit to the primary (by definition, at recovery time it must be globally
visible), and discard everything else (by definition, at recovery time anything
not committed has been aborted.

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Questions, problems, whatever:

* The implementation is endian-specific, that is, the WiredTiger metadata
stored on the Helium device is on not portable to a big-endian machine.
Helium's metadata is portable between different endian machines, so this
should probably be fixed.

* There's a problem with transactions in WiredTiger that span more than a
single data source.   For example, consider a transaction that modifies
both a Helium object and a Btree object.  If we commit and push the Helium
commit record to stable storage, and then crash before committing the Btree
change, the enclosing WiredTiger transaction will/should end up aborting,
and there's no way for us to back out the change in Helium.  I'm leaving
this problem alone until WiredTiger fine-grained durability is complete,
we're going to need WiredTiger support for some kind of 2PC to solve this.

* If a record in the cache gets too busy, we could end up unable to remove
it (there would always be an active transaction), and it would grow forever.
I suspect the solution is to clean it up when we realize we can't remove it,
that is, we can rebuild the record, discarding the no longer needed entries,
even if the record can't be entirely discarded.
# Boost.Filesystem

Boost.Filesystem, part of collection of the [Boost C++ Libraries](https://github.com/boostorg), provides facilities to manipulate files and directories, and the paths that identify them.

### Directories

* **doc** - Documentation sources
* **include** - Interface headers of Boost.Filesystem
* **src** - Compilable source files of Boost.Filesystem
* **test** - Boost.Filesystem unit tests
* **example** - Boost.Filesystem usage examples

### More information

* [Documentation](https://boost.org/libs/filesystem)
* [Report bugs](https://github.com/boostorg/filesystem/issues/new). Be sure to mention Boost version, platform and compiler you're using. A small compilable code sample to reproduce the problem is always good as well.
* Submit your patches as pull requests against **develop** branch. Note that by submitting patches you agree to license your modifications under the [Boost Software License, Version 1.0](https://www.boost.org/LICENSE_1_0.txt).

### Build status

Master: [![AppVeyor](https://ci.appveyor.com/api/projects/status/nx3e7bcavvn3q953?svg=true)](https://ci.appveyor.com/project/Lastique/filesystem/branch/master) [![Travis CI](https://travis-ci.org/boostorg/filesystem.svg?branch=master)](https://travis-ci.org/boostorg/filesystem)
Develop: [![AppVeyor](https://ci.appveyor.com/api/projects/status/nx3e7bcavvn3q953/branch/develop?svg=true)](https://ci.appveyor.com/project/Lastique/filesystem/branch/develop) [![Travis CI](https://travis-ci.org/boostorg/filesystem.svg?branch=develop)](https://travis-ci.org/boostorg/filesystem)

### License

Distributed under the [Boost Software License, Version 1.0](https://www.boost.org/LICENSE_1_0.txt).
# Boost.Bind

Branch   | Travis | Appveyor
---------|--------|---------
Develop  | [![Build Status](https://travis-ci.org/boostorg/bind.svg?branch=develop)](https://travis-ci.org/boostorg/bind) | [![Build Status](https://ci.appveyor.com/api/projects/status/github/boostorg/bind?branch=develop&svg=true)](https://ci.appveyor.com/project/pdimov/bind)
Master   | [![Build Status](https://travis-ci.org/boostorg/bind.svg?branch=master)](https://travis-ci.org/boostorg/bind) | [![Build Status](https://ci.appveyor.com/api/projects/status/github/boostorg/bind?branch=master&svg=true)](https://ci.appveyor.com/project/pdimov/bind)
DateTime, part of the collection of [Boost C++ Libraries](http://github.com/boostorg), makes programming with dates and times as simple and natural as programming with strings and integers. 

### License

Distributed under the [Boost Software License, Version 1.0](http://www.boost.org/LICENSE_1_0.txt).

### Properties

* C++03
* Requires Linking

### Build Status

Branch          | Travis | Appveyor | Coverity Scan | codecov.io | Deps | Docs | Tests |
:-------------: | ------ | -------- | ------------- | ---------- | ---- | ---- | ----- |
[`master`](https://github.com/boostorg/date_time/tree/master) | [![Build Status](https://travis-ci.org/boostorg/date_time.svg?branch=master)](https://travis-ci.org/boostorg/date_time) | [![Build status](https://ci.appveyor.com/api/projects/status/upf5c528fy09fudk?svg=true)](https://ci.appveyor.com/project/jeking3/date-time-1evbf) | [![Coverity Scan Build Status](https://scan.coverity.com/projects/14908/badge.svg)](https://scan.coverity.com/projects/boostorg-date_time) | [![codecov](https://codecov.io/gh/boostorg/date_time/branch/master/graph/badge.svg)](https://codecov.io/gh/boostorg/date_time/branch/master) | [![Deps](https://img.shields.io/badge/deps-master-brightgreen.svg)](https://pdimov.github.io/boostdep-report/master/date_time.html) | [![Documentation](https://img.shields.io/badge/docs-master-brightgreen.svg)](http://www.boost.org/doc/libs/master/doc/html/date_time.html) | [![Enter the Matrix](https://img.shields.io/badge/matrix-master-brightgreen.svg)](http://www.boost.org/development/tests/master/developer/date_time.html) 
[`develop`](https://github.com/boostorg/date_time/tree/develop) | [![Build Status](https://travis-ci.org/boostorg/date_time.svg?branch=develop)](https://travis-ci.org/boostorg/date_time) | [![Build status](https://ci.appveyor.com/api/projects/status/upf5c528fy09fudk/branch/develop?svg=true)](https://ci.appveyor.com/project/boostorg/date_time/branch/develop) | [![Coverity Scan Build Status](https://scan.coverity.com/projects/14908/badge.svg)](https://scan.coverity.com/projects/boostorg-date_time) | [![codecov](https://codecov.io/gh/boostorg/date_time/branch/develop/graph/badge.svg)](https://codecov.io/gh/boostorg/date_time/branch/develop) | [![Deps](https://img.shields.io/badge/deps-develop-brightgreen.svg)](https://pdimov.github.io/boostdep-report/develop/date_time.html) | [![Documentation](https://img.shields.io/badge/docs-develop-brightgreen.svg)](http://www.boost.org/doc/libs/develop/doc/html/date_time.html) | [![Enter the Matrix](https://img.shields.io/badge/matrix-develop-brightgreen.svg)](http://www.boost.org/development/tests/develop/developer/date_time.html)

### Directories

| Name      | Purpose                        |
| --------- | ------------------------------ |
| `build`   | build script for link library  |
| `data`    | timezone database              |
| `doc`     | documentation                  |
| `example` | use case examples              |
| `include` | headers                        |
| `src`     | source code for link library   |
| `test`    | unit tests                     |
| `xmldoc`  | additional documentation       |

### More information

* [Ask questions](http://stackoverflow.com/questions/ask?tags=c%2B%2B,boost,boost-date_time): Be sure to read the documentation first to see if it answers your question.
* [Report bugs](https://github.com/boostorg/date_time/issues): Be sure to mention Boost version, platform and compiler you're using. A small compilable code sample to reproduce the problem is always good as well.
* [Submit Pull Requests](https://github.com/boostorg/date_time/pulls) against the **develop** branch. Note that by submitting patches you agree to license your modifications under the [Boost Software License, Version 1.0](http://www.boost.org/LICENSE_1_0.txt).  Be sure to include tests proving your changes work properly.
* Discussions about the library are held on the [Boost developers mailing list](http://www.boost.org/community/groups.html#main). Be sure to read the [discussion policy](http://www.boost.org/community/policy.html) before posting and add the `[date_time]` tag at the beginning of the subject line.


The csv file containing the zone_specs used by the 
boost::local_time::tz_database is intended to be customized by the 
library user. When customizing this file (or creating your own) the 
file must follow a specific format.

This first line is expected to contain column headings and is therefore 
not processed by the tz_database.

Each record (line) must have eleven fields. Some of those fields can 
be empty. Every field (even empty ones) must be enclosed in double-quotes. 
Ex:
  "America/Phoenix" <- string enclosed in quotes
  ""                <- empty field

Some fields represent a length of time. The format of these fields must be: 
  "{+|-}hh:mm[:ss]" <- length-of-time format
Where the plus or minus is mandatory and the seconds are optional.

Since some time zones do not use daylight savings it is not always necessary 
for every field in a zone_spec to contain a value. All zone_specs must have 
at least ID and GMT offset. Zones that use daylight savings must have all 
fields filled except: STD ABBR, STD NAME, DST NAME. You should take note 
that DST ABBR is mandatory for zones that use daylight savings (see field 
descriptions for further details).


********* Fields and their description/details ********* 

* ID 
        Contains the identifying string for the zone_spec. Any string will
        do as long as it's unique. No two ID's can be the same. 

* STD ABBR
* STD NAME
* DST ABBR
* DST NAME
        These four are all the names and abbreviations used by the time 
        zone being described. While any string will do in these fields, 
        care should be taken. These fields hold the strings that will be 
        used in the output of many of the local_time classes. 
        Ex:
        time_zone nyc = tz_db.time_zone_from_region("America/New_York");
        local_time ny_time(date(2004, Aug, 30), IS_DST, nyc);
        cout << ny_time.to_long_string() << endl;
        // 2004-Aug-30 00:00:00 Eastern Daylight Time
        cout << ny_time.to_short_string() << endl;
        // 2004-Aug-30 00:00:00 EDT
        
        NOTE: The exact format/function names may vary - see local_time 
        documentation for further details.

* GMT offset
        This is the number of hours added to utc to get the local time 
        before any daylight savings adjustments are made. Some examples 
        are: America/New_York offset -5 hours, & Africa/Cairo offset +2 hours.
        The format must follow the length-of-time format described above.

* DST adjustment
        The amount of time added to gmt_offset when daylight savings is in 
        effect. The format must follow the length-of-time format described
        above.

#####################################################################
##### TODO: more rule capabilities are needed - this portion of #####
##### the tz_database is incomplete                             ##### 
#####################################################################
* DST Start Date rule
        This is a specially formatted string that describes the day of year
        in which the transition take place. It holds three fields of it's own,
        separated by semicolons. 
        * The first field indicates the "nth" weekday of the month. The
                possible values are: 1 (first), 2 (second), 3 (third), 
                4 (fourth), 5 (fifth), and -1 (last).
        * The second field indicates the day-of-week from 0-6 (Sun=0).
        * The third field indicates the month from 1-12 (Jan=1).
        
        Examples are: "-1;5;9"="Last Friday of September", 
        "2;1;3"="Second Monday of March"

* Start time
        Start time is the number of hours past midnight, on the day of the
        start transition, the transition takes place. More simply put, the 
        time of day the transition is made (in 24 hours format). The format
        must follow the length-of-time format described above with the 
        exception that it must always be positive.

* DST End date rule
        See DST Start date rule. The difference here is this is the day 
        daylight savings ends (transition to STD).
* End time
        Same as Start time.
# Boost.SmartPtr

Branch   | Travis | Appveyor
---------|--------|---------
Develop  | [![Build Status](https://travis-ci.org/boostorg/smart_ptr.svg?branch=develop)](https://travis-ci.org/boostorg/smart_ptr) | [![Build Status](https://ci.appveyor.com/api/projects/status/github/boostorg/smart_ptr?branch=develop&svg=true)](https://ci.appveyor.com/project/pdimov/smart-ptr)
Master   | [![Build Status](https://travis-ci.org/boostorg/smart_ptr.svg?branch=master)](https://travis-ci.org/boostorg/smart_ptr) | [![Build Status](https://ci.appveyor.com/api/projects/status/github/boostorg/smart_ptr?branch=master&svg=true)](https://ci.appveyor.com/project/pdimov/smart-ptr)
optional
========

A library for representing optional (nullable) objects in C++.

```cpp
optional<int> readInt(); // this function may return either an int or a not-an-int

if (optional<int> oi = readInt()) // did I get a real int
  cout << "my int is: " << *oi;   // use my int
else
  cout << "I have no int";
```

For more information refer to the documentation provided with this library.
# Boost.Integer

Boost.Integer, part of collection of the [Boost C++ Libraries](https://github.com/boostorg), provides
integer type support, particularly helpful in generic programming. It provides the means to select
an integer type based upon its properties, like the number of bits or the maximum supported value,
as well as compile-time bit mask selection. There is a derivative of `std::numeric_limits` that provides
integral constant expressions for `min` and `max`...
Finally, it provides two compile-time algorithms: determining the highest power of two in a
compile-time value; and computing min and max of constant expressions.

### Directories

* **doc** - QuickBook documentation sources
* **include** - Interface headers of Boost.Integer
* **test** - Boost.Integer unit tests

### More information

* [Documentation](https://boost.org/libs/integer)
* [Report bugs](https://github.com/boostorg/integer/issues/new). Be sure to mention Boost version, platform and compiler you're using. A small compilable code sample to reproduce the problem is always good as well.
* Submit your patches as pull requests against **develop** branch. Note that by submitting patches you agree to license your modifications under the [Boost Software License, Version 1.0](https://www.boost.org/LICENSE_1_0.txt).

### Build status

Master: [![AppVeyor](https://ci.appveyor.com/api/projects/status/iugyf5rf51n99g3w?svg=true)](https://ci.appveyor.com/project/Lastique/integer/branch/master) [![Travis CI](https://travis-ci.org/boostorg/integer.svg?branch=master)](https://travis-ci.org/boostorg/integer)
Develop: [![AppVeyor](https://ci.appveyor.com/api/projects/status/iugyf5rf51n99g3w/branch/develop?svg=true)](https://ci.appveyor.com/project/Lastique/integer/branch/develop) [![Travis CI](https://travis-ci.org/boostorg/integer.svg?branch=develop)](https://travis-ci.org/boostorg/integer)

### License

Distributed under the [Boost Software License, Version 1.0](https://www.boost.org/LICENSE_1_0.txt).
Iostreams, part of collection of the [Boost C++ Libraries](http://github.com/boostorg), provides:

* Tools to make it easy to create standard C++ streams and stream buffers for accessing new Sources and Sinks.
* A framework for defining filters and attaching them to standard streams and stream buffers.
* A collection of ready-to-use Filters, Sources and Sinks.
* Utilities to save and restore stream state.

### License

Distributed under the [Boost Software License, Version 1.0](http://www.boost.org/LICENSE_1_0.txt).

### Properties

* C++03
* Requires a Link Library

### Build Status

Branch          | Travis | Appveyor | Coverity Scan | codecov.io | Deps | Docs | Tests |
:-------------: | ------ | -------- | ------------- | ---------- | ---- | ---- | ----- |
[`master`](https://github.com/boostorg/iostreams/tree/master) | [![Build Status](https://travis-ci.org/boostorg/iostreams.svg?branch=master)](https://travis-ci.org/boostorg/iostreams) | [![Build status](https://ci.appveyor.com/api/projects/status/github/boostorg/iostreams?branch=master&svg=true)](https://ci.appveyor.com/project/eldiener/iostreams/branch/master) | [![Coverity Scan Build Status](https://scan.coverity.com/projects/16463/badge.svg)](https://scan.coverity.com/projects/boostorg-iostreams) | [![codecov](https://codecov.io/gh/boostorg/iostreams/branch/master/graph/badge.svg)](https://codecov.io/gh/boostorg/iostreams/branch/master)| [![Deps](https://img.shields.io/badge/deps-master-brightgreen.svg)](https://pdimov.github.io/boostdep-report/master/iostreams.html) | [![Documentation](https://img.shields.io/badge/docs-master-brightgreen.svg)](http://www.boost.org/doc/libs/master/doc/html/iostreams.html) | [![Enter the Matrix](https://img.shields.io/badge/matrix-master-brightgreen.svg)](http://www.boost.org/development/tests/master/developer/iostreams.html)
[`develop`](https://github.com/boostorg/iostreams/tree/develop) | [![Build Status](https://travis-ci.org/boostorg/iostreams.svg?branch=develop)](https://travis-ci.org/boostorg/iostreams) | [![Build status](https://ci.appveyor.com/api/projects/status/github/boostorg/iostreams?branch=develop&svg=true)](https://ci.appveyor.com/project/eldiener/iostreams/branch/develop) | [![Coverity Scan Build Status](https://scan.coverity.com/projects/16463/badge.svg)](https://scan.coverity.com/projects/boostorg-iostreams) | [![codecov](https://codecov.io/gh/boostorg/iostreams/branch/develop/graph/badge.svg)](https://codecov.io/gh/boostorg/iostreams/branch/develop) | [![Deps](https://img.shields.io/badge/deps-develop-brightgreen.svg)](https://pdimov.github.io/boostdep-report/develop/iostreams.html) | [![Documentation](https://img.shields.io/badge/docs-develop-brightgreen.svg)](http://www.boost.org/doc/libs/develop/doc/html/iostreams.html) | [![Enter the Matrix](https://img.shields.io/badge/matrix-develop-brightgreen.svg)](http://www.boost.org/development/tests/develop/developer/iostreams.html)

### Directories

| Name        | Purpose                        |
| ----------- | ------------------------------ |
| `doc`       | documentation                  |
| `example`   | examples                       |
| `include`   | headers                        |
| `test`      | unit tests                     |

### More information

* [Ask questions](http://stackoverflow.com/questions/ask?tags=c%2B%2B,boost,boost-iostreams)
* [Report bugs](https://github.com/boostorg/iostreams/issues): Be sure to mention Boost version, platform and compiler you're using. A small compilable code sample to reproduce the problem is always good as well.
* Submit your patches as pull requests against **develop** branch. Note that by submitting patches you agree to license your modifications under the [Boost Software License, Version 1.0](http://www.boost.org/LICENSE_1_0.txt).
* Discussions about the library are held on the [Boost developers mailing list](http://www.boost.org/community/groups.html#main). Be sure to read the [discussion policy](http://www.boost.org/community/policy.html) before posting and add the `[iostreams]` tag at the beginning of the subject line.

# Boost.Align

The Boost Align C++ library provides functions, classes, templates, traits,
and macros, for the control, inspection, and diagnostic of memory alignment.

### License

Distributed under the
[Boost Software License, Version 1.0](http://www.boost.org/LICENSE_1_0.txt).
# ![Boost.Utility](doc/logo.png)

Boost.Utility, part of collection of the [Boost C++ Libraries](https://github.com/boostorg), provides a number of smaller components, too small to be called libraries in their own right. See the documentation for the list of components.

### Directories

* **doc** - Documentation sources
* **include** - Interface headers of Boost.Utility
* **test** - Boost.Utility unit tests

### More information

* [Documentation](https://boost.org/libs/utility)
* [Report bugs](https://github.com/boostorg/utility/issues/new). Be sure to mention Boost version, Boost.Utility component, platform and compiler you're using. A small compilable code sample to reproduce the problem is always good as well.
* Submit your patches as pull requests against **develop** branch. Note that by submitting patches you agree to license your modifications under the [Boost Software License, Version 1.0](https://www.boost.org/LICENSE_1_0.txt).

### Build status

Master: [![Travis CI](https://travis-ci.org/boostorg/utility.svg?branch=master)](https://travis-ci.org/boostorg/utility)
Develop: [![Travis CI](https://travis-ci.org/boostorg/utility.svg?branch=develop)](https://travis-ci.org/boostorg/utility)

### License

Distributed under the [Boost Software License, Version 1.0](https://www.boost.org/LICENSE_1_0.txt).
# Boost.Function, a polymorphic function wrapper

[Boost.Function](http://boost.org/libs/function), part of the
[Boost C++ Libraries](http://boost.org), is the original implementation of the
polymorphic function wrapper `boost::function`, which was eventually accepted
into the C++11 standard as [`std::function`](https://en.cppreference.com/w/cpp/utility/functional/function).

## Currently supported compilers

* g++ 4.4 or later
* clang++ 3.3 or later
* Visual Studio 2005-2017

Tested on [Travis](https://travis-ci.org/boostorg/function/) and [Appveyor](https://ci.appveyor.com/project/pdimov/function/).

## License

Distributed under the [Boost Software License, Version 1.0](http://boost.org/LICENSE_1_0.txt).
Program Options, part of the collection of [Boost C++ Libraries](http://github.com/boostorg), allows for definition and acquisition of (name, value) pairs from the user via conventional methods such as command line and config file.  It is roughly analogous to getopt_long, but for use with C++.

### License

Distributed under the [Boost Software License, Version 1.0](http://www.boost.org/LICENSE_1_0.txt).

### Properties

* C++03
* Requires Linking

### Build Status
(in progress...)

|Branch          | Travis | Appveyor | codecov.io | Deps | Docs | Tests |
|:-------------: | ------ | -------- | ---------- | ---- | ---- | ----- |
|[`master`](https://github.com/boostorg/program_options/tree/master) | [![Build Status](https://travis-ci.org/boostorg/program_options.svg?branch=master)](https://travis-ci.org/boostorg/program_options) | [![Build status](https://ci.appveyor.com/api/projects/status/e0quisadwh1v7ok5/branch/master?svg=true)](https://ci.appveyor.com/project/vprus/program-options/branch/master) | [![codecov](https://codecov.io/gh/boostorg/program_options/branch/master/graph/badge.svg)](https://codecov.io/gh/boostorg/program_options/branch/master) | [![Deps](https://img.shields.io/badge/deps-master-brightgreen.svg)](https://pdimov.github.io/boostdep-report/master/program_options.html) | [![Documentation](https://img.shields.io/badge/docs-master-brightgreen.svg)](http://www.boost.org/doc/libs/master/doc/html/program_options.html) | [![Enter the Matrix](https://img.shields.io/badge/matrix-master-brightgreen.svg)](http://www.boost.org/development/tests/master/developer/program_options.html) 
|[`develop`](https://github.com/boostorg/program_options/tree/develop) | [![Build Status](https://travis-ci.org/boostorg/program_options.svg?branch=develop)](https://travis-ci.org/boostorg/program_options) | [![Build status](https://ci.appveyor.com/api/projects/status/e0quisadwh1v7ok5/branch/develop?svg=true)](https://ci.appveyor.com/project/vprus/program-options/branch/develop) | [![codecov](https://codecov.io/gh/boostorg/program_options/branch/develop/graph/badge.svg)](https://codecov.io/gh/boostorg/program_options/branch/develop) | [![Deps](https://img.shields.io/badge/deps-develop-brightgreen.svg)](https://pdimov.github.io/boostdep-report/develop/program_options.html) | [![Documentation](https://img.shields.io/badge/docs-develop-brightgreen.svg)](http://www.boost.org/doc/libs/develop/doc/html/program_options.html) | [![Enter the Matrix](https://img.shields.io/badge/matrix-develop-brightgreen.svg)](http://www.boost.org/development/tests/develop/developer/program_options.html)
 
### Directories

| Name      | Purpose                        |
| --------- | ------------------------------ |
| `build`   | build script for link library  |
| `ci`      | continuous integration scripts |
| `doc`     | documentation                  |
| `example` | use case examples              |
| `include` | headers                        |
| `src`     | source code for link library   |
| `test`    | unit tests                     |

### More information

* [Ask questions](http://stackoverflow.com/questions/ask?tags=c%2B%2B,boost,boost-program_options): Be sure to read the documentation first to see if it answers your question.
* [Report bugs](https://github.com/boostorg/program_options/issues): Be sure to mention Boost version, platform and compiler you're using. A small compilable code sample to reproduce the problem is always good as well.
* [Submit Pull Requests](https://github.com/boostorg/program_options/pulls) against the **develop** branch. Note that by submitting patches you agree to license your modifications under the [Boost Software License, Version 1.0](http://www.boost.org/LICENSE_1_0.txt).  Be sure to include tests proving your changes work properly.
* Discussions about the library are held on the [Boost developers mailing list](http://www.boost.org/community/groups.html#main). Be sure to read the [discussion policy](http://www.boost.org/community/policy.html) before posting and add the `[program_options]` tag at the beginning of the subject line.
http://code.google.com/p/double-conversion

This project (double-conversion) provides binary-decimal and decimal-binary
routines for IEEE doubles.

The library consists of efficient conversion routines that have been extracted
from the V8 JavaScript engine. The code has been refactored and improved so that
it can be used more easily in other projects.

There is extensive documentation in src/double-conversion.h. Other examples can
be found in test/cctest/test-conversions.cc.
Usage:

Requirements:
1) The shell has to be compiled with --enable-gctimer

Tested with python2.6
# Spidermonkey JSAPI rooting analysis

This directory contains scripts and a makefile for running Brian Hackett's
static GC rooting analysis on a JS source directory.

To use it on SpiderMonkey:

1.  Be on Fedora/CentOS/RedHat Linux x86_64.

    (Specifically, the prebuilt GCC **won't work on Ubuntu**
    without the `CFLAGS` and `CXXFLAGS` settings from
    http://trac.wildfiregames.com/wiki/StaticRootingAnalysis .)

2.  Have the Gecko build prerequisites installed.

3.  In this directory, run these commands.

        mkdir builddir
        cd builddir
        ../run-analysis.sh

`run-analysis.sh` is kind of like `configure` and `make` combined:
the build directory can be wherever you want
and you can name it whatever you want.
(You could just run it right here in the source tree, and it would work,
but don't do that -- it spits out files all over the place and
then you'd have to clean up your source tree later.)

Output goes to `hazards.txt` in the builddir.

To use this analysis on any other codebase,
make a copy of `run-analysis.sh` and adapt it for your code.


## Overview of what is going on here

So what does `run-analysis.sh` actually do?

1.  **It insecurely downloads software over HTTP.** Yeah.
    See `run-analysis.sh` for details.

2.  It runs `run_complete`, a Perl script, which builds the target
    codebase with a custom hacked GCC, generating a few database files
    containing (among other data) the full call graph.

3.  Then it runs `analyze.py`, a Python script, which runs all the scripts
    which actually perform the analysis -- the tricky parts.
    (Those scripts are written in JS.)

Snappy, a fast compressor/decompressor.


Introduction
============

Snappy is a compression/decompression library. It does not aim for maximum
compression, or compatibility with any other compression library; instead,
it aims for very high speeds and reasonable compression. For instance,
compared to the fastest mode of zlib, Snappy is an order of magnitude faster
for most inputs, but the resulting compressed files are anywhere from 20% to
100% bigger. (For more information, see "Performance", below.)

Snappy has the following properties:

 * Fast: Compression speeds at 250 MB/sec and beyond, with no assembler code.
   See "Performance" below.
 * Stable: Over the last few years, Snappy has compressed and decompressed
   petabytes of data in Google's production environment. The Snappy bitstream
   format is stable and will not change between versions.
 * Robust: The Snappy decompressor is designed not to crash in the face of
   corrupted or malicious input.
 * Free and open source software: Snappy is licensed under a BSD-type license.
   For more information, see the included COPYING file.

Snappy has previously been called "Zippy" in some Google presentations
and the like.


Performance
===========

Snappy is intended to be fast. On a single core of a Core i7 processor
in 64-bit mode, it compresses at about 250 MB/sec or more and decompresses at
about 500 MB/sec or more. (These numbers are for the slowest inputs in our
benchmark suite; others are much faster.) In our tests, Snappy usually
is faster than algorithms in the same class (e.g. LZO, LZF, QuickLZ,
etc.) while achieving comparable compression ratios.

Typical compression ratios (based on the benchmark suite) are about 1.5-1.7x
for plain text, about 2-4x for HTML, and of course 1.0x for JPEGs, PNGs and
other already-compressed data. Similar numbers for zlib in its fastest mode
are 2.6-2.8x, 3-7x and 1.0x, respectively. More sophisticated algorithms are
capable of achieving yet higher compression rates, although usually at the
expense of speed. Of course, compression ratio will vary significantly with
the input.

Although Snappy should be fairly portable, it is primarily optimized
for 64-bit x86-compatible processors, and may run slower in other environments.
In particular:

 - Snappy uses 64-bit operations in several places to process more data at
   once than would otherwise be possible.
 - Snappy assumes unaligned 32- and 64-bit loads and stores are cheap.
   On some platforms, these must be emulated with single-byte loads
   and stores, which is much slower.
 - Snappy assumes little-endian throughout, and needs to byte-swap data in
   several places if running on a big-endian platform.

Experience has shown that even heavily tuned code can be improved.
Performance optimizations, whether for 64-bit x86 or other platforms,
are of course most welcome; see "Contact", below.


Building
========

CMake is supported and autotools will soon be deprecated.
You need CMake 3.4 or above to build:

  mkdir build
  cd build && cmake ../ && make


Usage
=====

Note that Snappy, both the implementation and the main interface,
is written in C++. However, several third-party bindings to other languages
are available; see the home page at http://google.github.io/snappy/
for more information. Also, if you want to use Snappy from C code, you can
use the included C bindings in snappy-c.h.

To use Snappy from your own C++ program, include the file "snappy.h" from
your calling file, and link against the compiled library.

There are many ways to call Snappy, but the simplest possible is

  snappy::Compress(input.data(), input.size(), &output);

and similarly

  snappy::Uncompress(input.data(), input.size(), &output);

where "input" and "output" are both instances of std::string.

There are other interfaces that are more flexible in various ways, including
support for custom (non-array) input sources. See the header file for more
information.


Tests and benchmarks
====================

When you compile Snappy, snappy_unittest is compiled in addition to the
library itself. You do not need it to use the compressor from your own library,
but it contains several useful components for Snappy development.

First of all, it contains unit tests, verifying correctness on your machine in
various scenarios. If you want to change or optimize Snappy, please run the
tests to verify you have not broken anything. Note that if you have the
Google Test library installed, unit test behavior (especially failures) will be
significantly more user-friendly. You can find Google Test at

  http://github.com/google/googletest

You probably also want the gflags library for handling of command-line flags;
you can find it at

  http://gflags.github.io/gflags/

In addition to the unit tests, snappy contains microbenchmarks used to
tune compression and decompression performance. These are automatically run
before the unit tests, but you can disable them using the flag
--run_microbenchmarks=false if you have gflags installed (otherwise you will
need to edit the source).

Finally, snappy can benchmark Snappy against a few other compression libraries
(zlib, LZO, LZF, and QuickLZ), if they were detected at configure time.
To benchmark using a given file, give the compression algorithm you want to test
Snappy against (e.g. --zlib) and then a list of one or more file names on the
command line. The testdata/ directory contains the files used by the
microbenchmark, which should provide a reasonably balanced starting point for
benchmarking. (Note that baddata[1-3].snappy are not intended as benchmarks; they
are used to verify correctness in the presence of corrupted data in the unit
test.)


Contact
=======

Snappy is distributed through GitHub. For the latest version, a bug tracker,
and other information, see

  http://google.github.io/snappy/

or the repository at

  https://github.com/google/snappy
JSON Schema Test Suite [![Build Status](https://travis-ci.org/json-schema-org/JSON-Schema-Test-Suite.svg?branch=master)](https://travis-ci.org/json-schema-org/JSON-Schema-Test-Suite)
======================

This repository contains a set of JSON objects that implementors of JSON Schema
validation libraries can use to test their validators.

It is meant to be language agnostic and should require only a JSON parser.

The conversion of the JSON objects into tests within your test framework of
choice is still the job of the validator implementor.

Structure of a Test
-------------------

If you're going to use this suite, you need to know how tests are laid out. The
tests are contained in the `tests` directory at the root of this repository.

Inside that directory is a subdirectory for each draft or version of the
schema. We'll use `draft3` as an example.

If you look inside the draft directory, there are a number of `.json` files,
which logically group a set of test cases together. Often the grouping is by
property under test, but not always, especially within optional test files
(discussed below).

Inside each `.json` file is a single array containing objects. It's easiest to
illustrate the structure of these with an example:

```json
    {
        "description": "the description of the test case",
        "schema": {"the schema that should" : "be validated against"},
        "tests": [
            {
                "description": "a specific test of a valid instance",
                "data": "the instance",
                "valid": true
            },
            {
                "description": "another specific test this time, invalid",
                "data": 15,
                "valid": false
            }
        ]
    }
```

So a description, a schema, and some tests, where tests is an array containing
one or more objects with descriptions, data, and a boolean indicating whether
they should be valid or invalid.

Coverage
--------

Draft 3 and 4 should have full coverage. If you see anything missing or think
there is a useful test missing, please send a pull request or open an issue.

Who Uses the Test Suite
-----------------------

This suite is being used by:

### Coffeescript ###

* [jsck](https://github.com/pandastrike/jsck)

### C++ ###

* [Modern C++ JSON schema validator](https://github.com/pboettch/json-schema-validator)

### Dart ###

* [json_schema](https://github.com/patefacio/json_schema) 

### Elixir ###

* [ex_json_schema](https://github.com/jonasschmidt/ex_json_schema)

### Erlang ###

* [jesse](https://github.com/for-GET/jesse)

### Go ###

* [gojsonschema](https://github.com/sigu-399/gojsonschema) 
* [validate-json](https://github.com/cesanta/validate-json)

### Haskell ###

* [aeson-schema](https://github.com/timjb/aeson-schema)
* [hjsonschema](https://github.com/seagreen/hjsonschema)

### Java ###

* [json-schema-validator](https://github.com/daveclayton/json-schema-validator)
* [everit-org/json-schema](https://github.com/everit-org/json-schema)
* [networknt/json-schema-validator](https://github.com/networknt/json-schema-validator)

### JavaScript ###

* [json-schema-benchmark](https://github.com/Muscula/json-schema-benchmark)
* [direct-schema](https://github.com/IreneKnapp/direct-schema)
* [is-my-json-valid](https://github.com/mafintosh/is-my-json-valid)
* [jassi](https://github.com/iclanzan/jassi)
* [JaySchema](https://github.com/natesilva/jayschema)
* [json-schema-valid](https://github.com/ericgj/json-schema-valid)
* [Jsonary](https://github.com/jsonary-js/jsonary)
* [jsonschema](https://github.com/tdegrunt/jsonschema)
* [request-validator](https://github.com/bugventure/request-validator)
* [skeemas](https://github.com/Prestaul/skeemas)
* [tv4](https://github.com/geraintluff/tv4)
* [z-schema](https://github.com/zaggino/z-schema)
* [jsen](https://github.com/bugventure/jsen)
* [ajv](https://github.com/epoberezkin/ajv)
* [djv](https://github.com/korzio/djv)

### Node.js ###

The JSON Schema Test Suite is also available as an
[npm](https://www.npmjs.com/package/json-schema-test-suite) package.
Node-specific support is maintained on the [node branch](https://github.com/json-schema-org/JSON-Schema-Test-Suite/tree/node).
See [NODE-README.md](https://github.com/json-schema-org/JSON-Schema-Test-Suite/blob/node/NODE-README.md)
for more information.

### .NET ###

* [Newtonsoft.Json.Schema](https://github.com/JamesNK/Newtonsoft.Json.Schema)
* [Manatee.Json](https://github.com/gregsdennis/Manatee.Json)

### PHP ###

* [json-schema](https://github.com/justinrainbow/json-schema)
* [json-guard](https://github.com/thephpleague/json-guard)

### Python ###

* [jsonschema](https://github.com/Julian/jsonschema)

### Ruby ###

* [json-schema](https://github.com/hoxworth/json-schema)

### Rust ###

* [valico](https://github.com/rustless/valico)

### Swift ###

* [JSONSchema](https://github.com/kylef/JSONSchema.swift)

### Clojure ###

* [json-schema](https://github.com/tatut/json-schema)

### PostgreSQL ###

* [postgres-json-schema](https://github.com/gavinwahl/postgres-json-schema)

If you use it as well, please fork and send a pull request adding yourself to
the list :).

Contributing
------------

If you see something missing or incorrect, a pull request is most welcome!

There are some sanity checks in place for testing the test suite. You can run
them with `bin/jsonschema_suite check && npm test` or `tox && npm test`. They will be run automatically by
[Travis CI](https://travis-ci.org/) as well.
README file for PCRE (Perl-compatible regular expression library)
-----------------------------------------------------------------

NOTE: This set of files relates to PCRE releases that use the original API,
with library names libpcre, libpcre16, and libpcre32. January 2015 saw the
first release of a new API, known as PCRE2, with release numbers starting at
10.00 and library names libpcre2-8, libpcre2-16, and libpcre2-32. The old
libraries (now called PCRE1) are still being maintained for bug fixes, but
there will be no new development. New projects are advised to use the new PCRE2
libraries.


The latest release of PCRE1 is always available in three alternative formats
from:

  ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-xxx.tar.gz
  ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-xxx.tar.bz2
  ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-xxx.zip

There is a mailing list for discussion about the development of PCRE at
pcre-dev@exim.org. You can access the archives and subscribe or manage your
subscription here:

   https://lists.exim.org/mailman/listinfo/pcre-dev

Please read the NEWS file if you are upgrading from a previous release.
The contents of this README file are:

  The PCRE APIs
  Documentation for PCRE
  Contributions by users of PCRE
  Building PCRE on non-Unix-like systems
  Building PCRE without using autotools
  Building PCRE using autotools
  Retrieving configuration information
  Shared libraries
  Cross-compiling using autotools
  Using HP's ANSI C++ compiler (aCC)
  Compiling in Tru64 using native compilers
  Using Sun's compilers for Solaris
  Using PCRE from MySQL
  Making new tarballs
  Testing PCRE
  Character tables
  File manifest


The PCRE APIs
-------------

PCRE is written in C, and it has its own API. There are three sets of
functions, one for the 8-bit library, which processes strings of bytes, one for
the 16-bit library, which processes strings of 16-bit values, and one for the
32-bit library, which processes strings of 32-bit values. The distribution also
includes a set of C++ wrapper functions (see the pcrecpp man page for details),
courtesy of Google Inc., which can be used to call the 8-bit PCRE library from
C++. Other C++ wrappers have been created from time to time. See, for example:
https://github.com/YasserAsmi/regexp, which aims to be simple and similar in
style to the C API.

The distribution also contains a set of C wrapper functions (again, just for
the 8-bit library) that are based on the POSIX regular expression API (see the
pcreposix man page). These end up in the library called libpcreposix. Note that
this just provides a POSIX calling interface to PCRE; the regular expressions
themselves still follow Perl syntax and semantics. The POSIX API is restricted,
and does not give full access to all of PCRE's facilities.

The header file for the POSIX-style functions is called pcreposix.h. The
official POSIX name is regex.h, but I did not want to risk possible problems
with existing files of that name by distributing it that way. To use PCRE with
an existing program that uses the POSIX API, pcreposix.h will have to be
renamed or pointed at by a link.

If you are using the POSIX interface to PCRE and there is already a POSIX regex
library installed on your system, as well as worrying about the regex.h header
file (as mentioned above), you must also take care when linking programs to
ensure that they link with PCRE's libpcreposix library. Otherwise they may pick
up the POSIX functions of the same name from the other library.

One way of avoiding this confusion is to compile PCRE with the addition of
-Dregcomp=PCREregcomp (and similarly for the other POSIX functions) to the
compiler flags (CFLAGS if you are using "configure" -- see below). This has the
effect of renaming the functions so that the names no longer clash. Of course,
you have to do the same thing for your applications, or write them using the
new names.


Documentation for PCRE
----------------------

If you install PCRE in the normal way on a Unix-like system, you will end up
with a set of man pages whose names all start with "pcre". The one that is just
called "pcre" lists all the others. In addition to these man pages, the PCRE
documentation is supplied in two other forms:

  1. There are files called doc/pcre.txt, doc/pcregrep.txt, and
     doc/pcretest.txt in the source distribution. The first of these is a
     concatenation of the text forms of all the section 3 man pages except
     the listing of pcredemo.c and those that summarize individual functions.
     The other two are the text forms of the section 1 man pages for the
     pcregrep and pcretest commands. These text forms are provided for ease of
     scanning with text editors or similar tools. They are installed in
     <prefix>/share/doc/pcre, where <prefix> is the installation prefix
     (defaulting to /usr/local).

  2. A set of files containing all the documentation in HTML form, hyperlinked
     in various ways, and rooted in a file called index.html, is distributed in
     doc/html and installed in <prefix>/share/doc/pcre/html.

Users of PCRE have contributed files containing the documentation for various
releases in CHM format. These can be found in the Contrib directory of the FTP
site (see next section).


Contributions by users of PCRE
------------------------------

You can find contributions from PCRE users in the directory

  ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/Contrib

There is a README file giving brief descriptions of what they are. Some are
complete in themselves; others are pointers to URLs containing relevant files.
Some of this material is likely to be well out-of-date. Several of the earlier
contributions provided support for compiling PCRE on various flavours of
Windows (I myself do not use Windows). Nowadays there is more Windows support
in the standard distribution, so these contibutions have been archived.

A PCRE user maintains downloadable Windows binaries of the pcregrep and
pcretest programs here:

  http://www.rexegg.com/pcregrep-pcretest.html


Building PCRE on non-Unix-like systems
--------------------------------------

For a non-Unix-like system, please read the comments in the file
NON-AUTOTOOLS-BUILD, though if your system supports the use of "configure" and
"make" you may be able to build PCRE using autotools in the same way as for
many Unix-like systems.

PCRE can also be configured using the GUI facility provided by CMake's
cmake-gui command. This creates Makefiles, solution files, etc. The file
NON-AUTOTOOLS-BUILD has information about CMake.

PCRE has been compiled on many different operating systems. It should be
straightforward to build PCRE on any system that has a Standard C compiler and
library, because it uses only Standard C functions.


Building PCRE without using autotools
-------------------------------------

The use of autotools (in particular, libtool) is problematic in some
environments, even some that are Unix or Unix-like. See the NON-AUTOTOOLS-BUILD
file for ways of building PCRE without using autotools.


Building PCRE using autotools
-----------------------------

If you are using HP's ANSI C++ compiler (aCC), please see the special note
in the section entitled "Using HP's ANSI C++ compiler (aCC)" below.

The following instructions assume the use of the widely used "configure; make;
make install" (autotools) process.

To build PCRE on system that supports autotools, first run the "configure"
command from the PCRE distribution directory, with your current directory set
to the directory where you want the files to be created. This command is a
standard GNU "autoconf" configuration script, for which generic instructions
are supplied in the file INSTALL.

Most commonly, people build PCRE within its own distribution directory, and in
this case, on many systems, just running "./configure" is sufficient. However,
the usual methods of changing standard defaults are available. For example:

CFLAGS='-O2 -Wall' ./configure --prefix=/opt/local

This command specifies that the C compiler should be run with the flags '-O2
-Wall' instead of the default, and that "make install" should install PCRE
under /opt/local instead of the default /usr/local.

If you want to build in a different directory, just run "configure" with that
directory as current. For example, suppose you have unpacked the PCRE source
into /source/pcre/pcre-xxx, but you want to build it in /build/pcre/pcre-xxx:

cd /build/pcre/pcre-xxx
/source/pcre/pcre-xxx/configure

PCRE is written in C and is normally compiled as a C library. However, it is
possible to build it as a C++ library, though the provided building apparatus
does not have any features to support this.

There are some optional features that can be included or omitted from the PCRE
library. They are also documented in the pcrebuild man page.

. By default, both shared and static libraries are built. You can change this
  by adding one of these options to the "configure" command:

  --disable-shared
  --disable-static

  (See also "Shared libraries on Unix-like systems" below.)

. By default, only the 8-bit library is built. If you add --enable-pcre16 to
  the "configure" command, the 16-bit library is also built. If you add
  --enable-pcre32 to the "configure" command, the 32-bit library is also built.
  If you want only the 16-bit or 32-bit library, use --disable-pcre8 to disable
  building the 8-bit library.

. If you are building the 8-bit library and want to suppress the building of
  the C++ wrapper library, you can add --disable-cpp to the "configure"
  command. Otherwise, when "configure" is run without --disable-pcre8, it will
  try to find a C++ compiler and C++ header files, and if it succeeds, it will
  try to build the C++ wrapper.

. If you want to include support for just-in-time compiling, which can give
  large performance improvements on certain platforms, add --enable-jit to the
  "configure" command. This support is available only for certain hardware
  architectures. If you try to enable it on an unsupported architecture, there
  will be a compile time error.

. When JIT support is enabled, pcregrep automatically makes use of it, unless
  you add --disable-pcregrep-jit to the "configure" command.

. If you want to make use of the support for UTF-8 Unicode character strings in
  the 8-bit library, or UTF-16 Unicode character strings in the 16-bit library,
  or UTF-32 Unicode character strings in the 32-bit library, you must add
  --enable-utf to the "configure" command. Without it, the code for handling
  UTF-8, UTF-16 and UTF-8 is not included in the relevant library. Even
  when --enable-utf is included, the use of a UTF encoding still has to be
  enabled by an option at run time. When PCRE is compiled with this option, its
  input can only either be ASCII or UTF-8/16/32, even when running on EBCDIC
  platforms. It is not possible to use both --enable-utf and --enable-ebcdic at
  the same time.

. There are no separate options for enabling UTF-8, UTF-16 and UTF-32
  independently because that would allow ridiculous settings such as requesting
  UTF-16 support while building only the 8-bit library. However, the option
  --enable-utf8 is retained for backwards compatibility with earlier releases
  that did not support 16-bit or 32-bit character strings. It is synonymous with
  --enable-utf. It is not possible to configure one library with UTF support
  and the other without in the same configuration.

. If, in addition to support for UTF-8/16/32 character strings, you want to
  include support for the \P, \p, and \X sequences that recognize Unicode
  character properties, you must add --enable-unicode-properties to the
  "configure" command. This adds about 30K to the size of the library (in the
  form of a property table); only the basic two-letter properties such as Lu
  are supported.

. You can build PCRE to recognize either CR or LF or the sequence CRLF or any
  of the preceding, or any of the Unicode newline sequences as indicating the
  end of a line. Whatever you specify at build time is the default; the caller
  of PCRE can change the selection at run time. The default newline indicator
  is a single LF character (the Unix standard). You can specify the default
  newline indicator by adding --enable-newline-is-cr or --enable-newline-is-lf
  or --enable-newline-is-crlf or --enable-newline-is-anycrlf or
  --enable-newline-is-any to the "configure" command, respectively.

  If you specify --enable-newline-is-cr or --enable-newline-is-crlf, some of
  the standard tests will fail, because the lines in the test files end with
  LF. Even if the files are edited to change the line endings, there are likely
  to be some failures. With --enable-newline-is-anycrlf or
  --enable-newline-is-any, many tests should succeed, but there may be some
  failures.

. By default, the sequence \R in a pattern matches any Unicode line ending
  sequence. This is independent of the option specifying what PCRE considers to
  be the end of a line (see above). However, the caller of PCRE can restrict \R
  to match only CR, LF, or CRLF. You can make this the default by adding
  --enable-bsr-anycrlf to the "configure" command (bsr = "backslash R").

. When called via the POSIX interface, PCRE uses malloc() to get additional
  storage for processing capturing parentheses if there are more than 10 of
  them in a pattern. You can increase this threshold by setting, for example,

  --with-posix-malloc-threshold=20

  on the "configure" command.

. PCRE has a counter that limits the depth of nesting of parentheses in a
  pattern. This limits the amount of system stack that a pattern uses when it
  is compiled. The default is 250, but you can change it by setting, for
  example,

  --with-parens-nest-limit=500

. PCRE has a counter that can be set to limit the amount of resources it uses
  when matching a pattern. If the limit is exceeded during a match, the match
  fails. The default is ten million. You can change the default by setting, for
  example,

  --with-match-limit=500000

  on the "configure" command. This is just the default; individual calls to
  pcre_exec() can supply their own value. There is more discussion on the
  pcreapi man page.

. There is a separate counter that limits the depth of recursive function calls
  during a matching process. This also has a default of ten million, which is
  essentially "unlimited". You can change the default by setting, for example,

  --with-match-limit-recursion=500000

  Recursive function calls use up the runtime stack; running out of stack can
  cause programs to crash in strange ways. There is a discussion about stack
  sizes in the pcrestack man page.

. The default maximum compiled pattern size is around 64K. You can increase
  this by adding --with-link-size=3 to the "configure" command. In the 8-bit
  library, PCRE then uses three bytes instead of two for offsets to different
  parts of the compiled pattern. In the 16-bit library, --with-link-size=3 is
  the same as --with-link-size=4, which (in both libraries) uses four-byte
  offsets. Increasing the internal link size reduces performance. In the 32-bit
  library, the only supported link size is 4.

. You can build PCRE so that its internal match() function that is called from
  pcre_exec() does not call itself recursively. Instead, it uses memory blocks
  obtained from the heap via the special functions pcre_stack_malloc() and
  pcre_stack_free() to save data that would otherwise be saved on the stack. To
  build PCRE like this, use

  --disable-stack-for-recursion

  on the "configure" command. PCRE runs more slowly in this mode, but it may be
  necessary in environments with limited stack sizes. This applies only to the
  normal execution of the pcre_exec() function; if JIT support is being
  successfully used, it is not relevant. Equally, it does not apply to
  pcre_dfa_exec(), which does not use deeply nested recursion. There is a
  discussion about stack sizes in the pcrestack man page.

. For speed, PCRE uses four tables for manipulating and identifying characters
  whose code point values are less than 256. By default, it uses a set of
  tables for ASCII encoding that is part of the distribution. If you specify

  --enable-rebuild-chartables

  a program called dftables is compiled and run in the default C locale when
  you obey "make". It builds a source file called pcre_chartables.c. If you do
  not specify this option, pcre_chartables.c is created as a copy of
  pcre_chartables.c.dist. See "Character tables" below for further information.

. It is possible to compile PCRE for use on systems that use EBCDIC as their
  character code (as opposed to ASCII/Unicode) by specifying

  --enable-ebcdic

  This automatically implies --enable-rebuild-chartables (see above). However,
  when PCRE is built this way, it always operates in EBCDIC. It cannot support
  both EBCDIC and UTF-8/16/32. There is a second option, --enable-ebcdic-nl25,
  which specifies that the code value for the EBCDIC NL character is 0x25
  instead of the default 0x15.

. In environments where valgrind is installed, if you specify

  --enable-valgrind

  PCRE will use valgrind annotations to mark certain memory regions as
  unaddressable. This allows it to detect invalid memory accesses, and is
  mostly useful for debugging PCRE itself.

. In environments where the gcc compiler is used and lcov version 1.6 or above
  is installed, if you specify

  --enable-coverage

  the build process implements a code coverage report for the test suite. The
  report is generated by running "make coverage". If ccache is installed on
  your system, it must be disabled when building PCRE for coverage reporting.
  You can do this by setting the environment variable CCACHE_DISABLE=1 before
  running "make" to build PCRE. There is more information about coverage
  reporting in the "pcrebuild" documentation.

. The pcregrep program currently supports only 8-bit data files, and so
  requires the 8-bit PCRE library. It is possible to compile pcregrep to use
  libz and/or libbz2, in order to read .gz and .bz2 files (respectively), by
  specifying one or both of

  --enable-pcregrep-libz
  --enable-pcregrep-libbz2

  Of course, the relevant libraries must be installed on your system.

. The default size (in bytes) of the internal buffer used by pcregrep can be
  set by, for example:

  --with-pcregrep-bufsize=51200

  The value must be a plain integer. The default is 20480.

. It is possible to compile pcretest so that it links with the libreadline
  or libedit libraries, by specifying, respectively,

  --enable-pcretest-libreadline or --enable-pcretest-libedit

  If this is done, when pcretest's input is from a terminal, it reads it using
  the readline() function. This provides line-editing and history facilities.
  Note that libreadline is GPL-licenced, so if you distribute a binary of
  pcretest linked in this way, there may be licensing issues. These can be
  avoided by linking with libedit (which has a BSD licence) instead.

  Enabling libreadline causes the -lreadline option to be added to the pcretest
  build. In many operating environments with a sytem-installed readline
  library this is sufficient. However, in some environments (e.g. if an
  unmodified distribution version of readline is in use), it may be necessary
  to specify something like LIBS="-lncurses" as well. This is because, to quote
  the readline INSTALL, "Readline uses the termcap functions, but does not link
  with the termcap or curses library itself, allowing applications which link
  with readline the to choose an appropriate library." If you get error
  messages about missing functions tgetstr, tgetent, tputs, tgetflag, or tgoto,
  this is the problem, and linking with the ncurses library should fix it.

The "configure" script builds the following files for the basic C library:

. Makefile             the makefile that builds the library
. config.h             build-time configuration options for the library
. pcre.h               the public PCRE header file
. pcre-config          script that shows the building settings such as CFLAGS
                         that were set for "configure"
. libpcre.pc         ) data for the pkg-config command
. libpcre16.pc       )
. libpcre32.pc       )
. libpcreposix.pc    )
. libtool              script that builds shared and/or static libraries

Versions of config.h and pcre.h are distributed in the PCRE tarballs under the
names config.h.generic and pcre.h.generic. These are provided for those who
have to built PCRE without using "configure" or CMake. If you use "configure"
or CMake, the .generic versions are not used.

When building the 8-bit library, if a C++ compiler is found, the following
files are also built:

. libpcrecpp.pc        data for the pkg-config command
. pcrecpparg.h         header file for calling PCRE via the C++ wrapper
. pcre_stringpiece.h   header for the C++ "stringpiece" functions

The "configure" script also creates config.status, which is an executable
script that can be run to recreate the configuration, and config.log, which
contains compiler output from tests that "configure" runs.

Once "configure" has run, you can run "make". This builds the the libraries
libpcre, libpcre16 and/or libpcre32, and a test program called pcretest. If you
enabled JIT support with --enable-jit, a test program called pcre_jit_test is
built as well.

If the 8-bit library is built, libpcreposix and the pcregrep command are also
built, and if a C++ compiler was found on your system, and you did not disable
it with --disable-cpp, "make" builds the C++ wrapper library, which is called
libpcrecpp, as well as some test programs called pcrecpp_unittest,
pcre_scanner_unittest, and pcre_stringpiece_unittest.

The command "make check" runs all the appropriate tests. Details of the PCRE
tests are given below in a separate section of this document.

You can use "make install" to install PCRE into live directories on your
system. The following are installed (file names are all relative to the
<prefix> that is set when "configure" is run):

  Commands (bin):
    pcretest
    pcregrep (if 8-bit support is enabled)
    pcre-config

  Libraries (lib):
    libpcre16     (if 16-bit support is enabled)
    libpcre32     (if 32-bit support is enabled)
    libpcre       (if 8-bit support is enabled)
    libpcreposix  (if 8-bit support is enabled)
    libpcrecpp    (if 8-bit and C++ support is enabled)

  Configuration information (lib/pkgconfig):
    libpcre16.pc
    libpcre32.pc
    libpcre.pc
    libpcreposix.pc
    libpcrecpp.pc (if C++ support is enabled)

  Header files (include):
    pcre.h
    pcreposix.h
    pcre_scanner.h      )
    pcre_stringpiece.h  ) if C++ support is enabled
    pcrecpp.h           )
    pcrecpparg.h        )

  Man pages (share/man/man{1,3}):
    pcregrep.1
    pcretest.1
    pcre-config.1
    pcre.3
    pcre*.3 (lots more pages, all starting "pcre")

  HTML documentation (share/doc/pcre/html):
    index.html
    *.html (lots more pages, hyperlinked from index.html)

  Text file documentation (share/doc/pcre):
    AUTHORS
    COPYING
    ChangeLog
    LICENCE
    NEWS
    README
    pcre.txt         (a concatenation of the man(3) pages)
    pcretest.txt     the pcretest man page
    pcregrep.txt     the pcregrep man page
    pcre-config.txt  the pcre-config man page

If you want to remove PCRE from your system, you can run "make uninstall".
This removes all the files that "make install" installed. However, it does not
remove any directories, because these are often shared with other programs.


Retrieving configuration information
------------------------------------

Running "make install" installs the command pcre-config, which can be used to
recall information about the PCRE configuration and installation. For example:

  pcre-config --version

prints the version number, and

  pcre-config --libs

outputs information about where the library is installed. This command can be
included in makefiles for programs that use PCRE, saving the programmer from
having to remember too many details.

The pkg-config command is another system for saving and retrieving information
about installed libraries. Instead of separate commands for each library, a
single command is used. For example:

  pkg-config --cflags pcre

The data is held in *.pc files that are installed in a directory called
<prefix>/lib/pkgconfig.


Shared libraries
----------------

The default distribution builds PCRE as shared libraries and static libraries,
as long as the operating system supports shared libraries. Shared library
support relies on the "libtool" script which is built as part of the
"configure" process.

The libtool script is used to compile and link both shared and static
libraries. They are placed in a subdirectory called .libs when they are newly
built. The programs pcretest and pcregrep are built to use these uninstalled
libraries (by means of wrapper scripts in the case of shared libraries). When
you use "make install" to install shared libraries, pcregrep and pcretest are
automatically re-built to use the newly installed shared libraries before being
installed themselves. However, the versions left in the build directory still
use the uninstalled libraries.

To build PCRE using static libraries only you must use --disable-shared when
configuring it. For example:

./configure --prefix=/usr/gnu --disable-shared

Then run "make" in the usual way. Similarly, you can use --disable-static to
build only shared libraries.


Cross-compiling using autotools
-------------------------------

You can specify CC and CFLAGS in the normal way to the "configure" command, in
order to cross-compile PCRE for some other host. However, you should NOT
specify --enable-rebuild-chartables, because if you do, the dftables.c source
file is compiled and run on the local host, in order to generate the inbuilt
character tables (the pcre_chartables.c file). This will probably not work,
because dftables.c needs to be compiled with the local compiler, not the cross
compiler.

When --enable-rebuild-chartables is not specified, pcre_chartables.c is created
by making a copy of pcre_chartables.c.dist, which is a default set of tables
that assumes ASCII code. Cross-compiling with the default tables should not be
a problem.

If you need to modify the character tables when cross-compiling, you should
move pcre_chartables.c.dist out of the way, then compile dftables.c by hand and
run it on the local host to make a new version of pcre_chartables.c.dist.
Then when you cross-compile PCRE this new version of the tables will be used.


Using HP's ANSI C++ compiler (aCC)
----------------------------------

Unless C++ support is disabled by specifying the "--disable-cpp" option of the
"configure" script, you must include the "-AA" option in the CXXFLAGS
environment variable in order for the C++ components to compile correctly.

Also, note that the aCC compiler on PA-RISC platforms may have a defect whereby
needed libraries fail to get included when specifying the "-AA" compiler
option. If you experience unresolved symbols when linking the C++ programs,
use the workaround of specifying the following environment variable prior to
running the "configure" script:

  CXXLDFLAGS="-lstd_v2 -lCsup_v2"


Compiling in Tru64 using native compilers
-----------------------------------------

The following error may occur when compiling with native compilers in the Tru64
operating system:

  CXX    libpcrecpp_la-pcrecpp.lo
cxx: Error: /usr/lib/cmplrs/cxx/V7.1-006/include/cxx/iosfwd, line 58: #error
          directive: "cannot include iosfwd -- define __USE_STD_IOSTREAM to
          override default - see section 7.1.2 of the C++ Using Guide"
#error "cannot include iosfwd -- define __USE_STD_IOSTREAM to override default
- see section 7.1.2 of the C++ Using Guide"

This may be followed by other errors, complaining that 'namespace "std" has no
member'. The solution to this is to add the line

#define __USE_STD_IOSTREAM 1

to the config.h file.


Using Sun's compilers for Solaris
---------------------------------

A user reports that the following configurations work on Solaris 9 sparcv9 and
Solaris 9 x86 (32-bit):

  Solaris 9 sparcv9: ./configure --disable-cpp CC=/bin/cc CFLAGS="-m64 -g"
  Solaris 9 x86:     ./configure --disable-cpp CC=/bin/cc CFLAGS="-g"


Using PCRE from MySQL
---------------------

On systems where both PCRE and MySQL are installed, it is possible to make use
of PCRE from within MySQL, as an alternative to the built-in pattern matching.
There is a web page that tells you how to do this:

  http://www.mysqludf.org/lib_mysqludf_preg/index.php


Making new tarballs
-------------------

The command "make dist" creates three PCRE tarballs, in tar.gz, tar.bz2, and
zip formats. The command "make distcheck" does the same, but then does a trial
build of the new distribution to ensure that it works.

If you have modified any of the man page sources in the doc directory, you
should first run the PrepareRelease script before making a distribution. This
script creates the .txt and HTML forms of the documentation from the man pages.


Testing PCRE
------------

To test the basic PCRE library on a Unix-like system, run the RunTest script.
There is another script called RunGrepTest that tests the options of the
pcregrep command. If the C++ wrapper library is built, three test programs
called pcrecpp_unittest, pcre_scanner_unittest, and pcre_stringpiece_unittest
are also built. When JIT support is enabled, another test program called
pcre_jit_test is built.

Both the scripts and all the program tests are run if you obey "make check" or
"make test". For other environments, see the instructions in
NON-AUTOTOOLS-BUILD.

The RunTest script runs the pcretest test program (which is documented in its
own man page) on each of the relevant testinput files in the testdata
directory, and compares the output with the contents of the corresponding
testoutput files. RunTest uses a file called testtry to hold the main output
from pcretest. Other files whose names begin with "test" are used as working
files in some tests.

Some tests are relevant only when certain build-time options were selected. For
example, the tests for UTF-8/16/32 support are run only if --enable-utf was
used. RunTest outputs a comment when it skips a test.

Many of the tests that are not skipped are run up to three times. The second
run forces pcre_study() to be called for all patterns except for a few in some
tests that are marked "never study" (see the pcretest program for how this is
done). If JIT support is available, the non-DFA tests are run a third time,
this time with a forced pcre_study() with the PCRE_STUDY_JIT_COMPILE option.
This testing can be suppressed by putting "nojit" on the RunTest command line.

The entire set of tests is run once for each of the 8-bit, 16-bit and 32-bit
libraries that are enabled. If you want to run just one set of tests, call
RunTest with either the -8, -16 or -32 option.

If valgrind is installed, you can run the tests under it by putting "valgrind"
on the RunTest command line. To run pcretest on just one or more specific test
files, give their numbers as arguments to RunTest, for example:

  RunTest 2 7 11

You can also specify ranges of tests such as 3-6 or 3- (meaning 3 to the
end), or a number preceded by ~ to exclude a test. For example:

  Runtest 3-15 ~10

This runs tests 3 to 15, excluding test 10, and just ~13 runs all the tests
except test 13. Whatever order the arguments are in, the tests are always run
in numerical order.

You can also call RunTest with the single argument "list" to cause it to output
a list of tests.

The first test file can be fed directly into the perltest.pl script to check
that Perl gives the same results. The only difference you should see is in the
first few lines, where the Perl version is given instead of the PCRE version.

The second set of tests check pcre_fullinfo(), pcre_study(),
pcre_copy_substring(), pcre_get_substring(), pcre_get_substring_list(), error
detection, and run-time flags that are specific to PCRE, as well as the POSIX
wrapper API. It also uses the debugging flags to check some of the internals of
pcre_compile().

If you build PCRE with a locale setting that is not the standard C locale, the
character tables may be different (see next paragraph). In some cases, this may
cause failures in the second set of tests. For example, in a locale where the
isprint() function yields TRUE for characters in the range 128-255, the use of
[:isascii:] inside a character class defines a different set of characters, and
this shows up in this test as a difference in the compiled code, which is being
listed for checking. Where the comparison test output contains [\x00-\x7f] the
test will contain [\x00-\xff], and similarly in some other cases. This is not a
bug in PCRE.

The third set of tests checks pcre_maketables(), the facility for building a
set of character tables for a specific locale and using them instead of the
default tables. The tests make use of the "fr_FR" (French) locale. Before
running the test, the script checks for the presence of this locale by running
the "locale" command. If that command fails, or if it doesn't include "fr_FR"
in the list of available locales, the third test cannot be run, and a comment
is output to say why. If running this test produces instances of the error

  ** Failed to set locale "fr_FR"

in the comparison output, it means that locale is not available on your system,
despite being listed by "locale". This does not mean that PCRE is broken.

[If you are trying to run this test on Windows, you may be able to get it to
work by changing "fr_FR" to "french" everywhere it occurs. Alternatively, use
RunTest.bat. The version of RunTest.bat included with PCRE 7.4 and above uses
Windows versions of test 2. More info on using RunTest.bat is included in the
document entitled NON-UNIX-USE.]

The fourth and fifth tests check the UTF-8/16/32 support and error handling and
internal UTF features of PCRE that are not relevant to Perl, respectively. The
sixth and seventh tests do the same for Unicode character properties support.

The eighth, ninth, and tenth tests check the pcre_dfa_exec() alternative
matching function, in non-UTF-8/16/32 mode, UTF-8/16/32 mode, and UTF-8/16/32
mode with Unicode property support, respectively.

The eleventh test checks some internal offsets and code size features; it is
run only when the default "link size" of 2 is set (in other cases the sizes
change) and when Unicode property support is enabled.

The twelfth test is run only when JIT support is available, and the thirteenth
test is run only when JIT support is not available. They test some JIT-specific
features such as information output from pcretest about JIT compilation.

The fourteenth, fifteenth, and sixteenth tests are run only in 8-bit mode, and
the seventeenth, eighteenth, and nineteenth tests are run only in 16/32-bit
mode. These are tests that generate different output in the two modes. They are
for general cases, UTF-8/16/32 support, and Unicode property support,
respectively.

The twentieth test is run only in 16/32-bit mode. It tests some specific
16/32-bit features of the DFA matching engine.

The twenty-first and twenty-second tests are run only in 16/32-bit mode, when
the link size is set to 2 for the 16-bit library. They test reloading
pre-compiled patterns.

The twenty-third and twenty-fourth tests are run only in 16-bit mode. They are
for general cases, and UTF-16 support, respectively.

The twenty-fifth and twenty-sixth tests are run only in 32-bit mode. They are
for general cases, and UTF-32 support, respectively.


Character tables
----------------

For speed, PCRE uses four tables for manipulating and identifying characters
whose code point values are less than 256. The final argument of the
pcre_compile() function is a pointer to a block of memory containing the
concatenated tables. A call to pcre_maketables() can be used to generate a set
of tables in the current locale. If the final argument for pcre_compile() is
passed as NULL, a set of default tables that is built into the binary is used.

The source file called pcre_chartables.c contains the default set of tables. By
default, this is created as a copy of pcre_chartables.c.dist, which contains
tables for ASCII coding. However, if --enable-rebuild-chartables is specified
for ./configure, a different version of pcre_chartables.c is built by the
program dftables (compiled from dftables.c), which uses the ANSI C character
handling functions such as isalnum(), isalpha(), isupper(), islower(), etc. to
build the table sources. This means that the default C locale which is set for
your system will control the contents of these default tables. You can change
the default tables by editing pcre_chartables.c and then re-building PCRE. If
you do this, you should take care to ensure that the file does not get
automatically re-generated. The best way to do this is to move
pcre_chartables.c.dist out of the way and replace it with your customized
tables.

When the dftables program is run as a result of --enable-rebuild-chartables,
it uses the default C locale that is set on your system. It does not pay
attention to the LC_xxx environment variables. In other words, it uses the
system's default locale rather than whatever the compiling user happens to have
set. If you really do want to build a source set of character tables in a
locale that is specified by the LC_xxx variables, you can run the dftables
program by hand with the -L option. For example:

  ./dftables -L pcre_chartables.c.special

The first two 256-byte tables provide lower casing and case flipping functions,
respectively. The next table consists of three 32-byte bit maps which identify
digits, "word" characters, and white space, respectively. These are used when
building 32-byte bit maps that represent character classes for code points less
than 256.

The final 256-byte table has bits indicating various character types, as
follows:

    1   white space character
    2   letter
    4   decimal digit
    8   hexadecimal digit
   16   alphanumeric or '_'
  128   regular expression metacharacter or binary zero

You should not alter the set of characters that contain the 128 bit, as that
will cause PCRE to malfunction.


File manifest
-------------

The distribution should contain the files listed below. Where a file name is
given as pcre[16|32]_xxx it means that there are three files, one with the name
pcre_xxx, one with the name pcre16_xx, and a third with the name pcre32_xxx.

(A) Source files of the PCRE library functions and their headers:

  dftables.c              auxiliary program for building pcre_chartables.c
                          when --enable-rebuild-chartables is specified

  pcre_chartables.c.dist  a default set of character tables that assume ASCII
                          coding; used, unless --enable-rebuild-chartables is
                          specified, by copying to pcre[16]_chartables.c

  pcreposix.c                )
  pcre[16|32]_byte_order.c   )
  pcre[16|32]_compile.c      )
  pcre[16|32]_config.c       )
  pcre[16|32]_dfa_exec.c     )
  pcre[16|32]_exec.c         )
  pcre[16|32]_fullinfo.c     )
  pcre[16|32]_get.c          ) sources for the functions in the library,
  pcre[16|32]_globals.c      )   and some internal functions that they use
  pcre[16|32]_jit_compile.c  )
  pcre[16|32]_maketables.c   )
  pcre[16|32]_newline.c      )
  pcre[16|32]_refcount.c     )
  pcre[16|32]_string_utils.c )
  pcre[16|32]_study.c        )
  pcre[16|32]_tables.c       )
  pcre[16|32]_ucd.c          )
  pcre[16|32]_version.c      )
  pcre[16|32]_xclass.c       )
  pcre_ord2utf8.c            )
  pcre_valid_utf8.c          )
  pcre16_ord2utf16.c         )
  pcre16_utf16_utils.c       )
  pcre16_valid_utf16.c       )
  pcre32_utf32_utils.c       )
  pcre32_valid_utf32.c       )

  pcre[16|32]_printint.c     ) debugging function that is used by pcretest,
                             )   and can also be #included in pcre_compile()

  pcre.h.in               template for pcre.h when built by "configure"
  pcreposix.h             header for the external POSIX wrapper API
  pcre_internal.h         header for internal use
  sljit/*                 16 files that make up the JIT compiler
  ucp.h                   header for Unicode property handling

  config.h.in             template for config.h, which is built by "configure"

  pcrecpp.h               public header file for the C++ wrapper
  pcrecpparg.h.in         template for another C++ header file
  pcre_scanner.h          public header file for C++ scanner functions
  pcrecpp.cc              )
  pcre_scanner.cc         ) source for the C++ wrapper library

  pcre_stringpiece.h.in   template for pcre_stringpiece.h, the header for the
                            C++ stringpiece functions
  pcre_stringpiece.cc     source for the C++ stringpiece functions

(B) Source files for programs that use PCRE:

  pcredemo.c              simple demonstration of coding calls to PCRE
  pcregrep.c              source of a grep utility that uses PCRE
  pcretest.c              comprehensive test program

(C) Auxiliary files:

  132html                 script to turn "man" pages into HTML
  AUTHORS                 information about the author of PCRE
  ChangeLog               log of changes to the code
  CleanTxt                script to clean nroff output for txt man pages
  Detrail                 script to remove trailing spaces
  HACKING                 some notes about the internals of PCRE
  INSTALL                 generic installation instructions
  LICENCE                 conditions for the use of PCRE
  COPYING                 the same, using GNU's standard name
  Makefile.in             ) template for Unix Makefile, which is built by
                          )   "configure"
  Makefile.am             ) the automake input that was used to create
                          )   Makefile.in
  NEWS                    important changes in this release
  NON-UNIX-USE            the previous name for NON-AUTOTOOLS-BUILD
  NON-AUTOTOOLS-BUILD     notes on building PCRE without using autotools
  PrepareRelease          script to make preparations for "make dist"
  README                  this file
  RunTest                 a Unix shell script for running tests
  RunGrepTest             a Unix shell script for pcregrep tests
  aclocal.m4              m4 macros (generated by "aclocal")
  config.guess            ) files used by libtool,
  config.sub              )   used only when building a shared library
  configure               a configuring shell script (built by autoconf)
  configure.ac            ) the autoconf input that was used to build
                          )   "configure" and config.h
  depcomp                 ) script to find program dependencies, generated by
                          )   automake
  doc/*.3                 man page sources for PCRE
  doc/*.1                 man page sources for pcregrep and pcretest
  doc/index.html.src      the base HTML page
  doc/html/*              HTML documentation
  doc/pcre.txt            plain text version of the man pages
  doc/pcretest.txt        plain text documentation of test program
  doc/perltest.txt        plain text documentation of Perl test program
  install-sh              a shell script for installing files
  libpcre16.pc.in         template for libpcre16.pc for pkg-config
  libpcre32.pc.in         template for libpcre32.pc for pkg-config
  libpcre.pc.in           template for libpcre.pc for pkg-config
  libpcreposix.pc.in      template for libpcreposix.pc for pkg-config
  libpcrecpp.pc.in        template for libpcrecpp.pc for pkg-config
  ltmain.sh               file used to build a libtool script
  missing                 ) common stub for a few missing GNU programs while
                          )   installing, generated by automake
  mkinstalldirs           script for making install directories
  perltest.pl             Perl test program
  pcre-config.in          source of script which retains PCRE information
  pcre_jit_test.c         test program for the JIT compiler
  pcrecpp_unittest.cc          )
  pcre_scanner_unittest.cc     ) test programs for the C++ wrapper
  pcre_stringpiece_unittest.cc )
  testdata/testinput*     test data for main library tests
  testdata/testoutput*    expected test results
  testdata/grep*          input and output for pcregrep tests
  testdata/*              other supporting test files

(D) Auxiliary files for cmake support

  cmake/COPYING-CMAKE-SCRIPTS
  cmake/FindPackageHandleStandardArgs.cmake
  cmake/FindEditline.cmake
  cmake/FindReadline.cmake
  CMakeLists.txt
  config-cmake.h.in

(E) Auxiliary files for VPASCAL

  makevp.bat
  makevp_c.txt
  makevp_l.txt
  pcregexp.pas

(F) Auxiliary files for building PCRE "by hand"

  pcre.h.generic          ) a version of the public PCRE header file
                          )   for use in non-"configure" environments
  config.h.generic        ) a version of config.h for use in non-"configure"
                          )   environments

(F) Miscellaneous

  RunTest.bat            a script for running tests under Windows

Philip Hazel
Email local part: ph10
Email domain: cam.ac.uk
Last updated: 10 February 2015
libstemmer_c
============

This document pertains to the C version of the libstemmer distribution,
available for download from:

http://snowball.tartarus.org/dist/libstemmer_c.tgz


Compiling the library
=====================

A simple makefile is provided for Unix style systems.  On such systems, it
should be possible simply to run "make", and the file "libstemmer.o"
and the example program "stemwords" will be generated.

If this doesn't work on your system, you need to write your own build
system (or call the compiler directly).  The files to compile are
all contained in the "libstemmer", "runtime" and "src_c" directories,
and the public header file is contained in the "include" directory.

The library comes in two flavours; UTF-8 only, and UTF-8 plus other character
sets.  To use the utf-8 only flavour, compile "libstemmer_utf8.c" instead of
"libstemmer.c".

For convenience "mkinc.mak" is a makefile fragment listing the source files and
header files used to compile the standard version of the library.
"mkinc_utf8.mak" is a comparable makefile fragment listing just the source
files for the UTF-8 only version of the library.


Using the library
=================

The library provides a simple C API.  Essentially, a new stemmer can
be obtained by using "sb_stemmer_new".  "sb_stemmer_stem" is then
used to stem a word, "sb_stemmer_length" returns the stemmed
length of the last word processed, and "sb_stemmer_delete" is
used to delete a stemmer.

Creating a stemmer is a relatively expensive operation - the expected
usage pattern is that a new stemmer is created when needed, used
to stem many words, and deleted after some time.

Stemmers are re-entrant, but not threadsafe.  In other words, if
you wish to access the same stemmer object from multiple threads,
you must ensure that all access is protected by a mutex or similar
device.

libstemmer does not currently incorporate any mechanism for caching the results
of stemming operations.  Such caching can greatly increase the performance of a
stemmer under certain situations, so suitable patches will be considered for
inclusion.

The standard libstemmer sources contain an algorithm for each of the supported
languages.  The algorithm may be selected using the english name of the
language, or using the 2 or 3 letter ISO 639 language codes.  In addition,
the traditional "Porter" stemming algorithm for english is included for
backwards compatibility purposes, but we recommend use of the "English"
stemmer in preference for new projects.

(Some minor algorithms which are included only as curiosities in the snowball
website, such as the Lovins stemmer and the Kraaij Pohlmann stemmer, are not
included in the standard libstemmer sources.  These are not really supported by
the snowball project, but it would be possible to compile a modified libstemmer
library containing these if desired.)


The stemwords example
=====================

The stemwords example program allows you to run any of the stemmers
compiled into the libstemmer library on a sample vocabulary.  For
details on how to use it, run it with the "-h" command line option.


Using the library in a larger system
====================================

If you are incorporating the library into the build system of a larger
program, I recommend copying the unpacked tarball without modification into
a subdirectory of the sources of your program.  Future versions of the
library are intended to keep the same structure, so this will keep the
work required to move to a new version of the library to a minimum.

As an additional convenience, the list of source and header files used
in the library is detailed in mkinc.mak - a file which is in a suitable
format for inclusion by a Makefile.  By including this file in your build
system, you can link the snowball system into your program with a few
extra rules.

Using the library in a system using GNU autotools
=================================================

The libstemmer_c library can be integrated into a larger system which uses the
GNU autotool framework (and in particular, automake and autoconf) as follows:

1) Unpack libstemmer_c.tgz in the top level project directory so that there is
   a libstemmer_c subdirectory of the top level directory of the project.

2) Add a file "Makefile.am" to the unpacked libstemmer_c folder, containing:
   
noinst_LTLIBRARIES = libstemmer.la
include $(srcdir)/mkinc.mak
noinst_HEADERS = $(snowball_headers)
libstemmer_la_SOURCES = $(snowball_sources) 

(You may also need to add other lines to this, for example, if you are using
compiler options which are not compatible with compiling the libstemmer
library.)

3) Add libstemmer_c to the AC_CONFIG_FILES declaration in the project's
   configure.ac file.

4) Add to the top level makefile the following lines (or modify existing
   assignments to these variables appropriately):

AUTOMAKE_OPTIONS = subdir-objects
AM_CPPFLAGS = -I$(top_srcdir)/libstemmer_c/include
SUBDIRS=libstemmer_c
<name>_LIBADD = libstemmer_c/libstemmer.la

(Where <name> is the name of the library or executable which links against
libstemmer.) 

# benchmark
[![Build Status](https://travis-ci.org/google/benchmark.svg?branch=master)](https://travis-ci.org/google/benchmark)
[![Build status](https://ci.appveyor.com/api/projects/status/u0qsyp7t1tk7cpxs/branch/master?svg=true)](https://ci.appveyor.com/project/google/benchmark/branch/master)
[![Coverage Status](https://coveralls.io/repos/google/benchmark/badge.svg)](https://coveralls.io/r/google/benchmark)
[![slackin](https://slackin-iqtfqnpzxd.now.sh/badge.svg)](https://slackin-iqtfqnpzxd.now.sh/)

A library to support the benchmarking of functions, similar to unit-tests.

Discussion group: https://groups.google.com/d/forum/benchmark-discuss

IRC channel: https://freenode.net #googlebenchmark

[Known issues and common problems](#known-issues)

[Additional Tooling Documentation](docs/tools.md)

[Assembly Testing Documentation](docs/AssemblyTests.md)


## Building

The basic steps for configuring and building the library look like this:

```bash
$ git clone https://github.com/google/benchmark.git
# Benchmark requires Google Test as a dependency. Add the source tree as a subdirectory.
$ git clone https://github.com/google/googletest.git benchmark/googletest
$ mkdir build && cd build
$ cmake -G <generator> [options] ../benchmark
# Assuming a makefile generator was used
$ make
```

Note that Google Benchmark requires Google Test to build and run the tests. This
dependency can be provided two ways:

* Checkout the Google Test sources into `benchmark/googletest` as above.
* Otherwise, if `-DBENCHMARK_DOWNLOAD_DEPENDENCIES=ON` is specified during
  configuration, the library will automatically download and build any required
  dependencies.

If you do not wish to build and run the tests, add `-DBENCHMARK_ENABLE_GTEST_TESTS=OFF`
to `CMAKE_ARGS`.


## Installation Guide

For Ubuntu and Debian Based System

First make sure you have git and cmake installed (If not please install it)

```
sudo apt-get install git
sudo apt-get install cmake
```

Now, let's clone the repository and build it

```
git clone https://github.com/google/benchmark.git
cd benchmark
git clone https://github.com/google/googletest.git
mkdir build
cd build
cmake .. -DCMAKE_BUILD_TYPE=RELEASE
make
```

We need to install the library globally now

```
sudo make install
```

Now you have google/benchmark installed in your machine
Note: Don't forget to link to pthread library while building

## Stable and Experimental Library Versions

The main branch contains the latest stable version of the benchmarking library;
the API of which can be considered largely stable, with source breaking changes
being made only upon the release of a new major version.

Newer, experimental, features are implemented and tested on the
[`v2` branch](https://github.com/google/benchmark/tree/v2). Users who wish
to use, test, and provide feedback on the new features are encouraged to try
this branch. However, this branch provides no stability guarantees and reserves
the right to change and break the API at any time.

##Prerequisite knowledge

Before attempting to understand this framework one should ideally have some familiarity with the structure and format of the Google Test framework, upon which it is based. Documentation for Google Test, including a "Getting Started" (primer) guide, is available here:
https://github.com/google/googletest/blob/master/googletest/docs/Documentation.md


## Example usage
### Basic usage
Define a function that executes the code to be measured.

```c++
#include <benchmark/benchmark.h>

static void BM_StringCreation(benchmark::State& state) {
  for (auto _ : state)
    std::string empty_string;
}
// Register the function as a benchmark
BENCHMARK(BM_StringCreation);

// Define another benchmark
static void BM_StringCopy(benchmark::State& state) {
  std::string x = "hello";
  for (auto _ : state)
    std::string copy(x);
}
BENCHMARK(BM_StringCopy);

BENCHMARK_MAIN();
```

Don't forget to inform your linker to add benchmark library e.g. through 
`-lbenchmark` compilation flag. Alternatively, you may leave out the 
`BENCHMARK_MAIN();` at the end of the source file and link against 
`-lbenchmark_main` to get the same default behavior.

The benchmark library will reporting the timing for the code within the `for(...)` loop.

### Passing arguments
Sometimes a family of benchmarks can be implemented with just one routine that
takes an extra argument to specify which one of the family of benchmarks to
run. For example, the following code defines a family of benchmarks for
measuring the speed of `memcpy()` calls of different lengths:

```c++
static void BM_memcpy(benchmark::State& state) {
  char* src = new char[state.range(0)];
  char* dst = new char[state.range(0)];
  memset(src, 'x', state.range(0));
  for (auto _ : state)
    memcpy(dst, src, state.range(0));
  state.SetBytesProcessed(int64_t(state.iterations()) *
                          int64_t(state.range(0)));
  delete[] src;
  delete[] dst;
}
BENCHMARK(BM_memcpy)->Arg(8)->Arg(64)->Arg(512)->Arg(1<<10)->Arg(8<<10);
```

The preceding code is quite repetitive, and can be replaced with the following
short-hand. The following invocation will pick a few appropriate arguments in
the specified range and will generate a benchmark for each such argument.

```c++
BENCHMARK(BM_memcpy)->Range(8, 8<<10);
```

By default the arguments in the range are generated in multiples of eight and
the command above selects [ 8, 64, 512, 4k, 8k ]. In the following code the
range multiplier is changed to multiples of two.

```c++
BENCHMARK(BM_memcpy)->RangeMultiplier(2)->Range(8, 8<<10);
```
Now arguments generated are [ 8, 16, 32, 64, 128, 256, 512, 1024, 2k, 4k, 8k ].

You might have a benchmark that depends on two or more inputs. For example, the
following code defines a family of benchmarks for measuring the speed of set
insertion.

```c++
static void BM_SetInsert(benchmark::State& state) {
  std::set<int> data;
  for (auto _ : state) {
    state.PauseTiming();
    data = ConstructRandomSet(state.range(0));
    state.ResumeTiming();
    for (int j = 0; j < state.range(1); ++j)
      data.insert(RandomNumber());
  }
}
BENCHMARK(BM_SetInsert)
    ->Args({1<<10, 128})
    ->Args({2<<10, 128})
    ->Args({4<<10, 128})
    ->Args({8<<10, 128})
    ->Args({1<<10, 512})
    ->Args({2<<10, 512})
    ->Args({4<<10, 512})
    ->Args({8<<10, 512});
```

The preceding code is quite repetitive, and can be replaced with the following
short-hand. The following macro will pick a few appropriate arguments in the
product of the two specified ranges and will generate a benchmark for each such
pair.

```c++
BENCHMARK(BM_SetInsert)->Ranges({{1<<10, 8<<10}, {128, 512}});
```

For more complex patterns of inputs, passing a custom function to `Apply` allows
programmatic specification of an arbitrary set of arguments on which to run the
benchmark. The following example enumerates a dense range on one parameter,
and a sparse range on the second.

```c++
static void CustomArguments(benchmark::internal::Benchmark* b) {
  for (int i = 0; i <= 10; ++i)
    for (int j = 32; j <= 1024*1024; j *= 8)
      b->Args({i, j});
}
BENCHMARK(BM_SetInsert)->Apply(CustomArguments);
```

### Calculate asymptotic complexity (Big O)
Asymptotic complexity might be calculated for a family of benchmarks. The
following code will calculate the coefficient for the high-order term in the
running time and the normalized root-mean square error of string comparison.

```c++
static void BM_StringCompare(benchmark::State& state) {
  std::string s1(state.range(0), '-');
  std::string s2(state.range(0), '-');
  for (auto _ : state) {
    benchmark::DoNotOptimize(s1.compare(s2));
  }
  state.SetComplexityN(state.range(0));
}
BENCHMARK(BM_StringCompare)
    ->RangeMultiplier(2)->Range(1<<10, 1<<18)->Complexity(benchmark::oN);
```

As shown in the following invocation, asymptotic complexity might also be
calculated automatically.

```c++
BENCHMARK(BM_StringCompare)
    ->RangeMultiplier(2)->Range(1<<10, 1<<18)->Complexity();
```

The following code will specify asymptotic complexity with a lambda function,
that might be used to customize high-order term calculation.

```c++
BENCHMARK(BM_StringCompare)->RangeMultiplier(2)
    ->Range(1<<10, 1<<18)->Complexity([](int n)->double{return n; });
```

### Templated benchmarks
Templated benchmarks work the same way: This example produces and consumes
messages of size `sizeof(v)` `range_x` times. It also outputs throughput in the
absence of multiprogramming.

```c++
template <class Q> int BM_Sequential(benchmark::State& state) {
  Q q;
  typename Q::value_type v;
  for (auto _ : state) {
    for (int i = state.range(0); i--; )
      q.push(v);
    for (int e = state.range(0); e--; )
      q.Wait(&v);
  }
  // actually messages, not bytes:
  state.SetBytesProcessed(
      static_cast<int64_t>(state.iterations())*state.range(0));
}
BENCHMARK_TEMPLATE(BM_Sequential, WaitQueue<int>)->Range(1<<0, 1<<10);
```

Three macros are provided for adding benchmark templates.

```c++
#ifdef BENCHMARK_HAS_CXX11
#define BENCHMARK_TEMPLATE(func, ...) // Takes any number of parameters.
#else // C++ < C++11
#define BENCHMARK_TEMPLATE(func, arg1)
#endif
#define BENCHMARK_TEMPLATE1(func, arg1)
#define BENCHMARK_TEMPLATE2(func, arg1, arg2)
```

### A Faster KeepRunning loop

In C++11 mode, a ranged-based for loop should be used in preference to
the `KeepRunning` loop for running the benchmarks. For example:

```c++
static void BM_Fast(benchmark::State &state) {
  for (auto _ : state) {
    FastOperation();
  }
}
BENCHMARK(BM_Fast);
```

The reason the ranged-for loop is faster than using `KeepRunning`, is
because `KeepRunning` requires a memory load and store of the iteration count
ever iteration, whereas the ranged-for variant is able to keep the iteration count
in a register.

For example, an empty inner loop of using the ranged-based for method looks like:

```asm
# Loop Init
  mov rbx, qword ptr [r14 + 104]
  call benchmark::State::StartKeepRunning()
  test rbx, rbx
  je .LoopEnd
.LoopHeader: # =>This Inner Loop Header: Depth=1
  add rbx, -1
  jne .LoopHeader
.LoopEnd:
```

Compared to an empty `KeepRunning` loop, which looks like:

```asm
.LoopHeader: # in Loop: Header=BB0_3 Depth=1
  cmp byte ptr [rbx], 1
  jne .LoopInit
.LoopBody: # =>This Inner Loop Header: Depth=1
  mov rax, qword ptr [rbx + 8]
  lea rcx, [rax + 1]
  mov qword ptr [rbx + 8], rcx
  cmp rax, qword ptr [rbx + 104]
  jb .LoopHeader
  jmp .LoopEnd
.LoopInit:
  mov rdi, rbx
  call benchmark::State::StartKeepRunning()
  jmp .LoopBody
.LoopEnd:
```

Unless C++03 compatibility is required, the ranged-for variant of writing
the benchmark loop should be preferred.  

## Passing arbitrary arguments to a benchmark
In C++11 it is possible to define a benchmark that takes an arbitrary number
of extra arguments. The `BENCHMARK_CAPTURE(func, test_case_name, ...args)`
macro creates a benchmark that invokes `func`  with the `benchmark::State` as
the first argument followed by the specified `args...`.
The `test_case_name` is appended to the name of the benchmark and
should describe the values passed.

```c++
template <class ...ExtraArgs>
void BM_takes_args(benchmark::State& state, ExtraArgs&&... extra_args) {
  [...]
}
// Registers a benchmark named "BM_takes_args/int_string_test" that passes
// the specified values to `extra_args`.
BENCHMARK_CAPTURE(BM_takes_args, int_string_test, 42, std::string("abc"));
```
Note that elements of `...args` may refer to global variables. Users should
avoid modifying global state inside of a benchmark.

## Using RegisterBenchmark(name, fn, args...)

The `RegisterBenchmark(name, func, args...)` function provides an alternative
way to create and register benchmarks.
`RegisterBenchmark(name, func, args...)` creates, registers, and returns a
pointer to a new benchmark with the specified `name` that invokes
`func(st, args...)` where `st` is a `benchmark::State` object.

Unlike the `BENCHMARK` registration macros, which can only be used at the global
scope, the `RegisterBenchmark` can be called anywhere. This allows for
benchmark tests to be registered programmatically.

Additionally `RegisterBenchmark` allows any callable object to be registered
as a benchmark. Including capturing lambdas and function objects.

For Example:
```c++
auto BM_test = [](benchmark::State& st, auto Inputs) { /* ... */ };

int main(int argc, char** argv) {
  for (auto& test_input : { /* ... */ })
      benchmark::RegisterBenchmark(test_input.name(), BM_test, test_input);
  benchmark::Initialize(&argc, argv);
  benchmark::RunSpecifiedBenchmarks();
}
```

### Multithreaded benchmarks
In a multithreaded test (benchmark invoked by multiple threads simultaneously),
it is guaranteed that none of the threads will start until all have reached
the start of the benchmark loop, and all will have finished before any thread
exits the benchmark loop. (This behavior is also provided by the `KeepRunning()`
API) As such, any global setup or teardown can be wrapped in a check against the thread
index:

```c++
static void BM_MultiThreaded(benchmark::State& state) {
  if (state.thread_index == 0) {
    // Setup code here.
  }
  for (auto _ : state) {
    // Run the test as normal.
  }
  if (state.thread_index == 0) {
    // Teardown code here.
  }
}
BENCHMARK(BM_MultiThreaded)->Threads(2);
```

If the benchmarked code itself uses threads and you want to compare it to
single-threaded code, you may want to use real-time ("wallclock") measurements
for latency comparisons:

```c++
BENCHMARK(BM_test)->Range(8, 8<<10)->UseRealTime();
```

Without `UseRealTime`, CPU time is used by default.


## Manual timing
For benchmarking something for which neither CPU time nor real-time are
correct or accurate enough, completely manual timing is supported using
the `UseManualTime` function.

When `UseManualTime` is used, the benchmarked code must call
`SetIterationTime` once per iteration of the benchmark loop to
report the manually measured time.

An example use case for this is benchmarking GPU execution (e.g. OpenCL
or CUDA kernels, OpenGL or Vulkan or Direct3D draw calls), which cannot
be accurately measured using CPU time or real-time. Instead, they can be
measured accurately using a dedicated API, and these measurement results
can be reported back with `SetIterationTime`.

```c++
static void BM_ManualTiming(benchmark::State& state) {
  int microseconds = state.range(0);
  std::chrono::duration<double, std::micro> sleep_duration {
    static_cast<double>(microseconds)
  };

  for (auto _ : state) {
    auto start = std::chrono::high_resolution_clock::now();
    // Simulate some useful workload with a sleep
    std::this_thread::sleep_for(sleep_duration);
    auto end   = std::chrono::high_resolution_clock::now();

    auto elapsed_seconds =
      std::chrono::duration_cast<std::chrono::duration<double>>(
        end - start);

    state.SetIterationTime(elapsed_seconds.count());
  }
}
BENCHMARK(BM_ManualTiming)->Range(1, 1<<17)->UseManualTime();
```

### Preventing optimisation
To prevent a value or expression from being optimized away by the compiler
the `benchmark::DoNotOptimize(...)` and `benchmark::ClobberMemory()`
functions can be used.

```c++
static void BM_test(benchmark::State& state) {
  for (auto _ : state) {
      int x = 0;
      for (int i=0; i < 64; ++i) {
        benchmark::DoNotOptimize(x += i);
      }
  }
}
```

`DoNotOptimize(<expr>)` forces the  *result* of `<expr>` to be stored in either
memory or a register. For GNU based compilers it acts as read/write barrier
for global memory. More specifically it forces the compiler to flush pending
writes to memory and reload any other values as necessary.

Note that `DoNotOptimize(<expr>)` does not prevent optimizations on `<expr>`
in any way. `<expr>` may even be removed entirely when the result is already
known. For example:

```c++
  /* Example 1: `<expr>` is removed entirely. */
  int foo(int x) { return x + 42; }
  while (...) DoNotOptimize(foo(0)); // Optimized to DoNotOptimize(42);

  /*  Example 2: Result of '<expr>' is only reused */
  int bar(int) __attribute__((const));
  while (...) DoNotOptimize(bar(0)); // Optimized to:
  // int __result__ = bar(0);
  // while (...) DoNotOptimize(__result__);
```

The second tool for preventing optimizations is `ClobberMemory()`. In essence
`ClobberMemory()` forces the compiler to perform all pending writes to global
memory. Memory managed by block scope objects must be "escaped" using
`DoNotOptimize(...)` before it can be clobbered. In the below example
`ClobberMemory()` prevents the call to `v.push_back(42)` from being optimized
away.

```c++
static void BM_vector_push_back(benchmark::State& state) {
  for (auto _ : state) {
    std::vector<int> v;
    v.reserve(1);
    benchmark::DoNotOptimize(v.data()); // Allow v.data() to be clobbered.
    v.push_back(42);
    benchmark::ClobberMemory(); // Force 42 to be written to memory.
  }
}
```

Note that `ClobberMemory()` is only available for GNU or MSVC based compilers.

### Set time unit manually
If a benchmark runs a few milliseconds it may be hard to visually compare the
measured times, since the output data is given in nanoseconds per default. In
order to manually set the time unit, you can specify it manually:

```c++
BENCHMARK(BM_test)->Unit(benchmark::kMillisecond);
```

## Controlling number of iterations
In all cases, the number of iterations for which the benchmark is run is
governed by the amount of time the benchmark takes. Concretely, the number of
iterations is at least one, not more than 1e9, until CPU time is greater than
the minimum time, or the wallclock time is 5x minimum time. The minimum time is
set as a flag `--benchmark_min_time` or per benchmark by calling `MinTime` on
the registered benchmark object.

## Reporting the mean, median and standard deviation by repeated benchmarks
By default each benchmark is run once and that single result is reported.
However benchmarks are often noisy and a single result may not be representative
of the overall behavior. For this reason it's possible to repeatedly rerun the
benchmark.

The number of runs of each benchmark is specified globally by the
`--benchmark_repetitions` flag or on a per benchmark basis by calling
`Repetitions` on the registered benchmark object. When a benchmark is run more
than once the mean, median and standard deviation of the runs will be reported.

Additionally the `--benchmark_report_aggregates_only={true|false}` flag or
`ReportAggregatesOnly(bool)` function can be used to change how repeated tests
are reported. By default the result of each repeated run is reported. When this
option is `true` only the mean, median and standard deviation of the runs is reported.
Calling `ReportAggregatesOnly(bool)` on a registered benchmark object overrides
the value of the flag for that benchmark.

## User-defined statistics for repeated benchmarks
While having mean, median and standard deviation is nice, this may not be
enough for everyone. For example you may want to know what is the largest
observation, e.g. because you have some real-time constraints. This is easy.
The following code will specify a custom statistic to be calculated, defined
by a lambda function.

```c++
void BM_spin_empty(benchmark::State& state) {
  for (auto _ : state) {
    for (int x = 0; x < state.range(0); ++x) {
      benchmark::DoNotOptimize(x);
    }
  }
}

BENCHMARK(BM_spin_empty)
  ->ComputeStatistics("max", [](const std::vector<double>& v) -> double {
    return *(std::max_element(std::begin(v), std::end(v)));
  })
  ->Arg(512);
```

## Fixtures
Fixture tests are created by
first defining a type that derives from `::benchmark::Fixture` and then
creating/registering the tests using the following macros:

* `BENCHMARK_F(ClassName, Method)`
* `BENCHMARK_DEFINE_F(ClassName, Method)`
* `BENCHMARK_REGISTER_F(ClassName, Method)`

For Example:

```c++
class MyFixture : public benchmark::Fixture {};

BENCHMARK_F(MyFixture, FooTest)(benchmark::State& st) {
   for (auto _ : st) {
     ...
  }
}

BENCHMARK_DEFINE_F(MyFixture, BarTest)(benchmark::State& st) {
   for (auto _ : st) {
     ...
  }
}
/* BarTest is NOT registered */
BENCHMARK_REGISTER_F(MyFixture, BarTest)->Threads(2);
/* BarTest is now registered */
```

### Templated fixtures
Also you can create templated fixture by using the following macros:

* `BENCHMARK_TEMPLATE_F(ClassName, Method, ...)`
* `BENCHMARK_TEMPLATE_DEFINE_F(ClassName, Method, ...)`

For example:
```c++
template<typename T>
class MyFixture : public benchmark::Fixture {};

BENCHMARK_TEMPLATE_F(MyFixture, IntTest, int)(benchmark::State& st) {
   for (auto _ : st) {
     ...
  }
}

BENCHMARK_TEMPLATE_DEFINE_F(MyFixture, DoubleTest, double)(benchmark::State& st) {
   for (auto _ : st) {
     ...
  }
}

BENCHMARK_REGISTER_F(MyFixture, DoubleTest)->Threads(2);
```

## User-defined counters

You can add your own counters with user-defined names. The example below
will add columns "Foo", "Bar" and "Baz" in its output:

```c++
static void UserCountersExample1(benchmark::State& state) {
  double numFoos = 0, numBars = 0, numBazs = 0;
  for (auto _ : state) {
    // ... count Foo,Bar,Baz events
  }
  state.counters["Foo"] = numFoos;
  state.counters["Bar"] = numBars;
  state.counters["Baz"] = numBazs;
}
```

The `state.counters` object is a `std::map` with `std::string` keys
and `Counter` values. The latter is a `double`-like class, via an implicit
conversion to `double&`. Thus you can use all of the standard arithmetic
assignment operators (`=,+=,-=,*=,/=`) to change the value of each counter.

In multithreaded benchmarks, each counter is set on the calling thread only.
When the benchmark finishes, the counters from each thread will be summed;
the resulting sum is the value which will be shown for the benchmark.

The `Counter` constructor accepts two parameters: the value as a `double`
and a bit flag which allows you to show counters as rates and/or as
per-thread averages:

```c++
  // sets a simple counter
  state.counters["Foo"] = numFoos;

  // Set the counter as a rate. It will be presented divided
  // by the duration of the benchmark.
  state.counters["FooRate"] = Counter(numFoos, benchmark::Counter::kIsRate);

  // Set the counter as a thread-average quantity. It will
  // be presented divided by the number of threads.
  state.counters["FooAvg"] = Counter(numFoos, benchmark::Counter::kAvgThreads);

  // There's also a combined flag:
  state.counters["FooAvgRate"] = Counter(numFoos,benchmark::Counter::kAvgThreadsRate);
```

When you're compiling in C++11 mode or later you can use `insert()` with
`std::initializer_list`:

```c++
  // With C++11, this can be done:
  state.counters.insert({{"Foo", numFoos}, {"Bar", numBars}, {"Baz", numBazs}});
  // ... instead of:
  state.counters["Foo"] = numFoos;
  state.counters["Bar"] = numBars;
  state.counters["Baz"] = numBazs;
```

### Counter reporting

When using the console reporter, by default, user counters are are printed at
the end after the table, the same way as ``bytes_processed`` and
``items_processed``. This is best for cases in which there are few counters,
or where there are only a couple of lines per benchmark. Here's an example of
the default output:

```
------------------------------------------------------------------------------
Benchmark                        Time           CPU Iterations UserCounters...
------------------------------------------------------------------------------
BM_UserCounter/threads:8      2248 ns      10277 ns      68808 Bar=16 Bat=40 Baz=24 Foo=8
BM_UserCounter/threads:1      9797 ns       9788 ns      71523 Bar=2 Bat=5 Baz=3 Foo=1024m
BM_UserCounter/threads:2      4924 ns       9842 ns      71036 Bar=4 Bat=10 Baz=6 Foo=2
BM_UserCounter/threads:4      2589 ns      10284 ns      68012 Bar=8 Bat=20 Baz=12 Foo=4
BM_UserCounter/threads:8      2212 ns      10287 ns      68040 Bar=16 Bat=40 Baz=24 Foo=8
BM_UserCounter/threads:16     1782 ns      10278 ns      68144 Bar=32 Bat=80 Baz=48 Foo=16
BM_UserCounter/threads:32     1291 ns      10296 ns      68256 Bar=64 Bat=160 Baz=96 Foo=32
BM_UserCounter/threads:4      2615 ns      10307 ns      68040 Bar=8 Bat=20 Baz=12 Foo=4
BM_Factorial                    26 ns         26 ns   26608979 40320
BM_Factorial/real_time          26 ns         26 ns   26587936 40320
BM_CalculatePiRange/1           16 ns         16 ns   45704255 0
BM_CalculatePiRange/8           73 ns         73 ns    9520927 3.28374
BM_CalculatePiRange/64         609 ns        609 ns    1140647 3.15746
BM_CalculatePiRange/512       4900 ns       4901 ns     142696 3.14355
```

If this doesn't suit you, you can print each counter as a table column by
passing the flag `--benchmark_counters_tabular=true` to the benchmark
application. This is best for cases in which there are a lot of counters, or
a lot of lines per individual benchmark. Note that this will trigger a
reprinting of the table header any time the counter set changes between
individual benchmarks. Here's an example of corresponding output when
`--benchmark_counters_tabular=true` is passed:

```
---------------------------------------------------------------------------------------
Benchmark                        Time           CPU Iterations    Bar   Bat   Baz   Foo
---------------------------------------------------------------------------------------
BM_UserCounter/threads:8      2198 ns       9953 ns      70688     16    40    24     8
BM_UserCounter/threads:1      9504 ns       9504 ns      73787      2     5     3     1
BM_UserCounter/threads:2      4775 ns       9550 ns      72606      4    10     6     2
BM_UserCounter/threads:4      2508 ns       9951 ns      70332      8    20    12     4
BM_UserCounter/threads:8      2055 ns       9933 ns      70344     16    40    24     8
BM_UserCounter/threads:16     1610 ns       9946 ns      70720     32    80    48    16
BM_UserCounter/threads:32     1192 ns       9948 ns      70496     64   160    96    32
BM_UserCounter/threads:4      2506 ns       9949 ns      70332      8    20    12     4
--------------------------------------------------------------
Benchmark                        Time           CPU Iterations
--------------------------------------------------------------
BM_Factorial                    26 ns         26 ns   26392245 40320
BM_Factorial/real_time          26 ns         26 ns   26494107 40320
BM_CalculatePiRange/1           15 ns         15 ns   45571597 0
BM_CalculatePiRange/8           74 ns         74 ns    9450212 3.28374
BM_CalculatePiRange/64         595 ns        595 ns    1173901 3.15746
BM_CalculatePiRange/512       4752 ns       4752 ns     147380 3.14355
BM_CalculatePiRange/4k       37970 ns      37972 ns      18453 3.14184
BM_CalculatePiRange/32k     303733 ns     303744 ns       2305 3.14162
BM_CalculatePiRange/256k   2434095 ns    2434186 ns        288 3.1416
BM_CalculatePiRange/1024k  9721140 ns    9721413 ns         71 3.14159
BM_CalculatePi/threads:8      2255 ns       9943 ns      70936
```
Note above the additional header printed when the benchmark changes from
``BM_UserCounter`` to ``BM_Factorial``. This is because ``BM_Factorial`` does
not have the same counter set as ``BM_UserCounter``.

## Exiting Benchmarks in Error

When errors caused by external influences, such as file I/O and network
communication, occur within a benchmark the
`State::SkipWithError(const char* msg)` function can be used to skip that run
of benchmark and report the error. Note that only future iterations of the
`KeepRunning()` are skipped. For the ranged-for version of the benchmark loop
Users must explicitly exit the loop, otherwise all iterations will be performed.
Users may explicitly return to exit the benchmark immediately.

The `SkipWithError(...)` function may be used at any point within the benchmark,
including before and after the benchmark loop.

For example:

```c++
static void BM_test(benchmark::State& state) {
  auto resource = GetResource();
  if (!resource.good()) {
      state.SkipWithError("Resource is not good!");
      // KeepRunning() loop will not be entered.
  }
  for (state.KeepRunning()) {
      auto data = resource.read_data();
      if (!resource.good()) {
        state.SkipWithError("Failed to read data!");
        break; // Needed to skip the rest of the iteration.
     }
     do_stuff(data);
  }
}

static void BM_test_ranged_fo(benchmark::State & state) {
  state.SkipWithError("test will not be entered");
  for (auto _ : state) {
    state.SkipWithError("Failed!");
    break; // REQUIRED to prevent all further iterations.
  }
}
```

## Running a subset of the benchmarks

The `--benchmark_filter=<regex>` option can be used to only run the benchmarks
which match the specified `<regex>`. For example:

```bash
$ ./run_benchmarks.x --benchmark_filter=BM_memcpy/32
Run on (1 X 2300 MHz CPU )
2016-06-25 19:34:24
Benchmark              Time           CPU Iterations
----------------------------------------------------
BM_memcpy/32          11 ns         11 ns   79545455
BM_memcpy/32k       2181 ns       2185 ns     324074
BM_memcpy/32          12 ns         12 ns   54687500
BM_memcpy/32k       1834 ns       1837 ns     357143
```


## Output Formats
The library supports multiple output formats. Use the
`--benchmark_format=<console|json|csv>` flag to set the format type. `console`
is the default format.

The Console format is intended to be a human readable format. By default
the format generates color output. Context is output on stderr and the
tabular data on stdout. Example tabular output looks like:
```
Benchmark                               Time(ns)    CPU(ns) Iterations
----------------------------------------------------------------------
BM_SetInsert/1024/1                        28928      29349      23853  133.097kB/s   33.2742k items/s
BM_SetInsert/1024/8                        32065      32913      21375  949.487kB/s   237.372k items/s
BM_SetInsert/1024/10                       33157      33648      21431  1.13369MB/s   290.225k items/s
```

The JSON format outputs human readable json split into two top level attributes.
The `context` attribute contains information about the run in general, including
information about the CPU and the date.
The `benchmarks` attribute contains a list of every benchmark run. Example json
output looks like:
```json
{
  "context": {
    "date": "2015/03/17-18:40:25",
    "num_cpus": 40,
    "mhz_per_cpu": 2801,
    "cpu_scaling_enabled": false,
    "build_type": "debug"
  },
  "benchmarks": [
    {
      "name": "BM_SetInsert/1024/1",
      "iterations": 94877,
      "real_time": 29275,
      "cpu_time": 29836,
      "bytes_per_second": 134066,
      "items_per_second": 33516
    },
    {
      "name": "BM_SetInsert/1024/8",
      "iterations": 21609,
      "real_time": 32317,
      "cpu_time": 32429,
      "bytes_per_second": 986770,
      "items_per_second": 246693
    },
    {
      "name": "BM_SetInsert/1024/10",
      "iterations": 21393,
      "real_time": 32724,
      "cpu_time": 33355,
      "bytes_per_second": 1199226,
      "items_per_second": 299807
    }
  ]
}
```

The CSV format outputs comma-separated values. The `context` is output on stderr
and the CSV itself on stdout. Example CSV output looks like:
```
name,iterations,real_time,cpu_time,bytes_per_second,items_per_second,label
"BM_SetInsert/1024/1",65465,17890.7,8407.45,475768,118942,
"BM_SetInsert/1024/8",116606,18810.1,9766.64,3.27646e+06,819115,
"BM_SetInsert/1024/10",106365,17238.4,8421.53,4.74973e+06,1.18743e+06,
```

## Output Files
The library supports writing the output of the benchmark to a file specified
by `--benchmark_out=<filename>`. The format of the output can be specified
using `--benchmark_out_format={json|console|csv}`. Specifying
`--benchmark_out` does not suppress the console output.

## Debug vs Release
By default, benchmark builds as a debug library. You will see a warning in the output when this is the case. To build it as a release library instead, use:

```
cmake -DCMAKE_BUILD_TYPE=Release
```

To enable link-time optimisation, use

```
cmake -DCMAKE_BUILD_TYPE=Release -DBENCHMARK_ENABLE_LTO=true
```

If you are using gcc, you might need to set `GCC_AR` and `GCC_RANLIB` cmake cache variables, if autodetection fails.
If you are using clang, you may need to set `LLVMAR_EXECUTABLE`, `LLVMNM_EXECUTABLE` and `LLVMRANLIB_EXECUTABLE` cmake cache variables.

## Linking against the library

When the library is built using GCC it is necessary to link with `-pthread`,
due to how GCC implements `std::thread`.

For GCC 4.x failing to link to pthreads will lead to runtime exceptions, not linker errors.
See [issue #67](https://github.com/google/benchmark/issues/67) for more details.

## Compiler Support

Google Benchmark uses C++11 when building the library. As such we require
a modern C++ toolchain, both compiler and standard library.

The following minimum versions are strongly recommended build the library:

* GCC 4.8
* Clang 3.4
* Visual Studio 2013
* Intel 2015 Update 1

Anything older *may* work.

Note: Using the library and its headers in C++03 is supported. C++11 is only
required to build the library.

## Disable CPU frequency scaling
If you see this error:
```
***WARNING*** CPU scaling is enabled, the benchmark real time measurements may be noisy and will incur extra overhead.
```
you might want to disable the CPU frequency scaling while running the benchmark:
```bash
sudo cpupower frequency-set --governor performance
./mybench
sudo cpupower frequency-set --governor powersave
```

# Known Issues

### Windows with CMake

* Users must manually link `shlwapi.lib`. Failure to do so may result
in unresolved symbols.

### Solaris

* Users must explicitly link with kstat library (-lkstat compilation flag).
<p align="center"><img src="https://raw.githubusercontent.com/facebook/zstd/dev/doc/images/zstd_logo86.png" alt="Zstandard"></p>

__Zstandard__, or `zstd` as short version, is a fast lossless compression algorithm,
targeting real-time compression scenarios at zlib-level and better compression ratios.
It's backed by a very fast entropy stage, provided by [Huff0 and FSE library](https://github.com/Cyan4973/FiniteStateEntropy).

The project is provided as an open-source dual [BSD](LICENSE) and [GPLv2](COPYING) licensed **C** library,
and a command line utility producing and decoding `.zst`, `.gz`, `.xz` and `.lz4` files.
Should your project require another programming language,
a list of known ports and bindings is provided on [Zstandard homepage](http://www.zstd.net/#other-languages).

Development branch status : [![Build Status][travisDevBadge]][travisLink]   [![Build status][AppveyorDevBadge]][AppveyorLink]   [![Build status][CircleDevBadge]][CircleLink]

[travisDevBadge]: https://travis-ci.org/facebook/zstd.svg?branch=dev "Continuous Integration test suite"
[travisLink]: https://travis-ci.org/facebook/zstd
[AppveyorDevBadge]: https://ci.appveyor.com/api/projects/status/xt38wbdxjk5mrbem/branch/dev?svg=true "Windows test suite"
[AppveyorLink]: https://ci.appveyor.com/project/YannCollet/zstd-p0yf0
[CircleDevBadge]: https://circleci.com/gh/facebook/zstd/tree/dev.svg?style=shield "Short test suite"
[CircleLink]: https://circleci.com/gh/facebook/zstd

### Benchmarks

For reference, several fast compression algorithms were tested and compared
on a server running Linux Debian (`Linux version 4.14.0-3-amd64`),
with a Core i7-6700K CPU @ 4.0GHz,
using [lzbench], an open-source in-memory benchmark by @inikep
compiled with [gcc] 7.3.0,
on the [Silesia compression corpus].

[lzbench]: https://github.com/inikep/lzbench
[Silesia compression corpus]: http://sun.aei.polsl.pl/~sdeor/index.php?page=silesia
[gcc]: https://gcc.gnu.org/

| Compressor name         | Ratio | Compression| Decompress.|
| ---------------         | ------| -----------| ---------- |
| **zstd 1.3.4 -1**       | 2.877 |   470 MB/s |  1380 MB/s |
| zlib 1.2.11 -1          | 2.743 |   110 MB/s |   400 MB/s |
| brotli 1.0.2 -0         | 2.701 |   410 MB/s |   430 MB/s |
| quicklz 1.5.0 -1        | 2.238 |   550 MB/s |   710 MB/s |
| lzo1x 2.09 -1           | 2.108 |   650 MB/s |   830 MB/s |
| lz4 1.8.1               | 2.101 |   750 MB/s |  3700 MB/s |
| snappy 1.1.4            | 2.091 |   530 MB/s |  1800 MB/s |
| lzf 3.6 -1              | 2.077 |   400 MB/s |   860 MB/s |

[zlib]:http://www.zlib.net/
[LZ4]: http://www.lz4.org/

Zstd can also offer stronger compression ratios at the cost of compression speed.
Speed vs Compression trade-off is configurable by small increments.
Decompression speed is preserved and remains roughly the same at all settings,
a property shared by most LZ compression algorithms, such as [zlib] or lzma.

The following tests were run
on a server running Linux Debian (`Linux version 4.14.0-3-amd64`)
with a Core i7-6700K CPU @ 4.0GHz,
using [lzbench], an open-source in-memory benchmark by @inikep
compiled with [gcc] 7.3.0,
on the [Silesia compression corpus].

Compression Speed vs Ratio | Decompression Speed
---------------------------|--------------------
![Compression Speed vs Ratio](doc/images/CSpeed2.png "Compression Speed vs Ratio") | ![Decompression Speed](doc/images/DSpeed3.png "Decompression Speed")

A few other algorithms can produce higher compression ratios at slower speeds, falling outside of the graph.
For a larger picture including slow modes, [click on this link](doc/images/DCspeed5.png).


### The case for Small Data compression

Previous charts provide results applicable to typical file and stream scenarios (several MB). Small data comes with different perspectives.

The smaller the amount of data to compress, the more difficult it is to compress. This problem is common to all compression algorithms, and reason is, compression algorithms learn from past data how to compress future data. But at the beginning of a new data set, there is no "past" to build upon.

To solve this situation, Zstd offers a __training mode__, which can be used to tune the algorithm for a selected type of data.
Training Zstandard is achieved by providing it with a few samples (one file per sample). The result of this training is stored in a file called "dictionary", which must be loaded before compression and decompression.
Using this dictionary, the compression ratio achievable on small data improves dramatically.

The following example uses the `github-users` [sample set](https://github.com/facebook/zstd/releases/tag/v1.1.3), created from [github public API](https://developer.github.com/v3/users/#get-all-users).
It consists of roughly 10K records weighing about 1KB each.

Compression Ratio | Compression Speed | Decompression Speed
------------------|-------------------|--------------------
![Compression Ratio](doc/images/dict-cr.png "Compression Ratio") | ![Compression Speed](doc/images/dict-cs.png "Compression Speed") | ![Decompression Speed](doc/images/dict-ds.png "Decompression Speed")


These compression gains are achieved while simultaneously providing _faster_ compression and decompression speeds.

Training works if there is some correlation in a family of small data samples. The more data-specific a dictionary is, the more efficient it is (there is no _universal dictionary_).
Hence, deploying one dictionary per type of data will provide the greatest benefits.
Dictionary gains are mostly effective in the first few KB. Then, the compression algorithm will gradually use previously decoded content to better compress the rest of the file.

#### Dictionary compression How To:

1) Create the dictionary

`zstd --train FullPathToTrainingSet/* -o dictionaryName`

2) Compress with dictionary

`zstd -D dictionaryName FILE`

3) Decompress with dictionary

`zstd -D dictionaryName --decompress FILE.zst`


### Build instructions

#### Makefile

If your system is compatible with standard `make` (or `gmake`),
invoking `make` in root directory will generate `zstd` cli in root directory.

Other available options include:
- `make install` : create and install zstd cli, library and man pages
- `make check` : create and run `zstd`, tests its behavior on local platform

#### cmake

A `cmake` project generator is provided within `build/cmake`.
It can generate Makefiles or other build scripts
to create `zstd` binary, and `libzstd` dynamic and static libraries.

By default, `CMAKE_BUILD_TYPE` is set to `Release`.

#### Meson

A Meson project is provided within `contrib/meson`.

#### Visual Studio (Windows)

Going into `build` directory, you will find additional possibilities:
- Projects for Visual Studio 2005, 2008 and 2010.
  + VS2010 project is compatible with VS2012, VS2013, VS2015 and VS2017.
- Automated build scripts for Visual compiler by [@KrzysFR](https://github.com/KrzysFR), in `build/VS_scripts`,
  which will build `zstd` cli and `libzstd` library without any need to open Visual Studio solution.


### Status

Zstandard is currently deployed within Facebook. It is used continuously to compress large amounts of data in multiple formats and use cases.
Zstandard is considered safe for production environments.

### License

Zstandard is dual-licensed under [BSD](LICENSE) and [GPLv2](COPYING).

### Contributing

The "dev" branch is the one where all contributions are merged before reaching "master".
If you plan to propose a patch, please commit into the "dev" branch, or its own feature branch.
Direct commit to "master" are not permitted.
For more information, please read [CONTRIBUTING](CONTRIBUTING.md).
Zstandard library : usage examples
==================================

- [Simple compression](simple_compression.c) :
  Compress a single file.
  Introduces usage of : `ZSTD_compress()`

- [Simple decompression](simple_decompression.c) :
  Decompress a single file.
  Only compatible with simple compression.
  Result remains in memory.
  Introduces usage of : `ZSTD_decompress()`

- [Streaming memory usage](streaming_memory_usage.c) :
  Provides amount of memory used by streaming context
  Introduces usage of : `ZSTD_sizeof_CStream()`

- [Streaming compression](streaming_compression.c) :
  Compress a single file.
  Introduces usage of : `ZSTD_compressStream()`

- [Multiple Streaming compression](multiple_streaming_compression.c) :
  Compress multiple files in a single command line.
  Introduces memory usage preservation technique,
  reducing impact of malloc()/free() and memset() by re-using existing resources.

- [Streaming decompression](streaming_decompression.c) :
  Decompress a single file compressed by zstd.
  Compatible with both simple and streaming compression.
  Result is sent to stdout.
  Introduces usage of : `ZSTD_decompressStream()`

- [Dictionary compression](dictionary_compression.c) :
  Compress multiple files using the same dictionary.
  Introduces usage of : `ZSTD_createCDict()` and `ZSTD_compress_usingCDict()`

- [Dictionary decompression](dictionary_decompression.c) :
  Decompress multiple files using the same dictionary.
  Result remains in memory.
  Introduces usage of : `ZSTD_createDDict()` and `ZSTD_decompress_usingDDict()`
Command Line Interface for Zstandard library
============================================

Command Line Interface (CLI) can be created using the `make` command without any additional parameters.
There are however other Makefile targets that create different variations of CLI:
- `zstd` : default CLI supporting gzip-like arguments; includes dictionary builder, benchmark, and support for decompression of legacy zstd formats
- `zstd_nolegacy` : Same as `zstd` but without support for legacy zstd formats
- `zstd-small` : CLI optimized for minimal size; no dictionary builder, no benchmark, and no support for legacy zstd formats
- `zstd-compress` : version of CLI which can only compress into zstd format
- `zstd-decompress` : version of CLI which can only decompress zstd format


#### Compilation variables
`zstd` scope can be altered by modifying the following `make` variables :

- __HAVE_THREAD__ : multithreading is automatically enabled when `pthread` is detected.
  It's possible to disable multithread support, by setting `HAVE_THREAD=0`.
  Example : `make zstd HAVE_THREAD=0`
  It's also possible to force multithread support, using `HAVE_THREAD=1`.
  In which case, linking stage will fail if neither `pthread` nor `windows.h` library can be found.
  This is useful to ensure this feature is not silently disabled.

- __ZSTD_LEGACY_SUPPORT__ : `zstd` can decompress files compressed by older versions of `zstd`.
  Starting v0.8.0, all versions of `zstd` produce frames compliant with the [specification](../doc/zstd_compression_format.md), and are therefore compatible.
  But older versions (< v0.8.0) produced different, incompatible, frames.
  By default, `zstd` supports decoding legacy formats >= v0.4.0 (`ZSTD_LEGACY_SUPPORT=4`).
  This can be altered by modifying this compilation variable.
  `ZSTD_LEGACY_SUPPORT=1` means "support all formats >= v0.1.0".
  `ZSTD_LEGACY_SUPPORT=2` means "support all formats >= v0.2.0", and so on.
  `ZSTD_LEGACY_SUPPORT=0` means _DO NOT_ support any legacy format.
  if `ZSTD_LEGACY_SUPPORT >= 8`, it's the same as `0`, since there is no legacy format after `7`.
  Note : `zstd` only supports decoding older formats, and cannot generate any legacy format.

- __HAVE_ZLIB__ : `zstd` can compress and decompress files in `.gz` format.
  This is ordered through command `--format=gzip`.
  Alternatively, symlinks named `gzip` or `gunzip` will mimic intended behavior.
  `.gz` support is automatically enabled when `zlib` library is detected at build time.
  It's possible to disable `.gz` support, by setting `HAVE_ZLIB=0`.
  Example : `make zstd HAVE_ZLIB=0`
  It's also possible to force compilation with zlib support, `using HAVE_ZLIB=1`.
  In which case, linking stage will fail if `zlib` library cannot be found.
  This is useful to prevent silent feature disabling.

- __HAVE_LZMA__ : `zstd` can compress and decompress files in `.xz` and `.lzma` formats.
  This is ordered through commands `--format=xz` and `--format=lzma` respectively.
  Alternatively, symlinks named `xz`, `unxz`, `lzma`, or `unlzma` will mimic intended behavior.
  `.xz` and `.lzma` support is automatically enabled when `lzma` library is detected at build time.
  It's possible to disable `.xz` and `.lzma` support, by setting `HAVE_LZMA=0` .
  Example : `make zstd HAVE_LZMA=0`
  It's also possible to force compilation with lzma support, using `HAVE_LZMA=1`.
  In which case, linking stage will fail if `lzma` library cannot be found.
  This is useful to prevent silent feature disabling.

- __HAVE_LZ4__ : `zstd` can compress and decompress files in `.lz4` formats.
  This is ordered through commands `--format=lz4`.
  Alternatively, symlinks named `lz4`, or `unlz4` will mimic intended behavior.
  `.lz4` support is automatically enabled when `lz4` library is detected at build time.
  It's possible to disable `.lz4` support, by setting `HAVE_LZ4=0` .
  Example : `make zstd HAVE_LZ4=0`
  It's also possible to force compilation with lz4 support, using `HAVE_LZ4=1`.
  In which case, linking stage will fail if `lz4` library cannot be found.
  This is useful to prevent silent feature disabling.

- __BACKTRACE__ : `zstd` can display a stack backtrace when execution
  generates a runtime exception. By default, this feature may be
  degraded/disabled on some platforms unless additional compiler directives are
  applied. When triaging a runtime issue, enabling this feature can provide
  more context to determine the location of the fault.
  Example : `make zstd BACKTRACE=1`


#### Aggregation of parameters
CLI supports aggregation of parameters i.e. `-b1`, `-e18`, and `-i1` can be joined into `-b1e18i1`.


#### Symlink shortcuts
It's possible to invoke `zstd` through a symlink.
When the name of the symlink has a specific value, it triggers an associated behavior.
- `zstdmt` : compress using all cores available on local system.
- `zcat` : will decompress and output target file using any of the supported formats. `gzcat` and `zstdcat` are also equivalent.
- `gzip` : if zlib support is enabled, will mimic `gzip` by compressing file using `.gz` format, removing source file by default (use `--keep` to preserve). If zlib is not supported, triggers an error.
- `xz` : if lzma support is enabled, will mimic `xz` by compressing file using `.xz` format, removing source file by default (use `--keep` to preserve). If xz is not supported, triggers an error.
- `lzma` : if lzma support is enabled, will mimic `lzma` by compressing file using `.lzma` format, removing source file by default (use `--keep` to preserve). If lzma is not supported, triggers an error.
- `lz4` : if lz4 support is enabled, will mimic `lz4` by compressing file using `.lz4` format. If lz4 is not supported, triggers an error.
- `unzstd` and `unlz4` will decompress any of the supported format.
- `ungz`, `unxz` and `unlzma` will do the same, and will also remove source file by default (use `--keep` to preserve).


#### Dictionary builder in Command Line Interface
Zstd offers a training mode, which can be used to tune the algorithm for a selected
type of data, by providing it with a few samples. The result of the training is stored
in a file selected with the `-o` option (default name is `dictionary`),
which can be loaded before compression and decompression.

Using a dictionary, the compression ratio achievable on small data improves dramatically.
These compression gains are achieved while simultaneously providing faster compression and decompression speeds.
Dictionary work if there is some correlation in a family of small data (there is no universal dictionary).
Hence, deploying one dictionary per type of data will provide the greater benefits.
Dictionary gains are mostly effective in the first few KB. Then, the compression algorithm
will rely more and more on previously decoded content to compress the rest of the file.

Usage of the dictionary builder and created dictionaries with CLI:

1. Create the dictionary : `zstd --train PathToTrainingSet/* -o dictionaryName`
2. Compress with the dictionary: `zstd FILE -D dictionaryName`
3. Decompress with the dictionary: `zstd --decompress FILE.zst -D dictionaryName`


#### Benchmark in Command Line Interface
CLI includes in-memory compression benchmark module for zstd.
The benchmark is conducted using given filenames. The files are read into memory and joined together.
It makes benchmark more precise as it eliminates I/O overhead.
Multiple filenames can be supplied, as multiple parameters, with wildcards,
or names of directories can be used as parameters with `-r` option.

The benchmark measures ratio, compressed size, compression and decompression speed.
One can select compression levels starting from `-b` and ending with `-e`.
The `-i` parameter selects minimal time used for each of tested levels.


#### Usage of Command Line Interface
The full list of options can be obtained with `-h` or `-H` parameter:
```
Usage :
      zstd [args] [FILE(s)] [-o file]

FILE    : a filename
          with no FILE, or when FILE is - , read standard input
Arguments :
 -#     : # compression level (1-19, default: 3)
 -d     : decompression
 -D file: use `file` as Dictionary
 -o file: result stored into `file` (only if 1 input file)
 -f     : overwrite output without prompting and (de)compress links
--rm    : remove source file(s) after successful de/compression
 -k     : preserve source file(s) (default)
 -h/-H  : display help/long help and exit

Advanced arguments :
 -V     : display Version number and exit
 -v     : verbose mode; specify multiple times to increase verbosity
 -q     : suppress warnings; specify twice to suppress errors too
 -c     : force write to standard output, even if it is the console
 -l     : print information about zstd compressed files
--ultra : enable levels beyond 19, up to 22 (requires more memory)
--long  : enable long distance matching (requires more memory)
--no-dictID : don't write dictID into header (dictionary compression)
--[no-]check : integrity check (default: enabled)
 -r     : operate recursively on directories
--format=gzip : compress files to the .gz format
--format=xz : compress files to the .xz format
--format=lzma : compress files to the .lzma format
--test  : test compressed file integrity
--[no-]sparse : sparse mode (default: disabled)
 -M#    : Set a memory usage limit for decompression
--      : All arguments after "--" are treated as files

Dictionary builder :
--train ## : create a dictionary from a training set of files
--train-cover[=k=#,d=#,steps=#,split=#] : use the cover algorithm with optional args
--train-fastcover[=k=#,d=#,f=#,steps=#,split=#,accel=#] : use the fastcover algorithm with optional args
--train-legacy[=s=#] : use the legacy algorithm with selectivity (default: 9)
 -o file : `file` is dictionary name (default: dictionary)
--maxdict=# : limit dictionary to specified size (default: 112640)
--dictID=# : force dictionary ID to specified value (default: random)

Benchmark arguments :
 -b#    : benchmark file(s), using # compression level (default: 3)
 -e#    : test all compression levels from -bX to # (default: 1)
 -i#    : minimum evaluation time in seconds (default: 3s)
 -B#    : cut file into independent blocks of size # (default: no block)
--priority=rt : set process priority to real-time
```


#### Long distance matching mode
The long distance matching mode, enabled with `--long`, is designed to improve
the compression ratio for files with long matches at a large distance (up to the
maximum window size, `128 MiB`) while still maintaining compression speed.

Enabling this mode sets the window size to `128 MiB` and thus increases the memory
usage for both the compressor and decompressor. Performance in terms of speed is
dependent on long matches being found. Compression speed may degrade if few long
matches are found. Decompression speed usually improves when there are many long
distance matches.

Below are graphs comparing the compression speed, compression ratio, and
decompression speed with and without long distance matching on an ideal use
case: a tar of four versions of clang (versions `3.4.1`, `3.4.2`, `3.5.0`,
`3.5.1`) with a total size of `244889600 B`. This is an ideal use case as there
are many long distance matches within the maximum window size of `128 MiB` (each
version is less than `128 MiB`).

Compression Speed vs Ratio | Decompression Speed
---------------------------|---------------------
![Compression Speed vs Ratio](https://raw.githubusercontent.com/facebook/zstd/v1.3.3/doc/images/ldmCspeed.png "Compression Speed vs Ratio") | ![Decompression Speed](https://raw.githubusercontent.com/facebook/zstd/v1.3.3/doc/images/ldmDspeed.png "Decompression Speed")

| Method | Compression ratio | Compression speed | Decompression speed  |
|:-------|------------------:|-------------------------:|---------------------------:|
| `zstd -1`   | `5.065`   | `284.8 MB/s`  | `759.3 MB/s`  |
| `zstd -5`  | `5.826`    | `124.9 MB/s`  | `674.0 MB/s`  |
| `zstd -10` | `6.504`    | `29.5 MB/s`   | `771.3 MB/s`  |
| `zstd -1 --long` | `17.426` | `220.6 MB/s` | `1638.4 MB/s` |
| `zstd -5 --long` | `19.661` | `165.5 MB/s` | `1530.6 MB/s`|
| `zstd -10 --long`| `21.949` | `75.6 MB/s` | `1632.6 MB/s`|

On this file, the compression ratio improves significantly with minimal impact
on compression speed, and the decompression speed doubles.

On the other extreme, compressing a file with few long distance matches (such as
the [Silesia compression corpus]) will likely lead to a deterioration in
compression speed (for lower levels) with minimal change in compression ratio.

The below table illustrates this on the [Silesia compression corpus].

[Silesia compression corpus]: http://sun.aei.polsl.pl/~sdeor/index.php?page=silesia

| Method | Compression ratio | Compression speed | Decompression speed  |
|:-------|------------------:|------------------:|---------------------:|
| `zstd -1`        | `2.878` | `231.7 MB/s`      | `594.4 MB/s`   |
| `zstd -1 --long` | `2.929` | `106.5 MB/s`      | `517.9 MB/s`   |
| `zstd -5`        | `3.274` | `77.1 MB/s`       | `464.2 MB/s`   |
| `zstd -5 --long` | `3.319` | `51.7 MB/s`       | `371.9 MB/s`   |
| `zstd -10`       | `3.523` | `16.4 MB/s`       | `489.2 MB/s`   |
| `zstd -10 --long`| `3.566` | `16.2 MB/s`       | `415.7 MB/s`   |


#### zstdgrep

`zstdgrep` is a utility which makes it possible to `grep` directly a `.zst` compressed file.
It's used the same way as normal `grep`, for example :
`zstdgrep pattern file.zst`

`zstdgrep` is _not_ compatible with dictionary compression.

To search into a file compressed with a dictionary,
it's necessary to decompress it using `zstd` or `zstdcat`,
and then pipe the result to `grep`. For example  :
`zstdcat -D dictionary -qc -- file.zst | grep pattern`
Zstandard library files
================================

The __lib__ directory is split into several sub-directories,
in order to make it easier to select or exclude features.


#### Building

`Makefile` script is provided, supporting all standard [Makefile conventions](https://www.gnu.org/prep/standards/html_node/Makefile-Conventions.html#Makefile-Conventions),
including commands variables, staged install, directory variables and standard targets.
- `make` : generates both static and dynamic libraries
- `make install` : install libraries in default system directories

`libzstd` default scope includes compression, decompression, dictionary building,
and decoding support for legacy formats >= v0.5.0.


#### API

Zstandard's stable API is exposed within [lib/zstd.h](zstd.h).


#### Advanced API

Optional advanced features are exposed via :

- `lib/common/zstd_errors.h` : translates `size_t` function results
                              into an `ZSTD_ErrorCode`, for accurate error handling.
- `ZSTD_STATIC_LINKING_ONLY` : if this macro is defined _before_ including `zstd.h`,
                          it unlocks access to advanced experimental API,
                          exposed in second part of `zstd.h`.
                          These APIs are not "stable", their definition may change in the future.
                          As a consequence, it shall ___never be used with dynamic library___ !
                          Only static linking is allowed.


#### Modular build

It's possible to compile only a limited set of features.

- Directory `lib/common` is always required, for all variants.
- Compression source code lies in `lib/compress`
- Decompression source code lies in `lib/decompress`
- It's possible to include only `compress` or only `decompress`, they don't depend on each other.
- `lib/dictBuilder` : makes it possible to generate dictionaries from a set of samples.
        The API is exposed in `lib/dictBuilder/zdict.h`.
        This module depends on both `lib/common` and `lib/compress` .
- `lib/legacy` : source code to decompress legacy zstd formats, starting from `v0.1.0`.
        This module depends on `lib/common` and `lib/decompress`.
        To enable this feature, define `ZSTD_LEGACY_SUPPORT` during compilation.
        Specifying a number limits versions supported to that version onward.
        For example, `ZSTD_LEGACY_SUPPORT=2` means : "support legacy formats >= v0.2.0".
        `ZSTD_LEGACY_SUPPORT=3` means : "support legacy formats >= v0.3.0", and so on.
        Currently, the default library setting is `ZST_LEGACY_SUPPORT=5`.
        It can be changed at build by any other value.
        Note that any number >= 8 translates into "do __not__ support legacy formats",
        since all versions of `zstd` >= v0.8 are compatible with v1+ specification.
        `ZSTD_LEGACY_SUPPORT=0` also means "do __not__ support legacy formats".
        Once enabled, this capability is transparently triggered within decompression functions.
        It's also possible to invoke directly legacy API, as exposed in `lib/legacy/zstd_legacy.h`.
        Each version also provides an additional dedicated set of advanced API.
        For example, advanced API for version `v0.4` is exposed in `lib/legacy/zstd_v04.h` .
        Note : `lib/legacy` only supports _decoding_ legacy formats.
- Similarly, you can define `ZSTD_LIB_COMPRESSION, ZSTD_LIB_DECOMPRESSION`, `ZSTD_LIB_DICTBUILDER`,
        and `ZSTD_LIB_DEPRECATED` as 0 to forgo compilation of the corresponding features. This will
        also disable compilation of all dependencies (eg. `ZSTD_LIB_COMPRESSION=0` will also disable
        dictBuilder).


#### Multithreading support

Multithreading is disabled by default when building with `make`.
Enabling multithreading requires 2 conditions :
- set macro `ZSTD_MULTITHREAD`
- on POSIX systems : compile with pthread (`-pthread` compilation flag for `gcc`)

Both conditions are automatically triggered by invoking `make lib-mt` target.
Note that, when linking a POSIX program with a multithreaded version of `libzstd`,
it's necessary to trigger `-pthread` flag during link stage.

Multithreading capabilities are exposed
via [advanced API `ZSTD_compress_generic()` defined in `lib/zstd.h`](https://github.com/facebook/zstd/blob/dev/lib/zstd.h#L919).
This API is still considered experimental,
but is expected to become "stable" at some point in the future.


#### Windows : using MinGW+MSYS to create DLL

DLL can be created using MinGW+MSYS with the `make libzstd` command.
This command creates `dll\libzstd.dll` and the import library `dll\libzstd.lib`.
The import library is only required with Visual C++.
The header file `zstd.h` and the dynamic library `dll\libzstd.dll` are required to
compile a project using gcc/MinGW.
The dynamic library has to be added to linking options.
It means that if a project that uses ZSTD consists of a single `test-dll.c`
file it should be linked with `dll\libzstd.dll`. For example:
```
    gcc $(CFLAGS) -Iinclude/ test-dll.c -o test-dll dll\libzstd.dll
```
The compiled executable will require ZSTD DLL which is available at `dll\libzstd.dll`.


#### Deprecated API

Obsolete API on their way out are stored in directory `lib/deprecated`.
At this stage, it contains older streaming prototypes, in `lib/deprecated/zbuff.h`.
These prototypes will be removed in some future version.
Consider migrating code towards supported streaming API exposed in `zstd.h`.


#### Miscellaneous

The other files are not source code. There are :

 - `LICENSE` : contains the BSD license text
 - `Makefile` : `make` script to build and install zstd library (static and dynamic)
 - `BUCK` : support for `buck` build system (https://buckbuild.com/)
 - `libzstd.pc.in` : for `pkg-config` (used in `make install`)
 - `README.md` : this file
ZSTD Windows binary package
====================================

#### The package contents

- `zstd.exe`                  : Command Line Utility, supporting gzip-like arguments
- `dll\libzstd.dll`           : The ZSTD dynamic library (DLL)
- `dll\libzstd.lib`           : The import library of the ZSTD dynamic library (DLL) for Visual C++
- `example\`                  : The example of usage of the ZSTD library
- `include\`                  : Header files required by the ZSTD library
- `static\libzstd_static.lib` : The static ZSTD library (LIB)


#### Usage of Command Line Interface

Command Line Interface (CLI) supports gzip-like arguments.
By default CLI takes an input file and compresses it to an output file:
```
    Usage: zstd [arg] [input] [output]
```
The full list of commands for CLI can be obtained with `-h` or `-H`. The ratio can
be improved with commands from `-3` to `-16` but higher levels also have slower
compression. CLI includes in-memory compression benchmark module with compression
levels starting from `-b` and ending with `-e` with iteration time of `-i` seconds.
CLI supports aggregation of parameters i.e. `-b1`, `-e18`, and `-i1` can be joined
into `-b1e18i1`.


#### The example of usage of static and dynamic ZSTD libraries with gcc/MinGW

Use `cd example` and `make` to build `fullbench-dll` and `fullbench-lib`.
`fullbench-dll` uses a dynamic ZSTD library from the `dll` directory.
`fullbench-lib` uses a static ZSTD library from the `lib` directory.


#### Using ZSTD DLL with gcc/MinGW

The header files from `include\` and the dynamic library `dll\libzstd.dll`
are required to compile a project using gcc/MinGW.
The dynamic library has to be added to linking options.
It means that if a project that uses ZSTD consists of a single `test-dll.c`
file it should be linked with `dll\libzstd.dll`. For example:
```
    gcc $(CFLAGS) -Iinclude\ test-dll.c -o test-dll dll\libzstd.dll
```
The compiled executable will require ZSTD DLL which is available at `dll\libzstd.dll`.


#### The example of usage of static and dynamic ZSTD libraries with Visual C++

Open `example\fullbench-dll.sln` to compile `fullbench-dll` that uses a
dynamic ZSTD library from the `dll` directory. The solution works with Visual C++
2010 or newer. When one will open the solution with Visual C++ newer than 2010
then the solution will upgraded to the current version.


#### Using ZSTD DLL with Visual C++

The header files from `include\` and the import library `dll\libzstd.lib`
are required to compile a project using Visual C++.

1. The path to header files should be added to `Additional Include Directories` that can
   be found in project properties `C/C++` then `General`.
2. The import library has to be added to `Additional Dependencies` that can
   be found in project properties `Linker` then `Input`.
   If one will provide only the name `libzstd.lib` without a full path to the library
   the directory has to be added to `Linker\General\Additional Library Directories`.

The compiled executable will require ZSTD DLL which is available at `dll\libzstd.dll`.
### Summary

`adapt` is a new compression tool targeted at optimizing performance across network connections and pipelines. The tool is aimed at sensing network speeds and adapting compression level based on network or pipe speeds.
In situations where the compression level does not appropriately match the network/pipe speed, compression may be bottlenecking the entire pipeline or the files may not be compressed as much as they potentially could be, therefore losing efficiency. It also becomes quite impractical to manually measure and set an optimalcompression level (which could potentially change over time). 

### Using `adapt`

In order to build and use the tool, you can simply run `make adapt` in the `adaptive-compression` directory under `contrib`. This will generate an executable available for use. Another possible method of installation is running `make install`, which will create and install the binary as the command `zstd-adaptive`.

Similar to many other compression utilities, `zstd-adaptive` can be invoked by using the following format:

`zstd-adaptive [options] [file(s)]`

Supported options for the above format are described below. 

`zstd-adaptive` also supports reading from `stdin` and writing to `stdout`, which is potentially more useful. By default, if no files are given, `zstd-adaptive` reads from and writes to standard I/O. Therefore, you can simply insert it within a pipeline like so:

`cat FILE | zstd-adaptive | ssh "cat - > tmp.zst"`

If a file is provided, it is also possible to force writing to stdout using the `-c` flag like so:

`zstd-adaptive -c FILE | ssh "cat - > tmp.zst"`

Several options described below can be used to control the behavior of `zstd-adaptive`. More specifically, using the `-l#` and `-u#` flags will will set upper and lower bounds so that the compression level will always be within that range. The `-i#` flag can also be used to change the initial compression level. If an initial compression level is not provided, the initial compression level will be chosen such that it is within the appropriate range (it becomes equal to the lower bound). 

### Options
`-oFILE` : write output to `FILE`

`-i#`    : provide initial compression level (must within the appropriate bounds)

`-h`     : display help/information

`-f`     : force the compression level to stay constant

`-c`     : force write to `stdout`

`-p`     : hide progress bar

`-q`     : quiet mode -- do not show progress bar or other information

`-l#`    : set a lower bound on the compression level (default is 1)

`-u#`    : set an upper bound on the compression level (default is 22)
### Benchmarking / Test results
#### Artificial Tests
These artificial tests were run by using the `pv` command line utility in order to limit pipe speeds (25 MB/s read and 5 MB/s write limits were chosen to mimic severe throughput constraints). A 40 GB backup file was sent through a pipeline, compressed, and written out to a file. Compression time, size, and ratio were computed. Data for `zstd -15` was excluded from these tests because the test runs quite long.

<table>
<tr><th> 25 MB/s read limit </th></tr>
<tr><td>

| Compressor Name | Ratio | Compressed Size | Compression Time |
|:----------------|------:|----------------:|-----------------:| 
| zstd -3         | 2.108 |       20.718 GB |      29m 48.530s |
| zstd-adaptive   | 2.230 |       19.581 GB |      29m 48.798s |

</td><tr>
</table>

<table>
<tr><th> 5 MB/s write limit </th></tr>
<tr><td>

| Compressor Name | Ratio | Compressed Size | Compression Time |
|:----------------|------:|----------------:|-----------------:| 
| zstd -3         | 2.108 |       20.718 GB |   1h 10m 43.076s |
| zstd-adaptive   | 2.249 |       19.412 GB |   1h 06m 15.577s |

</td></tr>
</table>

The commands used for this test generally followed the form:

`cat FILE | pv -L 25m -q | COMPRESSION | pv -q > tmp.zst # impose 25 MB/s read limit`

`cat FILE | pv -q | COMPRESSION | pv -L 5m -q > tmp.zst  # impose 5 MB/s write limit`

#### SSH Tests

The following tests were performed by piping a relatively large backup file (approximately 80 GB) through compression and over SSH to be stored on a server. The test data includes statistics for time and compressed size  on `zstd` at several compression levels, as well as `zstd-adaptive`. The data highlights the potential advantages that `zstd-adaptive` has over using a low static compression level and the negative imapcts that using an excessively high static compression level can have on
pipe throughput.

| Compressor Name | Ratio | Compressed Size | Compression Time |
|:----------------|------:|----------------:|-----------------:|
| zstd -3         | 2.212 |       32.426 GB |   1h 17m 59.756s |
| zstd -15        | 2.374 |       30.213 GB |   2h 56m 59.441s |
| zstd-adaptive   | 2.315 |       30.993 GB |   1h 18m 52.860s |

The commands used for this test generally followed the form: 

`cat FILE | COMPRESSION | ssh dev "cat - > tmp.zst"`
## Project Support Notice

The VS2005 Project directory has been moved to the contrib directory in order to indicate that it will no longer be supported.
largeNbDicts
=====================

`largeNbDicts` is a benchmark test tool
dedicated to the specific scenario of
dictionary decompression using a very large number of dictionaries.
When dictionaries are constantly changing, they are always "cold",
suffering from increased latency due to cache misses.

The tool is created in a bid to investigate performance for this scenario,
and experiment mitigation techniques.

Command line :
```
largeNbDicts [Options] filename(s)

Options :
-r           : recursively load all files in subdirectories (default: off)
-B#          : split input into blocks of size # (default: no split)
-#           : use compression level # (default: 3)
-D #         : use # as a dictionary (default: create one)
-i#          : nb benchmark rounds (default: 6)
--nbDicts=#  : set nb of dictionaries to # (default: one per block)
-h           : help (this text)
```
# Parallel Zstandard (PZstandard)

Parallel Zstandard is a Pigz-like tool for Zstandard.
It provides Zstandard format compatible compression and decompression that is able to utilize multiple cores.
It breaks the input up into equal sized chunks and compresses each chunk independently into a Zstandard frame.
It then concatenates the frames together to produce the final compressed output.
Pzstandard will write a 12 byte header for each frame that is a skippable frame in the Zstandard format, which tells PZstandard the size of the next compressed frame.
PZstandard supports parallel decompression of files compressed with PZstandard.
When decompressing files compressed with Zstandard, PZstandard does IO in one thread, and decompression in another.

## Usage

PZstandard supports the same command line interface as Zstandard, but also provides the `-p` option to specify the number of threads.
Dictionary mode is not currently supported.

Basic usage

    pzstd input-file -o output-file -p num-threads -#          # Compression
    pzstd -d input-file -o output-file -p num-threads          # Decompression

PZstandard also supports piping and fifo pipes

    cat input-file | pzstd -p num-threads -# -c > /dev/null

For more options

    pzstd --help

PZstandard tries to pick a smart default number of threads if not specified (displayed in `pzstd --help`).
If this number is not suitable, during compilation you can define `PZSTD_NUM_THREADS` to the number of threads you prefer.

## Benchmarks

As a reference, PZstandard and Pigz were compared on an Intel Core i7 @ 3.1 GHz, each using 4 threads, with the [Silesia compression corpus](http://sun.aei.polsl.pl/~sdeor/index.php?page=silesia).

Compression Speed vs Ratio with 4 Threads | Decompression Speed with 4 Threads
------------------------------------------|-----------------------------------
![Compression Speed vs Ratio](images/Cspeed.png "Compression Speed vs Ratio") | ![Decompression Speed](images/Dspeed.png "Decompression Speed")

The test procedure was to run each of the following commands 2 times for each compression level, and take the minimum time.

    time pzstd -# -p 4    -c silesia.tar     > silesia.tar.zst
    time pzstd -d -p 4    -c silesia.tar.zst > /dev/null

    time pigz  -# -p 4 -k -c silesia.tar     > silesia.tar.gz
    time pigz  -d -p 4 -k -c silesia.tar.gz  > /dev/null

PZstandard was tested using compression levels 1-19, and Pigz was tested using compression levels 1-9.
Pigz cannot do parallel decompression, it simply does each of reading, decompression, and writing on separate threads.

## Tests

Tests require that you have [gtest](https://github.com/google/googletest) installed.
Set `GTEST_INC` and `GTEST_LIB` in `Makefile` to specify the location of the gtest headers and libraries.
Alternatively, run `make googletest`, which will clone googletest and build it.
Run `make tests && make check` to run tests.
Random Dictionary Builder

### Permitted Arguments:
Input File/Directory (in=fileName): required; file/directory used to build dictionary; if directory, will operate recursively for files inside directory; can include multiple files/directories, each following "in="
Output Dictionary (out=dictName): if not provided, default to defaultDict
Dictionary ID (dictID=#): nonnegative number; if not provided, default to 0
Maximum Dictionary Size (maxdict=#): positive number; in bytes, if not provided, default to 110KB
Size of Randomly Selected Segment (k=#): positive number; in bytes; if not provided, default to 200

###Running Test:
make test


###Usage:
To build a random dictionary with the provided arguments: make ARG= followed by arguments


### Examples:
make ARG="in=../../../lib/dictBuilder out=dict100 dictID=520"
make ARG="in=../../../lib/dictBuilder in=../../../lib/compress"
FastCover Dictionary Builder

### Permitted Arguments:
Input File/Directory (in=fileName): required; file/directory used to build dictionary; if directory, will operate recursively for files inside directory; can include multiple files/directories, each following "in="
Output Dictionary (out=dictName): if not provided, default to fastCoverDict
Dictionary ID (dictID=#): nonnegative number; if not provided, default to 0
Maximum Dictionary Size (maxdict=#): positive number; in bytes, if not provided, default to 110KB
Size of Selected Segment (k=#): positive number; in bytes; if not provided, default to 200
Size of Dmer (d=#): either 6 or 8; if not provided, default to 8
Number of steps (steps=#): positive number, if not provided, default to 32
Percentage of samples used for training(split=#): positive number; if not provided, default to 100


###Running Test:
make test


###Usage:
To build a FASTCOVER dictionary with the provided arguments: make ARG= followed by arguments
If k or d is not provided, the optimize version of FASTCOVER is run.

### Examples:
make ARG="in=../../../lib/dictBuilder out=dict100 dictID=520"
make ARG="in=../../../lib/dictBuilder in=../../../lib/compress"
Benchmarking Dictionary Builder

### Permitted Argument:
Input File/Directory (in=fileName): required; file/directory used to build dictionary; if directory, will operate recursively for files inside directory; can include multiple files/directories, each following "in="

###Running Test:
make test

###Usage:
Benchmark given input files: make ARG= followed by permitted arguments

### Examples:
make ARG="in=../../../lib/dictBuilder in=../../../lib/compress"

###Benchmarking Result:
- First Cover is optimize cover, second Cover uses optimized d and k from first one.
- For every f value of fastCover, the first one is optimize fastCover and the second one uses optimized d and k from first one. This is run for accel values from 1 to 10.
- Fourth column is chosen d and fifth column is chosen k

github:
NODICT       0.000004       2.999642        
RANDOM       0.024560       8.791189        
LEGACY       0.727109       8.173529        
COVER       40.565676       10.652243        8          1298
COVER       3.608284       10.652243        8          1298
FAST f=15 a=1       4.181024       10.570882        8          1154
FAST f=15 a=1       0.040788       10.570882        8          1154
FAST f=15 a=2       3.548352       10.574287        6          1970
FAST f=15 a=2       0.035535       10.574287        6          1970
FAST f=15 a=3       3.287364       10.613950        6          1010
FAST f=15 a=3       0.032182       10.613950        6          1010
FAST f=15 a=4       3.184976       10.573883        6          1058
FAST f=15 a=4       0.029878       10.573883        6          1058
FAST f=15 a=5       3.045513       10.580640        8          1154
FAST f=15 a=5       0.022162       10.580640        8          1154
FAST f=15 a=6       3.003296       10.583677        6          1010
FAST f=15 a=6       0.028091       10.583677        6          1010
FAST f=15 a=7       2.952655       10.622551        6          1106
FAST f=15 a=7       0.02724       10.622551        6          1106
FAST f=15 a=8       2.945674       10.614657        6          1010
FAST f=15 a=8       0.027264       10.614657        6          1010
FAST f=15 a=9       3.153439       10.564018        8          1154
FAST f=15 a=9       0.020635       10.564018        8          1154
FAST f=15 a=10       2.950416       10.511454        6          1010
FAST f=15 a=10       0.026606       10.511454        6          1010
FAST f=16 a=1       3.970029       10.681035        8          1154
FAST f=16 a=1       0.038188       10.681035        8          1154
FAST f=16 a=2       3.422892       10.484978        6          1874
FAST f=16 a=2       0.034702       10.484978        6          1874
FAST f=16 a=3       3.215836       10.632631        8          1154
FAST f=16 a=3       0.026084       10.632631        8          1154
FAST f=16 a=4       3.081353       10.626533        6          1106
FAST f=16 a=4       0.030032       10.626533        6          1106
FAST f=16 a=5       3.041241       10.545027        8          1922
FAST f=16 a=5       0.022882       10.545027        8          1922
FAST f=16 a=6       2.989390       10.638284        6          1874
FAST f=16 a=6       0.028308       10.638284        6          1874
FAST f=16 a=7       3.001581       10.797136        6          1106
FAST f=16 a=7       0.027479       10.797136        6          1106
FAST f=16 a=8       2.984107       10.658356        8          1058
FAST f=16 a=8       0.021099       10.658356        8          1058
FAST f=16 a=9       2.925788       10.523869        6          1010
FAST f=16 a=9       0.026905       10.523869        6          1010
FAST f=16 a=10       2.889605       10.745841        6          1874
FAST f=16 a=10       0.026846       10.745841        6          1874
FAST f=17 a=1       4.031953       10.672080        8          1202
FAST f=17 a=1       0.040658       10.672080        8          1202
FAST f=17 a=2       3.458107       10.589352        8          1106
FAST f=17 a=2       0.02926       10.589352        8          1106
FAST f=17 a=3       3.291189       10.662714        8          1154
FAST f=17 a=3       0.026531       10.662714        8          1154
FAST f=17 a=4       3.154950       10.549456        8          1346
FAST f=17 a=4       0.024991       10.549456        8          1346
FAST f=17 a=5       3.092271       10.541670        6          1202
FAST f=17 a=5       0.038285       10.541670        6          1202
FAST f=17 a=6       3.166146       10.729112        6          1874
FAST f=17 a=6       0.038217       10.729112        6          1874
FAST f=17 a=7       3.035467       10.810485        6          1106
FAST f=17 a=7       0.036655       10.810485        6          1106
FAST f=17 a=8       3.035668       10.530532        6          1058
FAST f=17 a=8       0.037715       10.530532        6          1058
FAST f=17 a=9       2.987917       10.589802        8          1922
FAST f=17 a=9       0.02217       10.589802        8          1922
FAST f=17 a=10       2.981647       10.722579        8          1106
FAST f=17 a=10       0.021948       10.722579        8          1106
FAST f=18 a=1       4.067144       10.634943        8          1154
FAST f=18 a=1       0.041386       10.634943        8          1154
FAST f=18 a=2       3.507377       10.546230        6          1970
FAST f=18 a=2       0.037572       10.546230        6          1970
FAST f=18 a=3       3.323015       10.648061        8          1154
FAST f=18 a=3       0.028306       10.648061        8          1154
FAST f=18 a=4       3.216735       10.705402        6          1010
FAST f=18 a=4       0.030755       10.705402        6          1010
FAST f=18 a=5       3.175794       10.588154        8          1874
FAST f=18 a=5       0.025315       10.588154        8          1874
FAST f=18 a=6       3.127459       10.751104        8          1106
FAST f=18 a=6       0.023897       10.751104        8          1106
FAST f=18 a=7       3.083017       10.780402        6          1106
FAST f=18 a=7       0.029158       10.780402        6          1106
FAST f=18 a=8       3.069700       10.547226        8          1346
FAST f=18 a=8       0.024046       10.547226        8          1346
FAST f=18 a=9       3.056591       10.674759        6          1010
FAST f=18 a=9       0.028496       10.674759        6          1010
FAST f=18 a=10       3.063588       10.737578        8          1106
FAST f=18 a=10       0.023033       10.737578        8          1106
FAST f=19 a=1       4.164041       10.650333        8          1154
FAST f=19 a=1       0.042906       10.650333        8          1154
FAST f=19 a=2       3.585409       10.577066        6          1058
FAST f=19 a=2       0.038994       10.577066        6          1058
FAST f=19 a=3       3.439643       10.639403        8          1154
FAST f=19 a=3       0.028427       10.639403        8          1154
FAST f=19 a=4       3.268869       10.554410        8          1298
FAST f=19 a=4       0.026866       10.554410        8          1298
FAST f=19 a=5       3.238225       10.615109        6          1010
FAST f=19 a=5       0.03078       10.615109        6          1010
FAST f=19 a=6       3.199558       10.609782        6          1874
FAST f=19 a=6       0.030099       10.609782        6          1874
FAST f=19 a=7       3.132395       10.794753        6          1106
FAST f=19 a=7       0.028964       10.794753        6          1106
FAST f=19 a=8       3.148446       10.554842        8          1298
FAST f=19 a=8       0.024277       10.554842        8          1298
FAST f=19 a=9       3.108324       10.668763        6          1010
FAST f=19 a=9       0.02896       10.668763        6          1010
FAST f=19 a=10       3.159863       10.757347        8          1106
FAST f=19 a=10       0.023351       10.757347        8          1106
FAST f=20 a=1       4.462698       10.661788        8          1154
FAST f=20 a=1       0.047174       10.661788        8          1154
FAST f=20 a=2       3.820269       10.678612        6          1106
FAST f=20 a=2       0.040807       10.678612        6          1106
FAST f=20 a=3       3.644955       10.648424        8          1154
FAST f=20 a=3       0.031398       10.648424        8          1154
FAST f=20 a=4       3.546257       10.559756        8          1298
FAST f=20 a=4       0.029856       10.559756        8          1298
FAST f=20 a=5       3.485248       10.646637        6          1010
FAST f=20 a=5       0.033756       10.646637        6          1010
FAST f=20 a=6       3.490438       10.775824        8          1106
FAST f=20 a=6       0.028338       10.775824        8          1106
FAST f=20 a=7       3.631289       10.801795        6          1106
FAST f=20 a=7       0.035228       10.801795        6          1106
FAST f=20 a=8       3.758936       10.545116        8          1346
FAST f=20 a=8       0.027495       10.545116        8          1346
FAST f=20 a=9       3.707024       10.677454        6          1010
FAST f=20 a=9       0.031326       10.677454        6          1010
FAST f=20 a=10       3.586593       10.756017        8          1106
FAST f=20 a=10       0.027122       10.756017        8          1106
FAST f=21 a=1       5.701396       10.655398        8          1154
FAST f=21 a=1       0.067744       10.655398        8          1154
FAST f=21 a=2       5.270542       10.650743        6          1106
FAST f=21 a=2       0.052999       10.650743        6          1106
FAST f=21 a=3       4.945294       10.652380        8          1154
FAST f=21 a=3       0.052678       10.652380        8          1154
FAST f=21 a=4       4.894079       10.543185        8          1298
FAST f=21 a=4       0.04997       10.543185        8          1298
FAST f=21 a=5       4.785417       10.630321        6          1010
FAST f=21 a=5       0.045294       10.630321        6          1010
FAST f=21 a=6       4.789381       10.664477        6          1874
FAST f=21 a=6       0.046578       10.664477        6          1874
FAST f=21 a=7       4.302955       10.805179        6          1106
FAST f=21 a=7       0.041205       10.805179        6          1106
FAST f=21 a=8       4.034630       10.551211        8          1298
FAST f=21 a=8       0.040121       10.551211        8          1298
FAST f=21 a=9       4.523868       10.799114        6          1010
FAST f=21 a=9       0.043592       10.799114        6          1010
FAST f=21 a=10       4.760736       10.750255        8          1106
FAST f=21 a=10       0.043483       10.750255        8          1106
FAST f=22 a=1       6.743064       10.640537        8          1154
FAST f=22 a=1       0.086967       10.640537        8          1154
FAST f=22 a=2       6.121739       10.626638        6          1970
FAST f=22 a=2       0.066337       10.626638        6          1970
FAST f=22 a=3       5.248851       10.640688        8          1154
FAST f=22 a=3       0.054935       10.640688        8          1154
FAST f=22 a=4       5.436579       10.588333        8          1298
FAST f=22 a=4       0.064113       10.588333        8          1298
FAST f=22 a=5       5.812815       10.652653        6          1010
FAST f=22 a=5       0.058189       10.652653        6          1010
FAST f=22 a=6       5.745472       10.666437        6          1874
FAST f=22 a=6       0.057188       10.666437        6          1874
FAST f=22 a=7       5.716393       10.806911        6          1106
FAST f=22 a=7       0.056       10.806911        6          1106
FAST f=22 a=8       5.698799       10.530784        8          1298
FAST f=22 a=8       0.0583       10.530784        8          1298
FAST f=22 a=9       5.710533       10.777391        6          1010
FAST f=22 a=9       0.054945       10.777391        6          1010
FAST f=22 a=10       5.685395       10.745023        8          1106
FAST f=22 a=10       0.056526       10.745023        8          1106
FAST f=23 a=1       7.836923       10.638828        8          1154
FAST f=23 a=1       0.099522       10.638828        8          1154
FAST f=23 a=2       6.627834       10.631061        6          1970
FAST f=23 a=2       0.066769       10.631061        6          1970
FAST f=23 a=3       5.602533       10.647288        8          1154
FAST f=23 a=3       0.064513       10.647288        8          1154
FAST f=23 a=4       6.005580       10.568747        8          1298
FAST f=23 a=4       0.062022       10.568747        8          1298
FAST f=23 a=5       5.481816       10.676921        6          1010
FAST f=23 a=5       0.058959       10.676921        6          1010
FAST f=23 a=6       5.460444       10.666194        6          1874
FAST f=23 a=6       0.057687       10.666194        6          1874
FAST f=23 a=7       5.659822       10.800377        6          1106
FAST f=23 a=7       0.06783       10.800377        6          1106
FAST f=23 a=8       6.826940       10.522167        8          1298
FAST f=23 a=8       0.070533       10.522167        8          1298
FAST f=23 a=9       6.804757       10.577799        8          1682
FAST f=23 a=9       0.069949       10.577799        8          1682
FAST f=23 a=10       6.774933       10.742093        8          1106
FAST f=23 a=10       0.068395       10.742093        8          1106
FAST f=24 a=1       8.444110       10.632783        8          1154
FAST f=24 a=1       0.094357       10.632783        8          1154
FAST f=24 a=2       7.289578       10.631061        6          1970
FAST f=24 a=2       0.098515       10.631061        6          1970
FAST f=24 a=3       8.619780       10.646289        8          1154
FAST f=24 a=3       0.098041       10.646289        8          1154
FAST f=24 a=4       8.508455       10.555199        8          1298
FAST f=24 a=4       0.093885       10.555199        8          1298
FAST f=24 a=5       8.471145       10.674363        6          1010
FAST f=24 a=5       0.088676       10.674363        6          1010
FAST f=24 a=6       8.426727       10.667228        6          1874
FAST f=24 a=6       0.087247       10.667228        6          1874
FAST f=24 a=7       8.356826       10.803027        6          1106
FAST f=24 a=7       0.085835       10.803027        6          1106
FAST f=24 a=8       6.756811       10.522049        8          1298
FAST f=24 a=8       0.07107       10.522049        8          1298
FAST f=24 a=9       6.548169       10.571882        8          1682
FAST f=24 a=9       0.0713       10.571882        8          1682
FAST f=24 a=10       8.238079       10.736453        8          1106
FAST f=24 a=10       0.07004       10.736453        8          1106


hg-commands:
NODICT       0.000005       2.425276        
RANDOM       0.046332       3.490331        
LEGACY       0.720351       3.911682        
COVER       45.507731       4.132653        8          386
COVER       1.868810       4.132653        8          386
FAST f=15 a=1       4.561427       3.866894        8          1202
FAST f=15 a=1       0.048946       3.866894        8          1202
FAST f=15 a=2       3.574462       3.892119        8          1538
FAST f=15 a=2       0.033677       3.892119        8          1538
FAST f=15 a=3       3.230227       3.888791        6          1346
FAST f=15 a=3       0.034312       3.888791        6          1346
FAST f=15 a=4       3.042388       3.899739        8          1010
FAST f=15 a=4       0.024307       3.899739        8          1010
FAST f=15 a=5       2.800148       3.896220        8          818
FAST f=15 a=5       0.022331       3.896220        8          818
FAST f=15 a=6       2.706518       3.882039        8          578
FAST f=15 a=6       0.020955       3.882039        8          578
FAST f=15 a=7       2.701820       3.885430        6          866
FAST f=15 a=7       0.026074       3.885430        6          866
FAST f=15 a=8       2.604445       3.906932        8          1826
FAST f=15 a=8       0.021789       3.906932        8          1826
FAST f=15 a=9       2.598568       3.870324        6          1682
FAST f=15 a=9       0.026004       3.870324        6          1682
FAST f=15 a=10       2.575920       3.920783        8          1442
FAST f=15 a=10       0.020228       3.920783        8          1442
FAST f=16 a=1       4.630623       4.001430        8          770
FAST f=16 a=1       0.047497       4.001430        8          770
FAST f=16 a=2       3.674721       3.974431        8          1874
FAST f=16 a=2       0.035761       3.974431        8          1874
FAST f=16 a=3       3.338384       3.978703        8          1010
FAST f=16 a=3       0.029436       3.978703        8          1010
FAST f=16 a=4       3.004412       3.983035        8          1010
FAST f=16 a=4       0.025744       3.983035        8          1010
FAST f=16 a=5       2.881892       3.987710        8          770
FAST f=16 a=5       0.023211       3.987710        8          770
FAST f=16 a=6       2.807410       3.952717        8          1298
FAST f=16 a=6       0.023199       3.952717        8          1298
FAST f=16 a=7       2.819623       3.994627        8          770
FAST f=16 a=7       0.021806       3.994627        8          770
FAST f=16 a=8       2.740092       3.954032        8          1826
FAST f=16 a=8       0.0226       3.954032        8          1826
FAST f=16 a=9       2.682564       3.969879        6          1442
FAST f=16 a=9       0.026324       3.969879        6          1442
FAST f=16 a=10       2.657959       3.969755        8          674
FAST f=16 a=10       0.020413       3.969755        8          674
FAST f=17 a=1       4.729228       4.046000        8          530
FAST f=17 a=1       0.049703       4.046000        8          530
FAST f=17 a=2       3.764510       3.991519        8          1970
FAST f=17 a=2       0.038195       3.991519        8          1970
FAST f=17 a=3       3.416992       4.006296        6          914
FAST f=17 a=3       0.036244       4.006296        6          914
FAST f=17 a=4       3.145626       3.979182        8          1970
FAST f=17 a=4       0.028676       3.979182        8          1970
FAST f=17 a=5       2.995070       4.050070        8          770
FAST f=17 a=5       0.025707       4.050070        8          770
FAST f=17 a=6       2.911833       4.040024        8          770
FAST f=17 a=6       0.02453       4.040024        8          770
FAST f=17 a=7       2.894796       4.015884        8          818
FAST f=17 a=7       0.023956       4.015884        8          818
FAST f=17 a=8       2.789962       4.039303        8          530
FAST f=17 a=8       0.023219       4.039303        8          530
FAST f=17 a=9       2.787625       3.996762        8          1634
FAST f=17 a=9       0.023651       3.996762        8          1634
FAST f=17 a=10       2.754796       4.005059        8          1058
FAST f=17 a=10       0.022537       4.005059        8          1058
FAST f=18 a=1       4.779117       4.038214        8          242
FAST f=18 a=1       0.048814       4.038214        8          242
FAST f=18 a=2       3.829753       4.045768        8          722
FAST f=18 a=2       0.036541       4.045768        8          722
FAST f=18 a=3       3.495053       4.021497        8          770
FAST f=18 a=3       0.032648       4.021497        8          770
FAST f=18 a=4       3.221395       4.039623        8          770
FAST f=18 a=4       0.027818       4.039623        8          770
FAST f=18 a=5       3.059369       4.050414        8          530
FAST f=18 a=5       0.026296       4.050414        8          530
FAST f=18 a=6       3.019292       4.010714        6          962
FAST f=18 a=6       0.031104       4.010714        6          962
FAST f=18 a=7       2.949322       4.031439        6          770
FAST f=18 a=7       0.030745       4.031439        6          770
FAST f=18 a=8       2.876425       4.032088        6          386
FAST f=18 a=8       0.027407       4.032088        6          386
FAST f=18 a=9       2.850958       4.053372        8          674
FAST f=18 a=9       0.023799       4.053372        8          674
FAST f=18 a=10       2.884352       4.020148        8          1730
FAST f=18 a=10       0.024401       4.020148        8          1730
FAST f=19 a=1       4.815669       4.061203        8          674
FAST f=19 a=1       0.051425       4.061203        8          674
FAST f=19 a=2       3.951356       4.013822        8          1442
FAST f=19 a=2       0.039968       4.013822        8          1442
FAST f=19 a=3       3.554682       4.050425        8          722
FAST f=19 a=3       0.032725       4.050425        8          722
FAST f=19 a=4       3.242585       4.054677        8          722
FAST f=19 a=4       0.028194       4.054677        8          722
FAST f=19 a=5       3.105909       4.064524        8          818
FAST f=19 a=5       0.02675       4.064524        8          818
FAST f=19 a=6       3.059901       4.036857        8          1250
FAST f=19 a=6       0.026396       4.036857        8          1250
FAST f=19 a=7       3.016151       4.068234        6          770
FAST f=19 a=7       0.031501       4.068234        6          770
FAST f=19 a=8       2.962902       4.077509        8          530
FAST f=19 a=8       0.023333       4.077509        8          530
FAST f=19 a=9       2.899607       4.067328        8          530
FAST f=19 a=9       0.024553       4.067328        8          530
FAST f=19 a=10       2.950978       4.059901        8          434
FAST f=19 a=10       0.023852       4.059901        8          434
FAST f=20 a=1       5.259834       4.027579        8          1634
FAST f=20 a=1       0.061123       4.027579        8          1634
FAST f=20 a=2       4.382150       4.025093        8          1634
FAST f=20 a=2       0.048009       4.025093        8          1634
FAST f=20 a=3       4.104323       4.060842        8          530
FAST f=20 a=3       0.040965       4.060842        8          530
FAST f=20 a=4       3.853340       4.023504        6          914
FAST f=20 a=4       0.041072       4.023504        6          914
FAST f=20 a=5       3.728841       4.018089        6          1634
FAST f=20 a=5       0.037469       4.018089        6          1634
FAST f=20 a=6       3.683045       4.069138        8          578
FAST f=20 a=6       0.028011       4.069138        8          578
FAST f=20 a=7       3.726973       4.063160        8          722
FAST f=20 a=7       0.028437       4.063160        8          722
FAST f=20 a=8       3.555073       4.057690        8          386
FAST f=20 a=8       0.027588       4.057690        8          386
FAST f=20 a=9       3.551095       4.067253        8          482
FAST f=20 a=9       0.025976       4.067253        8          482
FAST f=20 a=10       3.490127       4.068518        8          530
FAST f=20 a=10       0.025971       4.068518        8          530
FAST f=21 a=1       7.343816       4.064945        8          770
FAST f=21 a=1       0.085035       4.064945        8          770
FAST f=21 a=2       5.930894       4.048206        8          386
FAST f=21 a=2       0.067349       4.048206        8          386
FAST f=21 a=3       6.770775       4.063417        8          578
FAST f=21 a=3       0.077104       4.063417        8          578
FAST f=21 a=4       6.889409       4.066761        8          626
FAST f=21 a=4       0.0717       4.066761        8          626
FAST f=21 a=5       6.714896       4.051813        8          914
FAST f=21 a=5       0.071026       4.051813        8          914
FAST f=21 a=6       6.539890       4.047263        8          1922
FAST f=21 a=6       0.07127       4.047263        8          1922
FAST f=21 a=7       6.511052       4.068373        8          482
FAST f=21 a=7       0.065467       4.068373        8          482
FAST f=21 a=8       6.458788       4.071597        8          482
FAST f=21 a=8       0.063817       4.071597        8          482
FAST f=21 a=9       6.377591       4.052905        8          434
FAST f=21 a=9       0.063112       4.052905        8          434
FAST f=21 a=10       6.360752       4.047773        8          530
FAST f=21 a=10       0.063606       4.047773        8          530
FAST f=22 a=1       10.523471       4.040812        8          962
FAST f=22 a=1       0.14214       4.040812        8          962
FAST f=22 a=2       9.454758       4.059396        8          914
FAST f=22 a=2       0.118343       4.059396        8          914
FAST f=22 a=3       9.043197       4.043019        8          1922
FAST f=22 a=3       0.109798       4.043019        8          1922
FAST f=22 a=4       8.716261       4.044819        8          770
FAST f=22 a=4       0.099687       4.044819        8          770
FAST f=22 a=5       8.529472       4.070576        8          530
FAST f=22 a=5       0.093127       4.070576        8          530
FAST f=22 a=6       8.424241       4.070565        8          722
FAST f=22 a=6       0.093703       4.070565        8          722
FAST f=22 a=7       8.403391       4.070591        8          578
FAST f=22 a=7       0.089763       4.070591        8          578
FAST f=22 a=8       8.285221       4.089171        8          530
FAST f=22 a=8       0.087716       4.089171        8          530
FAST f=22 a=9       8.282506       4.047470        8          722
FAST f=22 a=9       0.089773       4.047470        8          722
FAST f=22 a=10       8.241809       4.064151        8          818
FAST f=22 a=10       0.090413       4.064151        8          818
FAST f=23 a=1       12.389208       4.051635        6          530
FAST f=23 a=1       0.147796       4.051635        6          530
FAST f=23 a=2       11.300910       4.042835        6          914
FAST f=23 a=2       0.133178       4.042835        6          914
FAST f=23 a=3       10.879455       4.047415        8          626
FAST f=23 a=3       0.129571       4.047415        8          626
FAST f=23 a=4       10.522718       4.038269        6          914
FAST f=23 a=4       0.118121       4.038269        6          914
FAST f=23 a=5       10.348043       4.066884        8          434
FAST f=23 a=5       0.112098       4.066884        8          434
FAST f=23 a=6       10.238630       4.048635        8          1010
FAST f=23 a=6       0.120281       4.048635        8          1010
FAST f=23 a=7       10.213255       4.061809        8          530
FAST f=23 a=7       0.1121       4.061809        8          530
FAST f=23 a=8       10.107879       4.074104        8          818
FAST f=23 a=8       0.116544       4.074104        8          818
FAST f=23 a=9       10.063424       4.064811        8          674
FAST f=23 a=9       0.109045       4.064811        8          674
FAST f=23 a=10       10.035801       4.054918        8          530
FAST f=23 a=10       0.108735       4.054918        8          530
FAST f=24 a=1       14.963878       4.073490        8          722
FAST f=24 a=1       0.206344       4.073490        8          722
FAST f=24 a=2       13.833472       4.036100        8          962
FAST f=24 a=2       0.17486       4.036100        8          962
FAST f=24 a=3       13.404631       4.026281        6          1106
FAST f=24 a=3       0.153961       4.026281        6          1106
FAST f=24 a=4       13.041164       4.065448        8          674
FAST f=24 a=4       0.155509       4.065448        8          674
FAST f=24 a=5       12.879412       4.054636        8          674
FAST f=24 a=5       0.148282       4.054636        8          674
FAST f=24 a=6       12.773736       4.081376        8          530
FAST f=24 a=6       0.142563       4.081376        8          530
FAST f=24 a=7       12.711310       4.059834        8          770
FAST f=24 a=7       0.149321       4.059834        8          770
FAST f=24 a=8       12.635459       4.052050        8          1298
FAST f=24 a=8       0.15095       4.052050        8          1298
FAST f=24 a=9       12.558104       4.076516        8          722
FAST f=24 a=9       0.144361       4.076516        8          722
FAST f=24 a=10       10.661348       4.062137        8          818
FAST f=24 a=10       0.108232       4.062137        8          818


hg-changelog:
NODICT       0.000017       1.377590        
RANDOM       0.186171       2.097487        
LEGACY       1.670867       2.058907        
COVER       173.561948       2.189685        8          98
COVER       4.811180       2.189685        8          98
FAST f=15 a=1       18.685906       2.129682        8          434
FAST f=15 a=1       0.173376       2.129682        8          434
FAST f=15 a=2       12.928259       2.131890        8          482
FAST f=15 a=2       0.102582       2.131890        8          482
FAST f=15 a=3       11.132343       2.128027        8          386
FAST f=15 a=3       0.077122       2.128027        8          386
FAST f=15 a=4       10.120683       2.125797        8          434
FAST f=15 a=4       0.065175       2.125797        8          434
FAST f=15 a=5       9.479092       2.127697        8          386
FAST f=15 a=5       0.057905       2.127697        8          386
FAST f=15 a=6       9.159523       2.127132        8          1682
FAST f=15 a=6       0.058604       2.127132        8          1682
FAST f=15 a=7       8.724003       2.129914        8          434
FAST f=15 a=7       0.0493       2.129914        8          434
FAST f=15 a=8       8.595001       2.127137        8          338
FAST f=15 a=8       0.0474       2.127137        8          338
FAST f=15 a=9       8.356405       2.125512        8          482
FAST f=15 a=9       0.046126       2.125512        8          482
FAST f=15 a=10       8.207111       2.126066        8          338
FAST f=15 a=10       0.043292       2.126066        8          338
FAST f=16 a=1       18.464436       2.144040        8          242
FAST f=16 a=1       0.172156       2.144040        8          242
FAST f=16 a=2       12.844825       2.148171        8          194
FAST f=16 a=2       0.099619       2.148171        8          194
FAST f=16 a=3       11.082568       2.140837        8          290
FAST f=16 a=3       0.079165       2.140837        8          290
FAST f=16 a=4       10.066749       2.144405        8          386
FAST f=16 a=4       0.068411       2.144405        8          386
FAST f=16 a=5       9.501121       2.140720        8          386
FAST f=16 a=5       0.061316       2.140720        8          386
FAST f=16 a=6       9.179332       2.139478        8          386
FAST f=16 a=6       0.056322       2.139478        8          386
FAST f=16 a=7       8.849438       2.142412        8          194
FAST f=16 a=7       0.050493       2.142412        8          194
FAST f=16 a=8       8.810919       2.143454        8          434
FAST f=16 a=8       0.051304       2.143454        8          434
FAST f=16 a=9       8.553900       2.140339        8          194
FAST f=16 a=9       0.047285       2.140339        8          194
FAST f=16 a=10       8.398027       2.143130        8          386
FAST f=16 a=10       0.046386       2.143130        8          386
FAST f=17 a=1       18.644657       2.157192        8          98
FAST f=17 a=1       0.173884       2.157192        8          98
FAST f=17 a=2       13.071242       2.159830        8          146
FAST f=17 a=2       0.10388       2.159830        8          146
FAST f=17 a=3       11.332366       2.153654        6          194
FAST f=17 a=3       0.08983       2.153654        6          194
FAST f=17 a=4       10.362413       2.156813        8          242
FAST f=17 a=4       0.070389       2.156813        8          242
FAST f=17 a=5       9.808159       2.155098        6          338
FAST f=17 a=5       0.072661       2.155098        6          338
FAST f=17 a=6       9.451165       2.153845        6          146
FAST f=17 a=6       0.064959       2.153845        6          146
FAST f=17 a=7       9.163097       2.155424        6          242
FAST f=17 a=7       0.064323       2.155424        6          242
FAST f=17 a=8       9.047276       2.156640        8          242
FAST f=17 a=8       0.053382       2.156640        8          242
FAST f=17 a=9       8.807671       2.152396        8          146
FAST f=17 a=9       0.049617       2.152396        8          146
FAST f=17 a=10       8.649827       2.152370        8          146
FAST f=17 a=10       0.047849       2.152370        8          146
FAST f=18 a=1       18.809502       2.168116        8          98
FAST f=18 a=1       0.175226       2.168116        8          98
FAST f=18 a=2       13.756502       2.170870        6          242
FAST f=18 a=2       0.119507       2.170870        6          242
FAST f=18 a=3       12.059748       2.163094        6          98
FAST f=18 a=3       0.093912       2.163094        6          98
FAST f=18 a=4       11.410294       2.172372        8          98
FAST f=18 a=4       0.073048       2.172372        8          98
FAST f=18 a=5       10.560297       2.166388        8          98
FAST f=18 a=5       0.065136       2.166388        8          98
FAST f=18 a=6       10.071390       2.162672        8          98
FAST f=18 a=6       0.059402       2.162672        8          98
FAST f=18 a=7       10.084214       2.166624        6          194
FAST f=18 a=7       0.073276       2.166624        6          194
FAST f=18 a=8       9.953226       2.167454        8          98
FAST f=18 a=8       0.053659       2.167454        8          98
FAST f=18 a=9       8.982461       2.161593        6          146
FAST f=18 a=9       0.05955       2.161593        6          146
FAST f=18 a=10       8.986092       2.164373        6          242
FAST f=18 a=10       0.059135       2.164373        6          242
FAST f=19 a=1       18.908277       2.176021        8          98
FAST f=19 a=1       0.177316       2.176021        8          98
FAST f=19 a=2       13.471313       2.176103        8          98
FAST f=19 a=2       0.106344       2.176103        8          98
FAST f=19 a=3       11.571406       2.172812        8          98
FAST f=19 a=3       0.083293       2.172812        8          98
FAST f=19 a=4       10.632775       2.177770        6          146
FAST f=19 a=4       0.079864       2.177770        6          146
FAST f=19 a=5       10.030190       2.175574        6          146
FAST f=19 a=5       0.07223       2.175574        6          146
FAST f=19 a=6       9.717818       2.169997        8          98
FAST f=19 a=6       0.060049       2.169997        8          98
FAST f=19 a=7       9.397531       2.172770        8          146
FAST f=19 a=7       0.057188       2.172770        8          146
FAST f=19 a=8       9.281061       2.175822        8          98
FAST f=19 a=8       0.053711       2.175822        8          98
FAST f=19 a=9       9.165242       2.169849        6          146
FAST f=19 a=9       0.059898       2.169849        6          146
FAST f=19 a=10       9.048763       2.173394        8          98
FAST f=19 a=10       0.049757       2.173394        8          98
FAST f=20 a=1       21.166917       2.183923        6          98
FAST f=20 a=1       0.205425       2.183923        6          98
FAST f=20 a=2       15.642753       2.182349        6          98
FAST f=20 a=2       0.135957       2.182349        6          98
FAST f=20 a=3       14.053730       2.173544        6          98
FAST f=20 a=3       0.11266       2.173544        6          98
FAST f=20 a=4       15.270019       2.183656        8          98
FAST f=20 a=4       0.107892       2.183656        8          98
FAST f=20 a=5       15.497927       2.174661        6          98
FAST f=20 a=5       0.100305       2.174661        6          98
FAST f=20 a=6       13.973505       2.172391        8          98
FAST f=20 a=6       0.087565       2.172391        8          98
FAST f=20 a=7       14.083296       2.172443        8          98
FAST f=20 a=7       0.078062       2.172443        8          98
FAST f=20 a=8       12.560048       2.175581        8          98
FAST f=20 a=8       0.070282       2.175581        8          98
FAST f=20 a=9       13.078645       2.173975        6          146
FAST f=20 a=9       0.081041       2.173975        6          146
FAST f=20 a=10       12.823328       2.177778        8          98
FAST f=20 a=10       0.074522       2.177778        8          98
FAST f=21 a=1       29.825370       2.183057        6          98
FAST f=21 a=1       0.334453       2.183057        6          98
FAST f=21 a=2       29.476474       2.182752        8          98
FAST f=21 a=2       0.286602       2.182752        8          98
FAST f=21 a=3       25.937186       2.175867        8          98
FAST f=21 a=3       0.17626       2.175867        8          98
FAST f=21 a=4       20.413865       2.179780        8          98
FAST f=21 a=4       0.206085       2.179780        8          98
FAST f=21 a=5       20.541889       2.178328        6          146
FAST f=21 a=5       0.199157       2.178328        6          146
FAST f=21 a=6       21.090670       2.174443        6          146
FAST f=21 a=6       0.190645       2.174443        6          146
FAST f=21 a=7       20.221569       2.177384        6          146
FAST f=21 a=7       0.184278       2.177384        6          146
FAST f=21 a=8       20.322357       2.179456        6          98
FAST f=21 a=8       0.178458       2.179456        6          98
FAST f=21 a=9       20.683912       2.174396        6          146
FAST f=21 a=9       0.190829       2.174396        6          146
FAST f=21 a=10       20.840865       2.174905        8          98
FAST f=21 a=10       0.172515       2.174905        8          98
FAST f=22 a=1       36.822827       2.181612        6          98
FAST f=22 a=1       0.437389       2.181612        6          98
FAST f=22 a=2       30.616902       2.183142        8          98
FAST f=22 a=2       0.324284       2.183142        8          98
FAST f=22 a=3       28.472482       2.178130        8          98
FAST f=22 a=3       0.236538       2.178130        8          98
FAST f=22 a=4       25.847028       2.181878        8          98
FAST f=22 a=4       0.263744       2.181878        8          98
FAST f=22 a=5       27.095881       2.180775        8          98
FAST f=22 a=5       0.24988       2.180775        8          98
FAST f=22 a=6       25.939172       2.170916        8          98
FAST f=22 a=6       0.240033       2.170916        8          98
FAST f=22 a=7       27.064194       2.177849        8          98
FAST f=22 a=7       0.242383       2.177849        8          98
FAST f=22 a=8       25.140221       2.178216        8          98
FAST f=22 a=8       0.237601       2.178216        8          98
FAST f=22 a=9       25.505283       2.177455        6          146
FAST f=22 a=9       0.223217       2.177455        6          146
FAST f=22 a=10       24.529362       2.176705        6          98
FAST f=22 a=10       0.222876       2.176705        6          98
FAST f=23 a=1       39.127310       2.183006        6          98
FAST f=23 a=1       0.417338       2.183006        6          98
FAST f=23 a=2       32.468161       2.183524        6          98
FAST f=23 a=2       0.351645       2.183524        6          98
FAST f=23 a=3       31.577620       2.172604        6          98
FAST f=23 a=3       0.319659       2.172604        6          98
FAST f=23 a=4       30.129247       2.183932        6          98
FAST f=23 a=4       0.307239       2.183932        6          98
FAST f=23 a=5       29.103376       2.183529        6          146
FAST f=23 a=5       0.285533       2.183529        6          146
FAST f=23 a=6       29.776045       2.174367        8          98
FAST f=23 a=6       0.276846       2.174367        8          98
FAST f=23 a=7       28.940407       2.178022        6          146
FAST f=23 a=7       0.274082       2.178022        6          146
FAST f=23 a=8       29.256009       2.179462        6          98
FAST f=23 a=8       0.26949       2.179462        6          98
FAST f=23 a=9       29.347312       2.170407        8          98
FAST f=23 a=9       0.265034       2.170407        8          98
FAST f=23 a=10       29.140081       2.171762        8          98
FAST f=23 a=10       0.259183       2.171762        8          98
FAST f=24 a=1       44.871179       2.182115        6          98
FAST f=24 a=1       0.509433       2.182115        6          98
FAST f=24 a=2       38.694867       2.180549        8          98
FAST f=24 a=2       0.406695       2.180549        8          98
FAST f=24 a=3       38.363769       2.172821        8          98
FAST f=24 a=3       0.359581       2.172821        8          98
FAST f=24 a=4       36.580797       2.184142        8          98
FAST f=24 a=4       0.340614       2.184142        8          98
FAST f=24 a=5       33.125701       2.183301        8          98
FAST f=24 a=5       0.324874       2.183301        8          98
FAST f=24 a=6       34.776068       2.173019        6          146
FAST f=24 a=6       0.340397       2.173019        6          146
FAST f=24 a=7       34.417625       2.176561        6          146
FAST f=24 a=7       0.308223       2.176561        6          146
FAST f=24 a=8       35.470291       2.182161        6          98
FAST f=24 a=8       0.307724       2.182161        6          98
FAST f=24 a=9       34.927252       2.172682        6          146
FAST f=24 a=9       0.300598       2.172682        6          146
FAST f=24 a=10       33.238355       2.173395        6          98
FAST f=24 a=10       0.249916       2.173395        6          98


hg-manifest:
NODICT       0.000004       1.866377        
RANDOM       0.696346       2.309436        
LEGACY       7.064527       2.506977        
COVER       876.312865       2.582528        8          434
COVER       35.684533       2.582528        8          434
FAST f=15 a=1       76.618201       2.404013        8          1202
FAST f=15 a=1       0.700722       2.404013        8          1202
FAST f=15 a=2       49.213058       2.409248        6          1826
FAST f=15 a=2       0.473393       2.409248        6          1826
FAST f=15 a=3       41.753197       2.409677        8          1490
FAST f=15 a=3       0.336848       2.409677        8          1490
FAST f=15 a=4       38.648295       2.407996        8          1538
FAST f=15 a=4       0.283952       2.407996        8          1538
FAST f=15 a=5       36.144936       2.402895        8          1874
FAST f=15 a=5       0.270128       2.402895        8          1874
FAST f=15 a=6       35.484675       2.394873        8          1586
FAST f=15 a=6       0.251637       2.394873        8          1586
FAST f=15 a=7       34.280599       2.397311        8          1778
FAST f=15 a=7       0.23984       2.397311        8          1778
FAST f=15 a=8       32.122572       2.396089        6          1490
FAST f=15 a=8       0.251508       2.396089        6          1490
FAST f=15 a=9       29.909842       2.390092        6          1970
FAST f=15 a=9       0.251233       2.390092        6          1970
FAST f=15 a=10       30.102938       2.400086        6          1682
FAST f=15 a=10       0.23688       2.400086        6          1682
FAST f=16 a=1       67.750401       2.475460        6          1346
FAST f=16 a=1       0.796035       2.475460        6          1346
FAST f=16 a=2       52.812027       2.480860        6          1730
FAST f=16 a=2       0.480384       2.480860        6          1730
FAST f=16 a=3       44.179259       2.469304        8          1970
FAST f=16 a=3       0.332657       2.469304        8          1970
FAST f=16 a=4       37.612728       2.478208        6          1970
FAST f=16 a=4       0.32498       2.478208        6          1970
FAST f=16 a=5       35.056222       2.475568        6          1298
FAST f=16 a=5       0.302824       2.475568        6          1298
FAST f=16 a=6       34.713012       2.486079        8          1730
FAST f=16 a=6       0.24755       2.486079        8          1730
FAST f=16 a=7       33.713687       2.477180        6          1682
FAST f=16 a=7       0.280358       2.477180        6          1682
FAST f=16 a=8       31.571412       2.475418        8          1538
FAST f=16 a=8       0.241241       2.475418        8          1538
FAST f=16 a=9       31.608069       2.478263        8          1922
FAST f=16 a=9       0.241764       2.478263        8          1922
FAST f=16 a=10       31.358002       2.472263        8          1442
FAST f=16 a=10       0.221661       2.472263        8          1442
FAST f=17 a=1       66.185775       2.536085        6          1346
FAST f=17 a=1       0.713549       2.536085        6          1346
FAST f=17 a=2       50.365000       2.546105        8          1298
FAST f=17 a=2       0.467846       2.546105        8          1298
FAST f=17 a=3       42.712843       2.536250        8          1298
FAST f=17 a=3       0.34047       2.536250        8          1298
FAST f=17 a=4       39.514227       2.535555        8          1442
FAST f=17 a=4       0.302989       2.535555        8          1442
FAST f=17 a=5       35.189292       2.524925        8          1202
FAST f=17 a=5       0.273451       2.524925        8          1202
FAST f=17 a=6       35.791683       2.523466        8          1202
FAST f=17 a=6       0.268261       2.523466        8          1202
FAST f=17 a=7       37.416136       2.526625        6          1010
FAST f=17 a=7       0.277558       2.526625        6          1010
FAST f=17 a=8       37.084707       2.533274        6          1250
FAST f=17 a=8       0.285104       2.533274        6          1250
FAST f=17 a=9       34.183814       2.532765        8          1298
FAST f=17 a=9       0.235133       2.532765        8          1298
FAST f=17 a=10       31.149235       2.528722        8          1346
FAST f=17 a=10       0.232679       2.528722        8          1346
FAST f=18 a=1       72.942176       2.559857        6          386
FAST f=18 a=1       0.718618       2.559857        6          386
FAST f=18 a=2       51.690440       2.559572        8          290
FAST f=18 a=2       0.403978       2.559572        8          290
FAST f=18 a=3       45.344908       2.561040        8          962
FAST f=18 a=3       0.357205       2.561040        8          962
FAST f=18 a=4       39.804522       2.558446        8          1010
FAST f=18 a=4       0.310526       2.558446        8          1010
FAST f=18 a=5       38.134888       2.561811        8          626
FAST f=18 a=5       0.273743       2.561811        8          626
FAST f=18 a=6       35.091890       2.555518        8          722
FAST f=18 a=6       0.260135       2.555518        8          722
FAST f=18 a=7       34.639523       2.562938        8          290
FAST f=18 a=7       0.234294       2.562938        8          290
FAST f=18 a=8       36.076431       2.563567        8          1586
FAST f=18 a=8       0.274075       2.563567        8          1586
FAST f=18 a=9       36.376433       2.560950        8          722
FAST f=18 a=9       0.240106       2.560950        8          722
FAST f=18 a=10       32.624790       2.559340        8          578
FAST f=18 a=10       0.234704       2.559340        8          578
FAST f=19 a=1       70.513761       2.572441        8          194
FAST f=19 a=1       0.726112       2.572441        8          194
FAST f=19 a=2       59.263032       2.574560        8          482
FAST f=19 a=2       0.451554       2.574560        8          482
FAST f=19 a=3       51.509594       2.571546        6          194
FAST f=19 a=3       0.393014       2.571546        6          194
FAST f=19 a=4       55.393906       2.573386        8          482
FAST f=19 a=4       0.38819       2.573386        8          482
FAST f=19 a=5       43.201736       2.567589        8          674
FAST f=19 a=5       0.292155       2.567589        8          674
FAST f=19 a=6       42.911687       2.572666        6          434
FAST f=19 a=6       0.303988       2.572666        6          434
FAST f=19 a=7       44.687591       2.573613        6          290
FAST f=19 a=7       0.308721       2.573613        6          290
FAST f=19 a=8       37.372868       2.571039        6          194
FAST f=19 a=8       0.287137       2.571039        6          194
FAST f=19 a=9       36.074230       2.566473        6          482
FAST f=19 a=9       0.280721       2.566473        6          482
FAST f=19 a=10       33.731720       2.570306        8          194
FAST f=19 a=10       0.224073       2.570306        8          194
FAST f=20 a=1       79.670634       2.581146        6          290
FAST f=20 a=1       0.899986       2.581146        6          290
FAST f=20 a=2       58.827141       2.579782        8          386
FAST f=20 a=2       0.602288       2.579782        8          386
FAST f=20 a=3       51.289004       2.579627        8          722
FAST f=20 a=3       0.446091       2.579627        8          722
FAST f=20 a=4       47.711068       2.581508        8          722
FAST f=20 a=4       0.473007       2.581508        8          722
FAST f=20 a=5       47.402929       2.578062        6          434
FAST f=20 a=5       0.497131       2.578062        6          434
FAST f=20 a=6       54.797102       2.577365        8          482
FAST f=20 a=6       0.515061       2.577365        8          482
FAST f=20 a=7       51.370877       2.583050        8          386
FAST f=20 a=7       0.402878       2.583050        8          386
FAST f=20 a=8       51.437931       2.574875        6          242
FAST f=20 a=8       0.453094       2.574875        6          242
FAST f=20 a=9       44.105456       2.576700        6          242
FAST f=20 a=9       0.456633       2.576700        6          242
FAST f=20 a=10       44.447580       2.578305        8          338
FAST f=20 a=10       0.409121       2.578305        8          338
FAST f=21 a=1       113.031686       2.582449        6          242
FAST f=21 a=1       1.456971       2.582449        6          242
FAST f=21 a=2       97.700932       2.582124        8          194
FAST f=21 a=2       1.072078       2.582124        8          194
FAST f=21 a=3       96.563648       2.585479        8          434
FAST f=21 a=3       0.949528       2.585479        8          434
FAST f=21 a=4       90.597813       2.582366        6          386
FAST f=21 a=4       0.76944       2.582366        6          386
FAST f=21 a=5       86.815980       2.579043        8          434
FAST f=21 a=5       0.858167       2.579043        8          434
FAST f=21 a=6       91.235820       2.578378        8          530
FAST f=21 a=6       0.684274       2.578378        8          530
FAST f=21 a=7       84.392788       2.581243        8          386
FAST f=21 a=7       0.814386       2.581243        8          386
FAST f=21 a=8       82.052310       2.582547        8          338
FAST f=21 a=8       0.822633       2.582547        8          338
FAST f=21 a=9       74.696074       2.579319        8          194
FAST f=21 a=9       0.811028       2.579319        8          194
FAST f=21 a=10       76.211170       2.578766        8          290
FAST f=21 a=10       0.809715       2.578766        8          290
FAST f=22 a=1       138.976871       2.580478        8          194
FAST f=22 a=1       1.748932       2.580478        8          194
FAST f=22 a=2       120.164097       2.583633        8          386
FAST f=22 a=2       1.333239       2.583633        8          386
FAST f=22 a=3       111.986474       2.582566        6          194
FAST f=22 a=3       1.305734       2.582566        6          194
FAST f=22 a=4       108.548148       2.583068        6          194
FAST f=22 a=4       1.314026       2.583068        6          194
FAST f=22 a=5       103.173017       2.583495        6          290
FAST f=22 a=5       1.228664       2.583495        6          290
FAST f=22 a=6       108.421262       2.582349        8          530
FAST f=22 a=6       1.076773       2.582349        8          530
FAST f=22 a=7       103.284127       2.581022        8          386
FAST f=22 a=7       1.112117       2.581022        8          386
FAST f=22 a=8       96.330279       2.581073        8          290
FAST f=22 a=8       1.109303       2.581073        8          290
FAST f=22 a=9       97.651348       2.580075        6          194
FAST f=22 a=9       0.933032       2.580075        6          194
FAST f=22 a=10       101.660621       2.584886        8          194
FAST f=22 a=10       0.796823       2.584886        8          194
FAST f=23 a=1       159.322978       2.581474        6          242
FAST f=23 a=1       2.015878       2.581474        6          242
FAST f=23 a=2       134.331775       2.581619        8          194
FAST f=23 a=2       1.545845       2.581619        8          194
FAST f=23 a=3       127.724552       2.579888        6          338
FAST f=23 a=3       1.444496       2.579888        6          338
FAST f=23 a=4       126.077675       2.578137        6          242
FAST f=23 a=4       1.364394       2.578137        6          242
FAST f=23 a=5       124.914027       2.580843        8          338
FAST f=23 a=5       1.116059       2.580843        8          338
FAST f=23 a=6       122.874153       2.577637        6          338
FAST f=23 a=6       1.164584       2.577637        6          338
FAST f=23 a=7       123.099257       2.582715        6          386
FAST f=23 a=7       1.354042       2.582715        6          386
FAST f=23 a=8       122.026753       2.577681        8          194
FAST f=23 a=8       1.210966       2.577681        8          194
FAST f=23 a=9       121.164312       2.584599        6          290
FAST f=23 a=9       1.174859       2.584599        6          290
FAST f=23 a=10       117.462222       2.580358        8          194
FAST f=23 a=10       1.075258       2.580358        8          194
FAST f=24 a=1       169.539659       2.581642        6          194
FAST f=24 a=1       1.916804       2.581642        6          194
FAST f=24 a=2       160.539270       2.580421        6          290
FAST f=24 a=2       1.71087       2.580421        6          290
FAST f=24 a=3       155.455874       2.580449        6          242
FAST f=24 a=3       1.60307       2.580449        6          242
FAST f=24 a=4       147.630320       2.582953        6          338
FAST f=24 a=4       1.396364       2.582953        6          338
FAST f=24 a=5       133.767428       2.580589        6          290
FAST f=24 a=5       1.19933       2.580589        6          290
FAST f=24 a=6       146.437535       2.579453        8          194
FAST f=24 a=6       1.385405       2.579453        8          194
FAST f=24 a=7       147.227507       2.584155        8          386
FAST f=24 a=7       1.48942       2.584155        8          386
FAST f=24 a=8       138.005773       2.584115        8          194
FAST f=24 a=8       1.352       2.584115        8          194
FAST f=24 a=9       141.442625       2.582902        8          290
FAST f=24 a=9       1.39647       2.582902        8          290
FAST f=24 a=10       142.157446       2.582701        8          434
FAST f=24 a=10       1.498889       2.582701        8          434
This Meson project is provided with no guarantee and maintained by Dima Krasner <dima@dimakrasner.com>.

It outputs one libzstd, either shared or static, depending on default_library.
# Linux Kernel Patch

There are four pieces, the `xxhash` kernel module, the `zstd_compress` and `zstd_decompress` kernel modules, the BtrFS patch, and the SquashFS patch.
The patches are based off of the linux kernel master branch.

## xxHash kernel module

* The patch is located in `xxhash.diff`.
* The header is in `include/linux/xxhash.h`.
* The source is in `lib/xxhash.c`.
* `test/XXHashUserLandTest.cpp` contains tests for the patch in userland by mocking the kernel headers.
  I tested the tests by commenting a line of of each branch in `xxhash.c` one line at a time, and made sure the tests failed.
  It can be run with the following commands:
  ```
  cd test && make googletest && make XXHashUserLandTest && ./XXHashUserLandTest
  ```
* I also benchmarked the `xxhash` module against upstream xxHash, and made sure that they ran at the same speed.

## Zstd Kernel modules

* The (large) patch is located in `zstd.diff`, which depends on `xxhash.diff`.
* The header is in `include/linux/zstd.h`.
* It is split up into `zstd_compress` and `zstd_decompress`, which can be loaded independently.
* Source files are in `lib/zstd/`.
* `lib/Kconfig` and `lib/Makefile` need to be modified by applying `lib/Kconfig.diff` and `lib/Makefile.diff` respectively.
  These changes are also included in the `zstd.diff`.
* `test/UserlandTest.cpp` contains tests for the patch in userland by mocking the kernel headers.
  It can be run with the following commands:
  ```
  cd test && make googletest && make UserlandTest && ./UserlandTest
  ```

## BtrFS

* The patch is located in `btrfs.diff`.
* Additionally `fs/btrfs/zstd.c` is provided as a source for convenience.
* The patch seems to be working, it doesn't crash the kernel, and compresses at speeds and ratios that are expected.
  It could still use some more testing for fringe features, like printing options.

### Benchmarks

Benchmarks run on a Ubuntu 14.04 with 2 cores and 4 GiB of RAM.
The VM is running on a Macbook Pro with a 3.1 GHz Intel Core i7 processor,
16 GB of ram, and a SSD.
The kernel running was built from the master branch with the patch.

The compression benchmark is copying 10 copies of the
unzipped [silesia corpus](http://mattmahoney.net/dc/silesia.html) into a BtrFS
filesystem mounted with `-o compress-force={none, lzo, zlib, zstd}`.
The decompression benchmark is timing how long it takes to `tar` all 10 copies
into `/dev/null`.
The compression ratio is measured by comparing the output of `df` and `du`.
See `btrfs-benchmark.sh` for details.

| Algorithm | Compression ratio | Compression speed | Decompression speed |
|-----------|-------------------|-------------------|---------------------|
| None      | 0.99              | 504 MB/s          | 686 MB/s            |
| lzo       | 1.66              | 398 MB/s          | 442 MB/s            |
| zlib      | 2.58              | 65 MB/s           | 241 MB/s            |
| zstd 1    | 2.57              | 260 MB/s          | 383 MB/s            |
| zstd 3    | 2.71              | 174 MB/s          | 408 MB/s            |
| zstd 6    | 2.87              | 70 MB/s           | 398 MB/s            |
| zstd 9    | 2.92              | 43 MB/s           | 406 MB/s            |
| zstd 12   | 2.93              | 21 MB/s           | 408 MB/s            |
| zstd 15   | 3.01              | 11 MB/s           | 354 MB/s            |


## SquashFS

* The patch is located in `squashfs.diff`
* Additionally `fs/squashfs/zstd_wrapper.c` is provided as a source for convenience.
* The patch has been tested on the master branch of the kernel.

### Benchmarks

Benchmarks run on a Ubuntu 14.04 with 2 cores and 4 GiB of RAM.
The VM is running on a Macbook Pro with a 3.1 GHz Intel Core i7 processor,
16 GB of ram, and a SSD.
The kernel running was built from the master branch with the patch.

The compression benchmark is the file tree from the SquashFS archive found in the
Ubuntu 16.10 desktop image (ubuntu-16.10-desktop-amd64.iso).
The compression benchmark uses mksquashfs with the default block size (128 KB)
and various compression algorithms/compression levels.
`xz` and `zstd` are also benchmarked with 256 KB blocks.
The decompression benchmark is timing how long it takes to `tar` the file tree
into `/dev/null`.
See `squashfs-benchmark.sh` for details.

| Algorithm      | Compression ratio | Compression speed | Decompression speed |
|----------------|-------------------|-------------------|---------------------|
| gzip           | 2.92              |   15 MB/s         | 128 MB/s            |
| lzo            | 2.64              |  9.5 MB/s         | 217 MB/s            |
| lz4            | 2.12              |   94 MB/s         | 218 MB/s            |
| xz             | 3.43              |  5.5 MB/s         |  35 MB/s            |
| xz 256 KB      | 3.53              |  5.4 MB/s         |  40 MB/s            |
| zstd 1         | 2.71              |   96 MB/s         | 210 MB/s            |
| zstd 5         | 2.93              |   69 MB/s         | 198 MB/s            |
| zstd 10        | 3.01              |   41 MB/s         | 225 MB/s            |
| zstd 15        | 3.13              | 11.4 MB/s         | 224 MB/s            |
| zstd 16 256 KB | 3.24              |  8.1 MB/s         | 210 MB/s            |
gen_html - a program for automatic generation of zstd manual 
============================================================

#### Introduction

This simple C++ program generates a single-page HTML manual from `zstd.h`.

The format of recognized comment blocks is following:
- comments of type `/*!` mean: this is a function declaration; switch comments with declarations
- comments of type `/**` and `/*-` mean: this is a comment; use a `<H2>` header for the first line
- comments of type `/*=` and `/**=` mean: use a `<H3>` header and show also all functions until first empty line
- comments of type `/*X` where `X` is different from above-mentioned are ignored

Moreover:
- `ZSTDLIB_API` is removed to improve readability
- `typedef` are detected and included even if uncommented
- comments of type `/**<` and `/*!<` are detected and only function declaration is highlighted (bold)


#### Usage

The program requires 3 parameters:
```
gen_html [zstd_version] [input_file] [output_html]
```

To compile program and generate zstd manual we have used: 
```
make
./gen_html.exe 1.1.1 ../../lib/zstd.h zstd_manual.html
```

## Requirement

The `Dockerfile` script requires a version of `docker` >= 17.05

## Installing docker

The officiel docker install docs use a ppa with a modern version available:
https://docs.docker.com/install/linux/docker-ce/ubuntu/

## How to run

`docker build -t zstd .`

## test

```
echo foo | docker run -i --rm zstd | docker run -i --rm zstd zstdcat
foo
```
Programs and scripts for automated testing of Zstandard
=======================================================

This directory contains the following programs and scripts:
- `datagen` : Synthetic and parametrable data generator, for tests
- `fullbench`  : Precisely measure speed for each zstd inner functions
- `fuzzer`  : Test tool, to check zstd integrity on target platform
- `paramgrill` : parameter tester for zstd
- `test-zstd-speed.py` : script for testing zstd speed difference between commits
- `test-zstd-versions.py` : compatibility test between zstd versions stored on Github (v0.1+)
- `zbufftest`  : Test tool to check ZBUFF (a buffered streaming API) integrity
- `zstreamtest` : Fuzzer test tool for zstd streaming API
- `legacy` : Test tool to test decoding of legacy zstd frames
- `decodecorpus` : Tool to generate valid Zstandard frames, for verifying decoder implementations


#### `test-zstd-versions.py` - script for testing zstd interoperability between versions

This script creates `versionsTest` directory to which zstd repository is cloned.
Then all tagged (released) versions of zstd are compiled.
In the following step interoperability between zstd versions is checked.


#### `test-zstd-speed.py` - script for testing zstd speed difference between commits

This script creates `speedTest` directory to which zstd repository is cloned.
Then it compiles all branches of zstd and performs a speed benchmark for a given list of files (the `testFileNames` parameter).
After `sleepTime` (an optional parameter, default 300 seconds) seconds the script checks repository for new commits.
If a new commit is found it is compiled and a speed benchmark for this commit is performed.
The results of the speed benchmark are compared to the previous results.
If compression or decompression speed for one of zstd levels is lower than `lowerLimit` (an optional parameter, default 0.98) the speed benchmark is restarted.
If second results are also lower than `lowerLimit` the warning e-mail is send to recipients from the list (the `emails` parameter).

Additional remarks:
- To be sure that speed results are accurate the script should be run on a "stable" target system with no other jobs running in parallel
- Using the script with virtual machines can lead to large variations of speed results
- The speed benchmark is not performed until computers' load average is lower than `maxLoadAvg` (an optional parameter, default 0.75)
- The script sends e-mails using `mutt`; if `mutt` is not available it sends e-mails without attachments using `mail`; if both are not available it only prints a warning


The example usage with two test files, one e-mail address, and with an additional message:
```
./test-zstd-speed.py "silesia.tar calgary.tar" "email@gmail.com" --message "tested on my laptop" --sleepTime 60
``` 

To run the script in background please use:
```
nohup ./test-zstd-speed.py testFileNames emails &
```

The full list of parameters:
```
positional arguments:
  testFileNames         file names list for speed benchmark
  emails                list of e-mail addresses to send warnings

optional arguments:
  -h, --help            show this help message and exit
  --message MESSAGE     attach an additional message to e-mail
  --lowerLimit LOWERLIMIT
                        send email if speed is lower than given limit
  --maxLoadAvg MAXLOADAVG
                        maximum load average to start testing
  --lastCLevel LASTCLEVEL
                        last compression level for testing
  --sleepTime SLEEPTIME
                        frequency of repository checking in seconds
```

#### `decodecorpus` - tool to generate Zstandard frames for decoder testing
Command line tool to generate test .zst files.

This tool will generate .zst files with checksums,
as well as optionally output the corresponding correct uncompressed data for
extra verfication.

Example:
```
./decodecorpus -ptestfiles -otestfiles -n10000 -s5
```
will generate 10,000 sample .zst files using a seed of 5 in the `testfiles` directory,
with the zstd checksum field set,
as well as the 10,000 original files for more detailed comparison of decompression results.

```
./decodecorpus -t -T1mn
```
will choose a random seed, and for 1 minute,
generate random test frames and ensure that the
zstd library correctly decompresses them in both simple and streaming modes.

#### `paramgrill` - tool for generating compression table parameters and optimizing parameters on file given constraints

Full list of arguments
```
 -T#          : set level 1 speed objective
 -B#          : cut input into blocks of size # (default : single block)
 -S           : benchmarks a single run (example command: -Sl3w10h12)
    w# - windowLog
    h# - hashLog
    c# - chainLog
    s# - searchLog
    l# - searchLength
    t# - targetLength
    S# - strategy
    L# - level
 --zstd=      : Single run, parameter selection syntax same as zstdcli with more parameters
                    (Added forceAttachDictionary / fadt) 
                    When invoked with --optimize, this represents the sample to exceed. 
 --optimize=  : find parameters to maximize compression ratio given parameters
                    Can use all --zstd= commands to constrain the type of solution found in addition to the following constraints
    cSpeed=   : Minimum compression speed
    dSpeed=   : Minimum decompression speed
    cMem=     : Maximum compression memory
    lvl=      : Searches for solutions which are strictly better than that compression lvl in ratio and cSpeed, 
    stc=      : When invoked with lvl=, represents percentage slack in ratio/cSpeed allowed for a solution to be considered (Default 100%)
              : In normal operation, represents percentage slack in choosing viable starting strategy selection in choosing the default parameters
                    (Lower value will begin with stronger strategies) (Default 90%)
    speedRatio=   (accepts decimals)
              : determines value of gains in speed vs gains in ratio
                    when determining overall winner (default 5 (1% ratio = 5% speed)).
    tries=    : Maximum number of random restarts on a single strategy before switching (Default 5)
                    Higher values will make optimizer run longer, more chances to find better solution.
    memLog    : Limits the log of the size of each memotable (1 per strategy). Will use hash tables when state space is larger than max size. 
                    Setting memLog = 0 turns off memoization 
 --display=   : specifiy which parameters are included in the output
                    can use all --zstd parameter names and 'cParams' as a shorthand for all parameters used in ZSTD_compressionParameters 
                    (Default: display all params available)
 -P#          : generated sample compressibility (when no file is provided)
 -t#          : Caps runtime of operation in seconds (default : 99999 seconds (about 27 hours )) 
 -v           : Prints Benchmarking output
 -D           : Next argument dictionary file
 -s           : Benchmark all files separately
 -q           : Quiet, repeat for more quiet
                  -q Prints parameters + results whenever a new best is found
                  -qq Only prints parameters whenever a new best is found, prints final parameters + results
                  -qqq Only print final parameters + results
                  -qqqq Only prints final parameter set in the form --zstd=
 -v           : Verbose, cancels quiet, repeat for more volume
                  -v Prints all candidate parameters and results

```
 Any inputs afterwards are treated as files to benchmark.
# Fuzzing

Each fuzzing target can be built with multiple engines.
Zstd provides a fuzz corpus for each target that can be downloaded with
the command:

```
make corpora
```

It will download each corpus into `./corpora/TARGET`.

## fuzz.py

`fuzz.py` is a helper script for building and running fuzzers.
Run `./fuzz.py -h` for the commands and run `./fuzz.py COMMAND -h` for
command specific help.

### Generating Data

`fuzz.py` provides a utility to generate seed data for each fuzzer.

```
make -C ../tests decodecorpus
./fuzz.py gen TARGET
```

By default it outputs 100 samples, each at most 8KB into `corpora/TARGET-seed`,
but that can be configured with the `--number`, `--max-size-log` and `--seed`
flags.

### Build
It respects the usual build environment variables `CC`, `CFLAGS`, etc.
The environment variables can be overridden with the corresponding flags
`--cc`, `--cflags`, etc.
The specific fuzzing engine is selected with `LIB_FUZZING_ENGINE` or
`--lib-fuzzing-engine`, the default is `libregression.a`.
It has flags that can easily set up sanitizers `--enable-{a,ub,m}san`, and
coverage instrumentation `--enable-coverage`.
It sets sane defaults which can be overriden with flags `--debug`,
`--enable-ubsan-pointer-overlow`, etc.
Run `./fuzz.py build -h` for help.

### Running Fuzzers

`./fuzz.py` can run `libfuzzer`, `afl`, and `regression` tests.
See the help of the relevant command for options.
Flags not parsed by `fuzz.py` are passed to the fuzzing engine.
The command used to run the fuzzer is printed for debugging.

## LibFuzzer

```
# Build libfuzzer if necessary
make libFuzzer
# Build the fuzz targets
./fuzz.py build all --enable-coverage --enable-asan --enable-ubsan --lib-fuzzing-engine Fuzzer/libFuzzer.a --cc clang --cxx clang++
# OR equivalently
CC=clang CXX=clang++ LIB_FUZZING_ENGINE=Fuzzer/libFuzzer.a ./fuzz.py build all --enable-coverage --enable-asan --enable-ubsan
# Run the fuzzer
./fuzz.py libfuzzer TARGET -max_len=8192 -jobs=4
```

where `TARGET` could be `simple_decompress`, `stream_round_trip`, etc.

### MSAN

Fuzzing with `libFuzzer` and `MSAN` will require building a C++ standard library
and libFuzzer with MSAN.
`fuzz.py` respects the environment variables / flags `MSAN_EXTRA_CPPFLAGS`,
`MSAN_EXTRA_CFLAGS`, `MSAN_EXTRA_CXXFLAGS`, `MSAN_EXTRA_LDFLAGS` to easily pass
the extra parameters only for MSAN.

## AFL

The default `LIB_FUZZING_ENGINE` is `libregression.a`, which produces a binary
that AFL can use.

```
# Build the fuzz targets
CC=afl-clang CXX=afl-clang++ ./fuzz.py build all --enable-asan --enable-ubsan
# Run the fuzzer without a memory limit because of ASAN
./fuzz.py afl TARGET -m none
```

## Regression Testing

The regression rest supports the `all` target to run all the fuzzers in one
command.

```
CC=clang CXX=clang++ ./fuzz.py build all --enable-asan --enable-ubsan
./fuzz.py regression all
CC=clang CXX=clang++ ./fuzz.py build all --enable-msan
./fuzz.py regression all
```
Zstandard Documentation
=======================

This directory contains material defining the Zstandard format,
as well as detailed instructions to use `zstd` library.

__`zstd_manual.html`__ : Documentation of `zstd.h` API, in html format.
Click on this link: [http://zstd.net/zstd_manual.html](http://zstd.net/zstd_manual.html)
to display documentation of latest release in readable format within a browser.

__`zstd_compression_format.md`__ : This document defines the Zstandard compression format.
Compliant decoders must adhere to this document,
and compliant encoders must generate data that follows it.

Should you look for ressources to develop your own port of Zstandard algorithm,
you may find the following ressources useful :

__`educational_decoder`__ : This directory contains an implementation of a Zstandard decoder,
compliant with the Zstandard compression format.
It can be used, for example, to better understand the format,
or as the basis for a separate implementation of Zstandard decoder.

[__`decode_corpus`__](https://github.com/facebook/zstd/tree/dev/tests#decodecorpus---tool-to-generate-zstandard-frames-for-decoder-testing) :
This tool, stored in `/tests` directory, is able to generate random valid frames,
which is useful if you wish to test your decoder and verify it fully supports the specification.
Educational Decoder
===================

`zstd_decompress.c` is a self-contained implementation in C99 of a decoder,
according to the [Zstandard format specification].
While it does not implement as many features as the reference decoder,
such as the streaming API or content checksums, it is written to be easy to
follow and understand, to help understand how the Zstandard format works.
It's laid out to match the [format specification],
so it can be used to understand how complex segments could be implemented.
It also contains implementations of Huffman and FSE table decoding.

[Zstandard format specification]: https://github.com/facebook/zstd/blob/dev/doc/zstd_compression_format.md
[format specification]: https://github.com/facebook/zstd/blob/dev/doc/zstd_compression_format.md

`harness.c` provides a simple test harness around the decoder:

    harness <input-file> <output-file> [dictionary]

As an additional resource to be used with this decoder,
see the `decodecorpus` tool in the [tests] directory.
It generates valid Zstandard frames that can be used to verify
a Zstandard decoder implementation.
Note that to use the tool to verify this decoder implementation,
the --content-size flag should be set,
as this decoder does not handle streaming decoding,
and so it must know the decompressed size in advance.

[tests]: https://github.com/facebook/zstd/blob/dev/tests/
Zstandard wrapper for zlib
================================

The main objective of creating a zstd wrapper for [zlib](http://zlib.net/) is to allow a quick and smooth transition to zstd for projects already using zlib.

#### Required files

To build the zstd wrapper for zlib the following files are required:
- zlib.h
- a static or dynamic zlib library
- zlibWrapper/zstd_zlibwrapper.h
- zlibWrapper/zstd_zlibwrapper.c
- zlibWrapper/gz*.c files (gzclose.c, gzlib.c, gzread.c, gzwrite.c)
- zlibWrapper/gz*.h files (gzcompatibility.h, gzguts.h)
- a static or dynamic zstd library

The first two files are required by all projects using zlib and they are not included with the zstd distribution.
The further files are supplied with the zstd distribution.


#### Embedding the zstd wrapper within your project

Let's assume that your project that uses zlib is compiled with:
```gcc project.o -lz```

To compile the zstd wrapper with your project you have to do the following:
- change all references with `#include "zlib.h"` to `#include "zstd_zlibwrapper.h"`
- compile your project with `zstd_zlibwrapper.c`, `gz*.c` and a static or dynamic zstd library

The linking should be changed to:
```gcc project.o zstd_zlibwrapper.o gz*.c -lz -lzstd```


#### Enabling zstd compression within your project

After embedding the zstd wrapper within your project the zstd library is turned off by default.
Your project should work as before with zlib. There are two options to enable zstd compression:
- compilation with `-DZWRAP_USE_ZSTD=1` (or using `#define ZWRAP_USE_ZSTD 1` before `#include "zstd_zlibwrapper.h"`)
- using the `void ZWRAP_useZSTDcompression(int turn_on)` function (declared in `#include "zstd_zlibwrapper.h"`)

During decompression zlib and zstd streams are automatically detected and decompressed using a proper library.
This behavior can be changed using `ZWRAP_setDecompressionType(ZWRAP_FORCE_ZLIB)` what will make zlib decompression slightly faster.


#### Example
We have take the file `test/example.c` from [the zlib library distribution](http://zlib.net/) and copied it to [zlibWrapper/examples/example.c](examples/example.c).
After compilation and execution it shows the following results: 
```
zlib version 1.2.8 = 0x1280, compile flags = 0x65
uncompress(): hello, hello!
gzread(): hello, hello!
gzgets() after gzseek:  hello!
inflate(): hello, hello!
large_inflate(): OK
after inflateSync(): hello, hello!
inflate with dictionary: hello, hello!
```
Then we have changed `#include "zlib.h"` to `#include "zstd_zlibwrapper.h"`, compiled the [example.c](examples/example.c) file
with `-DZWRAP_USE_ZSTD=1` and linked with additional `zstd_zlibwrapper.o gz*.c -lzstd`.
We were forced to turn off the following functions: `test_flush`, `test_sync` which use currently unsupported features.
After running it shows the following results:
```
zlib version 1.2.8 = 0x1280, compile flags = 0x65
uncompress(): hello, hello!
gzread(): hello, hello!
gzgets() after gzseek:  hello!
inflate(): hello, hello!
large_inflate(): OK
inflate with dictionary: hello, hello!
```
The script used for compilation can be found at [zlibWrapper/Makefile](Makefile).


#### The measurement of performace of Zstandard wrapper for zlib

The zstd distribution contains a tool called `zwrapbench` which can measure speed and ratio of zlib, zstd, and the wrapper.
The benchmark is conducted using given filenames or synthetic data if filenames are not provided.
The files are read into memory and processed independently.
It makes benchmark more precise as it eliminates I/O overhead. 
Many filenames can be supplied as multiple parameters, parameters with wildcards or names of directories can be used as parameters with the -r option.
One can select compression levels starting from `-b` and ending with `-e`. The `-i` parameter selects minimal time used for each of tested levels.
With `-B` option bigger files can be divided into smaller, independently compressed blocks. 
The benchmark tool can be compiled with `make zwrapbench` using [zlibWrapper/Makefile](Makefile).


#### Improving speed of streaming compression

During streaming compression the compressor never knows how big is data to compress.
Zstandard compression can be improved by providing size of source data to the compressor. By default streaming compressor assumes that data is bigger than 256 KB but it can hurt compression speed on smaller data. 
The zstd wrapper provides the `ZWRAP_setPledgedSrcSize()` function that allows to change a pledged source size for a given compression stream.
The function will change zstd compression parameters what may improve compression speed and/or ratio.
It should be called just after `deflateInit()`or `deflateReset()` and before `deflate()` or `deflateSetDictionary()`. The function is only helpful when data is compressed in blocks. There will be no change in case of `deflateInit()` or `deflateReset()`  immediately followed by `deflate(strm, Z_FINISH)`
as this case is automatically detected.


#### Reusing contexts

The ordinary zlib compression of two files/streams allocates two contexts:
- for the 1st file calls `deflateInit`, `deflate`, `...`, `deflate`, `defalateEnd`
- for the 2nd file calls `deflateInit`, `deflate`, `...`, `deflate`, `defalateEnd`

The speed of compression can be improved with reusing a single context with following steps:
- initialize the context with `deflateInit`
- for the 1st file call `deflate`, `...`, `deflate`
- for the 2nd file call `deflateReset`, `deflate`, `...`, `deflate`
- free the context with `deflateEnd`

To check the difference we made experiments using `zwrapbench -ri6b6` with zstd and zlib compression (both at level 6).
The input data was decompressed git repository downloaded from https://github.com/git/git/archive/master.zip which contains 2979 files.
The table below shows that reusing contexts has a minor influence on zlib but it gives improvement for zstd.
In our example (the last 2 lines) it gives 4% better compression speed and 5% better decompression speed.

| Compression type                                  | Compression | Decompress.| Compr. size | Ratio |
| ------------------------------------------------- | ------------| -----------| ----------- | ----- |
| zlib 1.2.8                                        |  30.51 MB/s | 219.3 MB/s |     6819783 | 3.459 |
| zlib 1.2.8 not reusing a context                  |  30.22 MB/s | 218.1 MB/s |     6819783 | 3.459 |
| zlib 1.2.8 with zlibWrapper and reusing a context |  30.40 MB/s | 218.9 MB/s |     6819783 | 3.459 |
| zlib 1.2.8 with zlibWrapper not reusing a context |  30.28 MB/s | 218.1 MB/s |     6819783 | 3.459 |
| zstd 1.1.0 using ZSTD_CCtx                        |  68.35 MB/s | 430.9 MB/s |     6868521 | 3.435 |
| zstd 1.1.0 using ZSTD_CStream                     |  66.63 MB/s | 422.3 MB/s |     6868521 | 3.435 |
| zstd 1.1.0 with zlibWrapper and reusing a context |  54.01 MB/s | 403.2 MB/s |     6763482 | 3.488 |
| zstd 1.1.0 with zlibWrapper not reusing a context |  51.59 MB/s | 383.7 MB/s |     6763482 | 3.488 |


#### Compatibility issues
After enabling zstd compression not all native zlib functions are supported. When calling unsupported methods they put error message into `strm->msg` and return Z_STREAM_ERROR.

Supported methods:
- deflateInit
- deflate (with exception of Z_FULL_FLUSH, Z_BLOCK, and Z_TREES)
- deflateSetDictionary
- deflateEnd
- deflateReset
- deflateBound
- inflateInit
- inflate
- inflateSetDictionary
- inflateReset
- inflateReset2
- compress
- compress2
- compressBound
- uncompress
- gzip file access functions

Ignored methods (they do nothing):
- deflateParams

Unsupported methods:
- deflateCopy
- deflateTune
- deflatePending
- deflatePrime
- deflateSetHeader
- inflateGetDictionary
- inflateCopy
- inflateSync
- inflatePrime
- inflateMark
- inflateGetHeader
- inflateBackInit
- inflateBack
- inflateBackEnd
Projects for various integrated development environments (IDE)
==============================================================

#### Included projects

The following projects are included with the zstd distribution:
- `cmake` - CMake project contributed by Artyom Dymchenko
- `VS2005` - Visual Studio 2005 Project (this project has been moved to the contrib directory and will no longer be supported)
- `VS2008` - Visual Studio 2008 project
- `VS2010` - Visual Studio 2010 project (which also works well with Visual Studio 2012, 2013, 2015)
- `VS_scripts` - command line scripts prepared for Visual Studio compilation without IDE


#### How to compile zstd with Visual Studio

1. Install Visual Studio e.g. VS 2015 Community Edition (it's free).
2. Download the latest version of zstd from https://github.com/facebook/zstd/releases
3. Decompress ZIP archive.
4. Go to decompressed directory then to `projects` then `VS2010` and open `zstd.sln`
5. Visual Studio will ask about converting VS2010 project to VS2015 and you should agree.
6. Change `Debug` to `Release` and if you have 64-bit Windows change also `Win32` to `x64`.
7. Press F7 on keyboard or select `BUILD` from the menu bar and choose `Build Solution`.
8. If compilation will be fine a compiled executable will be in `projects\VS2010\bin\x64\Release\zstd.exe`


#### Projects available within zstd.sln

The Visual Studio solution file `visual\VS2010\zstd.sln` contains many projects that will be compiled to the
`visual\VS2010\bin\$(Platform)_$(Configuration)` directory. For example `zstd` set to `x64` and
`Release` will be compiled to `visual\VS2010\bin\x64_Release\zstd.exe`. The solution file contains the
following projects:

- `zstd` : Command Line Utility, supporting gzip-like arguments
- `datagen` : Synthetic and parametrable data generator, for tests
- `fullbench`  : Precisely measure speed for each zstd inner functions
- `fuzzer` : Test tool, to check zstd integrity on target platform 
- `libzstd` : A static ZSTD library compiled to `libzstd_static.lib`
- `libzstd-dll` : A dynamic ZSTD library (DLL) compiled to `libzstd.dll` with the import library `libzstd.lib`
- `fullbench-dll` : The fullbench program compiled with the import library; the executable requires ZSTD DLL


#### Using ZSTD DLL with Microsoft Visual C++ project

The header file `lib\zstd.h` and the import library
`visual\VS2010\bin\$(Platform)_$(Configuration)\libzstd.lib` are required to compile
a project using Visual C++.

1. The path to header files should be added to `Additional Include Directories` that can
   be found in Project Properties of Visual Studio IDE in the `C/C++` Property Pages on the `General` page.
2. The import library has to be added to `Additional Dependencies` that can
   be found in Project Properties in the `Linker` Property Pages on the `Input` page.
   If one will provide only the name `libzstd.lib` without a full path to the library
   then the directory has to be added to `Linker\General\Additional Library Directories`.

The compiled executable will require ZSTD DLL which is available at
`visual\VS2010\bin\$(Platform)_$(Configuration)\libzstd.dll`. 
Command line scripts for Visual Studio compilation without IDE
==============================================================

Here are a few command lines for reference :

### Build with Visual Studio 2013 for msvcr120.dll

Running the following command will build both the `Release Win32` and `Release x64` versions:
```batch
build.VS2013.cmd
```
The result of each build will be in the corresponding `bin\Release\{ARCH}\` folder.

If you want to only need one architecture:
- Win32: `build.generic.cmd VS2013 Win32 Release v120`
- x64: `build.generic.cmd VS2013 x64 Release v120`

If you want a Debug build:
- Win32: `build.generic.cmd VS2013 Win32 Debug v120`
- x64: `build.generic.cmd VS2013 x64 Debug v120`

### Build with Visual Studio 2015 for msvcr140.dll

Running the following command will build both the `Release Win32` and `Release x64` versions:
```batch
build.VS2015.cmd
```
The result of each build will be in the corresponding `bin\Release\{ARCH}\` folder.

If you want to only need one architecture:
- Win32: `build.generic.cmd VS2015 Win32 Release v140`
- x64: `build.generic.cmd VS2015 x64 Release v140`

If you want a Debug build:
- Win32: `build.generic.cmd VS2015 Win32 Debug v140`
- x64: `build.generic.cmd VS2015 x64 Debug v140`

### Build with Visual Studio 2015 for msvcr120.dll

This capability is offered through `build.generic.cmd` using proper arguments:

**For Win32**
```batch
build.generic.cmd VS2015 Win32 Release v120
```
The result of the build will be in the `bin\Release\Win32\` folder.

**For x64**
```batch
build.generic.cmd VS2015 x64 Release v120
```
The result of the build will be in the `bin\Release\x64\` folder.

If you want Debug builds, replace `Release` with `Debug`.

### Build with Visual Studio 2017

`build.VS2017.cmd`, contributed by [@HaydnTrigg](https://github.com/HaydnTrigg),
will build both the `Release Win32` and `Release x64` versions
of the first VS2017 variant it finds, in this priority order :
Enterprise > Professional > Community

Alternatively, it's possible to target a specific version,
using appropriate script, such as `build.VS2017Enterprise.cmd` for example.
# yaml-cpp [![Build Status](https://travis-ci.org/jbeder/yaml-cpp.svg?branch=master)](https://travis-ci.org/jbeder/yaml-cpp) [![Documentation](https://codedocs.xyz/jbeder/yaml-cpp.svg)](https://codedocs.xyz/jbeder/yaml-cpp/)

yaml-cpp is a [YAML](http://www.yaml.org/) parser and emitter in C++ matching the [YAML 1.2 spec](http://www.yaml.org/spec/1.2/spec.html).

To get a feel for how it can be used, see the [Tutorial](https://github.com/jbeder/yaml-cpp/wiki/Tutorial) or [How to Emit YAML](https://github.com/jbeder/yaml-cpp/wiki/How-To-Emit-YAML). For the old API (version < 0.5.0), see [How To Parse A Document](https://github.com/jbeder/yaml-cpp/wiki/How-To-Parse-A-Document-(Old-API)).

# Problems? #

If you find a bug, post an [issue](https://github.com/jbeder/yaml-cpp/issues)! If you have questions about how to use yaml-cpp, please post it on http://stackoverflow.com and tag it [`yaml-cpp`](http://stackoverflow.com/questions/tagged/yaml-cpp).

# How to Build #

yaml-cpp uses [CMake](http://www.cmake.org) to support cross-platform building. The basic steps to build are:

1. Download and install [CMake](http://www.cmake.org) (Resources -> Download).

**Note:** If you don't use the provided installer for your platform, make sure that you add CMake's bin folder to your path.

2. Navigate into the source directory, and type:

```
mkdir build
cd build
```

3. Run CMake. The basic syntax is:

```
cmake [-G generator] [-DBUILD_SHARED_LIBS=ON|OFF] ..
```

  * The `generator` is whatever type of build system you'd like to use. To see a full list of generators on your platform, just run `cmake` (with no arguments). For example:
    * On Windows, you might use "Visual Studio 12 2013" to generate a Visual Studio 2013 solution or "Visual Studio 14 2015 Win64" to generate a 64-bit Visual Studio 2015 solution.
    * On OS X, you might use "Xcode" to generate an Xcode project
    * On a UNIX-y system, simply omit the option to generate a makefile

  * yaml-cpp defaults to building a static library, but you may build a shared library by specifying `-DBUILD_SHARED_LIBS=ON`.

  * For more options on customizing the build, see the [CMakeLists.txt](https://github.com/jbeder/yaml-cpp/blob/master/CMakeLists.txt) file.

4. Build it!

5. To clean up, just remove the `build` directory.

# Recent Release #

[yaml-cpp 0.6.0](https://github.com/jbeder/yaml-cpp/releases/tag/yaml-cpp-0.6.0) has been released! This release requires C++11, and no longer depends on Boost.

[yaml-cpp 0.3.0](https://github.com/jbeder/yaml-cpp/releases/tag/release-0.3.0) is still available if you want the old API.

**The old API will continue to be supported, and will still receive bugfixes!** The 0.3.x and 0.4.x versions will be old API releases, and 0.5.x and above will all be new API releases.




     ==================================================================
     ======= Intel(R) Decimal Floating-Point Math Library v2.1 ========
     ==================================================================

                                                        August 15, 2011


     ******************************************************************
     *** To report issues, please send email to decimalfp@intel.com ***
     ******************************************************************

     Release History:
     ================
        Jul 2009 - Version 1.0 - implemented all the mandatory functions 
                   from the IEEE Standard 754-2008
        Jun 2011 - Version 2.0 - implemented also the functions 
                   recommended in the ISO/IEC Technical Report 24732, 
                   'Extension for the programming language C to support 
                   decimal floating-point arithmetic'
        Aug 2011 - Version 2.0 Update 1 - fixed a small issue in fma128


  1. INTRODUCTION
  ===============

  This package contains the release 2.0 of the Intel(R) Decimal
Floating-Point Math Library, conforming to the IEEE Standard 754-2008 for
Floating-Point Arithmetic. This is an extension of Release 1.0 of 2009.

  The library implements the functions defined for decimal floating-point
arithmetic operations in the IEEE Standard 754-2008 for Floating-Point
Arithmetic, which is a revision of the IEEE Standard 754-1985 for Binary
Floating-Point Arithmetic.

The IEEE Standard 754-2008 for Floating-Point Arithmetic supports two
encoding formats: the decimal encoding format, and the binary encoding format.
The Intel(R) Decimal Floating-Point Math Library supports primarily the binary
encoding format for decimal floating-point values, but the decimal encoding
format is supported too in the library, by means of conversion functions
between the two encoding formats.

  Release 2.0 of the library contained in this package implements all
the operations mandated by the IEEE Standard 754-2008. Alternate exception
handling (not a mandatory feature) is not supported currently in the library,
but the design facilitates adding it in the future. It is worth noting that
several useful functions (not part of the IEEE 754-2008 definition) are
provided in LIBRARY/bid_round.c. They can be used to round a q-digit decimal
integer number represented in binary to q - x digits (1 <= x <= q - 1).

  For operations involving integer operands or results, the library supports
signed and unsigned 8-, 16-, 32-, and 64-bit integers.

  Release 2.0 adds transcendental functions (supported in 128-bit, 64-bit, 
and 32-bit decimal formats), including the ones specified in the technical 
report on decimal arithmetic ISO/IEC TR 24732 (available from www.iso.org).


  2. PACKAGE CONTENTS
  ===================

  This package contains:

  - eula.txt, a copy of the end user license agreement that applies to
    everything in this package

  - this README FILE

  - the LIBRARY subdirectory with all the source files necessary to build the
    library, and a README file which specifies how to build the library
    in Linux**, HP-UX**, Windows***, and other operating systems; a small set
    of command files (RUNLINUX, RUNWINDOWS, etc.) can be used to build the
    library with different options

  - the TESTS subdirectory with source and input files necessary to build and
    run a reduced set of tests for the library, and a README
    file which specifies how to build and run these tests;
    the test program will print the number of errors detected;
    note that tests involving 80-bit binary floating-point values (these are
    only conversions to and from decimal floating-point formats) are skipped
    if the 80-bit floating-point data type is not supported; a small set
    of command files (RUNLINUX, RUNWINDOWS, etc.) can be used to build and
    run the tests with different options

  - the EXAMPLES subdirectory containing eight examples of calls to library
    functions with various combinations of build options (see Section 8
    below); a README file is included; a small set of command files (RUNLINUX,
    RUNWINDOWS, etc.) can be used to build and run the examples with different
    options

  3. FUNCTION NAMES
  =================

  The function names used in the library are not identical to the names from
the IEEE Standard 754-2008 for Floating-Point Arithmetic. The mapping between
the two sets is given in Section 10 below. The function names can be changed
by editing the #define statements at the beginning of bid_conf.h.


  4. LIBRARY BUILD OPTIONS
  ========================

  The API for the library functions is intended to support constant modes,
global dynamic modes, and scoped dynamic modes. It should be convenient for
compilers with various requirements, even where default modes and no flag
tests can be assumed, as in C99 FENV_ACCESS OFF.

  Three build options are provided, that can be set by editing
LIBRARY/bid_conf.h, or (more conveniently) can be set on the compile
command line.

  (a) Function arguments and return values can be passed by reference if
DECIMAL_CALL_BY_REFERENCE is set to 1, or by value otherwise. However, the
floating-point status flags argument is passed by reference even when
DECIMAL_CALL_BY_REFERENCE is 0, unless it is stored in a global variable
(see (c) below).

  (b) The value of the rounding mode can be passed by reference or by value,
or it can be stored in a global variable if DECIMAL_GLOBAL_ROUNDING is
set to 1.
  If DECIMAL_GLOBAL_ROUNDING is set to 1 then the rounding mode is stored
in a global variable that must be declared as

        _IDEC_round __bid_IDEC_glbround;

In this case __bid_IDEC_glbround is a fixed name that *must* be used (but
it can be changed by editing the corresponding #define in bid_conf.h).  Its
initial value should be ROUNDING_TO_NEAREST (or an equivalent value with a name
chosen by the user, as shown in code samples from EXAMPLES where
_IDEC_nearesteven is used). The _IDEC_round type name can be different
(but equivalent), chosen by the user.

  (c) The value of the exception status flags is passed by reference if
they are not represented by a global variable, or it can be stored in a
global variable if DECIMAL_GLOBAL_EXCEPTION_FLAGS is set to 1.
  If DECIMAL_GLOBAL_EXCEPTION_FLAGS is set to 1 then the exception status
flags are stored in a global variable that must be declared as

        _IDEC_flags __bid_IDEC_glbflags;

In this case __bid_IDEC_glbflags is a fixed name that *must* be used but
it can be changed by editing the corresponding #define in bid_conf.h). Its
initial value should be EXACT_STATUS (or an equivalent value with a name chosen
by the user, as shown in code samples from EXAMPLES where _IDEC_allflagsclear
is used). The _IDEC_flags type name can be different (but equivalent),
chosen by the user.

  The three build options supported in this release are selected on the
'make' command line when building the library in LIBRARY and the tests in
TESTS using the makefile-s provided here (so editing bid_conf.h is not
necessary). For example when using the Intel(R) C++ Compiler in Linux**:

    make CC=icc CALL_BY_REF=0 GLOBAL_RND=0 GLOBAL_FLAGS=0 UNCHANGED_BINARY_FLAGS=0

selects parameter passing by value; the rounding mode is a parameter
passed to each function that requires it; the status flags are passed
as a parameter to functions that may modify them (note however that the
status flags represent an exception in that the CALL_BY_REF setting
is ignored - if not global, they are always passed by reference); the
decimal operations may change the inexact binary status flag.

  Another example, when using the Intel(R) C++ Compiler in Windows*** is:

    nmake -fmakefile.mak CC=icl CALL_BY_REF=1 GLOBAL_RND=1 GLOBAL_FLAGS=1 UNCHANGED_BINARY_FLAGS=1

where parameters are passed by reference; the rounding mode is a global
variable; the status flags are stored in a global variable; the
decimal operations will not change the inexact binary status flag.


  5. FUNCTION PROTOTYPES
  ======================

  Function prototypes are provided in LIBRARY/bid_functions.h (starting at
line 396 if parameters are passed by reference, and at line 2981 if they
are passed by value).


  6. TESTING
  ==========

  The library was tested on several different platforms (IA-32 Architecture, 
Intel(R) 64, and IA-64 Architecture running Linux**, Windows***, HP-UX**, 
Solaris**, and OSX**).  For example in Linux** icc (Intel(R) C++ Compiler 9.1 
or newer) and gcc** were used. In Windows*** icl (Intel(R) C++ Compiler 9.1 
or newer) and cl (Microsoft*** Visual C++ Compiler) were used. For each of 
these combinations eight combinations of parameter passing method and global 
or local rounding mode and status flags were tested.

  In limited situations, it is possible for incorrect compiler behavior to 
lead to incorrect results in the Intel(r) Decimal Floating-Point Math Library. 
For example, results of round-to-integer functions are incorrect when the 
library is built using gcc 4.2/4.3. Also, some gcc versions in an IA-32 
Linux environment cause slightly incorrect results in a few corner cases for 
the 64-bit decimal square root. (This is not an exhaustive list.)



  7. CHANGES SINCE THE V1.0 UPDATE 1 RELEASE
  ==========================================

  Support was added for decimal transcendental functions (see Section 11 
for details).  A small number of non-critical bugs were fixed.


  8. USAGE EXAMPLES
  =================

  Eight usage examples are given in the EXAMPLES subdirectory, which illustrate
calls to library functions with various combinations of build options (see
Section 4 above). A README file is included. Note that these examples do not
use any include files from the library: the necessary data types are defined
instead directly in the user-defined decimal.h. However, if the rounding mode
or exception status flags are stored in global variables, then these must have
the fixed names of _IDEC_glbround and _IDEC_glbflags.
  Alternatively - and this is the preferred method, one could use the data
types defined in the library by including two header files (and in this case
DECIMAL_CALL_BY_REFERENCE, DECIMAL_GLOBAL_ROUNDING, and
DECIMAL_GLOBAL_EXCEPTION_FLAGS would have to be properly defined not only when
building the library, but also for the application calling the library
functions):

        #include "../LIBRARY/bid_conf.h"
        #include "../LIBRARY/bid_functions.h"

Such an example is represented by the readtest program in TESTS/readtest.c.

  9. DECIMAL AND BINARY STATUS FLAGS
  ==================================

  The IEEE Standard 754-2008 specifies distinct rounding modes for binary
and for decimal floating-point operations. However, the floating-point status
flags may be identical for decimal and binary computations. In this
implementation of the decimal arithmetic, the decimal floating-point status
flags are kept separate from the binary flags. Still, it is possible to merge
the two sets (outside the library).
  One issue that needs to be pointed out is that the current implementation of
the decimal floating-point library may set the binary inexact status flag for
certain operations: division, square root, and several other operations where
integers are converted to floating-point values, and the conversion
is inexact. In order to avoid setting the binary inexact flag by decimal
functions, uncomment the following line in bid_conf.h
prior to building the library:
        // #define UNCHANGED_BINARY_STATUS_FLAGS

  10. MAPPING OF IEEE 754-2008 NAMES TO INTEL (R) DECIMAL FLOATING-POINT MATH
                          LIBRARY FUNCTION NAMES
  =========================================================================

Operand and result types are included, where:
        BID64 =  the 64-bit decimal floating-point format using the binary
            encoding; this becomes BID_UINT64 in the library
        BID128 =  the 128-bit decimal floating-point format using the binary
            encoding ; this becomes BID_UINT128 in the library
        binary32 = 32-bit binary floating-point data format
        binary64 = 64-bit binary floating-point data format
        binary80 = 80-bit binary floating-point data format
        binary128 = 128-bit binary floating-point data format
        string = char *
        boolean = int
        enum = int
        _IDEC_flags = int
        _IDEC_round = int

The library function names shown here can be changed by editing #define
statements in bid_conf.h.

================================================================================
IEEE 754-2008 Name                      Opd1   Opd2   Opd3   Result
                                                Intel(R) DFP Math Library Name
================================================================================
roundToIntegralTiesToEven           BID64                BID64
                                           __bid64_round_integral_nearest_even
                                    BID128               BID128
                                           __bid128_round_integral_nearest_even
roundToIntegralTiesToAway           BID64                BID64
                                           __bid64_round_integral_nearest_away
                                    BID128               BID128
                                           __bid128_round_integral_nearest_away
roundToIntegralTiesTowardZero       BID64                BID64
                                           __bid64_round_integral_zero
                                    BID128               BID128
                                           __bid128_round_integral_zero
roundToIntegralTiesTowardPositive   BID64                BID64
                                           __bid64_round_integral_positive
                                    BID128               BID128
                                           __bid128_round_integral_positive
roundToIntegralTiesTowardNegative   BID64                BID64
                                           __bid64_round_integral_negative
                                    BID128               BID128
                                           __bid128_round_integral_negative
roundToIntegralExact                BID64                BID64
                                           __bid64_round_integral_exact
                                    BID128               BID128
                                           __bid128_round_integral_exact
nextUp                              BID64                BID64
                                           __bid64_nextup
                                    BID128               BID128
                                           __bid128_nextup
nextDown                            BID64                BID64
                                           __bid64_nextdown
                                    BID128               BID128
                                           __bid128_nextdown
N/A                                 BID64  BID64         BID64
                                           __bid64_nextafter
                                    BID128 BID128        BID128
                                           __bid128_nextafter
remainder                           BID64  BID64         BID64
                                           __bid64_rem
                                    BID128 BID128        BID128
                                           __bid128_rem
minNum                              BID64  BID64         BID64
                                           __bid64_minnum
                                    BID128 BID128        BID128
                                           __bid128_minnum
maxNum                              BID64  BID64         BID64
                                           __bid64_maxnum
                                    BID128 BID128        BID128
                                           __bid128_maxnum
minNumMag                           BID64  BID64         BID64
                                           __bid64_minnum_mag
                                    BID128 BID128        BID128
                                           __bid128_minnum_mag
maxNumMag                           BID64  BID64         BID64
                                           __bid64_maxnum_mag
                                    BID128 BID128        BID128
                                           __bid128_maxnum_mag
quantize                            BID64  BID64         BID64
                                           __bid64_quantize
                                    BID128 BID128        BID128
                                           __bid128_quantize
logB                                BID64                BID64
                                           __bid64_ilogb
                                    BID128               BID128
                                           __bid128_ilogb
scaleB                              BID64  BID64         BID64
                                           __bid64_scalbn
                                    BID128 BID128        BID128
                                           __bid128_scalbn
addition                            BID64  BID64         BID64
                                           __bid64_add
                                    BID128 BID128        BID128
                                           __bid128_add
subtraction                         BID64  BID64         BID64
                                           __bid64_sub
                                    BID128 BID128        BID128
                                           __bid128_sub
multiplication                      BID64  BID64         BID64
                                           __bid64_mul
                                    BID128 BID128        BID128
                                           __bid128_mul
division                            BID64  BID64         BID64
                                           __bid64_div
                                    BID128 BID128        BID128
                                           __bid128_div
squareRoot                          BID64                BID64
                                           __bid64_sqrt
                                    BID128               BID128
                                           __bid128_sqrt
fusedMultiplyAdd                    BID64  BID64  BID64  BID64
                                           __bid64_fma
                                    BID128 BID128 BID128 BID128
                                           __bid128_fma
convertFromInt                      int32                BID64
                                           __bid64_from_int32
                                    uint32               BID64
                                           __bid64_from_uint32
                                    int64                BID64
                                           __bid64_from_int64
                                    uint64               BID64
                                           __bid64_from_uint64
                                    int32                BID128
                                           __bid128_from_int32
                                    uint32               BID128
                                           __bid128_from_uint32
                                    int64                BID128
                                           __bid128_from_int64
                                    uint64               BID128
                                           __bid128_from_uint64
convertToIntegerTiesToEven          BID64                int32
                                           __bid64_to_int32_rnint
                                    BID64                uint32
                                           __bid64_to_uint32_rnint
                                    BID64                int64
                                           __bid64_to_int64_rnint
                                    BID64                uint64
                                           __bid64_to_uint64_rnint
                                    BID128               int32
                                           __bid128_to_int32_rnint
                                    BID128               uint32
                                           __bid128_to_uint32_rnint
                                    BID128               int64
                                           __bid128_to_int64_rnint
                                    BID128               uint64
                                           __bid128_to_uint64_rnint
convertToIntegerTowardZero          BID64                int32
                                           __bid64_to_int32_int
                                    BID64                uint32
                                           __bid64_to_uint32_int
                                    BID64                int64
                                           __bid64_to_int64_int
                                    BID64                uint64
                                           __bid64_to_uint64_int
                                    BID128               int32
                                           __bid128_to_int32_int
                                    BID128               uint32
                                           __bid128_to_uint32_int
                                    BID128               int64
                                           __bid128_to_int64_int
                                    BID128               uint64
                                           __bid128_to_uint64_int
convertToIntegerTowardPositive      BID64                int32
                                           __bid64_to_int32_ceil
                                    BID64                uint32
                                           __bid64_to_uint32_ceil
                                    BID64                int64
                                           __bid64_to_int64_ceil
                                    BID64                uint64
                                           __bid64_to_uint64_ceil
                                    BID128               int32
                                           __bid128_to_int32_ceil
                                    BID128               uint32
                                           __bid128_to_uint32_ceil
                                    BID128               int64
                                           __bid128_to_int64_ceil
                                    BID128               uint64
                                           __bid128_to_uint64_ceil
convertToIntegerTowardNegative      BID64                int32
                                           __bid64_to_int32_floor
                                    BID64                int32
                                           __bid64_to_uint32_floor
                                    BID64                int64
                                           __bid64_to_int64_floor
                                    BID64                uint64
                                           __bid64_to_uint64_floor
                                    BID128               int32
                                           __bid128_to_int32_floor
                                    BID128               uint32
                                           __bid128_to_uint32_floor
                                    BID128               int64
                                           __bid128_to_int64_floor
                                    BID128               uint64
                                           __bid128_to_uint64_floor
convertToIntegerTiesToAway          BID64                int32
                                           __bid64_to_int32_rninta
                                    BID64                uint32
                                           __bid64_to_uint32_rninta
                                    BID64                int64
                                           __bid64_to_int64_rninta
                                    BID64                uint64
                                           __bid64_to_uint64_rninta
                                    BID128               int32
                                           __bid128_to_int32_rninta
                                    BID128               uint32
                                           __bid128_to_uint32_rninta
                                    BID128               int64
                                           __bid128_to_int64_rninta
                                    BID128               uint64
                                           __bid128_to_uint64_rninta
convertToIntegerExactTiesToEven     BID64                int32
                                           __bid64_to_int32_xrnint
                                    BID64                uint32
                                           __bid64_to_uint32_xrnint
                                    BID64                int64
                                           __bid64_to_int64_xrnint
                                    BID64                uint64
                                           __bid64_to_uint64_xrnint
                                    BID128               int32
                                           __bid128_to_int32_xrnint
                                    BID128               uint32
                                           __bid128_to_uint32_xrnint
                                    BID128               int64
                                           __bid128_to_int64_xrnint
                                    BID128               uint64
                                           __bid128_to_uint64_xrnint
convertToIntegerExactTowardZero     BID64                int32
                                           __bid64_to_int32_xint
                                    BID64                uint32
                                           __bid64_to_uint32_xint
                                    BID64                int64
                                           __bid64_to_int64_xint
                                    BID64                uint64
                                           __bid64_to_uint64_xint
                                    BID128               int32
                                           __bid128_to_int32_xint
                                    BID128               uint32
                                           __bid128_to_uint32_xint
                                    BID128               int64
                                           __bid128_to_int64_xint
                                    BID128               uint64
                                           __bid128_to_uint64_xint
convertToIntegerExactTowardPositive BID64                int32
                                           __bid64_to_int32_xceil
                                    BID64                uint32
                                           __bid64_to_uint32_xceil
                                    BID64                int64
                                           __bid64_to_int64_xceil
                                    BID64                uint64
                                           __bid64_to_uint64_xceil
                                    BID128               int32
                                           __bid128_to_int32_xceil
                                    BID128               uint32
                                           __bid128_to_uint32_xceil
                                    BID128               int64
                                           __bid128_to_int64_xceil
                                    BID128               uint64
                                           __bid128_to_uint64_xceil
convertToIntegerExactTowardNegative BID64                int32
                                           __bid64_to_int32_xfloor
                                    BID64                uint32
                                           __bid64_to_uint32_xfloor
                                    BID64                int64
                                           __bid64_to_int64_xfloor
                                    BID64                uint64
                                           __bid64_to_uint64_xfloor
                                    BID128               int32
                                           __bid128_to_int32_xfloor
                                    BID128               uint32
                                           __bid128_to_uint32_xfloor
                                    BID128               int64
                                           __bid128_to_int64_xfloor
                                    BID128               uint64
                                           __bid128_to_uint64_xfloor
convertToIntegerExactTiesToAway     BID64                int32
                                           __bid64_to_int32_xrninta
                                    BID64                uint32
                                           __bid64_to_uint32_xrninta
                                    BID64                int64
                                           __bid64_to_int64_rninta
                                    BID64                uint64
                                           __bid64_to_uint64_xrninta
                                    BID128               int32
                                           __bid128_to_int32_xrninta
                                    BID128               uint32
                                           __bid128_to_uint32_xrninta
                                    BID128               int64
                                           __bid128_to_int64_xrninta
                                    BID128               uint64
                                           __bid128_to_uint64_xrninta
convert                             BID32                BID64
                                           __bid32_to_bid64
                                    BID32                BID128
                                           __bid32_to_bid128
                                    BID32                bin32
                                           __bid32_to_binary32
                                    BID32                bin64
                                           __bid32_to_binary64
                                    BID32                bin80
                                           __bid32_to_binary80
                                    BID32                bin128
                                           __bid32_to_binary128
                                    BID64                BID32
                                           __bid64_to_bid32
                                    BID64                BID128
                                           __bid64_to_bid128
                                    BID64                bin32
                                           __bid64_to_binary32
                                    BID64                bin64
                                           __bid64_to_binary64
                                    BID64                bin80
                                           __bid64_to_binary80
                                    BID64                bin128
                                           __bid64_to_binary128
                                    BID128               BID32
                                           __bid128_to_bid32
                                    BID128               BID64
                                           __bid128_to_bid64
                                    BID128               bin32
                                           __bid128_to_binary32
                                    BID128               bin64
                                           __bid128_to_binary64
                                    BID128               bin80
                                           __bid128_to_binary80
                                    BID128               bin128
                                           __bid128_to_binary128
                                    bin32                BID32
                                           __binary32_to_bid32
                                    bin32                BID64
                                           __binary32_to_bid64
                                    bin32                BID128
                                           __binary32_to_bid128
                                    bin64                BID32
                                           __binary64_to_bid32
                                    bin64                BID64
                                           __binary64_to_bid64
                                    bin64                BID128
                                           __binary64_to_bid128
                                    bin80                BID32
                                           __binary80_to_bid32
                                    bin80                BID64
                                           __binary80_to_bid64
                                    bin80                BID128
                                           __binary80_to_bid128
                                    bin128               BID32
                                           __binary128_to_bid32
                                    bin128               BID64
                                           __binary128_to_bid64
                                    bin128               BID128
                                           __binary128_to_bid128
convertFromDecimalCharacter         string               BID64
                                           __bid64_from_string
                                    string               BID128
                                           __bid128_from_string
convertToDecimalCharacter           BID64                string
                                           __bid64_to_string
                                    BID128               string
                                           __bid128_to_string
copy                                BID64                BID64
                                           __bid64_copy
                                    BID128               BID128
                                           __bid128_copy
negate                              BID64                BID64
                                           __bid64_negate
                                    BID128               BID128
                                           __bid128_negate
abs                                 BID64                BID64
                                           __bid64_abs
                                    BID128               BID128
                                           __bid128_abs
copySign                            BID64  BID64         BID64
                                           __bid64_copySign
                                    BID128 BID128        BID128
                                           __bid128_copySign
encodeDecimal                       BID32                DPD32
                                           __bid_to_dpd32
                                    BID64                DPD64
                                           __bid_to_dpd64
                                    BID128               DPD128
                                           __bid_to_dpd128
decodeDecimal                       DPD32                BID32
                                           __bid_dpd_to_bid32
                                    DPD64                BID64
                                           __bid_dpd_to_bid64
                                    DPD128               BID128
                                           __bid_dpd_to_bid128
compareQuietEqual                   BID64  BID64         boolean
                                           __bid64_quiet_equal
                                    BID128 BID128        boolean
                                           __bid128_quiet_equal
compareQuietGreater                 BID64  BID64         boolean
                                           __bid64_quiet_greater
                                    BID128 BID128        boolean
                                           __bid128_quiet_greater
compareQuietGreaterEqual            BID64  BID64         boolean
                                           __bid64_quiet_greater_equal
                                    BID128 BID128        boolean
                                           __bid128_quiet_greater_equal
compareQuietGreaterUnordered        BID64  BID64         boolean
                                           __bid64_quiet_greater_unordered
                                    BID128 BID128        boolean
                                           __bid128_quiet_greater_unordered
compareQuietLess                    BID64  BID64         boolean
                                           __bid64_quiet_less
                                    BID128 BID128        boolean
                                           __bid128_quiet_less
compareQuietLessEqual               BID64  BID64         boolean
                                           __bid64_quiet_less_equal
                                    BID128 BID128        boolean
                                           __bid128_quiet_less_equal
compareQuietLessUnordered           BID64  BID64         boolean
                                           __bid64_quiet_less_unordered
                                    BID128 BID128        boolean
                                           __bid128_quiet_less_unordered
compareQuietNotEqual                BID64  BID64         boolean
                                           __bid64_quiet_not_equal
                                    BID128 BID128        boolean
                                           __bid128_quiet_not_equal
compareQuietNotGreater              BID64  BID64         boolean
                                           __bid64_quiet_not_greater
                                    BID128 BID128        boolean
                                           __bid128_quiet_not_greater
compareQuietNotLess                 BID64  BID64         boolean
                                           __bid64_quiet_not_less
                                    BID128 BID128        boolean
                                           __bid128_quiet_not_less
compareQuietOrdered                 BID64  BID64         boolean
                                           __bid64_quiet_ordered
                                    BID128 BID128        boolean
                                           __bid128_quiet_ordered
compareQuietUnordered               BID64  BID64         boolean
                                           __bid64_quiet_unordered
                                    BID128 BID128        boolean
                                           __bid128_quiet_unordered
compareSignalingEqual               BID64  BID64         boolean
                                           __bid64_signaling_equal (not currently implemented)
                                    BID128 BID128        boolean
                                           __bid128_signaling_equal (not currently implemented)
compareSignalingGreater             BID64  BID64         boolean
                                           __bid64_signaling_greater
                                    BID128 BID128        boolean
                                           __bid128_signaling_greater
compareSignalingGreaterEqual        BID64  BID64         boolean
                                           __bid64_signaling_greater_equal
                                    BID128 BID128        boolean
                                           __bid128_signaling_greater_equal
compareSignalingGreaterUnordered    BID64  BID64         boolean
                                           __bid64_signaling_greater_unordered
                                    BID128 BID128        boolean
                                           __bid128_signaling_greater_unordered
compareSignalingLess                BID64  BID64         boolean
                                           __bid64_signaling_less
                                    BID128 BID128        boolean
                                           __bid128_signaling_less
compareSignalingLessEqual           BID64  BID64         boolean
                                           __bid64_signaling_less_equal
                                    BID128 BID128        boolean
                                           __bid128_signaling_less_equal
compareSignalingLessUnordered       BID64  BID64         boolean
                                           __bid64_signaling_less_unordered
                                    BID128 BID128        boolean
                                           __bid128_signaling_less_unordered
compareSignalingNotEqual            BID64  BID64         boolean
                                           __bid64_signaling_not_equal (not currently implemented)
                                    BID128 BID128        boolean
                                           __bid128_signaling_not_equal (not currently implemented)
compareSignalingNotGreater          BID64  BID64         boolean
                                           __bid64_signaling_not_greater
                                    BID128 BID128        boolean
                                           __bid128_signaling_not_greater
compareSignalingNotLess             BID64  BID64         boolean
                                           __bid64_signaling_not_less
                                    BID128 BID128        boolean
                                           __bid128_signaling_not_less
N/A                                 IDEC_flags *IDEC_flags
                                           __bid_signalException
is754version1985                                         int
                                           __bid_is754
is754version2008                                         int
                                           __bid_is754R
isSignMinus                         BID64                boolean
                                           __bid64_isSigned
                                    BID128               boolean
                                           __bid128_isSigned
isNormal                            BID64                boolean
                                           __bid64_isNormal
                                    BID128               boolean
                                           __bid128_isNormal
isFinite                            BID64                boolean
                                           __bid64_isFinite
                                    BID128               boolean
                                           __bid128_isFinite
isZero                              BID64                boolean
                                           __bid64_isZero
                                    BID128               boolean
                                           __bid128_isZero
isSubnormal                         BID64                boolean
                                           __bid64_isSubnormal
                                    BID128               boolean
                                           __bid128_isSubnormal
isInfinite                          BID64                boolean
                                           __bid64_isInf
                                    BID128               boolean
                                           __bid128_isInf
isNaN                               BID64                boolean
                                           __bid64_isNaN
                                    BID128               boolean
                                           __bid128_isNaN
isSignaling                         BID64                boolean
                                           __bid64_isSignaling
                                    BID128               boolean
                                           __bid128_isSignaling
isCanonical                         BID64                boolean
                                           __bid64_isCanonical
                                    BID128               boolean
                                           __bid128_isCanonical
radix                               BID64                boolean
                                           __bid64_radix
                                    BID128               boolean
                                           __bid128_radix
class                               BID64                enum
                                           __bid64_class
                                    BID128               enum
                                           __bid128_class
totalOrder                          BID64  BID64         boolean
                                           __bid64_totalOrder
                                    BID128 BID128        boolean
                                           __bid128_totalOrder
totalOrderMag                       BID64  BID64         boolean
                                           __bid64_totalOrderMag
                                    BID128 BID128        boolean
                                           __bid128_totalOrderMag
sameQuantum                         BID64  BID64         boolean
                                           __bid64_sameQuantum
                                    BID128 BID128        boolean
                                           __bid128_sameQuantum
lowerFlags                          _IDEC_flags
                                           __bid_lowerFlags
testFlags                           _IDEC_flags          boolean
                                           __bid_testFlags
testSavedFlags                      _IDEC_flags _IDEC_flags boolean
                                           __bid_testSavedFlags
restoreFlags                        _IDEC_flags _IDEC_flags
                                           __bid_restoreFlags
saveAllFlags                        _IDEC_flags         IDEC_flags
                                           __bid_saveFlags
getDecimalRoundingDirection                             _IDEC_round
                                           __bid_getDecimalRoundingDirection
setDecimalRoundingDirection         _IDEC_round
                                           __bid_setDecimalRoundingDirection


  11. DESCRIPTION OF THE INTEL(R) DECIMAL FP MATH LIBRARY FUNCTIONS

This section gives brief descriptions of the functions available in the
Intel(R) Decimal Floating-Point Math Library v2.0. The prototypes are
shown assuming all arguments are passed by value, the rounding mode variable is
passed as an argument to each function that requires it, a pointer to a
variable containing the status flags is passed to each function that requires
it, and alternate exception handling is not supported. The function prototypes
for other variants allowed for building the library can be determined from
header files bid_functions.h and bid_conf.h, which contain also all the type
definitions used in the following description, as well as the possible values of
the rounding mode variable rnd_mode and the positions of the individual status
flags in the status word *pfpsf.
Notes:
 1. Three decimal floating-point formats are supported, as defined in
    IEEE Standard 754-2008: 32-bit, 64-bit, and 128-bit.
    The data types used in the library for entities in the three formats are
    UINT32, UINT64, and UINT128 which can be mapped externally to types of
    appropriate sizes and alignments but having different names, for example
    _Decimal32, _Decimal64, and _Decimal128.
    The maximum number of decimal digits in the significand of numerical
    values represented in these three formats are:
      P = 7 decimal digits for the 32-bit decimal floating-point format
      P = 16 decimal digits for the 64-bit decimal floating-point format
      P = 34 decimal digits for the 128-bit decimal floating-point format
    The ranges for normal decimal floating-point numbers are (in magnitude):
      1.000000 * 10^(-95) <= x <= 9.999999 * 10^96 for 32-bit format
      1.0...0 * 10^(-383) <= x <= 9.9...9 * 10^384 for 64-bit format
            (15 decimal digits in the fractional part of the significand)
      1.0...0 * 10^(-6143) <= x <= 9.9...9 * 10^6144 for 128-bit format
            (33 decimal digits in the fractional part of the significand)
    The ranges for subnormal decimal floating-point numbers are (in magnitude):
      0.000001 * 10^(-95) <= x <= 0.999999 * 10^(-95) for 32-bit format
      0.0...01 * 10^(-383) <= x <= 0.9...9 * 10^(-383) for 64-bit format
            (15 decimal digits in the fractional part of the significand)
      0.0...01 * 10^(-6144) <= x <= 0.9...9 * 10^(-6144) for 128-bit format
            (33 decimal digits in the fractional part of the significand)
    Operations with decimal floating-point results usually choose one
    representation of the result from among several possible that have the
    same numerical value (constituting a 'cohort'). The chosen representation
    must have the 'preferred exponent' specified in the IEEE Standard 754-2008.
    (For example 1.0 * 10^(-2) + 10.0 * 10^(-3) = 20.0 * 10^(-3), and not
    2.0 * 10^(-2).)
    The encoding methods for decimal floating-point values are not explained
    here. Decimal floating-point values can be encoded using the
    string-to-decimal conversion functions (__bid64_from_string and
    __bid128_from_string), or decoded using the decimal-to-string conversion
    functions (__bid64_to_string and __bid128_to_string).
 2. The acronym 'dpd' or 'DPD' is used to identify the decimal encoding method
    for decimal floating-point values, defined in the IEEE Standard 754-2008.
    The acronym 'bid' or 'BID' is used to identify the binary encoding method
    for decimal floating-point values, defined in the IEEE Standard 754-2008.
 3. The library functions that operate on decimal floating-point values do so on
    values encoded in BID format.
 4. The floating-point status flags for inexact result, underflow, overflow,
    division by zero and invalid operation are denoted by P, U, O, Z, I
    respectively

Note that function names can be changed by editing #define statements in
bid_conf.h.

===============================================================================
FUNCTION: Convert a 32-bit decimal floating-point value encoded in BID format to
  the same value encoded in DPD format
PROTOTYPE:
  UINT32 __bid_to_dpd32 (
    UINT32 px);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Convert a 64-bit decimal floating-point value encoded in BID format to
  the same value encoded in DPD format
PROTOTYPE:
  UINT64 __bid_to_dpd64 (
    UINT64 px);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Convert a 128-bit decimal floating-point value encoded in BID format
  to the  same value encoded in DPD format
PROTOTYPE:
  UINT128 __bid_to_dpd128 (
    UINT128 px);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Convert a 32-bit decimal floating-point value encoded in DPD format
  to the  same value encoded in BID format
PROTOTYPE:
  UINT32 __bid_dpd_to_bid32 (
    UINT32 px);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Convert a 64-bit decimal floating-point value encoded in DPD format
  to the same value encoded in BID format
PROTOTYPE:
  UINT64 __bid_dpd_to_bid64 (
    UINT64 px);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Convert a 128-bit decimal floating-point value encoded in DPD format
  to the same value encoded in BID format
PROTOTYPE:
  UINT128 __bid_dpd_to_bid128 (
    UINT128 px);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Decimal floating-point addition, UINT64 + UINT64 -> UINT128
PROTOTYPE:
  UINT128 __bid128dd_add (
    UINT64 x, UINT64 y, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point addition, UINT64 + UINT128 -> UINT128
PROTOTYPE:
  UINT128 __bid128dq_add (
    UINT64 x, UINT128 y, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point addition, UINT128 + UINT64 -> UINT128
PROTOTYPE:
  UINT128 __bid128qd_add (
    UINT128 x, UINT64 y, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point addition, UINT128 + UINT128 -> UINT128
PROTOTYPE:
  UINT128 __bid128_add (
    UINT128 x, UINT128 y, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point subtraction, UINT64 - UINT64 -> UINT128
PROTOTYPE:
  UINT128 __bid128dd_sub (
    UINT64 x, UINT64 y, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point subtraction, UINT64 - UINT128 -> UINT128
PROTOTYPE:
  UINT128 __bid128dq_sub (
    UINT64 x, UINT128 y, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point subtraction, UINT128 - UINT64 -> UINT128
PROTOTYPE:
  UINT128 __bid128qd_sub (
    UINT128 x, UINT64 y, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point subtraction, UINT128 - UINT128 -> UINT128
PROTOTYPE:
  UINT128 __bid128_sub (
    UINT128 x, UINT128 y, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point multiplication, UINT64 * UINT64 -> UINT128
PROTOTYPE:
  UINT128 __bid128dd_mul (
    UINT64 x, UINT64 y, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point multiplication, UINT64 * UINT128 -> UINT128
PROTOTYPE:
  UINT128 __bid128dq_mul (
    UINT64 x, UINT128 y, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point multiplication, UINT128 * UINT64 -> UINT128
PROTOTYPE:
  UINT128 __bid128qd_mul (
    UINT128 x, UINT64 y, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point multiplication, UINT128 * UINT128 -> UINT128
PROTOTYPE:
  UINT128 __bid128_mul (
    UINT128 x, UINT128 y, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point division, UINT128 / UINT128 -> UINT128
PROTOTYPE:
  UINT128 __bid128_div (
    UINT128 x, UINT128 y, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point division, UINT64 / UINT64 -> UINT128
PROTOTYPE:
  UINT128 __bid128dd_div (
    UINT64 x, UINT64 y, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, Z, I

FUNCTION: Decimal floating-point division, UINT64 / UINT128 -> UINT128
PROTOTYPE:
  UINT128 __bid128dq_div (
    UINT64 x, UINT128 y, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, Z, I

FUNCTION: Decimal floating-point division, UINT128 / UINT64 -> UINT128
PROTOTYPE:
  UINT128 __bid128qd_div (
    UINT128 x, UINT64 y, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, Z, I

FUNCTION: Decimal floating-point fused multiply-add,
    UINT128 * UINT128 + UINT128 -> UINT128
PROTOTYPE:
  UINT128 __bid128_fma (
    UINT128 x, UINT128 y, UINT128 z, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point fused multiply-add,
    UINT64 * UINT64 + UINT64 -> UINT128
PROTOTYPE:
  UINT128 __bid128ddd_fma (
    UINT64 x, UINT64 y, UINT64 z, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point fused multiply-add,
    UINT64 * UINT64 + UINT128 -> UINT128
PROTOTYPE:
  UINT128 __bid128ddq_fma (
    UINT64 x, UINT64 y, UINT128 z, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point fused multiply-add,
    UINT64 * UINT128 + UINT64 -> UINT128
PROTOTYPE:
  UINT128 __bid128dqd_fma (
    UINT64 x, UINT128 y, UINT64 z, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point fused multiply-add,
    UINT64 * UINT128 + UINT128 -> UINT128
PROTOTYPE:
  UINT128 __bid128dqq_fma (
    UINT64 x, UINT128 y, UINT128 z, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point fused multiply-add,
    UINT128 * UINT64 + UINT64 -> UINT128
PROTOTYPE:
  UINT128 __bid128qdd_fma (
    UINT128 x, UINT64 y, UINT64 z, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point fused multiply-add,
    UINT128 * UINT64 + UINT128 -> UINT128
PROTOTYPE:
  UINT128 __bid128qdq_fma (
    UINT128 x, UINT64 y, UINT128 z, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point fused multiply-add,
    UINT128 * UINT128 + UINT64 -> UINT128
PROTOTYPE:
  UINT128 __bid128qqd_fma (
    UINT128 x, UINT128 y, UINT64 z, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point fused multiply-add,
    UINT64 * UINT64 + UINT64 -> UINT64
PROTOTYPE:
  UINT64 __bid64_fma (
    UINT64 x, UINT64 y, UINT64 z, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point fused multiply-add,
    UINT64 * UINT64 + UINT128 -> UINT64
PROTOTYPE:
  UINT64 __bid64ddq_fma (
    UINT64 x, UINT64 y, UINT128 z, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point fused multiply-add,
    UINT64 * UINT128 + UINT64 -> UINT64
PROTOTYPE:
  UINT64 __bid64dqd_fma (
    UINT64 x, UINT128 y, UINT64 z, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point fused multiply-add,
    UINT64 * UINT128 + UINT128 -> UINT64
PROTOTYPE:
  UINT64 __bid64dqq_fma (
    UINT64 x, UINT128 y, UINT128 z, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point fused multiply-add,
    UINT128 * UINT64 + UINT64 -> UINT64
PROTOTYPE:
  UINT64 __bid64qdd_fma (
    UINT128 x, UINT64 y, UINT64 z, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point fused multiply-add,
    UINT128 * UINT64 + UINT128 -> UINT64
PROTOTYPE:
  UINT64 __bid64qdq_fma (
    UINT128 x, UINT64 y, UINT128 z, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point fused multiply-add,
    UINT128 * UINT128 + UINT64 -> UINT64
PROTOTYPE:
  UINT64 __bid64qqd_fma (
    UINT128 x, UINT128 y, UINT64 z, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point fused multiply-add,
    UINT128 * UINT128 + UINT128 -> UINT64
PROTOTYPE:
  UINT64 __bid64qqq_fma (
    UINT128 x, UINT128 y, UINT128 z, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point square root, UINT128 -> UINT128
PROTOTYPE:
  UINT128 __bid128_sqrt (
    UINT128 x, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, I

FUNCTION: Decimal floating-point square root, UINT64 -> UINT128
PROTOTYPE:
  UINT128 __bid128d_sqrt (
    UINT64 x, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, I

FUNCTION: Decimal floating-point addition, UINT64 + UINT64 -> UINT64
PROTOTYPE:
  UINT64 __bid64_add (
    UINT64 x, UINT64 y, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, O , I

FUNCTION: Decimal floating-point addition, UINT64 + UINT128 -> UINT64
PROTOTYPE:
  UINT64 __bid64dq_add (
    UINT64 x, UINT128 y, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point addition, UINT128 + UINT64 -> UINT64
PROTOTYPE:
  UINT64 __bid64qd_add (
    UINT128 x, UINT64 y, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point addition, UINT128 + UINT128 -> UINT64
PROTOTYPE:
  UINT64 __bid64qq_add (
    UINT128 x, UINT128 y, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point subtraction, UINT64 - UINT64 -> UINT64
PROTOTYPE:
  UINT64 __bid64_sub (
    UINT64 x, UINT64 y, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, O, I

FUNCTION: Decimal floating-point subtraction, UINT64 - UINT128 -> UINT64
PROTOTYPE:
  UINT64 __bid64dq_sub (
    UINT64 x, UINT128 y, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point subtraction, UINT128 - UINT64 -> UINT64
PROTOTYPE:
  UINT64 __bid64qd_sub (
    UINT128 x, UINT64 y, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point subtraction, UINT128 - UINT128 -> UINT64
PROTOTYPE:
  UINT64 __bid64qq_sub (
    UINT128 x, UINT128 y, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point multiplication, UINT64 * UINT64 -> UINT64
PROTOTYPE:
  UINT64 __bid64_mul (
    UINT64 x, UINT64 y, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point multiplication, UINT64 * UINT128 -> UINT64
PROTOTYPE:
  UINT64 __bid64dq_mul (
    UINT64 x, UINT128 y, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point multiplication, UINT128 * UINT64 -> UINT64
PROTOTYPE:
  UINT64 __bid64qd_mul (
    UINT128 x, UINT64 y, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point multiplication, UINT128 * UINT128 -> UINT64
PROTOTYPE:
  UINT64 __bid64qq_mul (
    UINT128 x, UINT128 y, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Decimal floating-point division, UINT64 / UINT64 -> UINT64
PROTOTYPE:
  UINT64 __bid64_div (
    UINT64 x, UINT64 y, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, Z, I

FUNCTION: Decimal floating-point division, UINT64 / UINT128 -> UINT64
PROTOTYPE:
  UINT64 __bid64dq_div (
    UINT64 x, UINT128 y, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, Z, I

FUNCTION: Decimal floating-point division, UINT128 / UINT64 -> UINT64
PROTOTYPE:
  UINT64 __bid64qd_div (
    UINT128 x, UINT64 y, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, Z, I

FUNCTION: Decimal floating-point division, UINT128 / UINT128 -> UINT64
PROTOTYPE:
  UINT64 __bid64qq_div (
    UINT128 x, UINT128 y, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, Z, I

FUNCTION: Decimal floating-point square root, UINT64 -> UINT64
PROTOTYPE:
  UINT64 __bid64_sqrt (
    UINT64 x, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, I

FUNCTION: Decimal floating-point square root, UINT128 -> UINT64
PROTOTYPE:
  UINT64 __bid64q_sqrt (
    UINT128 x, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, I

FUNCTION: Convert 128-bit decimal floating-point value to 8-bit signed integer
  in rounding-to-nearest even mode; inexact exceptions not signaled
PROTOTYPE:
  char __bid128_to_int8_rnint (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 8-bit signed integer
  in rounding-to-nearest even mode; inexact exceptions signaled
PROTOTYPE:
  char __bid128_to_int8_xrnint (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 8-bit signed integer
  in rounding-to-nearest away mode; inexact exceptions not signaled
PROTOTYPE:
  char __bid128_to_int8_rninta (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 8-bit signed integer
  in rounding-to-nearest away mode; inexact exceptions signaled
PROTOTYPE:
  char __bid128_to_int8_xrninta (
    UINT128 x, _IDEC_flags *pfpsf);
  FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 8-bit signed integer
  in rounding-to-zero mode; inexact exceptions not signaled
PROTOTYPE:
  char __bid128_to_int8_int (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 8-bit signed integer
  in rounding-to-zero mode; inexact exceptions signaled
PROTOTYPE:
  char __bid128_to_int8_xint (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 8-bit signed integer
  in rounding-down mode; inexact exceptions not signaled
PROTOTYPE:
  char __bid128_to_int8_floor (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 8-bit signed integer
  in rounding-down mode; inexact exceptions signaled
PROTOTYPE:
  char __bid128_to_int8_xfloor (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 8-bit signed integer
  in rounding-up mode; inexact exceptions not signaled
PROTOTYPE:
  char __bid128_to_int8_ceil (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 8-bit signed integer
  in rounding-up mode; inexact exceptions signaled
PROTOTYPE:
  char __bid128_to_int8_xceil (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 16-bit signed integer
  in rounding-to-zero mode; inexact exceptions not signaled
PROTOTYPE:
  short __bid128_to_int16_rnint (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 16-bit signed integer
  in rounding-to-nearest-even mode; inexact exceptions signaled
PROTOTYPE:
  short __bid128_to_int16_xrnint (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 16-bit signed integer
  in rounding-to-nearest-even mode; inexact exceptions not signaled
PROTOTYPE:
  short __bid128_to_int16_rninta (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 16-bit signed integer
  in rounding-to-nearest-away; inexact exceptions signaled
PROTOTYPE:
  short __bid128_to_int16_xrninta (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 16-bit signed integer
  in rounding-to-zero; inexact exceptions not signaled
PROTOTYPE:
  short __bid128_to_int16_int (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 16-bit signed integer
  in rounding-to-zero mode; inexact exceptions signaled
PROTOTYPE:
  short __bid128_to_int16_xint (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 16-bit signed integer
  in rounding-down mode; inexact exceptions not signaled
PROTOTYPE:
  short __bid128_to_int16_floor (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 16-bit signed integer
  in rounding-down mode; inexact exceptions signaled
PROTOTYPE:
  short __bid128_to_int16_xfloor (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 16-bit signed integer
  in rounding-up mode; inexact exceptions not signaled
PROTOTYPE:
  short __bid128_to_int16_ceil (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 16-bit signed integer
  in rounding-up mode; inexact exceptions signaled
PROTOTYPE:
  short __bid128_to_int16_xceil (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 8-bit signed integer
  in rounding-to-nearest-even mode; inexact exceptions P, signaled
PROTOTYPE:
  unsigned char __bid128_to_uint8_rnint (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 8-bit signed integer
  in rounding-to-nearest-even mode; inexact exceptions signaled
PROTOTYPE:
  unsigned char __bid128_to_uint8_xrnint (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 8-bit signed integer
  in rounding-to-nearest-away; inexact exceptions not signaled
PROTOTYPE:
  unsigned char __bid128_to_uint8_rninta (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 8-bit signed integer
  in rounding-to-nearest-away; inexact exceptions signaled
PROTOTYPE:
  unsigned char __bid128_to_uint8_xrninta (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 8-bit signed integer
  in rounding-to-zero; inexact exceptions not signaled
PROTOTYPE:
  unsigned char __bid128_to_uint8_int (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 8-bit unsigned integer
  in rounding-to-zero; inexact exceptions signaled
PROTOTYPE:
  unsigned char __bid128_to_uint8_xint (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 8-bit unsigned integer
  in rounding-down mode; inexact exceptions not signaled
PROTOTYPE:
  unsigned char __bid128_to_uint8_floor (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 8-bit unsigned integer
  in rounding-down mode; inexact exceptions signaled
PROTOTYPE:
  unsigned char __bid128_to_uint8_xfloor (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 8-bit unsigned integer
  in rounding-up mode; inexact exceptions not signaled
PROTOTYPE:
  unsigned char __bid128_to_uint8_ceil (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 8-bit unsigned integer
  in rounding-up mode; inexact exceptions signaled
PROTOTYPE:
  unsigned char __bid128_to_uint8_xceil (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 16-bit unsigned
  integer in rounding-to-nearest-even mode; inexact exceptions not signaled
PROTOTYPE:
  unsigned short __bid128_to_uint16_rnint (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 16-bit unsigned
  integer in rounding-to-nearest-even mode; inexact exceptions signaled
PROTOTYPE:
  unsigned short __bid128_to_uint16_xrnint (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 16-bit unsigned
  integer in rounding-to-nearest-away; inexact exceptions not signaled
PROTOTYPE:
  unsigned short __bid128_to_uint16_rninta (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 16-bit unsigned
  integer in rounding-to-nearest-away; inexact exceptions signaled
PROTOTYPE:
  unsigned short __bid128_to_uint16_xrninta (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 16-bit unsigned
  integer in rounding-to-zero; inexact exceptions not signaled
PROTOTYPE:
  unsigned short __bid128_to_uint16_int (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 16-bit unsigned
  integer in rounding-to-zero; inexact exceptions signaled
PROTOTYPE:
  unsigned short __bid128_to_uint16_xint (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 16-bit unsigned
  integer in rounding-down mode; inexact exceptions not signaled
PROTOTYPE:
  unsigned short __bid128_to_uint16_floor (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 16-bit unsigned
  integer in rounding-down mode; inexact exceptions signaled
PROTOTYPE:
  unsigned short __bid128_to_uint16_xfloor (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 16-bit unsigned
  integer in rounding-up mode; inexact exceptions not signaled
PROTOTYPE:
  unsigned short __bid128_to_uint16_ceil (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 16-bit unsigned
  integer in rounding-up mode; inexact exceptions signaled
PROTOTYPE:
  unsigned short __bid128_to_uint16_xceil (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 32-bit signed
  integer in rounding-to-nearest-even mode; inexact exceptions not signaled
PROTOTYPE:
  int __bid128_to_int32_rnint (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 32-bit signed integer
  in rounding-to-nearest-even mode; inexact exceptions signaled
PROTOTYPE:
  int __bid128_to_int32_xrnint (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 32-bit signed integer
  in rounding-to-nearest-away; inexact exceptions not signaled
PROTOTYPE:
  int __bid128_to_int32_rninta (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 32-bit signed integer
  in rounding-to-nearest-away; inexact exceptions signaled
PROTOTYPE:
  int __bid128_to_int32_xrninta (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 32-bit signed integer
  in rounding-to-zero; inexact exceptions not signaled
PROTOTYPE:
  int __bid128_to_int32_int (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 32-bit signed integer
  in rounding-to-zero; inexact exceptions signaled
PROTOTYPE:
  int __bid128_to_int32_xint (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 32-bit signed integer
  in rounding-down mode; inexact exceptions not signaled
PROTOTYPE:
  int __bid128_to_int32_floor (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 32-bit signed integer
  in rounding-down mode; inexact exceptions signaled
PROTOTYPE:
  int __bid128_to_int32_xfloor (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 32-bit signed integer
  in rounding-up mode; inexact exceptions not signaled
PROTOTYPE:
  int __bid128_to_int32_ceil (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 32-bit signed integer
  in rounding-up mode; inexact exceptions signaled
PROTOTYPE:
  int __bid128_to_int32_xceil (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 32-bit unsigned
  integer in rounding-to-nearest-even mode; inexact exceptions not signaled
PROTOTYPE:
  unsigned int __bid128_to_uint32_rnint (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 32-bit unsigned
  integer in rounding-to-nearest-even mode; inexact exceptions signaled
PROTOTYPE:
  unsigned int __bid128_to_uint32_xrnint (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 32-bit unsigned
  integer in rounding-to-nearest-away; inexact exceptions not signaled
PROTOTYPE:
  unsigned int __bid128_to_uint32_rninta (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 32-bit unsigned
  integer in rounding-to-nearest-away; inexact exceptions signaled
PROTOTYPE:
  unsigned int __bid128_to_uint32_xrninta (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 32-bit unsigned
  integer in rounding-to-zero; inexact exceptions not signaled
PROTOTYPE:
  unsigned int __bid128_to_uint32_int (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 32-bit unsigned
  integer in rounding-to-zero; inexact exceptions signaled
PROTOTYPE:
  unsigned int __bid128_to_uint32_xint (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 32-bit unsigned
  integer in rounding-down mode; inexact exceptions not signaled
PROTOTYPE:
  unsigned int __bid128_to_uint32_floor (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 32-bit unsigned
  integer in rounding-down mode; inexact exceptions signaled
PROTOTYPE:
  unsigned int __bid128_to_uint32_xfloor (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 32-bit unsigned
  integer in rounding-up mode; inexact exceptions not signaled
PROTOTYPE:
  unsigned int __bid128_to_uint32_ceil (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 32-bit unsigned
  integer in rounding-up mode; inexact exceptions signaled
PROTOTYPE:
  unsigned int __bid128_to_uint32_xceil (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 64-bit signed
  integer in rounding-to-nearest-even mode; inexact exceptions not signaled
PROTOTYPE:
  SINT64 __bid128_to_int64_rnint (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 64-bit signed
  integer in rounding-to-nearest-even mode; inexact exceptions signaled
PROTOTYPE:
  SINT64 __bid128_to_int64_xrnint (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 64-bit signed
  integer in rounding-to-nearest-away; inexact exceptions not signaled
PROTOTYPE:
  SINT64 __bid128_to_int64_rninta (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 64-bit signed
  integer in rounding-to-nearest-away; inexact exceptions signaled
PROTOTYPE:
  SINT64 __bid128_to_int64_xrninta (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 64-bit signed integer
  in rounding-to-zero; inexact exceptions not signaled
PROTOTYPE:
  SINT64 __bid128_to_int64_int (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 64-bit signed integer
  in rounding-to-zero; inexact exceptions signaled
PROTOTYPE:
  SINT64 __bid128_to_int64_xint (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 64-bit signed integer
  in rounding-down mode; inexact exceptions not signaled
PROTOTYPE:
  SINT64 __bid128_to_int64_floor (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 64-bit signed integer
  in rounding-down mode; inexact exceptions signaled
PROTOTYPE:
  SINT64 __bid128_to_int64_xfloor (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 64-bit signed integer
  in rounding-up mode; inexact exceptions not signaled
PROTOTYPE:
  SINT64 __bid128_to_int64_ceil (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 64-bit signed integer
  in rounding-up mode; inexact exceptions signaled
PROTOTYPE:
  SINT64 __bid128_to_int64_xceil (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 64-bit unsigned
  integer in rounding-to-nearest-even mode; inexact exceptions not signaled
PROTOTYPE:
  UINT64 __bid128_to_uint64_rnint (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 64-bit unsigned
  integer in rounding-to-nearest-even mode; inexact exceptions signaled
PROTOTYPE:
  UINT64 __bid128_to_uint64_xrnint (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 64-bit unsigned
  integer in rounding-to-nearest-away; inexact exceptions not signaled
PROTOTYPE:
  UINT64 __bid128_to_uint64_rninta (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 64-bit unsigned
  integer in rounding-to-nearest-away; inexact exceptions signaled
PROTOTYPE:
  UINT64 __bid128_to_uint64_xrninta (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 64-bit unsigned
  integer in rounding-to-zero; inexact exceptions not signaled
PROTOTYPE:
  UINT64 __bid128_to_uint64_int (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 64-bit unsigned
  integer in rounding-to-zero; inexact exceptions signaled
PROTOTYPE:
  UINT64 __bid128_to_uint64_xint (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 64-bit unsigned
  integer in rounding-down mode; inexact exceptions not signaled
PROTOTYPE:
  UINT64 __bid128_to_uint64_floor (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 64-bit unsigned
  integer in rounding-down mode; inexact exceptions signaled
PROTOTYPE:
  UINT64 __bid128_to_uint64_xfloor (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value to 64-bit unsigned
  integer in rounding-up mode; inexact exceptions not signaled
PROTOTYPE:
  UINT64 __bid128_to_uint64_ceil (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 128-bit decimal floating-point value to 64-bit unsigned
  integer in rounding-up mode; inexact exceptions signaled
PROTOTYPE:
  UINT64 __bid128_to_uint64_xceil (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 32-bit signed
  integer in rounding-to-nearest-even mode; inexact exceptions not signaled
PROTOTYPE:
  int __bid64_to_int32_rnint (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 32-bit signed integer
  in rounding-to-nearest-even mode; inexact exceptions signaled
PROTOTYPE:
  int __bid64_to_int32_xrnint (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 32-bit signed integer
  in rounding-to-nearest-away; inexact exceptions not signaled
PROTOTYPE:
  int __bid64_to_int32_rninta (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 32-bit signed integer
  in rounding-to-nearest-away; inexact exceptions signaled
PROTOTYPE:
  int __bid64_to_int32_xrninta (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 32-bit signed integer
  in rounding-to-zero; inexact exceptions not signaled
PROTOTYPE:
  int __bid64_to_int32_int (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 32-bit signed integer
  in rounding-to-zero; inexact exceptions signaled
PROTOTYPE:
  int __bid64_to_int32_xint (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 32-bit signed integer
  in rounding-down mode; inexact exceptions not signaled
PROTOTYPE:
  int __bid64_to_int32_floor (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 32-bit signed integer
  in rounding-down mode; inexact exceptions signaled
PROTOTYPE:
  int __bid64_to_int32_xfloor (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 32-bit signed integer
  in rounding-up mode; inexact exceptions not signaled
PROTOTYPE:
  int __bid64_to_int32_ceil (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 32-bit signed integer
  in rounding-up mode; inexact exceptions signaled
PROTOTYPE:
  int __bid64_to_int32_xceil (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 8-bit signed integer
  in rounding-to-nearest-even mode; inexact exceptions not signaled
PROTOTYPE:
  char __bid64_to_int8_rnint (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 8-bit signed integer
  in rounding-to-nearest-even mode; inexact exceptions signaled
PROTOTYPE:
  char __bid64_to_int8_xrnint (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 8-bit signed integer
  in rounding-to-nearest-away; inexact exceptions not signaled
PROTOTYPE:
  char __bid64_to_int8_rninta (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 8-bit signed integer
  in rounding-to-nearest-away; inexact exceptions signaled
PROTOTYPE:
  char __bid64_to_int8_xrninta (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 8-bit signed integer
  in rounding-to-zero; inexact exceptions not signaled
PROTOTYPE:
  char __bid64_to_int8_int (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 8-bit signed integer
  in rounding-to-zero; inexact exceptions signaled
PROTOTYPE:
  char __bid64_to_int8_xint (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 8-bit signed integer
  in rounding-down mode; inexact exceptions not signaled
PROTOTYPE:
  char __bid64_to_int8_floor (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 8-bit signed integer
  in rounding-down mode; inexact exceptions signaled
PROTOTYPE:
  char __bid64_to_int8_xfloor (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 8-bit signed integer
  in rounding-up mode; inexact exceptions not signaled
PROTOTYPE:
  char __bid64_to_int8_ceil (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 8-bit signed integer
  in rounding-up mode; inexact exceptions signaled
PROTOTYPE:
  char __bid64_to_int8_xceil (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 16-bit signed integer
  in rounding-to-nearest-even mode; inexact exceptions not signaled
PROTOTYPE:
  short __bid64_to_int16_rnint (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 16-bit signed integer
  in rounding-to-nearest-even mode; inexact exceptions signaled
PROTOTYPE:
  short __bid64_to_int16_xrnint (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 16-bit signed integer
  in rounding-to-nearest-away; inexact exceptions not signaled
PROTOTYPE:
  short __bid64_to_int16_rninta (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 16-bit signed integer
  in rounding-to-nearest-away; inexact exceptions signaled
PROTOTYPE:
  short __bid64_to_int16_xrninta (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 16-bit signed integer
  in rounding-to-zero; inexact exceptions not signaled
PROTOTYPE:
  short __bid64_to_int16_int (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 16-bit signed integer
  in rounding-to-zero; inexact exceptions signaled
PROTOTYPE:
  short __bid64_to_int16_xint (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 16-bit signed integer
  in rounding-down mode; inexact exceptions not signaled
PROTOTYPE:
  short __bid64_to_int16_floor (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 16-bit signed integer
  in rounding-down mode; inexact exceptions signaled
PROTOTYPE:
  short __bid64_to_int16_xfloor (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 16-bit signed integer
  in rounding-up mode; inexact exceptions not signaled
PROTOTYPE:
  short __bid64_to_int16_ceil (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 16-bit signed integer
  in rounding-up mode; inexact exceptions signaled
PROTOTYPE:
  short __bid64_to_int16_xceil (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 8-bit unsigned integer
  in rounding-to-nearest-even mode; inexact exceptions not signaled
PROTOTYPE:
  unsigned char __bid64_to_uint8_rnint (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 8-bit unsigned integer
  in rounding-to-nearest-even mode; inexact exceptions signaled
PROTOTYPE:
  unsigned char __bid64_to_uint8_xrnint (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 8-bit unsigned integer
  in rounding-to-nearest-away; inexact exceptions not signaled
PROTOTYPE:
  unsigned char __bid64_to_uint8_rninta (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 8-bit unsigned integer
  in rounding-to-nearest-away; inexact exceptions signaled
PROTOTYPE:
  unsigned char __bid64_to_uint8_xrninta (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 8-bit unsigned integer
  in rounding-to-zero; inexact exceptions not signaled
PROTOTYPE:
  unsigned char __bid64_to_uint8_int (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 8-bit unsigned integer
  in rounding-to-zero; inexact exceptions signaled
PROTOTYPE:
  unsigned char __bid64_to_uint8_xint (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 8-bit unsigned integer
  in rounding-down mode; inexact exceptions not signaled
PROTOTYPE:
  unsigned char __bid64_to_uint8_floor (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 8-bit unsigned integer
  in rounding-down mode; inexact exceptions signaled
PROTOTYPE:
  unsigned char __bid64_to_uint8_xfloor (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 8-bit unsigned integer
  in rounding-up mode; inexact exceptions not signaled
PROTOTYPE:
  unsigned char __bid64_to_uint8_ceil (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 8-bit unsigned integer
  in rounding-up mode; inexact exceptions signaled
PROTOTYPE:
  unsigned char __bid64_to_uint8_xceil (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 16-bit unsigned integer
  in rounding-to-nearest-even mode; inexact exceptions not signaled
PROTOTYPE:
  unsigned short __bid64_to_uint16_rnint (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 16-bit unsigned integer
  in rounding-to-nearest-even mode; inexact exceptions signaled
PROTOTYPE:
  unsigned short __bid64_to_uint16_xrnint (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 16-bit unsigned integer
  in rounding-to-nearest-away; inexact exceptions not signaled
PROTOTYPE:
  unsigned short __bid64_to_uint16_rninta (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 16-bit unsigned integer
  in rounding-to-nearest-away; inexact exceptions signaled
PROTOTYPE:
  unsigned short __bid64_to_uint16_xrninta (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 16-bit unsigned integer
  in rounding-to-zero; inexact exceptions not signaled
PROTOTYPE:
  unsigned short __bid64_to_uint16_int (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 16-bit unsigned integer
  in rounding-to-zero; inexact exceptions signaled
PROTOTYPE:
  unsigned short __bid64_to_uint16_xint (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 16-bit unsigned integer
  in rounding-down mode; inexact exceptions not signaled
PROTOTYPE:
  unsigned short __bid64_to_uint16_floor (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 16-bit unsigned integer
  in rounding-down mode; inexact exceptions signaled
PROTOTYPE:
  unsigned short __bid64_to_uint16_xfloor (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 16-bit unsigned integer
  in rounding-up mode; inexact exceptions not signaled
PROTOTYPE:
  unsigned short __bid64_to_uint16_ceil (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 16-bit unsigned integer
  in rounding-up mode; inexact exceptions signaled
PROTOTYPE:
  unsigned short __bid64_to_uint16_xceil (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 32-bit unsigned integer
  in rounding-to-nearest-even mode; inexact exceptions not signaled
PROTOTYPE:
  unsigned int __bid64_to_uint32_rnint (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 32-bit unsigned integer
  in rounding-to-nearest-even mode; inexact exceptions signaled
PROTOTYPE:
  unsigned int __bid64_to_uint32_xrnint (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 32-bit unsigned integer
  in rounding-to-nearest-away; inexact exceptions not signaled
PROTOTYPE:
  unsigned int __bid64_to_uint32_rninta (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 32-bit unsigned integer
  in rounding-to-nearest-away; inexact exceptions signaled
PROTOTYPE:
  unsigned int __bid64_to_uint32_xrninta (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 32-bit unsigned integer
  in rounding-to-zero; inexact exceptions not signaled
PROTOTYPE:
  unsigned int __bid64_to_uint32_int (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 32-bit unsigned integer
  in rounding-to-zero; inexact exceptions signaled
PROTOTYPE:
  unsigned int __bid64_to_uint32_xint (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 32-bit unsigned integer
  in rounding-down mode; inexact exceptions not signaled
PROTOTYPE:
  unsigned int __bid64_to_uint32_floor (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 32-bit unsigned integer
  in rounding-down mode; inexact exceptions signaled
PROTOTYPE:
  unsigned int __bid64_to_uint32_xfloor (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 32-bit unsigned integer
  in rounding-up mode; inexact exceptions not signaled
PROTOTYPE:
  unsigned int __bid64_to_uint32_ceil (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 32-bit unsigned integer
  in rounding-up mode; inexact exceptions signaled
PROTOTYPE:
  unsigned int __bid64_to_uint32_xceil (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 64-bit signed integer
  in rounding-to-nearest-even mode; inexact exceptions not signaled
PROTOTYPE:
  SINT64 __bid64_to_int64_rnint (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 64-bit signed integer
  in rounding-to-nearest-even mode; inexact exceptions signaled
PROTOTYPE:
  SINT64 __bid64_to_int64_xrnint (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 64-bit signed integer
  in rounding-to-nearest-away; inexact exceptions not signaled
PROTOTYPE:
  SINT64 __bid64_to_int64_rninta (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 64-bit signed integer
  in rounding-to-nearest-away; inexact exceptions signaled
PROTOTYPE:
  SINT64 __bid64_to_int64_xrninta (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 64-bit signed integer
  in rounding-to-zero; inexact exceptions not signaled
PROTOTYPE:
  SINT64 __bid64_to_int64_int (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 64-bit signed integer
  in rounding-to-zero; inexact exceptions signaled
PROTOTYPE:
  SINT64 __bid64_to_int64_xint (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 64-bit signed integer
  in rounding-down mode; inexact exceptions not signaled
PROTOTYPE:
  SINT64 __bid64_to_int64_floor (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 64-bit signed integer
  in rounding-down mode; inexact exceptions signaled
PROTOTYPE:
  SINT64 __bid64_to_int64_xfloor (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 64-bit signed integer
  in rounding-up mode; inexact exceptions not signaled
PROTOTYPE:
  SINT64 __bid64_to_int64_ceil (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 64-bit signed integer
  in rounding-up mode; inexact exceptions signaled
PROTOTYPE:
  SINT64 __bid64_to_int64_xceil (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 64-bit unsigned integer
  in rounding-to-nearest-even mode; inexact exceptions not signaled
PROTOTYPE:
  UINT64 __bid64_to_uint64_rnint (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 64-bit unsigned integer
  in rounding-to-nearest-even mode; inexact exceptions signaled
PROTOTYPE:
  UINT64 __bid64_to_uint64_xrnint (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 64-bit unsigned integer
  in rounding-to-nearest-away; inexact exceptions not signaled
PROTOTYPE:
  UINT64 __bid64_to_uint64_rninta (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 64-bit unsigned integer
  in rounding-to-nearest-away; inexact exceptions signaled
PROTOTYPE:
  UINT64 __bid64_to_uint64_xrninta (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 64-bit unsigned integer
  in rounding-to-zero; inexact exceptions not signaled
PROTOTYPE:
  UINT64 __bid64_to_uint64_int (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 64-bit unsigned integer
  in rounding-to-zero mode; inexact exceptions signaled
PROTOTYPE:
  UINT64 __bid64_to_uint64_xint (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 64-bit unsigned integer
  in rounding-down mode; inexact exceptions not signaled
PROTOTYPE:
  UINT64 __bid64_to_uint64_floor (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 64-bit unsigned integer
  in rounding-down mode; inexact exceptions signaled
PROTOTYPE:
  UINT64 __bid64_to_uint64_xfloor (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value to 64-bit unsigned integer
  in rounding-up mode; inexact exceptions not signaled
PROTOTYPE:
  UINT64 __bid64_to_uint64_ceil (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 64-bit unsigned integer
  in rounding-up mode; inexact exceptions signaled
PROTOTYPE:
  UINT64 __bid64_to_uint64_xceil (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Compare 64-bit decimal floating-point numbers for specified relation;
  do not signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid64_quiet_equal (
    UINT64 x, UINT64 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 64-bit decimal floating-point numbers for specified relation;
  do not signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid64_quiet_greater (
    UINT64 x, UINT64 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 64-bit decimal floating-point numbers for specified relation;
  do not signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid64_quiet_greater_equal (
    UINT64 x, UINT64 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 64-bit decimal floating-point numbers for specified relation;
  do not signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid64_quiet_greater_unordered (
    UINT64 x, UINT64 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 64-bit decimal floating-point numbers for specified relation;
  do not signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid64_quiet_less (
    UINT64 x, UINT64 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 64-bit decimal floating-point numbers for specified relation;
  do not signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid64_quiet_less_equal (
    UINT64 x, UINT64 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 64-bit decimal floating-point numbers for specified relation;
  do not signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid64_quiet_less_unordered (
    UINT64 x, UINT64 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 64-bit decimal floating-point numbers for specified relation;
  do not signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid64_quiet_not_equal (
    UINT64 x, UINT64 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 64-bit decimal floating-point numbers for specified relation;
  do not signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid64_quiet_not_greater (
    UINT64 x, UINT64 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 64-bit decimal floating-point numbers for specified relation;
  do not signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid64_quiet_not_less (
    UINT64 x, UINT64 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 64-bit decimal floating-point numbers for specified relation;
  do not signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid64_quiet_ordered (
    UINT64 x, UINT64 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 64-bit decimal floating-point numbers for specified relation;
  do not signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid64_quiet_unordered (
    UINT64 x, UINT64 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 64-bit decimal floating-point numbers for specified relation;
  signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid64_signaling_greater (
    UINT64 x, UINT64 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 64-bit decimal floating-point numbers for specified relation;
  signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid64_signaling_greater_equal (
    UINT64 x, UINT64 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 64-bit decimal floating-point numbers for specified relation;
  signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid64_signaling_greater_unordered (
    UINT64 x, UINT64 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 64-bit decimal floating-point numbers for specified relation;
  signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid64_signaling_less (
    UINT64 x, UINT64 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 64-bit decimal floating-point numbers for specified relation;
  signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid64_signaling_less_equal (
    UINT64 x, UINT64 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 64-bit decimal floating-point numbers for specified relation;
  signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid64_signaling_less_unordered (
    UINT64 x, UINT64 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 64-bit decimal floating-point numbers for specified relation;
  signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid64_signaling_not_greater (
    UINT64 x, UINT64 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 64-bit decimal floating-point numbers for specified relation;
  signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid64_signaling_not_less (
    UINT64 x, UINT64 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 128-bit decimal floating-point numbers for specified relation;
  do not signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid128_quiet_equal (
    UINT128 x, UINT128 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 128-bit decimal floating-point numbers for specified relation;
  do not signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid128_quiet_greater (
    UINT128 x, UINT128 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 128-bit decimal floating-point numbers for specified relation;
  do not signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid128_quiet_greater_equal (
    UINT128 x, UINT128 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 128-bit decimal floating-point numbers for specified relation;
  do not signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid128_quiet_greater_unordered (
    UINT128 x, UINT128 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 128-bit decimal floating-point numbers for specified relation;
  do not signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid128_quiet_less (
    UINT128 x, UINT128 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 128-bit decimal floating-point numbers for specified relation;
  do not signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid128_quiet_less_equal (
    UINT128 x, UINT128 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 128-bit decimal floating-point numbers for specified relation;
  do not signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid128_quiet_less_unordered (
    UINT128 x, UINT128 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 128-bit decimal floating-point numbers for specified relation;
  do not signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid128_quiet_not_equal (
    UINT128 x, UINT128 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 128-bit decimal floating-point numbers for specified relation;
  do not signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid128_quiet_not_greater (
    UINT128 x, UINT128 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 128-bit decimal floating-point numbers for specified relation;
  do not signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid128_quiet_not_less (
    UINT128 x, UINT128 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 128-bit decimal floating-point numbers for specified relation;
  do not signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid128_quiet_ordered (
    UINT128 x, UINT128 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 128-bit decimal floating-point numbers for specified relation;
  do not signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid128_quiet_unordered (
    UINT128 x, UINT128 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 128-bit decimal floating-point numbers for specified relation;
  signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid128_signaling_greater (
    UINT128 x, UINT128 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 128-bit decimal floating-point numbers for specified relation;
  signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid128_signaling_greater_equal (
    UINT128 x, UINT128 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 128-bit decimal floating-point numbers for specified relation;
  signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid128_signaling_greater_unordered (
    UINT128 x, UINT128 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 128-bit decimal floating-point numbers for specified relation;
  signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid128_signaling_less (
    UINT128 x, UINT128 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 128-bit decimal floating-point numbers for specified relation;
  signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid128_signaling_less_equal (
    UINT128 x, UINT128 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 128-bit decimal floating-point numbers for specified relation;
  signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid128_signaling_less_unordered (
    UINT128 x, UINT128 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 128-bit decimal floating-point numbers for specified relation;
  signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid128_signaling_not_greater (
    UINT128 x, UINT128 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Compare 128-bit decimal floating-point numbers for specified relation;
  signal invalid exception for quiet NaNs
PROTOTYPE:
  int __bid128_signaling_not_less (
    UINT128 x, UINT128 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Round 64-bit decimal floating-point value to integral-valued decimal
  floating-point value in the same format, using the current rounding mode;
  signal inexact exceptions
PROTOTYPE:
  UINT64 __bid64_round_integral_exact (
    UINT64 x, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Round 64-bit decimal floating-point value to integral-valued decimal
  floating-point value in the same format, using the rounding-to-nearest-even
  mode; do not signal inexact exceptions
PROTOTYPE:
  UINT64 __bid64_round_integral_nearest_even (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Round 64-bit decimal floating-point value to integral-valued decimal
  floating-point value in the same format, using the rounding-down mode; do not
  signal inexact exceptions
PROTOTYPE:
  UINT64 __bid64_round_integral_negative (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Round 64-bit decimal floating-point value to integral-valued decimal
  floating-point value in the same format, using the rounding-up  mode; do not
  signal inexact exceptions
PROTOTYPE:
  UINT64 __bid64_round_integral_positive (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Round 64-bit decimal floating-point value to integral-valued decimal
  floating-point value in the same format, using the rounding-to-zero  mode;
  do not  signal inexact exceptions
PROTOTYPE:
  UINT64 __bid64_round_integral_zero (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Round 64-bit decimal floating-point value to integral-valued decimal
  floating-point value in the same format, using the rounding-to-nearest-away
  mode; do not signal inexact exceptions
PROTOTYPE:
  UINT64 __bid64_round_integral_nearest_away (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Round 128-bit decimal floating-point value to integral-valued decimal
  floating-point value in the same format, using the current rounding mode;
  signal inexact exceptions
PROTOTYPE:
  UINT128 __bid128_round_integral_exact (
    UINT128 x, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Round 128-bit decimal floating-point value to integral-valued decimal
  floating-point value in the same format, using the rounding-to-nearest-even   mode; do not signal inexact exceptions
PROTOTYPE:
  UINT128 __bid128_round_integral_nearest_even (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Round 128-bit decimal floating-point value to integral-valued decimal
  floating-point value in the same format, using the rounding-down mode; do not
  signal inexact exceptions
PROTOTYPE:
  UINT128 __bid128_round_integral_negative (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Round 128-bit decimal floating-point value to integral-valued decimal
  floating-point value in the same format, using the rounding-up  mode; do not
  signal inexact exceptions
PROTOTYPE:
  UINT128 __bid128_round_integral_positive (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Round 128-bit decimal floating-point value to integral-valued decimal
  floating-point value in the same format, using the rounding-to-zero  mode;
  do not  signal inexact exceptions
PROTOTYPE:
  UINT128 __bid128_round_integral_zero (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Round 128-bit decimal floating-point value to integral-valued decimal
  floating-point value in the same format, using the rounding-to-nearest-away
  mode; do not signal inexact exceptions
PROTOTYPE:
  UINT128 __bid128_round_integral_nearest_away (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Returns the least 64-bit decimal floating-point number that
  compares greater than the operand
PROTOTYPE:
  UINT64 __bid64_nextup (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Returns the greatest 64-bit decimal floating-point number that
  compares less than the operand
PROTOTYPE:
  UINT64 __bid64_nextdown (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Returns the next 64-bit decimal floating-point number that neighbors
  the first operand in the direction toward the second operand
PROTOTYPE:
  UINT64 __bid64_nextafter (
    UINT64 x, UINT64 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Returns the least 128-bit decimal floating-point number that
  compares greater than the operand
PROTOTYPE:
  UINT128 __bid128_nextup (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Returns the greatest 128-bit decimal floating-point number that
  compares less than the operand
PROTOTYPE:
  UINT128 __bid128_nextdown (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Returns the next 128-bit decimal floating-point number that neighbors
  the first operand in the direction toward the second operand
PROTOTYPE:
  UINT128 __bid128_nextafter (
    UINT128 x, UINT128 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Returns the canonicalized floating-point number x if x < y,
  y if y < x, the canonicalized floating-point number if one operand is
  a floating-point number and the other a quiet NaN. Otherwise it is
  either x or y, canonicalized.
PROTOTYPE:
  UINT64 __bid64_minnum (
    UINT64 x, UINT64 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Returns the canonicalized floating-point number x if |x| < |y|,
  y if |y| < |x|, otherwise this function is identical to __bid64_minnum
PROTOTYPE:
  UINT64 __bid64_minnum_mag (
    UINT64 x, UINT64 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Returns the canonicalized floating-point number y if x < y,
  x if y < x, the canonicalized floating-point number if one operand is a
  floating-point number and the other a quiet NaN.  Otherwise it is either x
  or y, canonicalized.
PROTOTYPE:
  UINT64 __bid64_maxnum (
    UINT64 x, UINT64 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Returns the canonicalized floating-point number x if |x| > |y|,
  y if |y| > |x|, otherwise this function is identical to __bid64_maxnum
PROTOTYPE:
  UINT64 __bid64_maxnum_mag (
    UINT64 x, UINT64 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Returns the canonicalized floating-point number x if x < y,
  y if y < x, the canonicalized floating-point number if one operand is
  a floating-point number and the other a quiet NaN. Otherwise it is    either x or y, canonicalized.
PROTOTYPE:
  UINT128 __bid128_minnum (
    UINT128 x, UINT128 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Returns the canonicalized floating-point number x if |x| < |y|,
  y if |y| < |x|, otherwise this function is identical to __bid128_minnum
PROTOTYPE:
  UINT128 __bid128_minnum_mag (
    UINT128 x, UINT128 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Returns the canonicalized floating-point number y if x < y,
  x if y < x, the canonicalized floating-point number if one operand is a
  floating-point number and the other a quiet NaN.  Otherwise it is either x
  or y, canonicalized.
PROTOTYPE:
  UINT128 __bid128_maxnum (
    UINT128 x, UINT128 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Returns the canonicalized floating-point number x if |x| > |y|,
  y if |y| > |x|, otherwise this function is identical to __bid128_maxnum
PROTOTYPE:
  UINT128 __bid128_maxnum_mag (
    UINT128 x, UINT128 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 32-bit signed integer to 64-bit decimal floating-point number
PROTOTYPE:
  UINT64 __bid64_from_int32 (
    int x);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Convert 32-bit unsigned integer to 64-bit decimal floating-point
  number
PROTOTYPE:
  UINT64 __bid64_from_uint32 (
    unsigned int x);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Convert 64-bit signed integer to 64-bit decimal floating-point number
PROTOTYPE:
  UINT64 __bid64_from_int64 (
    SINT64 x, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P

FUNCTION: Convert 64-bit unsigned integer to 64-bit decimal floating-point
  number
PROTOTYPE:
  UINT64 __bid64_from_uint64 (
    UINT64, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P

FUNCTION: Convert 32-bit signed integer to 128-bit decimal floating-point number
PROTOTYPE:
  UINT128 __bid128_from_int32 (
    int x);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Convert 32-bit unsigned integer to 128-bit decimal floating-point
  number
PROTOTYPE:
  UINT128 __bid128_from_uint32 (
    unsigned int x);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Convert 64-bit signed integer to 128-bit decimal floating-point number
PROTOTYPE:
  UINT128 __bid128_from_int64 (
    SINT64 x);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Convert 64-bit unsigned integer to 128-bit decimal floating-point
  number
PROTOTYPE:
  UINT128 __bid128_from_uint64 (
    UINT64 x);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Return true if and only if x has negative sign
PROTOTYPE:
  int __bid64_isSigned (
    UINT64 x);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Return true if and only if x is normal (not zero, subnormal,
  infinite, or NaN)
PROTOTYPE:
  int __bid64_isNormal (
    UINT64 x);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Return true if and only if x is subnormal
PROTOTYPE:
  int __bid64_isSubnormal (
    UINT64 x);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Return true if and only if x is zero, subnormal or normal
  (not infinite or NaN)
PROTOTYPE:
  int __bid64_isFinite (
    UINT64 x);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Return true if and only if x is +0 or -0
PROTOTYPE:
  int __bid64_isZero (
    UINT64 x);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Return true if and only if x is infinite
PROTOTYPE:
  int __bid64_isInf (
    UINT64 x);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Return true if and only if x is a signaling NaN
PROTOTYPE:
  int __bid64_isSignaling (
    UINT64 x);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Return true if and only if x is a finite number, infinity, or
  NaN that is canonical.
PROTOTYPE:
  int __bid64_isCanonical (
    UINT64 x);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Return true if and only if x is a NaN
PROTOTYPE:
  int __bid64_isNaN (
    UINT64 x);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Copies a decimal floating-point operand x to a destination in the
  same format, with no change
PROTOTYPE:
  UINT64 __bid64_copy (
    UINT64 x);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Copies a 64-bit decimal floating-point operand x to a destination
  in the same format, reversing the sign
PROTOTYPE:
  UINT64 __bid64_negate (
    UINT64 x);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Copies a 64-bit decimal floating-point operand x to a destination
  in the same format, changing the sign to positive
PROTOTYPE:
  UINT64 __bid64_abs (
    UINT64 x);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Copies a 64-bit decimal floating-point operand x to a destination
  in the same format as x, but with the sign of y
PROTOTYPE:
  UINT64 __bid64_copySign (
    UINT64 x, UINT64 y);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Tells which of the following ten classes x falls into (details in
  the IEEE Standard 754-2008): signalingNaN, quietNaN, negativeInfinity,
  negativeNormal, negativeSubnormal, negativeZero, positiveZero,
  positiveSubnormal, positiveNormal, positiveInfinity
PROTOTYPE:
  int __bid64_class (
    UINT64 x);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: sameQuantum(x, y) is true if the exponents of x and y are the same,
  and false otherwise; sameQuantum(NaN, NaN) and sameQuantum(inf, inf) are
  true; if exactly one operand is infinite or exactly one operand is NaN,
  sameQuantum is false
PROTOTYPE:
  int __bid64_sameQuantum (
    UINT64 x, UINT64 y);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Return true if x and y are ordered (see the IEEE Standard 754-2008)
PROTOTYPE:
  int __bid64_totalOrder (
    UINT64 x, UINT64 y);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Return true if the absolute values of x and y are ordered
  (see the IEEE Standard 754-2008)
PROTOTYPE:
  int __bid64_totalOrderMag (
    UINT64 x, UINT64 y);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Return the radix b of the format of x, 2 or 10
PROTOTYPE:
  int __bid64_radix (
    UINT64 x);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Return true if and only if x has negative sign
PROTOTYPE:
  int __bid128_isSigned (
    UINT128 x);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Return true if and only if x is normal (not zero, subnormal,
  infinite, or NaN)
PROTOTYPE:
  int __bid128_isNormal (
    UINT128 x);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Return true if and only if x is subnormal
PROTOTYPE:
  int __bid128_isSubnormal (
    UINT128 x);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Return true if and only if x is zero, subnormal or normal
  (not infinite or NaN)
PROTOTYPE:
  int __bid128_isFinite (
    UINT128 x);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Return true if and only if x is +0 or -0
PROTOTYPE:
  int __bid128_isZero (
    UINT128 x);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Return true if and only if x is infinite
PROTOTYPE:
  int __bid128_isInf (
    UINT128 x);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Return true if and only if x is a signaling NaN
PROTOTYPE:
  int __bid128_isSignaling (
    UINT128 x);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Return Return true if and only if x is a finite number, infinity, or    NaN that is canonical.
PROTOTYPE:
  int __bid128_isCanonical (
    UINT128 x);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Return true if and only if x is a NaN
PROTOTYPE:
  int __bid128_isNaN (
    UINT128 x);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Copies a decimal floating-point operand x to a destination in the    same format, with no change
PROTOTYPE:
  UINT128 __bid128_copy (
    UINT128 x);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Copies a 128-bit decimal floating-point operand x to a destination
  in the same format, reversing the sign
PROTOTYPE:
  UINT128 __bid128_negate (
    UINT128 x);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Copies a 128-bit decimal floating-point operand x to a destination
  in the same format, changing the sign to positive
PROTOTYPE:
  UINT128 __bid128_abs (
    UINT128 x);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Copies a 128-bit decimal floating-point operand x to a destination
  in the  same format as x, but with the sign of y
PROTOTYPE:
  UINT128 __bid128_copySign (
    UINT128 x, UINT128 y);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Tells which of the following ten classes x falls into (details in
  the IEEE Standard 754-2008): signalingNaN, quietNaN, negativeInfinity,
  negativeNormal, negativeSubnormal, negativeZero, positiveZero,
  positiveSubnormal, positiveNormal, positiveInfinity
PROTOTYPE:
  int __bid128_class (
    UINT128 x);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: sameQuantum(x, y) is true if the exponents of x and y are the same,
  and false otherwise; sameQuantum(NaN, NaN) and sameQuantum(inf, inf) are
  true; if exactly one operand is infinite or exactly one operand is NaN,
  sameQuantum is false
PROTOTYPE:
  int __bid128_sameQuantum (
    UINT128 x, UINT128 y);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Return true if x and y are ordered (see the IEEE Standard 754-2008)
PROTOTYPE:
  int __bid128_totalOrder (
    UINT128 x, UINT128 y);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Return true if the absolute values of x and y are ordered
  (see the IEEE Standard 754-2008)
PROTOTYPE:
  int __bid128_totalOrderMag (
    UINT128 x, UINT128 y);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Return the radix b of the format of x, 2 or 10
PROTOTYPE:
  int __bid128_radix (
    UINT128 x);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Decimal floating-point remainder
PROTOTYPE:
  UINT64 __bid64_rem (
    UINT64 x, UINT64 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Returns the exponent e of x, a signed integral value, determined
  as though x were represented with infinite range and minimum exponent
PROTOTYPE:
  UINT64 __bid64_ilogb (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: Z, I

FUNCTION: Returns x * 10^N
PROTOTYPE:
  UINT64 __bid64_scalbn (
    UINT64 x, int n, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Decimal floating-point remainder
PROTOTYPE:
  UINT128 __bid128_rem (
    UINT128 x, UINT128 y, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Returns the exponent e of x, a signed integral value, determined
  as though x were represented with infinite range and minimum exponent
PROTOTYPE:
  UINT128 __bid128_ilogb (
    UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: Z, I

FUNCTION: Returns x * 10^N
PROTOTYPE:
  UINT128 __bid128_scalbn (
    UINT128 x, int n, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 32-bit decimal floating-point value to 64-bit decimal
  floating-point format (binary encoding)
PROTOTYPE:
  UINT64 __bid32_to_bid64 (
    UINT32 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 32-bit decimal floating-point value to 128-bit decimal
  floating-point format (binary encoding)
PROTOTYPE:
  UINT128 __bid32_to_bid128 (
    UINT32 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 128-bit decimal
  floating-point format (binary encoding)
PROTOTYPE:
  UINT128 __bid64_to_bid128 (
    UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: I

FUNCTION: Convert 64-bit decimal floating-point value to 32-bit decimal
  floating-point format (binary encoding)
PROTOTYPE:
  UINT32 __bid64_to_bid32 (
    UINT64 x, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, I

FUNCTION: Convert 128-bit decimal floating-point value to 32-bit decimal
  floating-point format (binary encoding)
PROTOTYPE:
  UINT32 __bid128_to_bid32 (
    UINT128 x, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, I

FUNCTION: Convert 128-bit decimal floating-point value to 64-bit decimal
  floating-point format (binary encoding)
PROTOTYPE:
  UINT64 __bid128_to_bid64 (
    UINT128 x, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, I

FUNCTION: Convert 64-bit decimal floating-point value (binary encoding)
  to string format (decimal character sequence)
PROTOTYPE:
  void __bid64_to_string (
    char *ps, UINT64 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Convert a decimal floating-point value represented in string format
  (decimal character sequence) to 64-bit decimal floating-point format
  (binary encoding)
PROTOTYPE:
  UINT64 __bid64_from_string (
    char *ps, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O

FUNCTION: Convert 128-bit decimal floating-point value (binary encoding)
  to string format (decimal character sequence)
PROTOTYPE:
  void __bid128_to_string (
    char *str, UINT128 x, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Convert a decimal floating-point value represented in string format
  (decimal character sequence) to 128-bit decimal floating-point format
  (binary encoding)
PROTOTYPE:
  UINT128 __bid128_from_string (
    char *ps, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O

FUNCTION: Quantize(x, y) is a floating-point number in the same format that
  has, if possible, the same numerical value as x and the same quantum
  (unit-in-the-last-place) as y. If the exponent is being increased, rounding
  according to the prevailing rounding-direction mode might occur: the result
  is a different floating-point representation and inexact is signaled if the
  result does not have the same numerical value as x. If the exponent is being
  decreased and the significand of the result would have more than 16 digits,
  invalid is signaled and the result is NaN. If one or both operands are NaN
  the rules for NaNs are followed. Otherwise if only one operand is
  infinite then invalid is signaled and the result is NaN. If both operands
  are infinite then the result is canonical infinity with the sign of x
PROTOTYPE:
  UINT64 __bid64_quantize (
    UINT64 x, UINT64 y, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Quantize(x, y) is a floating-point number in the same format that
  has, if possible, the same numerical value as x and the same quantum
  (unit-in-the-last-place) as y. If the exponent is being increased, rounding
  according to the prevailing rounding-direction mode might occur: the result
  is a different floating-point representation and inexact is signaled if the
  result does not have the same numerical value as x. If the exponent is being
  decreased and the significand of the result would have more than 34 digits,
  invalid is signaled and the result is NaN. If one or both operands are NaN
  the rules for NaNs are followed. Otherwise if only one operand is
  infinite then invalid is signaled and the result is NaN. If both operands
  are infinite then the result is canonical infinity with the sign of x
PROTOTYPE:
  UINT128 __bid128_quantize (
    UINT128 x, UINT128 y, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit binary floating-point value to 32-bit decimal
  floating-point format (binary encoding)
PROTOTYPE:
  UINT32 __binary128_to_bid32 (
    BINARY128 x, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Convert 128-bit binary floating-point value to 64-bit decimal
  floating-point format (binary encoding)
PROTOTYPE:
  UINT64 __binary128_to_bid64 (
                  BINARY128 x, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Convert 128-bit binary floating-point value to 128-bit decimal
  floating-point format (binary encoding)
PROTOTYPE:
  UINT128 __binary128_to_bid128 (
    BINARY128 x, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit binary floating-point value to 32-bit decimal
  floating-point format (binary encoding)
PROTOTYPE:
  UINT32 __binary64_to_bid32 (
    double x, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Convert 64-bit binary floating-point value to 64-bit decimal
  floating-point format (binary encoding)
PROTOTYPE:
  UINT64 __binary64_to_bid64 (
    double x, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit binary floating-point value to 128-bit decimal
  floating-point format (binary encoding)
PROTOTYPE:
  UINT128 __binary64_to_bid128 (
    double x, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 80-bit binary floating-point value to 32-bit decimal
  floating-point format (binary encoding)
PROTOTYPE:
  UINT32 __binary80_to_bid32 (
    BINARY80 x, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Convert 80-bit binary floating-point value to 64-bit decimal
  floating-point format (binary encoding)
PROTOTYPE:
  UINT64 __binary80_to_bid64 (
    BINARY80 x, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Convert 80-bit binary floating-point value to 128-bit decimal
  floating-point format (binary encoding)
PROTOTYPE:
  UINT128 __binary80_to_bid128 (
    BINARY80 x, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 32-bit binary floating-point value to 32-bit decimal
  floating-point format (binary encoding)
PROTOTYPE:
  UINT32 __binary32_to_bid32 (
    float x, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 32-bit binary floating-point value to 64-bit decimal
  floating-point format (binary encoding)
PROTOTYPE:
  UINT64 __binary32_to_bid64 (
    float x, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 32-bit binary floating-point value to 128-bit decimal
  floating-point format (binary encoding)
PROTOTYPE:
  UINT128 __binary32_to_bid128 (
    float x, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 128-bit decimal floating-point value (binary encoding)
  to 32-bit binary floating-point format
PROTOTYPE:
  float __bid128_to_binary32 (
    UINT128 x, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Convert 128-bit decimal floating-point value (binary encoding)
  to 64-bit binary floating-point format
PROTOTYPE:
  double __bid128_to_binary64 (
    UINT128 x, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Convert 128-bit decimal floating-point value (binary encoding)
  to 80-bit binary floating-point format
PROTOTYPE:
  BINARY80 __bid128_to_binary80 (
    UINT128 x, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Convert 128-bit decimal floating-point value (binary encoding)
  to 128-bit binary floating-point format
PROTOTYPE:
  BINARY128 __bid128_to_binary128 (
    UINT128 x, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Convert 64-bit decimal floating-point value (binary encoding)
  to 32-bit binary floating-point format
PROTOTYPE:
  float __bid64_to_binary32 (
    UINT64 x, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Convert 64-bit decimal floating-point value (binary encoding)
  to 64-bit binary floating-point format
PROTOTYPE:
  double __bid64_to_binary64 (
    UINT64 x, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Convert 64-bit decimal floating-point value (binary encoding)
  to 80-bit binary floating-point format
PROTOTYPE:
  BINARY80 __bid64_to_binary80 (
    UINT64 x, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 64-bit decimal floating-point value (binary encoding)
  to 128-bit binary floating-point format
PROTOTYPE:
  BINARY128 __bid64_to_binary128 (
    UINT64 x, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 32-bit decimal floating-point value (binary encoding)
  to 32-bit binary floating-point format
PROTOTYPE:
  float __bid32_to_binary32 (
    UINT32 x, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, I

FUNCTION: Convert 32-bit decimal floating-point value (binary encoding)
  to 64-bit binary floating-point format
PROTOTYPE:
  double __bid32_to_binary64 (
    UINT32 x, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 32-bit decimal floating-point value (binary encoding)
  to 80-bit binary floating-point format
PROTOTYPE:
  BINARY80 __bid32_to_binary80 (
    UINT32 x, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Convert 32-bit decimal floating-point value (binary encoding)
  to 128-bit binary floating-point format
PROTOTYPE:
  BINARY128 __bid32_to_binary128 (
    UINT32 x, _IDEC_round rnd_mode, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, I

FUNCTION: Return true if and only if this programming environment conforms
  to the 1985 version of the standard
PROTOTYPE:
  int __bid_is754 (
    void);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Return true if and only if this programming environment conforms
  to the revised version of the standard
PROTOTYPE:
  int __bid_is754R (
    void);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Signals the exceptions specified in the flagmask operand, which
  can represent any subset of the exceptions
PROTOTYPE:
  void __bid_signalException (
    _IDEC_flags flagsmask, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: P, U, O, Z, I

FUNCTION: Lowers (clears) the flags corresponding to the exceptions specified
  in the flagmask operand, which can represent any subset of the exceptions
PROTOTYPE:
  void __bid_lowerFlags (
    _IDEC_flags flagsmask, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Queries whether any of the flags corresponding to the exceptions
  specified in the flagsmask operand, which can represent any subset of the
  exceptions, are raised
PROTOTYPE:
  _IDEC_flags __bid_testFlags (
    _IDEC_flags flagsmask, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Queries whether any of the flags in the savedflags operand
  corresponding to the exceptions specified in the flagmask operand, which
  can represent any subset of the exceptions, are raised
PROTOTYPE:
  _IDEC_flags __bid_testSavedFlags (
    _IDEC_flags savedflags, _IDEC_flags flagsmask);
FLOATING-POINT EXCEPTIONS: none
FUNCTION: Restores the flags corresponding to the exceptions specified in the
  flagsmask operand, which can represent any subset of the exceptions, to
  their state represented in the flagsvalues operand
PROTOTYPE:
  void __bid_restoreFlags (
    _IDEC_flags flagsvalues, _IDEC_flags flagsmask, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Returns a representation of the state of those flags corresponding
  to the exceptions specified in the flagmask operand
PROTOTYPE:
  _IDEC_flags __bid_saveFlags (
    _IDEC_flags flagsmask, _IDEC_flags *pfpsf);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Gets the prevailing value of the decimal floating-point rounding
  mode. Under constant specification for the rounding mode, it returns
  the constant value. Under dynamic specification for the rounding mode, it
   returns the current value of the dynamic rounding mode variable. Elsewhere,
  the return value is language-defined (and may be unspecified)
PROTOTYPE:
  _IDEC_round __bid_getDecimalRoundingDirection (
    _IDEC_round rnd_mode);
FLOATING-POINT EXCEPTIONS: none

FUNCTION: Sets the value of the dynamic rounding mode variable. The operand
  may be any of the language-defined representations for the default and
  each specific value of the rounding mode. The effect of this operation if
  used outside the static scope of a dynamic specification for the rounding
  mode is language-defined (and may be unspecified)
PROTOTYPE:
  _IDEC_round __bid_setDecimalRoundingDirection (
    _IDEC_round rounding_mode, _IDEC_round rnd_mode);
FLOATING-POINT EXCEPTIONS: none



Functions Added in Release 2.0
____________________________________________

The functions listed below are described in ISO/IEC TR 24732 (a proposed 
extension to the ISO C99 standard).  They are also implemented in the Intel(R) 
Decimal Floating-Point Math Library.  
In general, the maximum ulp error was estimated mathematically to be:
    - below 1 ulp for 32-bit functions
    - below 2 ulps for 64-bit functions
    - below 8 ulps for 128-bit functions
Testing for hundreds of millions of points did not contradict these values. 
A few exceptions exist (notably for the gamma function family):
    - the 32-bit atanh, with measured errors of less than 6 ulps 
    - the 64-bit acosh and atanh, with measured errors of less than 6 ulps
    - the 128-bit sinh, cosh, and erfc, with measured errors of less than 9 ulps
    - the 128-bit tgamma and lgamma functions, whose last 5 digits of the 
      34-digit significand in the result are not reliable
As with the rest of the library, these functions can be built to use a global 
rounding mode and/or global decimal status flags.  Alternatively, they can be 
built to take the rounding mode and a pointer to the status flags as arguments 
(as seen for the functions described in the previous section).
Depending on how the library is built, the arguments and result can be passed 
by value or by reference.

The names used by the implementation differ from the names listed in ISO/IEC 
TR 24732; they are given below (as C comments).   However, the user may easily 
redefine these names by editing the #define statements at the beginning of 
bid_conf.h. 

Below, _Decimal64 stands for BID64;  _Decimal32 stands for BID32 and _Decimal128 
stands for BID128. 

_Decimal64 acosd64(_Decimal64 x);  // library name: __bid64_acos    
_Decimal32 acosd32(_Decimal32 x);  // library name: __bid32_acos
_Decimal128 acosd128(_Decimal128 x);  // library name: __bid128_acos
_Decimal64 asind64(_Decimal64 x);  // library name: __bid64_asin
_Decimal32 asind32(_Decimal32 x);  // library name: __bid32_asin
_Decimal128 asind128(_Decimal128 x);  // library name: __bid128_asin
_Decimal64 atand64(_Decimal64 x);  // library name: __bid64_atan
_Decimal32 atand32(_Decimal32 x);  // library name: __bid32_atan
_Decimal128 atand128(_Decimal128 x);  // library name: __bid128_atan
_Decimal64 atan2d64(_Decimal64 y, _Decimal64 x);  // library name: __bid64_atan2
_Decimal32 atan2d32(_Decimal32 y, _Decimal32 x);  // library name: __bid32_atan2
_Decimal128 atan2d128(_Decimal128 y, _Decimal128 x);  // library name: __bid128_atan2
_Decimal64 cosd64(_Decimal64 x);  // library name: __bid64_cos
_Decimal32 cosd32(_Decimal32 x);  // library name: __bid32_cos
_Decimal128 cosd128(_Decimal128 x);  // library name: __bid128_cos
_Decimal64 sind64(_Decimal64 x);  // library name: __bid64_sin
_Decimal32 sind32(_Decimal32 x);  // library name: __bid32_sin
_Decimal128 sind128(_Decimal128 x);  // library name: __bid128_sin
_Decimal64 tand64(_Decimal64 x);  // library name: __bid64_tan
_Decimal32 tand32(_Decimal32 x);  // library name: __bid32_tan
_Decimal128 tand128(_Decimal128 x);  // library name: __bid128_tan
_Decimal64 acoshd64(_Decimal64 x);  // library name: __bid64_acosh
_Decimal32 acoshd32(_Decimal32 x);  // library name: __bid32_acosh
_Decimal128 acoshd128(_Decimal128 x);  // library name: __bid128_acosh
_Decimal64 asinhd64(_Decimal64 x);  // library name: __bid64_asinh
_Decimal32 asinhd32(_Decimal32 x);  // library name: __bid32_asinh
_Decimal128 asinhd128(_Decimal128 x);  // library name: __bid128_asinh
_Decimal64 atanhd64(_Decimal64 x);  // library name: __bid64_atanh
_Decimal32 atanhd32(_Decimal32 x);  // library name: __bid32_atanh
_Decimal128 atanhd128(_Decimal128 x);  // library name: __bid128_atanh
_Decimal64 coshd64(_Decimal64 x);  // library name: __bid64_cosh
_Decimal32 coshd32(_Decimal32 x);  // library name: __bid32_cosh
_Decimal128 coshd128(_Decimal128 x);  // library name: __bid128_cosh
_Decimal64 sinhd64(_Decimal64 x);  // library name: __bid64_sinh
_Decimal32 sinhd32(_Decimal32 x);  // library name: __bid32_sinh
_Decimal128 sinhd128(_Decimal128 x);  // library name: __bid128_sinh
_Decimal64 tanhd64(_Decimal64 x);  // library name: __bid64_tanh
_Decimal32 tanhd32(_Decimal32 x);  // library name: __bid32_tanh
_Decimal128 tanhd128(_Decimal128 x);  // library name: __bid128_tanh
_Decimal64 expd64(_Decimal64 x);  // library name: __bid64_exp
_Decimal32 expd32(_Decimal32 x);  // library name: __bid32_exp
_Decimal128 expd128(_Decimal128 x);  // library name: __bid128_exp
_Decimal64 exp2d64(_Decimal64 x);  // library name: __bid64_exp2
_Decimal32 exp2d32(_Decimal32 x);  // library name: __bid32_exp2
_Decimal128 exp2d128(_Decimal128 x);  // library name: __bid128_exp2
_Decimal64 expm1d64(_Decimal64 x);  // library name: __bid64_expm1
_Decimal32 expm1d32(_Decimal32 x);  // library name: __bid32_expm1
_Decimal128 expm1d128(_Decimal128 x);  // library name: __bid128_expm1
_Decimal64 frexpd64(_Decimal64 value, int *exp);  // library name: __bid64_frexp
_Decimal32 frexpd32(_Decimal32 value, int *exp);  // library name: __bid32_frexp
_Decimal128 frexpd128(_Decimal128 value, int *exp);  // library name: __bid128_frexp
_Decimal64 ldexpd64(_Decimal64 x, int exp);  // library name: __bid64_ldexp
_Decimal32 ldexpd32(_Decimal32 x, int exp);  // library name: __bid32_ldexp
_Decimal128 ldexpd128(_Decimal128 x, int exp);  // library name: __bid128_ldexp
_Decimal64 logd64(_Decimal64 x);  // library name: __bid64_log
_Decimal32 logd32(_Decimal32 x);  // library name: __bid32_log
_Decimal128 logd128(_Decimal128 x);  // library name: __bid128_log
_Decimal64 log10d64(_Decimal64 x);  // library name: __bid64_log10
_Decimal32 log10d32(_Decimal32 x);  // library name: __bid32_log10
_Decimal128 log10d128(_Decimal128 x);  // library name: __bid128_log10
_Decimal64 log1pd64(_Decimal64 x);  // library name: __bid64_log1p
_Decimal32 log1pd32(_Decimal32 x);  // library name: __bid32_log1p
_Decimal128 log1pd128(_Decimal128 x);  // library name: __bid128_log1p
_Decimal64 log2d64(_Decimal64 x);  // library name: __bid64_log2
_Decimal32 log2d32(_Decimal32 x);  // library name: __bid32_log2
_Decimal128 log2d128(_Decimal128 x);  // library name: __bid128_log2
_Decimal64 modfd64(_Decimal64 value, _Decimal64 *iptr);  // library name: __bid64_modf
_Decimal32 modfd32(_Decimal32 value, _Decimal32 *iptr);  // library name: __bid32_modf
_Decimal128 modfd128(_Decimal128 value, _Decimal128 *iptr);  // library name: __bid128_modf
_Decimal64 scalblnd64(_Decimal64 x, long int n);  // library name: __bid64_scalbln
_Decimal32 scalblnd32(_Decimal32 x, long int n);  // library name: __bid32_scalbln
_Decimal128 scalblnd128(_Decimal128 x, long int n);  // library name: __bid128_scalbln
_Decimal64 cbrtd64(_Decimal64 x);  // library name: __bid64_cbrt
_Decimal32 cbrtd32(_Decimal32 x);  // library name: __bid32_cbrt
_Decimal128 cbrtd128(_Decimal128 x);  // library name: __bid128_cbrt
_Decimal64 fabsd64(_Decimal64 x);  // library name: __bid64_abs
_Decimal32 fabsd32(_Decimal32 x);  // library name: __bid32_abs
_Decimal128 fabsd128(_Decimal128 x);  // library name: __bid128_abs
_Decimal64 hypotd64(_Decimal64 x, _Decimal64 y);  // library name: __bid64_hypot
_Decimal32 hypotd32(_Decimal32 x, _Decimal32 y);  // library name: __bid32_hypot
_Decimal128 hypotd128(_Decimal128 x, _Decimal128 y);  // library name: __bid128_hypot
_Decimal64 powd64(_Decimal64 x, _Decimal64 y);  // library name: __bid64_pow
_Decimal32 powd32(_Decimal32 x, _Decimal32 y);  // library name: __bid32_pow
_Decimal128 powd128(_Decimal128 x, _Decimal128 y);  // library name: __bid128_pow
_Decimal64 erfd64(_Decimal64 x);  // library name: __bid64_erf
_Decimal32 erfd32(_Decimal32 x);  // library name: __bid32_erf
_Decimal128 erfd128(_Decimal128 x);  // library name: __bid128_erf
_Decimal64 erfcd64(_Decimal64 x);  // library name: __bid64_erfc
_Decimal32 erfcd32(_Decimal32 x);  // library name: __bid32_erfc
_Decimal128 erfcd128(_Decimal128 x);  // library name: __bid128_erfc
_Decimal64 lgammad64(_Decimal64 x);  // library name: __bid64_lgamma
_Decimal32 lgammad32(_Decimal32 x);  // library name: __bid32_lgamma
_Decimal128 lgammad128(_Decimal128 x);  // library name: __bid128_lgamma
_Decimal64 tgammad64(_Decimal64 x);  // library name: __bid64_tgamma
_Decimal32 tgammad32(_Decimal32 x);  // library name: __bid32_tgamma
_Decimal128 tgammad128(_Decimal128 x);  // library name: __bid128_tgamma
_Decimal64 ceild64(_Decimal64 x);  // library name: __bid64_ceil
_Decimal32 ceild32(_Decimal32 x);  // library name: __bid32_ceil
_Decimal128 ceild128(_Decimal128 x);  // library name: __bid128_ceil
_Decimal64 floord64(_Decimal64 x);  // library name: __bid64_floor
_Decimal32 floord32(_Decimal32 x);  // library name: __bid32_floor
_Decimal128 floord128(_Decimal128 x);  // library name: __bid128_floor
_Decimal64 nearbyintd64(_Decimal64 x);  // library name: __bid64_nearbyint
_Decimal32 nearbyintd32(_Decimal32 x);  // library name: __bid32_nearbyint
_Decimal128 nearbyintd128(_Decimal128 x);  // library name: __bid128_nearbyint
long int lrintd64(_Decimal64 x);  // library name: __bid64_lrint
long int lrintd32(_Decimal32 x);  // library name: __bid32_lrint
long int lrintd128(_Decimal128 x);  // library name: __bid128_lrint
long long int llrintd64(_Decimal64 x);  // library name: __bid64_llrint
long long int llrintd32(_Decimal32 x);  // library name: __bid32_llrint
long long int llrintd128(_Decimal128 x);  // library name: __bid128_llrint
long int lroundd64(_Decimal64 x);  // library name: __bid64_lround
long int lroundd32(_Decimal32 x);  // library name: __bid32_lround
long int lroundd128(_Decimal128 x);  // library name: __bid128_lround
long long int llroundd64(_Decimal64 x);  // library name: __bid64_llround
long long int llroundd32(_Decimal32 x);  // library name: __bid32_llround
long long int llroundd128(_Decimal128 x);  // library name: __bid128_llround
_Decimal64 nexttowardd64(_Decimal64 x, _Decimal128 y);  // library name: __bid64_nexttoward
_Decimal32 nexttowardd32(_Decimal32 x, _Decimal128 y);  // library name: __bid32_nexttoward
_Decimal128 nexttowardd128(_Decimal128 x, _Decimal128 y);  // library name: __bid128_nexttoward
_Decimal64 fdimd64(_Decimal64 x, _Decimal64 y);  // library name: __bid64_fdim
_Decimal32 fdimd32(_Decimal32 x, _Decimal32 y);  // library name: __bid32_fdim
_Decimal128 fdimd128(_Decimal128 x, _Decimal128 y);  // library name: __bid128_fdim


Calling Transcendental Functions
_________________________________

Transcendental function prototypes are similar to those of the basic decimal
functions, so they are called in a similar manner.
All function prototypes can be found in bid_functions.h.

As an example, consider the following code from bid_functions.h (also consult
bid_conf.h, where the user can rename functions via #define directives):
#if DECIMAL_CALL_BY_REFERENCE
....
     BID_EXTERN_C void bid64_exp (BID_UINT64 * pres, BID_UINT64 * px
                            _RND_MODE_PARAM _EXC_FLAGS_PARAM
                            _EXC_MASKS_PARAM _EXC_INFO_PARAM);
....
     BID_EXTERN_C void bid128_pow (BID_UINT128 * pres, BID_UINT128 * px, BID_UINT128 * py
                            _RND_MODE_PARAM _EXC_FLAGS_PARAM
                            _EXC_MASKS_PARAM _EXC_INFO_PARAM);
....
#else
....
     BID_EXTERN_C BID_UINT64 bid64_exp (BID_UINT64 x
                              _RND_MODE_PARAM _EXC_FLAGS_PARAM
                              _EXC_MASKS_PARAM _EXC_INFO_PARAM);
....
     BID_EXTERN_C BID_UINT128 bid128_pow (BID_UINT128 x, BID_UINT128 y
                              _RND_MODE_PARAM _EXC_FLAGS_PARAM
                              _EXC_MASKS_PARAM _EXC_INFO_PARAM);
....
#endif

Consider also the following code from bid_conf.h:
....  #define bid64_exp         __bid64_exp
....
#define bid128_pow        __bid128_pow
...

The code examples provided with this package (in the EXAMPLES directory) 
show how to call __bid128_mul(), and can be followed for transcendental 
functions as well.

Here are two simple examples, to compute z=bid128_pow(x,y) and b=bid64_exp(a):

  Decimal128 x, y, z;
  Decimal64 a, b;

  // The user must initialize input arguments x, y, a

  // Call sequences, assuming the library is built using:
  //  DECIMAL_CALL_BY_REFERENCE=1 (arguments passed by reference) 
  //  DECIMAL_GLOBAL_ROUNDING=0 (rounding mode passed as argument to function)
  //  DECIMAL_GLOBAL_EXCEPTION_FLAGS=0 (status flags passed as argument)
  // Need to declare and initialize rounding mode and status flags variables
  _IDEC_round my_rnd_mode = _IDEC_dflround;
  _IDEC_flags my_fpsf = _IDEC_allflagsclear;
  .....
  __bid128_pow (&z, &x, &y, &my_rnd_mode, &my_fpsf);
  __bid64_exp (&b, &a, &my_rnd_mode, &my_fpsf);

  // Call sequences, assuming the library is built using:
  //  DECIMAL_CALL_BY_REFERENCE=0 (arguments passed by value) 
  //  DECIMAL_GLOBAL_ROUNDING=1 (rounding mode stored in global variable)
  //  DECIMAL_GLOBAL_EXCEPTION_FLAGS=1 (status flags stored in global variable)
  z = __bid128_pow (x, y);
  b = __bid64_exp (a);

  For more details, including how to access the global rounding mode and 
status flags variables and how to call decimal functions when the library is 
built using any of the 8 combinations specified by DECIMAL_CALL_BY_REFERENCE, 
DECIMAL_GLOBAL_ROUNDING, and DECIMAL_GLOBAL_EXCEPTION_FLAGS, please see the 
EXAMPLES directory.


Footnotes:
==========
* BID stands for Binary Integer Decimal, which is an informal name for
the binary encoding format of decimal floating-point values, described in the
IEEE Standard 754-2008.

** Other names and brands may be claimed as the property of others.

*** Microsoft, Windows, and the Windows logo are trademarks, or registered
trademarks of Microsoft Corporation in the United States and/or other countries


Note 1:
=======
  Functions operating on the BID32 format are implemented, but some are not 
  listed here (for example bid32_add). See the prototypes in 
  LIBRARY/bid_functions.h for a complete list of the library functions.

Note 2:
=======
  UNCHANGED_BINARY_STATUS_FLAGS allows for prevention of binary flag pollution 

To build readtest - the tests for the Intel(R) Decimal Floating-Point Math 
Library v2.0 on processors that are implementations of the 
IA-32 Architecture, Intel(R) 64, or IA-64 Architecture:  

  In Linux* with icc (Intel(R) C++ Compiler 9.1 or newer) or gcc:

    make clean OS_TYPE=LINUX
    make OS_TYPE=LINUX CC=icc CALL_BY_REF=0 GLOBAL_RND=0 GLOBAL_FLAGS=0 UNCHANGED_BINARY_FLAGS=0
      - CC can be icc, gcc
      - CALL_BY_REF, GLOBAL_RND, GLOBAL_FLAGS, UNCHANGED_BINARY_FLAGS can be any of 0000, 0001, ... , 1111

  In Windows** with icl (Intel(R) C++ Compiler 9.1 or newer) or cl (Microsoft
  Visual C++ Compiler**):  

    nmake clean OS_TYPE=WIN
    nmake -fmakefile.mak CC=icl CALL_BY_REF=0 GLOBAL_RND=0 GLOBAL_FLAGS=0 UNCHANGED_BINARY_FLAGS=0
      -  CC can be cl, icl; EXCEPTION for Itanium when CC=cl: OS_TYPE=WIN_IA64
      -  CALL_BY_REF, GLOBAL_RND, GLOBAL_FLAGS, UNCHANGED_BINARY_FLAGS can be any of 0000, 0001, ... , 1111
      -  [g]make which stands for a GNU make-compatible make program (e.g. make from
         cygwin) can also be used

    Note: The scripts and makefiles provided here may need adjustments, 
        depending on the environment in which they are used; for example if 
        moving files from Windows to Linux, running dos2unix on the Linux 
        script files may be necessary.

To run readtest:
    ./readtest < readtest.in (Linux)
    readtest < readtest.in (Windows)     

Note: 
=====
  For some other operating systems and architecture combinations see the
  following command files, as well as any command files invoked from these ones:
        RUNLINUX
        RUNWINDOWS_nmake.bat
        RUNWINDOWSINTEL64.bat (for Itanium Architecture)
        RUNOSX
        RUNOSXINTEL64 (for Itanium Architecture)
        RUNSOLARIS
        RUNHPUX32 (for HP-UX* on IA-64 Architecture, 32-bit data mode) 
        RUNHPUX64 (for HP-UX* on IA-64 Architecture, 64-bit data mode)
  These command files build and run the tests from this directory,
  possibly using more than one compiler. Changes may be necessary in certain
  environments. However, prior to building these tests the similar RUN*
  command has to be executed in ../LIBRARY/ in order to build all the 
  necessary versions of the Intel(R) Decimal Floating-Point Math Library.
  The tests [when built correctly] pass if the word FAIL does not appear in
  the output. Note that failures may possibly occur due to incorrect code 
  generated by a compiler.


Note:
=====
If the makefile provided here is not used, the parameter passing method and  
local/global rounding mode and status flags may be selected by editing  
test_bid_conf.h:

Parameter passing is determined by an environment variable in test_bid_conf.h:
  - by value:
        #define DECIMAL_CALL_BY_REFERENCE 0
  - by reference:
        #define DECIMAL_CALL_BY_REFERENCE 1
 
Global variables are determined by two environment variables in test_bid_conf.h:
  - rnd_mode passed as parameter
        #define DECIMAL_GLOBAL_ROUNDING 0
  - rnd_mode global
        #define DECIMAL_GLOBAL_ROUNDING 1
  - status flags *pfpsf passed as parameter
        #define DECIMAL_GLOBAL_EXCEPTION_FLAGS 0
  - status flags *pfpsf global
        #define DECIMAL_GLOBAL_EXCEPTION_FLAGS 1

For more information see ../README

* Other names and brands may be claimed as the property of others.

** Microsoft, Windows, and the Windows logo are trademarks, or registered 
trademarks of Microsoft Corporation in the United States and/or other countries

Note: 000, 001, ..., 111 are associated with the following three conditions:

bit 2 [msb]: 0 = call by value (except for the pointer to the status flags, 
                 passed by reference unless global)
             1 = call by reference;
bit 1      : 0 = rounding mode passed as a parameter
             1 = rounding mode passed in global variable _IDEC_glbround 
                 (fixed name)
bit 0 [lsb]: 0 = pointer to status flags passed as a parameter
             1 = status flags passed in global variable _IDEC_glbflags 
                 (fixed name)

Example (one of eight possible, for Linux only; similar for other OS-es):

Build libbid.a in ../LIBRARY with '...CALL_BY_REF=0 GLOBAL_RND=0 GLOBAL_FLAGS=0'
$ cp main.c_000 main.c
$ cp decimal.h_000 decimal.h
$ icc main.c ../LIBRARY/libbid.a
$ ./a.out 
Begin Decimal Floating-Point Sanity Check
TEST CASE 1 FOR bid128_mul 000 () PASSED
TEST CASE 2 FOR bid128_mul 000 () PASSED
TEST CASE 3 FOR bid128_mul 000 () PASSED
End Decimal Floating-Point Sanity Check
$ rm main.c decimal.h a.out

    Note: The scripts and makefiles provided here may need adjustments, 
        depending on the environment in which they are used; for example if 
        moving files from Windows to Linux, running dos2unix on the Linux 
        script files may be necessary.

Note: For some other operating systems and architecture combinations see the 
  following command files, as well as any command files invoked from these ones:
	RUNLINUX
	RUNWINDOWS.bat
	RUNWINDOWSINTEL64.bat (for IA-64 Architecture)
	RUNOSX
	RUNOSXINTEL64 (for IA-64 Architecture)
	RUNSOLARIS
        RUNHPUX32 (for HP-UX* on IA-64 Architecture, 32-bit data mode)
        RUNHPUX64 (for HP-UX* on IA-64 Architecture, 64-bit data mode)
  These command files build and run all eight examples from this directory,
  possibly using more than one compiler. Changes may be needed for certain
  environments. However, prior to building these examples the similar RUN*
  command has to be executed in ../LIBRARY/ in order to build all the
  necessary versions of the Intel(R) Decimal Floating-Point Math Library
  v1.0 Update 1.
  The tests [when built correctly] pass if the word FAIL does not appear in
  the output.

* Other names and brands may be claimed as the property of others.

To build the Intel(R) Decimal Floating-Point Math Library v2.0
(conforming to the IEEE Standard 754-2008 for Floating-Point Arithmetic) 
on processors that are implementations of the IA-32 Architecture, Intel(R) 64, 
or IA-64 Architecture:

  In Linux* with icc (Intel(R) Compiler 9.1 or newer) or gcc:

    make clean  
    make CC=icc CALL_BY_REF=0 GLOBAL_RND=0 GLOBAL_FLAGS=0 UNCHANGED_BINARY_FLAGS=0
      - CC can be icc, gcc
      - CALL_BY_REF, GLOBAL_RND, GLOBAL_FLAGS, UNCHANGED_BINARY_FLAGS can be any of 0000, 0001, ... , 1111

  Big-endian builds require some additional command line parameters (see the
  following files for examples: solarisbuild, hpuxbuild*)
 
  In Windows** with icl (Intel(R) C++ Compiler 9.1 or newer) or cl (Microsoft
  Visual C++ Compiler**):

    nmake clean 
    nmake -fmakefile.mak CC=icl CALL_BY_REF=0 GLOBAL_RND=0 GLOBAL_FLAGS=0 UNCHANGED_BINARY_FLAGS=0
      -  CC can be cl, icl
      -  CALL_BY_REF, GLOBAL_RND, GLOBAL_FLAGS, UNCHANGED_BINARY_FLAGS can be any of 0000, 0001, ... , 1111
      -  [g]make, which stands for a GNU make-compatible make program (e.g. make from
         cygwin) may also be used
    
    Note: The scripts and makefiles provided here may need adjustments, 
        depending on the environment in which they are used; for example if 
        moving files from Windows to Linux, running dos2unix on the Linux 
        script files may be necessary.

     The makefiles currently support these environments, but can be extended to 
  support additional ones (such as a new Cygwin release):  Linux, FreeBSD,  
  Darwin, SunOS, HP-UX, Windows_NT, CYGWIN_NT-5.1, CYGWIN_NT-5.2-WOW64, 
  CYGWIN_NT-6.1-WOW64.
  See makefile.iml_head (line 330) for more information.

Note:
=====
  For some other operating systems and architecture combinations see the
  following command files, as well as any command files invoked from these ones:
        RUNLINUX
        RUNWINDOWS_nmake.bat
        RUNWINDOWSINTEL64.bat (for IA-64 Architecture)
        RUNOSX
        RUNOSXINTEL64 (for IA-64) Architecture
        RUNSOLARIS
        RUNHPUX32 (for HP-UX* on IA-64 Architecture, 32-bit data mode)
        RUNHPUX64 (for HP-UX* on IA-64 Architecture, 64-bit data mode)
  These command files build the Intel(R) Decimal Floating-Point Math Library,
  possibly using more than one compiler. Changes may be necessary in certain
  environments. Note that all the necessary versions of the Intel(R) Decimal 
  Floating-Point Math Library have to be built in this directory prior to
  executing the similar RUN* command in either of ../LIBRARY/ or ../TESTS/.
  Check that all the expected *.a files (or *.lib in Windows) have been created
  prior to building and running the tests or examples from ../LIBRARY/ or 
  ../TESTS/.

Note:
=====
If the makefile provided here is not used, the parameter passing method and 
local/global rounding mode and status flags may be selected by editing 
bid_conf.h:
 
Parameter passing is determined by an environment variable in bid_conf.h:
  - by value:
        #define DECIMAL_CALL_BY_REFERENCE 0
  - by reference:
        #define DECIMAL_CALL_BY_REFERENCE 1
 
Global variables are determined by two environment variables in bid_conf.h:
  - rnd_mode passed as parameter
        #define DECIMAL_GLOBAL_ROUNDING 0
  - rnd_mode global
        #define DECIMAL_GLOBAL_ROUNDING 1
  - status flags *pfpsf passed as parameter
        #define DECIMAL_GLOBAL_EXCEPTION_FLAGS 0
  - status flags *pfpsf global
        #define DECIMAL_GLOBAL_EXCEPTION_FLAGS 1
 
For more information see ../README
 
 
 
* Other names and brands may be claimed as the property of others.
 
** Microsoft, Windows, and the Windows logo are trademarks, or registered
trademarks of Microsoft Corporation in the United States and/or other countries

timelib
=======

Timelib is a timezone and date/time library that can calculate local time,
convert between timezones and parse textual descriptions of date/time
information.

It is the library supporting PHP's Date/Time extension and MongoDB's time zone
support.
Building the timezone files
---------------------------

The building of files is done through the ``Makefile`` with:

- ``make clean`` (important if data files have changed)
- ``make release-pecl`` (PECL timezonedb extension)
- ``make release-docs`` (documentation updates)
- ``make release-php`` (changes to embed database in PHP)

It has the following prerequisites:

- The directory contains **one** ``tzcode2014i.tar.gz`` file and **one**
  ``tzdata2014i.tar.gz`` file.
- You have a PECL SVN checkout in ``~/dev/php/pecl``
- You have a PHPDOC GIT checkout in ``~/dev/php/phpdoc``
- You can commit to PHP's GIT ``php-src`` repository.
- You can commit to PHP's GIT ``doc-base`` and ``doc-en`` repositories.
- You can commit to PECL's SVN repository.
- ``php`` is in your path.

Do not run this script, unless you're Derick Rethans.
ZLIB DATA COMPRESSION LIBRARY

zlib 1.2.11 is a general purpose data compression library.  All the code is
thread safe.  The data format used by the zlib library is described by RFCs
(Request for Comments) 1950 to 1952 in the files
http://tools.ietf.org/html/rfc1950 (zlib format), rfc1951 (deflate format) and
rfc1952 (gzip format).

All functions of the compression library are documented in the file zlib.h
(volunteer to write man pages welcome, contact zlib@gzip.org).  A usage example
of the library is given in the file test/example.c which also tests that
the library is working correctly.  Another example is given in the file
test/minigzip.c.  The compression library itself is composed of all source
files in the root directory.

To compile all files and run the test program, follow the instructions given at
the top of Makefile.in.  In short "./configure; make test", and if that goes
well, "make install" should work for most flavors of Unix.  For Windows, use
one of the special makefiles in win32/ or contrib/vstudio/ .  For VMS, use
make_vms.com.

Questions about zlib should be sent to <zlib@gzip.org>, or to Gilles Vollant
<info@winimage.com> for the Windows DLL version.  The zlib home page is
http://zlib.net/ .  Before reporting a problem, please check this site to
verify that you have the latest version of zlib; otherwise get the latest
version and check whether the problem still exists or not.

PLEASE read the zlib FAQ http://zlib.net/zlib_faq.html before asking for help.

Mark Nelson <markn@ieee.org> wrote an article about zlib for the Jan.  1997
issue of Dr.  Dobb's Journal; a copy of the article is available at
http://marknelson.us/1997/01/01/zlib-engine/ .

The changes made in version 1.2.11 are documented in the file ChangeLog.

Unsupported third party contributions are provided in directory contrib/ .

zlib is available in Java using the java.util.zip package, documented at
http://java.sun.com/developer/technicalArticles/Programming/compression/ .

A Perl interface to zlib written by Paul Marquess <pmqs@cpan.org> is available
at CPAN (Comprehensive Perl Archive Network) sites, including
http://search.cpan.org/~pmqs/IO-Compress-Zlib/ .

A Python interface to zlib written by A.M. Kuchling <amk@amk.ca> is
available in Python 1.5 and later versions, see
http://docs.python.org/library/zlib.html .

zlib is built into tcl: http://wiki.tcl.tk/4610 .

An experimental package to read and write files in .zip format, written on top
of zlib by Gilles Vollant <info@winimage.com>, is available in the
contrib/minizip directory of zlib.


Notes for some targets:

- For Windows DLL versions, please see win32/DLL_FAQ.txt

- For 64-bit Irix, deflate.c must be compiled without any optimization. With
  -O, one libpng test fails. The test works in 32 bit mode (with the -n32
  compiler flag). The compiler bug has been reported to SGI.

- zlib doesn't work with gcc 2.6.3 on a DEC 3000/300LX under OSF/1 2.1 it works
  when compiled with cc.

- On Digital Unix 4.0D (formely OSF/1) on AlphaServer, the cc option -std1 is
  necessary to get gzprintf working correctly. This is done by configure.

- zlib doesn't work on HP-UX 9.05 with some versions of /bin/cc. It works with
  other compilers. Use "make test" to check your compiler.

- gzdopen is not supported on RISCOS or BEOS.

- For PalmOs, see http://palmzlib.sourceforge.net/


Acknowledgments:

  The deflate format used by zlib was defined by Phil Katz.  The deflate and
  zlib specifications were written by L.  Peter Deutsch.  Thanks to all the
  people who reported problems and suggested various improvements in zlib; they
  are too numerous to cite here.

Copyright notice:

 (C) 1995-2017 Jean-loup Gailly and Mark Adler

  This software is provided 'as-is', without any express or implied
  warranty.  In no event will the authors be held liable for any damages
  arising from the use of this software.

  Permission is granted to anyone to use this software for any purpose,
  including commercial applications, and to alter it and redistribute it
  freely, subject to the following restrictions:

  1. The origin of this software must not be misrepresented; you must not
     claim that you wrote the original software. If you use this software
     in a product, an acknowledgment in the product documentation would be
     appreciated but is not required.
  2. Altered source versions must be plainly marked as such, and must not be
     misrepresented as being the original software.
  3. This notice may not be removed or altered from any source distribution.

  Jean-loup Gailly        Mark Adler
  jloup@gzip.org          madler@alumni.caltech.edu

If you use the zlib library in a product, we would appreciate *not* receiving
lengthy legal documents to sign.  The sources are provided for free but without
warranty of any kind.  The library has been entirely written by Jean-loup
Gailly and Mark Adler; it does not include third-party code.

If you redistribute modified sources, we would appreciate that you include in
the file ChangeLog history information documenting your changes.  Please read
the FAQ for more information on the distribution of modified source versions.
# MPark.Variant

> __C++17__ `std::variant` for __C++11__/__14__/__17__

[![release][badge.release]][release]
[![header][badge.header]][header]
[![travis][badge.travis]][travis]
[![appveyor][badge.appveyor]][appveyor]
[![license][badge.license]][license]
[![godbolt][badge.godbolt]][godbolt]
[![wandbox][badge.wandbox]][wandbox]

[badge.release]: https://img.shields.io/github/release/mpark/variant.svg
[badge.header]: https://img.shields.io/badge/single%20header-master-blue.svg
[badge.travis]: https://travis-ci.org/mpark/variant.svg?branch=master
[badge.appveyor]: https://ci.appveyor.com/api/projects/status/github/mpark/variant?branch=master&svg=true
[badge.license]: https://img.shields.io/badge/license-boost-blue.svg
[badge.godbolt]: https://img.shields.io/badge/try%20it-on%20godbolt-222266.svg
[badge.wandbox]: https://img.shields.io/badge/try%20it-on%20wandbox-5cb85c.svg

[release]: https://github.com/mpark/variant/releases/latest
[header]: https://github.com/mpark/variant/blob/single-header/master/variant.hpp
[travis]: https://travis-ci.org/mpark/variant
[appveyor]: https://ci.appveyor.com/project/mpark/variant
[license]: https://github.com/mpark/variant/blob/master/LICENSE.md
[godbolt]: https://godbolt.org/g/1qYDAK
[wandbox]: https://wandbox.org/permlink/QV3gZ2KQQNwgoFIB

## Introduction

__MPark.Variant__ is an implementation of __C++17__ `std::variant` for __C++11__/__14__/__17__.

  - Based on [my implementation of `std::variant` for __libc++__][libcxx-impl]
  - Continuously tested against __libc++__'s `std::variant` test suite.

[libcxx-impl]: https://reviews.llvm.org/rL288547

## Documentation

  - [cppreference.com](http://en.cppreference.com/w/cpp/utility/variant)
  - [eel.is/c++draft](http://eel.is/c++draft/variant)

## Integration

### Single Header

The [single-header] branch provides a standalone `variant.hpp`
file for each [release](https://github.com/mpark/variant/releases).
Copy it and `#include` away!

[single-header]: https://github.com/mpark/variant/tree/single-header

### Submodule

You can add `mpark/variant` as a submodule to your project.

```bash
git submodule add https://github.com/mpark/variant.git 3rdparty/variant
```

Add the `include` directory to your include path with
`-I3rdparty/variant/include` then `#include` the `variant.hpp` header
with `#include <mpark/variant.hpp>`.

If you use CMake, you can simply use `add_subdirectory(3rdparty/variant)`:

```cmake
cmake_minimum_required(VERSION 3.6.3)

project(HelloWorld CXX)

add_subdirectory(3rdparty/variant)

add_executable(hello-world hello_world.cpp)
target_link_libraries(hello-world mpark_variant)
```

### Installation / CMake `find_package`

```bash
git clone https://github.com/mpark/variant.git
mkdir variant/build && cd variant/build
cmake ..
cmake --build . --target install
```

This will install `mpark/variant` to the default install-directory for
your platform (`/usr/local` for Unix, `C:\Program Files` for Windows).
You can also install at a custom location via the `CMAKE_INSTALL_PREFIX`
variable, (e.g., `cmake .. -DCMAKE_INSTALL_PREFIX=/opt`).

The installed `mpark/variant` can then be found by CMake via `find_package`:

```cmake
cmake_minimum_required(VERSION 3.6.3)

project(HelloWorld CXX)

find_package(mpark_variant 1.3.0 REQUIRED)

add_executable(hello-world hello_world.cpp)
target_link_libraries(hello-world mpark_variant)
```

CMake will search for `mpark/variant` in its default set of
installation prefixes. If `mpark/variant` is installed in
a custom location via the `CMAKE_INSTALL_PREFIX` variable,
you'll likely need to use the `CMAKE_PREFIX_PATH` to specify
the location (e.g., `cmake .. -DCMAKE_PREFIX_PATH=/opt`).

## Requirements

This library requires a standard conformant __C++11__ compiler.
The following compilers are continously tested:

| Compiler                               | Operating System                            | Version String                                                                             |
| -------------------------------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------ |
| GCC 4.8.5                              | Ubuntu 14.04.5 LTS                          | g++-4.8 (Ubuntu 4.8.5-2ubuntu1~14.04.1) 4.8.5                                              |
| GCC 4.9.4                              | Ubuntu 14.04.5 LTS                          | g++-4.9 (Ubuntu 4.9.4-2ubuntu1~14.04.1) 4.9.4                                              |
| GCC 5.4.1                              | Ubuntu 14.04.5 LTS                          | g++-5 (Ubuntu 5.4.1-2ubuntu1~14.04) 5.4.1 20160904                                         |
| GCC 6.3.0                              | Ubuntu 14.04.5 LTS                          | g++-6 (Ubuntu/Linaro 6.3.0-18ubuntu2~14.04) 6.3.0 20170519                                 |
| GCC 7.2.0                              | Ubuntu 14.04.5 LTS                          | g++-7 (Ubuntu 7.2.0-1ubuntu1~14.04) 7.2.0                                                  |
| Clang 3.5.0                            | Ubuntu 14.04.5 LTS                          | Ubuntu clang version 3.5.0-4ubuntu2~trusty2 (tags/RELEASE_350/final) (based on LLVM 3.5.0) |
| Clang 3.6.2                            | Ubuntu 14.04.5 LTS                          | Ubuntu clang version 3.6.2-svn240577-1~exp1 (branches/release_36) (based on LLVM 3.6.2)    |
| Clang 3.7.1                            | Ubuntu 14.04.5 LTS                          | Ubuntu clang version 3.7.1-svn253571-1~exp1 (branches/release_37) (based on LLVM 3.7.1)    |
| Clang 3.8.0                            | Ubuntu 14.04.5 LTS                          | clang version 3.8.0-2ubuntu3~trusty5 (tags/RELEASE_380/final)                              |
| Clang 3.9.1                            | Ubuntu 14.04.5 LTS                          | clang version 3.9.1-4ubuntu3~14.04.2 (tags/RELEASE_391/rc2)                                |
| Clang 4.0.1                            | Ubuntu 14.04.5 LTS                          | clang version 4.0.1-svn305264-1~exp1 (branches/release_40)                                 |
| Clang 5.0.0                            | Ubuntu 14.04.5 LTS                          | clang version 5.0.0-svn312333-1~exp1 (branches/release_50)                                 |
| Clang Xcode 6.4                        | Darwin Kernel Version 14.5.0 (OS X 10.10.3) | Apple LLVM version 6.1.0 (clang-602.0.53) (based on LLVM 3.6.0svn)                         |
| Clang Xcode 7.3                        | Darwin Kernel Version 15.6.0 (OS X 10.10.5) | Apple LLVM version 7.3.0 (clang-703.0.31)                                                  |
| Clang Xcode 8.3                        | Darwin Kernel Version 16.6.0 (OS X 10.12.5) | Apple LLVM version 8.1.0 (clang-802.0.42)                                                  |
| Visual Studio 14 2015                  | Visual Studio 2015 with Update 3            | MSVC 19.0.24215.1  | Microsoft (R) Build Engine version 14.0.25420.1                       |
| Visual Studio 15 2017                  | Visual Studio 2017                          | MSVC 19.11.25547.0 | Microsoft (R) Build Engine version 15.4.8.50001                       |
| Visual Studio 14 2015 (__Clang/LLVM__) | Visual Studio 2015 with Update 3            | Clang 4.0.0        | Microsoft (R) Build Engine version 14.0.25420.1                       |

#### NOTES
  - __GCC 4.8__/__4.9__: `constexpr` support is not available for `visit` and relational operators.
  - Enabling __libc++__ `std::variant` tests require `-std=c++17` support.

## CMake Variables

  -  __`MPARK_VARIANT_INCLUDE_TESTS`__:`STRING` (__default__: `""`)

     Semicolon-separated list of tests to build.
     Possible values are `mpark`, and `libc++`.

     __NOTE__: The __libc++__ `std::variant` tests are built with `-std=c++17`.

## Unit Tests

Refer to [test/README.md](test/README.md).

## License

Distributed under the [Boost Software License, Version 1.0](LICENSE.md).
# MPark.Variant

> __C++17__ `std::variant` for __C++11__/__14__/__17__

[![release][badge.release]][release]
[![header][badge.header]][header]
[![travis][badge.travis]][travis]
[![appveyor][badge.appveyor]][appveyor]
[![license][badge.license]][license]
[![godbolt][badge.godbolt]][godbolt]
[![wandbox][badge.wandbox]][wandbox]

[badge.release]: https://img.shields.io/github/release/mpark/variant.svg
[badge.header]: https://img.shields.io/badge/single%20header-master-blue.svg
[badge.travis]: https://travis-ci.org/mpark/variant.svg?branch=master
[badge.appveyor]: https://ci.appveyor.com/api/projects/status/github/mpark/variant?branch=master&svg=true
[badge.license]: https://img.shields.io/badge/license-boost-blue.svg
[badge.godbolt]: https://img.shields.io/badge/try%20it-on%20godbolt-222266.svg
[badge.wandbox]: https://img.shields.io/badge/try%20it-on%20wandbox-5cb85c.svg

[release]: https://github.com/mpark/variant/releases/latest
[header]: https://github.com/mpark/variant/blob/single-header/master/variant.hpp
[travis]: https://travis-ci.org/mpark/variant
[appveyor]: https://ci.appveyor.com/project/mpark/variant
[license]: https://github.com/mpark/variant/blob/master/LICENSE.md
[godbolt]: https://godbolt.org/g/1qYDAK
[wandbox]: https://wandbox.org/permlink/QV3gZ2KQQNwgoFIB

## Test

This directory contains the tests for __MPark.Variant__.

## CMake Variables

  -  __`MPARK_VARIANT_EXCEPTIONS`__:`BOOL` (__default__: `ON`)

     Build the tests with exceptions support.

## Build / Run

Execute the following commands from the top-level directory:

```bash
mkdir build
cd build
cmake -DMPARK_VARIANT_INCLUDE_TESTS="mpark;libc++" ..
cmake --build .
ctest --output-on-failure
```
# Abseil - C++ Common Libraries

The repository contains the Abseil C++ library code. Abseil is an open-source
collection of C++ code (compliant to C++11) designed to augment the C++
standard library.

## Table of Contents

- [About Abseil](#about)
- [Quickstart](#quickstart)
- [Building Abseil](#build)
- [Codemap](#codemap)
- [License](#license)
- [Links](#links)

<a name="about"></a>
## About Abseil

Abseil is an open-source collection of C++ library code designed to augment
the C++ standard library. The Abseil library code is collected from Google's
own C++ code base, has been extensively tested and used in production, and
is the same code we depend on in our daily coding lives.

In some cases, Abseil provides pieces missing from the C++ standard; in
others, Abseil provides alternatives to the standard for special needs
we've found through usage in the Google code base. We denote those cases
clearly within the library code we provide you.

Abseil is not meant to be a competitor to the standard library; we've
just found that many of these utilities serve a purpose within our code
base, and we now want to provide those resources to the C++ community as
a whole.

<a name="quickstart"></a>
## Quickstart

If you want to just get started, make sure you at least run through the
[Abseil Quickstart](https://abseil.io/docs/cpp/quickstart). The Quickstart
contains information about setting up your development environment, downloading
the Abseil code, running tests, and getting a simple binary working.

<a name="build"></a>
## Building Abseil

[Bazel](http://bazel.build) is the official build system for Abseil,
which is supported on most major platforms (Linux, Windows, MacOS, for example)
and compilers. See the [quickstart](https://abseil.io/docs/cpp/quickstart) for
more information on building Abseil using the Bazel build system.

<a name="cmake"></a>
If you require CMake support, please check the
[CMake build instructions](CMake/README.md).

## Codemap

Abseil contains the following C++ library components:

* [`base`](absl/base/) Abseil Fundamentals
  <br /> The `base` library contains initialization code and other code which
  all other Abseil code depends on. Code within `base` may not depend on any
  other code (other than the C++ standard library).
* [`algorithm`](absl/algorithm/)
  <br /> The `algorithm` library contains additions to the C++ `<algorithm>`
  library and container-based versions of such algorithms.
* [`container`](absl/container/)
  <br /> The `container` library contains additional STL-style containers,
  including Abseil's unordered "Swiss table" containers.
* [`debugging`](absl/debugging/)
  <br /> The `debugging` library contains code useful for enabling leak
  checks, and stacktrace and symbolization utilities.
* [`hash`](absl/hash/)
  <br /> The `hash` library contains the hashing framework and default hash
  functor implementations for hashable types in Abseil.
* [`memory`](absl/memory/)
  <br /> The `memory` library contains C++11-compatible versions of
  `std::make_unique()` and related memory management facilities.
* [`meta`](absl/meta/)
  <br /> The `meta` library contains C++11-compatible versions of type checks
  available within C++14 and C++17 versions of the C++ `<type_traits>` library.
* [`numeric`](absl/numeric/)
  <br /> The `numeric` library contains C++11-compatible 128-bit integers.
* [`strings`](absl/strings/)
  <br /> The `strings` library contains a variety of strings routines and
  utilities, including a C++11-compatible version of the C++17
  `std::string_view` type.
* [`synchronization`](absl/synchronization/)
  <br /> The `synchronization` library contains concurrency primitives (Abseil's
  `absl::Mutex` class, an alternative to `std::mutex`) and a variety of
  synchronization abstractions.
* [`time`](absl/time/)
  <br /> The `time` library contains abstractions for computing with absolute
  points in time, durations of time, and formatting and parsing time within
  time zones.
* [`types`](absl/types/)
  <br /> The `types` library contains non-container utility types, like a
  C++11-compatible version of the C++17 `std::optional` type.
* [`utility`](absl/utility/)
  <br /> The `utility` library contains utility and helper code.

## License

The Abseil C++ library is licensed under the terms of the Apache
license. See [LICENSE](LICENSE) for more information.

## Links

For more information about Abseil:

* Consult our [Abseil Introduction](http://abseil.io/about/intro)
* Read [Why Adopt Abseil](http://abseil.io/about/philosophy) to understand our
  design philosophy.
* Peruse our
  [Abseil Compatibility Guarantees](http://abseil.io/about/compatibility) to
  understand both what we promise to you, and what we expect of you in return.
testdata/zoneinfo contains time-zone data files that may be used with CCTZ.
Install them in a location referenced by the ${TZDIR} environment variable.
Symbolic and hard links have been eliminated for portability.

On Linux systems the distribution's versions of these files can probably
already be found in the default ${TZDIR} location, /usr/share/zoneinfo.

New versions can be generated using the following shell script.

  #!/bin/sh -
  set -e
  DESTDIR=$(mktemp -d)
  trap "rm -fr ${DESTDIR}" 0 2 15
  (
    cd ${DESTDIR}
    git clone https://github.com/eggert/tz.git
    make --directory=tz \
        install DESTDIR=${DESTDIR} \
                DATAFORM=vanguard \
                TZDIR=/zoneinfo \
                REDO=posix_only \
                LOCALTIME=Factory \
                TZDATA_TEXT= \
                ZONETABLES=zone1970.tab
    tar --create --dereference --hard-dereference --file tzfile.tar \
        --directory=tz tzfile.h
    tar --create --dereference --hard-dereference --file zoneinfo.tar \
        --exclude=zoneinfo/posixrules zoneinfo \
        --directory=tz version
  )
  tar --extract --directory src --file ${DESTDIR}/tzfile.tar
  tar --extract --directory testdata --file ${DESTDIR}/zoneinfo.tar
  exit 0

To run the CCTZ tests using the testdata/zoneinfo files, execute:

  bazel test --test_env=TZDIR=${PWD}/testdata/zoneinfo ...
# Abseil CMake Build Instructions

Abseil comes with a CMake build script ([CMakeLists.txt](../CMakeLists.txt))
that can be used on a wide range of platforms ("C" stands for cross-platform.).
If you don't have CMake installed already, you can download it for free from
<http://www.cmake.org/>.

CMake works by generating native makefiles or build projects that can
be used in the compiler environment of your choice.

For API/ABI compatibility reasons, we strongly recommend building Abseil in a
subdirectory of your project or as an embedded dependency.

## Incorporating Abseil Into a CMake Project

The recommendations below are similar to those for using CMake within the
googletest framework
(<https://github.com/google/googletest/blob/master/googletest/README.md#incorporating-into-an-existing-cmake-project>)

### Step-by-Step Instructions

1. If you want to build the Abseil tests, integrate the Abseil dependency
[Google Test](https://github.com/google/googletest) into your CMake project. To disable Abseil tests, you have to pass
`-DBUILD_TESTING=OFF` when configuring your project with CMake.

2. Download Abseil and copy it into a subdirectory in your CMake project or add
Abseil as a [git submodule](https://git-scm.com/docs/git-submodule) in your
CMake project.

3. You can then use the CMake command
[`add_subdirectory()`](https://cmake.org/cmake/help/latest/command/add_subdirectory.html)
to include Abseil directly in your CMake project.

4. Add the **absl::** target you wish to use to the
[`target_link_libraries()`](https://cmake.org/cmake/help/latest/command/target_link_libraries.html)
section of your executable or of your library.<br>
Here is a short CMakeLists.txt example of a project file using Abseil.

```cmake
cmake_minimum_required(VERSION 2.8.12)
project(my_project)

set(CMAKE_CXX_FLAGS "-std=c++11 -stdlib=libc++ ${CMAKE_CXX_FLAGS}")

if(MSVC)
  # /wd4005  macro-redefinition
  # /wd4068  unknown pragma
  # /wd4244  conversion from 'type1' to 'type2'
  # /wd4267  conversion from 'size_t' to 'type2'
  # /wd4800  force value to bool 'true' or 'false' (performance warning)
  add_compile_options(/wd4005 /wd4068 /wd4244 /wd4267 /wd4800)
  add_definitions(/DNOMINMAX /DWIN32_LEAN_AND_MEAN=1 /D_CRT_SECURE_NO_WARNINGS)
endif()

add_subdirectory(abseil-cpp)

add_executable(my_exe source.cpp)
target_link_libraries(my_exe absl::base absl::synchronization absl::strings)
```

### Running Abseil Tests with CMake

Use the `-DABSL_RUN_TESTS=ON` flag to run Abseil tests.  Note that if the `-DBUILD_TESTING=OFF` flag is passed then Abseil tests will not be run.

You will need to provide Abseil with a Googletest dependency.  There are two
options for how to do this:

* Use `-DABSL_USE_GOOGLETEST_HEAD`.  This will automatically download the latest
Googletest source into the build directory at configure time.  Googletest will
then be compiled directly alongside Abseil's tests.
* Manually integrate Googletest with your build.  See
https://github.com/google/googletest/blob/master/googletest/README.md#using-cmake
for more information on using Googletest in a CMake project.

For example, to run just the Abseil tests, you could use this script:

```
cd path/to/abseil-cpp
mkdir build
cd build
cmake -DABSL_USE_GOOGLETEST_HEAD=ON -DABSL_RUN_TESTS=ON ..
make -j
ctest
```

Currently, we only run our tests with CMake in a Linux environment, but we are
working on the rest of our supported platforms. See
https://github.com/abseil/abseil-cpp/projects/1 and
https://github.com/abseil/abseil-cpp/issues/109 for more information.

### Available Abseil CMake Public Targets

Here's a non-exhaustive list of Abseil CMake public targets:

```cmake
absl::base
absl::algorithm
absl::container
absl::debugging
absl::memory
absl::meta
absl::numeric
absl::strings
absl::synchronization
absl::time
absl::utility
```
Storage Engine API
==================

The purpose of the Storage Engine API is to allow for pluggable storage engines in MongoDB (refer
to the [Storage FAQ][]). This document gives a brief overview of the API, and provides pointers
to places with more detailed documentation. Where referencing code, links are to the version that
was current at the time when the reference was made. Always compare with the latest version for
changes not yet reflected here.  For questions on the API that are not addressed by this material,
use the [mongodb-dev][] Google group. Everybody involved in the Storage Engine API will read your
post.

Third-party storage engines are integrated through self-contained modules that can be dropped into
an existing MongoDB source tree, and will be automatically configured and included. A typical
module would at least have the following files:

    src/             Directory with the actual source files
    README.md        Information specific to the storage engine
    SConscript       Scons build rules
    build.py         Module configuration script

See <https://github.com/mongodb-partners/mongo-rocks> for a good example of the structure.


Concepts
--------

### Record Stores
A database contains one or more collections, each with a number of indexes, and a catalog listing
them. All MongoDB collections are implemented with record stores: one for the documents themselves,
and one for each index. By using the KVEngine class, you only have to deal with the abstraction, as
the KVStorageEngine implements the StorageEngine interface, using record stores for catalogs and
indexes.

#### Record Identities
A RecordId is a unique identifier, assigned by the storage engine, for a specific document or entry
in a record store at a given time. For storage engines based in the KVEngine the record identity is
fixed, but other storage engines, such as MMAPv1, may change it when updating a document. Note that
changing record ids can be very expensive, as indexes map to the RecordId. A single document with a
large array may have thousands of index entries, resulting in very expensive updates.

#### Cloning and bulk operations
Currently all cloning, [initial sync][] and other operations are done in terms of operating on
individual documents, though there is a BulkBuilder class for more efficiently building indexes.

### Locking and Concurrency
MongoDB uses multi-granular intent locking; see the [Concurrency FAQ][]. In all cases, this will
ensure that operations to meta-data, such as creation and deletion of record stores, are serialized
with respect to other accesses. Storage engines can choose to support document-level concurrency,
in which case the storage engine is responsible for any additional synchronization necessary. For
storage engines not supporting document-level concurrency, MongoDB will use shared/exclusive locks
at the collection level, so all record store accesses will be serialized.

MongoDB uses [two-phase locking][] (2PL) to guarantee serializability of accesses to resources it
manages. For storage engines that support document level concurrency, MongoDB will only use intent
locks for the most common operations, leaving synchronization at the record store layer up to the
storage engine.

### Transactions
Each operation creates an OperationContext with a new RecoveryUnit, implemented by the storage
engine, that lives until the operation finishes. Currently, query operations that return a cursor
to the client live as long as that client cursor, with the operation context switching between its
own recovery unit and that of the client cursor. In a few other cases an internal command may use
an extra recovery unit as well. The recovery unit must implement transaction semantics as described
below.

#### Atomicity
Writes must only become visible when explicitly committed, and in that case all pending writes
become visible atomically. Writes that are not committed before the unit of work ends must be
rolled back. In addition to writes done directly through the Storage API, such as document updates
and creation of record stores, other custom changes can be registered with the recovery unit.

#### Consistency
Storage engines must ensure that atomicity and isolation guarantees span all record stores, as
otherwise the guarantee of atomic updates on a document and all its indexes would be violated.

#### Isolation
Storage engines must provide snapshot isolation, either through locking (as is the case for the
MMAPv1 engine), through multi-version concurrency control (MVCC) or otherwise. The first read
implicitly establishes the snapshot. Operations can always see all changes they make in the context
of a recovery unit, but other operations cannot until a successful commit.

#### Durability
Once a transaction is committed, it is not necessarily durable: if, and only if the server fails,
as result of power loss or otherwise, the database may recover to an earlier point in time.
However, atomicity of transactions must remain preserved. Similarly, in a replica set, a primary
that becomes unavailable may need to roll back to an earlier state when rejoining the replica set,
if its changes were not yet seen by a majority of nodes. The RecoveryUnit implements methods to
allow operations to wait for their committed transactions to become durable.

A transaction may become visible to other transactions as soon as it commits, and a storage engine
may use a group commit, bundling a number of transactions to achieve durability. Alternatively, a
storage engine may wait for durability at commit time.

### Write Conflicts
Systems with optimistic concurrency control (OCC) or multi-version concurrency control (MVCC) may
find that a transaction conflicts with other transactions, that executing an operation would result
in deadlock or violate other resource constraints. In such cases the storage engine may throw a
WriteConflictException to signal the transient failure. MongoDB will handle the exception, abort
and restart the transaction.

### Point-in-time snapshot reads
Two functions on the RecoveryUnit help storage engines implement point-in-time reads: setTimestamp()
and selectSnapshot().  setTimestamp() is used by write transactions to label any forthcoming writes
with a timestamp; these timestamps are then used to produce a point-in-time read transaction via a
call to selectSnapshot() at the start of the read.  The storage engine must produce the effect of
reading from a snapshot that includes only writes with timestamps at or earlier than the
selectSnapshot timestamp.  This means that a point-in-time read may slice across prior write
transactions by hiding only some data from a given write transaction, if that transaction had a
different timestamp set prior to each write it did.

Classes to implement
--------------------

A storage engine should generally implement the following classes. See their definitions for more
details.

* [KVEngine](kv/kv_engine.h)
* [RecordStore](record_store.h)
* [RecoveryUnit](recovery_unit.h)
* [SeekableRecordCursor](record_store.h)
* [SortedDataInterface](sorted_data_interface.h)
* [ServerStatusSection](../commands/server_status.h)
* [ServerParameter](../server_parameters.h)


[Concurrency FAQ]: http://docs.mongodb.org/manual/faq/concurrency/
[initial sync]: http://docs.mongodb.org/manual/core/replica-set-sync/#replica-set-initial-sync
[mongodb-dev]: https://groups.google.com/forum/#!forum/mongodb-dev
[replica set]: http://docs.mongodb.org/manual/replication/
[Storage FAQ]: http://docs.mongodb.org/manual/faq/storage
[two-phase locking]: http://en.wikipedia.org/wiki/Two-phase_locking
"BSON" stands for "binary JSON" - a binary storage format that is JSON inspired 
(and adds a couple extra types such as Date).

This is the C++ implementation.  Implementations which translate BSON<->JSON 
are available for most languages at bsonspec.org.


This directory contains a number of C++ headers which describe concepts for
C++ types used by and with the Mongo library.  These headers do not describe
instantiable types, but instead are used to concisely describe models of C++
type concepts.  When C++ grows a proper `Concepts` feature, these files can be
converted to proper concepts.
MongoDB Tools
===================================

 - **bsondump** - _display BSON files in a human-readable format_
 - **mongoimport** - _Convert data from JSON, TSV or CSV and insert them into a collection_
 - **mongoexport** - _Write an existing collection to CSV or JSON format_
 - **mongodump/mongorestore** - _Dump MongoDB backups to disk in .BSON format, or restore them to a live database_
 - **mongostat** - _Monitor live MongoDB servers, replica sets, or sharded clusters_
 - **mongofiles** - _Read, write, delete, or update files in [GridFS](http://docs.mongodb.org/manual/core/gridfs/)_
 - **mongotop** - _Monitor read/write activity on a mongo server_
 - **mongoreplay** - _Capture, observe, and replay traffic for MongoDB_


Report any bugs, improvements, or new feature requests at https://jira.mongodb.org/browse/TOOLS

Setup
---------------
Clone the repo and run `. ./set_gopath.sh` (`set_gopath.bat` on Windows) to setup your GOPATH:

```
git clone https://github.com/mongodb/mongo-tools
cd mongo-tools
. ./set_gopath.sh
```

Building Tools
---------------
To build the tools, you need to have Go version 1.3 and up.

An additional flag, `-tags`, can be passed to the `go build` command in order to build the tools with support for SSL and/or SASL. For example:

```
mkdir bin
go build -o bin/mongoimport mongoimport/main/mongoimport.go # build mongoimport
go build -o bin/mongoimport -tags ssl mongoimport/main/mongoimport.go # build mongoimport with SSL support enabled
go build -o bin/mongoimport -tags "ssl sasl" mongoimport/main/mongoimport.go # build mongoimport with SSL and SASL support enabled
```

Contributing
---------------
See our [Contributor's Guide](CONTRIBUTING.md).

Documentation
---------------
See the MongoDB packages [documentation](http://docs.mongodb.org/master/reference/program/).

# Go Text

This repository holds supplementary Go libraries for text processing, many involving Unicode.

## Semantic Versioning
This repo uses Semantic versioning (http://semver.org/), so
1. MAJOR version when you make incompatible API changes,
1. MINOR version when you add functionality in a backwards-compatible manner,
   and
1. PATCH version when you make backwards-compatible bug fixes.

Until version 1.0.0 of x/text is reached, the minor version is considered a
major version. So going from 0.1.0 to 0.2.0 is considered to be a major version
bump.

A major new CLDR version is mapped to a minor version increase in x/text.
Any other new CLDR version is mapped to a patch version increase in x/text.

It is important that the Unicode version used in `x/text` matches the one used
by your Go compiler. The `x/text` repository supports multiple versions of
Unicode and will match the version of Unicode to that of the Go compiler. At the
moment this is supported for Go compilers from version 1.7.

## Download/Install

The easiest way to install is to run `go get -u golang.org/x/text`. You can
also manually git clone the repository to `$GOPATH/src/golang.org/x/text`.

## Contribute
To submit changes to this repository, see http://golang.org/doc/contribute.html.

To generate the tables in this repository (except for the encoding tables),
run go generate from this directory. By default tables are generated for the
Unicode version in core and the CLDR version defined in
golang.org/x/text/unicode/cldr.

Running go generate will as a side effect create a DATA subdirectory in this
directory, which holds all files that are used as a source for generating the
tables. This directory will also serve as a cache.

## Testing
Run

    go test ./...

from this directory to run all tests. Add the "-tags icu" flag to also run
ICU conformance tests (if available). This requires that you have the correct
ICU version installed on your system.

TODO:
- updating unversioned source files.

## Generating Tables

To generate the tables in this repository (except for the encoding
tables), run `go generate` from this directory. By default tables are
generated for the Unicode version in core and the CLDR version defined in
golang.org/x/text/unicode/cldr.

Running go generate will as a side effect create a DATA subdirectory in this
directory which holds all files that are used as a source for generating the
tables. This directory will also serve as a cache.

## Versions
To update a Unicode version run

    UNICODE_VERSION=x.x.x go generate

where `x.x.x` must correspond to a directory in http://www.unicode.org/Public/.
If this version is newer than the version in core it will also update the
relevant packages there. The idna package in x/net will always be updated.

To update a CLDR version run

    CLDR_VERSION=version go generate

where `version` must correspond to a directory in
http://www.unicode.org/Public/cldr/.

Note that the code gets adapted over time to changes in the data and that
backwards compatibility is not maintained.
So updating to a different version may not work.

The files in DATA/{iana|icu|w3|whatwg} are currently not versioned.

## Report Issues / Send Patches

This repository uses Gerrit for code changes. To learn how to submit changes to
this repository, see https://golang.org/doc/contribute.html.

The main issue tracker for the image repository is located at
https://github.com/golang/go/issues. Prefix your issue with "x/image:" in the
subject line, so it is easy to find.
The export directory contains packages that are generated using the x/text
infrastructure, but live elsewhere.
At some point we can expose some of the infrastructure, but for now this
is not done.
This repository holds supplementary Go cryptography libraries.

To submit changes to this repository, see http://golang.org/doc/contribute.html.
The MongoDB driver for Go
-------------------------

Please go to [http://labix.org/mgo](http://labix.org/mgo) for all project details.

## Testing

Tests require custom orchestration.  Install
[daemontools](https://cr.yp.to/daemontools.html) as a prerequisite and make
sure mongod and mongos are in your path.  To start the orchestration:

    $ export PATH=/path/to/mongodb/bin:$PATH
    $ make startdb

To stop the orchestration:

    $ make stopdb

Run all tests like this (`gocheck.v` turns on verbose output):

    $ go test -gocheck.v

To run a specific test, use the `gocheck.f` flag:

    $ go test -gocheck.v -gocheck.f TestFindAndModifyBug997828
Installation and usage
----------------------

See [gopkg.in/tomb.v2](https://gopkg.in/tomb.v2) for documentation and usage details.
go-runewidth
============

[![Build Status](https://travis-ci.org/mattn/go-runewidth.png?branch=master)](https://travis-ci.org/mattn/go-runewidth)
[![Coverage Status](https://coveralls.io/repos/mattn/go-runewidth/badge.png?branch=HEAD)](https://coveralls.io/r/mattn/go-runewidth?branch=HEAD)
[![GoDoc](https://godoc.org/github.com/mattn/go-runewidth?status.svg)](http://godoc.org/github.com/mattn/go-runewidth)

Provides functions to get fixed width of the character or string.

Usage
-----

```go
runewidth.StringWidth("つのだ☆HIRO") == 12
```


Author
------

Yasuhiro Matsumoto

License
-------

under the MIT License: http://mattn.mit-license.org/2013
[![GoDoc](https://godoc.org/github.com/xdg/stringprep?status.svg)](https://godoc.org/github.com/xdg/stringprep)
[![Build Status](https://travis-ci.org/xdg/stringprep.svg?branch=master)](https://travis-ci.org/xdg/stringprep)

# stringprep – Go implementation of RFC-3454 stringprep and RFC-4013 SASLprep

## Synopsis

```
    import "github.com/xdg/stringprep"

    prepped := stringprep.SASLprep.Prepare("TrustNô1")

```

## Description

This library provides an implementation of the stringprep algorithm
(RFC-3454) in Go, including all data tables.

A pre-built SASLprep (RFC-4013) profile is provided as well.

## Copyright and License

Copyright 2018 by David A. Golden. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"). You may
obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
gls
===

Goroutine local storage

### IMPORTANT NOTE ###

It is my duty to point you to https://blog.golang.org/context, which is how 
Google solves all of the problems you'd perhaps consider using this package
for at scale. 

One downside to Google's approach is that *all* of your functions must have
a new first argument, but after clearing that hurdle everything else is much
better.

If you aren't interested in this warning, read on.

### Huhwaht? Why? ###

Every so often, a thread shows up on the
[golang-nuts](https://groups.google.com/d/forum/golang-nuts) asking for some
form of goroutine-local-storage, or some kind of goroutine id, or some kind of
context. There are a few valid use cases for goroutine-local-storage, one of
the most prominent being log line context. One poster was interested in being
able to log an HTTP request context id in every log line in the same goroutine
as the incoming HTTP request, without having to change every library and
function call he was interested in logging.

This would be pretty useful. Provided that you could get some kind of
goroutine-local-storage, you could call
[log.SetOutput](http://golang.org/pkg/log/#SetOutput) with your own logging
writer that checks goroutine-local-storage for some context information and
adds that context to your log lines.

But alas, Andrew Gerrand's typically diplomatic answer to the question of
goroutine-local variables was:

> We wouldn't even be having this discussion if thread local storage wasn't
> useful. But every feature comes at a cost, and in my opinion the cost of
> threadlocals far outweighs their benefits. They're just not a good fit for
> Go.

So, yeah, that makes sense. That's a pretty good reason for why the language
won't support a specific and (relatively) unuseful feature that requires some
runtime changes, just for the sake of a little bit of log improvement.

But does Go require runtime changes?

### How it works ###

Go has pretty fantastic introspective and reflective features, but one thing Go
doesn't give you is any kind of access to the stack pointer, or frame pointer,
or goroutine id, or anything contextual about your current stack. It gives you
access to your list of callers, but only along with program counters, which are
fixed at compile time.

But it does give you the stack.

So, we define 16 special functions and embed base-16 tags into the stack using
the call order of those 16 functions. Then, we can read our tags back out of
the stack looking at the callers list.

We then use these tags as an index into a traditional map for implementing
this library.

### What are people saying? ###

"Wow, that's horrifying."

"This is the most terrible thing I have seen in a very long time."

"Where is it getting a context from? Is this serializing all the requests? 
What the heck is the client being bound to? What are these tags? Why does he 
need callers? Oh god no. No no no."

### Docs ###

Please see the docs at http://godoc.org/github.com/jtolds/gls

### Related ###

If you're okay relying on the string format of the current runtime stacktrace 
including a unique goroutine id (not guaranteed by the spec or anything, but 
very unlikely to change within a Go release), you might be able to squeeze 
out a bit more performance by using this similar library, inspired by some 
code Brad Fitzpatrick wrote for debugging his HTTP/2 library: 
https://github.com/tylerb/gls (in contrast, jtolds/gls doesn't require 
any knowledge of the string format of the runtime stacktrace, which 
probably adds unnecessary overhead).
The MongoDB driver for Go
-------------------------

Please go to [http://labix.org/mgo](http://labix.org/mgo) for all project details.
# OpenSSL bindings for Go

Please see http://godoc.org/github.com/spacemonkeygo/openssl for more info

### License

Copyright (C) 2017. See AUTHORS.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

### Installing on a Unix-ish system with pkg-config

1.  (If necessary) install the openssl C library with a package manager
    that provides an openssl.pc file OR install openssl manually and create
    an openssl.pc file.

2.  Ensure that `pkg-config --cflags --libs openssl` finds your openssl
    library.  If it doesn't, try setting `PKG_CONFIG_PATH` to the directory
    containing your openssl.pc file.  E.g. for darwin: with MacPorts,
    `PKG_CONFIG_PATH=/opt/local/lib/pkgconfig` or for Homebrew,
    `PKG_CONFIG_PATH=/usr/local/Cellar/openssl/1.0.2l/lib/pkgconfig`

### Installing on a Unix-ish system without pkg-config

1.  (If necessary) install the openssl C library in your customary way

2.  Set the `CGO_CPP_FLAGS`, `CGO_CFLAGS` and `CGO_LDFLAGS` as necessary to
    provide `-I`, `-L` and other options to the compiler.  E.g. on darwin,
    MongoDB's darwin build servers use the native libssl, but provide the
    missing headers in a custom directory, so it the build hosts set
    `CGO_CPPFLAGS=-I/opt/mongodbtoolchain/v2/include`

### Installing on Windows

1. Install [mingw-w64](http://mingw-w64.sourceforge.net/) and add it to
   your `PATH`

2. Install the C openssl into `C:\openssl`.  (Unfortunately, this is still
   hard-coded.)  You should have directories like `C:\openssl\include` and
   `C:\openssl\bin`.
# escaper [![GoDoc](http://img.shields.io/badge/go-documentation-blue.svg?style=flat_square)](http://godoc.org/github.com/lucasem/escaper)

**`escaper`** lets you create your own formatting syntax. By design,
expanding a format string with this utility requires no additional arguments
(unlike fmt.Sprinf) by letting you easily register your own escape handlers.
This makes it **ideal for configurability**, where only a string is
necessary to specify a complex output format.

![escaper](http://i.imgur.com/qAAPq5y.png)

## Motivation

There is often desire to make some program output user-configurable.
A lot of software doesn't bother with configurability and has hard-coded
output formats. This package aims to eliminate this unfortunate paradigm,
and easily permit customizability where it is often disregarded. Inspired by
the style of zsh prompt expansion, **`escaper`** makes output formatting a
better abstraction for its users.

## Install

```bash
go get github.com/lucasem/escaper
```

## Examples

### Basics

```go
format := "add some ANSI %F{blue}text color%f easily"

esc := escaper.Default()
output := esc.Expand(format)
```

### Advanced

```go
format := "my name is %n, and the time is %D{3:04PM}"
name := "Ben Bitdiddle"

// use New() if you don't want the default ANSI escapes
esc := escaper.New()

// register a new escape
esc.Register('n', func() string {
  return name
})

// register an escape that takes an argument
esc.RegisterArg('D', func(arg string) string {
  return time.Now().Format(arg)
})

// "my name is Ben Bitdiddle, and the time is 11:15AM"
output := esc.Expand(format)
```

## The Default

The default escaper (`escaper.Default()`) supports the following ANSI
escapes:
- `%F{<color>}text%f` colors the text
- `%K{<color>}text%k` colors the background
- `%Btext%b` bolds the text
- `%Utext%u` underlines the text
- `%Stext%s` standouts (color inverts) the text

`<color>` can be one of:
```
black   (0)
red     (1)
green   (2)
yellow  (3)
blue    (4)
magenta (5)
cyan    (6)
white   (7)
```

## License

The MIT License (MIT) - see [`LICENSE`](https://github.com/lucasem/escaper/blob/master/LICENSE) for details
# assertions
--
    import "github.com/smartystreets/assertions"

Package assertions contains the implementations for all assertions which are
referenced in goconvey's `convey` package
(github.com/smartystreets/goconvey/convey) and gunit
(github.com/smartystreets/gunit) for use with the So(...) method. They can also
be used in traditional Go test functions and even in applications.

Many of the assertions lean heavily on work done by Aaron Jacobs in his
excellent oglematchers library. (https://github.com/jacobsa/oglematchers) The
ShouldResemble assertion leans heavily on work done by Daniel Jacques in his
very helpful go-render library. (https://github.com/luci/go-render)

## Usage

#### func  GoConveyMode

```go
func GoConveyMode(yes bool)
```
GoConveyMode provides control over JSON serialization of failures. When using
the assertions in this package from the convey package JSON results are very
helpful and can be rendered in a DIFF view. In that case, this function will be
called with a true value to enable the JSON serialization. By default, the
assertions in this package will not serializer a JSON result, making standalone
ussage more convenient.

#### func  ShouldAlmostEqual

```go
func ShouldAlmostEqual(actual interface{}, expected ...interface{}) string
```
ShouldAlmostEqual makes sure that two parameters are close enough to being
equal. The acceptable delta may be specified with a third argument, or a very
small default delta will be used.

#### func  ShouldBeBetween

```go
func ShouldBeBetween(actual interface{}, expected ...interface{}) string
```
ShouldBeBetween receives exactly three parameters: an actual value, a lower
bound, and an upper bound. It ensures that the actual value is between both
bounds (but not equal to either of them).

#### func  ShouldBeBetweenOrEqual

```go
func ShouldBeBetweenOrEqual(actual interface{}, expected ...interface{}) string
```
ShouldBeBetweenOrEqual receives exactly three parameters: an actual value, a
lower bound, and an upper bound. It ensures that the actual value is between
both bounds or equal to one of them.

#### func  ShouldBeBlank

```go
func ShouldBeBlank(actual interface{}, expected ...interface{}) string
```
ShouldBeBlank receives exactly 1 string parameter and ensures that it is equal
to "".

#### func  ShouldBeChronological

```go
func ShouldBeChronological(actual interface{}, expected ...interface{}) string
```
ShouldBeChronological receives a []time.Time slice and asserts that the are in
chronological order starting with the first time.Time as the earliest.

#### func  ShouldBeEmpty

```go
func ShouldBeEmpty(actual interface{}, expected ...interface{}) string
```
ShouldBeEmpty receives a single parameter (actual) and determines whether or not
calling len(actual) would return `0`. It obeys the rules specified by the len
function for determining length: http://golang.org/pkg/builtin/#len

#### func  ShouldBeFalse

```go
func ShouldBeFalse(actual interface{}, expected ...interface{}) string
```
ShouldBeFalse receives a single parameter and ensures that it is false.

#### func  ShouldBeGreaterThan

```go
func ShouldBeGreaterThan(actual interface{}, expected ...interface{}) string
```
ShouldBeGreaterThan receives exactly two parameters and ensures that the first
is greater than the second.

#### func  ShouldBeGreaterThanOrEqualTo

```go
func ShouldBeGreaterThanOrEqualTo(actual interface{}, expected ...interface{}) string
```
ShouldBeGreaterThanOrEqualTo receives exactly two parameters and ensures that
the first is greater than or equal to the second.

#### func  ShouldBeIn

```go
func ShouldBeIn(actual interface{}, expected ...interface{}) string
```
ShouldBeIn receives at least 2 parameters. The first is a proposed member of the
collection that is passed in either as the second parameter, or of the
collection that is comprised of all the remaining parameters. This assertion
ensures that the proposed member is in the collection (using ShouldEqual).

#### func  ShouldBeLessThan

```go
func ShouldBeLessThan(actual interface{}, expected ...interface{}) string
```
ShouldBeLessThan receives exactly two parameters and ensures that the first is
less than the second.

#### func  ShouldBeLessThanOrEqualTo

```go
func ShouldBeLessThanOrEqualTo(actual interface{}, expected ...interface{}) string
```
ShouldBeLessThan receives exactly two parameters and ensures that the first is
less than or equal to the second.

#### func  ShouldBeNil

```go
func ShouldBeNil(actual interface{}, expected ...interface{}) string
```
ShouldBeNil receives a single parameter and ensures that it is nil.

#### func  ShouldBeTrue

```go
func ShouldBeTrue(actual interface{}, expected ...interface{}) string
```
ShouldBeTrue receives a single parameter and ensures that it is true.

#### func  ShouldBeZeroValue

```go
func ShouldBeZeroValue(actual interface{}, expected ...interface{}) string
```
ShouldBeZeroValue receives a single parameter and ensures that it is the Go
equivalent of the default value, or "zero" value.

#### func  ShouldContain

```go
func ShouldContain(actual interface{}, expected ...interface{}) string
```
ShouldContain receives exactly two parameters. The first is a slice and the
second is a proposed member. Membership is determined using ShouldEqual.

#### func  ShouldContainKey

```go
func ShouldContainKey(actual interface{}, expected ...interface{}) string
```
ShouldContainKey receives exactly two parameters. The first is a map and the
second is a proposed key. Keys are compared with a simple '=='.

#### func  ShouldContainSubstring

```go
func ShouldContainSubstring(actual interface{}, expected ...interface{}) string
```
ShouldContainSubstring receives exactly 2 string parameters and ensures that the
first contains the second as a substring.

#### func  ShouldEndWith

```go
func ShouldEndWith(actual interface{}, expected ...interface{}) string
```
ShouldEndWith receives exactly 2 string parameters and ensures that the first
ends with the second.

#### func  ShouldEqual

```go
func ShouldEqual(actual interface{}, expected ...interface{}) string
```
ShouldEqual receives exactly two parameters and does an equality check.

#### func  ShouldEqualTrimSpace

```go
func ShouldEqualTrimSpace(actual interface{}, expected ...interface{}) string
```
ShouldEqualTrimSpace receives exactly 2 string parameters and ensures that the
first is equal to the second after removing all leading and trailing whitespace
using strings.TrimSpace(first).

#### func  ShouldEqualWithout

```go
func ShouldEqualWithout(actual interface{}, expected ...interface{}) string
```
ShouldEqualWithout receives exactly 3 string parameters and ensures that the
first is equal to the second after removing all instances of the third from the
first using strings.Replace(first, third, "", -1).

#### func  ShouldHappenAfter

```go
func ShouldHappenAfter(actual interface{}, expected ...interface{}) string
```
ShouldHappenAfter receives exactly 2 time.Time arguments and asserts that the
first happens after the second.

#### func  ShouldHappenBefore

```go
func ShouldHappenBefore(actual interface{}, expected ...interface{}) string
```
ShouldHappenBefore receives exactly 2 time.Time arguments and asserts that the
first happens before the second.

#### func  ShouldHappenBetween

```go
func ShouldHappenBetween(actual interface{}, expected ...interface{}) string
```
ShouldHappenBetween receives exactly 3 time.Time arguments and asserts that the
first happens between (not on) the second and third.

#### func  ShouldHappenOnOrAfter

```go
func ShouldHappenOnOrAfter(actual interface{}, expected ...interface{}) string
```
ShouldHappenOnOrAfter receives exactly 2 time.Time arguments and asserts that
the first happens on or after the second.

#### func  ShouldHappenOnOrBefore

```go
func ShouldHappenOnOrBefore(actual interface{}, expected ...interface{}) string
```
ShouldHappenOnOrBefore receives exactly 2 time.Time arguments and asserts that
the first happens on or before the second.

#### func  ShouldHappenOnOrBetween

```go
func ShouldHappenOnOrBetween(actual interface{}, expected ...interface{}) string
```
ShouldHappenOnOrBetween receives exactly 3 time.Time arguments and asserts that
the first happens between or on the second and third.

#### func  ShouldHappenWithin

```go
func ShouldHappenWithin(actual interface{}, expected ...interface{}) string
```
ShouldHappenWithin receives a time.Time, a time.Duration, and a time.Time (3
arguments) and asserts that the first time.Time happens within or on the
duration specified relative to the other time.Time.

#### func  ShouldHaveLength

```go
func ShouldHaveLength(actual interface{}, expected ...interface{}) string
```
ShouldHaveLength receives 2 parameters. The first is a collection to check the
length of, the second being the expected length. It obeys the rules specified by
the len function for determining length: http://golang.org/pkg/builtin/#len

#### func  ShouldHaveSameTypeAs

```go
func ShouldHaveSameTypeAs(actual interface{}, expected ...interface{}) string
```
ShouldHaveSameTypeAs receives exactly two parameters and compares their
underlying types for equality.

#### func  ShouldImplement

```go
func ShouldImplement(actual interface{}, expectedList ...interface{}) string
```
ShouldImplement receives exactly two parameters and ensures that the first
implements the interface type of the second.

#### func  ShouldNotAlmostEqual

```go
func ShouldNotAlmostEqual(actual interface{}, expected ...interface{}) string
```
ShouldNotAlmostEqual is the inverse of ShouldAlmostEqual

#### func  ShouldNotBeBetween

```go
func ShouldNotBeBetween(actual interface{}, expected ...interface{}) string
```
ShouldNotBeBetween receives exactly three parameters: an actual value, a lower
bound, and an upper bound. It ensures that the actual value is NOT between both
bounds.

#### func  ShouldNotBeBetweenOrEqual

```go
func ShouldNotBeBetweenOrEqual(actual interface{}, expected ...interface{}) string
```
ShouldNotBeBetweenOrEqual receives exactly three parameters: an actual value, a
lower bound, and an upper bound. It ensures that the actual value is nopt
between the bounds nor equal to either of them.

#### func  ShouldNotBeBlank

```go
func ShouldNotBeBlank(actual interface{}, expected ...interface{}) string
```
ShouldNotBeBlank receives exactly 1 string parameter and ensures that it is
equal to "".

#### func  ShouldNotBeEmpty

```go
func ShouldNotBeEmpty(actual interface{}, expected ...interface{}) string
```
ShouldNotBeEmpty receives a single parameter (actual) and determines whether or
not calling len(actual) would return a value greater than zero. It obeys the
rules specified by the `len` function for determining length:
http://golang.org/pkg/builtin/#len

#### func  ShouldNotBeIn

```go
func ShouldNotBeIn(actual interface{}, expected ...interface{}) string
```
ShouldNotBeIn receives at least 2 parameters. The first is a proposed member of
the collection that is passed in either as the second parameter, or of the
collection that is comprised of all the remaining parameters. This assertion
ensures that the proposed member is NOT in the collection (using ShouldEqual).

#### func  ShouldNotBeNil

```go
func ShouldNotBeNil(actual interface{}, expected ...interface{}) string
```
ShouldNotBeNil receives a single parameter and ensures that it is not nil.

#### func  ShouldNotContain

```go
func ShouldNotContain(actual interface{}, expected ...interface{}) string
```
ShouldNotContain receives exactly two parameters. The first is a slice and the
second is a proposed member. Membership is determinied using ShouldEqual.

#### func  ShouldNotContainKey

```go
func ShouldNotContainKey(actual interface{}, expected ...interface{}) string
```
ShouldNotContainKey receives exactly two parameters. The first is a map and the
second is a proposed absent key. Keys are compared with a simple '=='.

#### func  ShouldNotContainSubstring

```go
func ShouldNotContainSubstring(actual interface{}, expected ...interface{}) string
```
ShouldNotContainSubstring receives exactly 2 string parameters and ensures that
the first does NOT contain the second as a substring.

#### func  ShouldNotEndWith

```go
func ShouldNotEndWith(actual interface{}, expected ...interface{}) string
```
ShouldEndWith receives exactly 2 string parameters and ensures that the first
does not end with the second.

#### func  ShouldNotEqual

```go
func ShouldNotEqual(actual interface{}, expected ...interface{}) string
```
ShouldNotEqual receives exactly two parameters and does an inequality check.

#### func  ShouldNotHappenOnOrBetween

```go
func ShouldNotHappenOnOrBetween(actual interface{}, expected ...interface{}) string
```
ShouldNotHappenOnOrBetween receives exactly 3 time.Time arguments and asserts
that the first does NOT happen between or on the second or third.

#### func  ShouldNotHappenWithin

```go
func ShouldNotHappenWithin(actual interface{}, expected ...interface{}) string
```
ShouldNotHappenWithin receives a time.Time, a time.Duration, and a time.Time (3
arguments) and asserts that the first time.Time does NOT happen within or on the
duration specified relative to the other time.Time.

#### func  ShouldNotHaveSameTypeAs

```go
func ShouldNotHaveSameTypeAs(actual interface{}, expected ...interface{}) string
```
ShouldNotHaveSameTypeAs receives exactly two parameters and compares their
underlying types for inequality.

#### func  ShouldNotImplement

```go
func ShouldNotImplement(actual interface{}, expectedList ...interface{}) string
```
ShouldNotImplement receives exactly two parameters and ensures that the first
does NOT implement the interface type of the second.

#### func  ShouldNotPanic

```go
func ShouldNotPanic(actual interface{}, expected ...interface{}) (message string)
```
ShouldNotPanic receives a void, niladic function and expects to execute the
function without any panic.

#### func  ShouldNotPanicWith

```go
func ShouldNotPanicWith(actual interface{}, expected ...interface{}) (message string)
```
ShouldNotPanicWith receives a void, niladic function and expects to recover a
panic whose content differs from the second argument.

#### func  ShouldNotPointTo

```go
func ShouldNotPointTo(actual interface{}, expected ...interface{}) string
```
ShouldNotPointTo receives exactly two parameters and checks to see that they
point to different addresess.

#### func  ShouldNotResemble

```go
func ShouldNotResemble(actual interface{}, expected ...interface{}) string
```
ShouldNotResemble receives exactly two parameters and does an inverse deep equal
check (see reflect.DeepEqual)

#### func  ShouldNotStartWith

```go
func ShouldNotStartWith(actual interface{}, expected ...interface{}) string
```
ShouldNotStartWith receives exactly 2 string parameters and ensures that the
first does not start with the second.

#### func  ShouldPanic

```go
func ShouldPanic(actual interface{}, expected ...interface{}) (message string)
```
ShouldPanic receives a void, niladic function and expects to recover a panic.

#### func  ShouldPanicWith

```go
func ShouldPanicWith(actual interface{}, expected ...interface{}) (message string)
```
ShouldPanicWith receives a void, niladic function and expects to recover a panic
with the second argument as the content.

#### func  ShouldPointTo

```go
func ShouldPointTo(actual interface{}, expected ...interface{}) string
```
ShouldPointTo receives exactly two parameters and checks to see that they point
to the same address.

#### func  ShouldResemble

```go
func ShouldResemble(actual interface{}, expected ...interface{}) string
```
ShouldResemble receives exactly two parameters and does a deep equal check (see
reflect.DeepEqual)

#### func  ShouldStartWith

```go
func ShouldStartWith(actual interface{}, expected ...interface{}) string
```
ShouldStartWith receives exactly 2 string parameters and ensures that the first
starts with the second.

#### func  So

```go
func So(actual interface{}, assert assertion, expected ...interface{}) (bool, string)
```
So is a convenience function (as opposed to an inconvenience function?) for
running assertions on arbitrary arguments in any context, be it for testing or
even application logging. It allows you to perform assertion-like behavior (and
get nicely formatted messages detailing discrepancies) but without the program
blowing up or panicking. All that is required is to import this package and call
`So` with one of the assertions exported by this package as the second
parameter. The first return parameter is a boolean indicating if the assertion
was true. The second return parameter is the well-formatted message showing why
an assertion was incorrect, or blank if the assertion was correct.

Example:

    if ok, message := So(x, ShouldBeGreaterThan, y); !ok {
         log.Println(message)
    }

#### type Assertion

```go
type Assertion struct {
}
```


#### func  New

```go
func New(t testingT) *Assertion
```
New swallows the *testing.T struct and prints failed assertions using t.Error.
Example: assertions.New(t).So(1, should.Equal, 1)

#### func (*Assertion) Failed

```go
func (this *Assertion) Failed() bool
```
Failed reports whether any calls to So (on this Assertion instance) have failed.

#### func (*Assertion) So

```go
func (this *Assertion) So(actual interface{}, assert assertion, expected ...interface{}) bool
```
So calls the standalone So function and additionally, calls t.Error in failure
scenarios.

#### type FailureView

```go
type FailureView struct {
	Message  string `json:"Message"`
	Expected string `json:"Expected"`
	Actual   string `json:"Actual"`
}
```

This struct is also declared in
github.com/smartystreets/goconvey/convey/reporting. The json struct tags should
be equal in both declarations.

#### type Serializer

```go
type Serializer interface {
	// contains filtered or unexported methods
}
```
go-render: A verbose recursive Go type-to-string conversion library.
====================================================================

[![GoDoc](https://godoc.org/github.com/luci/go-render?status.svg)](https://godoc.org/github.com/luci/go-render)
[![Build Status](https://travis-ci.org/luci/go-render.svg)](https://travis-ci.org/luci/go-render)

This is not an official Google product.

## Overview

The *render* package implements a more verbose form of the standard Go string
formatter, `fmt.Sprintf("%#v", value)`, adding:
  - Pointer recursion. Normally, Go stops at the first pointer and prints its
    address. The *render* package will recurse and continue to render pointer
    values.
  - Recursion loop detection. Recursion is nice, but if a recursion path detects
    a loop, *render* will note this and move on.
  - Custom type name rendering.
  - Deterministic key sorting for `string`- and `int`-keyed maps.
  - Testing!

Call `render.Render` and pass it an `interface{}`.

For example:

```Go
type customType int
type testStruct struct {
        S string
        V *map[string]int
        I interface{}
}

a := testStruct{
        S: "hello",
        V: &map[string]int{"foo": 0, "bar": 1},
        I: customType(42),
}

fmt.Println("Render test:")
fmt.Printf("fmt.Printf:    %#v\n", a)))
fmt.Printf("render.Render: %s\n", Render(a))
```

Yields:
```
fmt.Printf:    render.testStruct{S:"hello", V:(*map[string]int)(0x600dd065), I:42}
render.Render: render.testStruct{S:"hello", V:(*map[string]int){"bar":1, "foo":0}, I:render.customType(42)}
```

This is not intended to be a high-performance library, but it's not terrible
either.

Contributing
------------

  * Sign the [Google CLA](https://cla.developers.google.com/clas).
  * Make sure your `user.email` and `user.name` are configured in `git config`.
  * Install the [pcg](https://github.com/maruel/pre-commit-go) git hook:
    `go get -u github.com/maruel/pre-commit-go/cmd/... && pcg`

Run the following to setup the code review tool and create your first review:

    git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git $HOME/src/depot_tools
    export PATH="$PATH:$HOME/src/depot_tools"
    cd $GOROOT/github.com/luci/go-render
    git checkout -b work origin/master

    # hack hack

    git commit -a -m "This is awesome\nR=joe@example.com"
    # This will ask for your Google Account credentials.
    git cl upload -s
    # Wait for LGTM over email.
    # Check the commit queue box in codereview website.
    # Wait for the change to be tested and landed automatically.

Use `git cl help` and `git cl help <cmd>` for more details.
[![GoDoc](https://godoc.org/github.com/smartystreets/assertions/internal/oglemock?status.svg)](https://godoc.org/github.com/smartystreets/assertions/internal/oglemock)

`oglemock` is a mocking framework for the Go programming language with the
following features:

 *  An extensive and extensible set of matchers for expressing call
    expectations (provided by the [oglematchers][] package).

 *  Clean, readable output that tells you exactly what you need to know.

 *  Style and semantics similar to [Google Mock][googlemock] and
    [Google JS Test][google-js-test].

 *  Seamless integration with the [ogletest][] unit testing framework.

It can be integrated into any testing framework (including Go's `testing`
package), but out of the box support is built in to [ogletest][] and that is the
easiest place to use it.


Installation
------------

First, make sure you have installed Go 1.0.2 or newer. See
[here][golang-install] for instructions.

Use the following command to install `oglemock` and its dependencies, and to
keep them up to date:

    go get -u github.com/smartystreets/assertions/internal/oglemock
    go get -u github.com/smartystreets/assertions/internal/oglemock/createmock

Those commands will install the `oglemock` package itself, along with the
`createmock` tool that is used to auto-generate mock types.


Generating and using mock types
-------------------------------

Automatically generating a mock implementation of an interface is easy. If you
want to mock interfaces `Bar` and `Baz` from package `foo`, simply run the
following:

    createmock foo Bar Baz

That will print source code that can be saved to a file and used in your tests.
For example, to create a `mock_io` package containing mock implementations of
`io.Reader` and `io.Writer`:

    mkdir mock_io
    createmock io Reader Writer > mock_io/mock_io.go

The new package will be named `mock_io`, and contain types called `MockReader`
and `MockWriter`, which implement `io.Reader` and `io.Writer` respectively.

For each generated mock type, there is a corresponding function for creating an
instance of that type given a `Controller` object (see below). For example, to
create a mock reader:

```go
someController := [...]  // See next section.
someReader := mock_io.NewMockReader(someController, "Mock file reader")
```

The snippet above creates a mock `io.Reader` that reports failures to
`someController`. The reader can subsequently have expectations set up and be
passed to your code under test that uses an `io.Reader`.


Getting ahold of a controller
-----------------------------

[oglemock.Controller][controller-ref] is used to create mock objects, and to set
up and verify expectations for them. You can create one by calling
`NewController` with an `ErrorReporter`, which is the basic type used to
interface between `oglemock` and the testing framework within which it is being
used.

If you are using [ogletest][] you don't need to worry about any of this, since
the `TestInfo` struct provided to your test's `SetUp` function already contains
a working `Controller` that you can use to create mock object, and you can use
the built-in `ExpectCall` function for setting expectations. (See the
[ogletest documentation][ogletest-docs] for more info.) Otherwise, you will need
to implement the simple [ErrorReporter interface][reporter-ref] for your test
environment.


Documentation
-------------

For thorough documentation, including information on how to set up expectations,
see [here][oglemock-docs].


[controller-ref]: http://godoc.org/github.com/smartystreets/assertions/internal/oglemock#Controller
[reporter-ref]: http://godoc.org/github.com/smartystreets/assertions/internal/oglemock#ErrorReporter
[golang-install]: http://golang.org/doc/install.html
[google-js-test]: http://code.google.com/p/google-js-test/
[googlemock]: http://code.google.com/p/googlemock/
[oglematchers]: https://github.com/smartystreets/assertions/internal/oglematchers
[oglemock-docs]: http://godoc.org/github.com/smartystreets/assertions/internal/oglemock
[ogletest]: https://github.com/smartystreets/assertions/internal/ogletest
[ogletest-docs]: http://godoc.org/github.com/smartystreets/assertions/internal/ogletest
This directory contains sample code generated with the `createmock` command. For
example, the file `mock_io.go` can be regenerated with:

    createmock io Reader > sample/mock_io/mock_io.go

The files are also used by `integration_test.go`.
[![GoDoc](https://godoc.org/github.com/smartystreets/assertions/internal/ogletest?status.svg)](https://godoc.org/github.com/smartystreets/assertions/internal/ogletest)

`ogletest` is a unit testing framework for Go with the following features:

 *  An extensive and extensible set of matchers for expressing expectations.
 *  Automatic failure messages; no need to say `t.Errorf("Expected %v, got
    %v"...)`.
 *  Clean, readable output that tells you exactly what you need to know.
 *  Built-in support for mocking through the [oglemock][] package.
 *  Style and semantics similar to [Google Test][googletest] and
    [Google JS Test][google-js-test].

It integrates with Go's built-in `testing` package, so it works with the
`go test` command, and even with other types of test within your package. Unlike
the `testing` package which offers only basic capabilities for signalling
failures, it offers ways to express expectations and get nice failure messages
automatically.


Installation
------------

First, make sure you have installed Go 1.0.2 or newer. See
[here][golang-install] for instructions.

Use the following command to install `ogletest` and its dependencies, and to
keep them up to date:

    go get -u github.com/smartystreets/assertions/internal/ogletest


Documentation
-------------

See [here][reference] for package documentation containing an exhaustive list of
exported symbols. Alternatively, you can install the package and then use
`godoc`:

    godoc github.com/smartystreets/assertions/internal/ogletest

An important part of `ogletest` is its use of matchers provided by the
[oglematchers][matcher-reference] package. See that package's documentation
for information on the built-in matchers available, and check out the
`oglematchers.Matcher` interface if you want to define your own.


Example
-------

Let's say you have a function in your package `people` with the following
signature:

```go
// GetRandomPerson returns the name and phone number of Tony, Dennis, or Scott.
func GetRandomPerson() (name, phone string) {
  [...]
}
```

A silly function, but it will do for an example. You can write a couple of tests
for it as follows:

```go
package people

import (
  "github.com/smartystreets/assertions/internal/oglematchers"
  "github.com/smartystreets/assertions/internal/ogletest"
  "testing"
)

// Give ogletest a chance to run your tests when invoked by 'go test'.
func TestOgletest(t *testing.T) { ogletest.RunTests(t) }

// Create a test suite, which groups together logically related test methods
// (defined below). You can share common setup and teardown code here; see the
// package docs for more info.
type PeopleTest struct {}
func init() { ogletest.RegisterTestSuite(&PeopleTest{}) }

func (t *PeopleTest) ReturnsCorrectNames() {
  // Call the function a few times, and make sure it never strays from the set
  // of expected names.
  for i := 0; i < 25; i++ {
    name, _ := GetRandomPerson()
    ogletest.ExpectThat(name, oglematchers.AnyOf("Tony", "Dennis", "Scott"))
  }
}

func (t *PeopleTest) FormatsPhoneNumbersCorrectly() {
  // Call the function a few times, and make sure it returns phone numbers in a
  // standard US format.
  for i := 0; i < 25; i++ {
    _, phone := GetRandomPerson()
    ogletest.ExpectThat(phone, oglematchers.MatchesRegexp(`^\(\d{3}\) \d{3}-\d{4}$`))
}
```

Note that test control functions (`RunTests`, `ExpectThat`, and so on) are part
of the `ogletest` package, whereas built-in matchers (`AnyOf`, `MatchesRegexp`,
and more) are part of the [oglematchers][matcher-reference] library. You can of
course use dot imports so that you don't need to prefix each function with its
package name:

```go
import (
  . "github.com/smartystreets/assertions/internal/oglematchers"
  . "github.com/smartystreets/assertions/internal/ogletest"
)
```

If you save the test in a file whose name ends in `_test.go`, you can run your
tests by simply invoking the following in your package directory:

    go test

Here's what the failure output of ogletest looks like, if your function's
implementation is bad.

    [----------] Running tests from PeopleTest
    [ RUN      ] PeopleTest.FormatsPhoneNumbersCorrectly
    people_test.go:32:
    Expected: matches regexp "^\(\d{3}\) \d{3}-\d{4}$"
    Actual:   +1 800 555 5555
    
    [  FAILED  ] PeopleTest.FormatsPhoneNumbersCorrectly
    [ RUN      ] PeopleTest.ReturnsCorrectNames
    people_test.go:23:
    Expected: or(Tony, Dennis, Scott)
    Actual:   Bart
    
    [  FAILED  ] PeopleTest.ReturnsCorrectNames
    [----------] Finished with tests from PeopleTest

And if the test passes:

    [----------] Running tests from PeopleTest
    [ RUN      ] PeopleTest.FormatsPhoneNumbersCorrectly
    [       OK ] PeopleTest.FormatsPhoneNumbersCorrectly
    [ RUN      ] PeopleTest.ReturnsCorrectNames
    [       OK ] PeopleTest.ReturnsCorrectNames
    [----------] Finished with tests from PeopleTest


[reference]: http://godoc.org/github.com/smartystreets/assertions/internal/ogletest
[matcher-reference]: http://godoc.org/github.com/smartystreets/assertions/internal/oglematchers
[golang-install]: http://golang.org/doc/install.html
[googletest]: http://code.google.com/p/googletest/
[google-js-test]: http://code.google.com/p/google-js-test/
[howtowrite]: http://golang.org/doc/code.html
[oglemock]: https://github.com/smartystreets/assertions/internal/oglemock
[![GoDoc](https://godoc.org/github.com/smartystreets/assertions/internal/oglematchers?status.svg)](https://godoc.org/github.com/smartystreets/assertions/internal/oglematchers)

`oglematchers` is a package for the Go programming language containing a set of
matchers, useful in a testing or mocking framework, inspired by and mostly
compatible with [Google Test][googletest] for C++ and
[Google JS Test][google-js-test]. The package is used by the
[ogletest][ogletest] testing framework and [oglemock][oglemock] mocking
framework, which may be more directly useful to you, but can be generically used
elsewhere as well.

A "matcher" is simply an object with a `Matches` method defining a set of golang
values matched by the matcher, and a `Description` method describing that set.
For example, here are some matchers:

```go
// Numbers
Equals(17.13)
LessThan(19)

// Strings
Equals("taco")
HasSubstr("burrito")
MatchesRegex("t.*o")

// Combining matchers
AnyOf(LessThan(17), GreaterThan(19))
```

There are lots more; see [here][reference] for a reference. You can also add
your own simply by implementing the `oglematchers.Matcher` interface.


Installation
------------

First, make sure you have installed Go 1.0.2 or newer. See
[here][golang-install] for instructions.

Use the following command to install `oglematchers` and keep it up to date:

    go get -u github.com/smartystreets/assertions/internal/oglematchers


Documentation
-------------

See [here][reference] for documentation. Alternatively, you can install the
package and then use `godoc`:

    godoc github.com/smartystreets/assertions/internal/oglematchers


[reference]: http://godoc.org/github.com/smartystreets/assertions/internal/oglematchers
[golang-install]: http://golang.org/doc/install.html
[googletest]: http://code.google.com/p/googletest/
[google-js-test]: http://code.google.com/p/google-js-test/
[ogletest]: http://github.com/smartystreets/assertions/internal/ogletest
[oglemock]: http://github.com/smartystreets/assertions/internal/oglemock
[![GoDoc](https://godoc.org/github.com/smartystreets/assertions/internal/reqtrace?status.svg)](https://godoc.org/github.com/smartystreets/assertions/internal/reqtrace)

reqtrace is a package for simple request tracing. It requires nothing of its
user except:

 *  They must use [golang.org/x/net/context][context].
 *  They must add a single line to each function they want to be visible in
    traces.

[context]: http://godoc.org/golang.org/x/net/context

In particular, reqtrace is console-based and doesn't require an HTTP server.

**Warning**: This package is still barebones and in its early days. I reserve
the right to make backwards-incompatible changes to its API. But if it's useful
to you in your current form, have at it.

## Use

Call reqtrace.Trace anywhere you want to start a new root trace. (This is
probably where you create your root context.) This returns a new context that
you should pass to child operations, and a reporting function that you must use
to inform reqtrace when the trace is complete.

For example:

```Go
func HandleRequest(r *someRequest) (err error) {
  ctx, report := reqtrace.Trace(context.Background(), "HandleRequest")
  defer func() { report(err) }()

  // Do two things for this request.
  DoSomething(ctx, r)
  DoSomethingElse(ctx, r)
}
```

Within other functions that you want to show up in the trace, you
reqtrace.StartSpan (or its more convenient sibling reqtrace.StartSpanWithError):

```Go
func DoSomething(ctx context.Context, r *someRequest) (err error) {
  defer reqtrace.StartSpanWithError(&ctx, &err, "DoSomething")()

  // Process the request somehow using ctx. If downstream code also annotes
  // using reqtrace, reqtrace will know that its spans are descendants of
  // this one.
  CallAnotherLibrary(ctx, r.Param)
}
```

When `--reqtrace.enable` is set, the completion of a trace will cause helpful
ASCII art to be spit out.
GoConvey is awesome Go testing
==============================

[![Build Status](https://travis-ci.org/smartystreets/goconvey.png)](https://travis-ci.org/smartystreets/goconvey)
[![GoDoc](https://godoc.org/github.com/smartystreets/goconvey?status.svg)](http://godoc.org/github.com/smartystreets/goconvey)


Welcome to GoConvey, a yummy Go testing tool for gophers. Works with `go test`. Use it in the terminal or browser according to your viewing pleasure. **[View full feature tour.](http://goconvey.co)**

**Features:**

- Directly integrates with `go test`
- Fully-automatic web UI (works with native Go tests, too)
- Huge suite of regression tests
- Shows test coverage (Go 1.2+)
- Readable, colorized console output (understandable by any manager, IT or not)
- Test code generator
- Desktop notifications (optional)
- Immediately open problem lines in [Sublime Text](http://www.sublimetext.com) ([some assembly required](https://github.com/asuth/subl-handler))


You can ask questions about how to use GoConvey on [StackOverflow](http://stackoverflow.com/questions/ask?tags=goconvey,go&title=GoConvey%3A%20). Use the tags `go` and `goconvey`.

**Menu:**

- [Installation](#installation)
- [Quick start](#quick-start)
- [Documentation](#documentation)
- [Screenshots](#screenshots)
- [Contributors](#contributors-thanks)




Installation
------------

	$ go get github.com/smartystreets/goconvey

[Quick start](https://github.com/smartystreets/goconvey/wiki#get-going-in-25-seconds)
-----------

Make a test, for example:

```go
package package_name

import (
    "testing"
    . "github.com/smartystreets/goconvey/convey"
)

func TestSpec(t *testing.T) {

	// Only pass t into top-level Convey calls
	Convey("Given some integer with a starting value", t, func() {
		x := 1

		Convey("When the integer is incremented", func() {
			x++

			Convey("The value should be greater by one", func() {
				So(x, ShouldEqual, 2)
			})
		})
	})
}
```


#### [In the browser](https://github.com/smartystreets/goconvey/wiki/Web-UI)

Start up the GoConvey web server at your project's path:

	$ $GOPATH/bin/goconvey

Then watch the test results display in your browser at:

	http://localhost:8080


If the browser doesn't open automatically, please click [http://localhost:8080](http://localhost:8080) to open manually.

There you have it.
![](http://d79i1fxsrar4t.cloudfront.net/goconvey.co/gc-1-dark.png)
As long as GoConvey is running, test results will automatically update in your browser window.

![](http://d79i1fxsrar4t.cloudfront.net/goconvey.co/gc-5-dark.png)
The design is responsive, so you can squish the browser real tight if you need to put it beside your code.


The [web UI](https://github.com/smartystreets/goconvey/wiki/Web-UI) supports traditional Go tests, so use it even if you're not using GoConvey tests.



#### [In the terminal](https://github.com/smartystreets/goconvey/wiki/Execution)

Just do what you do best:

    $ go test

Or if you want the output to include the story:

    $ go test -v


[Documentation](https://github.com/smartystreets/goconvey/wiki)

-----------

Check out the

- [GoConvey wiki](https://github.com/smartystreets/goconvey/wiki),
- [![GoDoc](https://godoc.org/github.com/smartystreets/goconvey?status.png)](http://godoc.org/github.com/smartystreets/goconvey)
- and the *_test.go files scattered throughout this project.

[Screenshots](http://goconvey.co)

-----------

For web UI and terminal screenshots, check out [the full feature tour](http://goconvey.co).


----------------------

GoConvey is brought to you by [SmartyStreets](https://github.com/smartystreets) and [several contributors](https://github.com/smartystreets/goconvey/graphs/contributors) (Thanks!).
The Snappy compression format in the Go programming language.

To download and install from source:
$ go get github.com/golang/snappy

Unless otherwise noted, the Snappy-Go source files are distributed
under the BSD-style license found in the LICENSE file.



Benchmarks.

The golang/snappy benchmarks include compressing (Z) and decompressing (U) ten
or so files, the same set used by the C++ Snappy code (github.com/google/snappy
and note the "google", not "golang"). On an "Intel(R) Core(TM) i7-3770 CPU @
3.40GHz", Go's GOARCH=amd64 numbers as of 2016-05-29:

"go test -test.bench=."

_UFlat0-8         2.19GB/s ± 0%  html
_UFlat1-8         1.41GB/s ± 0%  urls
_UFlat2-8         23.5GB/s ± 2%  jpg
_UFlat3-8         1.91GB/s ± 0%  jpg_200
_UFlat4-8         14.0GB/s ± 1%  pdf
_UFlat5-8         1.97GB/s ± 0%  html4
_UFlat6-8          814MB/s ± 0%  txt1
_UFlat7-8          785MB/s ± 0%  txt2
_UFlat8-8          857MB/s ± 0%  txt3
_UFlat9-8          719MB/s ± 1%  txt4
_UFlat10-8        2.84GB/s ± 0%  pb
_UFlat11-8        1.05GB/s ± 0%  gaviota

_ZFlat0-8         1.04GB/s ± 0%  html
_ZFlat1-8          534MB/s ± 0%  urls
_ZFlat2-8         15.7GB/s ± 1%  jpg
_ZFlat3-8          740MB/s ± 3%  jpg_200
_ZFlat4-8         9.20GB/s ± 1%  pdf
_ZFlat5-8          991MB/s ± 0%  html4
_ZFlat6-8          379MB/s ± 0%  txt1
_ZFlat7-8          352MB/s ± 0%  txt2
_ZFlat8-8          396MB/s ± 1%  txt3
_ZFlat9-8          327MB/s ± 1%  txt4
_ZFlat10-8        1.33GB/s ± 1%  pb
_ZFlat11-8         605MB/s ± 1%  gaviota



"go test -test.bench=. -tags=noasm"

_UFlat0-8          621MB/s ± 2%  html
_UFlat1-8          494MB/s ± 1%  urls
_UFlat2-8         23.2GB/s ± 1%  jpg
_UFlat3-8         1.12GB/s ± 1%  jpg_200
_UFlat4-8         4.35GB/s ± 1%  pdf
_UFlat5-8          609MB/s ± 0%  html4
_UFlat6-8          296MB/s ± 0%  txt1
_UFlat7-8          288MB/s ± 0%  txt2
_UFlat8-8          309MB/s ± 1%  txt3
_UFlat9-8          280MB/s ± 1%  txt4
_UFlat10-8         753MB/s ± 0%  pb
_UFlat11-8         400MB/s ± 0%  gaviota

_ZFlat0-8          409MB/s ± 1%  html
_ZFlat1-8          250MB/s ± 1%  urls
_ZFlat2-8         12.3GB/s ± 1%  jpg
_ZFlat3-8          132MB/s ± 0%  jpg_200
_ZFlat4-8         2.92GB/s ± 0%  pdf
_ZFlat5-8          405MB/s ± 1%  html4
_ZFlat6-8          179MB/s ± 1%  txt1
_ZFlat7-8          170MB/s ± 1%  txt2
_ZFlat8-8          189MB/s ± 1%  txt3
_ZFlat9-8          164MB/s ± 1%  txt4
_ZFlat10-8         479MB/s ± 1%  pb
_ZFlat11-8         270MB/s ± 1%  gaviota



For comparison (Go's encoded output is byte-for-byte identical to C++'s), here
are the numbers from C++ Snappy's

make CXXFLAGS="-O2 -DNDEBUG -g" clean snappy_unittest.log && cat snappy_unittest.log

BM_UFlat/0     2.4GB/s  html
BM_UFlat/1     1.4GB/s  urls
BM_UFlat/2    21.8GB/s  jpg
BM_UFlat/3     1.5GB/s  jpg_200
BM_UFlat/4    13.3GB/s  pdf
BM_UFlat/5     2.1GB/s  html4
BM_UFlat/6     1.0GB/s  txt1
BM_UFlat/7   959.4MB/s  txt2
BM_UFlat/8     1.0GB/s  txt3
BM_UFlat/9   864.5MB/s  txt4
BM_UFlat/10    2.9GB/s  pb
BM_UFlat/11    1.2GB/s  gaviota

BM_ZFlat/0   944.3MB/s  html (22.31 %)
BM_ZFlat/1   501.6MB/s  urls (47.78 %)
BM_ZFlat/2    14.3GB/s  jpg (99.95 %)
BM_ZFlat/3   538.3MB/s  jpg_200 (73.00 %)
BM_ZFlat/4     8.3GB/s  pdf (83.30 %)
BM_ZFlat/5   903.5MB/s  html4 (22.52 %)
BM_ZFlat/6   336.0MB/s  txt1 (57.88 %)
BM_ZFlat/7   312.3MB/s  txt2 (61.91 %)
BM_ZFlat/8   353.1MB/s  txt3 (54.99 %)
BM_ZFlat/9   289.9MB/s  txt4 (66.26 %)
BM_ZFlat/10    1.2GB/s  pb (19.68 %)
BM_ZFlat/11  527.4MB/s  gaviota (37.72 %)
# GoPacket

This library provides packet decoding capabilities for Go.
See [godoc](https://godoc.org/github.com/google/gopacket) for more details.

[![Build Status](https://travis-ci.org/google/gopacket.svg?branch=master)](https://travis-ci.org/google/gopacket)
[![GoDoc](https://godoc.org/github.com/google/gopacket?status.svg)](https://godoc.org/github.com/google/gopacket)

Originally forked from the gopcap project written by Andreas
Krennmair <ak@synflood.at> (http://github.com/akrennmair/gopcap).
# getpasswd in Go [![GoDoc](https://godoc.org/github.com/howeyc/gopass?status.svg)](https://godoc.org/github.com/howeyc/gopass)

Retrieve password from user terminal input without echo

Verified on BSD, Linux, and Windows.

Example:
```go
package main

import "fmt"
import "github.com/howeyc/gopass"

func main() {
	fmt.Printf("Password: ")
	pass := gopass.GetPasswd() // Silent, for *'s use gopass.GetPasswdMasked()
    // Do something with pass
}
```

Caution: Multi-byte characters not supported!
GopherJS - A compiler from Go to JavaScript
-------------------------------------------

[![GoDoc](https://godoc.org/github.com/gopherjs/gopherjs/js?status.svg)](https://godoc.org/github.com/gopherjs/gopherjs/js)
[![Sourcegraph](https://sourcegraph.com/github.com/gopherjs/gopherjs/-/badge.svg)](https://sourcegraph.com/github.com/gopherjs/gopherjs?badge)
[![Circle CI](https://circleci.com/gh/gopherjs/gopherjs.svg?style=svg)](https://circleci.com/gh/gopherjs/gopherjs)

GopherJS compiles Go code ([golang.org](https://golang.org/)) to pure JavaScript code. Its main purpose is to give you the opportunity to write front-end code in Go which will still run in all browsers.

### Playground
Give GopherJS a try on the [GopherJS Playground](http://gopherjs.github.io/playground/).

### What is supported?
Nearly everything, including Goroutines ([compatibility table](https://github.com/gopherjs/gopherjs/blob/master/doc/packages.md)). Performance is quite good in most cases, see [HTML5 game engine benchmark](https://ajhager.github.io/engi/demos/botmark.html). Cgo is not supported.

### Installation and Usage
Get or update GopherJS and dependencies with:

```
go get -u github.com/gopherjs/gopherjs
```

Now you can use `gopherjs build [package]`, `gopherjs build [files]` or `gopherjs install [package]` which behave similar to the `go` tool. For `main` packages, these commands create a `.js` file and `.js.map` source map in the current directory or in `$GOPATH/bin`. The generated JavaScript file can be used as usual in a website. Use `gopherjs help [command]` to get a list of possible command line flags, e.g. for minification and automatically watching for changes.

`gopherjs` uses your platform's default `GOOS` value when generating code. Supported `GOOS` values are: `linux`, `darwin`. If you're on a different platform (e.g., Windows or FreeBSD), you'll need to set the `GOOS` environment variable to a supported value. For example, `GOOS=linux gopherjs build [package]`.

*Note: GopherJS will try to write compiled object files of the core packages to your $GOROOT/pkg directory. If that fails, it will fall back to $GOPATH/pkg.*

#### gopherjs run, gopherjs test

If you want to use `gopherjs run` or `gopherjs test` to run the generated code locally, install Node.js 10.0.0 (or newer), and the `source-map-support` module:

```
npm install --global source-map-support
```

On supported `GOOS` platforms, it's possible to make system calls (file system access, etc.) available. See [doc/syscalls.md](https://github.com/gopherjs/gopherjs/blob/master/doc/syscalls.md) for instructions on how to do so.

#### gopherjs serve

`gopherjs serve` is a useful command you can use during development. It will start an HTTP server serving on ":8080" by default, then dynamically compile your Go packages with GopherJS and serve them.

For example, navigating to `http://localhost:8080/example.com/user/project/` should compile and run the Go package `example.com/user/project`. The generated JavaScript output will be served at `http://localhost:8080/example.com/user/project/project.js` (the .js file name will be equal to the base directory name). If the directory contains `index.html` it will be served, otherwise a minimal `index.html` that includes `<script src="project.js"></script>` will be provided, causing the JavaScript to be executed. All other static files will be served too.

Refreshing in the browser will rebuild the served files if needed. Compilation errors will be displayed in terminal, and in browser console. Additionally, it will serve $GOROOT and $GOPATH for sourcemaps.

If you include an argument, it will be the root from which everything is served. For example, if you run `gopherjs serve github.com/user/project` then the generated JavaScript for the package github.com/user/project/mypkg will be served at http://localhost:8080/mypkg/mypkg.js.

### Performance Tips

- Use the `-m` command line flag to generate minified code.
- Apply gzip compression (https://en.wikipedia.org/wiki/HTTP_compression).
- Use `int` instead of `(u)int8/16/32/64`.
- Use `float64` instead of `float32`.

### Community
- [#gopherjs Channel on Gophers Slack](https://gophers.slack.com/messages/gopherjs/) (invites to Gophers Slack are available [here](http://blog.gopheracademy.com/gophers-slack-community/#how-can-i-be-invited-to-join:2facdc921b2310f18cb851c36fa92369))
- [Bindings to JavaScript APIs and libraries](https://github.com/gopherjs/gopherjs/wiki/bindings)
- [GopherJS Blog](https://medium.com/gopherjs)
- [GopherJS on Twitter](https://twitter.com/GopherJS)

### Getting started

#### Interacting with the DOM
The package `github.com/gopherjs/gopherjs/js` (see [documentation](https://godoc.org/github.com/gopherjs/gopherjs/js)) provides functions for interacting with native JavaScript APIs. For example the line

```js
document.write("Hello world!");
```

would look like this in Go:

```go
js.Global.Get("document").Call("write", "Hello world!")
```

You may also want use the [DOM bindings](http://dominik.honnef.co/go/js/dom), the [jQuery bindings](https://github.com/gopherjs/jquery) (see [TodoMVC Example](https://github.com/gopherjs/todomvc)) or the [AngularJS bindings](https://github.com/wvell/go-angularjs). Those are some of the [bindings to JavaScript APIs and libraries](https://github.com/gopherjs/gopherjs/wiki/bindings) by community members.

#### Providing library functions for use in other JavaScript code
Set a global variable to a map that contains the functions:

```go
package main

import "github.com/gopherjs/gopherjs/js"

func main() {
	js.Global.Set("pet", map[string]interface{}{
		"New": New,
	})
}

type Pet struct {
	name string
}

func New(name string) *js.Object {
	return js.MakeWrapper(&Pet{name})
}

func (p *Pet) Name() string {
	return p.name
}

func (p *Pet) SetName(name string) {
	p.name = name
}
```

For more details see [Jason Stone's blog post](http://legacytotheedge.blogspot.de/2014/03/gopherjs-go-to-javascript-transpiler.html) about GopherJS.

### Architecture

#### General
GopherJS emulates a 32-bit environment. This means that `int`, `uint` and `uintptr` have a precision of 32 bits. However, the explicit 64-bit integer types `int64` and `uint64` are supported. The `GOARCH` value of GopherJS is "js". You may use it as a build constraint: `// +build js`.

#### Application Lifecycle

The `main` function is executed as usual after all `init` functions have run. JavaScript callbacks can also invoke Go functions, even after the `main` function has exited. Therefore the end of the `main` function should not be regarded as the end of the application and does not end the execution of other goroutines.

In the browser, calling `os.Exit` (e.g. indirectly by `log.Fatal`) also does not terminate the execution of the program. For convenience, it calls `runtime.Goexit` to immediately terminate the calling goroutine.

#### Goroutines
Goroutines are fully supported by GopherJS. The only restriction is that you need to start a new goroutine if you want to use blocking code called from external JavaScript:

```go
js.Global.Get("myButton").Call("addEventListener", "click", func() {
  go func() {
    [...]
    someBlockingFunction()
    [...]
  }()
})
```

How it works:

JavaScript has no concept of concurrency (except web workers, but those are too strictly separated to be used for goroutines). Because of that, instructions in JavaScript are never blocking. A blocking call would effectively freeze the responsiveness of your web page, so calls with callback arguments are used instead.

GopherJS does some heavy lifting to work around this restriction: Whenever an instruction is blocking (e.g. communicating with a channel that isn't ready), the whole stack will unwind (= all functions return) and the goroutine will be put to sleep. Then another goroutine which is ready to resume gets picked and its stack with all local variables will be restored.

### GopherJS Development
If you're looking to make changes to the GopherJS compiler, see [Developer Guidelines](https://github.com/gopherjs/gopherjs/wiki/Developer-Guidelines) for additional developer information.
# go-cache

go-cache is an in-memory key:value store/cache similar to memcached that is
suitable for applications running on a single machine. Its major advantage is
that, being essentially a thread-safe `map[string]interface{}` with expiration
times, it doesn't need to serialize or transmit its contents over the network.

Any object can be stored, for a given duration or forever, and the cache can be
safely used by multiple goroutines.

Although go-cache isn't meant to be used as a persistent datastore, the entire
cache can be saved to and loaded from a file (using `c.Items()` to retrieve the
items map to serialize, and `NewFrom()` to create a cache from a deserialized
one) to recover from downtime quickly. (See the docs for `NewFrom()` for caveats.)

### Installation

`go get github.com/patrickmn/go-cache`

### Usage

```go
	import (
		"fmt"
		"github.com/patrickmn/go-cache"
		"time"
	)

	func main() {

		// Create a cache with a default expiration time of 5 minutes, and which
		// purges expired items every 30 seconds
		c := cache.New(5*time.Minute, 30*time.Second)

		// Set the value of the key "foo" to "bar", with the default expiration time
		c.Set("foo", "bar", cache.DefaultExpiration)

		// Set the value of the key "baz" to 42, with no expiration time
		// (the item won't be removed until it is re-set, or removed using
		// c.Delete("baz")
		c.Set("baz", 42, cache.NoExpiration)

		// Get the string associated with the key "foo" from the cache
		foo, found := c.Get("foo")
		if found {
			fmt.Println(foo)
		}

		// Since Go is statically typed, and cache values can be anything, type
		// assertion is needed when values are being passed to functions that don't
		// take arbitrary types, (i.e. interface{}). The simplest way to do this for
		// values which will only be used once--e.g. for passing to another
		// function--is:
		foo, found := c.Get("foo")
		if found {
			MyFunction(foo.(string))
		}

		// This gets tedious if the value is used several times in the same function.
		// You might do either of the following instead:
		if x, found := c.Get("foo"); found {
			foo := x.(string)
			// ...
		}
		// or
		var foo string
		if x, found := c.Get("foo"); found {
			foo = x.(string)
		}
		// ...
		// foo can then be passed around freely as a string

		// Want performance? Store pointers!
		c.Set("foo", &MyStruct, cache.DefaultExpiration)
		if x, found := c.Get("foo"); found {
			foo := x.(*MyStruct)
			// ...
		}

		// If you store a reference type like a pointer, slice, map or channel, you
		// do not need to run Set if you modify the underlying data. The cached
		// reference points to the same memory, so if you modify a struct whose
		// pointer you've stored in the cache, retrieving that pointer with Get will
		// point you to the same data:
		foo := &MyStruct{Num: 1}
		c.Set("foo", foo, cache.DefaultExpiration)
		// ...
		x, _ := c.Get("foo")
		foo := x.(*MyStruct)
		fmt.Println(foo.Num)
		// ...
		foo.Num++
		// ...
		x, _ := c.Get("foo")
		foo := x.(*MyStruct)
		foo.Println(foo.Num)

		// will print:
		// 1
		// 2

	}
```

### Reference

`godoc` or [http://godoc.org/github.com/patrickmn/go-cache](http://godoc.org/github.com/patrickmn/go-cache)
## Termbox
Termbox is a library that provides a minimalistic API which allows the programmer to write text-based user interfaces. The library is crossplatform and has both terminal-based implementations on *nix operating systems and a winapi console based implementation for windows operating systems. The basic idea is an abstraction of the greatest common subset of features available on all major terminals and other terminal-like APIs in a minimalistic fashion. Small API means it is easy to implement, test, maintain and learn it, that's what makes the termbox a distinct library in its area.

### Installation
Install and update this go package with `go get -u github.com/nsf/termbox-go`

### Examples
For examples of what can be done take a look at demos in the _demos directory. You can try them with go run: `go run _demos/keyboard.go`

There are also some interesting projects using termbox-go:
 - [godit](https://github.com/nsf/godit) is an emacsish lightweight text editor written using termbox.
 - [gomatrix](https://github.com/GeertJohan/gomatrix) connects to The Matrix and displays its data streams in your terminal.
 - [gotetris](https://github.com/jjinux/gotetris) is an implementation of Tetris.
 - [sokoban-go](https://github.com/rn2dy/sokoban-go) is an implementation of sokoban game.
 - [hecate](https://github.com/evanmiller/hecate) is a hex editor designed by Satan.
 - [httopd](https://github.com/verdverm/httopd) is top for httpd logs.
 - [mop](https://github.com/michaeldv/mop) is stock market tracker for hackers.
 - [termui](https://github.com/gizak/termui) is a terminal dashboard.
 - [termloop](https://github.com/JoelOtter/termloop) is a terminal game engine.
 - [xterm-color-chart](https://github.com/kutuluk/xterm-color-chart) is a XTerm 256 color chart.
 - [gocui](https://github.com/jroimartin/gocui) is a minimalist Go library aimed at creating console user interfaces.
 - [dry](https://github.com/moncho/dry) is an interactive cli to manage Docker containers.
 - [pxl](https://github.com/ichinaski/pxl) displays images in the terminal.
 - [snake-game](https://github.com/DyegoCosta/snake-game) is an implementation of the Snake game.
 - [gone](https://github.com/guillaumebreton/gone) is a CLI pomodoro® timer.

### API reference
[godoc.org/github.com/nsf/termbox-go](http://godoc.org/github.com/nsf/termbox-go)
# spacelog [![Build Status](https://api.travis-ci.org/spacemonkeygo/spacelog.svg?branch=master)](https://travis-ci.org/spacemonkeygo/spacelog)

Please see http://godoc.org/github.com/spacemonkeygo/spacelog for info

### License

Copyright (C) 2014 Space Monkey, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
go-flags: a go library for parsing command line arguments
=========================================================

[![GoDoc](https://godoc.org/github.com/jessevdk/go-flags?status.png)](https://godoc.org/github.com/jessevdk/go-flags) [![Build Status](https://travis-ci.org/jessevdk/go-flags.svg?branch=master)](https://travis-ci.org/jessevdk/go-flags) [![Coverage Status](https://img.shields.io/coveralls/jessevdk/go-flags.svg)](https://coveralls.io/r/jessevdk/go-flags?branch=master)

This library provides similar functionality to the builtin flag library of
go, but provides much more functionality and nicer formatting. From the
documentation:

Package flags provides an extensive command line option parser.
The flags package is similar in functionality to the go builtin flag package
but provides more options and uses reflection to provide a convenient and
succinct way of specifying command line options.

Supported features:
* Options with short names (-v)
* Options with long names (--verbose)
* Options with and without arguments (bool v.s. other type)
* Options with optional arguments and default values
* Multiple option groups each containing a set of options
* Generate and print well-formatted help message
* Passing remaining command line arguments after -- (optional)
* Ignoring unknown command line options (optional)
* Supports -I/usr/include -I=/usr/include -I /usr/include option argument specification
* Supports multiple short options -aux
* Supports all primitive go types (string, int{8..64}, uint{8..64}, float)
* Supports same option multiple times (can store in slice or last option counts)
* Supports maps
* Supports function callbacks
* Supports namespaces for (nested) option groups

The flags package uses structs, reflection and struct field tags
to allow users to specify command line options. This results in very simple
and concise specification of your application options. For example:

```go
type Options struct {
	Verbose []bool `short:"v" long:"verbose" description:"Show verbose debug information"`
}
```

This specifies one option with a short name -v and a long name --verbose.
When either -v or --verbose is found on the command line, a 'true' value
will be appended to the Verbose field. e.g. when specifying -vvv, the
resulting value of Verbose will be {[true, true, true]}.

Example:
--------
```go
var opts struct {
	// Slice of bool will append 'true' each time the option
	// is encountered (can be set multiple times, like -vvv)
	Verbose []bool `short:"v" long:"verbose" description:"Show verbose debug information"`

	// Example of automatic marshalling to desired type (uint)
	Offset uint `long:"offset" description:"Offset"`

	// Example of a callback, called each time the option is found.
	Call func(string) `short:"c" description:"Call phone number"`

	// Example of a required flag
	Name string `short:"n" long:"name" description:"A name" required:"true"`

	// Example of a value name
	File string `short:"f" long:"file" description:"A file" value-name:"FILE"`

	// Example of a pointer
	Ptr *int `short:"p" description:"A pointer to an integer"`

	// Example of a slice of strings
	StringSlice []string `short:"s" description:"A slice of strings"`

	// Example of a slice of pointers
	PtrSlice []*string `long:"ptrslice" description:"A slice of pointers to string"`

	// Example of a map
	IntMap map[string]int `long:"intmap" description:"A map from string to int"`
}

// Callback which will invoke callto:<argument> to call a number.
// Note that this works just on OS X (and probably only with
// Skype) but it shows the idea.
opts.Call = func(num string) {
	cmd := exec.Command("open", "callto:"+num)
	cmd.Start()
	cmd.Process.Release()
}

// Make some fake arguments to parse.
args := []string{
	"-vv",
	"--offset=5",
	"-n", "Me",
	"-p", "3",
	"-s", "hello",
	"-s", "world",
	"--ptrslice", "hello",
	"--ptrslice", "world",
	"--intmap", "a:1",
	"--intmap", "b:5",
	"arg1",
	"arg2",
	"arg3",
}

// Parse flags from `args'. Note that here we use flags.ParseArgs for
// the sake of making a working example. Normally, you would simply use
// flags.Parse(&opts) which uses os.Args
args, err := flags.ParseArgs(&opts, args)

if err != nil {
	panic(err)
	os.Exit(1)
}

fmt.Printf("Verbosity: %v\n", opts.Verbose)
fmt.Printf("Offset: %d\n", opts.Offset)
fmt.Printf("Name: %s\n", opts.Name)
fmt.Printf("Ptr: %d\n", *opts.Ptr)
fmt.Printf("StringSlice: %v\n", opts.StringSlice)
fmt.Printf("PtrSlice: [%v %v]\n", *opts.PtrSlice[0], *opts.PtrSlice[1])
fmt.Printf("IntMap: [a:%v b:%v]\n", opts.IntMap["a"], opts.IntMap["b"])
fmt.Printf("Remaining args: %s\n", strings.Join(args, " "))

// Output: Verbosity: [true true]
// Offset: 5
// Name: Me
// Ptr: 3
// StringSlice: [hello world]
// PtrSlice: [hello world]
// IntMap: [a:1 b:5]
// Remaining args: arg1 arg2 arg3
```

More information can be found in the godocs: <http://godoc.org/github.com/jessevdk/go-flags>
Golint is a linter for Go source code.

To install, run
  go get github.com/golang/lint/golint

Invoke golint with one or more filenames or directories.
The output of this tool is a list of suggestions in Vim quickfix format,
which is accepted by lots of different editors.

Golint differs from gofmt. Gofmt reformats Go source code, whereas
golint prints out style mistakes.

Golint differs from govet. Govet is concerned with correctness, whereas
golint is concerned with coding style. Golint is in use at Google, and it
seeks to match the accepted style of the open source Go project.

The suggestions made by golint are exactly that: suggestions.
Golint is not perfect, and has both false positives and false negatives.
Do not treat its output as a gold standard. We will not be adding pragmas
or other knobs to suppress specific warnings, so do not expect or require
code to be completely "lint-free".
In short, this tool is not, and will never be, trustworthy enough for its
suggestions to be enforced automatically, for example as part of a build process.

If you find an established style that is frequently violated, and which
you think golint could statically check, file an issue at
  https://github.com/golang/lint/issues


Contributions
-------------
Contributions to this project are welcome, though please send mail before
starting work on anything major. Contributors retain their copyright, so we
need you to fill out a short form before we can accept your contribution:
  https://developers.google.com/open-source/cla/individual


Vim
---
Add this to your ~/.vimrc:
  set rtp+=$GOPATH/src/github.com/golang/lint/misc/vim
If you have multiple entries in your GOPATH, replace $GOPATH with the right value.

Running :Lint will run golint on the current file and populate the quickfix list.

Optionally, add this to your ~/.vimrc to automatically run golint on :w
  autocmd BufWritePost,FileWritePost *.go execute 'Lint' | cwindow


Emacs
-----
Add this to your .emacs file:
  (add-to-list 'load-path (concat (getenv "GOPATH")  "/src/github.com/golang/lint/misc/emacs"))
  (require 'golint)
If you have multiple entries in your GOPATH, replace $GOPATH with the right value.

Running M-x golint will run golint on the current file.
For more usage, see Compilation-Mode:
  http://www.gnu.org/software/emacs/manual/html_node/emacs/Compilation-Mode.html
# mongoreplay
##### Purpose

`mongoreplay` is a traffic capture and replay tool for MongoDB. It can be used to inspect commands being sent to a MongoDB instance, record them, and replay them back onto another host at a later time.
##### Use cases
- Preview how well your database cluster would perform a production workload under a different environment (storage engine, index, hardware, OS, etc.)
- Reproduce and investigate bugs by recording and replaying the operations that trigger them 
- Inspect the details of what an application is doing to a mongo cluster (i.e. a more flexible version of [mongosniff](https://docs.mongodb.org/manual/reference/program/mongosniff/))

## Quickstart

Make a recording:

    mongoreplay record -i lo0 -e "port 27017" -p playback.bson
Analyze it:

    mongoreplay stat -p playback.bson --report playback_stats.json
Replay it against another server, at 2x speed:

    mongoreplay play -p playback.bson --speed=2.0 --report replay_stats.json --host 192.168.0.4:27018

## Detailed Usage

Basic usage of `mongoreplay` works in two phases: `record` and `play`. Analyzing recordings can also be performed with the `stat` command.
* The `record` phase takes a [pcap](https://en.wikipedia.org/wiki/Pcap) file (generated by `tcpdump`) and analyzes it to produce a playback file (in BSON format). The playback file contains a list of all the requests and replies to/from the Mongo instance that were recorded in the pcap dump, along with their connection identifier, timestamp, and other metadata.
* The `play` reads in the playback file that was generated by `record`, and re-executes the workload against some target host. 
* The `stat` command reads a playback file and analyzes it, detecting the latency between each request and response. 

#### Capturing TCP (pcap) data

To create a recording of traffic, use the `record` command as follows:

    mongoreplay record -i lo0 -e "port 27017" -p recording.bson
    

This will record traffic on the network interface `lo0` targeting port 27017.
The options to `record` are:
* `-i`: The network interface to listen on, e.g. `eth0` or `lo0`. You may be required to run `mongoreplay` with root privileges for this to work.
* `-e`: An expression in Berkeley Packet Filter (BPF) syntax to apply to incoming traffic to record. See http://biot.com/capstats/bpf.html for details on how to construct BPF expressions.
* `-p`: The output file to write the recording to.

#### Recording a playback file from pcap data

Alternatively, you can capture traffic using `tcpdump` and create a recording from a static PCAP file. First, capture TCP traffic on the system where the workload you wish to record is targeting. Then, run `mongoreplay record` using the `-f` argument (instead of `-i`) to create the playback file.

    sudo tcpdump -i lo0 -n "port 27017" -w traffic.pcap

    $ ./mongoreplay record -f traffic.pcap -p playback.bson

Using the `record` command of mongoreplay, this will process the .pcap file to create a playback file. The playback file will contain everything needed to re-execute the workload.

### Using playback files

There are several useful operations that can be performed with the playback file.

##### Re-executing the playback file
The `play` command takes a playback file and executes the operations in it against a target host.

    ./mongoreplay play -p playback.bson --host mongodb://target-host.com:27017
    
To modify playback speed, add the `--speed` command line flag to the `play` command. For example, `--speed=2.0` will run playback at twice the rate of the recording, while `--speed=0.5` will run playback at half the rate of the recording.

    mongoreplay play -p workload.playback --host staging-mongo-cluster-hostname

###### Playback speed
You can also play the workload back at a faster rate by adding the --speed argument; for example, --speed=2.0 will execute the workload at twice the speed it was recorded at. 

###### Logging metrics about execution performance during playback
Use the `--report=<path-to-file>` flag to save  detailed metrics about the performance of each operation performed during playback to the specified json file. This can be used in later analysis to compare performance and behavior across  different executions of the same workload.

##### Inspecting the operations in a playback file

The `stat` command takes a static workload file (bson) and generates a json report, showing each operation and some metadata about its execution. The output is in the same format as that used by the json output generated by using the `play` command with `--report`.

###### Report format

The data in the json reports consists of one record for each request/response. Each record has the following format:
```json
{
    "connection_num": 1,
    "latency_us": 89,
    "ns": "test.test",
    "op": "getmore",
    "order": 16,
    "play_at": "2016-02-02T16:24:16.309322601-05:00",
    "played_at": "2016-02-02T16:24:16.310908311-05:00",
    "playbacklag_us": 1585
}             
```

The fields are as follows:
 * `connection_num`: a key that identifies the connection on which the request was executed. All requests/replies that executed on the same connection will have the same value for this field. The value for this field does *not* match the connection ID logged on the server-side.
 * `latency_us`: the time difference (in microseconds) between when the request was sent by the client, and a response from the server was received.
 * `ns`: the namespace that the request was executed on.
 * `op`: the type of operation represented by the request - e.g. "query", "insert", "command", "getmore"
 * `order`: a monotonically increasing key indicating the order in which the operations were recorded and played back. This can be used to reconstruct the ordering of the series of ops executed on a connection, since the order in which they appear in the report file might not match the order of playback.
 * `data`: the payload of the actual operation. For queries, this will contain the actual query that was issued. For inserts, this will contain the documents being inserted. For updates, it will contain the query selector and the update modifier, etc.
 * `play_at`: The time at which the operation was supposed to be executed.
 * `played_at`: The time at which the `play` command actually executed the operation.
 * `playbacklag_us`: The difference (in microseconds) in time between `played_at` and `play_at`. Higher values generally indicate that the target server is not able to keep up with the rate at which requests need to be executed according to the playback file.
This suite contains tests that are unusually susceptible to availability of machine resources;
therefore, this suite is always run with --jobs=1 via Evergreen config.rollover_*.pem are certificates and a CA used to test rolling over X509 cluster authentication

# Generate the root CA certificate:
openssl genrsa -out rollover_ca.key 4096
openssl req -key rollover_ca.key -new -x509 -days 3650 -out rollover_ca.pem \
    -subj '/CN=Kernel Rollover Test CA/OU=Kernel/O=MongoDB\, Inc./L=New York/ST=New York/C=US' \
    -addext "keyUsage = critical, digitalSignature, cRLSign, keyCertSign"

cat rollover_ca.pem ca.pem > rollover_ca_merged.pem
cat rollover_ca.key >> rollover_ca.pem
rm rollover_ca.key

# Generate the server key and cert:
openssl genrsa -out rollover_server.key 2048
openssl req -new -key rollover_server.key -days 3650 -out rollover_server.csr \
    -subj '/CN=server/OU=Kernel (Rollover)/O=MongoDB\, Inc. (Rollover)/L=New York/ST=New York/C=US/'

# Sign the new server cert and clean up
openssl x509 -req -days 3650 -in rollover_server.csr -CA rollover_ca.pem -CAcreateserial \
    -out rollover_server.pem -sha256 -extfile <(printf "subjectAltName=DNS:localhost,DNS:127.0.0.1")
cat rollover_server.key >> rollover_server.pem
rm rollover_server.key
rm rollover_server.csr
rm rollover_ca.srl

---------------------------

client-self-signed.pem represents the same RDN as client.pem, but using itself as a CA:

openssl req -nodes -new -subj '/CN=client/OU=KernelUser/O=MongoDB/L=New York City/ST=New York/C=US' -out css.csr -keyout css.rsa
openssl rsa -in css.rsa -out css.key
openssl x509 -in css.csr -out jstests/libs/client-self-signed.pem -req -signkey client-self-signed.key -days 3650
cat css.key >> jstests/libs/client-self-signed.pem
rm css.{csr,rsa,key}

---------------------------
client-multivalue-rdn.pem represents the same RDN as client.pem, but grouping some elements together:

openssl req -new -nodes -subj '/CN=client+OU=KernelUser+O=MongoDB/L=New York City+ST=New York+C=US' -multivalue-rdn \
            -keyout client-multivalue-rdn.key -out client-multivalue-rdn.csr
openssl rsa -in client-multivalue-rdn.key -out client-multivalue-rdn.rsa
openssl x509 -in client-multivalue-rdn.csr -out client-multivalue-rdn.pem -req -CA ca.pem -days 3650 -CAcreateserial
cat client-multivalue-rdn.rsa >> client-multivalue-rdn.pem
rm ca.srl client-multivalue-rdn.key client-multivalue-rdn.rsa client-multivalue-rdn.csr

---------------------------
ecdsa-*.pem are ECDSA signed certificates:

generate an ec-key (from a well known curve)
openssl ecparam -name prime256v1 -genkey -out mykey.key

create certificate request
openssl req -new -key mykey.key -out mycsr.csr

sign key and generate certificate
openssl x509 -req -days 3650 -in mycsr.csr -CA ecdsa-ca.pem -CAcreateserial -out mycrt.crt -sha256

to include SANs in the certificate, instead run
openssl x509 -req -days 3650 -in mycsr.csr -CA ecdsa-ca.pem -CAcreateserial -out mycrt.crt -sha256 -extfile <(printf "subjectAltName=DNS:localhost,DNS:127.0.0.1")

combine key and certificate
cat mycrt.crt mykey.key > mycrt.pem

---------------------------
The other ceriticates in this directory come from x509gen.
How to generate a certificate with a custom extension:

1. Generate a normal certificate signing request without an extension
2. Make a copy of the system openssl.cnf and append this text to the file
    On Redhat/Fedora, openssl.cnf is in /etc/pki/tls

See jstests\libs\mongodbauthorizationgrant.cnf for how to generate the text with the
'openssl asn1parse' command.

[MongoDBAuthorizationGrant]
1.3.6.1.4.1.34601.2.1.1 = DER:312B300F0C066261636B75700C0561646D696E30180C0F72656164416E7944617461626173650C0561646D696E

3. Sign the certificate and add the custom extension
4. Make a new pem with the certificate and key

Example Commands
----------------
openssl req -config openssl.cnf -newkey rsa:2048 -nodes -keyout roles.key -out roles.csr

Example with subject name:
openssl req -config openssl.cnf -newkey rsa:2048 -nodes -keyout roles.key -out roles.csr -subj "/C=US/ST=New York/L=New York City/O=MongoDB/OU=KernelUser/CN=client/emailAddress=example@mongodb.com"

openssl x509 -req -sha256 -in roles.csr -days 3650 -out roles.pem -extfile openssl.cnf -extensions MongoDBAuthorizationGrant -CA jstests/libs/ca.pem -CAcreateserial

openssl rsa -in roles.key -out roles2.key

cat roles.pem roles2.key > roles_final.pem


Example Commands for UTF-8
--------------------------
openssl req -new -utf8 -nameopt multiline,utf8  -config .\jstests\libs\client_utf8.cnf -newkey rsa:2048 -nodes -keyout roles.key -out roles.csr
# Profiling an Application on iOS
How to profile a test application for iOS

## Set up Your Mac OSX Environment
1. Download Xcode

## Set up Xcode
1. Enable the Developer app on the iOS device
   * Settings/General/Device Management: Select the Developer app and Trust

## MongoProfiler
The `MongoProfiler` is a custom profiling template which includes
  * Energy Log - this must be imported from the iOS device and should be captured untethered
    Captures battery level
  * Activity Monitor - this can be captured via USB cable or wirelessly
    Captures CPU load
  * Virtual Memory Trace - this can be captured via USB cable or wirelessly
    Captures memory usage

## Run Profiler on the Mac
1. Connect the iOS device to the Mac via USB cable
1. Start Instruments on Mac
  * Can be started from within Xcode or from the Spotlight Search
1. Connect to the iOS device and select an app to profile
1. Open a Custom profiling template and select `MongoProfiler`
1. Start recording
1. Start the application on the iOS device
1. Stop recording in Instruments

## Run Profiler Wirelessly on the Mac
1. Ensure the Mac and iOS device are on the same WiFi network
1. Connect the iOS device to the Mac via USB cable
1. Pair the devices in Xcode
See https://help.apple.com/xcode/mac/9.0/index.html?localePath=en.lproj#/devbc48d1bad
  * Select Windows/Devices & Simulators
  * Select the Devices tab, select the iOS device and select `Connect via network`
1. Disconnect the USB cable
1. Follow the instructions from step 2 in `Run profiler on the Mac`

## Measuring Energy Usage on the iOS device
Unfortunately Instruments cannot measure Energy usage by recording from the Mac, but only from the iOS device.
1. Select Settings/Developer/Logging on the iOS device
1. Enable Energy
1. Select `Start Recording` (note this can be done before recording within Instruments for the other probes)
1. After the test is completed, select `Stop Recording`
1. From within Instruments on the Mac (note this can be done using the `MongoProfiler` so all probes are captured together)
  * Select File, `Import Logged Data From Device`
# Profiling an Application on Android
How to profile a test application for Android

## Set up Your Local Environment
1. Download ADB SDK
1. Add the SDK platform-tools to your PATH
   * export PATH="$PATH:$HOME/Library/Android/sdk/platform-tools"

## Run the ADB profiler
The ADB profiler is a custom script which provides
  * Battery statistics - battery.csv
  * Memory statistics - memory.csv
  * CPU statistics - cpu.json
`python buildscripts/mobile/adb_monitor.py`


## Enable USB Debugging on Android Device
Enabling USB debugging can differ by device, see https://developer.android.com/studio/debug/dev-options
1. Enable USB debugging via ADB, example
  * Select Settings/About phone(or tablet)
  * Select Build number 7 times, to enable Developer Options
  * Select Settings/Developer Options/USB Debugging
1. Connect the Android device to the computer via USB cable
1. Select "Aways allow from this computer" and OK, when the prompt "Allow USB debugging?" appears on the device

## Run the ADB Profiler Wirelessly
1. Ensure the local computer and Android device are on the same network
1. Connect the Android device to the computer via USB cable
1. Set the Android device's ADB listening port
   * `adb devices`
   * `adb tcpip 5555`
1. Disconnect the USB cable
1. Identify the Android's IP address
   * Settings/About phone(or tablet)/Status
   * `adb_ip=<ip_address>`, i.e., adb_ip=10.4.123.244
1. Connect wirelessly to the Android device
   * `adb connect $adb_ip`
1. Ensure you can connect to the Android device
   * `adb shell uptime`
1. Run the ADB profiler as detailed above
MongoDB README

Welcome to MongoDB!

COMPONENTS

  mongod - The database server.
  mongos - Sharding router.
  mongo  - The database shell (uses interactive javascript).

UTILITIES

  mongodump         - Create a binary dump of the contents of a database.
  mongorestore      - Restore data from the output created by mongodump.
  mongoexport       - Export the contents of a collection to JSON or CSV.
  mongoimport       - Import data from JSON, CSV or TSV.
  mongofiles        - Put, get and delete files from GridFS.
  mongostat         - Show the status of a running mongod/mongos.
  bsondump          - Convert BSON files into human-readable formats.
  mongoreplay       - Traffic capture and replay tool.
  mongotop          - Track time spent reading and writing data.
  install_compass   - Installs MongoDB Compass for your platform.

BUILDING

  See docs/building.md.

RUNNING

  For command line options invoke:

    $ ./mongod --help

  To run a single server database:

    $ sudo mkdir -p /data/db
    $ ./mongod
    $
    $ # The mongo javascript shell connects to localhost and test database by default:
    $ ./mongo
    > help

INSTALLING COMPASS

  You can install compass using the install_compass script packaged with MongoDB:

    $ ./install_compass

  This will download the appropriate MongoDB Compass package for your platform
  and install it.

DRIVERS

  Client drivers for most programming languages are available at
  https://docs.mongodb.com/manual/applications/drivers/. Use the shell
  ("mongo") for administrative tasks.

BUG REPORTS

  See https://github.com/mongodb/mongo/wiki/Submit-Bug-Reports.

PACKAGING

  Packages are created dynamically by the package.py script located in the
  buildscripts directory. This will generate RPM and Debian packages.

DOCUMENTATION

  https://docs.mongodb.com/manual/

CLOUD HOSTED MONGODB

  https://www.mongodb.com/cloud/atlas

MAIL LISTS

  https://groups.google.com/forum/#!forum/mongodb-user

    A forum for technical questions about using MongoDB.

  https://groups.google.com/forum/#!forum/mongodb-dev

    A forum for technical questions about building and developing MongoDB.

LEARN MONGODB

  https://university.mongodb.com/

LICENSE

  MongoDB is free and open-source. Versions released prior to October 16,
  2018 are published under the AGPL. All versions released after October
  16, 2018, including patch fixes for prior versions, are published under
  the Server Side Public License (SSPL) v1. See individual files for
  details.

