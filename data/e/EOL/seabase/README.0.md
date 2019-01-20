<!-- $Id: readme.html,v 1.14 2005/05/05 13:55:13 coulouri Exp $ -->
<HTML>
<HEAD>
<TITLE>Introduction to the Standalone WWW Blast server</TITLE>
</HEAD>
<BODY LINK="#0000ff" VLINK="#800080" BGCOLOR="#ffffff" ALINK="#660099">

<P><!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML//EN"></P>
<P><HR></P>
<H2 ALIGN="CENTER">Introduction to the Standalone WWW Blast server</H2>
<P><HR></P>
<H3>Index</H3>

<UL>
<LI><A HREF="#Inroduction">Introduction</A> </LI>
<LI><A HREF="#Whatsnew">What's new in this revision?</A> </LI>
<LI><A HREF="#Installation">Installation of the Standalone WWW server</A> </LI>
<LI><A HREF="#Description_of_files">Description of files in the distribution</A> </LI>
<LI><A HREF="#Configuration_of_databases">Configuration of BLAST databases</A> </LI>
<LI><A HREF="#PSI_PHI_Notes">PSI/PHI Blast notes</A> </LI>
<LI><A HREF="#CS_Notes">Client/server versions for Entrez lookup and taxonomy reports</A> </LI>
<LI><a href="#Bl2Seq">Blast 2 sequences</a>
<LI><A HREF="#XML_Output">XML output</A>
<LI><A HREF="#OOF_blastx">Out of Frame BLASTX</A>
<LI><A HREF="#RPS_blast">RPS Blast</A>
<LI><A HREF="#Description_of_tags">Description of tags for main BLAST input page</A> </LI>
<LI><A HREF="#Configuration_file">Server configuration file and logfile</A> </LI>
<LI><A HREF="#Debugging">How to debug WWW Blast programs</A> </LI>
</UL>

<H3><A NAME="Inroduction">Introduction</A> </H3>
<P>This standalone WWW BLAST server suite of programs was designed similar to the regular NCBI BLAST server and such command-line NCBI BLAST programs like "blastall", "blastpgp", "rpsblast" and "megablast". It incorporates most features, which exist in NCBI BLAST programs and should be relatively easy to use. This server does not support any request queuing and load balancing. As soon as the user hits a "Search" button, BLAST starts immediately if entered information is valid. So, this server is not intended to handle large load, which may exist in public service. Such queueing and loadbalancing however may be implemented using such products as Load Sharing Facility - "LSF" from <a href="http://www.platform.com">Platform Computing Corporation</a>. Interface to "LSF" was implemented in NCBI, however this was not included in this suite. Standalone server assumes that users have their own BLAST or RPS-BLAST database(s), that should be searched and want to have a simple WWW interface to such search. It is STRONLY recommended that user have experience in installation and running standalone NCBI BLAST programs. </P>
<P>After files are uncompressed, server is ready to be used immediately. Any customizations to the program are welcomed. The source code for WWW BLAST is now part of the NCBI C toolkit, which can be downloaded from the NCBI FTP web site: <A HREF="ftp://ftp.ncbi.nih.gov/toolbox/ncbi_tools/README.htm">ftp://ftp.ncbi.nih.gov</A> <BR>The compilation of the NCBI C toolkit includes the WWW BLAST executables. The files in the C toolkit most relevant for the WWW BLAST executables are: wwwblast.c, wwwbutl.c, psiblast.c, wblast2.c.</P>
<H3><A NAME="Whatsnew">What's new in this revision?</A></H3>

<TABLE BORDER=1>
<TR VALIGN=top>
<TD> May 10, 2004
<TD>
<UL>
<LI> XML output brought in sync with the text output, masking filtered locations in query sequences.
</UL>
</TR>
<TR VALIGN=top>
<TD> February 2, 2004
<TD>
<UL>
<LI> All source code moved to the NCBI C toolkit.
<LI> Mouseover feature fixed in graphical overview.
<LI> All binaries synchronized with the latest NCBI C toolkit release. All future
releases will be automatically synchronized with future toolkit releases.
<LI> Recompilation procedure changed. WWW BLAST binaries are now compiled as part
of the C toolkit.
</UL>
</TR>
<TR VALIGN=top>
<TD> November 21, 2003
<TD>
<UL>
<LI> Fixed a bug with absent images on PSI-BLAST iterations.
<LI> Removed header and progress messages from XML output. 
<LI> All binaries recompiled with the newest version of the NCBI C toolkit libra
ries.
</UL>
</TR>
<TR VALIGN=top>
<TD> May 9, 2003
<TD>
<UL>
<LI> Cleaned the Makefile for recompiling the sources.
<LI> Added discontiguous Mega BLAST options.
<LI> Added option to choose a subsequence location for query.
<LI> Added option to choose database genetic code.
<LI> All binaries recompiled.
</UL>
</TR>
<TR VALIGN=top>
<TD> April 21, 2003
<TD>
<UL>
<LI> Added instructions for recompilation of binaries from the source code to this readme file.
<LI> Fixed a bug in processing of the configuration file that limited allowed number of databases.
<LI> Added images for the Linkout and UniGene links from the BLAST output.
<LI> Corrected paths to the graphical overview for PSI/PHI BLAST output.
<LI> All binaries recompiled with the newest version of the NCBI C toolkit libraries.
</UL>
</TR>
<TR VALIGN=top>
<TD> February 10, 2003
<TD>
<UL>
<LI> Added support for multi-query XML output.
<LI> All binaries recompiled.
</UL>
</TR>
<TR VALIGN=top>
<TD> December 2, 2002
<TD>
<UL>
<LI> All binaries recompiled with the newest version of the toolkit. 
</UL>
</TR>
<TR VALIGN=top>
<TD> August 6, 2002
<TD>
<UL>
<LI> Recompiled all binaries to include recent bug fixes.
</UL>
</TR>
<TR VALIGN=top>
<TD> June 18, 2002
<TD>
<UL>
<LI> Removed limit on the total length of database names. 
<LI> Removed xmlblast.cgi and other unneeded XML related files. 
<LI> Recompiled all programs.
</UL>
</TR>
<TR VALIGN=top>
<TD> January 11, 2002
<TD>
<UL>
<LI> Removed formatdb, makemat and copymat binaries from the archive - those should be taken from the <a href="ftp://ncbi.nlm.nih.gov/blast/executables">NCBI BLAST executables archive</a>
<LI> Added tabular output format
<LI> Added option to mask lower case in query
</UL>
</TR>
<TR VALIGN=top>
<TD> May, 2 2001 
<TD>
<UL>
<LI> No major changes. All programs have been recompiled and made synchronous to the latest NCBI tookit release.
</UL>
</TR>
<TR VALIGN=top>
<TD> November 3, 2000 
<TD>
<UL>
<LI> <a href="#Bl2Seq">Blast 2 sequences</a> was added
</UL>
</TR><TR VALIGN=top>
<TD> October, 19 2000 
<TD>
<UL>
<LI> <a href="#RPS_blast">RPS Blast</a> was added
<LI> <a href=#OOF_blastx>Out of Frame BLASTX</a> (OOF) now available for testing and suggestions.
</UL>
</TR><TR VALIGN=top>
<TD> September, 28 2000 
<TD>
<UL>
<LI> Added possibility to limit search to results of Entrez query (Regular
     client/server BLAST)
