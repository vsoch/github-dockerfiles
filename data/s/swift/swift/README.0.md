<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE book PUBLIC "-//OASIS//DTD DocBook XML V4.5//EN"
"http://www.oasis-open.org/docbook/xml/4.5/docbookx.dtd">
<book>
  <title>README: Web-based Help from DocBook XML</title>

  <bookinfo>
    <legalnotice>
      <para>Permission is hereby granted, free of charge, to any person
      obtaining a copy of this software and associated documentation files
      (the <quote>Software</quote>), to deal in the Software without
      restriction, including without limitation the rights to use, copy,
      modify, merge, publish, distribute, sublicense, and/or sell copies of
      the Software, and to permit persons to whom the Software is furnished to
      do so, subject to the following conditions: <itemizedlist>
          <listitem>
            <para>The above copyright notice and this permission notice shall
            be included in all copies or substantial portions of the
            Software.</para>
          </listitem>

          <listitem>
            <para>Except as contained in this notice, the names of individuals
            credited with contribution to this software shall not be used in
            advertising or otherwise to promote the sale, use or other
            dealings in this Software without prior written authorization from
            the individuals in question.</para>
          </listitem>

          <listitem>
            <para>Any stylesheet derived from this Software that is publicly
            distributed will be identified with a different name and the
            version strings in any derived Software will be changed so that no
            possibility of confusion between the derived package and this
            Software will exist.</para>
          </listitem>
        </itemizedlist></para>

      <formalpara>
        <title>Warranty:</title>

        <para>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
        EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
        MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
        IN NO EVENT SHALL DAVID CRAMER, KASUN GAJASINGHE, OR ANY OTHER CONTRIBUTOR BE LIABLE FOR
        ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
        CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.</para>
      </formalpara>

      <para>This package is maintained by Kasun Gajasinghe, <email>kasunbg AT
      gmail DOT com</email> and David Cramer, <email>david AT thingbag DOT
      net</email>.</para>

      <para>This package also includes the following software written and
      copyrighted by others:<itemizedlist>
          <listitem>
            <para>Files in <filename
            class="directory">template/common/jquery</filename> are
            copyrighted by <ulink url="http://jquery.com/">JQuery</ulink>
            under the MIT License. The file
            <filename>jquery.cookie.js</filename> Copyright (c) 2006 Klaus
            Hartl under the MIT license.</para>

            <indexterm>
              <primary>jquery</primary>
            </indexterm>
          </listitem>

          <listitem>
            <para>Some files in the <filename
            class="directory">template/content/search</filename> and <filename
            class="directory">indexer</filename> directories were originally
            part of N. Quaine's htmlsearch DITA plugin. The htmlsearch DITA
            plugin is available from the <ulink
            url="http://tech.groups.yahoo.com/group/dita-users/files/Demos/">files
            page</ulink> of the DITA-users yahoogroup. The htmlsearch plugin
            was released under a BSD-style license. See
            <filename>indexer/license.txt</filename> for details. <indexterm>
                <primary>htmlsearch</primary>
              </indexterm> <indexterm>
                <primary>DITA</primary>

                <secondary>htmlsearch plugin</secondary>
              </indexterm></para>
          </listitem>

          <listitem>
            <para>Stemmers from the <ulink
            url="http://snowball.tartarus.org/texts/stemmersoverview.html">Snowball
            project</ulink> released under a BSD license.</para>
          </listitem>

          <listitem>
            <para>Code from the <ulink url="http://lucene.apache.org/">Apache
            Lucene</ulink> search engine provides support for tokenizing
            Chinese, Japanese, and Korean content released under the Apache
            2.0 license. </para>
          </listitem>
        </itemizedlist>
		Webhelp for DocBook was developed as a <ulink url="http://socghop.appspot.com">Google Summer of Code</ulink> project. 
	  </para>
    </legalnotice>

    <copyright>
      <year>2008-2010</year>

      <holder>Kasun Gajasinghe</holder>

      <holder>David Cramer</holder>
    </copyright>

    <author>
      <firstname>David</firstname>

      <surname>Cramer</surname>

      <email>dcramer AT motive DOT com</email>

      <email>david AT thingbag DOT net</email>
    </author>

    <author>
      <firstname>Kasun</firstname>

      <surname>Gajasinghe</surname>

      <email>kasunbg AT gmail DOT com</email>
    </author>

    <pubdate>August 2010</pubdate>
  </bookinfo>

  <chapter>
    <chapterinfo>
      <abstract>
        <!-- This becomes the brief description that appears in search results UNLESS there's a para or phrase with role="summary". If there is, then the role="summary" text wins. -->

        <para>Overview of the package.</para>
      </abstract>
    </chapterinfo>

    <title>Introduction</title>

    <para>A common requirement for technical publications groups is to produce a Web-based help
      format that includes a table of contents pane, a search feature, and an index similar to what
      you get from the Microsoft HTML Help (.chm) format or Eclipse help. If the content is help for
      a Web application that is not exposed to the Internet or requires that the user be logged in,
      then it is impossible to use services like Google to add search. <indexterm class="singular">
        <primary>features</primary>
      </indexterm>
      <itemizedlist>
        <title>Features</title>
        <listitem>
          <para>Full text search.<indexterm class="singular">
              <primary>search</primary>
              <secondary>features</secondary>
            </indexterm></para>
          <itemizedlist>
            <listitem>
              <para>Stemming support for English, French, and German. Stemming support can be added
                for other languages by implementing a stemmer.<indexterm class="singular">
                  <primary>search</primary>
                  <secondary>stemming</secondary>
                </indexterm></para>
            </listitem>
            <listitem>
              <para>Support for Chinese, Japanese, and Korean using code from the Lucene search
                engine. </para>
            </listitem>
            <listitem>
              <para>Search highlighting shows where the searched for term appears in the results.
                Use the <guibutton>H</guibutton> button to toggle the highlighting off and on.
                  <indexterm class="singular">
                  <primary>search</primary>
                  <secondary>highlighting</secondary>
                </indexterm></para>
            </listitem>
            <listitem>
              <para>Search results can include brief descriptions of the target.<indexterm
                  class="singular">
                  <primary>search</primary>
                  <secondary>descriptions</secondary>
                </indexterm></para>
            </listitem>
          </itemizedlist>
        </listitem>
        <listitem>
          <para>Table of contents pane with collapsible toc tree.</para>
        </listitem>
        <listitem>
          <para>Auto-synchronization of content pane and TOC.</para>
        </listitem>
        <listitem>
          <para>TOC and search pane implemented without the use of a frameset.</para>
        </listitem>
        <listitem>
          <para>An Ant <filename>build.xml</filename> file to generate output. You can use this
            build file by importing it into your own or use it as a model for integrating this
            output format into your own build system.</para>
        </listitem>
      </itemizedlist>
      <itemizedlist>
        <title>Possible future enhancements</title>
        <listitem>
          <para>Move webhelp-specific parameters and gentext strings into base DocBook stylesheets.
          </para>
        </listitem>
        <listitem>
          <para>Use <sgmltag class="attribute">tabindex</sgmltag> attributes to control the tab
            order in the output. The Contents and Search tabs should be first and second, then the
            search box and button, then the table of contents items, and so on.</para>
        </listitem>
        <listitem>
          <para>Add "Expand all" and "Collapse all" buttons to the table of contents.</para>
        </listitem>
        <listitem>
          <para>Add other search options:</para>
          <itemizedlist>
            <listitem>
              <para>Add an option to use Lucene for server-side searches with table of contents
                state persisted on the server.</para>
            </listitem>
            <listitem>
              <para>Add a simple form that uses a Google site:my.domain.com based search.</para>
            </listitem>
          </itemizedlist>
        </listitem>
        <listitem>
          <para>Sort search results based on relevance</para>
        </listitem>
        <listitem>
          <para>Support wild card characters in the search query.</para>
        </listitem>
        <listitem>
          <para>Parameterize width of the TOC pane OR make the TOC pane resizeable by the
            user.</para>
        </listitem>
        <listitem>
          <para>Automate search results summary text:</para>
          <itemizedlist>
            <listitem>
              <para>Automatically use the first non-heading content as the summary in the search
                results.</para>
            </listitem>
            <listitem>
              <para>Automatically limit the size of the search description to something 140
                characters.</para>
            </listitem>
          </itemizedlist>
        </listitem>
        <listitem>
          <para>Support boolean operators in search.</para>
        </listitem>
        <listitem>
          <para>Parameterize list of files to exclude from indexing. Currently it's hard coded that
            we don't index <filename>index.html </filename>and <filename>ix01.html</filename> (the
            legal notice and index topics). It should be smarter and automatically not index the
            index file even if it's not named <filename>ix01.html</filename>.</para>
        </listitem>
        <listitem>
          <para>Improve performance by moving the table of contents div out of each page and into a
            separate JavaScript file which then adds it to the page.</para>
        </listitem>
        <listitem>
          <para>Add to the indexer the ability to specify a list of files or file patterns not to
            index. Currently it does not index <filename>index.html</filename> or
              <filename>ix01.html</filename>, which is generally appropriate, but it should be up to
            the user to decide.</para>
        </listitem>
        <listitem>
          <para>Add an index tab populated by a separate JavaScript file. Include a param/property
            that allows the content creator to disable the index.</para>
        </listitem>
        <listitem>
          <para>Add functionality to the <filename>build.xml</filename> file so that when a property
            is set, the build generates a pdf version of the document and includes a link to it from
            the header.</para>
        </listitem>
        <listitem>
          <para>Add <ulink
              url="http://www.comparenetworks.com/developers/jqueryplugins/jbreadcrumb.html"
              >breadcrumbs</ulink> so the user will know what topics he's been to.</para>
        </listitem>
        <listitem>
          <para>Consider using more advanced Lucene indexers for Chinese and Japanese than the
            CJKAnalyzer</para>
        </listitem>
      </itemizedlist></para>
  </chapter>

  <chapter>
    <title>Using the package</title>

    <para role="summary">The following sections describe how to install and
    use the package on Windows.</para>

    <section>
      <sectioninfo>
        <abstract>
          <para>Installation instructions</para>
        </abstract>
      </sectioninfo>

      <title>Generating webhelp output</title>

      <procedure>
        <title>To install the package on Windows</title>

        <note>
          <para>The examples in this procedure assume a Windows installation,
          but the process is the same in other environments,
          <foreignphrase>mutatis mutandis</foreignphrase>.</para>
        </note>

        <step>
          <para>If necessary, install <ulink
          url="http://www.java.com/en/download/manual.jsp">Java 1.6</ulink> or
          higher.</para>

          <substeps>
            <step>
              <para>Confirm that Java is installed and in your
              <envar>PATH</envar> by typing the following at a command prompt:
              <programlisting>java -version</programlisting></para>
	      <note>
		<para>To build the indexer, you must have the JDK.</para>
	      </note>
            </step>
          </substeps>
        </step>

        <step>
          <para>If necessary, install <ulink
          url="http://ant.apache.org/bindownload.cgi">Apache Ant</ulink> 1.6.5 
          or higher.</para>

          <substeps>
            <step>
              <para>Unzip the Ant binary distribution to a convenient location
              on your system. For example: <filename>c:\Program
              Files</filename>.</para>
            </step>

            <step>
              <para>Set the environment variable <envar>ANT_HOME</envar> to
              the top-level Ant directory. For example: <filename>c:\Program
              Files\apache-ant-1.7.1</filename>. <tip>
                  <para>See <ulink
                  url="http://support.microsoft.com/kb/310519">How To Manage
                  Environment Variables in Windows XP</ulink> for information
                  on setting environment variables.</para>
                </tip></para>
            </step>

            <step>
              <para>Add the Ant <filename>bin</filename> directory to your
              <envar>PATH</envar>. For example: <filename>c:\Program
              Files\apache-ant-1.7.1\bin</filename></para>
            </step>

            <step>
              <para>Confirm that Ant is installed by typing the following at a
              command prompt: <programlisting>ant -version</programlisting></para>

              <note>
                <para>If you see a message about the file
                <filename>tools.jar</filename> being missing, you can safely
                ignore it.</para>
              </note>
            </step>
          </substeps>
        </step>

        <step>
          <para>Download <ulink url="http://prdownloads.sourceforge.net/saxon/saxon6-5-5.zip">Saxon
              6.5.x</ulink> and unzip the distribution to a convenient location on your file system.
            You will use the path to <filename>saxon.jar</filename> in <xref
              linkend="edit-build-properties"/> below.<note>
              <para>The <filename>build.xml</filename> has only been tested with Saxon 6.5, though
                it could be adapted to work with other XSLT processors. However, when you generate
                output, the Saxon jar must <emphasis role="bold">not</emphasis> be in your
                  <envar>CLASSPATH</envar>.</para>
            </note></para>
        </step>

        <step id="edit-build-properties">
          <para>In a text editor, edit the
          <filename>build.properties</filename> file in the webhelp directory
          and make the changes indicated by the comments:<programlisting># The path (relative to the build.xml file) to your input document.
