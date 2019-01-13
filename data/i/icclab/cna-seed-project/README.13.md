

========================================================
 This pattern is downloaded from www.subtlepatterns.com 
 If you need more, that's where to get'em.
 ========================================================
 
 

========================================================
 This pattern is downloaded from www.subtlepatterns.com 
 If you need more, that's where to get'em.
 ========================================================
 
 

========================================================
 This pattern is downloaded from www.subtlepatterns.com 
 If you need more, that's where to get'em.
 ========================================================
 
 

========================================================
 This pattern is downloaded from www.subtlepatterns.com 
 If you need more, that's where to get'em.
 ========================================================
 
 

========================================================
 This pattern is downloaded from www.subtlepatterns.com 
 If you need more, that's where to get'em.
 ========================================================
 
 

========================================================
 This pattern is downloaded from www.subtlepatterns.com 
 If you need more, that's where to get'em.
 ========================================================
 
 

========================================================
 This pattern is downloaded from www.subtlepatterns.com 
 If you need more, that's where to get'em.
 ========================================================
 
 

========================================================
 This pattern is downloaded from www.subtlepatterns.com 
 If you need more, that's where to get'em.
 ========================================================
 
 

========================================================
 This pattern is downloaded from www.subtlepatterns.com 
 If you need more, that's where to get'em.
 ========================================================
 
 

========================================================
 This pattern is downloaded from www.subtlepatterns.com 
 If you need more, that's where to get'em.
 ========================================================
 
 

========================================================
 This pattern is downloaded from www.subtlepatterns.com 
 If you need more, that's where to get'em.
 ========================================================
 
 

========================================================
 This pattern is downloaded from www.subtlepatterns.com 
 If you need more, that's where to get'em.
 ========================================================
 
 

========================================================
 This pattern is downloaded from www.subtlepatterns.com 
 If you need more, that's where to get'em.
 ========================================================
 
 

========================================================
 This pattern is downloaded from www.subtlepatterns.com 
 If you need more, that's where to get'em.
 ========================================================
 
 

========================================================
 This pattern is downloaded from www.subtlepatterns.com 
 If you need more, that's where to get'em.
 ========================================================
 
 

========================================================
 This pattern is downloaded from www.subtlepatterns.com 
 If you need more, that's where to get'em.
 ========================================================
 
 

========================================================
 This pattern is downloaded from www.subtlepatterns.com 
 If you need more, that's where to get'em.
 ========================================================
 
 In order to use the user-extensions.js with selinium through command line, you will have to use the following Syntax:

Java -jar selenium-server-standalone-2.7.0.jar -htmlSuite *firefox http://localhost/zurmo/app/ inputTestSuiteFilePath outputTestSuiteResult -userExtensions pathToTheUserExtensionJS

Default Location: app/protected/tests/functional/assets/extensions/user-extensions.js

Purpose: So as to enable the use of global variables in the entire TestSuite.### Zurmo application container
This container is a data only container and offers the zurmo application files (PHP).

#### Volumes
This is the volume which contains all the php files for zurmo:

```
/zurmo
```

#### Add volumes of this container in your container
Basic usage:

```
docker create --name zurmo_application icclabcna/zurmo_application
docker run --volumes-from zurmo_application your_container
```

Typical usage:  
The typical usage is using the zurmo_apache and the zurmo_config container together with this zurmo_application container

```
docker create --name zurmo_application icclabcna/zurmo_application
docker run --name zurmo_apache -p 80:80 --volumes-from zurmo_application --volumes-from zurmo_config icclabcna/zurmo_apache /apache-run.sh
```**Zurmo Open Source CRM**

Zurmo is an open source CRM  application written in PHP utilizing jQuery, Yii Framework, and RedBeanPHP.

Our goal with Zurmo is to provide  an easy-to-use, easy-to-customize CRM application that can be adapted
to any  business use case. 
We have taken special care to think through many different use cases and have
designed a system that we believe provides a high degree of flexibility, covering a wide variety of use
cases out of the box.

We don't have a million features. We can never beat out existing players in a feature war.

But considering companies wind up only using a handful of features, we don't think it really  matters.

What we have so far is the beginning of a high-quality sales force  automation tool.
Stay tuned as we continue to make improvements.