</UL>
</TR><TR VALIGN=top>
<TD> September, 11 2000 
<TD>
<UL>
<LI> Added <A HREF="docs/megablast_readme.html">MEGABLAST</A> search.
<LI> Added possibility to have multiple FASTA query input - batch searches 
     with multiple graphical overviews. (Regular BLAST)
</UL>
</TR><TR VALIGN=top>
<TD> August, 22 2000 
<TD>
<UL>
<LI> Added new advanced statistics to PSI Blast and ability to produce Smith-Waterman alignments
<LI>Added support for XML output.
</UL>
</TR><TR VALIGN=top>
<TD> May, 17 2000 
<TD>
<UL>
<LI>PSI and PHI Blast were added to this distribution
<LI>Added support for client/server interface for gi/accession
     lookups using Entrez
<LI>Added possibility to print Taxonomy reports
<LI>Added option to print alternative alignment with specific color schema
</UL>
</TR><TR VALIGN=top>
<TD> March, 20 2000 
<TD>
<UL>
<LI> Initial revision
</UL>
</TR>
</TABLE>

<H3><A NAME="Installation">Installation of the Standalone WWW server</A></H3>
<P>After downloading the file wwwblast.Your_platform.tar.gz to your computer, place it into document directory of HTTPD server and uncompress it by </P>
<PRE>
    gzip -d wwwblast.Your_platform.tar.gz
    tar -xvpf wwwblast.Your_platform.tar</PRE>
<P>Please note that parameter "p" in tar options is significant - it will preserve file access options stored in the distribution. Temporary directory for BLAST overview images (TmpGifs) should have 777 permission, and logfiles (wwwblast.log and psiblast.log) should have 666. </P>
<P>After you have uncompressed the distribution file, "blast" directory will be created. You can access sample BLAST HTML input forms using URLs:
<UL> 
<LI>http://your_hostname/blast/blast.html
<LI>http://your_hostname/blast/blast_cs.html
<LI>http://your_hostname/blast/psiblast.html
<LI>http://your_hostname/blast/psiblast_cs.html
<LI>http://your_hostname/blast/megablast.html
<LI>http://your_hostname/blast/megablast_cs.html
<LI>http://your_hostname/blast/wblast2.html
<LI>http://your_hostname/blast/wblast2_cs.html
</UL>
This distribution comes with 2 BLAST databases: "test_aa_db" - sample protein database and "test_na_db" - sample nucleotide database. These databases are configured to be searchable immediately with compatible BLAST programs. </P>
<H3><A NAME="Description_of_files">Description of files in the distribution</A></H3>

<UL>
<LI>Root directory (<B>./blast</B>): </LI></UL>

Files with suffix "*_cs.*" are analogous to the files without such suffix,
with added capability to make client/server Entrez lookups for sequence
gis and accessions.
<P>
<TABLE CELLSPACING=0 BORDER=0>
<TR><TD VALIGN="MIDDLE">
<P><I>blast.cgi, blast_cs.cgi</I></TD>
<TD>
<P>- BLAST search start-up C-shell files</TD>
</TR>
<TR><TD>
<P><I>.nlmstmanrc</I></TD>
<TD>
<P>- Configuration file for the graphical overview image (do not edit!)</TD>
</TR>
<TR><TD>
<I><P>blast.html, blast_cs.html</I></TD>
<TD>
<P>- sample BLAST search input HTML forms</TD>
</TR>
<TR><TD>
<I><P>megablast.html, megablast_cs.html</I></TD>
<TD>
<P>- sample MEGABLAST search input HTML forms</TD>
</TR>
<TR><TD>
<I><P>rpsblast.html, rpsblast_cs.html</I></TD>
<TD>
<P>- sample RPS BLAST search input HTML forms</TD>
</TR>
<TR><TD>
<I><P>blast.rc</I></TD>
<TD>
<P>- <A HREF="#Configuration_file">Default configuration file</A> for the WWW BLAST server</TD>
</TR>
<TR><TD>
<I><P>psiblast.rc</I></TD>
<TD>
<P>- <A HREF="#Configuration_file">Default configuration file</A> for the PSI/PHI WWW BLAST server</TD>
</TR>
<TR><TD>
<P><I>psiblast.cgi, psiblast_cs.cgi</I></TD>
<TD>
<P>- PSI/PHI BLAST search start-up C-shell files</TD>
</TR>
<TR><TD>
<I><P>psiblast.html, psiblast_cs.html</I></TD>
<TD>
<P>- sample PSI/PHI BLAST search input HTML forms</TD>
</TR>
<TR><TD>
<I><P>psiblast.REAL, psiblast_cs.REAL</I></TD>
<TD>
<P>- Main PSI/PHI BLAST server executables</TD>
</TR>
<TR><TD>
<I><P>wblast2.html, wblast2_cs.html</I></TD>
<TD>
<P>- sample BLAST 2 sequences search input HTML forms</TD>
</TR>
<TR><TD>
<I><P>wblast2.REAL, wblast2_cs.REAL</I></TD>
<TD>
<P>- Main BLAST 2 sequences server executables</TD>
</TR>
<TR><TD>
<I><P>bl2bag.cgi</I></TD>
<TD>
<P>- CGI used to create 2 sequences alignment image on the fly</TD>
</TR>
<TR><TD>
<I><P>blast_form.map</I></TD>
<TD>
<P>- Auxiliary map file for the front BLAST image</TD>
</TR>
<TR><TD>
<I><P>nph-viewgif.cgi</I></TD>
<TD>
<P>- CGI program used to view and delete overview images</TD>
</TR>
<TR><TD>
<I><P>readme.html</I></TD>
<TD>
<P>- this documentation</TD>
</TR>
<TR><TD>
<I><P>wwwblast.log</I></TD>
<TD>
<P>- default logfile</TD>
</TR>
<TR><TD>
<I><P>psiblast.log</I></TD>
<TD>
<P>- default PSI/PHI Blast logfile</TD>
</TR>
<TR><TD>
<I><P>ncbi_blast.rc</I></TD>
<TD>
<P>- sample file for full NCBI set of databases</TD>
</TR>
</TABLE>

<UL>
<B><LI>./data</B> directory - matrices used in BLAST search </LI>
<B><LI>./db</B> directory. - Files of test BLAST and RPS-BLAST databases. </LI>
<B><LI>./docs:</B> - HTML pages used in sample BLAST search input pages </LI>
<B><LI>./images</B> - images used in the sample BLAST search input pages </LI>
<B><LI>./Src</B> - source directory for the WWW BLAST server. </LI>
<B><LI>./Src/XML</B> - source directory for creation of files related to the XML output.
<UL>
    <LI> blstxml.asn - ASN.1 definition for Blast XML
    <LI> blstxml.dtd - corresponding DTD
</UL>

<B><LI>./TmpGifs</B> - storage for temporary BLAST overview gif files </LI></UL>

<H3><A NAME="Configuration_of_databases">Configuration of BLAST databases</A></H3>
<P>To set up databases for the standalone WWW BLAST server, it is necessary to follow these steps: </P>
<OL>

<LI>Put a file with concatenated FASTA entries in the "./db" directory </LI>
<LI>Run "formatdb" program, available from the <a href="ftp://ncbi.nlm.nih.gov/blast/executables">NCBI ftp site</a> to format the database. </LI>
<LI>Add name of the database into <A HREF="#Configuration_file">server configuration file</A> </LI>
<LI>Add name of the database into (PSI/PHI) WWW BLAST search form </LI></OL>