# To use your own input document, create a build.xml file of your own
# and import this build.xml.
input-xml=docsrc/readme.xml

# The directory in which to put the output files. 
# This directory is created if it does not exist.
output-dir=docs

# If you are using a customization layer that imports webhelp.xsl, use
# this property to point to it. 
stylesheet-path=${ant.file.dir}/xsl/webhelp.xsl

# If your document has image directories that need to be copied
# to the output directory, you can list patterns here. 
# See the Ant documentation for fileset for documentation
# on patterns.
#input-images-dirs=images/**,figures/**,graphics/**

# By default, the ant script assumes your images are stored
# in the same directory as the input-xml. If you store your
# image directories in another directory, specify it here.
# and uncomment this line.
#input-images-basedir=/path/to/image/location

# Modify this so that it points to your copy of the Saxon 6.5 jar.
xslt-processor-classpath=/usr/share/java/saxon-6.5.5.jar

# For non-ns version only, this validates the document 
# against a dtd.
validate-against-dtd=true

# Set this to false if you don't need a search tab.
webhelp.include.search.tab=true

# indexer-language is used to tell the search indexer which language
# the docbook is written.  This will be used to identify the correct
# stemmer, and punctuations that differs from language to language.
# see the documentation for details. en=English, fr=French, de=German,
# zh=Chinese, ja=Japanese etc.  
webhelp.indexer.language=en</programlisting></para>
        </step>

        <step>
          <para>Test the package by running the command <code>ant webhelp
              -Doutput-dir=test-ouput</code> at the command line in the webhelp directory. It should
            generate a copy of this documentation in the <filename class="directory">doc</filename>
            directory. Type <code>start test-output\index.html</code> to open the output in a
            browser. Once you have confirmed that the process worked, you can delete the <filename
              class="directory">test-output</filename> directory. <important>
              <para>The Saxon 6.5 jar should <emphasis>not</emphasis> be in your
                  <envar>CLASSPATH</envar> when you generate the webhelp output. If you have any
                problems, try running ant with an empty <envar>CLASSPATH</envar>.</para>
            </important></para>
        </step>

        <step>
          <para>To process your own document, simply refer to this package
          from another <filename>build.xml</filename> in arbitrary location on
          your system:</para>

          <substeps>
            <step>
              <para>Create a new <filename>build.xml</filename> file that
              defines the name of your source file, the desired output
              directory, and imports the <filename>build.xml</filename> from
              this package. For example: <programlisting>&lt;project&gt;
  &lt;property name="input-xml" value="<replaceable>path-to/yourfile.xml</replaceable>"/&gt;
  &lt;property name="input-images-dirs" value="<replaceable>images/** figures/** graphics/**</replaceable>"/&gt;
  &lt;property name="output-dir" value="<replaceable>path-to/desired-output-dir</replaceable>"/&gt;
  &lt;import file="<replaceable>path-to/docbook-webhelp/</replaceable>build.xml"/&gt;
&lt;/project&gt;</programlisting></para>
            </step>

            <step>
              <para>From the directory containing your newly created
              <filename>build.xml</filename> file, type <code>ant
              webhelp</code> to build your document.</para>
              <important>
                <para>The Saxon 6.5 jar should <emphasis>not</emphasis> be in your
                    <envar>CLASSPATH</envar> when you generate the webhelp output. If you have any
                  problems, try running ant with an empty <envar>CLASSPATH</envar>.</para>
              </important>
            </step>
          </substeps>
        </step>
      </procedure>
    </section>

    <section>
      <title>Using and customizing the output</title>

      <para>To deep link to a topic inside the help set, simply link directly
      to the page. This help system uses no frameset, so nothing further is
      necessary. <tip>
          <para>See <ulink
          url="http://www.sagehill.net/docbookxsl/Chunking.html">Chunking into
          multiple HTML files</ulink> in Bob Stayton's <ulink
          url="http://www.sagehill.net/docbookxsl/index.html">DocBook XSL: The
          Complete Guide</ulink> for information on controlling output file
          names and which files are chunked in DocBook.</para>
        </tip></para>

      <para>When you perform a search, the results can include brief
      summaries. These are populated in one of two ways:<itemizedlist>
          <listitem>
            <para>By adding <sgmltag>role="summary"</sgmltag> to a
            <sgmltag>para</sgmltag> or <sgmltag>phrase</sgmltag> in the
            <sgmltag>chapter</sgmltag> or <sgmltag>section</sgmltag>.</para>
          </listitem>

          <listitem>
            <para>By adding an <sgmltag>abstract</sgmltag> to the
            <sgmltag>chapterinfo</sgmltag> or <sgmltag>sectioninfo</sgmltag>
            element.</para>
          </listitem>
        </itemizedlist></para>

      <para>To customize the look and feel of the help, study the following
      css files:<itemizedlist>
          <listitem>
            <para><filename>docs/common/css/positioning.css</filename>: This
            handles the Positioning of DIVs in appropriate positions. For
            example, it causes the <code>leftnavigation</code> div to appear
            on the left, the header on top, and so on. Use this if you need to
            change the relative positions or need to change the width/height
            etc.</para>
          </listitem>

          <listitem>
            <para><filename>docs/common/jquery/theme-redmond/jquery-ui-1.8.2.custom.css</filename>:
            This is the theming part which adds colors and stuff. This is a
            default theme comes with <ulink
            url="http://jqueryui.com/download">jqueryui</ulink> unchanged. You
            can get any theme based your interest from this. (Themes are on
            right navigation bar.) Then replace the css theme folder
            (theme-redmond) with it, and change the xsl to point to the new
            css.</para>
          </listitem>

          <listitem>
            <para><filename>docs/common/jquery/treeview/jquery.treeview.css</filename>:
            This styles the toc Tree. Generally, you don't have to edit this
            file.</para>
          </listitem>
        </itemizedlist></para>

      <section>
        <title>Recommended Apache configurations</title>

        <para>If you are serving a long document from an Apache web server, we
        recommend you make the following additions or changes to your
        <filename>httpd.conf</filename> or <filename>.htaccess</filename>
        file. <remark>TODO: Explain what each thing
        does.</remark><programlisting>AddDefaultCharSet UTF-8 # <co
              id="AddDefaultCharSet" />
  
      # 480 weeks
      &lt;FilesMatch "\.(ico|pdf|flv|jpg|jpeg|png|gif|js|css|swf)$"&gt; # <co
                    id="CachingSettings" />
      Header set Cache-Control "max-age=290304000, public"
      &lt;/FilesMatch&gt;
      
      # 2 DAYS
      &lt;FilesMatch "\.(xml|txt)$"&gt;
      Header set Cache-Control "max-age=172800, public, must-revalidate"
      &lt;/FilesMatch&gt;
      
      # 2 HOURS
      &lt;FilesMatch "\.(html|htm)$"&gt;
      Header set Cache-Control "max-age=7200, must-revalidate"
      &lt;/FilesMatch&gt;
      
      # compress text, html, javascript, css, xml:
      AddOutputFilterByType DEFLATE text/plain # <co id="CompressSetting" />
      AddOutputFilterByType DEFLATE text/html
      AddOutputFilterByType DEFLATE text/xml
      AddOutputFilterByType DEFLATE text/css
      AddOutputFilterByType DEFLATE application/xml
      AddOutputFilterByType DEFLATE application/xhtml+xml
      AddOutputFilterByType DEFLATE application/rss+xml
      AddOutputFilterByType DEFLATE application/javascript
      AddOutputFilterByType DEFLATE application/x-javascript
      
      # Or, compress certain file types by extension:
      &lt;Files *.html&gt; 
      SetOutputFilter DEFLATE
      &lt;/Files&gt;
      </programlisting><calloutlist>
            <callout arearefs="AddDefaultCharSet">
              <para>See <ulink
              url="http://www.sagehill.net/docbookxsl/SpecialChars.html">Odd
              characters in HTML output</ulink> in Bob Stayton's book
              <citetitle>DocBook XSL: The Complete Guide</citetitle> for more
              information about this setting.</para>
            </callout>

            <callout arearefs="CachingSettings">
              <para>These lines and those that follow cause the browser to
              cache various resources such as bitmaps and JavaScript files.
              Note that caching JavaScript files could cause your users to
              have stale search indexes if you update your document since the
              search index is stored in JavaScript files.</para>
            </callout>

            <callout arearefs="CompressSetting">
              <para>These lines cause the the server to compress html, css,
              and JavaScript files and the brower to uncompress them to
              improve download performance.</para>
            </callout>
          </calloutlist></para>
      </section>
    </section>

    <section>
      <title>Building the indexer</title>

      <para role="summary">To build the indexer, you must have installed the
      JDK version 1.5 or higher and set the <envar>ANT_HOME</envar>
      environment variable. Run <code>ant build-indexer</code> to recompile
      <filename>nw-cms.jar</filename></para>

      <indexterm>
        <primary>ANT_HOME</primary>
      </indexterm>

      <indexterm>
        <primary>indexer</primary>

        <secondary>building</secondary>
      </indexterm>
    </section>

    <section>
      <title>Adding support for other (non-CJKV) languages</title>

      <para>To support stemming for a language, the search mechanism requires
      a stemmer implemented in both Java and JavaScript. The Java version is
      used by the indexer and the JavaScript verison is used to stem the
      user's input on the search form. Currently the search mechanism supports
      stemming for English and German. In addition, Java stemmers are included
      for the following languages. Therefore, to support these languages, you
      only need to implement the stemmer in JavaScript and add it to the
      template. If you do undertake this task, please consider contributing
      the JavaScript version back to this project and to <ulink
      url="http://snowball.tartarus.org/texts/stemmersoverview.html">Martin
      Porter's project</ulink>.<itemizedlist>
          <listitem>
            <para>Danish</para>
          </listitem>

          <listitem>
            <para>Dutch</para>
          </listitem>

          <listitem>
            <para>Finnish</para>
          </listitem>

          <listitem>
            <para>Hungarian</para>
          </listitem>

          <listitem>
            <para>Italian</para>
          </listitem>

          <listitem>
            <para>Norwegian</para>
          </listitem>

          <listitem>
            <para>Portuguese</para>
          </listitem>

          <listitem>
            <para>Romanian</para>
          </listitem>

          <listitem>
            <para>Russian</para>
          </listitem>

          <listitem>
            <para>Spanish</para>
          </listitem>

          <listitem>
            <para>Swedish</para>
          </listitem>

          <listitem>
            <para>Turkish</para>
          </listitem>
        </itemizedlist></para>
    </section>
  </chapter>

  <chapter>
    <title>Developer Docs</title>

    <para role="summary">This chapter provides an overview of how webhelp is implemented.</para>

    <para>The table of contents and search panes are implemented as divs and
    rendered as if they were the left pane in a frameset. As a result, the
    page must save the state of the table of contents and the search in
    cookies when you navigate away from a page. When you load a new page, the
    page reads these cookies and restores the state of the table of contents
    tree and search. The result is that the help system behaves exactly as if
    it were a frameset.</para>
    
    <section>
      <title>Design</title>
      <para role="summary">An overview of webhelp page structure.</para>
      <para>DocBook WebHelp page structure is fully built on css-based design
        abandoning frameset structure. Overall page structure can be divided in to three main sections
        <itemizedlist>
          <listitem>
            <para>Header: Header is a separate Div which include company logo, 
              navigation button(prev, next etc.), page title and heading of parent topic.</para>
          </listitem>
          
          <listitem>
            <para>Content: This includes the content of the documentation. The processing of this part is
              done by <ulink
                url="http://docbook.sourceforge.net/release/xsl/current/xhtml/chunk.xsl">
                DocBook XSL Chunking customization</ulink>. Few further css-styling applied from 
              <filename>positioning.css</filename>.            
            </para>
          </listitem>
          
          <listitem>
            <para>Left Navigation: This includes the table of contents and search tab. This 
              is customized using <ulink url="http://jqueryui.com/">jquery-ui</ulink> styling.</para>
            <itemizedlist>
              <listitem>
                <para>Tabbed Navigation: The navigation pane is organized in to two tabs. 
                  Contents tab, and Search tab. Tabbed output is achieved using 
                  <ulink url="http://docs.jquery.com/UI/Tabs">JQuery Tabs plugin</ulink>.
                </para>  
              </listitem>
              
              <listitem>
                <para>Table of Contents (TOC) tree: When building the chunked html from the 
                  docbook file, Table of Contents is generated as an Unordered List (a list 
                  made from <code>&lt;ul> &lt;li></code> tags). When page loads in the browser,
                  we apply styling to it to achieve the nice look that you see. Styling for TOC 
                  tree is done by a JQuery UI plugin called 
                  <ulink url="http://bassistance.de/jquery-plugins/jquery-plugin-treeview/">
                  TreeView</ulink>. We can generate the tree easily by following javascript code:
                  