From a technical perspective, we  are very excited. We have decided to build Zurmo on three awesome
development  frameworks, Yii, RedBeanPHP, and jQuery.
With almost a religious zeal for  testing,
you will find that our obsession with test driven development means a  more stable application.

Gone are the days of 'upgrade and pray'. Now it is  'upgrade and test'.

We have installation walkthroughs based on different development  platforms.

[Windows  Installation Instructions for Development using Apache] [wi]
[wi]: http://zurmo.org/wiki/windows-installation-instructions-for-development

[Linux  Installation Instructions for Development] [li]
[li]: http://zurmo.org/wiki/linux-installation-instructions-for-development
 
For support please visit and register for our [forum] [fp] pages.
[fp]: http://zurmo.org/forums/

WideImage, a PHP image manipulation library
Copyright 2007-2011 Gasper Kozak

For documentation, please visit http://wideimage.sourceforge.net/


    This file is part of WideImage.
		
    WideImage is free software; you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation; either version 2.1 of the License, or
    (at your option) any later version.
		
    WideImage is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.
		
    You should have received a copy of the GNU Lesser General Public License
    along with WideImage; if not, write to the Free Software
    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
Swift Mailer, by Chris Corbyn
-----------------------------

Swift Mailer is a component based mailing solution for PHP 5.
It is released under the LGPL license.

Homepage:      http://swiftmailer.org
Documentation: http://swiftmailer.org/docs
Mailing List:  http://groups.google.com/group/swiftmailer
Bugs:          https://github.com/swiftmailer/swiftmailer/issues
Repository:    https://github.com/swiftmailer/swiftmailer

Swift Mailer is highly object-oriented by design and lends itself
to use in complex web application with a great deal of flexibility.

For full details on usage, see the documentation.

IMPORTANT: Users upgrading from version 3.x or earlier absolutely
           MUST read the documentation.  In short, the API is considerably
           different so your old code won't "just work".

If you'd like to make a donation, we are working on a system where
donations are taken on a per-feature-request basis via the website
with target amounts for each feature. In the meantime however you
may donate directly to the author via PayPal:

  PayPal: chris@w3style.co.uk

Donations are certainly voluntary, but seriously, you donors are
complete legends and drive this project! :)
Yii Web Programming Framework
=============================

Thank you for choosing Yii - a high-performance component-based PHP framework.


INSTALLATION
------------

Please make sure the release file is unpacked under a Web-accessible
directory. You shall see the following files and directories:

      demos/               demos
      framework/           framework source files
      requirements/        requirement checker
      CHANGELOG            describing changes in every Yii release
      LICENSE              license of Yii
      README               this file
      UPGRADE              upgrading instructions


REQUIREMENTS
------------

The minimum requirement by Yii is that your Web server supports
PHP 5.1.0 or above. Yii has been tested with Apache HTTP server
on Windows and Linux operating systems.

Please access the following URL to check if your Web server reaches
the requirements by Yii, assuming "YiiPath" is where Yii is installed:

      http://hostname/YiiPath/requirements/index.php


QUICK START
-----------

Yii comes with a command line tool called "yiic" that can create
a skeleton Yii application for you to start with.

On command line, type in the following commands:

        $ cd YiiPath/framework                (Linux)
        cd YiiPath\framework                  (Windows)

        $ ./yiic webapp ../testdrive          (Linux)
        yiic webapp ..\testdrive              (Windows)

The new Yii application will be created at "YiiPath/testdrive".
You can access it with the following URL:

        http://hostname/YiiPath/testdrive/index.php


WHAT's NEXT
-----------

Please visit the project website for tutorials, class reference
and join discussions with other Yii users.



The Yii Developer Team
http://www.yiiframework.com

                CLDR v1.6 (July 2, 2008)