<H3><A NAME="PSI_PHI_Notes">PSI/PHI Blast notes</A> </H3>
There is one significant feature of the PSI/PHI Blast server: FASTA
files from which the BLAST databases are formatted should have GI numbers in all 
sequence ids. This is almost always true for FASTA files from the NCBI FTP site.
Local databases may not be used with this version of PSI/PHI Blast unless
they have "&gt;gi|12345..." prefix in the definition line.
<P>
Databases for the PSI/PHI Blast should always be created with formatdb using
the "-o T" flag. Test database "test_aa_db" was created using this flag and
database "test_na_db" was created without this flag.
<P>
If this distribution is installed not in the "/blast" directory under HTTPD
documents root directory, than path to the distribution should be set
by an environment variable WWW_ROOT_PATH in the file psiblast.cgi or psiblast_cs.cgi
<H3><A NAME="CS_Notes">Client/server version for Entrez lookup and taxonomy reports</A> </H3>
Regular Blast, PSI/PHI Blast, MegaBlast and Blast 2 Sequences have client/server versions for
Entrez gi/accession lookups and printing Taxonomy reports. Configuration of
client/server interface from the user to NCBI should be done the same way as for any
other client/server program to NCBI. If program "blastcl3" works without
problems, this server should work OK as well. If user has firewall - default
configuration will definitely fail to work properly and this case will
require special configuration. If user has problems with such configuration,
one should write to
<a href="mailto:info@ncbi.nlm.nih.gov">info@ncbi.nlm.nih.gov</a>
 for further assistance.
<H3><A NAME="XML_Output">XML output</A></H3>
Possibility to produce XML output was added to this server. XML definition
of BLAST output is tied to the simple ASN.1 specification designed for this
case. These definitions  may be found in the directory ./Src/XML. Any 
recommendations on improvements to this (possible) standard may be sent to 
<a href = "mailto:blast-help@ncbi.nlm.nih.gov">blast-help@ncbi.nlm.nih.gov</a> 
XML may be printed by setting "Alignment view" in blast.html or (blast_cs.html)
page to "BLAST XML".
Resulting page will look empty - but if you open the page source (in Netscape -
View -> Page source) - you will see the complete XML document.
<H3><A NAME="Bl2Seq">Blast 2 sequences</A></H3>
Blast 2 sequences program was initially written by Tatiana Tatusova and
Tom Madden and was presented in the article: Tatiana A. Tatusova, 
Thomas L. Madden (1999), "Blast 2 sequences - a new tool for
comparing protein and nucleotide sequences", 
<A HREF = "http://www.ncbi.nlm.nih.gov/htbin-post/Entrez/query?uid=10339815&form=6&db=m&Dopt=b">FEMS Microbiol Lett. 174:247-250</A>.
The standalone WWW version of the program mirrors the <a href="http://www.ncbi.nlm.nih.gov/blast/bl2seq/bl2.html">NCBI Blast 2 Sequences</a> web page. 
<H3><A NAME="RPS_blast">RPS Blast</A></H3>
RPS Blast or "Reversed Position Specific BLAST" is a
very fast alternative to the program <a href="http://www.ncbi.nlm.nih.gov:80/entrez/query.fcgi?cmd=Retrieve&db=PubMed&list_uids=10745990&dopt=Abstract">IMPALA</a>. It has the same general
objective - to compare a sequence to a collection of conserved domains (aka motifs, profiles, HMMs).
RPS Blast has a completely different implementation that has
increased the speed of profiles search 10 to 100 times depending on search
conditions in comparison to IMPALA. RPS Blast has an option to perform a translated search of DNA sequences against these conserved domains. 
Currently RPS Blast is one of the tools chosen to annotate human 
genome at NCBI and is the basis for the <a href ="http://www.ncbi.nlm.nih.gov/Structure/cdd/wrpsb.cgi">CDD Blast search</a> page.
<P>
Databases for RPS blast are hardware dependent - for speed reasons. Hence 
they are different for big/little endian platforms.
<P>
To build RPS database it is necessary to follow the procedure explained in
the file "README.rps", that comes with this distribution.
There is a small RPS database available for testing. This database is a part
of a real NCBI database used in CDD search page. Full NCBI database is
available in platform-independent form from FTP site.

<H3><A NAME="OOF_blastx">Out of Frame BLASTX</A></H3>
The OOF version of the blastx program finds alignments between a nucleotide 
sequence translated into 3 frames and protein sequences, in which query sequence 
frames can be shifted within one alignment. The algorithm and low-level alignment 
functions were written by Zheng Zhang, currently at <a href="http://www.paracel.com">Paracel Inc.</a>, and incorporated into regular BLAST API by Sergei Shavirin. 
<P>
XML and tabular output are not yet implemented for the OOF alignments.
<H3><A NAME="Description_of_tags">Description of tags for the main BLAST input page</A></H3>
<P>This standalone server has a tag convention analogous to the regular NCBI BLAST server. Sample BLAST search forms may be changed to accommodate particular needs of the user in the custom search. Here is the list of these tags and their meaning. If some tag is missing from the search input page, it will take a default value. Exceptions are tags PROGRAM, DATALIB and SEQUENCE (or SEQFILE), that should always be set. </P>