<programlisting>
//Generate the tree
$("#tree").treeview({
collapsed: true,
animated: "medium",
control: "#sidetreecontrol",
persist: "cookie"
});
</programlisting> 
                  </para>
              </listitem>
              
              <listitem>
                <para>Search Tab: This includes the search feature.</para>
              </listitem>
              </itemizedlist>
            
          </listitem>
        </itemizedlist> 
      </para>       
    </section>
    
    <section>
      <title>Search</title>
      <para role="summary">Overview design of Search mechanism.</para>
      <para>
        The searching is a fully client-side implementation of querying texts for
        content searching, and no server is involved. That means when a user enters a query, 
        it is processed by JavaScript inside the browser, and displays the matching results by
        comparing the query with a generated 'index', which too reside in the client-side web browser.
        
        Mainly the search mechanism has two parts.
        <itemizedlist>
          <listitem>
            <para>Indexing: First we need to traverse the content in the docs/content folder and index 
              the words in it. This is done by <filename>nw-cms.jar</filename>. You can invoke it by  
            <code>ant index</code> command from the root of webhelp of directory. You can recompile it 
              again and build the jar file by <code>ant build-indexer</code>. Indexer has some extensive 
              support for such as stemming of words. Indexer has extensive support for English, German,
              French languages. By extensive support, what I meant is that those texts are stemmed
              first, to get the root word and then indexes them. For CJK (Chinese, Japanese, Korean)
              languages, it uses bi-gram tokenizing to break up the words. (CJK languages does not have 
              spaces between words.)                
            </para>
            <para>
              When we run <code>ant index</code>, it generates five output files:
                <itemizedlist>
                  <listitem>
                    <para><filename>htmlFileList.js</filename> - This contains an array named <code>fl</code> which stores details 
                    all the files indexed by the indexer.  
                    </para>
                  </listitem>
                  <listitem>
                    <para><filename>htmlFileInfoList.js</filename> - This includes some meta data about the indexed files in an array 
                      named <code>fil</code>. It includes details about file name, file (html) title, a summary 
                      of the content.Format would look like, 
      <code>fil["4"]= "ch03.html@@@Developer Docs@@@This chapter provides an overview of how webhelp is implemented.";</code> 
                    </para>
                  </listitem>
                  
                  <listitem>
                    <para><filename>index-*.js</filename> (Three index files) - These three files actually stores the index of the content. 
                      Index is added to an array named <code>w</code>.</para>
                  </listitem>
                </itemizedlist>
              
            </para>
          </listitem>
          
          <listitem>
            <para>
              Querying: Query processing happens totally in client side. Following JavaScript files handles them.
              <itemizedlist>
                <listitem>
                  <para><filename>nwSearchFnt.js</filename> - This handles the user query and returns the search results. It does query 
                    word tokenizing, drop unnecessary punctuations and common words, do stemming if docbook language 
                    supports it, etc.</para>
                </listitem>
                <listitem>
                  <para><filename>{$indexer-language-code}_stemmer.js</filename> - This includes the stemming library. 
                    <filename>nwSearchFnt.js</filename> file calls <code>stemmer</code> method in this file for stemming.
                    ex: <code>var stem = stemmer(foobar);</code>                    
                  </para>
                </listitem>
              </itemizedlist>
            </para>
          </listitem>
        </itemizedlist>
      </para>
      
      <section>
        <title>New Stemmers</title>
        <para role="summary">Adding new Stemmers is very simple.</para>
        <para>Currently, only English, French, and German stemmers are integrated in to WebHelp. But the code is
        extensible such that you can add new stemmers easily by few steps.</para>
        <para>What you need:
        <itemizedlist> 
          <listitem>
            <para>You'll need two versions of the stemmer; One written in JavaScript, and another in Java. But fortunately, 
              Snowball contains Java stemmers for number of popular languages, and are already included with the package. 
              You can see the full list in <ulink url="ch02s04.html">Adding support for other (non-CJKV) languages</ulink>. 
              If your language is listed there,
              Then you have to find javascript version of the stemmer. Generally, new stemmers are getting added in to
              <ulink url="http://snowball.tartarus.org/otherlangs/index.html">Snowball Stemmers in other languages</ulink> location.
              If javascript stemmer for your language is available, then download it. Else, you can write a new stemmer in 
              JavaScript using SnowBall algorithm fairly easily. Algorithms are at  
              <ulink url="http://snowball.tartarus.org/">Snowball</ulink>. 
            </para>
          </listitem>
          <listitem>
            <para>Then, name the JS stemmer exactly like this: <filename>{$language-code}_stemmer.js</filename>. For example, 
              for Italian(it), name it as, <filename>it_stemmer.js</filename>. Then, copy it to the 
              <filename>docbook-webhelp/template/content/search/stemmers/</filename> folder. (I assumed 
              <filename>docbook-webhelp</filename> is the root folder for webhelp.)
              <note>
                <para>Make sure you changed the <code>webhelp.indexer.language</code> property in <filename>build.properties</filename>
                to your language.
                </para>
              </note>

            </para>
            
          </listitem>
          <listitem>
            <para>Now two easy changes needed for the indexer.</para>
            <itemizedlist>
              <listitem>
                <para>Open <filename>docbook-webhelp/indexer/src/com/nexwave/nquindexer/IndexerTask.java</filename> in 
                  a text editor and add your language code to the <code>supportedLanguages</code> String Array. </para>
                <example>
                  <title>Add new language to supportedLanguages array</title>
                  <para>
                    change the Array from,
<programlisting>
private String[] supportedLanguages= {"en", "de", "fr", "cn", "ja", "ko"}; 
    //currently extended support available for
    // English, German, French and CJK (Chinese, Japanese, Korean) languages only.
</programlisting>
                    To,</para>
                    <programlisting>
private String[] supportedLanguages= {"en", "de", "fr", "cn", "ja", "ko", <emphasis>"it"</emphasis>}; 
  //currently extended support available for
  // English, German, French, CJK (Chinese, Japanese, Korean), and Italian languages only.
                    </programlisting>
                  
                </example>
              </listitem>
              <listitem>
                <para>
                  Now, open <filename>docbook-webhelp/indexer/src/com/nexwave/nquindexer/SaxHTMLIndex.java</filename> and 
                  add the following line to the code where it initializes the Stemmer (Search for 
                  <code>SnowballStemmer stemmer;</code>). Then add code to initialize the stemmer Object in your language. 
                  It's self understandable. See the example. The class names are at: 
                  <filename>docbook-webhelp/indexer/src/com/nexwave/stemmer/snowball/ext/</filename>.
                </para>                  
                  <example>
                    <title>initialize correct stemmer based on the <code>webhelp.indexer.language</code> specified</title>
<programlisting>
      SnowballStemmer stemmer;
      if(indexerLanguage.equalsIgnoreCase("en")){
           stemmer = new EnglishStemmer();
      } else if (indexerLanguage.equalsIgnoreCase("de")){
          stemmer= new GermanStemmer();
      } else if (indexerLanguage.equalsIgnoreCase("fr")){
          stemmer= new FrenchStemmer();
      }
<emphasis>else if (indexerLanguage.equalsIgnoreCase("it")){ //If language code is "it" (Italian)
          stemmer= new italianStemmer();  //Initialize the stemmer to <code>italianStemmer</code> object.
      } </emphasis>      
      else {
          stemmer = null;
      }
</programlisting>
                  </example>
              </listitem>
            </itemizedlist> 
          </listitem>
        </itemizedlist>
        </para>
        <para>That's all. Now run <code>ant build-indexer</code> to compile and build the java code. 
          Then, run <code>ant webhelp</code> to generate the output from your docbook file. 
          For any questions, contact us or email to the docbook mailing list 
          <email>docbook-apps@lists.oasis-open.org</email>.
        </para> 
      </section>      
    </section> 
  </chapter>
</book>
# Sluift

## Building/Installing

If you have a Lua installed on your system, edit `config.py` to point the build
to it using the `lua_libdir`, `lua_includedir`, and `lua_libname` (usually 
only needed on Windows) variables.

In case no Lua installation is found, a bundled Lua version will be used.
Note that there are several limitations when using the bundled Lua:

- The standalone Sluift binary will not support dynamic loading of modules.
- The Sluift module will not be built

The standalone executable will be placed into `Sluift/exe`, and the loadable
Lua module in `Sluift/dll`.

In order to use the Sluift Lua module, make sure it is copied to a location in the
Lua search path (`LUA_PATH`, or the built-in path). On Linux and Mac OS X, this is
typically `<LUA_INSTALLPREFIX>/lib/lua/<LUA_VERSION>/`. If `require 'sluift'` fails,
the error message will give an indication what this path is.


## Examples

Example scripts can be found in `Examples/`, and in the Swift tree under
`Swiften/QA/ScriptedTests`.

## Extending

### Adding support for payloads

To add support for a specific Swiften payload, create a new `LuaElementConvertor`
in `ElementConvertors/` by inheriting from `GenericLuaElementConvertor`, and register
it it `LuaElementConvertors.cpp`. The name of the convertor passed in the constructor
of `GenericLuaElementConvertor` should correspond to the snake case version of the 
Swiften element it converts. For examples, see the existing convertors in
`ElementConvertors/`.

When the convertor is registered, you can use it in message bodies, or in get/set
queries. For example, for the `command` convertor:
  
    client:set{to = 'alice@wonderland.lit', query = {_type = 'command', 
      type = 'execute', node = 'uptime'}}

Optionally, you can add a convenience `set_<type>` shortcut on the client object by
adding it to the list of `get_set_shortcuts` in `boot.lua`. With such a shortcut, the
command above can be rewritten as:

    client:set_command{to = 'alice@wonderland.lit', command = {
      type = 'execute', node = 'uptime'}}


Lato font family (Desktop version)

==================================

Version 2.015; Latin+Cyrillic+Greek+IPA opensource

Created by: tyPoland Lukasz Dziedzic
Creation year: 2015

Copyright (c) 2010-2015 by tyPoland Lukasz Dziedzic with Reserved Font Name "Lato". Licensed under the SIL Open Font License, Version 1.1.

Lato is a trademark of tyPoland Lukasz Dziedzic.

Source URL: http://www.latofonts.com/
License URL: http://scripts.sil.org/OFL

================

Lato is a sanserif typeface family designed in the Summer 2010 and extended in the Summer 2013 by Warsaw-based designer Lukasz Dziedzic ("Lato" means "Summer" in Polish). It tries to carefully balance some potentially conflicting priorities: it should seem quite "transparent" when used in body text but would display some original traits when used in larger sizes. The classical proportions, particularly visible in the uppercase, give the letterforms familiar harmony and elegance. At the same time, its sleek sanserif look makes evident the fact that Lato was designed in the 2010s, even though it does not follow any current trend. The semi-rounded details of the letters give Lato a feeling of warmth, while the strong structure provides stability and seriousness. In 2013-2014, the family was greatly extended (with the help of Adam Twardoch and Botio Nikoltchev) to cover 3000+ glyphs over nine weights with italics. It now supports 100+ Latin-based languages, 50+ Cyrillic-based languages as well as Greek and IPA phonetics. The Lato fonts are available free of charge under the SIL Open Font License from http://www.latofonts.com/

================

CONTENTS: 

This folder contains 18 font files in OpenType TT (.ttf) format. You can install these fonts on your computer and use in any desktop applications (such as Word, InDesign, Illustrator, Photoshop, Keynote or Pages). 