This directory contains the CLDR data files in form of PHP scripts.
They are obtained by extracting the CLDR data (http://www.unicode.org/cldr/)
with the script "tools/cldr/build.php".

Only the data relevant to date and number formatting are extracted.
Each PHP file contains an array representing the data for a particular
locale. Data inherited from parent locales are also in the array.
<html>
<head>
<title>Third-Party Library List</title>
</head>

<body>
<h1>Third-Party Library List</h1>
<p>
This folder includes third-party libraries that are used by the Yii framework.
<em>All these libraries are using licenses that are compatible to the BSD license used by Yii.</em>
This means you can safely use Yii for whatever purpose, provided you comply to the BSD license.
Please refer to the detailed license information as shown below:
</p>
<table border="1">
<tr>
  <th>Library Name</th>
  <th>License</th>
  <th>Related Yii Component</th>
</tr>

<tr>
  <td><a href="http://jquery.com">jQuery 1.8.3</a></td>
  <td><a href="jquery/LICENSE.txt">MIT</a></td>
  <td>most JavaScript-related functionalities</td>
</tr>
<tr>
  <td><a href="http://www.jqueryui.com">jQuery UI 1.9.2</a></td>
  <td><a href="jqueryui/MIT-LICENSE.txt">MIT</a></td>
  <td>the widgets under zii/widgets/jui</td>
</tr>
<tr>
  <td><a href="http://benalman.com/projects/jquery-bbq-plugin/">jQuery BBQ Plugin 1.2.1</a></td>
  <td><a href="bbq/LICENSE.txt">MIT</a></td>
  <td><a href="http://www.yiiframework.com/doc/api/1.1/CGridView">CGridView</a> and <a href="http://www.yiiframework.com/doc/api/1.1/CListView">CListView</a> widgets</td>
</tr>
<tr>
  <td><a href="http://bassistance.de/jquery-plugins/jquery-plugin-autocomplete/">jQuery Autocomplete 1.1.0</a></td>
  <td><a href="jquery/autocomplete/LICENSE.txt">MIT</a></td>
  <td>CHtml::autoComplete()</td>
</tr>
<tr>
  <td><a href="http://digitalbush.com/projects/masked-input-plugin">jQuery Masked Input 1.3</a></td>
  <td><a href="jquery/maskedinput/LICENSE.txt">MIT</a></td>
  <td><a href="http://www.yiiframework.com/doc/api/1.1/CMaskedTextField">CMaskedTextField</a></td>
</tr>
<tr>
  <td><a href="http://www.fyneworks.com/jquery/multiple-file-upload/">jQuery Multi File Upload 1.47</a></td>
  <td><a href="http://www.fyneworks.com/jquery/multiple-file-upload/#tab-License">MIT</a></td>
  <td><a href="http://www.yiiframework.com/doc/api/1.1/CMultiFileUpload">CMultiFileUpload</a></td>
</tr>
<tr>
  <td><a href="http://bassistance.de/jquery-plugins/jquery-plugin-treeview/">jQuery TreeView 1.4.1</a></td>
  <td><a href="jquery/autocomplete/LICENSE.txt">MIT</a></td>
  <td><a href="http://www.yiiframework.com/doc/api/1.1/CTreeView">CTreeView</a></td>
</tr>
<tr>
  <td><a href="http://www.fyneworks.com/jquery/star-rating/">jQuery Star Rating 3.13</a></td>
  <td><a href="http://www.opensource.org/licenses/mit-license.php">MIT</a></td>
  <td><a href="http://www.yiiframework.com/doc/api/1.1/CStarRating">CStarRating</a></td>
</tr>
<tr>
  <td><a href="http://pear.php.net/pepr/pepr-proposal-show.php?id=198">PEAR JSON</a></td>
  <td><a href="json/LICENSE.txt">BSD</a></td>
  <td><a href="http://www.yiiframework.com/doc/api/1.1/CJSON">CJSON</a>, <a href="http://www.yiiframework.com/doc/api/1.1/CJavaScript">CJavaScript</a></td>
</tr>
<tr>
  <td><a href="http://www.unicode.org/cldr/">Unicode CLDR Data 1.6</a></td>
  <td><a href="cldr/LICENSE.txt">Unicode</a></td>
  <td>I18N-related functionalities</td>
</tr>
<tr>
  <td><a href="http://phplens.com/phpeverywhere/">ADOdb Date Library</a></td>
  <td><a href="adodb/LICENSE.txt">BSD</a></td>
  <td><a href="http://www.yiiframework.com/doc/api/1.1/CTimestamp">CTimestamp</a></td>
</tr>
<tr>
  <td><a href="http://pear.php.net/package/Text_Highlighter/">Text_Highlighter - Generic Syntax Highlighter</a> (v0.7.0 beta)</td>
  <td><a href="http://www.php.net/license/3_01.txt">The PHP License</a></td>
  <td><a href="http://www.yiiframework.com/doc/api/1.1/CTextHighlighter">CTextHighlighter</a> (note: many PHP files are modified to make them workable in PHP 5 strict mode and their PEAR dependency are also removed.) </td>
</tr>
<tr>
  <td><a href="http://pear.php.net/package/File_Gettext/">PEAR Gettext</a> (v0.4.1 beta)</td>
  <td><a href="gettext/LICENSE.txt">The PHP License</a></td>
  <td><a href="http://www.yiiframework.com/doc/api/1.1/CGettextMoFile">CGettextMoFile</a></td>
</tr>
<tr>
  <td><a href="http://htmlpurifier.org/">HTML Purifier</a> (v4.4.0)</td>
  <td><a href="htmlpurifier/LICENSE.txt">LGPL</a></td>
  <td><a href="http://www.yiiframework.com/doc/api/1.1/CHtmlPurifier">CHtmlPurifier</a></td>
</tr>
<tr>
  <td><a href="http://michelf.com/projects/php-markdown/">PHP Markdown Extra</a> (v1.2.5)</td>
  <td><a href="markdown/LICENSE.txt">BSD</a></td>
  <td><a href="http://www.yiiframework.com/doc/api/1.1/CMarkdown">CMarkdown</a></td>
</tr>
<tr>
  <td><a href="https://github.com/balupton/history.js/">History.js</a> (v1.7.1) - October 4 2011</td>
  <td><a href="history/license.txt">BSD</a></td>
  <td><a href="http://www.yiiframework.com/doc/api/1.1/CGridView">CGridView</a>, <a href="http://www.yiiframework.com/doc/api/1.1/CGridView">CListView</a></td>
</tr>
<tr>
  <td><a href="http://phlymail.com/en/downloads/idna-convert.html">Net_IDNA - IDNA Converter in PHP</a> (Version 0.8.0 from 2011-03-11)</td>
  <td><a href="idna_convert/LICENCE">LGPL</a></td>
  <td><a href="http://www.yiiframework.com/doc/api/1.1/CUrlValidator">CUrlValidator</a>, <a href="http://www.yiiframework.com/doc/api/1.1/CEmailValidator">CEmailValidator</a></td>
</tr>
<tr>
  <td><a href="https://github.com/bestiejs/punycode.js">Punycode.js</a> (v1.1.1) - June 27 2012</td>
  <td><a href="punycode/LICENSE-MIT.txt">MIT</a>, <a href="punycode/LICENSE-GPL.txt">GPL</a></td>
  <td><a href="http://www.yiiframework.com/doc/api/1.1/CUrlValidator">CUrlValidator</a>, <a href="http://www.yiiframework.com/doc/api/1.1/CEmailValidator">CEmailValidator</a></td>
</tr>
</table>

</body>
</html>
# $Id: README,v 1.2 2007/06/13 10:09:47 ssttoo Exp $

Introduction
============

Text_Highlighter is a class for syntax highlighting. The main idea is to
simplify creation of subclasses implementing syntax highlighting for
particular language. Subclasses do not implement any new functioanality, they
just provide syntax highlighting rules. The rules sources are in XML format.
To create a highlighter for a language, there is no need to code a new class
manually. Simply describe the rules in XML file and use Text_Highlighter_Generator
to create a new class.


This document does not contain a formal description of API - it is very
simple, and I believe providing some examples of code is sufficient.


Highlighter XML source
======================

Basics
------

Creating a new syntax highlighter begins with describing the highlighting
rules. There are two basic elements: block and region. A block is just a
portion of text matching a regular expression and highlighted with a single
color. Keyword is an example of a block. A region is defined by two regular
expressions: one for start of region, and another for the end. The main
difference from a block is that a region can contain blocks and regions
(including same-named regions). An example of a region is a group of
statements enclosed in curly brackets (this is used in many languages, for
example PHP and C). Also, characters matching start and end of a region may be
highlighted with their own color, and region contents with another.

Blocks and regions may be declared as contained. Contained blocks and regions
can only appear inside regions. If a region or a block is not declared as
contained, it can appear both on top level and inside regions. Block or region
declared as not-contained can only appear on top level.

For any region, a list of blocks and regions that can appear inside this
region can be specified.

In this document, the term "color group" is used. Chunks of text assigned to
same color group will be highlighted with same color. Note that in versions
prior 0.5.0 color goups were refered as CSS classes, but since 0.5.0 not only
HTML output is supported, so "color group" is more appropriate term.

Elements
--------

The toplevel element is <highlight>. Attribute lang is required and denotes
the name of the language. Its value is used as a part of generated class name,
and must only contain letters, digits and underscores. Optional attribute
case, when given value yes, makes the language case sensitive (default is case
insensitive). Allowed subelements are:

    * <authors>: Information about the authors of the file.
        <author>: Information about a single author of the file. (May be used
        multiple times, one per author.)
                - name="...": Author's name. Required.
                - email="...": Author's email address. Optional.

    * <default>: Default color group.
          - innerGroup="...": color group name. Required.
    
    * <region>: Region definition
          - name="...": Region name. Required.
          - innerGroup="...": Default color group of region contents. Required.
          - delimGroup="...": color group of start and end of region. Optional,
            defaults to value of innerGroup attribute.
          - start="...", end="...": Regular expression matching start and end
            of region. Required. Regular expression delimiters are optional, but
            if you need to specify delimiter, use /. The only case when the
            delimiters are needed, is specifying regular expression modifiers,
            such as m or U. Examples: \/\* or /$/m.
          - contained="yes": Marks region as contained.
          - never-contained="yes": Marks region as not-contained.
          - <contains>: Elements allowed inside this region.
                - all="yes" Region can contain any other region or block
                (except not-contained). May be used multiple times.
                      - <but> Do not allow certain regions or blocks.
                            - region="..." Name of region not allowed within
                              current region.
                            - block="..." Name of block not allowed within
                              current region.
                - region="..." Name of region allowed within current region.
                - block="..." Name of block allowed within current region.
          - <onlyin> Only allow this region within certain regions. May be
            used multiple times.
                - block="..." Name of parent region
    
    * <block>: Block definition
          - name="...": Block name. Required.
          - innerGroup="...": color group of block contents. Optional. If not
            specified, color group of parent region or default color group will be
            used. One would only want to omit this attribute if there are
            keyword groups (see below) inherited from this block, and no special
            highlighting should apply when the block does not match the keyword.
          - match="..." Regular expression matching the block. Required.
            Regular expression delimiters are optional, but if you need to
            specify delimiter, use /. The only case when the delimiters are
            needed, is specifying regular expression modifiers, such as m or U.
            Examples: #|\/\/ or /$/m.
          - contained="yes": Marks block as contained.
          - never-contained="yes": Marks block as not-contained.
          - <onlyin> Only allow this block within certain regions. May be used
              multiple times.
                - block="..." Name of parent region
          - multiline="yes": Marks block as multi-line. By default, whole
            blocks are assumed to reside in a single line. This make the things
            faster. If you need to declare a multi-line block, use this
            attribute.
          - <partgroup>: Assigns another color group to a part of the block that
              matched a subpattern.
                - index="n": Subpattern index. Required.
                - innerGroup="...": color group name. Required.

              This is an example from CSS highlighter: the measure is matched as
              a whole, but the measurement units are highlighted with different
              color.

                <block name="measure"  match="\d*\.?\d+(\%|em|ex|pc|pt|px|in|mm|cm)"
                        innerGroup="number" contained="yes">
                    <onlyin region="property"/>
                    <partGroup index="1" innerGroup="string" />
                </block>
  
    * <keywords>: Keyword group definition. Keyword groups are useful when you
      want to highlight some words that match a condition for a block with a
      different color. Keywords are defined with literal match, not regular
      expressions. For example, you have a block named identifier matching a
      general identifier, and want to highlight reserved words (which match
      this block as well) with different color. You inherit a keyword group
      "reserved" from "identifier" block.
          - name="...": Keyword group. Required.
          - ifdef="...", ifndef="..." : Conditional declaration. See
            "Conditions" below.
          - inherits="...": Inherited block name. Required.
          - innerGroup="...": color group of keyword group. Required.
          - case="yes|no": Overrides case-sensitivity of the language.
            Optional, defaults to global value.
          - <keyword>: Single keyword definition.
                - match="..." The keyword. Note: this is not a regular
                  expression, but literal match (possibly case insensitive).

Note that for BC reasons element partClass is alias for partGroup, and
attributes innerClass and  delimClass  are aliases of innerGroup and
delimGroup, respectively.
    

Conditions
----------

Conditional declarations allow enabling or disabling certain highlighting
rules at runtime. For example, Java highlighter has a very big list of
keywords matching Java standard classes. Finding a match in this list can take
much time. For that reason, corresponding keyword group is declared with
"ifdef" attribute :

  <keywords name="builtin" inherits="identifier" innerClass="builtin" 
            case="yes" ifdef="java.builtins">
	<keyword match="AbstractAction" />
	<keyword match="AbstractBorder" />
	<keyword match="AbstractButton" />
    ...
    ...
	<keyword match="_Remote_Stub" />
	<keyword match="_ServantActivatorStub" />
	<keyword match="_ServantLocatorStub" />
  </keywords>

This keyword group will be only enabled when "java.builtins" is passed as an
element of "defines" option:

    $options = array(
        'defines' => array(
            'java.builtins',
        ),
        'numbers' => HL_NUMBERS_TABLE,
    );
    $highlighter =& Text_Highlighter::factory('java', $options);

"ifndef" attribute has reverse meaning.

Currently, "ifdef" and "ifndef" attributes are only supported for <keywords>
tag. 



Class generation
================

Creating XML description of highlighting rules is the most complicated part of
the process. To generate the class, you need just few lines of code:

    <?php
    require_once 'Text/Highlighter/Generator.php';
    $generator =& new Text_Highlighter_Generator('php.xml');
    $generator->generate();
    $generator->saveCode('PHP.php');
    ?>



Command-line class generation tool
==================================

Example from previous section looks pretty simple, but it does not handle any
errors which may occur during parsing of XML source. The package provides a
command-line script to make generation of classes even more simple, and takes
care of possible errors. It is called generate (on Unix/Linux) or generate.bat
(on Windows). This script is able to process multiple files in one run, and
also to process XML from standard input and write generated code to standard
output.

    Usage:
    generate options

    Options:
      -x filename, --xml=filename
            source XML file. Multiple input files can be specified, in which
            case each -x option must be followed by -p unless -d is specified
            Defaults to stdin
      -p filename, --php=filename
            destination PHP file. Defaults to stdout. If specied multiple times,
            each -p must follow -x
      -d dirname, --dir=dirname
            Default destination directory. File names will be taken from XML input
            ("lang" attribute of <highlight> tag)
      -h, --help
            This help

Examples

    Read from php.xml, write to PHP.php

        generate -x php.xml -p PHP.php

    Read from php.xml, write to standard output

        generate -x php.xml

    Read from php.xml, write to PHP.php, read from xml.xml, write to XML.php

        generate -x php.xml -p PHP.php -x xml.xml -p XML.php

    Read from php.xml, write to /some/dir/PHP.php, read from xml.xml, write to
    /some/dir/XML.php (assuming that xml.xml contains <highlight lang="xml">, and
    php.xml contains <highlight lang="php">)

        generate -x php.xml -x xml.xml -d /some/dir/



Renderers
=========

Introduction
------------

Text_Highlighter supports renderes. Using renderers, you can get output in
different formats. Two renderers are included in the package:

    - HTML renderer. Generates HTML output. A style sheet should be linked to
      the document to display colored text

    - Console renderer. Can be used to output highlighted text to
      color-capable terminals, either directly or trough less -r


Renderers API
-------------

Renderers are subclasses of Text_Highlighter_Renderer. Renderer should
override at least two methods - acceptToken and getOutput. Overriding other
methods is optional, depending on the nature of renderer's output and details
of implementation.

    string reset()
        resets renderer state. This method is called every time before a new
        source file is highlighted.

    string preprocess(string $code)
        preprocesses code. Can be used, for example, to normalize whitespace
        before highlighting. Returns preprocessed string.

    void acceptToken(string $group, string $content)
        the core method of the renderer. Highlighter passes chunks of text to
        this method in $content, and color group in $group

    void finalize()
        signals the renderer that no more tokens are available.

    mixed getOutput()
        returns generated output.


Setting renderer options
--------------------------------

Renderers accept an optional argument to their constructor  - options array.
Elements of this array are renderer-specific.

HTML renderer
-------------

HTML renderer produces HTML output with optional line numbering. The renderer
itself does not provide information about actual colors of highlighted text.
Instead, <span class="hl-XXX"> is used, where XXX is replaced with color group
name (hl-var, hl-string, etc.). It is up to you to create a CSS stylesheet.
If 'use_language' option with value evaluating to true was passed, class names
will be formatted as "LANG-hl-XXX", where LANG is language name as defined in
highlighter XML source ("lang" attribute of <highlight> tag) in lower case.

There are 3 special CSS classes:

    hl-main - this class applies to whole output or right table column,
              depending on 'numbers' option
    hl-gutter - applies to left column in table
    hl-table - applies to whole table

HTML renderer accepts following options (each being optional):
    
    * numbers - line numbering style.
        0 - no numbering (default)
        HL_NUMBERS_LI - use <ol></ol> for line numbering
        HL_NUMBERS_TABLE  - create a 2-column table, with line numbers in left
                            column and highlighted text in right column

    * tabsize - tabulation size. Defaults to 4

    Example:
        
        require_once 'Text/Highlighter/Renderer/Html.php';
        $options = array(
            'numbers' => HL_NUMBERS_LI,
            'tabsize' => 8,
        );
        $renderer =& new Text_Highlighter_Renderer_HTML($options);

Console renderer
----------------

Console renderer produces output for displaying on a color-capable terminal,
either directly or through less -r, using ANSI escape sequences. By default,
this renderer only highlights most common color groups. Additional colors
can be specified using 'colors' option. This renderer also accepts 'numbers'
option - a boolean value, and 'tabsize' option.

    Example :

        require_once 'Text/Highlighter/Renderer/Console.php';
        $colors = array(
            'prepro' => "\033[35m",
            'types' => "\033[32m",
        );
        $options = array(
            'numbers' => true,
            'tabsize' => 8,
            'colors' => $colors,
        );
        $renderer =& new Text_Highlighter_Renderer_Console($options);


ANSI color escape sequences have the following format:

    ESC[#;#;....;#m

where ESC is character with ASCII code 27 (033 octal, 0x1B hexadecimal). # is
one of the following:

        0 for normal display
        1 for bold on
        4 underline (mono only)
        5 blink on
        7 reverse video on
        8 nondisplayed (invisible)
        30 black foreground
        31 red foreground
        32 green foreground
        33 yellow foreground
        34 blue foreground
        35 magenta foreground
        36 cyan foreground
        37 white foreground
        40 black background
        41 red background
        42 green background
        43 yellow background
        44 blue background
        45 magenta background
        46 cyan background
        47 white background


How to use Text_Highlighter class
=================================

Creating a highlighter object
-----------------------------

To create a highlighter for a certain language, use Text_Highlighter::factory()
static method:

    require_once 'Text/Highlighter.php';
    $hl =& Text_Highlighter::factory('php');


Setting a renderer
------------------

Actual output is produced by a renderer.

    require_once 'Text/Highlighter.php';
    require_once 'Text/Highlighter/Renderer/Html.php';
    $options = array(
        'numbers' => HL_NUMBERS_LI,
        'tabsize' => 8,
    );
    $renderer =& new Text_Highlighter_Renderer_HTML($options);
    $hl =& Text_Highlighter::factory('php');
    $hl->setRenderer($renderer);

Note that for BC reasons, it is possible to use highlighter without setting a
renderer. If no renderer is set, HTML renderer will be used by default. In
this case, you should pass options as second parameter to factory method. The
following example works exactly as previous one:

    require_once 'Text/Highlighter.php';
    $options = array(
        'numbers' => HL_NUMBERS_LI,
        'tabsize' => 8,
    );
    $hl =& Text_Highlighter::factory('php', $options);


Getting output
--------------

And finally, do the highlighting and get the output:

    require_once 'Text/Highlighter.php';
    require_once 'Text/Highlighter/Renderer/Html.php';
    $options = array(
        'numbers' => HL_NUMBERS_LI,
        'tabsize' => 8,
    );
    $renderer =& new Text_Highlighter_Renderer_HTML($options);
    $hl =& Text_Highlighter::factory('php');
    $hl->setRenderer($renderer);
    $html = $hl->highlight(file_get_contents('example.php'));

# vim: set autoindent tabstop=4 shiftwidth=4 softtabstop=4 tw=78: */