<UL>
<B><LI>PROGRAM</B> - name of the BLAST program. Supported values include programs: blastn, blastp, blastx, tblastx and tblastn </LI>
<B><LI>DATALIB</B> - name of the database(s) to search. This implementation includes possibility to use multiple databases. To use multiple databases several "DATALIB" tags should be used on the page for example using checkboxes (look for example at <A HREF="http://www.ncbi.nlm.nih.gov/Microb_blast/unfinishedgenome.html">Microbial Genomes Blast Databases BLAST</A> at NCBI). Note, that all of these databases should be properly written in the server configuration file. </LI>
<B><LI>SEQUENCE</B> and <B>SEQFILE</B> - these tags used to pass sequence. First SEQUENCE tag is used for the input sequence. If it is missing, the SEQFILE tag is used instead. </LI>
<B><LI>UNGAPPED_ALIGNMENT</B> - default BLAST search is a gapped search; this tag, if set, will turn gapped alignment off. </LI>
<B><LI>MAT_PARAM</B> used to set 3 parameters at the same time. Value for this tag should be in format "<mat_name> <d1><d2>" where mat_name - string name of the matrix (BLOSUM62, etc), d1 - integer for cost to open gap and d2 - cost to extend gap (-G and -E parameters in blastall respectably) </LI>
<B><LI>GAP_OPEN</B> - set value for cost to open gap - 0 or missing tag invoked default behavior </LI>
<B><LI>GAP_EXTEND</B> - set value for cost to extend gap - 0 or missing tag invoked default behavior </LI>
<B><LI>X_DROPOFF</B> - Dropoff (X) for blast extensions in bits (default if zero) (-y parameter in "blastpgp" program) </LI>
<B><LI>GENETIC_CODE</B> - Query Genetic code to use (for blastx only) </LI>
<B><LI>THRESHOLD_2</B> - Threshold for extending hits in second pass in multipass model search </LI>
<B><LI>MATRIX</B> - Matrix (default is BLOSUM62) (-M in blastall) </LI>
<B><LI>EXPECT</B> - Expectation value (-e in blastall) </LI>
<B><LI>NUM_OF_BITS</B> - Number of bits to trigger gapping (-N in blastpgp) </LI>
<B><LI>NCBI_GI</B> - If formated database use SeqIds in the NCBI format this option will turn printing of gis together with accessions. </LI>
<B><LI>FILTER</B> - Multiple instances of values of this tag are concatenated and passed to the engine as "filter_string" ("L" for low complexity and "m" if filter should be set for lookup table only) - any letter will turn default filtering on - DUST for nucleotides and SEG for proteins (-F in blastall) </LI>
<B><LI>DESCRIPTIONS</B> - Number of one-line descriptions in the output (-v in blastall) </LI>
<B><LI>ALIGNMENTS</B> - Number of alignments to show (-b in blastall) </LI>
<B><LI>COLOR_SCHEMA</B> - Color schema to use in printing of alternative alignment. This option is valid only for blastp and blastn programs. If set - it will
override option set by "ALIGNMENT_VIEW" </LI>
<B><LI>TAX_BLAST</B> - Print taxonomy reports. This option is valid only for
client/server version of regular Blast </LI>
<B><LI>XML_OUTPUT</B> - Print XML Blast output. All other alignment view options will be disabled </LI>
<B><LI>ENTREZ_QUERY</B> - Limit search to results of Entrez query. Only for 
client/server version </LI>
<B><LI>RPSBLAST</B> - This tag with turn "blastp" or "blastx" search into RPS Blast search for the rps blast database. </LI>
<B><LI>OOF_ALIGN</B> -This flag if set to non-zero digit will turn on OOF alignment for "blastx" and will set frame shift penalty to this value. </LI>
<B><LI>OTHER_ADVANCED</B> - this tag allows to input string analogous to the command line parameters of blastall. Setting parameter in OTHER_ADVANCED tag will override all other settings of this parameter. Supported options include: </LI>
<UL>
<B><LI>-G</B> gap open cost </LI>
<B><LI>-E</B> gap extend cost </LI>
<B><LI>-q</B> penalty for nucleotide mismatch </LI>
<B><LI>-r</B> reward for nucleotide match </LI>
<B><LI>-e</B> expect value </LI>
<B><LI>-W</B> wordsize </LI>
<B><LI>-v</B> Number of descriptions to print </LI>
<B><LI>-b</B> Number of alignments to show </LI>
<B><LI>-K</B> Number of best hits from a region to keep </LI>
<B><LI>-Y</B> effective search space </LI></UL>

<B><LI>ALIGNMENT_VIEW</B> - will set type of alignment to show. Available options include: </LI>

<UL>
<LI>0 - Pairwise </LI>
<LI>1 - query-anchored with identities </LI>
<LI>2 - query-anchored without identities </LI>
<LI>3 - flat query-anchored with identities </LI>
<LI>4 - flat query-anchored without identities </LI>
<LI>7 - BLAST XML (equivalent to setting the XML_OUTPUT tag)</LI>
<LI>9 - Hit Table - to produce tabular output
</UL>

<B><LI>OVERVIEW</B> - used to turn on or off printing of alignment overview image </LI>
<B><LI>BLAST_TYPE</B> - a special tag to distinguish different BLAST search types. See the description of a configuration file. </LI></UL>

<H3><A NAME="Configuration_file">Server configuration file and logfile</A></H3>
<P>Default configuration file is "blast.rc" and logfile "wwwblast.log". Setting tag BLAST_TYPE to specific value may change these names. This is useful if few different search input pages use the same CGI search engine, but significantly different by content and priorities. A sample configuration file comes with this distribution: </P>
This file will set how many CPUs will be used in the BLAST search and what databases may be used with what programs. Logfile currently stores only limited information but also may be updated by programmers to store more values in it. Please note, that usually HTTPD servers run by accounts that do not have write access to disk, so the logfile permission should be set to 666. </P>
<H3><A NAME="Debugging">How to debug WWW Blast programs</A></H3>

There is a way to debug these programs.

<OL>
<LI> Add line "setenv DEBUG_COMMAND_LINE TRUE" into the *.cgi file
   (uncomment it)
<LI> Run search that results in the problem - this should create a
   file "/tmp/__web.in" in the "/tmp" directory.
<LI> Set all necessary environment variables on the command line (BLASTDB at least)
   and run from command-line: "blast.REAL &lt; /tmp/__web.in"
</OL>
This should do your problematic search without WWW. If this resulted
in coredump - you may look into the core file with:
<P>
dbx blast.REAL core
<P>
and then use command "where" to print stack.

<P><HR></P>
<ADDRESS><A HREF="mailto:blast-help@ncbi.nlm.nih.gov">BLAST Help Desk</A></ADDRESS>
<P><!-- Created: Thu Mar 16 16:41:05 EST 2000 -->
<!-- hhmts start -->Last modified: Fri Jan 11, 2002 <!-- hhmts end --></P></BODY>
</HTML>
------------------------------------------------------------------------


    Introduction to the Standalone WWW Blast server

------------------------------------------------------------------------


      Index

    * Introduction <#Inroduction>
    * What's new in this revision? <#Whatsnew>
    * Installation of the Standalone WWW server <#Installation>
    * Description of files in the distribution <#Description_of_files>
    * Configuration of BLAST databases <#Configuration_of_databases>
    * PSI/PHI Blast notes <#PSI_PHI_Notes>
    * Client/server versions for Entrez lookup and taxonomy reports
      <#CS_Notes>
    * Blast 2 sequences <#Bl2Seq>
    * XML output <#XML_Output>
    * Out of Frame BLASTX <#OOF_blastx>
    * RPS Blast <#RPS_blast>
    * Description of tags for main BLAST input page <#Description_of_tags>
    * Server configuration file and logfile <#Configuration_file>
    * How to debug WWW Blast programs <#Debugging>


      Introduction

This standalone WWW BLAST server suite of programs was designed similar
to the regular NCBI BLAST server and such command-line NCBI BLAST
programs like "blastall", "blastpgp", "rpsblast" and "megablast". It
incorporates most features, which exist in NCBI BLAST programs and
should be relatively easy to use. This server does not support any
request queuing and load balancing. As soon as the user hits a "Search"
button, BLAST starts immediately if entered information is valid. So,
this server is not intended to handle large load, which may exist in
public service. Such queueing and loadbalancing however may be
implemented using such products as Load Sharing Facility - "LSF" from
Platform Computing Corporation <http://www.platform.com>. Interface to
"LSF" was implemented in NCBI, however this was not included in this
suite. Standalone server assumes that users have their own BLAST or
RPS-BLAST database(s), that should be searched and want to have a simple
WWW interface to such search. It is STRONLY recommended that user have
experience in installation and running standalone NCBI BLAST programs.

After files are uncompressed, server is ready to be used immediately.
Any customizations to the program are welcomed. The source code for WWW
BLAST is now part of the NCBI C toolkit, which can be downloaded from
the NCBI FTP web site: ftp://ftp.ncbi.nih.gov
<ftp://ftp.ncbi.nih.gov/toolbox/ncbi_tools/README.htm>
The compilation of the NCBI C toolkit includes the WWW BLAST
executables. The files in the C toolkit most relevant for the WWW BLAST
executables are: wwwblast.c, wwwbutl.c, psiblast.c, wblast2.c.


      What's new in this revision?

May 10, 2004

    * XML output brought in sync with the text output, masking filtered
locations in query sequences.