================

REVISION LOG:

# Version 2.015 (2015-08-06)
Initial implementation of mark positioning (should work for most glyphs)
Autohinted using ttfautohint 1.3.

# Version 2.010 (2014-09-01)
Improved some contour bugs and diacritics positioning. 
Improved outline quality.
Revised OTL features so that they work in browsers (ot-sanitise).
Autohinted using ttfautohint 1.1.
Interpolated the Medium weight differently so it provides more visual difference from Regular.

# Version 2.007 (2014-02-27)
Greatly expanded character set, revised metrics, four additional weights.

# Version 1.104 (2011-11-08)
Merged the distribution again
Autohinted with updated ttfautohint 0.4 (which no longer causes Adobe and iOS problems) 
except the Hai and Lig weights which are hinted in FLS 5.1.

# Version 1.102 (2011-10-28)
Added OpenType Layout features
Ssplit between desktop and web versions
Desktop version: all weights autohinted with FontLab Studio
Web version autohinted with ttfautohint 0.4 except the Hai and Lig weights

# Version 1.101 (2011-09-30)
Fixed OS/2 table Unicode and codepage entries

# Version 1.100 (2011-09-12)
Added Polish diacritics to the character set
Weights Hai and Lig autohinted with FontLab Studio
Other weights autohinted with ttfautohint 0.3

# Version 1.011 (2010-12-29)
Added the soft hyphen glyph

# Version 1.010 (2010-12-13)
Initial version released under SIL Open Font License
Western character set

================
# Breakpad

Breakpad is a set of client and server components which implement a
crash-reporting system.