February 2, 2004

    * All source code moved to the NCBI C toolkit.
    * Mouseover feature fixed in graphical overview.
    * All binaries synchronized with the latest NCBI C toolkit release.
      All future releases will be automatically synchronized with future
      toolkit releases.
    * Recompilation procedure changed. WWW BLAST binaries are now
compiled as part of the C toolkit.

November 21, 2003

    * Fixed a bug with absent images on PSI-BLAST iterations.
    * Removed header and progress messages from XML output.
    * All binaries recompiled with the newest version of the NCBI C
toolkit libra ries.

May 9, 2003

    * Cleaned the Makefile for recompiling the sources.
    * Added discontiguous Mega BLAST options.
    * Added option to choose a subsequence location for query.
    * Added option to choose database genetic code.
* All binaries recompiled.

April 21, 2003

    * Added instructions for recompilation of binaries from the source
      code to this readme file.
    * Fixed a bug in processing of the configuration file that limited
      allowed number of databases.
    * Added images for the Linkout and UniGene links from the BLAST output.
    * Corrected paths to the graphical overview for PSI/PHI BLAST output.
    * All binaries recompiled with the newest version of the NCBI C
toolkit libraries.

February 10, 2003

    * Added support for multi-query XML output.
* All binaries recompiled.

December 2, 2002

* All binaries recompiled with the newest version of the toolkit.

August 6, 2002

* Recompiled all binaries to include recent bug fixes.

June 18, 2002

    * Removed limit on the total length of database names.
    * Removed xmlblast.cgi and other unneeded XML related files.
* Recompiled all programs.

January 11, 2002

    * Removed formatdb, makemat and copymat binaries from the archive -
      those should be taken from the NCBI BLAST executables archive
      <ftp://ncbi.nlm.nih.gov/blast/executables>
    * Added tabular output format
* Added option to mask lower case in query

May, 2 2001

    * No major changes. All programs have been recompiled and made
synchronous to the latest NCBI tookit release.

November 3, 2000

* Blast 2 sequences <#Bl2Seq> was added

October, 19 2000

    * RPS Blast <#RPS_blast> was added
    * Out of Frame BLASTX <#OOF_blastx> (OOF) now available for testing
and suggestions.

September, 28 2000

    * Added possibility to limit search to results of Entrez query
(Regular client/server BLAST)

September, 11 2000

    * Added MEGABLAST <docs/megablast_readme.html> search.
    * Added possibility to have multiple FASTA query input - batch
searches with multiple graphical overviews. (Regular BLAST)

August, 22 2000

    * Added new advanced statistics to PSI Blast and ability to produce
      Smith-Waterman alignments
* Added support for XML output.

May, 17 2000

    * PSI and PHI Blast were added to this distribution
    * Added support for client/server interface for gi/accesion lookups
      using Entrez
    * Added possibility to print Taxonomy reports
    * Added option to print alternative alignment with specific color
schema

March, 20 2000

* Initial revision


      Installation of the Standalone WWW server

After downloading the file wwwblast.Your_platform.tar.gz to your
computer, place it into document directory of HTTPD server and
uncompress it by

    gzip -d wwwblast.Your_platform.tar.gz
    tar -xvpf wwwblast.Your_platform.tar

Please note that parameter "p" in tar options is significant - it will
preserve file access options stored in the distribution. Temporary
directory for BLAST overview images (TmpGifs) should have 777
permission, and logfiles (wwwblast.log and psiblast.log) should have 666.

After you have uncompressed the distribution file, "blast" directory
will be created. You can access sample BLAST HTML input forms using URLs:

    * http://your_hostname/blast/blast.html
    * http://your_hostname/blast/blast_cs.html
    * http://your_hostname/blast/psiblast.html
    * http://your_hostname/blast/psiblast_cs.html
    * http://your_hostname/blast/megablast.html
    * http://your_hostname/blast/megablast_cs.html
    * http://your_hostname/blast/wblast2.html
* http://your_hostname/blast/wblast2_cs.html

This distribution comes with 2 BLAST databases: "test_aa_db" - sample
protein database and "test_na_db" - sample nucleotide database. These
databases are configured to be searchable immediately with compatible
BLAST programs.


      Description of files in the distribution

* Root directory (./blast):

Files with suffix "*_cs.*" are analogous to the files without such
suffix, with added capability to make client/server Entrez lookups for
sequence gis and accessions.

blast.cgi, blast_cs.cgi

- BLAST search start-up C-shell files

.nlmstmanrc

- Configuration file for the graphical overview image (do not edit!)

blast.html, blast_cs.html

- sample BLAST search input HTML forms

megablast.html, megablast_cs.html

- sample MEGABLAST search input HTML forms

rpsblast.html, rpsblast_cs.html

- sample RPS BLAST search input HTML forms

blast.rc

- Default configuration file <#Configuration_file> for the WWW BLAST server

psiblast.rc

- Default configuration file <#Configuration_file> for the PSI/PHI WWW
BLAST server

psiblast.cgi, psiblast_cs.cgi

- PSI/PHI BLAST search start-up C-shell files

psiblast.html, psiblast_cs.html

- sample PSI/PHI BLAST search input HTML forms

psiblast.REAL, psiblast_cs.REAL

- Main PSI/PHI BLAST server executables

wblast2.html, wblast2_cs.html

- sample BLAST 2 sequences search input HTML forms

wblast2.REAL, wblast2_cs.REAL

- Main BLAST 2 sequences server executables

bl2bag.cgi

- CGI used to create 2 sequences alignment image on the fly

blast_form.map

- Auxiliary map file for the front BLAST image

nph-viewgif.cgi

- CGI program used to view and delete overview images

readme.html

- this documentation

wwwblast.log

- default logfile

psiblast.log

- default PSI/PHI Blast logfile

ncbi_blast.rc

- sample file for full NCBI set of databases

    * ./data
    * directory - matrices used in BLAST search ./db
    * directory. - Files of test BLAST and RPS-BLAST databases. ./docs:
    * - HTML pages used in sample BLAST search input pages ./images
    * - images used in the sample BLAST search input pages ./Src
    * - source directory for the WWW BLAST server. ./Src/XML
      - source directory for creation of files related to the XML output.
          o blstxml.asn - ASN.1 definition for Blast XML
    o blstxml.dtd - corresponding DTD
    * ./TmpGifs
- storage for temporary BLAST overview gif files


      Configuration of BLAST databases

To set up databases for the standalone WWW BLAST server, it is necessary
to follow these steps:

   1. Put a file with concatenated FASTA entries in the "./db" directory
   2. Run "formatdb" program, available from the NCBI ftp site
      <ftp://ncbi.nlm.nih.gov/blast/executables> to format the database.
   3. Add name of the database into server configuration file
      <#Configuration_file>
   4. Add name of the database into (PSI/PHI) WWW BLAST search form 


      PSI/PHI Blast notes

There is one significant feature of the PSI/PHI Blast server: FASTA
files from which the BLAST databases are formatted should have GI
numbers in all sequence ids. This is almost always true for FASTA files
from the NCBI FTP site. Local databases may not be used with this
version of PSI/PHI Blast unless they have ">gi|12345..." prefix in the
definition line.

Databases for the PSI/PHI Blast should always be created with formatdb
using the "-o T" flag. Test database "test_aa_db" was created using this
flag and database "test_na_db" was created without this flag.

If this distribution is installed not in the "/blast" directory under
HTTPD documents root directory, than path to the distribution should be
set by an environment variable WWW_ROOT_PATH in the file psiblast.cgi or
psiblast_cs.cgi


      Client/server version for Entrez lookup and taxonomy reports

Regular Blast, PSI/PHI Blast, MegaBlast and Blast 2 Sequences have
client/server versions for Entrez gi/accession lookups and printing
Taxonomy reports. Configuration of client/server interface from the user
to NCBI should be done the same way as for any other client/server
program to NCBI. If program "blastcl3" works without problems, this
server should work OK as well. If user has firewall - default
configuration will definitely fail to work properly and this case will
require special configuration. If user has problems with such
configuration, one should write to info@ncbi.nlm.nih.gov
<mailto:info@ncbi.nlm.nih.gov> for further assistance.


      XML output

Possibility to produce XML output was added to this server. XML
definition of BLAST output is tied to the simple ASN.1 specification
designed for this case. These definitions may be found in the directory
./Src/XML. Any recommendations on improvements to this (possible)
standard may be sent to blast-help@ncbi.nlm.nih.gov
<mailto:blast-help@ncbi.nlm.nih.gov> XML may be printed by setting
"Alignment view" in blast.html or (blast_cs.html) page to "BLAST XML".
Resulting page will look empty - but if you open the page source (in
Netscape - View -> Page source) - you will see the complete XML document.


      Blast 2 sequences

Blast 2 sequences program was initially written by Tatiana Tatusova and
Tom Madden and was presented in the article: Tatiana A. Tatusova, Thomas
L. Madden (1999), "Blast 2 sequences - a new tool for comparing protein
and nucleotide sequences", FEMS Microbiol Lett. 174:247-250
<http://www.ncbi.nlm.nih.gov/htbin-post/Entrez/query?uid=10339815&form=6&db=m&Dopt=b>.
The standalone WWW version of the program mirrors the NCBI Blast 2
Sequences <http://www.ncbi.nlm.nih.gov/blast/bl2seq/bl2.html> web page.


      RPS Blast

RPS Blast or "Reversed Position Specific BLAST" is a very fast
alternative to the program IMPALA
<http://www.ncbi.nlm.nih.gov:80/entrez/query.fcgi?cmd=Retrieve&db=PubMed&list_uids=10745990&dopt=Abstract>.
It has the same general objective - to compare a sequence to a
collection of conserved domains (aka motifs, profiles, HMMs). RPS Blast
has a completely different implementation that has increased the speed
of profiles search 10 to 100 times depending on search conditions in
comarison to IMPALA. RPS Blast has an option to perform a translated
search of DNA sequences against these conserved domains. Currently RPS
Blast is one of the tools chosen to annotate human genome at NCBI and is
the basis for the CDD Blast search
<http://www.ncbi.nlm.nih.gov/Structure/cdd/wrpsb.cgi> page.

Databases for RPS blast are hardware dependent - for speed reasons.
Hence they are different for big/little endian platforms.

To build RPS database it is necessary to follow the procedure explained
in the file "README.rps", that comes with this distribution. There is a
small RPS database available for testing. This database is a part of a
real NCBI database used in CDD search page. Full NCBI database is
available in platform-independent form from FTP site.


      Out of Frame BLASTX

The OOF version of the blastx program finds alignments between a
nucleotide sequence translated into 3 frames and protein sequences, in
which query sequence frames can be shifted within one alignment. The
algorithm and low-level alignment functions were written by Zheng Zhang,
currently at Paracel Inc. <http://www.paracel.com>, and incorporated
into regular BLAST API by Sergei Shavirin.

XML and tabular output are not yet implemented for the OOF alignments.


      Description of tags for the main BLAST input page

This standalone server has a tag convention analogous to the regular
NCBI BLAST server. Sample BLAST search forms may be changed to
accommodate particular needs of the user in the custom search. Here is
the list of these tags and their meaning. If some tag is missing from
the search input page, it will take a default value. Exceptions are tags
PROGRAM, DATALIB and SEQUENCE (or SEQFILE), that should always be set.

    * PROGRAM
      - name of the BLAST program. Supported values include programs:
    * blastn, blastp, blastx, tblastx and tblastn DATALIB
      - name of the database(s) to search. This implementation includes
      possibility to use multiple databases. To use multiple databases
      several "DATALIB" tags should be used on the page for example
      using checkboxes (look for example at Microbial Genomes Blast
      Databases BLAST
      <http://www.ncbi.nlm.nih.gov/Microb_blast/unfinishedgenome.html>
      at NCBI). Note, that all of these databases should be properly
    * written in the server configuration file. SEQUENCE
      and SEQFILE - these tags used to pass sequence. First SEQUENCE tag
      is used for the input sequence. If it is missing, the SEQFILE tag
    * is used instead. UNGAPPED_ALIGNMENT
      - default BLAST search is a gapped search; this tag, if set, will
    * turn gapped alignment off. MAT_PARAM
      used to set 3 parameters at the same time. Value for this tag
      should be in format " " where mat_name - string name of the matrix
      (BLOSUM62, etc), d1 - integer for cost to open gap and d2 - cost
    * to extend gap (-G and -E parameters in blastall respectably) GAP_OPEN
      - set value for cost to open gap - 0 or missing tag invoked
    * default behavior GAP_EXTEND
      - set value for cost to extend gap - 0 or missing tag invoked
    * default behavior X_DROPOFF
      - Dropoff (X) for blast extensions in bits (default if zero) (-y
    * parameter in "blastpgp" program) GENETIC_CODE
    * - Query Genetic code to use (for blastx only) THRESHOLD_2
      - Threshold for extending hits in second pass in multipass model
    * search MATRIX
    * - Matrix (default is BLOSUM62) (-M in blastall) EXPECT
    * - Expectation value (-e in blastall) NUM_OF_BITS
    * - Number of bits to trigger gapping (-N in blastpgp) NCBI_GI
      - If formated database use SeqIds in the NCBI format this option
    * will turn printing of gis together with accessions. FILTER
      - Multiple instances of values of this tag are concatenated and
      passed to the engine as "filter_string" ("L" for low complexity
      and "m" if filter should be set for lookup table only) - any
      letter will turn default filtering on - DUST for nucleotides and
    * SEG for proteins (-F in blastall) DESCRIPTIONS
    * - Number of one-line descriptions in the output (-v in blastall)
      ALIGNMENTS
    * - Number of alignments to show (-b in blastall) COLOR_SCHEMA
      - Color schema to use in printing of alternative alignment. This
      option is valid only for blastp and blastn programs. If set - it
    * will override option set by "ALIGNMENT_VIEW" TAX_BLAST
      - Print taxonomy reports. This option is valid only for
    * client/server version of regular Blast XML_OUTPUT
      - Print XML Blast output. All other alignment view options will be
    * disabled ENTREZ_QUERY
      - Limit search to results of Entrez query. Only for client/server
    * version RPSBLAST
      - This tag with turn "blastp" or "blastx" search into RPS Blast
    * search for the rps blast database. OOF_ALIGN
      -This flag if set to non-zero digit will turn on OOF alignment for
    * "blastx" and will set frame shift penalty to this value.
      OTHER_ADVANCED
      - this tag allows to input string analogous to the command line
      parameters of blastall. Setting parameter in OTHER_ADVANCED tag
      will override all other settings of this parameter. Supported
      options include:
          o -G
          o gap open cost -E
          o gap extend cost -q
          o penalty for nucleotide mismatch -r
          o reward for nucleotide match -e
          o expect value -W
          o wordsize -v
          o Number of descriptions to print -b
          o Number of alignments to show -K
          o Number of best hits from a region to keep -Y
    * effective search space ALIGNMENT_VIEW
      - will set type of alignment to show. Available options include:
          o 0 - Pairwise
          o 1 - query-anchored with identities
          o 2 - query-anchored without identities
          o 3 - flat query-anchored with identities
          o 4 - flat query-anchored without identities
          o 7 - BLAST XML (equivalent to setting the XML_OUTPUT tag)
    o 9 - Hit Table - to produce tabular output
    * OVERVIEW
    * - used to turn on or off printing of alignment overview image
      BLAST_TYPE
      - a special tag to distinguish different BLAST search types. See