* [Homepage](https://chromium.googlesource.com/breakpad/breakpad/)
* [Documentation](https://chromium.googlesource.com/breakpad/breakpad/+/master/docs/)
* [Bugs](https://bugs.chromium.org/p/google-breakpad/)
* Discussion/Questions: [google-breakpad-discuss@googlegroups.com](https://groups.google.com/d/forum/google-breakpad-discuss)
* Developer/Reviews: [google-breakpad-dev@googlegroups.com](https://groups.google.com/d/forum/google-breakpad-dev)
* Tests: [![Build Status](https://travis-ci.org/google/breakpad.svg?branch=master)](https://travis-ci.org/google/breakpad) [![Build status](https://ci.appveyor.com/api/projects/status/eguv4emv2rhq68u2?svg=true)](https://ci.appveyor.com/project/vapier/breakpad)
* Coverage [![Coverity Status](https://scan.coverity.com/projects/9215/badge.svg)](https://scan.coverity.com/projects/google-breakpad)

## Getting started (from master)

1.  First, [download depot_tools](http://dev.chromium.org/developers/how-tos/install-depot-tools)
    and ensure that they’re in your `PATH`.

2.  Create a new directory for checking out the source code (it must be named
    breakpad).

    ```sh
    mkdir breakpad && cd breakpad
    ```

3.  Run the `fetch` tool from depot_tools to download all the source repos.

    ```sh
    fetch breakpad
    cd src
    ```

4.  Build the source.

    ```sh
    ./configure && make
    ```

    You can also cd to another directory and run configure from there to build
    outside the source tree.

    This will build the processor tools (`src/processor/minidump_stackwalk`,
    `src/processor/minidump_dump`, etc), and when building on Linux it will
    also build the client libraries and some tools
    (`src/tools/linux/dump_syms/dump_syms`,
    `src/tools/linux/md2core/minidump-2-core`, etc).

5.  Optionally, run tests.

    ```sh
    make check
    ```

6.  Optionally, install the built libraries

    ```sh
    make install
    ```

If you need to reconfigure your build be sure to run `make distclean` first.

To update an existing checkout to a newer revision, you can
`git pull` as usual, but then you should run `gclient sync` to ensure that the
dependent repos are up-to-date.

## To request change review

1.  Follow the steps above to get the source and build it.

2.  Make changes. Build and test your changes.
    For core code like processor use methods above.
    For linux/mac/windows, there are test targets in each project file.

3.  Commit your changes to your local repo and upload them to the server.
    http://dev.chromium.org/developers/contributing-code
    e.g. `git commit ... && git cl upload ...`
    You will be prompted for credential and a description.

4.  At https://chromium-review.googlesource.com/ you'll find your issue listed;
    click on it, then “Add reviewer”, and enter in the code reviewer. Depending
    on your settings, you may not see an email, but the reviewer has been
    notified with google-breakpad-dev@googlegroups.com always CC’d.


                 SCons - a software construction tool

                         Version __VERSION__


This is SCons, a tool for building software (and other files).  SCons is
implemented in Python, and its "configuration files" are actually Python
scripts, allowing you to use the full power of a real scripting language
to solve build problems.  You do not, however, need to know Python to
use SCons effectively.

See the RELEASE.txt file for notes about this specific release,
including known problems.  See the CHANGES.txt file for a list of
changes since the previous release.


LATEST VERSION
==============

Before going further, you can check that this package you have is
the latest version by checking the SCons download page at:

        http://www.scons.org/download.html


EXECUTION REQUIREMENTS
======================

Running SCons requires Python version 2.7.*.  Currently it does not 
run on the Python 3.x release.  There should be
no other dependencies or requirements to run SCons.  (There is, however,
an additional requirement to *install* SCons from this particular
package; see the next section.)

By default, SCons knows how to search for available programming tools
on various systems--see the SCons man page for details.  You may,
of course, override the default SCons choices made by appropriate
configuration of Environment construction variables.


INSTALLATION REQUIREMENTS
=========================

Nothing special.


INSTALLATION
============

Assuming your system satisfies the installation requirements in the
previous section, install SCons from this package simply by running the
provided Python-standard setup script as follows:

        # python setup.py install

By default, the above command will do the following:

    --  Install the version-numbered "scons-__VERSION__" and "sconsign-__VERSION__"
        scripts in the default system script directory (/usr/bin or
        C:\Python*\Scripts, for example).  This can be disabled by
        specifying the "--no-version-script" option on the command
        line.

    --  Install scripts named "scons" and "sconsign" scripts in the
        default system script directory (/usr/bin or C:\Python*\Scripts,
        for example).  This can be disabled by specifying the
        "--no-scons-script" option on the command line, which is useful
        if you want to install and experiment with a new version before
        making it the default on your system.

        On UNIX or Linux systems, you can have the "scons" and "sconsign"
        scripts be hard links or symbolic links to the "scons-__VERSION__" and
        "sconsign-__VERSION__" scripts by specifying the "--hardlink-scons"
        or "--symlink-scons" options on the command line.

    --  Install "scons-__VERSION__.bat" and "scons.bat" wrapper scripts in the
        Python prefix directory on Windows (C:\Python*, for example).
        This can be disabled by specifying the "--no-install-bat" option
        on the command line.

        On UNIX or Linux systems, the "--install-bat" option may be
        specified to have "scons-__VERSION__.bat" and "scons.bat" files
        installed in the default system script directory, which is useful
        if you want to install SCons in a shared file system directory
        that can be used to execute SCons from both UNIX/Linux and
        Windows systems.

    --  Install the SCons build engine (a Python module) in an
        appropriate version-numbered SCons library directory
        (/usr/lib/scons-__VERSION__ or C:\Python*\scons-__VERSION__, for example).
        See below for more options related to installing the build
        engine library.

    --  Install the troff-format man pages in an appropriate directory
        on UNIX or Linux systems (/usr/share/man/man1 or /usr/man/man1,
        for example).  This can be disabled by specifying the
        "--no-install-man" option on the command line.  The man pages
        can be installed on Windows systems by specifying the
        "--install-man" option on the command line.

Note that, by default, SCons does not install its build engine library
in the standard Python library directories.  If you want to be able to
use the SCons library modules (the build engine) in other Python
scripts, specify the "--standard-lib" option on the command line, as
follows:

        # python setup.py install --standard-lib

This will install the build engine in the standard Python library
directory (/usr/lib/python*/site-packages or
C:\Python*\Lib\site-packages).

Alternatively, you can have SCons install its build engine library in a
hard-coded standalone library directory, instead of the default
version-numbered directory, by specifying the "--standalone-lib" option
on the command line, as follows:

        # python setup.py install --standalone-lib

This is usually not recommended, however.

Note that, to install SCons in any of the above system directories,
you should have system installation privileges (that is, "root" or
"Administrator") when running the setup.py script.  If you don't have
system installation privileges, you can use the --prefix option to
specify an alternate installation location, such as your home directory:

        $ python setup.py install --prefix=$HOME

This will install SCons in the appropriate locations relative to
$HOME--that is, the scons script itself $HOME/bin and the associated
library in $HOME/lib/scons, for example.


DOCUMENTATION
=============

See the RELEASE.txt file for notes about this specific release,
including known problems.  See the CHANGES.txt file for a list of
changes since the previous release.

The scons.1 man page is included in this package, and contains a section
of small examples for getting started using SCons.

Additional documentation for SCons is available at:

        http://www.scons.org/doc.html


LICENSING
=========

SCons is distributed under the MIT license, a full copy of which is
available in the LICENSE.txt file. The MIT license is an approved Open
Source license, which means:

        This software is OSI Certified Open Source Software.  OSI
        Certified is a certification mark of the Open Source Initiative.

More information about OSI certifications and Open Source software is
available at:

        http://www.opensource.org/


REPORTING BUGS
==============

Please report bugs by following the detailed instructions on our Bug
Submission page:

        http://scons.tigris.org/bug-submission.html

You can also send mail to the SCons developers' mailing list:

        scons-dev@scons.org

But even if you send email to the mailing list please make sure that you
ALSO submit a bug report to the project page bug tracker, because bug
reports in email often get overlooked in the general flood of messages.


MAILING LISTS
=============

An active mailing list for users of SCons is available.  You may send
questions or comments to the list at:

        scons-users@scons.org

You may subscribe to the mailing list by sending email to:

        scons-users-join@scons.org

There is also a low-volume mailing list available for announcements
about SCons.  Subscribe by sending email to:

        announce-subscribe@scons.tigris.org

There are other mailing lists available for SCons developers, for
notification of SCons code changes, and for notification of updated
bug reports and project documents.  Please see our mailing lists page
for details.


DONATIONS
=========

If you find SCons helpful, please consider making a donation (of cash,
software, or hardware) to support continued work on the project.
Information is available at:

        http://www.scons.org/donate.html


FOR MORE INFORMATION
====================

Check the SCons web site at:

        http://www.scons.org/


AUTHOR INFO
===========
SCons was originally written by Steven Knight, knight at baldmt dot com.
Since around 2010 it has been maintained by the SCons
development team, co-managed by Bill Deegan and Gary Oberbrunner, with
many contributors, including but not at all limited to:

- Chad Austin
- Dirk Baechle
- Charles Crain
- William Deegan
- Steve Leblanc
- Rob Managan
- Greg Noel
- Gary Oberbrunner
- Anthony Roach
- Greg Spencer
- Tom Tanner
- Anatoly Techtonik
- Christoph Wiedemann
- Russel Winder

\... and many others.

Copyright (c) 2001 - 2015 The SCons Foundation
----------------------------------------------------------------------
              README file for the DocBook XSL Stylesheets
----------------------------------------------------------------------
$Id: README 8484 2009-07-13 20:35:34Z mzjn $

These are XSL stylesheets for transforming DocBook XML document
instances into various output formats.

This README file provides only very minimal documentation on using
the stylesheets. For more complete information, see Bob Stayton's
book "DocBook XSL: The Complete Guide", available online at:

  http://www.sagehill.net/docbookxsl/

----------------------------------------------------------------------
Installation
----------------------------------------------------------------------
See the INSTALL file for information about installing this release.

----------------------------------------------------------------------
How to use the stylesheets
----------------------------------------------------------------------
The base canonical URI for these stylesheets is:

  http://docbook.sourceforge.net/release/xsl/current/

You call any of the stylesheets in this distribution by doing one
of the following:

  - Use the base canonical URI in combination with one of the
    pathnames below. For example, for "chunked" HTML, output:

    http://docbook.sourceforge.net/release/xsl/current/html/chunk.xsl

    If your system has a working XML Catalog or SGML Catalog setup
    (most Linux systems do), then that URI will automatically be
    resolved and replaced with a local pathname on your system.

  - Use a "real" local system base path in combination with one of
    the pathnames below. For example, for "chunked" HTML, output:

    /usr/share/xml/docbook/stylesheet/nwalsh/html/chunk.xsl

To transform documents created with the standard DocBook
schema/DTD, use one of the following stylesheets:

  fo/docbook.xsl              - for XSL-FO

  html/docbook.xsl            - for HTML (as a single file)
  html/chunk.xsl              - for HTML (chunked into multiple files)
  html/onechunk.xsl           - for HTML (chunked output in single file)

  xhtml/*.xsl                 - for XHTML versions of the above

  xhtml-1_1/*.xsl             - for XHTML 1.1 versions of the above

  epub/docbook.xsl            - for .epub 

  htmlhelp/htmlhelp.xsl       - for HTML Help
  javahelp/javahelp.xsl       - for JavaHelp
  eclipse/eclipse.xsl         - for Eclipse Help

  manpages/docbook.xsl        - for groff/nroff man pages

  */profile-*                 - single-pass-profiling versions of all above

  roundtrip/*.xsl             - for DocBook to WordML, etc., to DocBook

To transform documents created with the DocBook Slides schema/DTD,
use one of the following stylesheets:

  slides/html/*.xsl           - for HTML slides of various kinds
  slides/xhtml/*.xsl          - for XHTML slides of various kinds
  slides/fo/plain.xsl         - for XSL-FO slides
  slides/htmlhelp/...         - for HTML Help slides

To transform documents created with the DocBook Website
schema/DTD, use one of the following stylesheets:

  website/website.xsl         - for non-tabular, non-chunked output
  website/tabular.xsl         - for tabular, non-chunked output
  website/chunk-*             - for chunked output

To generate a titlepage customization layer from a titlepage spec:

  template/titlepage.xsl

For details about creating titlepage spec files and generating and
using titlepage customization layers, see "DocBook XSL: The
Complete Guide" <http://www.sagehill.net/docbookxsl/>

----------------------------------------------------------------------
Manifest
----------------------------------------------------------------------
AUTHORS       contact information
BUGS          about known problems
COPYING       copyright information
INSTALL       installation instructions
README        this file
RELEASE.*     per-release cumulative summaries of user-visible changes
TODO          about planned features not yet implemented
VERSION       release metadata, including the current version
              number (note that the VERSION file is an XSL stylesheet)
NEWS          changes since the last public release (for a cumulative list of
              changes, see the ChangeHistory.xml file)

common/       code used among several output formats (HTML, FO, manpages,...)
docsrc/       documentation sources
eclipse/      for producing Eclipse Help
epub/         for producing .epub
extensions/   DocBook XSL Java extensions
fo/           for producing XSL-FO
highlighting  files used for adding source-code syntax highlighting in output
html/         for producing HTML
htmlhelp/     for producing HTML Help
images/       images used in callouts and graphical admonitions
javahelp/     for producing Java Help
lib/          utility stylesheets with schema-independent functions
manpages/     for producing groff/troff man pages
profiling/    for profiling (omitting/including conditional text)
roundtrip/    for "round trip" conversion among DocBook and
              various word-processor formats (WordML, etc.)
slides/       for producing slides output (from Slides source)
template/     templates for building stylesheet customization layers
tools/        assorted supplementary tools
website/      for producing website output (from Website source)
xhtml/        for producing XHTML
xhtml-1_1/    for producing (stricter) XHTML 1.1

----------------------------------------------------------------------
Changes
----------------------------------------------------------------------
See the NEWS file for changes made since the previous release.

See the RELEASE-NOTES.html or RELEASE-NOTES.txt or RELEASE-NOTES.pdf
files for per-release cumulative summaries of significant
user-visible changes.

For online access to a hyperlinked view of all changes made over
the entire history of the codebase, see the following:

  http://docbook.svn.sourceforge.net/viewvc/docbook/trunk/xsl/?view=log

WARNING: That above change history is a very long list and may
take a long time to load/download.

You can also create an XML-formatted "ChangeHistory.xml" copy of
the complete change history for the codebase by running the
following commands:

  svn checkout https://docbook.svn.sf.net/svnroot/docbook/trunk/xsl
  svn log --xml --verbose xsl > ChangeHistory.xml

----------------------------------------------------------------------
Copyright information
----------------------------------------------------------------------
See the accompanying file named COPYING.
To use the syntax higlighting extension with DocBook-XSL 1.74.3+, you must:
1. Use a processor that works with the extension: Saxon 6 or Xalan-J.
2. Add the latest version of xslthl-2.X.X.jar to your classpath.
3. Set the highlight.source parameter to 1.
4. Import into your customization one of the following stylesheet module:
  * html/highlight.xsl
  * xhtml/highlight.xsl
  * xhtml-1_1/highlight.xsl
  * fo/highlight.xsl
5. Use that customiztion layer.


Note: Saxon 8.5 or later is also supported, but since it is an XSLT 2.0
processor it is not guaranteed to work with DocBook-XSL in all
circumstances. 

----------------------------------------------------------------------
              README file for the DocBook XSL Stylesheets
----------------------------------------------------------------------

These are XSL stylesheets for transforming DocBook XML document
instances into .epub format.

.epub is an open standard of the The International Digital Publishing Forum (IDPF), 
a the trade and standards association for the digital publishing industry. 

An alpha-quality reference implementation (dbtoepub) for a DocBook to .epub 
converter (written in Ruby) is available under bin/. 

From http://idpf.org
  What is EPUB, .epub, OPS/OCF & OEB?

  ".epub" is the file extension of an XML format for reflowable digital 
  books and publications.  ".epub" is composed of three open standards, 
  the Open Publication Structure (OPS), Open Packaging Format (OPF) and 
  Open Container Format (OCF), produced by the IDPF. "EPUB" allows 
  publishers to produce and send a single digital publication file 
  through distribution and offers consumers interoperability between 
  software/hardware for unencrypted reflowable digital books and other 
  publications. The Open eBook Publication Structure or "OEB", 
  originally produced in 1999, is the precursor to OPS. 

----------------------------------------------------------------------
.epub Constraints 
----------------------------------------------------------------------

.epub does not support all of the image formats that DocBook supports.
When an image is available in an accepted format, it will be used. The
accepted @formats are: 'GIF','GIF87a','GIF89a','JPEG','JPG','PNG','SVG'
A mime-type for the image will be guessed from the file extension, 
which may not work if your file extensions are non-standard.

Non-supported elements:
  * <mediaobjectco> 
  * <inlinegraphic>, <graphic>, <textdata>, <imagedata> with text/XML 
    @filerefs
  * <olink>
  * <cmdsynopsis> in lists (generic XHTML rendering inability)
  * <footnote><para><programlisting> (just make your programlistings 
    siblings, rather than descendents of paras)

----------------------------------------------------------------------
dbtoepub Reference Implementation
----------------------------------------------------------------------

An alpha-quality DocBook to .epub conversion program, dbtoepub, is provided
in bin/dbtoepub. 

This tool requires:
 - 'xsltproc' in your PATH
 - 'zip' in your PATH
 - Ruby 1.8.4+

Windows compatibility has not been extensively tested; bug reports encouraged.
[See http://www.zlatkovic.com/libxml.en.html and http://unxutils.sourceforge.net/]

$ dbtoepub --help
  Usage: dbtoepub [OPTIONS] [DocBook Files]

  dbtoepub converts DocBook <book> and <article>s into to .epub files.

  .epub is defined by the IDPF at www.idpf.org and is made up of 3 standards:
  - Open Publication Structure (OPS)
  - Open Packaging Format (OPF) 
  - Open Container Format (OCF)

  Specific options:
      -d, --debug                      Show debugging output.
      -h, --help                       Display usage info
      -v, --verbose                    Make output verbose


----------------------------------------------------------------------
Validation
----------------------------------------------------------------------

The epubcheck project provides limited validation for .epub documents. 
See http://code.google.com/p/epubcheck/ for details.

----------------------------------------------------------------------
Copyright information
----------------------------------------------------------------------
See the accompanying file named COPYING.

See webhelp/docs/index.html for more information about the webhelp
indexer and the webhelp output format. See webhelp/docs/index.html for
more information about the webhelp indexer and the webhelp output
format.
#![Boost.Atomic](doc/logo.png)

Boost.Atomic, part of collection of the [Boost C++ Libraries](http://github.com/boostorg), implements atomic operations for various CPU architectures, reflecting the standard interface defined in C++11.

### Directories

* **build** - Boost.Atomic build scripts
* **doc** - QuickBook documentation sources
* **include** - Interface headers of Boost.Atomic
* **src** - Compilable source code of Boost.Atomic
* **test** - Boost.Atomic unit tests

### More information

* [Documentation](http://boost.org/libs/atomic)

### License

Distributed under the [Boost Software License, Version 1.0](http://www.boost.org/LICENSE_1_0.txt).
README for the DocBook XML DTD

For more information about DocBook, please see

  http://www.oasis-open.org/docbook/

Please send all questions, comments, concerns, and bug reports to the
DocBook mailing list: docbook@lists.oasis-open.org
XML Entity Declarations for Characters

The character entity sets distributed with DocBook XML are direct
copies of the official entities located at

  http://www.w3.org/2003/entities/

They are distributed for historical compatibility and user convenience.
The DocBook Technical Committee no longer attempts to maintain these
definitions and will periodically update them from the W3C site if and
as they are updated there.

Please direct all questions or comments about the entities to the
individuals or working groups who maintain the official sets.
----------------------------------------------------------------------
              README file for the DocBook XSL Stylesheets
----------------------------------------------------------------------
$Id: README 8032 2008-06-01 21:07:20Z abdelazer $

These are XSL stylesheets for transforming DocBook XML document
instances into various output formats.

This README file provides only very minimal documentation on using
the stylesheets. For more complete information, see Bob Stayton's
book "DocBook XSL: The Complete Guide", available online at:

  http://www.sagehill.net/docbookxsl/

----------------------------------------------------------------------
Installation
----------------------------------------------------------------------
See the INSTALL file for information about installing this release.

----------------------------------------------------------------------
How to use the stylesheets
----------------------------------------------------------------------
The base canonical URI for these stylesheets is:

  http://docbook.sourceforge.net/release/xsl/current/

You call any of the stylesheets in this distribution by doing one
of the following:

  - Use the base canonical URI in combination with one of the
    pathnames below. For example, for "chunked" HTML, output:

    http://docbook.sourceforge.net/release/xsl/current/html/chunk.xsl

    If your system has a working XML Catalog or SGML Catalog setup
    (most Linux systems do), then that URI will automatically be
    resolved and replaced with a local pathname on your system.

  - Use a "real" local system base path in combination with one of
    the pathnames below. For example, for "chunked" HTML, output:

    /usr/share/xml/docbook/stylesheet/nwalsh/html/chunk.xsl

To transform documents created with the standard DocBook
schema/DTD, use one of the following stylesheets:

  fo/docbook.xsl              - for XSL-FO

  html/docbook.xsl            - for HTML (as a single file)
  html/chunk.xsl              - for HTML (chunked into multiple files)
  html/onechunk.xsl           - for HTML (chunked output in single file)

  xhtml/*.xsl                 - for XHTML versions of the above

  xhtml-1_1/*.xsl             - for XHTML 1.1 versions of the above

  epub/docbook.xsl            - for .epub 

  htmlhelp/htmlhelp.xsl       - for HTML Help
  javahelp/javahelp.xsl       - for JavaHelp
  eclipse/eclipse.xsl         - for Eclipse Help

  manpages/docbook.xsl        - for groff/nroff man pages[1]
  [1] more information at http://wiki.docbook.org/topic/ManPages

  */profile-*                 - single-pass-profiling versions of all above

  roundtrip/*.xsl             - for DocBook to WordML, etc., to DocBook

To transform documents created with the DocBook Slides schema/DTD,
use one of the following stylesheets:

  slides/html/*.xsl           - for HTML slides of various kinds
  slides/xhtml/*.xsl          - for XHTML slides of various kinds
  slides/fo/plain.xsl         - for XSL-FO slides
  slides/htmlhelp/...         - for HTML Help slides

To transform documents created with the DocBook Website
schema/DTD, use one of the following stylesheets:

  website/website.xsl         - for non-tabular, non-chunked output
  website/tabular.xsl         - for tabular, non-chunked output
  website/chunk-*             - for chunked output

To generate a titlepage customization layer from a titlepage spec:

  template/titlepage.xsl

For details about creating titlepage spec files and generating and
using titlepage customization layers, see "DocBook XSL: The
Complete Guide" <http://www.sagehill.net/docbookxsl/>

----------------------------------------------------------------------
Manifest
----------------------------------------------------------------------
AUTHORS       contact information
BUGS          about known problems
COPYING       copyright information
INSTALL       installation instructions
README        this file
RELEASE.*     per-release cumulative summaries of user-visible changes
TODO          about planned features not yet implemented
VERSION       release metadata, including the current version
              number (note that the VERSION file is an XSL stylesheet)
NEWS          changes since the last public release (for a cumulative list of
              changes, see the ChangeHistory.xml file)

common/       code used among several output formats (HTML, FO, manpages,...)
docsrc/       documentation sources
eclipse/      for producing Eclipse Help
epub/         for producing .epub
extensions/   DocBook XSL Java extensions
fo/           for producing XSL-FO
highlighting  files used for adding source-code syntax highlighting in output
html/         for producing HTML
htmlhelp/     for producing HTML Help
images/       images used in callouts and graphical admonitions
javahelp/     for producing Java Help
lib/          utility stylesheets with schema-independent functions
manpages/     for producing groff/troff man pages
profiling/    for profiling (omitting/including conditional text)
roundtrip/    for "round trip" conversion among DocBook and
              various word-processor formats (WordML, etc.)
slides/       for producing slides output (from Slides source)
template/     templates for building stylesheet customization layers
tools/        assorted supplementary tools
website/      for producing website output (from Website source)
xhtml/        for producing XHTML
xhtml-1_1/    for producing (stricter) XHTML 1.1

----------------------------------------------------------------------
Changes
----------------------------------------------------------------------
See the NEWS file for changes made since the previous release.

See the RELEASE-NOTES.html or RELEASE-NOTES.txt or RELEASE-NOTES.pdf
files for per-release cumulative summaries of significant
user-visible changes.

For online access to a hyperlinked view of all changes made over
the entire history of the codebase, see the following:

  http://docbook.svn.sourceforge.net/viewvc/docbook/trunk/xsl/?view=log

WARNING: That above change history is a very long list and may
take a long time to load/download.

You can also create an XML-formatted "ChangeHistory.xml" copy of
the complete change history for the codebase by running the
following commands:

  svn checkout https://docbook.svn.sf.net/svnroot/docbook/trunk/xsl
  svn log --xml --verbose xsl > ChangeHistory.xml

----------------------------------------------------------------------
Copyright information
----------------------------------------------------------------------
See the accompanying file named COPYING.
To use the syntax higlighting extension with DocBook-XSL 1.74.3+, you must:
1. Use a processor that works with the extension: Saxon 6 or Xalan-J.
2. Add the latest version of xslthl-2.X.X.jar to your classpath.
3. Set the highlight.source parameter to 1.
4. Import into your customization one of the following stylesheet module:
  * html/highlight.xsl
  * xhtml/highlight.xsl
  * xhtml-1_1/highlight.xsl
  * fo/highlight.xsl
5. Use that customiztion layer.


Note: Saxon 8.5 or later is also supported, but since it is an XSLT 2.0
processor it is not guaranteed to work with DocBook-XSL in all
circumstances. 

----------------------------------------------------------------------
              README file for the DocBook XSL Stylesheets
----------------------------------------------------------------------

These are XSL stylesheets for transforming DocBook XML document
instances into .epub format.

.epub is an open standard of the The International Digital Publishing Forum (IDPF), 
a the trade and standards association for the digital publishing industry. 

An alpha-quality reference implementation (dbtoepub) for a DocBook to .epub 
converter (written in Ruby) is available under bin/. 

From http://idpf.org
  What is EPUB, .epub, OPS/OCF & OEB?

  ".epub" is the file extension of an XML format for reflowable digital 
  books and publications.  ".epub" is composed of three open standards, 
  the Open Publication Structure (OPS), Open Packaging Format (OPF) and 
  Open Container Format (OCF), produced by the IDPF. "EPUB" allows 
  publishers to produce and send a single digital publication file 
  through distribution and offers consumers interoperability between 
  software/hardware for unencrypted reflowable digital books and other 
  publications. The Open eBook Publication Structure or "OEB", 
  originally produced in 1999, is the precursor to OPS. 

----------------------------------------------------------------------
.epub Constraints 
----------------------------------------------------------------------

.epub does not support all of the image formats that DocBook supports.
When an image is available in an accepted format, it will be used. The
accepted @formats are: 'GIF','GIF87a','GIF89a','JPEG','JPG','PNG','SVG'
A mime-type for the image will be guessed from the file extension, 
which may not work if your file extensions are non-standard.

Non-supported elements:
  * <mediaobjectco> 
  * <inlinegraphic>, <graphic>, <textdata>, <imagedata> with text/XML 
    @filerefs
  * <olink>
  * <cmdsynopsis> in lists (generic XHTML rendering inability)
  * <footnote><para><programlisting> (just make your programlistings 
    siblings, rather than descendents of paras)

----------------------------------------------------------------------
dbtoepub Reference Implementation
----------------------------------------------------------------------

An alpha-quality DocBook to .epub conversion program, dbtoepub, is provided
in bin/dbtoepub. 

This tool requires:
 - 'xsltproc' in your PATH
 - 'zip' in your PATH
 - Ruby 1.8.4+

Windows compatibility has not been extensively tested; bug reports encouraged.
[See http://www.zlatkovic.com/libxml.en.html and http://unxutils.sourceforge.net/]

$ dbtoepub --help
  Usage: dbtoepub [OPTIONS] [DocBook Files]

  dbtoepub converts DocBook <book> and <article>s into to .epub files.

  .epub is defined by the IDPF at www.idpf.org and is made up of 3 standards:
  - Open Publication Structure (OPS)
  - Open Packaging Format (OPF) 
  - Open Container Format (OCF)

  Specific options:
      -d, --debug                      Show debugging output.
      -h, --help                       Display usage info
      -v, --verbose                    Make output verbose


----------------------------------------------------------------------
Validation
----------------------------------------------------------------------

The epubcheck project provides limited validation for .epub documents. 
See http://code.google.com/p/epubcheck/ for details.

----------------------------------------------------------------------
Copyright information
----------------------------------------------------------------------
See the accompanying file named COPYING.


# Google Test #

[![Build Status](https://travis-ci.org/google/googletest.svg?branch=master)](https://travis-ci.org/google/googletest)
[![Build status](https://ci.appveyor.com/api/projects/status/4o38plt0xbo1ubc8/branch/master?svg=true)](https://ci.appveyor.com/project/BillyDonahue/googletest/branch/master)

Welcome to **Google Test**, Google's C++ test framework!

This repository is a merger of the formerly separate GoogleTest and
GoogleMock projects. These were so closely related that it makes sense to
maintain and release them together.

Please see the project page above for more information as well as the
mailing list for questions, discussions, and development.  There is
also an IRC channel on OFTC (irc.oftc.net) #gtest available.  Please
join us!

Getting started information for **Google Test** is available in the 
[Google Test Primer](googletest/docs/Primer.md) documentation.

**Google Mock** is an extension to Google Test for writing and using C++ mock
classes.  See the separate [Google Mock documentation](googlemock/README.md).

More detailed documentation for googletest (including build instructions) are
in its interior [googletest/README.md](googletest/README.md) file.

## Features ##

  * An [XUnit](https://en.wikipedia.org/wiki/XUnit) test framework.
  * Test discovery.
  * A rich set of assertions.
  * User-defined assertions.
  * Death tests.
  * Fatal and non-fatal failures.
  * Value-parameterized tests.
  * Type-parameterized tests.
  * Various options for running the tests.
  * XML test report generation.

## Platforms ##

Google test has been used on a variety of platforms:

  * Linux
  * Mac OS X
  * Windows
  * Cygwin
  * MinGW
  * Windows Mobile
  * Symbian

## Who Is Using Google Test? ##

In addition to many internal projects at Google, Google Test is also used by
the following notable projects:

  * The [Chromium projects](http://www.chromium.org/) (behind the Chrome
    browser and Chrome OS).
  * The [LLVM](http://llvm.org/) compiler.
  * [Protocol Buffers](https://github.com/google/protobuf), Google's data
    interchange format.
  * The [OpenCV](http://opencv.org/) computer vision library.

## Related Open Source Projects ##

[Google Test UI](https://github.com/ospector/gtest-gbar) is test runner that runs
your test binary, allows you to track its progress via a progress bar, and
displays a list of test failures. Clicking on one shows failure text. Google
Test UI is written in C#.

[GTest TAP Listener](https://github.com/kinow/gtest-tap-listener) is an event
listener for Google Test that implements the
[TAP protocol](https://en.wikipedia.org/wiki/Test_Anything_Protocol) for test
result output. If your test runner understands TAP, you may find it useful.

## Requirements ##

Google Test is designed to have fairly minimal requirements to build
and use with your projects, but there are some.  Currently, we support
Linux, Windows, Mac OS X, and Cygwin.  We will also make our best
effort to support other platforms (e.g. Solaris, AIX, and z/OS).
However, since core members of the Google Test project have no access
to these platforms, Google Test may have outstanding issues there.  If
you notice any problems on your platform, please notify
<googletestframework@googlegroups.com>. Patches for fixing them are
even more welcome!

### Linux Requirements ###

These are the base requirements to build and use Google Test from a source
package (as described below):

  * GNU-compatible Make or gmake
  * POSIX-standard shell
  * POSIX(-2) Regular Expressions (regex.h)
  * A C++98-standard-compliant compiler

### Windows Requirements ###

  * Microsoft Visual C++ v7.1 or newer

### Cygwin Requirements ###

  * Cygwin v1.5.25-14 or newer

### Mac OS X Requirements ###

  * Mac OS X v10.4 Tiger or newer
  * Xcode Developer Tools

### Requirements for Contributors ###

We welcome patches.  If you plan to contribute a patch, you need to
build Google Test and its own tests from a git checkout (described
below), which has further requirements:

  * [Python](https://www.python.org/) v2.3 or newer (for running some of
    the tests and re-generating certain source files from templates)
  * [CMake](https://cmake.org/) v2.6.4 or newer

## Regenerating Source Files ##

Some of Google Test's source files are generated from templates (not
in the C++ sense) using a script.
For example, the
file include/gtest/internal/gtest-type-util.h.pump is used to generate
gtest-type-util.h in the same directory.

You don't need to worry about regenerating the source files
unless you need to modify them.  You would then modify the
corresponding `.pump` files and run the '[pump.py](googletest/scripts/pump.py)'
generator script.  See the [Pump Manual](googletest/docs/PumpManual.md).

### Contributing Code ###

We welcome patches.  Please read the
[Developer's Guide](googletest/docs/DevGuide.md)
for how you can contribute. In particular, make sure you have signed
the Contributor License Agreement, or we won't be able to accept the
patch.

Happy testing!

### Generic Build Instructions ###

#### Setup ####

To build Google Test and your tests that use it, you need to tell your
build system where to find its headers and source files.  The exact
way to do it depends on which build system you use, and is usually
straightforward.

#### Build ####

Suppose you put Google Test in directory `${GTEST_DIR}`.  To build it,
create a library build target (or a project as called by Visual Studio
and Xcode) to compile

    ${GTEST_DIR}/src/gtest-all.cc

with `${GTEST_DIR}/include` in the system header search path and `${GTEST_DIR}`
in the normal header search path.  Assuming a Linux-like system and gcc,
something like the following will do:

    g++ -isystem ${GTEST_DIR}/include -I${GTEST_DIR} \
        -pthread -c ${GTEST_DIR}/src/gtest-all.cc
    ar -rv libgtest.a gtest-all.o

(We need `-pthread` as Google Test uses threads.)

Next, you should compile your test source file with
`${GTEST_DIR}/include` in the system header search path, and link it
with gtest and any other necessary libraries:

    g++ -isystem ${GTEST_DIR}/include -pthread path/to/your_test.cc libgtest.a \
        -o your_test

As an example, the make/ directory contains a Makefile that you can
use to build Google Test on systems where GNU make is available
(e.g. Linux, Mac OS X, and Cygwin).  It doesn't try to build Google
Test's own tests.  Instead, it just builds the Google Test library and
a sample test.  You can use it as a starting point for your own build
script.

If the default settings are correct for your environment, the
following commands should succeed:

    cd ${GTEST_DIR}/make
    make
    ./sample1_unittest

If you see errors, try to tweak the contents of `make/Makefile` to make
them go away.  There are instructions in `make/Makefile` on how to do
it.

### Using CMake ###

Google Test comes with a CMake build script (
[CMakeLists.txt](CMakeLists.txt)) that can be used on a wide range of platforms ("C" stands for
cross-platform.). If you don't have CMake installed already, you can
download it for free from <http://www.cmake.org/>.

CMake works by generating native makefiles or build projects that can
be used in the compiler environment of your choice.  The typical
workflow starts with:

    mkdir mybuild       # Create a directory to hold the build output.
    cd mybuild
    cmake ${GTEST_DIR}  # Generate native build scripts.

If you want to build Google Test's samples, you should replace the
last command with

    cmake -Dgtest_build_samples=ON ${GTEST_DIR}

If you are on a \*nix system, you should now see a Makefile in the
current directory.  Just type 'make' to build gtest.

If you use Windows and have Visual Studio installed, a `gtest.sln` file
and several `.vcproj` files will be created.  You can then build them
using Visual Studio.

On Mac OS X with Xcode installed, a `.xcodeproj` file will be generated.

### Legacy Build Scripts ###

Before settling on CMake, we have been providing hand-maintained build
projects/scripts for Visual Studio, Xcode, and Autotools.  While we
continue to provide them for convenience, they are not actively
maintained any more.  We highly recommend that you follow the
instructions in the previous two sections to integrate Google Test
with your existing build system.

If you still need to use the legacy build scripts, here's how:

The msvc\ folder contains two solutions with Visual C++ projects.
Open the `gtest.sln` or `gtest-md.sln` file using Visual Studio, and you
are ready to build Google Test the same way you build any Visual
Studio project.  Files that have names ending with -md use DLL
versions of Microsoft runtime libraries (the /MD or the /MDd compiler
option).  Files without that suffix use static versions of the runtime
libraries (the /MT or the /MTd option).  Please note that one must use
the same option to compile both gtest and the test code.  If you use
Visual Studio 2005 or above, we recommend the -md version as /MD is
the default for new projects in these versions of Visual Studio.

On Mac OS X, open the `gtest.xcodeproj` in the `xcode/` folder using
Xcode.  Build the "gtest" target.  The universal binary framework will
end up in your selected build directory (selected in the Xcode
"Preferences..." -> "Building" pane and defaults to xcode/build).
Alternatively, at the command line, enter:

    xcodebuild

This will build the "Release" configuration of gtest.framework in your
default build location.  See the "xcodebuild" man page for more
information about building different configurations and building in
different locations.

If you wish to use the Google Test Xcode project with Xcode 4.x and
above, you need to either:

 * update the SDK configuration options in xcode/Config/General.xconfig.
   Comment options `SDKROOT`, `MACOS_DEPLOYMENT_TARGET`, and `GCC_VERSION`. If
   you choose this route you lose the ability to target earlier versions
   of MacOS X.
 * Install an SDK for an earlier version. This doesn't appear to be
   supported by Apple, but has been reported to work
   (http://stackoverflow.com/questions/5378518).

### Tweaking Google Test ###

Google Test can be used in diverse environments.  The default
configuration may not work (or may not work well) out of the box in
some environments.  However, you can easily tweak Google Test by
defining control macros on the compiler command line.  Generally,
these macros are named like `GTEST_XYZ` and you define them to either 1
or 0 to enable or disable a certain feature.

We list the most frequently used macros below.  For a complete list,
see file [include/gtest/internal/gtest-port.h](include/gtest/internal/gtest-port.h).

### Choosing a TR1 Tuple Library ###

Some Google Test features require the C++ Technical Report 1 (TR1)
tuple library, which is not yet available with all compilers.  The
good news is that Google Test implements a subset of TR1 tuple that's
enough for its own need, and will automatically use this when the
compiler doesn't provide TR1 tuple.

Usually you don't need to care about which tuple library Google Test
uses.  However, if your project already uses TR1 tuple, you need to
tell Google Test to use the same TR1 tuple library the rest of your
project uses, or the two tuple implementations will clash.  To do
that, add

    -DGTEST_USE_OWN_TR1_TUPLE=0

to the compiler flags while compiling Google Test and your tests.  If
you want to force Google Test to use its own tuple library, just add

    -DGTEST_USE_OWN_TR1_TUPLE=1

to the compiler flags instead.

If you don't want Google Test to use tuple at all, add

    -DGTEST_HAS_TR1_TUPLE=0

and all features using tuple will be disabled.

### Multi-threaded Tests ###

Google Test is thread-safe where the pthread library is available.
After `#include "gtest/gtest.h"`, you can check the `GTEST_IS_THREADSAFE`
macro to see whether this is the case (yes if the macro is `#defined` to
1, no if it's undefined.).

If Google Test doesn't correctly detect whether pthread is available
in your environment, you can force it with

    -DGTEST_HAS_PTHREAD=1

or

    -DGTEST_HAS_PTHREAD=0

When Google Test uses pthread, you may need to add flags to your
compiler and/or linker to select the pthread library, or you'll get
link errors.  If you use the CMake script or the deprecated Autotools
script, this is taken care of for you.  If you use your own build
script, you'll need to read your compiler and linker's manual to
figure out what flags to add.

### As a Shared Library (DLL) ###

Google Test is compact, so most users can build and link it as a
static library for the simplicity.  You can choose to use Google Test
as a shared library (known as a DLL on Windows) if you prefer.

To compile *gtest* as a shared library, add

    -DGTEST_CREATE_SHARED_LIBRARY=1

to the compiler flags.  You'll also need to tell the linker to produce
a shared library instead - consult your linker's manual for how to do
it.

To compile your *tests* that use the gtest shared library, add

    -DGTEST_LINKED_AS_SHARED_LIBRARY=1

to the compiler flags.

Note: while the above steps aren't technically necessary today when
using some compilers (e.g. GCC), they may become necessary in the
future, if we decide to improve the speed of loading the library (see
<http://gcc.gnu.org/wiki/Visibility> for details).  Therefore you are
recommended to always add the above flags when using Google Test as a
shared library.  Otherwise a future release of Google Test may break
your build script.

### Avoiding Macro Name Clashes ###

In C++, macros don't obey namespaces.  Therefore two libraries that
both define a macro of the same name will clash if you `#include` both
definitions.  In case a Google Test macro clashes with another
library, you can force Google Test to rename its macro to avoid the
conflict.

Specifically, if both Google Test and some other code define macro
FOO, you can add

    -DGTEST_DONT_DEFINE_FOO=1

to the compiler flags to tell Google Test to change the macro's name
from `FOO` to `GTEST_FOO`.  Currently `FOO` can be `FAIL`, `SUCCEED`,
or `TEST`.  For example, with `-DGTEST_DONT_DEFINE_TEST=1`, you'll
need to write

    GTEST_TEST(SomeTest, DoesThis) { ... }

instead of

    TEST(SomeTest, DoesThis) { ... }

in order to define a test.

## Developing Google Test ##

This section discusses how to make your own changes to Google Test.

### Testing Google Test Itself ###

To make sure your changes work as intended and don't break existing
functionality, you'll want to compile and run Google Test's own tests.
For that you can use CMake:

    mkdir mybuild
    cd mybuild
    cmake -Dgtest_build_tests=ON ${GTEST_DIR}

Make sure you have Python installed, as some of Google Test's tests
are written in Python.  If the cmake command complains about not being
able to find Python (`Could NOT find PythonInterp (missing:
PYTHON_EXECUTABLE)`), try telling it explicitly where your Python
executable can be found:

    cmake -DPYTHON_EXECUTABLE=path/to/python -Dgtest_build_tests=ON ${GTEST_DIR}

Next, you can build Google Test and all of its own tests.  On \*nix,
this is usually done by 'make'.  To run the tests, do

    make test

All tests should pass.

Normally you don't need to worry about regenerating the source files,
unless you need to modify them.  In that case, you should modify the
corresponding .pump files instead and run the pump.py Python script to
regenerate them.  You can find pump.py in the [scripts/](scripts/) directory.
Read the [Pump manual](docs/PumpManual.md) for how to use it.
## Google Mock ##

The Google C++ mocking framework.

### Overview ###

Google's framework for writing and using C++ mock classes.
It can help you derive better designs of your system and write better tests.

It is inspired by:

  * [jMock](http://www.jmock.org/),
  * [EasyMock](http://www.easymock.org/), and
  * [Hamcrest](http://code.google.com/p/hamcrest/),

and designed with C++'s specifics in mind.

Google mock:

  * lets you create mock classes trivially using simple macros.
  * supports a rich set of matchers and actions.
  * handles unordered, partially ordered, or completely ordered expectations.
  * is extensible by users.

We hope you find it useful!

### Features ###

  * Provides a declarative syntax for defining mocks.
  * Can easily define partial (hybrid) mocks, which are a cross of real
    and mock objects.
  * Handles functions of arbitrary types and overloaded functions.
  * Comes with a rich set of matchers for validating function arguments.
  * Uses an intuitive syntax for controlling the behavior of a mock.
  * Does automatic verification of expectations (no record-and-replay needed).
  * Allows arbitrary (partial) ordering constraints on
    function calls to be expressed,.
  * Lets a user extend it by defining new matchers and actions.
  * Does not use exceptions.
  * Is easy to learn and use.

Please see the project page above for more information as well as the
mailing list for questions, discussions, and development.  There is
also an IRC channel on OFTC (irc.oftc.net) #gtest available.  Please
join us!

Please note that code under [scripts/generator](scripts/generator/) is
from [cppclean](http://code.google.com/p/cppclean/) and released under
the Apache License, which is different from Google Mock's license.

## Getting Started ##

If you are new to the project, we suggest that you read the user
documentation in the following order:

  * Learn the [basics](../googletest/docs/Primer.md) of
    Google Test, if you choose to use Google Mock with it (recommended).
  * Read [Google Mock for Dummies](docs/ForDummies.md).
  * Read the instructions below on how to build Google Mock.

You can also watch Zhanyong's [talk](http://www.youtube.com/watch?v=sYpCyLI47rM) on Google Mock's usage and implementation.

Once you understand the basics, check out the rest of the docs:

  * [CheatSheet](docs/CheatSheet.md) - all the commonly used stuff
    at a glance.
  * [CookBook](docs/CookBook.md) - recipes for getting things done,
    including advanced techniques.

If you need help, please check the
[KnownIssues](docs/KnownIssues.md) and
[FrequentlyAskedQuestions](docs/FrequentlyAskedQuestions.md) before
posting a question on the
[discussion group](http://groups.google.com/group/googlemock).


### Using Google Mock Without Google Test ###

Google Mock is not a testing framework itself.  Instead, it needs a
testing framework for writing tests.  Google Mock works seamlessly
with [Google Test](http://code.google.com/p/googletest/), but
you can also use it with [any C++ testing framework](googlemock/ForDummies.md#Using_Google_Mock_with_Any_Testing_Framework).

### Requirements for End Users ###

Google Mock is implemented on top of [Google Test](
http://github.com/google/googletest/), and depends on it.
You must use the bundled version of Google Test when using Google Mock.

You can also easily configure Google Mock to work with another testing
framework, although it will still need Google Test.  Please read
["Using_Google_Mock_with_Any_Testing_Framework"](
    docs/ForDummies.md#Using_Google_Mock_with_Any_Testing_Framework)
for instructions.

Google Mock depends on advanced C++ features and thus requires a more
modern compiler. The following are needed to use Google Mock:

#### Linux Requirements ####

  * GNU-compatible Make or "gmake"
  * POSIX-standard shell
  * POSIX(-2) Regular Expressions (regex.h)
  * C++98-standard-compliant compiler (e.g. GCC 3.4 or newer)

#### Windows Requirements ####

  * Microsoft Visual C++ 8.0 SP1 or newer

#### Mac OS X Requirements ####

  * Mac OS X 10.4 Tiger or newer
  * Developer Tools Installed

### Requirements for Contributors ###

We welcome patches. If you plan to contribute a patch, you need to
build Google Mock and its tests, which has further requirements:

  * Automake version 1.9 or newer
  * Autoconf version 2.59 or newer
  * Libtool / Libtoolize
  * Python version 2.3 or newer (for running some of the tests and
    re-generating certain source files from templates)

### Building Google Mock ###

#### Preparing to Build (Unix only) ####

If you are using a Unix system and plan to use the GNU Autotools build
system to build Google Mock (described below), you'll need to
configure it now.

To prepare the Autotools build system:

    cd googlemock
    autoreconf -fvi

To build Google Mock and your tests that use it, you need to tell your
build system where to find its headers and source files.  The exact
way to do it depends on which build system you use, and is usually
straightforward.

This section shows how you can integrate Google Mock into your
existing build system.

Suppose you put Google Mock in directory `${GMOCK_DIR}` and Google Test
in `${GTEST_DIR}` (the latter is `${GMOCK_DIR}/gtest` by default).  To
build Google Mock, create a library build target (or a project as
called by Visual Studio and Xcode) to compile

    ${GTEST_DIR}/src/gtest-all.cc and ${GMOCK_DIR}/src/gmock-all.cc

with

    ${GTEST_DIR}/include and ${GMOCK_DIR}/include

in the system header search path, and

    ${GTEST_DIR} and ${GMOCK_DIR}

in the normal header search path.  Assuming a Linux-like system and gcc,
something like the following will do:

    g++ -isystem ${GTEST_DIR}/include -I${GTEST_DIR} \
        -isystem ${GMOCK_DIR}/include -I${GMOCK_DIR} \
        -pthread -c ${GTEST_DIR}/src/gtest-all.cc
    g++ -isystem ${GTEST_DIR}/include -I${GTEST_DIR} \
        -isystem ${GMOCK_DIR}/include -I${GMOCK_DIR} \
        -pthread -c ${GMOCK_DIR}/src/gmock-all.cc
    ar -rv libgmock.a gtest-all.o gmock-all.o

(We need -pthread as Google Test and Google Mock use threads.)

Next, you should compile your test source file with
${GTEST\_DIR}/include and ${GMOCK\_DIR}/include in the header search
path, and link it with gmock and any other necessary libraries:

    g++ -isystem ${GTEST_DIR}/include -isystem ${GMOCK_DIR}/include \
        -pthread path/to/your_test.cc libgmock.a -o your_test

As an example, the make/ directory contains a Makefile that you can
use to build Google Mock on systems where GNU make is available
(e.g. Linux, Mac OS X, and Cygwin).  It doesn't try to build Google
Mock's own tests.  Instead, it just builds the Google Mock library and
a sample test.  You can use it as a starting point for your own build
script.

If the default settings are correct for your environment, the
following commands should succeed:

    cd ${GMOCK_DIR}/make
    make
    ./gmock_test

If you see errors, try to tweak the contents of
[make/Makefile](make/Makefile) to make them go away.

### Windows ###

The msvc/2005 directory contains VC++ 2005 projects and the msvc/2010
directory contains VC++ 2010 projects for building Google Mock and
selected tests.

Change to the appropriate directory and run "msbuild gmock.sln" to
build the library and tests (or open the gmock.sln in the MSVC IDE).
If you want to create your own project to use with Google Mock, you'll
have to configure it to use the `gmock_config` propety sheet.  For that:

 * Open the Property Manager window (View | Other Windows | Property Manager)
 * Right-click on your project and select "Add Existing Property Sheet..."
 * Navigate to `gmock_config.vsprops` or `gmock_config.props` and select it.
 * In Project Properties | Configuration Properties | General | Additional
   Include Directories, type <path to Google Mock>/include.

### Tweaking Google Mock ###

Google Mock can be used in diverse environments.  The default
configuration may not work (or may not work well) out of the box in
some environments.  However, you can easily tweak Google Mock by
defining control macros on the compiler command line.  Generally,
these macros are named like `GTEST_XYZ` and you define them to either 1
or 0 to enable or disable a certain feature.

We list the most frequently used macros below.  For a complete list,
see file [${GTEST\_DIR}/include/gtest/internal/gtest-port.h](
../googletest/include/gtest/internal/gtest-port.h).

### Choosing a TR1 Tuple Library ###

Google Mock uses the C++ Technical Report 1 (TR1) tuple library
heavily.  Unfortunately TR1 tuple is not yet widely available with all
compilers.  The good news is that Google Test 1.4.0+ implements a
subset of TR1 tuple that's enough for Google Mock's need.  Google Mock
will automatically use that implementation when the compiler doesn't
provide TR1 tuple.

Usually you don't need to care about which tuple library Google Test
and Google Mock use.  However, if your project already uses TR1 tuple,
you need to tell Google Test and Google Mock to use the same TR1 tuple
library the rest of your project uses, or the two tuple
implementations will clash.  To do that, add

    -DGTEST_USE_OWN_TR1_TUPLE=0

to the compiler flags while compiling Google Test, Google Mock, and
your tests.  If you want to force Google Test and Google Mock to use
their own tuple library, just add

    -DGTEST_USE_OWN_TR1_TUPLE=1

to the compiler flags instead.

If you want to use Boost's TR1 tuple library with Google Mock, please
refer to the Boost website (http://www.boost.org/) for how to obtain
it and set it up.

### As a Shared Library (DLL) ###

Google Mock is compact, so most users can build and link it as a static
library for the simplicity.  Google Mock can be used as a DLL, but the
same DLL must contain Google Test as well.  See
[Google Test's README][gtest_readme]
for instructions on how to set up necessary compiler settings.

### Tweaking Google Mock ###

Most of Google Test's control macros apply to Google Mock as well.
Please see [Google Test's README][gtest_readme] for how to tweak them.

### Upgrading from an Earlier Version ###

We strive to keep Google Mock releases backward compatible.
Sometimes, though, we have to make some breaking changes for the
users' long-term benefits.  This section describes what you'll need to
do if you are upgrading from an earlier version of Google Mock.

#### Upgrading from 1.1.0 or Earlier ####

You may need to explicitly enable or disable Google Test's own TR1
tuple library.  See the instructions in section "[Choosing a TR1 Tuple
Library](../googletest/#choosing-a-tr1-tuple-library)".

#### Upgrading from 1.4.0 or Earlier ####

On platforms where the pthread library is available, Google Test and
Google Mock use it in order to be thread-safe.  For this to work, you
may need to tweak your compiler and/or linker flags.  Please see the
"[Multi-threaded Tests](../googletest#multi-threaded-tests
)" section in file Google Test's README for what you may need to do.

If you have custom matchers defined using `MatcherInterface` or
`MakePolymorphicMatcher()`, you'll need to update their definitions to
use the new matcher API (
[monomorphic](http://code.google.com/p/googlemock/wiki/CookBook#Writing_New_Monomorphic_Matchers),
[polymorphic](http://code.google.com/p/googlemock/wiki/CookBook#Writing_New_Polymorphic_Matchers)).
Matchers defined using `MATCHER()` or `MATCHER_P*()` aren't affected.

### Developing Google Mock ###

This section discusses how to make your own changes to Google Mock.

#### Testing Google Mock Itself ####

To make sure your changes work as intended and don't break existing
functionality, you'll want to compile and run Google Test's own tests.
For that you'll need Autotools.  First, make sure you have followed
the instructions above to configure Google Mock.
Then, create a build output directory and enter it.  Next,

    ${GMOCK_DIR}/configure  # try --help for more info

Once you have successfully configured Google Mock, the build steps are
standard for GNU-style OSS packages.

    make        # Standard makefile following GNU conventions
    make check  # Builds and runs all tests - all should pass.

Note that when building your project against Google Mock, you are building
against Google Test as well.  There is no need to configure Google Test
separately.

#### Contributing a Patch ####

We welcome patches.
Please read the [Developer's Guide](docs/DevGuide.md)
for how you can contribute. In particular, make sure you have signed
the Contributor License Agreement, or we won't be able to accept the
patch.

Happy testing!

[gtest_readme]: ../googletest/README.md "googletest"
Goal:
-----
  CppClean attempts to find problems in C++ source that slow development
  in large code bases, for example various forms of unused code.
  Unused code can be unused functions, methods, data members, types, etc
  to unnecessary #include directives.  Unnecessary #includes can cause
  considerable extra compiles increasing the edit-compile-run cycle.

  The project home page is:   http://code.google.com/p/cppclean/


Features:
---------
 * Find and print C++ language constructs: classes, methods, functions, etc.
 * Find classes with virtual methods, no virtual destructor, and no bases
 * Find global/static data that are potential problems when using threads
 * Unnecessary forward class declarations
 * Unnecessary function declarations
 * Undeclared function definitions
 * (planned) Find unnecessary header files #included
   - No direct reference to anything in the header
   - Header is unnecessary if classes were forward declared instead
 * (planned) Source files that reference headers not directly #included,
   ie, files that rely on a transitive #include from another header
 * (planned) Unused members (private, protected, & public) methods and data
 * (planned) Store AST in a SQL database so relationships can be queried

AST is Abstract Syntax Tree, a representation of parsed source code.
http://en.wikipedia.org/wiki/Abstract_syntax_tree


System Requirements:
--------------------
 * Python 2.4 or later (2.3 probably works too)
 * Works on Windows (untested), Mac OS X, and Unix


How to Run:
-----------
  For all examples, it is assumed that cppclean resides in a directory called
  /cppclean.

  To print warnings for classes with virtual methods, no virtual destructor and
  no base classes:

      /cppclean/run.sh nonvirtual_dtors.py file1.h file2.h file3.cc ...

  To print all the functions defined in header file(s):

      /cppclean/run.sh functions.py file1.h file2.h ...

  All the commands take multiple files on the command line.  Other programs
  include: find_warnings, headers, methods, and types.  Some other programs
  are available, but used primarily for debugging.

  run.sh is a simple wrapper that sets PYTHONPATH to /cppclean and then
  runs the program in /cppclean/cpp/PROGRAM.py.  There is currently
  no equivalent for Windows.  Contributions for a run.bat file
  would be greatly appreciated.


How to Configure:
-----------------
  You can add a siteheaders.py file in /cppclean/cpp to configure where
  to look for other headers (typically -I options passed to a compiler).
  Currently two values are supported:  _TRANSITIVE and GetIncludeDirs.
  _TRANSITIVE should be set to a boolean value (True or False) indicating
  whether to transitively process all header files.  The default is False.

  GetIncludeDirs is a function that takes a single argument and returns
  a sequence of directories to include.  This can be a generator or
  return a static list.

      def GetIncludeDirs(filename):
          return ['/some/path/with/other/headers']

      # Here is a more complicated example.
      def GetIncludeDirs(filename):
          yield '/path1'
          yield os.path.join('/path2', os.path.dirname(filename))
          yield '/path3'


How to Test:
------------
  For all examples, it is assumed that cppclean resides in a directory called
  /cppclean.  The tests require

  cd /cppclean
  make test
  # To generate expected results after a change:
  make expected


Current Status:
---------------
  The parser works pretty well for header files, parsing about 99% of Google's
  header files.  Anything which inspects structure of C++ source files should
  work reasonably well.  Function bodies are not transformed to an AST,
  but left as tokens.  Much work is still needed on finding unused header files
  and storing an AST in a database.


Non-goals:
----------
 * Parsing all valid C++ source
 * Handling invalid C++ source gracefully
 * Compiling to machine code (or anything beyond an AST)


Contact:
--------
  If you used cppclean, I would love to hear about your experiences
  cppclean@googlegroups.com.  Even if you don't use cppclean, I'd like to
  hear from you.  :-)  (You can contact me directly at:  nnorwitz@gmail.com)

The Google Mock class generator is an application that is part of cppclean.
For more information about cppclean, see the README.cppclean file or
visit http://code.google.com/p/cppclean/

cppclean requires Python 2.3.5 or later.  If you don't have Python installed
on your system, you will also need to install it.  You can download Python
from:  http://www.python.org/download/releases/

To use the Google Mock class generator, you need to call it
on the command line passing the header file and class for which you want
to generate a Google Mock class.

Make sure to install the scripts somewhere in your path.  Then you can
run the program.

  gmock_gen.py header-file.h [ClassName]...

If no ClassNames are specified, all classes in the file are emitted.

To change the indentation from the default of 2, set INDENT in
the environment.  For example to use an indent of 4 spaces:

INDENT=4 gmock_gen.py header-file.h ClassName

This version was made from SVN revision 281 in the cppclean repository.

Known Limitations
-----------------
Not all code will be generated properly.  For example, when mocking templated
classes, the template information is lost.  You will need to add the template
information manually.

Not all permutations of using multiple pointers/references will be rendered
properly.  These will also have to be fixed manually.