the description of a configuration file.


      Server configuration file and logfile

Default configuration file is "blast.rc" and logfile "wwwblast.log".
Setting tag BLAST_TYPE to specific value may change these names. This is
useful if few different search input pages use the same CGI search
engine, but significantly different by content and priorities. A sample
configuration file comes with this distribution:

This file will set how many CPUs will be used in the BLAST search and
what databases may be used with what programs. Logfile currently stores
only limited information but also may be updated by programmers to store
more values in it. Please note, that usually HTTPD servers run by
accounts that do not have write access to disk, so the logfile
permission should be set to 666.


      How to debug WWW Blast programs

There is a way to debug these programs.

   1. Add line "setenv DEBUG_COMMAND_LINE TRUE" into the *.cgi file
      (uncomment it)
   2. Run search that results in the problem - this should create a file
      "/tmp/__web.in" in the "/tmp" directory.
   3. Set all necessary environment variables on the command line
      (BLASTDB at least) and run from command-line: "blast.REAL <
      /tmp/__web.in" 

This should do your problematic search without WWW. If this resulted in
coredump - you may look into the core file with:

dbx blast.REAL core

and then use command "where" to print stack.

------------------------------------------------------------------------

BLAST Help Desk <mailto:blast-help@ncbi.nlm.nih.gov>

Last modified: Fri Jan 11, 2002

Seabase cosine similarity calculation
=====================================

Usage
-----

* Download and set classpath for [mysql jdbc driver][1]

    Classpath can be changed in either /etc/environment, .bashrc, .bash_profile 

    export CLASSPATH=$CLASSPATH:path/to/mysql...jar

    source ~/.bashrc # or whatever has modified CLASSPATH

* Compile 

    javac CosineCalc.java

* Execute
 
    java CosineCalc

* Use result from java/similarities.tsv
Seabase
=======

A tool for searching, analysing and sharing gene expression data of marine
organisms.


Transcriptomic repository for multiple species

Schema:

taxons:
	int id
	scientific_name string 256 # "Human", "Mouse", "Nematostella" ? Should this be restricted to a latin name?
	common_name string 256
rails generate scaffold Taxon scientific_name:string common_name:string

condition:
	id int
	description text
rails generate scaffold Condition description:text

replicates:
	id int
	taxon_id int
	name string 80 # "18h_B_L2"
	stage int # 18
	condition_id int
	technical_replicate int # B Distinct extracted sample
	lane_replicate int # Read of a sample L1-L7 (is this adding anything not already covered by id and name?)
	y_intercept float
	slope float
	total_mapping int

    rails generate scaffold Replicate taxon:references name:string:80 stage:int condition:references technical_replicate:int lane_replicate:int y_intercept:float slope:float total_mapping:int

transcripts:
	id int
	name string 20 # comp100008_c0_seq1
	isogroup int # 1000080
	length int # 254
	transcript_sequence text

    rails generate scaffold Transcript name:string:20 isogroup:int length:int transcript_sequence:text

mapping_counts:
	id int
	replicate_id int
	transcript_id int
	mapping_count int # 3

    rails generate scaffold MappingCount replicate:references transcript:references mapping_count:int

external_sources:
	id int
	name string 256
	
	rails generate scaffold ExternalSource name:string

external_identifiers:
	id int
	external_source_id int
	name string 6 # Q14738
	
	  rails generate scaffold ExternalIdentifier external_source:references name:string:6

# Comes from BLASTing mouse, human and searching UNIPROT
external_matches: ? Is this a reasonable name?
	id int
	external_name_id int
	paralog int # 1
	transcript_id int
	length int # 602
	query_from int # 65
	query_to int # 138
	isoform int # 1

external_names:
  id int
  taxon_id int
  external_identifier_id int
  gene_name string
  functional_name text
  
  
    rails generate scaffold ExternalMatch taxon:references external_identifier:references transcript:references gene_name:string function_name:text length:int query_from:int query_to:int paralog:int isoform:int

    rails generate scaffold ExternalName taxon:references external_identifier:references gene_name:string function_name:text

Queries from Perl:
autoComplete.cgi:my $sql = "SELECT DISTINCT(acc), gn, fn from $form_input{'type'}Name WHERE acc LIKE '%$form_input{'term'}%' OR gn LIKE '%$form_input{'term'}%' OR fn LIKE '%$form_input{'term'}%' LIMIT 10";
graph.cgi:my $sql = "SELECT * FROM normalization";
graph.cgi:	my $sql = "SELECT mapping_count FROM $table where id = '$id' LIMIT 1";
graph.cgi:	my $sql = "SELECT length FROM Sequences where id = '$id' LIMIT 1";
graph.cgi:	my $sql = "SELECT sequence FROM $database"."_prediction WHERE gene = '$id'";
graph.cgi:	my $sql = "SELECT length, sequence FROM Sequences WHERE id = '$input'";
graph.cgi:	my $sql = "SELECT gn, fn FROM $database where acc = '$input'";
graph.cgi:	my $sql = "SELECT acc, gn, fn FROM mouseName WHERE sequence ='$input'";
graph.cgi:        my $sql = "SELECT acc, gn, fn FROM humanName WHERE sequence ='$input'";
graph.cgi:        my $sql = "SELECT acc, gn, fn FROM nematostellaName WHERE sequence ='$input'";
orthologSearch.cgi:my $sql = "SELECT DISTINCT(acc) from $form_input{'type'}Name WHERE acc = '$form_input{'term'}' or gn = '$form_input{'term'}'";
orthologSearch.cgi:my $sql = "SELECT DISTINCT(acc), gn, fn from $form_input{'type'}Name WHERE acc LIKE '%$form_input{'term'}%' OR gn LIKE '%$form_input{'term'}%' OR fn LIKE '%$form_input{'term'}%' LIMIT 100";


	id = comp824_c0_seq1 (transcript)
	sample = |  9h_A_L2 |  -4.4469180 | 15899.5300 |      16450010 |     0 | (half_sample?)
	sequence_length = 2323
	hour = 9
	raw_expression = get_hour_expression(sample, id) = 3070
	per_embryo(raw_expression, sample, sequence_length)

	get_fpkm(sequence_length, raw_expression, total_mapping)
	(2323, 3070, 16450010)

	(3070 * 1000 * 1000 * 1000)/(2323 * 16450010)
	fpkm = 80.33836692516454

	normalize_rpkm(80.33836692516454, -4.4469180, 15899.5300, 0)

	(/ (/ (+ (* 80.33836692516454 15899.5300) -4.4469180) 300) 0.1)
	[Should be / 10]
	42577.92760532204

	(/ (* 3070 1000 1000 1000.0) (* 2323 16450010.0))
	80.33836692516454

	(/ (/ (+ (* 80.33836692516454 15899.5300) -4.4469180) 300) 0.1)
	42577.92760532204


	3106
	(/ (* 3106 1000 1000 1000.0) (* 2323 16530015.0))
	80.88704947918852

	(/ (/ (+ (* 80.88704947918852 14489.8700) -1.7842870) 300) 0.1)
	39068.03491166698

	(/ (+ 39068.03491166698 42577.92760532204) 2)

	40822.98125849451 (Hooray!)


	(m(c * 10e9/(l * n))+b)/(300 * 0.1)


	select * from normalization where id like ' 9%';                                
	select mapping_count from 9h_A_L2 where id = 'comp824_c0_seq1';                 
	SELECT length FROM Sequences where id = 'comp824_c0_seq1';                      
RPS Blast: Reversed Position Specific Blast


RPS-BLAST (Reverse PSI-BLAST) searches a query sequence against a database 
of profiles.  This is the opposite of PSI-BLAST that searches a profile 
against a database of sequences, hence the 'Reverse'.  RPS-BLAST
uses a BLAST-like algorithm, finding single- or double-word hits
and then performing an ungapped extension on these candidate matches.
If a sufficiently high-scoring ungapped alignment is produced, a gapped
extension is performed and those (gapped) alignments with sufficiently
low expect value are reported.  This procedure is in contrast to IMPALA
that performs a Smith-Waterman calculation between the query and 
each profile, rather than using a word-hit approach to identify
matches that should be extended.

RPS-BLAST uses a BLAST database, with addition of some other files that
contain a precomputed lookup table for the profiles to allow the search
to proceed faster.  Unfortunately it was not possible to make this
lookup table architecture independent (like the BLAST databases themselves)
and one cannot take an RPS-BLAST database prepared on a big-endian
system (e.g., Solaris Sparc) and run it on a small-endian system
(e.g., NT).  The RPS-BLAST database must be prepared again for the small-endian
system.

The CD-Search databases for RPS-BLAST can be found at:

 ftp://ftp.ncbi.nlm.nih.gov/pub/mmdb/cdd/

It is necessary to untar the archive and run copymat and formatdb. 
It is not necessary to run makemat on the databases from this
directory.

RPS-BLAST was coded by Sergei Shavirin with some help from Tom Madden.
RPS-BLAST reuses some of the IMPALA code for precomputing the lookup tables 
and all of the IMPALA code for evaluating the statistical significance of a match.  


1. Binary files used in RPS Blast:

The following binary files are used to setup and run RPS Blast:

makemat	: primary profile preprocessor 
  (converts a collection of binary profiles, created by the -C option
   of PSI-BLAST, into portable ASCII form);

copymat	: secondary profile preprocessor 
  (converts ASCII matrices, produced by the primary preprocessor, 
   into database that can be read into memory quickly);

formatdb  : general BLAST database formatter.    

rpsblast  : search program (searches a database of score 
  matrices, prepared by copymat, producing BLAST-like output).

2. Conversion of profiles into searchable database

*Note*: if you are starting with *.mtx files obtained from the NCBI FTP site or
another source you should skip the steps listed in 2.1.

2.1. Primary preprocessing

Prepare the following files:

i.	a collection of PSI-BLAST-generated profiles with arbitrary 
       names and suffix .chk; 

ii.	a collection of "profile master sequences", associated with 
    the profiles, each in a separate file with arbitrary name and a 3 character
    suffix starting with c;
    the sequences can have deflines; they need not be sequences in nr or
    in any other sequence database; if the sequences have deflines, then
    the deflines must be unique.

iii.	a list of profile file names, one per line, named 
    <database_name>.pn;

iv.	a list of master sequence file names, one per line, in the same 
    order as a list of profile names, named 
     <database_name>.sn;

The following files will be created:

a.	a collection of ASCII files, corresponding to each of the 
      original profiles, named 
     <profile_name>.mtx;

b.	a list of ASCII matrix files, named 
      <database_name>.mn;

c.	ASCII file with auxiliary information, named 
       <database_name>.aux;

Arguments to makemat:

    -P database name (required)
    -G Cost to open a gap (optional)
       default = 11
    -E Cost to extend a gap (optional)
       default = 1
    -U Underlying amino acid scoring matrix (optional)
       default = BLOSUM62
    -d Underlying sequence database used to create profiles (optional)
       default = nr
    -z Effective size of sequence database given by -d
       default = current size of -d option
       Note: It may make sense to use -z without -d when the
       profiles were created with an older, smaller version of an
       existing database 
    -S  Scaling factor for  matrix outputs to avoid round-off problems
       default = PRO_DEFAULT_SCALING_UP (currently defined as 100)
       Use 1.0 to have no scaling
       Output scores will be scaled back down to a unit scale to make
       them look more like BLAST scores, but we found working with a larger
       scale to help with roundoff problems.
    -H get help (overrides all other arguments)
Note: It is not enforced that the values of -G and -E passed to makemat
were actually used in making the checkpoints. However, the values fed
in to makemat are propagated to copymat and rpsblast.

ATTENTION: It is strongly recommended to use -S 1 - the scaling factor
	    should be set to 1 for rpsblast at this point in time.

2.2. Secondary preprocessing

Prepare the following files:

i.	a collection of ASCII files, corresponding to each of the 
  original profiles, named 
  <profile_name>.mtx 
(created by makemat);

ii.	a collection of "profile master sequences", associated with 
  the profiles, each in a separate file with arbitrary name and a 3 character
  suffix starting with c.

iii.	a list of ASCII_matrix files, named 
     <database_name>.mn 
   (created by makemat);

iv.	a list of master sequence file names, one per
  line, in the same order as a list of matrix names, named 
  <database_name>.sn;

v.	ASCII file with auxiliary information, named 
  <database_name>.aux 
(created by makemat);

The files input to copymatices are in ASCII format and thus portable 
between machines with different encodings for machine-readable files

The following files will be created:

a.	a huge binary file, containing all profile matrices, named
 <database_name>.rps;
b.     a huge binary file, containing lookup table for the Blast search
 corresponding to matrixes named <database_name>.loo
c.    File containing concatenation of all FASTA  "profile master sequences".
     named  <database_name> (without extention)

Arguments to copymat

    -P database name (required)
    -H get help (overrides all other arguments)
    -r format data for RPS Blast

ATTENTION: "-r" parameter have to be set to TRUE to format data for
           RPS Blast at this step.

NOTE: copymat requires a fair amount of memory as it first constructs
the the lookup table in memory before writing it to disk.  Users have
found that they require a machine with at least 500 Meg of memory for this
task.

2.3 Creating of BLAST database from <database_name> file containing
    all "profile master sequences".

"formatdb" program should be run to create regular BLAST database of all
"profile master sequences":

    formatdb -i <database_name>    -o T

3. Search

Arguments to RPS Blast

   -i  query sequence file (required)
   -p  if query sequence protein (if FALSE 6 frame franslation will be
                                  conducted as in blastx program)
   -P  database of profiles (required)
   -o  output file (optional)
       default = stdout
   -e  Expectation value threshold  (E), (optional, same as for BLAST)
       default = 10 
   -m  alignment view (optional, same as for BLAST)
   -z  effective length of database (optional)
       -1 = length given via -z option to makemat
       default (0) implies  length is actual length of profile library
          adjusted for end effects



