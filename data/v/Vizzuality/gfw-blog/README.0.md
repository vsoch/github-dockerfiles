<!DOCTYPE html>
<html>
<head>
	<meta name="viewport" content="width=device-width" />
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title>WordPress &#8250; ReadMe</title>
	<link rel="stylesheet" href="wp-admin/css/install.css?ver=20100228" type="text/css" />
</head>
<body>
<h1 id="logo">
	<a href="https://wordpress.org/"><img alt="WordPress" src="wp-admin/images/wordpress-logo.png" /></a>
</h1>
<p style="text-align: center">Semantic Personal Publishing Platform</p>

<h2>First Things First</h2>
<p>Welcome. WordPress is a very special project to me. Every developer and contributor adds something unique to the mix, and together we create something beautiful that I&#8217;m proud to be a part of. Thousands of hours have gone into WordPress, and we&#8217;re dedicated to making it better every day. Thank you for making it part of your world.</p>
<p style="text-align: right">&#8212; Matt Mullenweg</p>

<h2>Installation: Famous 5-minute install</h2>
<ol>
	<li>Unzip the package in an empty directory and upload everything.</li>
	<li>Open <span class="file"><a href="wp-admin/install.php">wp-admin/install.php</a></span> in your browser. It will take you through the process to set up a <code>wp-config.php</code> file with your database connection details.
		<ol>
			<li>If for some reason this doesn&#8217;t work, don&#8217;t worry. It doesn&#8217;t work on all web hosts. Open up <code>wp-config-sample.php</code> with a text editor like WordPad or similar and fill in your database connection details.</li>
			<li>Save the file as <code>wp-config.php</code> and upload it.</li>
			<li>Open <span class="file"><a href="wp-admin/install.php">wp-admin/install.php</a></span> in your browser.</li>
		</ol>
	</li>
	<li>Once the configuration file is set up, the installer will set up the tables needed for your blog. If there is an error, double check your <code>wp-config.php</code> file, and try again. If it fails again, please go to the <a href="https://wordpress.org/support/" title="WordPress support">support forums</a> with as much data as you can gather.</li>
	<li><strong>If you did not enter a password, note the password given to you.</strong> If you did not provide a username, it will be <code>admin</code>.</li>
	<li>The installer should then send you to the <a href="wp-login.php">login page</a>. Sign in with the username and password you chose during the installation. If a password was generated for you, you can then click on &#8220;Profile&#8221; to change the password.</li>
</ol>

<h2>Updating</h2>
<h3>Using the Automatic Updater</h3>
<p>If you are updating from version 2.7 or higher, you can use the automatic updater:</p>
<ol>
	<li>Open <span class="file"><a href="wp-admin/update-core.php">wp-admin/update-core.php</a></span> in your browser and follow the instructions.</li>
	<li>You wanted more, perhaps? That&#8217;s it!</li>
</ol>

<h3>Updating Manually</h3>
<ol>
	<li>Before you update anything, make sure you have backup copies of any files you may have modified such as <code>index.php</code>.</li>
	<li>Delete your old WordPress files, saving ones you&#8217;ve modified.</li>
	<li>Upload the new files.</li>
	<li>Point your browser to <span class="file"><a href="wp-admin/upgrade.php">/wp-admin/upgrade.php</a>.</span></li>
</ol>

<h2>Migrating from other systems</h2>
<p>WordPress can <a href="https://codex.wordpress.org/Importing_Content">import from a number of systems</a>. First you need to get WordPress installed and working as described above, before using <a href="wp-admin/import.php" title="Import to WordPress">our import tools</a>.</p>

<h2>System Requirements</h2>
<ul>
	<li><a href="https://secure.php.net/">PHP</a> version <strong>5.2.4</strong> or higher.</li>
	<li><a href="https://www.mysql.com/">MySQL</a> version <strong>5.0</strong> or higher.</li>
</ul>

<h3>Recommendations</h3>
<ul>
	<li><a href="https://secure.php.net/">PHP</a> version <strong>7.2</strong> or higher.</li>
	<li><a href="https://www.mysql.com/">MySQL</a> version <strong>5.6</strong> or higher.</li>
	<li>The <a href="https://httpd.apache.org/docs/2.2/mod/mod_rewrite.html">mod_rewrite</a> Apache module.</li>
	<li><a href="https://wordpress.org/news/2016/12/moving-toward-ssl/">HTTPS</a> support.</li>
	<li>A link to <a href="https://wordpress.org/">wordpress.org</a> on your site.</li>
</ul>

<h2>Online Resources</h2>
<p>If you have any questions that aren&#8217;t addressed in this document, please take advantage of WordPress&#8217; numerous online resources:</p>
<dl>
	<dt><a href="https://codex.wordpress.org/">The WordPress Codex</a></dt>
		<dd>The Codex is the encyclopedia of all things WordPress. It is the most comprehensive source of information for WordPress available.</dd>
	<dt><a href="https://wordpress.org/news/">The WordPress Blog</a></dt>
		<dd>This is where you&#8217;ll find the latest updates and news related to WordPress. Recent WordPress news appears in your administrative dashboard by default.</dd>
	<dt><a href="https://planet.wordpress.org/">WordPress Planet</a></dt>
		<dd>The WordPress Planet is a news aggregator that brings together posts from WordPress blogs around the web.</dd>
	<dt><a href="https://wordpress.org/support/">WordPress Support Forums</a></dt>
		<dd>If you&#8217;ve looked everywhere and still can&#8217;t find an answer, the support forums are very active and have a large community ready to help. To help them help you be sure to use a descriptive thread title and describe your question in as much detail as possible.</dd>
	<dt><a href="https://codex.wordpress.org/IRC">WordPress <abbr title="Internet Relay Chat">IRC</abbr> Channel</a></dt>
		<dd>There is an online chat channel that is used for discussion among people who use WordPress and occasionally support topics. The above wiki page should point you in the right direction. (<a href="irc://irc.freenode.net/wordpress">irc.freenode.net #wordpress</a>)</dd>
</dl>

<h2>Final Notes</h2>
<ul>
	<li>If you have any suggestions, ideas, or comments, or if you (gasp!) found a bug, join us in the <a href="https://wordpress.org/support/">Support Forums</a>.</li>
	<li>WordPress has a robust plugin <abbr title="application programming interface">API</abbr> that makes extending the code easy. If you are a developer interested in utilizing this, see the <a href="https://developer.wordpress.org/plugins/">Plugin Developer Handbook</a>. You shouldn&#8217;t modify any of the core code.</li>
</ul>

<h2>Share the Love</h2>
<p>WordPress has no multi-million dollar marketing campaign or celebrity sponsors, but we do have something even better&#8212;you. If you enjoy WordPress please consider telling a friend, setting it up for someone less knowledgable than yourself, or writing the author of a media article that overlooks us.</p>

<p>WordPress is the official continuation of <a href="http://cafelog.com/">b2/caf&#233;log</a>, which came from Michel V. The work has been continued by the <a href="https://wordpress.org/about/">WordPress developers</a>. If you would like to support WordPress, please consider <a href="https://wordpress.org/donate/" title="Donate to WordPress">donating</a>.</p>

<h2>License</h2>
<p>WordPress is free software, and is released under the terms of the <abbr title="GNU General Public License">GPL</abbr> version 2 or (at your option) any later version. See <a href="license.txt">license.txt</a>.</p>

</body>
</html>
/////////////////////////////////////////////////////////////////
/// getID3() by James Heinrich <info@getid3.org>               //
//  available at http://getid3.sourceforge.net                 //
//            or http://www.getid3.org                         //
//          also https://github.com/JamesHeinrich/getID3       //
/////////////////////////////////////////////////////////////////

*****************************************************************
*****************************************************************

   getID3() is released under multiple licenses. You may choose
   from the following licenses, and use getID3 according to the
   terms of the license most suitable to your project.

GNU GPL: https://gnu.org/licenses/gpl.html                   (v3)
         https://gnu.org/licenses/old-licenses/gpl-2.0.html  (v2)
         https://gnu.org/licenses/old-licenses/gpl-1.0.html  (v1)

GNU LGPL: https://gnu.org/licenses/lgpl.html                 (v3)

Mozilla MPL: http://www.mozilla.org/MPL/2.0/                 (v2)

getID3 Commercial License: http://getid3.org/#gCL (payment required)

*****************************************************************
*****************************************************************
Copies of each of the above licenses are included in the 'licenses'
directory of the getID3 distribution.


       +---------------------------------------------+
       | If you want to donate, there is a link on   |
       | http://www.getid3.org for PayPal donations. |
       +---------------------------------------------+


Quick Start
===========================================================================

Q: How can I check that getID3() works on my server/files?
A: Unzip getID3() to a directory, then access /demos/demo.browse.php



Support
===========================================================================

Q: I have a question, or I found a bug. What do I do?
A: The preferred method of support requests and/or bug reports is the
   forum at http://support.getid3.org/



Sourceforge Notification
===========================================================================

It's highly recommended that you sign up for notification from
Sourceforge for when new versions are released. Please visit:
http://sourceforge.net/project/showfiles.php?group_id=55859
and click the little "monitor package" icon/link.  If you're
previously signed up for the mailing list, be aware that it has
been discontinued, only the automated Sourceforge notification
will be used from now on.



What does getID3() do?
===========================================================================

Reads & parses (to varying degrees):
 ¤ tags:
  * APE (v1 and v2)
  * ID3v1 (& ID3v1.1)
  * ID3v2 (v2.4, v2.3, v2.2)
  * Lyrics3 (v1 & v2)

 ¤ audio-lossy:
  * MP3/MP2/MP1
  * MPC / Musepack
  * Ogg (Vorbis, OggFLAC, Speex)
  * AAC / MP4
  * AC3
  * DTS
  * RealAudio
  * Speex
  * DSS
  * VQF

 ¤ audio-lossless:
  * AIFF
  * AU
  * Bonk
  * CD-audio (*.cda)
  * FLAC
  * LA (Lossless Audio)
  * LiteWave
  * LPAC
  * MIDI
  * Monkey's Audio
  * OptimFROG
  * RKAU
  * Shorten
  * TTA
  * VOC
  * WAV (RIFF)
  * WavPack

 ¤ audio-video:
  * ASF: ASF, Windows Media Audio (WMA), Windows Media Video (WMV)
  * AVI (RIFF)
  * Flash
  * Matroska (MKV)
  * MPEG-1 / MPEG-2
  * NSV (Nullsoft Streaming Video)
  * Quicktime (including MP4)
  * RealVideo

 ¤ still image:
  * BMP
  * GIF
  * JPEG
  * PNG
  * TIFF
  * SWF (Flash)
  * PhotoCD

 ¤ data:
  * ISO-9660 CD-ROM image (directory structure)
  * SZIP (limited support)
  * ZIP (directory structure)
  * TAR
  * CUE


Writes:
  * ID3v1 (& ID3v1.1)
  * ID3v2 (v2.3 & v2.4)
  * VorbisComment on OggVorbis
  * VorbisComment on FLAC (not OggFLAC)
  * APE v2
  * Lyrics3 (delete only)



Requirements
===========================================================================

* PHP 4.2.0 up to 5.2.x for getID3() 1.7.x (and earlier)
* PHP 5.0.5 (or higher) for getID3() 1.8.x (and up)
* PHP 5.0.5 (or higher) for getID3() 2.0.x (and up)
* at least 4MB memory for PHP. 8MB or more is highly recommended.
  12MB is required with all modules loaded.



Usage
===========================================================================

See /demos/demo.basic.php for a very basic use of getID3() with no
fancy output, just scanning one file.

See structure.txt for the returned data structure.

*>  For an example of a complete directory-browsing,       <*
*>  file-scanning implementation of getID3(), please run   <*
*>  /demos/demo.browse.php                                 <*

See /demos/demo.mysql.php for a sample recursive scanning code that
scans every file in a given directory, and all sub-directories, stores
the results in a database and allows various analysis / maintenance
operations

To analyze remote files over HTTP or FTP you need to copy the file
locally first before running getID3(). Your code would look something
like this:

// Copy remote file locally to scan with getID3()
$remotefilename = 'http://www.example.com/filename.mp3';
if ($fp_remote = fopen($remotefilename, 'rb')) {
    $localtempfilename = tempnam('/tmp', 'getID3');
    if ($fp_local = fopen($localtempfilename, 'wb')) {
        while ($buffer = fread($fp_remote, 8192)) {
            fwrite($fp_local, $buffer);
        }
        fclose($fp_local);

		// Initialize getID3 engine
		$getID3 = new getID3;

		$ThisFileInfo = $getID3->analyze($filename);

        // Delete temporary file
        unlink($localtempfilename);
    }
    fclose($fp_remote);
}


See /demos/demo.write.php for how to write tags.



What does the returned data structure look like?
===========================================================================

See structure.txt

It is recommended that you look at the output of
/demos/demo.browse.php scanning the file(s) you're interested in to
confirm what data is actually returned for any particular filetype in
general, and your files in particular, as the actual data returned
may vary considerably depending on what information is available in
the file itself.



Notes
===========================================================================

getID3() 1.x:
If the format parser encounters a critical problem, it will return
something in $fileinfo['error'], describing the encountered error. If
a less critical error or notice is generated it will appear in
$fileinfo['warning']. Both keys may contain more than one warning or
error. If something is returned in ['error'] then the file was not
correctly parsed and returned data may or may not be correct and/or
complete. If something is returned in ['warning'] (and not ['error'])
then the data that is returned is OK - usually getID3() is reporting
errors in the file that have been worked around due to known bugs in
other programs. Some warnings may indicate that the data that is
returned is OK but that some data could not be extracted due to
errors in the file.

getID3() 2.x:
See above except errors are thrown (so you will only get one error).



Disclaimer
===========================================================================

getID3() has been tested on many systems, on many types of files,
under many operating systems, and is generally believe to be stable
and safe. That being said, there is still the chance there is an
undiscovered and/or unfixed bug that may potentially corrupt your
file, especially within the writing functions. By using getID3() you
agree that it's not my fault if any of your files are corrupted.
In fact, I'm not liable for anything :)



License
===========================================================================

GNU General Public License - see license.txt

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to:
Free Software Foundation, Inc.
59 Temple Place - Suite 330
Boston, MA  02111-1307, USA.

FAQ:
Q: Can I use getID3() in my program? Do I need a commercial license?
A: You're generally free to use getID3 however you see fit. The only
   case in which you would require a commercial license is if you're
   selling your closed-source program that integrates getID3. If you
   sell your program including a copy of getID3, that's fine as long
   as you include a copy of the sourcecode when you sell it.  Or you
   can distribute your code without getID3 and say "download it from
   getid3.sourceforge.net"



Why is it called "getID3()" if it does so much more than just that?
===========================================================================

v0.1 did in fact just do that. I don't have a copy of code that old, but I
could essentially write it today with a one-line function:
  function getID3($filename) { return unpack('a3TAG/a30title/a30artist/a30album/a4year/a28comment/c1track/c1genreid', substr(file_get_contents($filename), -128)); }


Future Plans
===========================================================================
http://www.getid3.org/phpBB3/viewforum.php?f=7

* Better support for MP4 container format
* Scan for appended ID3v2 tag at end of file per ID3v2.4 specs (Section 5.0)
* Support for JPEG-2000 (http://www.morgan-multimedia.com/jpeg2000_overview.htm)
* Support for MOD (mod/stm/s3m/it/xm/mtm/ult/669)
* Support for ACE (thanks Vince)
* Support for Ogg other than Vorbis, Speex and OggFlac (ie. Ogg+Xvid)
* Ability to create Xing/LAME VBR header for VBR MP3s that are missing VBR header
* Ability to "clean" ID3v2 padding (replace invalid padding with valid padding)
* Warn if MP3s change version mid-stream (in full-scan mode)
* check for corrupt/broken mid-file MP3 streams in histogram scan
* Support for lossless-compression formats
  (http://www.firstpr.com.au/audiocomp/lossless/#Links)
  (http://compression.ca/act-sound.html)
  (http://web.inter.nl.net/users/hvdh/lossless/lossless.htm)
* Support for RIFF-INFO chunks
  * http://lotto.st-andrews.ac.uk/~njh/tag_interchange.html
    (thanks Nick Humfrey <njhØsurgeradio*co*uk>)
  * http://abcavi.narod.ru/sof/abcavi/infotags.htm
    (thanks Kibi)
* Better support for Bink video
* http://www.hr/josip/DSP/AudioFile2.html
* http://www.pcisys.net/~melanson/codecs/
* Detect mp3PRO
* Support for PSD
* Support for JPC
* Support for JP2
* Support for JPX
* Support for JB2
* Support for IFF
* Support for ICO
* Support for ANI
* Support for EXE (comments, author, etc) (thanks p*quaedackersØplanet*nl)
* Support for DVD-IFO (region, subtitles, aspect ratio, etc)
  (thanks p*quaedackersØplanet*nl)
* More complete support for SWF - parsing encapsulated MP3 and/or JPEG content
    (thanks n8n8Øyahoo*com)
* Support for a2b
* Optional scan-through-frames for AVI verification
  (thanks rockcohenØmassive-interactive*nl)
* Support for TTF (thanks infoØbutterflyx*com)
* Support for DSS (http://www.getid3.org/phpBB3/viewtopic.php?t=171)
* Support for SMAF (http://smaf-yamaha.com/what/demo.html)
  http://www.getid3.org/phpBB3/viewtopic.php?t=182
* Support for AMR (http://www.getid3.org/phpBB3/viewtopic.php?t=195)
* Support for 3gpp (http://www.getid3.org/phpBB3/viewtopic.php?t=195)
* Support for ID4 (http://www.wackysoft.cjb.net grizlyY2KØhotmail*com)
* Parse XML data returned in Ogg comments
* Parse XML data from Quicktime SMIL metafiles (klausrathØmac*com)
* ID3v2 genre string creator function
* More complete parsing of JPG
* Support for all old-style ASF packets
* ASF/WMA/WMV tag writing
* Parse declared T??? ID3v2 text information frames, where appropriate
    (thanks Christian Fritz for the idea)
* Recognize encoder:
  http://www.guerillasoft.com/EncSpot2/index.html
  http://ff123.net/identify.html
  http://www.hydrogenaudio.org/?act=ST&f=16&t=9414
  http://www.hydrogenaudio.org/?showtopic=11785
* Support for other OS/2 bitmap structures: Bitmap Array('BA'),
  Color Icon('CI'), Color Pointer('CP'), Icon('IC'), Pointer ('PT')
  http://netghost.narod.ru/gff/graphics/summary/os2bmp.htm
* Support for WavPack RAW mode
* ASF/WMA/WMV data packet parsing
* ID3v2FrameFlagsLookupTagAlter()
* ID3v2FrameFlagsLookupFileAlter()
* obey ID3v2 tag alter/preserve/discard rules
* http://www.geocities.com/SiliconValley/Sector/9654/Softdoc/Illyrium/Aolyr.htm
* proper checking for LINK/LNK frame validity in ID3v2 writing
* proper checking for ASPI-TLEN frame validity in ID3v2 writing
* proper checking for COMR frame validity in ID3v2 writing
* http://www.geocities.co.jp/SiliconValley-Oakland/3664/index.html
* decode GEOB ID3v2 structure as encoded by RealJukebox,
  decode NCON ID3v2 structure as encoded by MusicMatch
  (probably won't happen - the formats are proprietary)



Known Bugs/Issues in getID3() that may be fixed eventually
===========================================================================
http://www.getid3.org/phpBB3/viewtopic.php?t=25

* Cannot determine bitrate for MPEG video with VBR video data
  (need documentation)
* Interlace/progressive cannot be determined for MPEG video
  (need documentation)
* MIDI playtime is sometimes inaccurate
* AAC-RAW mode files cannot be identified
* WavPack-RAW mode files cannot be identified
* mp4 files report lots of "Unknown QuickTime atom type"
   (need documentation)
* Encrypted ASF/WMA/WMV files warn about "unhandled GUID
  ASF_Content_Encryption_Object"
* Bitrate split between audio and video cannot be calculated for
  NSV, only the total bitrate. (need documentation)
* All Ogg formats (Vorbis, OggFLAC, Speex) are affected by the
  problem of large VorbisComments spanning multiple Ogg pages, but
  but only OggVorbis files can be processed with vorbiscomment.
* The version of "head" supplied with Mac OS 10.2.8 (maybe other
  versions too) does only understands a single option (-n) and
  therefore fails. getID3 ignores this and returns wrong md5_data.



Known Bugs/Issues in getID3() that cannot be fixed
--------------------------------------------------
http://www.getid3.org/phpBB3/viewtopic.php?t=25

* 32-bit PHP installations only:
  Files larger than 2GB cannot always be parsed fully by getID3()
  due to limitations in the 32-bit PHP filesystem functions.
  NOTE: Since v1.7.8b3 there is partial support for larger-than-
  2GB files, most of which will parse OK, as long as no critical
  data is located beyond the 2GB offset.
  Known will-work:
  * all file formats on 64-bit PHP
  * ZIP  (format doesn't support files >2GB)
  * FLAC (current encoders don't support files >2GB)
  Known will-not-work:
  * ID3v1 tags (always located at end-of-file)
  * Lyrics3 tags (always located at end-of-file)
  * APE tags (always located at end-of-file)
  Maybe-will-work:
  * Quicktime (will work if needed metadata is before 2GB offset,
    that is if the file has been hinted/optimized for streaming)
  * RIFF.WAV (should work fine, but gives warnings about not being
    able to parse all chunks)
  * RIFF.AVI (playtime will probably be wrong, is only based on
    "movi" chunk that fits in the first 2GB, should issue error
    to show that playtime is incorrect. Other data should be mostly
    correct, assuming that data is constant throughout the file)
* PHP <= v5 on Windows cannot read UTF-8 filenames


Known Bugs/Issues in other programs
-----------------------------------
http://www.getid3.org/phpBB3/viewtopic.php?t=25

* Windows Media Player (up to v11) and iTunes (up to v10+) do
    not correctly handle ID3v2.3 tags with UTF-16BE+BOM
    encoding (they assume the data is UTF-16LE+BOM and either
    crash (WMP) or output Asian character set (iTunes)
* Winamp (up to v2.80 at least) does not support ID3v2.4 tags,
    only ID3v2.3
    see: http://forums.winamp.com/showthread.php?postid=387524
* Some versions of Helium2 (www.helium2.com) do not write
    ID3v2.4-compliant Frame Sizes, even though the tag is marked
    as ID3v2.4)  (detected by getID3())
* MP3ext V3.3.17 places a non-compliant padding string at the end
    of the ID3v2 header. This is supposedly fixed in v3.4b21 but
    only if you manually add a registry key. This fix is not yet
    confirmed.  (detected by getID3())
* CDex v1.40 (fixed by v1.50b7) writes non-compliant Ogg comment
    strings, supposed to be in the format "NAME=value" but actually
    written just "value"  (detected by getID3())
* Oggenc 0.9-rc3 flags the encoded file as ABR whether it's
    actually ABR or VBR.
* iTunes (versions "X v2.0.3", "v3.0.1" are known-guilty, probably
    other versions are too) writes ID3v2.3 comment tags using a
    frame name 'COM ' which is not valid for ID3v2.3+ (it's an
    ID3v2.2-style frame name)  (detected by getID3())
* MP2enc does not encode mono CBR MP2 files properly (half speed
    sound and double playtime)
* MP2enc does not encode mono VBR MP2 files properly (actually
    encoded as stereo)
* tooLAME does not encode mono VBR MP2 files properly (actually
    encoded as stereo)
* AACenc encodes files in VBR mode (actually ABR) even if CBR is
   specified
* AAC/ADIF - bitrate_mode = cbr for vbr files
* LAME 3.90-3.92 prepends one frame of null data (space for the
  LAME/VBR header, but it never gets written) when encoding in CBR
  mode with the DLL
* Ahead Nero encodes TwinVQF with a DSIZ value (which is supposed
  to be the filesize in bytes) of "0" for TwinVQF v1.0 and "1" for
  TwinVQF v2.0  (detected by getID3())
* Ahead Nero encodes TwinVQF files 1 second shorter than they
  should be
* AAC-ADTS files are always actually encoded VBR, even if CBR mode
  is specified (the CBR-mode switches on the encoder enable ABR
  mode, not CBR as such, but it's not possible to tell the
  difference between such ABR files and true VBR)
* STREAMINFO.audio_signature in OggFLAC is always null. "The reason
  it's like that is because there is no seeking support in
  libOggFLAC yet, so it has no way to go back and write the
  computed sum after encoding. Seeking support in Ogg FLAC is the
  #1 item for the next release." - Josh Coalson (FLAC developer)
  NOTE: getID3() will calculate md5_data in a method similar to
  other file formats, but that value cannot be compared to the
  md5_data value from FLAC data in a FLAC file format.
* STREAMINFO.audio_signature is not calculated in FLAC v0.3.0 &
  v0.4.0 - getID3() will calculate md5_data in a method similar to
  other file formats, but that value cannot be compared to the
  md5_data value from FLAC v0.5.0+
* RioPort (various versions including 2.0 and 3.11) tags ID3v2 with
  a WCOM frame that has no data portion
* Earlier versions of Coolplayer adds illegal ID3 tags to Ogg Vorbis
  files, thus making them corrupt.
* Meracl ID3 Tag Writer v1.3.4 (and older) incorrectly truncates the
  last byte of data from an MP3 file when appending a new ID3v1 tag.
  (detected by getID3())
* Lossless-Audio files encoded with and without the -noseek switch
  do actually differ internally and therefore cannot match md5_data
* iTunes has been known to append a new ID3v1 tag on the end of an
  existing ID3v1 tag when ID3v2 tag is also present
  (detected by getID3())
* MediaMonkey may write a blank RGAD ID3v2 frame but put actual
  replay gain adjustments in a series of user-defined TXXX frames
  (detected and handled by getID3() since v1.9.2)




Reference material:
===========================================================================

[www.id3.org material now mirrored at http://id3lib.sourceforge.net/id3/]
* http://www.id3.org/id3v2.4.0-structure.txt
* http://www.id3.org/id3v2.4.0-frames.txt
* http://www.id3.org/id3v2.4.0-changes.txt
* http://www.id3.org/id3v2.3.0.txt
* http://www.id3.org/id3v2-00.txt
* http://www.id3.org/mp3frame.html
* http://minnie.tuhs.org/pipermail/mp3encoder/2001-January/001800.html <mathewhendry@hotmail.com>
* http://www.dv.co.yu/mpgscript/mpeghdr.htm
* http://www.mp3-tech.org/programmer/frame_header.html
* http://users.belgacom.net/gc247244/extra/tag.html
* http://gabriel.mp3-tech.org/mp3infotag.html
* http://www.id3.org/iso4217.html
* http://www.unicode.org/Public/MAPPINGS/ISO8859/8859-1.TXT
* http://www.xiph.org/ogg/vorbis/doc/framing.html
* http://www.xiph.org/ogg/vorbis/doc/v-comment.html
* http://leknor.com/code/php/class.ogg.php.txt
* http://www.id3.org/iso639-2.html
* http://www.id3.org/lyrics3.html
* http://www.id3.org/lyrics3200.html
* http://www.psc.edu/general/software/packages/ieee/ieee.html
* http://www.scri.fsu.edu/~jac/MAD3401/Backgrnd/ieee-expl.html
* http://www.scri.fsu.edu/~jac/MAD3401/Backgrnd/binary.html
* http://www.jmcgowan.com/avi.html
* http://www.wotsit.org/
* http://www.herdsoft.com/ti/davincie/davp3xo2.htm
* http://www.mathdogs.com/vorbis-illuminated/bitstream-appendix.html
* "Standard MIDI File Format" by Dustin Caldwell (from www.wotsit.org)
* http://midistudio.com/Help/GMSpecs_Patches.htm
* http://www.xiph.org/archives/vorbis/200109/0459.html
* http://www.replaygain.org/
* http://www.lossless-audio.com/
* http://download.microsoft.com/download/winmediatech40/Doc/1.0/WIN98MeXP/EN-US/ASF_Specification_v.1.0.exe
* http://mediaxw.sourceforge.net/files/doc/Active%20Streaming%20Format%20(ASF)%201.0%20Specification.pdf
* http://www.uni-jena.de/~pfk/mpp/sv8/ (archived at http://www.hydrogenaudio.org/musepack/klemm/www.personal.uni-jena.de/~pfk/mpp/sv8/)
* http://jfaul.de/atl/
* http://www.uni-jena.de/~pfk/mpp/ (archived at http://www.hydrogenaudio.org/musepack/klemm/www.personal.uni-jena.de/~pfk/mpp/)
* http://www.libpng.org/pub/png/spec/png-1.2-pdg.html
* http://www.real.com/devzone/library/creating/rmsdk/doc/rmff.htm
* http://www.fastgraph.com/help/bmp_os2_header_format.html
* http://netghost.narod.ru/gff/graphics/summary/os2bmp.htm
* http://flac.sourceforge.net/format.html
* http://www.research.att.com/projects/mpegaudio/mpeg2.html
* http://www.audiocoding.com/wiki/index.php?page=AAC
* http://libmpeg.org/mpeg4/doc/w2203tfs.pdf
* http://www.geocities.com/xhelmboyx/quicktime/formats/qtm-layout.txt
* http://developer.apple.com/techpubs/quicktime/qtdevdocs/RM/frameset.htm
* http://www.nullsoft.com/nsv/
* http://www.wotsit.org/download.asp?f=iso9660
* http://sandbox.mc.edu/~bennet/cs110/tc/tctod.html
* http://www.cdroller.com/htm/readdata.html
* http://www.speex.org/manual/node10.html
* http://www.harmony-central.com/Computer/Programming/aiff-file-format.doc
* http://www.faqs.org/rfcs/rfc2361.html
* http://ghido.shelter.ro/
* http://www.ebu.ch/tech_t3285.pdf
* http://www.sr.se/utveckling/tu/bwf
* http://ftp.aessc.org/pub/aes46-2002.pdf
* http://cartchunk.org:8080/
* http://www.broadcastpapers.com/radio/cartchunk01.htm
* http://www.hr/josip/DSP/AudioFile2.html
* http://home.attbi.com/~chris.bagwell/AudioFormats-11.html
* http://www.pure-mac.com/extkey.html
* http://cesnet.dl.sourceforge.net/sourceforge/bonkenc/bonk-binary-format-0.9.txt
* http://www.headbands.com/gspot/
* http://www.openswf.org/spec/SWFfileformat.html
* http://j-faul.virtualave.net/
* http://www.btinternet.com/~AnthonyJ/Atari/programming/avr_format.html
* http://cui.unige.ch/OSG/info/AudioFormats/ap11.html
* http://sswf.sourceforge.net/SWFalexref.html
* http://www.geocities.com/xhelmboyx/quicktime/formats/qti-layout.txt
* http://www-lehre.informatik.uni-osnabrueck.de/~fbstark/diplom/docs/swf/Flash_Uncovered.htm
* http://developer.apple.com/quicktime/icefloe/dispatch012.html
* http://www.csdn.net/Dev/Format/graphics/PCD.htm
* http://tta.iszf.irk.ru/
* http://www.atsc.org/standards/a_52a.pdf
* http://www.alanwood.net/unicode/
* http://www.freelists.org/archives/matroska-devel/07-2003/msg00010.html
* http://www.its.msstate.edu/net/real/reports/config/tags.stats
* http://homepages.slingshot.co.nz/~helmboy/quicktime/formats/qtm-layout.txt
* http://brennan.young.net/Comp/LiveStage/things.html
* http://www.multiweb.cz/twoinches/MP3inside.htm
* http://www.geocities.co.jp/SiliconValley-Oakland/3664/alittle.html#GenreExtended
* http://www.mactech.com/articles/mactech/Vol.06/06.01/SANENormalized/
* http://www.unicode.org/unicode/faq/utf_bom.html
* http://tta.corecodec.org/?menu=format
* http://www.scvi.net/nsvformat.htm
* http://pda.etsi.org/pda/queryform.asp
* http://cpansearch.perl.org/src/RGIBSON/Audio-DSS-0.02/lib/Audio/DSS.pm
* http://trac.musepack.net/trac/wiki/SV8Specification
* http://wyday.com/cuesharp/specification.php
* http://www.sno.phy.queensu.ca/~phil/exiftool/TagNames/Nikon.html=== WordPress Native PHP Sessions ===
Contributors: getpantheon, outlandish josh, mpvanwinkle77, danielbachhuber
Tags: comments, sessions
Requires at least: 3.0.1
Tested up to: 4.9
Stable tag: 0.6.9
License: GPLv2 or later
License URI: http://www.gnu.org/licenses/gpl-2.0.html

Use native PHP sessions and stay horizontally scalable. Better living through superior technology.

== Description ==

[![Build Status](https://travis-ci.org/pantheon-systems/wp-native-php-sessions.svg?branch=master)](https://travis-ci.org/pantheon-systems/wp-native-php-sessions) [![CircleCI](https://circleci.com/gh/pantheon-systems/wp-native-php-sessions/tree/master.svg?style=svg)](https://circleci.com/gh/pantheon-systems/wp-native-php-sessions/tree/master)

WordPress core does not use PHP sessions, but sometimes they are required by your use-case, a plugin or theme.

This plugin implements PHP's native session handlers, backed by the WordPress database. This allows plugins, themes, and custom code to safely use PHP `$_SESSION`s in a distributed environment where PHP's default tempfile storage just won't work.

Note that primary development is on GitHub if you would like to contribute:

https://github.com/pantheon-systems/wp-native-php-sessions

== Installation ==

1. Upload to the `/wp-content/plugins/` directory
2. Activate the plugin through the 'Plugins' menu in WordPress

That's it!

== Contributing ==

The best way to contribute to the development of this plugin is by participating on the GitHub project:

https://github.com/pantheon-systems/wp-native-php-sessions

Pull requests and issues are welcome!

You may notice there are two sets of tests running, on two different services:

* Travis CI runs the [PHPUnit](https://phpunit.de/) test suite.
* Circle CI runs the [Behat](http://behat.org/) test suite against a Pantheon site, to ensure the plugin's compatibility with the Pantheon platform.

Both of these test suites can be run locally, with a varying amount of setup.

PHPUnit requires the [WordPress PHPUnit test suite](https://make.wordpress.org/core/handbook/testing/automated-testing/phpunit/), and access to a database with name `wordpress_test`. If you haven't already configured the test suite locally, you can run `bash bin/install-wp-tests.sh wordpress_test root '' localhost`.

Behat requires a Pantheon site. Once you've created the site, you'll need [install Terminus](https://github.com/pantheon-systems/terminus#installation), and set the `TERMINUS_TOKEN`, `TERMINUS_SITE`, and `TERMINUS_ENV` environment variables. Then, you can run `./bin/behat-prepare.sh` to prepare the site for the test suite.

== Frequently Asked Questions ==

= Why not use another session plugin? =

This implements the built-in PHP session handling functions, rather than introducing anything custom. That way you can use built-in language functions like the `$_SESSION` superglobal and `session_start()` in your code. Everything else will "just work".

= Why store them in the database? =

PHP's fallback default functionality is to allow sessions to be stored in a temporary file. This is what most code that invokes sessions uses by default, and in simple use-cases it works, which is why so many plugins do it.

However, if you intend to scale your application, local tempfiles are a dangerous choice. They are not shared between different instances of the application, producing erratic behavior that can be impossible to debug. By storing them in the database the state of the sessions is shared across all application instances.

== Troubleshooting ==

If you see an error like "Fatal error: session_start(): Failed to initialize storage module: user (path: ) in .../code/wp-content/plugins/plugin-that-uses-sessions/example.php on line 2" you likely have a plugin in the mu-plugins directory that is instantiating a session prior to this plugin loading. To fix, you will need to deactivate this plugin and instead load it via an mu-plugin that loads first, e.g. create an mu-plugin called 00.php and add a line in it to include the wp-native-php-sessions/pantheon-sessions.php file and the problem should disappear.


== Changelog ==

= 0.6.9 (May 15th, 2018) =
* Ensures `_pantheon_session_destroy()` uses a return value.

= 0.6.8 (May 4th, 2018) =
* Switches to `E_USER_WARNING` instead of `E_WARNING` when triggering errors.

= 0.6.7 (April 26th, 2018) =
* Disables plugin load when `WP_INSTALLING`, because session table creation breaks installation process.

= 0.6.6 (March 8th, 2018) =
* Restores session instantiation when WP-CLI is executing, because not doing so causes other problems.

= 0.6.5 (February 6th, 2018) =
* Disables session instantiation when `defined( 'WP_CLI' ) && WP_CLI` because sessions don't work on CLI.

= 0.6.4 (October 10th, 2017) =
* Triggers PHP error when plugin fails to write session to database.

= 0.6.3 (September 29th, 2017) =
* Returns false when we entirely fail to generate a session.

= 0.6.2 (June 6th, 2017) =
* Syncs session user id when a user logs in and logs out.

= 0.6.1 (May 25th, 2017) =
* Bug fix: Prevents warning session_write_close() expects exactly 0 parameters, 1 given.

= 0.6.0 (November 23rd, 2016) =
* Bug fix: Prevents PHP fatal error in `session_write_close()` by running on WordPress' `shutdown` action, before `$wpdb` destructs itself.
* Bug fix: Stores the actual user id in the sessions table, instead of `(bool) $user_id`.

= 0.5 =
* Compatibility with PHP 7.
* Adds `pantheon_session_expiration` filter to modify session expiration value.

= 0.4 = 
* Adjustment to `session_id()` behavior for wider compatibility
* Using superglobal for REQUEST_TIME as opposed to `time()`

= 0.3 = 
* Fixes issue related to WordPress plugin load order

= 0.1 =
* Initial release
=== Yoast SEO ===
Contributors: yoast, joostdevalk, tacoverdo, omarreiss, atimmer, jipmoors
Donate link: https://yoa.st/1up
License: GPLv3
License URI: http://www.gnu.org/licenses/gpl.html
Tags: SEO, XML sitemap, Google Search Console, Content analysis, Readability
Requires at least: 4.9
Tested up to: 5.0.3
Stable tag: 9.4
Requires PHP: 5.2.4

Improve your WordPress SEO: Write better content and have a fully optimized WordPress site using the Yoast SEO plugin.

== Description ==

### Yoast SEO: the #1 WordPress SEO plugin

Need some help with your search engine optimization? Need an SEO plugin that helps you reach for the stars? Yoast SEO is the original WordPress SEO plugin since 2008. It is the favorite tool of millions of users, ranging from the bakery around the corner to some of the most popular sites on the planet. With Yoast SEO, you get a solid toolset that helps you aim for that number one spot in the search results. Yoast: SEO for everyone.

Yoast SEO does everything in its power to please both visitors and search engine spiders. How? Below you’ll find a small sampling of the powers of Yoast SEO:

#### Taking care of your WordPress SEO

* The most advanced XML Sitemaps functionality at the push of a button.
* Full control over site breadcrumbs: add a piece of code and you’re good to go.
* Set canonical URLs to avoid duplicate content. Never have to worry about Google penalties again.
* Title and meta description templating for better branding and consistent snippets in the search results.
* **[Premium]** Expand Yoast SEO with the News SEO, Video SEO, Local SEO and WooCommerce SEO extensions.
* **[Premium]** Need help? Yoast SEO Premium users get 1 year free access to our awesome support team.

> Note: some features are Premium. Which means you need Yoast SEO Premium to unlock those features. You can [get Yoast SEO Premium here](https://yoa.st/1v8)!

#### Write killer content with Yoast SEO

* Content & SEO analysis: Invaluable tools to write SEO-friendly texts.
* The snippet preview shows you how your post or page will look in the search results - even on mobile. Yoast SEO Premium even has social media previews!
* **[Premium]** The Insights tool shows you what your text focuses on so you can keep your article in line with your keyphrases.
* **[Premium]** Synonyms & related keyphrases: Optimize your article for synonyms and related keyphrases.
* **[Premium]** Automatic internal linking suggestions: write your article and get automatic suggested posts to link to.

#### Keep your site in perfect shape

* Yoast SEO tunes the engine of your site so you can work on creating great content.
* Our cornerstone content and internal linking features help you optimize your site structure in a breeze.
* Integrates with Google Search Console: See how your site performs in the search engines and fix crawl errors.
* Manage SEO roles: Give your colleagues access to specific sections of the Yoast SEO plugin.
* Bulk editor: Make large-scale edits to your site.
* **[Premium]** Social previews to manage the way your page is shared on social networks like Facebook and Twitter.
* **[Premium]** Redirect manager: It keeps your site healthy by easily redirecting errors from Google Search Console, deleted pages and changed URLs.

### Premium support

The Yoast team does not always provide active support for the Yoast SEO plugin on the WordPress.org forums, as we prioritize our email support. One-on-one email support is available to people who [bought Yoast SEO Premium](https://yoa.st/1v8) only.

Note that the [Yoast SEO Premium](https://yoa.st/1v8) also has several extra features too, including the option to have synonyms and related keyphrases, internal linking suggestions, cornerstone content checks and a redirect manager, so it is well worth your investment!

You should also check out the [Yoast Local SEO](https://yoa.st/1uu), [Yoast News SEO](https://yoa.st/1uv) and [Yoast Video SEO](https://yoa.st/1uw) extensions to Yoast SEO. They work with the free version of Yoast SEO already, and these premium extensions of course come with support too.

### Bug reports

Bug reports for Yoast SEO are [welcomed on GitHub](https://github.com/Yoast/wordpress-seo). Please note GitHub is not a support forum, and issues that aren’t properly qualified as bugs will be closed.

### Further Reading

For more info on search engine optimization, check out the following:

* The [Yoast SEO Plugin](https://yoa.st/1v8) official homepage.
* The [Yoast SEO Knowledgebase](https://yoa.st/1va).
* [WordPress SEO - The definitive Guide by Yoast](https://yoa.st/1v6).
* Other [WordPress Plugins](https://yoa.st/1v9) by the same team.
* Follow Yoast on [Facebook](https://facebook.com/yoast) & [Twitter](https://twitter.com/yoast).

== Installation ==

=== From within WordPress ===

1. Visit 'Plugins > Add New'
1. Search for 'Yoast SEO'
1. Activate Yoast SEO from your Plugins page.
1. Go to "after activation" below.

=== Manually ===

1. Upload the `wordpress-seo` folder to the `/wp-content/plugins/` directory
1. Activate the Yoast SEO plugin through the 'Plugins' menu in WordPress
1. Go to "after activation" below.

=== After activation ===

1. You should see (a notice to start) the Yoast SEO configuration wizard.
1. Go through the configuration wizard and set up the plugin for your site.
1. You're done!

== Frequently Asked Questions ==

You'll find answers to many of your questions on [kb.yoast.com](https://yoa.st/1va).

== Screenshots ==

1. The Yoast SEO plugin general meta box. You'll see this on edit post pages, for posts, pages and custom post types.
2. Example of the SEO analysis functionality.
3. Example of the readability analysis functionality.
4. Overview of site-wide SEO problems and possible improvements.
5. Control over which features you want to use.
6. Easily import SEO data from other SEO plugins like All In One SEO pack, HeadSpace2 SEO and wpSEO.de.

== Changelog ==

= 9.4.0 =
Release Date: January 8th, 2019

Content analysis recalibration (beta):

* Adds a toggle feature for subscribing to the recalibration beta under SEO -> General -> Features.
* When the recalibration feature is enabled:
  * The single title assessment is added. This assessment makes sure that you don't use superfluous H1s in your text.
  * Assessments changes:
    * Keyphrase density: changes scoring schema to account for the length of the keyphrase and changes feedback strings so that we give feedback about the number of occurrences rather than a percentage.
    * Outbound links assessment: changes the scoring schema so that red bullet instead of an orange bullet is shown when you have no outbound links.
    * Image alt attributes: if there are at least 5 images, checks whether the alt tags contain the keyphrase or synoynyms in 30-70% of all images. If there are less than 5 images, 1 image with the keyphrase or synonym in the alt tag is still scored as good.
    * Keyphrase in title: function words preceding the exact match keyphrase are ignored when determining the position of the keyphrase in the title.
    * Keyphrase length: makes the scoring scheme less strict for languages that don't have function word support, so that for these languages keyphrases with 1-6 words are scored as green, 7-9 as orange, and more than 9 as red.
    * Keyphrase in subheading: only takes H2 and H3 level subheadings into account and changes the scoring schema so that 30%-75% of these subheadings need to include the keyphrase or its synonyms. In languages without function word support, a match is only counted if all the words from the keyphrase/synonym appear in the subheading.
    * Text length: on taxonomy pages, the recommended minimum text length is increased from 150 to 250 words.
  * Assessment removals:
    * The assessment checking the length or your URL.
    * The assessment checking whether your URL contains stopwords.

Enhancements:

* Improve accessibility of the analysis results.
* Improve accessibility of the Title Separator setting.
* Adds a new filter for adjacent-rel links: `wpseo_adjacent_rel_url`.

Bugfixes:

* Fixes a bug where special characters from certain word lists weren't correctly escaped when matched with a regex. This resulted in `eggs` being incorrectly matched as the transition word `e.g.`, for example.
* Fixes a bug where the search appearance setting for a custom content type named `profile` would have a broken layout.
* Fixes a bug where pagination elements were not shown in the Genesis theme.

Other:

* Uses method `is_simple_page` instead of `is_singular` in method robots. Props to: [stodorovic](https://github.com/stodorovic)
* Adds method `is_woocommerce_active` and check is woocommerce activate before registering hooks. Props to [stodorovic](https://github.com/stodorovic)
* Adds static variables to "cache" results of functions [`is_shop`](https://docs.woocommerce.com/wc-apidocs/function-is_shop.html) and [`wc_get_page_id`](https://docs.woocommerce.com/wc-apidocs/function-wc_get_page_id.html). Props to [stodorovic](https://github.com/stodorovic)
* Verifies that variable `post` is an instance of `WP_Post` in `WPSEO_Admin_Bar_Menu ::get_singular_post()`. Props to [@yingles](https://github.com/yingles).
* Improves strings to be more easily translated. Props to [pedro-mendonca](https://github.com/pedro-mendonca)
* The browser console now shows more descriptive error messages when something went wrong during analyses in the web worker.
* Avoids irrelevant warning and error in the WPEngine PHP Compatibility plugin.

= 9.3.0 =
Release Date: December 18th, 2018

Enhancements:

* Reapplies the markers in Gutenberg when the content changes to make sure they stay up-to-date.
* Changes the output of schema preventing unnecessary escaping of forward slashes, only available on sites running PHP 5.4 or higher.
* Changes the website schema `@id` attribute to include the home URL to be a unique identifier.
* Adds the page number to the breadcrumbs when an archived page is entered.
* Removes a redundant Edge-specific CSS fix for the tooltips in the post overview. Props [mkronenfeld](https://github.com/mkronenfeld).

Bugfixes:

* Fixes a bug where the 'Select primary category' label in the primary taxonomy picker would overlap the 'Add new category' button.
* Fixes a bug where the cornerstone filter was still visible with the metabox disabled.
* Fixes a bug where non-functional markers are shown for taxonomy pages.
* Fixes a bug where the `og:description` tag would remain empty after setting the author description.
* Fixes a bug where texts in the configuration wizard would overlap each other and break out of the columns in Internet Explorer 11. Props [DrGrimshaw](https://github.com/DrGrimshaw).
* Fixes a bug where keyphrases weren't recognized in the URL when the words in the URL were separated by underscore characters instead of hyphens.
* Fixes a bug that caused numbers to be stripped when marking a keyphrase containing a number, e.g. 'Yoast SEO 9.3'.
* Fixes a bug where the first tab of the metabox would be empty when using WordPress 4.8.x.
* Fixes a bug where private post types would have a sitemap with their 'private' entries.

Other:

* Implemented performance optimizations in FAQ and How To blocks.

= Earlier versions =

For the changelog of earlier versions, please refer to [the Yoast SEO changelog on yoast.com](https://yoa.st/yoast-seo-changelog)
=== WP Mail SMTP by WPForms ===
Contributors: wpforms, jaredatch, smub, slaFFik
Tags: smtp, wp mail smtp, wordpress smtp, gmail smtp, sendgrid smtp, mailgun smtp, mail, mailer, phpmailer, wp_mail, email, mailgun, sengrid, gmail, wp smtp
Requires at least: 3.6
Tested up to: 5.0
Stable tag: 1.4.1
Requires PHP: 5.3

The most popular WordPress SMTP and PHP Mailer plugin. Trusted by over 1 million sites.

== Description ==

= WordPress Mail SMTP Plugin =

Having problems with your WordPress site not sending emails? You're not alone. Over 1 million websites use WP Mail SMTP to fix their email deliverability issues.

WP Mail SMTP fixes your email deliverability by reconfiguring the wp_mail() PHP function to use a proper SMTP provider.

= What is SMTP? =

SMTP (Simple Mail Transfer Protocol) is an industry standard for sending emails. SMTP helps increase email deliverability by using proper authentication.

Popular email clients like Gmail, Yahoo, Outlook, etc are constantly improving their services to reduce email spam. One of the things their spam tools look for is whether an email is originating from the location it claims to be originating from.

If the proper authentication isn't there, then the emails either go in your SPAM folder or worst not get delivered at all.

This is a problem for a lot of WordPress sites because by default, WordPress uses the PHP mail function to send emails generated by WordPress or any contact form plugin like <a href="https://wpforms.com/" rel="friend">WPForms</a>.

The issue is that most <a href"http://www.wpbeginner.com/wordpress-hosting/" rel="friend">WordPress hosting companies</a> don't have their servers properly configured for sending PHP emails.

The combination of two causes your WordPress emails to not get delivered.

= How does WP Mail SMTP work? =

WP Mail SMTP plugin allows you to easily reconfigure the wp_mail() function to use a trusted SMTP provider.

This helps you fix all WordPress not sending email issues.

WP Mail SMTP plugin includes four different SMTP setup options:

1. Mailgun SMTP
2. SendGrid SMTP
3. Gmail SMTP
4. All Other SMTP

For all options, you can specify the "from name" and "email address" for outgoing emails.

Instead of having users use different SMTP plugins and workflows for different SMTP providers, we decided to bring it all in one. This is what makes WP Mail SMTP, the best SMTP solution for WordPress.

= Mailgun SMTP =

Mailgun SMTP is a popular SMTP service provider that allows you to send large quantities of emails. They allow you to send your first 10,000 emails for free every month.

WP Mail SMTP plugin offers a native integration with MailGun. All you have to do is connect your Mailgun account, and you will improve your email deliverability.

Read our <a href="https://wpforms.com/how-to-send-wordpress-emails-with-mailgun/" rel="friend">Mailgun documentation</a> for more details.

= Gmail SMTP =

Often bloggers and small business owners don't want to use third-party SMTP services. Well you can use your Gmail or G Suite account for SMTP emails.

This allows you to use your <a href="http://www.wpbeginner.com/beginners-guide/how-to-setup-a-professional-email-address-with-gmail-and-google-apps/" rel="friend">professional email address</a> and improve email deliverability.

Unlike other Gmail SMTP plugins, our Gmail SMTP option uses OAuth to authenticate your Google account, keeping your login information 100% secure.

Read our <a href="https://wpforms.com/how-to-securely-send-wordpress-emails-using-gmail-smtp/" rel="friend">Gmail documentation</a> for more details.

= SendGrid SMTP =

SendGrid has a free SMTP plan that you can use to send up to 100 emails per day. With our native SendGrid SMTP integration, you can easily and securely set up SendGrid SMTP on your WordPress site.

Read our <a href="https://wpforms.com/fix-wordpress-email-notifications-with-sendgrid/" rel="friend">SendGrid documentation</a> for more details.

= Other SMTP =

WP Mail SMTP plugin also works with all major email services such as Gmail, Yahoo, Outlook, Microsoft Live, and any other email sending service that offers SMTP.

You can set the following options:

* Specify an SMTP host.
* Specify an SMTP port.
* Choose SSL / TLS encryption.
* Choose to use SMTP authentication or not.
* Specify an SMTP username and password.

WP Mail SMTP also gives you the option to insert your password in your wp-config.php file, so it's not visible in your WordPress settings.

To see recommended settings for the popular services as well as troubleshooting tips, check out our <a href="https://wpforms.com/docs/how-to-set-up-smtp-using-the-wp-mail-smtp-plugin/" rel="friend">SMTP documentation</a>.

We hope that you find WP Mail SMTP plugin helpful.

= Credits =

WP Mail SMTP plugin was originally created by Callum Macdonald. It is now owned and maintained by the team behind <a href="https://wpforms.com/" rel="friend">WPForms</a> - the best drag & drop form builder for WordPress.

You can try the <a href="https://wordpress.org/plugins/wpforms-lite/" rel="friend">free version of WPForms plugin</a> to see why it's the best in the market.

= What's Next =

If you like this plugin, then please consider checking out our other popular plugins:

* <a href="http://optinmonster.com/" rel="friend" title="OptinMonster">OptinMonster</a> - Get More Email Subscribers
* <a href="https://www.monsterinsights.com/" rel="friend" title="MonsterInsights">MonsterInsights</a> - Best Google Analytics Plugin for WordPress

Visit <a href="http://www.wpbeginner.com/" rel="friend" title="WPBeginner">WPBeginner</a> to learn from our <a href="http://www.wpbeginner.com/category/wp-tutorials/" rel="friend" title="WordPress Tutorials">WordPress Tutorials</a> and find out about other <a href="http://www.wpbeginner.com/category/plugins/" rel="friend" title="Best WordPress Plugins">best WordPress plugins</a>.

== Installation ==

1. Install WP Mail SMTP by WPForms either via the WordPress.org plugin repository or by uploading the files to your server. (See instructions on <a href="http://www.wpbeginner.com/beginners-guide/step-by-step-guide-to-install-a-wordpress-plugin-for-beginners/" rel="friend">how to install a WordPress plugin</a>)
2. Activate WP Mail SMTP by WPForms.
3. Navigate to the Settings area of WP Mail SMTP in the WordPress admin.
4. Choose your SMTP option (Mailgun SMTP, SendGrid SMTP, Gmail SMTP, or Other SMTP) and follow the instructions to set it up.
5. Want to support us? Consider trying <a href="https://wpforms.com/?utm_source=wprepo&utm_medium=link&utm_campaign=liteversion" rel="friend" title="WPForms">WPForms Pro</a> - the best WordPress contact form plugin!

== Frequently Asked Questions ==

= Can I use this plugin to send email via Gmail, G Suite, Outlook.com, Office 365, Hotmail, Yahoo, or AOL SMTP? =

Yes! We have extensive documentation that covers setting up SMTP most popular email services.

<a href="https://wpforms.com/docs/how-to-set-up-smtp-using-the-wp-mail-smtp-plugin/" rel="friend">Read our docs</a> to see the correct SMTP settings for each service.

= Help! I need support or have an issue. =

Please read <a href="https://wordpress.org/support/topic/wp-mail-smtp-support-policy/">our support policy</a> for more information.

= I found a bug, now what? =

If you've stumbled upon a bug, the best place to report it is in the <a href="https://github.com/awesomemotive/wp-mail-smtp">WP Mail SMTP GitHub repository</a>. GitHub is where the plugin is actively developed, and posting there will get your issue quickly seen by our developers (myself and Slava). Once posted, we'll review your bug report and triage the bug. When creating an issue, the more details you can add to your report, the faster the bug can be solved.

= Can you add feature x, y or z to the plugin? =

Short answer: maybe.

By all means please contact us to discuss features or options you'd like to see added to the plugin. We can't guarantee to add all of them, but we will consider all sensible requests. We can be contacted here:
<a href="https://wpforms.com/contact/" rel="friend">https://wpforms.com/contact/</a>

== Screenshots ==

1. WP Mail SMTP Settings page
2. Gmail / G Suite settings
3. Mailgun settings
4. SendGrid settings
5. SMTP settings
6. Send a Test Email

== Changelog ==

= 1.4.1 - 2018-12-03 =
* Fixed: correctly process backslashes in SMTP passwords defined via constants.
* Changed: allow to send a Test Email when Default (none) mailer is selected in plugin settings.

= 1.4.0 - 2018-11-29 =
* Added: New option: Do Not Send - block emails from being sent.
* Added: New option: Send HTML or plain text emails when doing an Email Test.
* Added: New option: Mailgun region selection - US and EU (US is default to preserve compatibility).
* Fixed: Compatibility with WordPress 3.6+.
* Fixed: Compatibility with WordPress 5.0.
* Fixed: Constants usage is much more reliable now, works correctly on Multisite. Constants are global accross the whole network.
* Fixed: Preserve multipart emails when using Sendgrid/Mailgun mailers (were converted to HTML-only).
* Fixed: Security hardening.
* Changed: Prefill Email Test page From field with currently logged in user email.
* Changed: Update libraries: google/apiclient-services, google/auth, phpseclib/phpseclib and their dependecies.
* Changed: Display in debug output cURL version if Gmail mailing failed.
* Changed: Display in debug output OpenSSL version if it exists if Gmail/SMTP mailing failed.
* Changed: Display plugin version in dashboard error notice when emailing failed.
* Changed: Do not allow to send Test Email if mailer not configured properly.
* Changed: Notify in plugin admin area that Gmail doesn't allow to redefine From Name/Email etc.
* Changed: List all constants with descriptions in plugin main file: wp_mail_smtp.php.
* Changed: TGMPA: change descriptions from "Required" to "Recommended" (labels were incorrect).

= 1.3.3 - 2018-07-05 =
* Fixed: Compatibility with other plugins, that are using Google Service or Google Client classes.
* Changed: Optimize code loading.

= 1.3.2 - 2018-06-29 =
* Make sure that other plugins/themes are not conflicting with our TGMPA library.

= 1.3.1 - 2018-06-29 =
* Fixed: Other SMTP: Clear new Debug messages about failed email delivery on next successful email sending.
* Fixed: Introduce conditional autoloader to workaround Gmail PHP 5.5 requirement and its library compatibility issues vs PHP 5.3+ minimum viable plugin version.

= 1.3.0 - 2018-06-28 =
* Added: New option: force From Email rewrite regardless of the current value.
* Added: New option: force From Name rewrite regardless of the current value.
* Added: New option: remove all plugin data on plugin uninstall (when user deletes it).
* Added: Notify site admins in wp-admin area with a notice about last failed email delivery. Cleans up on successful delivery.
* Added: Notify site admins in wp-admin area with a notice about possible compatibility issues with other SMTP and email delivery plugins.
* Added: Improve User Debug Experience when doing Email Test - display helpful description and steps to fix the issue.
* Added: New users: provide default SMTP Port value for new users based on Encryption selection.
* Added: New users: notify about not configured plugin settings.
* Added: New users: Recommend free WPForms Lite plugin for those who don't have it.
* Added: SendGrid/Mailgun: provide support for multipart/alternative types of emails.
* Added: Gmail: new button to remove connection and to connect a new Google account.
* Fixed: Support plugin installation into /mu-plugins/ directory.
* Fixed: SendGrid: required text/plain part of email being the first one - fixes plain text emails not having links.
* Fixed: SendGrid and Mailgun: improperly sending plain text emails in html format.
* Fixed: SMTP Debug output was empty in some cases.
* Fixed: Compatibility with lots of other plugins that use Google Analytics library of different versions.
* Fixed: "client_id is empty" is no more a problem, should be fixed.
* Changed: For SendGrid and Mailgun allow using custom defined attachments names if present. Fallback to file name.
* Changed: Gmail: switch to a wider scope to prevent possible issues in certain circumstances.
* Changed: Remove whitespaces start/end of keys, secrets etc.
* Changed: Improved helpful description tests of various options.
* Changed: Improved plugin autoloading functionality.

= 1.2.5 - 2017-02-05 =
* Fixed: `Return path` can't be turned off.
* Fixed: `Authentication` sometimes can't be turned off.
* Fixed: `Auto TLS` sometimes can't be turned off.
* Fixed: BCC support for Gmail was broken.
* Fixed: Debug output improved to handle SELinux and grsecurity.
* Fixed: Strip slashes from plugin settings (useful for `From Name` option).
* Fixed: Change the way sanitization is done to prevent accidental removal of useful data.
* Fixed: Plugin activation will not overwrite settings back to defaults.
* Fixed: Properly set `Auto TLS` option on plugin activation.
* Fixed: Providers autoloading improved for certain Windows-based installs.
* Fixed: Use the proper path to load translations from plugin's `/languages` directory.
* Changed: Do not autoload on each page request plugin settings from WordPress options table.
* Changed: Do not autoload Pepipost classes unless it's saved as active mailer in settings.

= 1.2.4 - 2017-01-28 =
* Fixed: Improved escaping in debug reporting.

= 1.2.3 - 2017-01-22 =
* Fixed: Gmail tokens were reset after clicking Save Settings.
* Fixed: Slight typo in Gmail success message.

= 1.2.2 - 2017-12-27 =
* Fixed: Correctly handle Mailgun debug message for an incorrect api key.
* Fixed: Fatal error for Gmail and SMTP mailers with Nginx web-server (without Apache at all).
* Changed: Update X-Mailer emails header to show the real sender with a mailer and plugin version.

= 1.2.1 - 2017-12-21 =
* Fixed: Failed SMTP connections generate fatal errors.

= 1.2.0 - 2017-12-21 =
* Fixed: Decrease the factual minimum WordPress version from 3.9 to 3.6.
* Changed: Improve debug output for all mail providers.

= 1.1.0 - 2017-12-18 =
* Added: New option "Auto TLS" for SMTP mailer. Default is enabled. Migration routine for all sites.
* Changed: Improve debug output - clear styles and context-aware content.
* Changed: Better exceptions handling for Google authentication process.
* Changed: Do not sanitize passwords, api keys etc - as they may contain special characters in certain order and sanitization will break those values.
* Changed: Improve wording of some helpful texts inside plugin admin area.
* Fixed: Do not include certain files in dependency libraries that are not used by Google mailer. This should stop flagging plugin by Wordfence and VaultPress.
* Fixed: Constants usage is working now, to define the SMTP password, for example.
* Fixed: Notice for default mailer.

= 1.0.2 - 2017-12-12 =
* Fixed: PHPMailer using incorrect SMTPSecure value.

= 1.0.1 - 2017-12-12 =
* Fixed: Global POST processing conflict.

= 1.0.0 - 2017-12-12 =
* Added: Automatic migration tool to move options from older storage format to a new one.
* Added: Added Gmail & G Suite email provider integration - without your email and password.
* Added: Added SendGrid email provider integration - using the API key only.
* Added: Added Mailgun email provider integration - using the API key and configured domain only.
* Added: New compatibility mode - for PHP 5.2 old plugin will be loaded, for PHP 5.3 and higher - new version of admin area and new functionality.
* Changed: The new look of the admin area.
* Changed: SMTP password field now has "password" type.
* Changed: SMTP password field does not display real password at all when using constants in `wp-config.php` to define it.
* Changed: Escape properly all translations.
* Changed: More helpful test email content (with a mailer name).

= 0.11.2 - 2017-11-28 =
* Added: Setting to hide announcement feed.
* Changed: Announcement feed data.

= 0.11.1 - 2017-10-30 =
* Fixed: Older PHP compatibility fix.

= 0.11 - 2017-10-30 =
* Added: Helper description to Return Path option.
* Added: Filter `wp_mail_smtp_admin_test_email_smtp_debug` to increase the debug message verbosity.
* Added: PHP 5.2 notice.
* Added: Announcement feed.
* Changed: Localization fixes, proper locale name.
* Changed: Code style improvements and optimizations for both HTML and PHP.
* Changed: Inputs for emails now have a proper type `email`, instead of a generic `text`.
* Changed: Turn off `$phpmailer->SMTPAutoTLS` when `No encryption` option is set to prevent error while sending emails.
* Changed: Hide Pepipost for those who are not using it.
* Changed: WP CLI support improved.

= 0.10.1 =
* Addition of Pepipost and cleanup of admin page.

= 0.10.0 =
* Addition of Pepipost and cleanup of admin page.

= 0.9.6 =
* Minor security fix, sanitize test email address.

= 0.9.5 =
* Minor security fix, hat tip JD Grimes.

= 0.9.4 =
* Improvement to the test email function, very low priority update.

= 0.9.3 =
* Fixing reported issue with passing by reference. props Adam Conway

= 0.9.2 =
* Removing the deprecation notice.

= 0.9.1 =
* $phpmailer->language became protected in WP 3.2, no longer unset on debug output.

= 0.9.0 =
* Typo in the From email description.
* Removed changelog from plugin file, no need to duplicate it.
* Optionally set $phpmailer->Sender from from email, helps with sendmail / mail().

= 0.8.7 =
* Fix for a long standing bug that caused an error during plugin activation.

= 0.8.6 =
* The Settings link really does work this time, promise. Apologies for the unnecessary updates.

= 0.8.5 =
* Bugfix, the settings link on the Plugin page was broken by 0.8.4.

= 0.8.4 =
* Minor bugfix, remove use of esc_html() to improve backwards compatibility.
* Removed second options page menu props ovidiu.

= 0.8.3 =
* Bugfix, return WPMS_MAIL_FROM_NAME, props nacin.
* Add Settings link, props Mike Challis http://profiles.wordpress.org/MikeChallis/

= 0.8.2 =
* Bugfix, call phpmailer_init_smtp() correctly, props Sinklar.

= 0.8.1 =
* Internationalisation improvements.

= 0.8 =
* Added port, SSL/TLS, option whitelisting, validate_email(), and constant options.

= 0.7 =
* Added checks to only override the default from name / email

= 0.6 =
* Added additional SMTP debugging output

= 0.5.2 =
* Fixed a pre 2.3 bug to do with mail from

= 0.5.1 =
* Added a check to display a warning on versions prior to 2.3

= 0.5.0 =
* Upgraded to match 2.3 filters which add a second filter for from name

= 0.4.2 =
* Fixed a bug in 0.4.1 and added more debugging output

= 0.4.1 =
* Added $phpmailer->ErroInfo to the test mail output

= 0.4 =
* Added the test email feature and cleaned up some other bits and pieces

= 0.3.2 =
* Changed to use register_activation_hook for greater compatability

= 0.3.1 =
* Added readme for WP-Plugins.org compatability

= 0.3 =
* Various bugfixes and added From options

= 0.2 =
* Reworked approach as suggested by westi, added options page

= 0.1 =
* Initial approach, copying the wp_mail function and replacing it

== Upgrade Notice ==

= 0.10.1 =
Addition of Pepipost and cleanup of admin page.

= 0.10.0 =
Addition of Pepipost and cleanup of admin page.

= 0.9.6 =
Minor security fix, sanitize test email address.

= 0.9.5 =
Minor security fix, hat tip JD Grimes.

= 0.9.4 =
Improvement to the test email function, very low priority update.

= 0.9.3 =
Fixing reported issue with passing by reference.

= 0.9.2 =
Removing the deprecation notice.

= 0.9.1 =
Test mail functionality was broken on upgrade to 3.2, now restored.

= 0.9.0 =
Low priority upgrade. Improves the appearance of the options page.

= 0.8.7 =
Very low priority update. Fixes a bug that causes a spurious error during activation.

= 0.8.6 =
Low priority update. The Settings link was still broken in 0.8.5.

= 0.8.5 =
Minor bugfix correcting the Settings link bug introduced in 0.8.4. Very low priority update.

= 0.8.4 =
Minor bugfix for users using constants. Another very low priority upgrade. Apologies for the version creep.

= 0.8.3 =
Minor bugfix for users using constants. Very low priority upgrade.
=== Revision Control ===
Contributors: dd32
Tags: revisions, post, admin
Requires at least: 4.0
Stable tag: 2.3.2

Revision Control allows finer control over the Post Revision system included with WordPress

== Description ==

Revision Control is a plugin for WordPress which gives the user more control over the Revision functionality.

PLEASE NOTE: Active support for this plugin is no longer offered.

The plugin allows the user to set a site-global setting (Settings -> Revisions) for pages/posts to enable/disable/limit the number of revisions which are saved for the page/post. The user may change this setting on a per-page/post basis from the Revisions Meta box.

The plugin also allows the deletion of specific revisions via the Revisions post metabox.

== Upgrade Notice ==

= 2.3.2 =
PHP 7 compatability changes, Uses WordPress.org Language Packs for translations, Requires WordPress 4.0.

== Changelog ==

= 2.3.2 =
 * PHP 7 compatibility
 * Replaced bundled translations to support Language Packs, see https://translate.wordpress.org/projects/wp-plugins/revision-control to contribute

= 2.3.1 =
 * PHP compatability changes (PHP Strict mode warnings)
 * Fix the Revision Restore link (Are you sure you want to do this?)
 * Bumps the requirement to WordPress 4.0
 * Added a no-support note.

== Screenshots ==

1. The Revisions Meta box
2. Revision Controls global settings
=== Embedly ===

Contributors: Embedly
Tags: embed, oembed, video, image, pdf, card
Requires at least: 3.8
Tested up to: 4.9.4
Stable tag: 4.9.2
License: GPLv2
License URI: http://www.gnu.org/licenses/gpl-2.0.html

The Embedly Plugin extends Wordpress's auto-embed feature to give your blog more media types and style optons.

== Description ==

Enhance the default Wordpress embedding to get previews for any article,
including your own blog posts. You also get embeds for Gfycat, Twitch, Google
Maps, and Embedly’s growing list of [500+ supported
providers](http://embed.ly/providers).

You can customize the style of the embeds, to optimize for darker WP themes,
alignment, and width. In addition, social buttons can be added around the embeds
to make it easier to share content from your blog posts.

If you have an Embedly Cards account, you can link it to the plugin with your Embedly API key.  Not only does this remove branding from the cards, it also gives you access to analytics and viewer behaviors for most popular music and video player embeds (YouTube, Vimeo, Instagram, SoundCloud).  Find out how many people viewed your embeds for how long. To learn more about Embedly Cards please visit [our website](http://embed.ly/cards).

Using it is as simple as the default Wordpress embedding. Embed media by pasting its URL in a single line when writing a post

The plugin automatically displays an embed of the media in the Wordpress post
editor (for WP 4.0+).

Fair Warning: This plugin generates static HTML content for your posts.  After you deactivate
the plugin, that HTML will still remain behind in all posts where the plugin was used to create
embeds.


== Installation ==


Using the Plugin Manager

1. Click Plugins in the Wordpress Dashboard sidebar.

1. Click Add New.

1. Search for Embedly.

1. Click Install

1. Click Install Now

1. Click Activate Plugin

1. Create a new post and paste a URL. It will automatically turn into an embed.

1. (optional) Save your Embedly API key to link your Embedly Cards account for analytics and unbranding


Manually

1. Upload `embedly` to the `/wp-content/plugins/` directory

1. Activate the plugin through the 'Plugins' menu in WordPress

1. Go through the sign up flow as described above.



Multi-Site

1. Navigate to My Sites -> Network Admin

1. Follow Steps 1-5 in Using the Plugin Manager setup above, `Do not Network Activate`

1. Go to each site's dashboard and activate Embedly in Plugins section

1. Go through the sign up flow as described above.



== Frequently Asked Questions ==

=
Is this plugin for me?
=

Yes

=
Where do I get a key?
=

You can obtain a key when sign up for an Embedly account. You
can also get your key anytime by going to your [Embedly
account](http://app.embed.ly).

=
How do I embed "any" URL?
=

In the post editor, once the plugin is installed, paste in the URL you are
trying to embed.

=
What happens after I deactivate the plugin or delete my Embedly account?
=

Cards will remain active even if you delete the plugin and/or delete your Embedly account.  This happens
because after we generate a card for your post, it is converted into static HTML.  This HTML gets saved
to the post.  Removing the plugin has no effect on posts that were created in the past.

=
I updated a setting for an embed but the embed didn't reflect the change?
=

Advanced Settings only affect newly generated cards.  If you wish to change the appearance of a pre-existing
card, you will have to recreate the card in the post editor after making any settings changes.

=
Do I need a key?
=

No. An Embedly API key is optional. It's only required if you have an Embedly Cards account and you want to remove embedly branding or you want to view analytics about the content embedded on your posts.

=
What is your support email?
=

support@embed.ly

=
Do you support multi-site?
=

Yes, see steps above to install for multi-site.
Note: You will need to activate Embedly for each site.

=
Can the width and alignment be changed?
=
Yes! Both the width and alignment can be changed for embeds that use the plugin.
You can make these adjustments under Advanced Embed Settings in the Embedly
plugin settings in your Wordpress Dashboard.

=
Can I change the CSS of the embeds?
=

No, but you have a few options in styling under the Advanced Embed Settings section of
the Embedly plugin dashboard.

=
What options are there for styling the embeds?
=

You can change the width, alignment, and adjust the cards to work better for
darker themes.

=
How do I find more analytics?
=

You can view the full set of analytics on your embed by going to your account
dashboard.

=
How does this affect my SEO?
=

The embeds from the Embedly Wordpress plugin include title and description meta
information that can provide relevant information to search engines about the
embeds to boost SEO.

== Screenshots ==


1. Advanced Embed Settings

2. Writing a post and embedding.

3. Sample Post.


== Changelog ==

= 4.7.0 =

* Having an active app.embed.ly account is now optional to use the plugin! Users who want access to unbranded
card embeds and/or analytics can elect to input their Embedly API key in the plugin settings, but users who just want
to get started embedding no longer need to create an embedly account and activate the plugin.

= 4.0.9 =

* Improved plugin security.

= 4.0.6 =

* Embedly is not currently supporting historical analytics for embeds, but you can still see realtime views.
* Improves the implementation of javascript dependencies via the wp_enqueue_script api.

= 4.0 =

* Removed Embedly TinyMCE Button.
* Added Editor Preview URL functionality for all URLS (WP v4.0+)
* Redesigned Embedly Admin page
* All embeds will be generated as Embedly Cards

= 3.2 =

* Embedly TinyMCE dialog and dependencies managed server side.
* Refactor code to use class structure.
* Clean up deprecated SQL generation to make compliant with WP3.6 and above.

= 3.1.3 =

* Fix Add Post bug in IE.

= 3.1.2 =

* Enable Twitter WP OEmbed.

= 3.1 =

* Fixes issue with Embedly not loading on WP3.9.
* Load tiny_mce_popup_4_0.js when TinyMCE is v4.0.

= 3.0 =

* Upgrade Embedly TinyMce editor option to use Embedly Cards.

= 2.3.0 =

* Use TinyMCE provided by WP Core.
* Fixes issue with HTML editting and formatting.

= 2.2.2 =

* Change server side calls to HTTP to avoid issues.
* Disable rocketloader syntax.

= 2.2 =

* Update TinyMce Popup js to latest.
* Update to latest JQuery 1.10.2.
* Update Powered by link destination to code generator.
* Fix powered by logo for RSS generation.
* Add support for links to open in new window.

= 2.1.4 =

* Support for blogs using HTTPS.
* Steps for multi-site setup.

= 2.1.2 =

* Use wp-includes tiny_mce_popup.js
* Compatible with WP 3.5

= 2.1.1 =

* Providers save fix.

= 2.1 =

* Admin Redesign.
* embedly_settngs option for wp_options table.
* SQL optimizations.

= 2.0.9 =

* Fix for feature status check.

= 2.0.8 =

* Allow script tag embeds.

= 2.0.6 =

* Add Embedly providers on 'plugins_loaded' instead of 'init' and other tweaks

= 2.0.5 =

* Fixing the path to TinyMCE plugin.

= 2.0.4 =

* Updated flow for previewing and updating embeds.

* Improved previews for preview endpoint.

* Better error handling for loading plugin in Post Editor.

= 2.0.3 =

* Resolve issue with tag attributes getting stripped

* Resolve quirks with height getting set incorrectly

= 2.0.2 =

* Resolve conflict with WordPress image editing

= 2.0.1 =

* Resolves Rich Editor not showing up.

= 2.0 =

* Adds Embedly TinyMCE plugin to Rich Editor.

* Support for Embedly Key to Embed "any" URL.

= 1.0 =

A few fixes.

= 0.9 =

Initial Version



== Upgrade Notice ==

= 2.0 =

Embed "any" URL.

= 2.1 =

Admin Redesign.

= 2.2 =

Update tinymce and jquery libs.

= 3.0 =

Embedly rich post editor option now uses Embedly Cards layout.

= 3.1 =

Dynamically loading Embedly popup based on TinyMCE Version.

= 3.2 =

Refactor Embedly TinyMCE Dialog to generate via iframe request.
# Twenty Nineteen

[![Build Status](https://travis-ci.org/WordPress/twentynineteen.svg?branch=master)](https://travis-ci.org/WordPress/twentynineteen)

**Contributors:** the WordPress team  
**Requires at least:** WordPress 4.9.6  
**Tested up to:** WordPress 4.9.8  
**Version:** 1.0  
**License:** GPLv2 or later  
**License URI:** http://www.gnu.org/licenses/gpl-2.0.html  
**Tags:** one-column, flexible-header, accessibility-ready, custom-colors, custom-menu, custom-logo, editor-style, featured-images, footer-widgets, rtl-language-support, sticky-post, theme-options, threaded-comments, translation-ready

## Description

Twenty Nineteen is a Gutenberg-ready theme for WordPress.

## Installation

1. In your admin panel, go to Appearance -> Themes and click the 'Add New' button.
2. Type in Twenty Nineteen in the search form and press the 'Enter' key on your keyboard.
3. Click on the 'Activate' button to use your new theme right away.
4. Go to https://codex.wordpress.org/Twenty_Nineteen for a guide on how to customize this theme.
5. Navigate to Appearance > Customize in your admin panel and customize to taste.

## Copyright

Twenty Nineteen WordPress Theme, Copyright 2018 WordPress.org
Twenty Nineteen is distributed under the terms of the GNU GPL.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

Twenty Nineteen bundles the following third-party resources:

_s, Copyright 2015-2018 Automattic, Inc.
**License:** GPLv2 or later
Source: https://github.com/Automattic/_s/

normalize.css, Copyright 2012-2016 Nicolas Gallagher and Jonathan Neal
**License:** MIT
Source: https://necolas.github.io/normalize.css/

Bundled header image 1, Copyright XXXXX XXXXX
**License:** CC0 1.0 Universal (CC0 1.0)
Source: https://pexels.com/xxxxxxxxxx

Bundled header image 2, Copyright XXXXX XXXXX
**License:** CC0 1.0 Universal (CC0 1.0)
Source: https://pexels.com/xxxxxxxxxx

## Changelog

### 1.0

* Released: December 6, 2018

Initial release
Pantheon Plugin
=================

Building on Pantheon's and WordPress's strengths, together.

Workflow
--------
Integrates WordPress with Pantheon Flow. Encourages updating plugins and themes in the Development environment and using Pantheon's git-based upstream core updates.

Edge Cache
-----------
Facilitates communication between Pantheon's Edge Cache layer and WordPress. It allows you to set the default cache age, clear individual pages on demand, and it will automatically clear relevant urls when the site is updated. Authored by [Matthew Boynes](http://www.alleyinteractive.com/).
Pimple
======

.. caution::

    This is the documentation for Pimple 3.x. If you are using Pimple 1.x, read
    the `Pimple 1.x documentation`_. Reading the Pimple 1.x code is also a good
    way to learn more about how to create a simple Dependency Injection
    Container (recent versions of Pimple are more focused on performance).

Pimple is a small Dependency Injection Container for PHP.

Installation
------------

Before using Pimple in your project, add it to your ``composer.json`` file:

.. code-block:: bash

    $ ./composer.phar require pimple/pimple "^3.0"

Usage
-----

Creating a container is a matter of creating a ``Container`` instance:

.. code-block:: php

    use Pimple\Container;

    $container = new Container();

As many other dependency injection containers, Pimple manages two different
kind of data: **services** and **parameters**.

Defining Services
~~~~~~~~~~~~~~~~~

A service is an object that does something as part of a larger system. Examples
of services: a database connection, a templating engine, or a mailer. Almost
any **global** object can be a service.

Services are defined by **anonymous functions** that return an instance of an
object:

.. code-block:: php

    // define some services
    $container['session_storage'] = function ($c) {
        return new SessionStorage('SESSION_ID');
    };

    $container['session'] = function ($c) {
        return new Session($c['session_storage']);
    };

Notice that the anonymous function has access to the current container
instance, allowing references to other services or parameters.

As objects are only created when you get them, the order of the definitions
does not matter.

Using the defined services is also very easy:

.. code-block:: php

    // get the session object
    $session = $container['session'];

    // the above call is roughly equivalent to the following code:
    // $storage = new SessionStorage('SESSION_ID');
    // $session = new Session($storage);

Defining Factory Services
~~~~~~~~~~~~~~~~~~~~~~~~~

By default, each time you get a service, Pimple returns the **same instance**
of it. If you want a different instance to be returned for all calls, wrap your
anonymous function with the ``factory()`` method

.. code-block:: php

    $container['session'] = $container->factory(function ($c) {
        return new Session($c['session_storage']);
    });

Now, each call to ``$container['session']`` returns a new instance of the
session.

Defining Parameters
~~~~~~~~~~~~~~~~~~~

Defining a parameter allows to ease the configuration of your container from
the outside and to store global values:

.. code-block:: php

    // define some parameters
    $container['cookie_name'] = 'SESSION_ID';
    $container['session_storage_class'] = 'SessionStorage';

If you change the ``session_storage`` service definition like below:

.. code-block:: php

    $container['session_storage'] = function ($c) {
        return new $c['session_storage_class']($c['cookie_name']);
    };

You can now easily change the cookie name by overriding the
``cookie_name`` parameter instead of redefining the service
definition.

Protecting Parameters
~~~~~~~~~~~~~~~~~~~~~

Because Pimple sees anonymous functions as service definitions, you need to
wrap anonymous functions with the ``protect()`` method to store them as
parameters:

.. code-block:: php

    $container['random_func'] = $container->protect(function () {
        return rand();
    });

Modifying Services after Definition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In some cases you may want to modify a service definition after it has been
defined. You can use the ``extend()`` method to define additional code to be
run on your service just after it is created:

.. code-block:: php

    $container['session_storage'] = function ($c) {
        return new $c['session_storage_class']($c['cookie_name']);
    };

    $container->extend('session_storage', function ($storage, $c) {
        $storage->...();

        return $storage;
    });

The first argument is the name of the service to extend, the second a function
that gets access to the object instance and the container.

Extending a Container
~~~~~~~~~~~~~~~~~~~~~

If you use the same libraries over and over, you might want to reuse some
services from one project to the next one; package your services into a
**provider** by implementing ``Pimple\ServiceProviderInterface``:

.. code-block:: php

    use Pimple\Container;

    class FooProvider implements Pimple\ServiceProviderInterface
    {
        public function register(Container $pimple)
        {
            // register some services and parameters
            // on $pimple
        }
    }

Then, register the provider on a Container:

.. code-block:: php

    $pimple->register(new FooProvider());

Fetching the Service Creation Function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you access an object, Pimple automatically calls the anonymous function
that you defined, which creates the service object for you. If you want to get
raw access to this function, you can use the ``raw()`` method:

.. code-block:: php

    $container['session'] = function ($c) {
        return new Session($c['session_storage']);
    };

    $sessionFunction = $container->raw('session');

PSR-11 compatibility
--------------------

For historical reasons, the ``Container`` class does not implement the PSR-11
``ContainerInterface``. However, Pimple provides a helper class that will let
you decouple your code from the Pimple container class.

The PSR-11 container class
~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``Pimple\Psr11\Container`` class lets you access the content of an
underlying Pimple container using ``Psr\Container\ContainerInterface``
methods:

.. code-block:: php

    use Pimple\Container;
    use Pimple\Psr11\Container as PsrContainer;

    $container = new Container();
    $container['service'] = function ($c) {
        return new Service();
    };
    $psr11 = new PsrContainer($container);

    $controller = function (PsrContainer $container) {
        $service = $container->get('service');
    };
    $controller($psr11);

Using the PSR-11 ServiceLocator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes, a service needs access to several other services without being sure
that all of them will actually be used. In those cases, you may want the
instantiation of the services to be lazy.

The traditional solution is to inject the entire service container to get only
the services really needed. However, this is not recommended because it gives
services a too broad access to the rest of the application and it hides their
actual dependencies.

The ``ServiceLocator`` is intended to solve this problem by giving access to a
set of predefined services while instantiating them only when actually needed.

It also allows you to make your services available under a different name than
the one used to register them. For instance, you may want to use an object
that expects an instance of ``EventDispatcherInterface`` to be available under
the name ``event_dispatcher`` while your event dispatcher has been
registered under the name ``dispatcher``:

.. code-block:: php

    use Monolog\Logger;
    use Pimple\Psr11\ServiceLocator;
    use Psr\Container\ContainerInterface;
    use Symfony\Component\EventDispatcher\EventDispatcher;

    class MyService
    {
        /**
         * "logger" must be an instance of Psr\Log\LoggerInterface
         * "event_dispatcher" must be an instance of Symfony\Component\EventDispatcher\EventDispatcherInterface
         */
        private $services;

        public function __construct(ContainerInterface $services)
        {
            $this->services = $services;
        }
    }

    $container['logger'] = function ($c) {
        return new Monolog\Logger();
    };
    $container['dispatcher'] = function () {
        return new EventDispatcher();
    };

    $container['service'] = function ($c) {
        $locator = new ServiceLocator($c, array('logger', 'event_dispatcher' => 'dispatcher'));

        return new MyService($locator);
    };

Referencing a Collection of Services Lazily
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Passing a collection of services instances in an array may prove inefficient
if the class that consumes the collection only needs to iterate over it at a
later stage, when one of its method is called. It can also lead to problems
if there is a circular dependency between one of the services stored in the
collection and the class that consumes it.

The ``ServiceIterator`` class helps you solve these issues. It receives a
list of service names during instantiation and will retrieve the services
when iterated over:

.. code-block:: php

    use Pimple\Container;
    use Pimple\ServiceIterator;

    class AuthorizationService
    {
        private $voters;

        public function __construct($voters)
        {
            $this->voters = $voters;
        }

        public function canAccess($resource)
        {
            foreach ($this->voters as $voter) {
                if (true === $voter->canAccess($resource) {
                    return true;
                }
            }

            return false;
        }
    }

    $container = new Container();

    $container['voter1'] = function ($c) {
        return new SomeVoter();
    }
    $container['voter2'] = function ($c) {
        return new SomeOtherVoter($c['auth']);
    }
    $container['auth'] = function ($c) {
        return new AuthorizationService(new ServiceIterator($c, array('voter1', 'voter2'));
    }

.. _Pimple 1.x documentation: https://github.com/silexphp/Pimple/tree/1.1
Idiorm
======

[![Build Status](https://travis-ci.org/j4mie/idiorm.png?branch=master)](https://travis-ci.org/j4mie/idiorm) [![Latest Stable Version](https://poser.pugx.org/j4mie/idiorm/v/stable.png)](https://packagist.org/packages/j4mie/idiorm) [![Total Downloads](https://poser.pugx.org/j4mie/idiorm/downloads.png)](https://packagist.org/packages/j4mie/idiorm) [![Code Climate](https://codeclimate.com/github/j4mie/idiorm/badges/gpa.svg)](https://codeclimate.com/github/j4mie/idiorm)

[http://j4mie.github.com/idiormandparis/](http://j4mie.github.com/idiormandparis/)

---
### Feature complete

Idiorm is now considered to be feature complete as of version 1.5.0. Whilst it will continue to be maintained with bug fixes there will be no further new features added from this point on.

**Please do not submit feature requests or pull requests adding new features as they will be closed without ceremony.**

---

A lightweight nearly-zero-configuration object-relational mapper and fluent query builder for PHP5 and above.

Tested on PHP 5.2.0+ - may work on earlier versions with PDO and the correct database drivers.

Released under a [BSD license](http://en.wikipedia.org/wiki/BSD_licenses).

**See Also: [Paris](http://github.com/j4mie/paris), an Active Record implementation built on top of Idiorm.**

Features
--------

* Makes simple queries and simple CRUD operations completely painless.
* Gets out of the way when more complex SQL is required.
* Built on top of [PDO](http://php.net/pdo).
* Uses [prepared statements](http://uk.php.net/manual/en/pdo.prepared-statements.php) throughout to protect against [SQL injection](http://en.wikipedia.org/wiki/SQL_injection) attacks.
* Requires no model classes, no XML configuration and no code generation: works out of the box, given only a connection string.
* Consists of one main class called `ORM`. Additional classes are prefixed with `Idiorm`. Minimal global namespace pollution.
* Database agnostic. Currently supports SQLite, MySQL, Firebird and PostgreSQL. May support others, please give it a try!
* Supports collections of models with method chaining to filter or apply actions to multiple results at once.
* Multiple connections supported
* PSR-1 compliant methods (any method can be called in camelCase instead of underscores eg. `find_many()` becomes `findMany()`) - you'll need PHP 5.3+

Documentation
-------------

The documentation is hosted on Read the Docs: [idiorm.rtfd.org](http://idiorm.rtfd.org)

### Building the Docs ###

You will need to install [Sphinx](http://sphinx-doc.org/) and then in the docs folder run:

    make html

The documentation will now be in docs/_build/html/index.html

Let's See Some Code
-------------------

```php
$user = ORM::for_table('user')
    ->where_equal('username', 'j4mie')
    ->find_one();

$user->first_name = 'Jamie';
$user->save();

$tweets = ORM::for_table('tweet')
    ->select('tweet.*')
    ->join('user', array(
        'user.id', '=', 'tweet.user_id'
    ))
    ->where_equal('user.username', 'j4mie')
    ->find_many();

foreach ($tweets as $tweet) {
    echo $tweet->text;
}
```

Tests
-----

Tests are written with PHPUnit and be run through composer

    composer test

To make testing on PHP 5.2 (Idiorm maintains support back to this version of PHP) there
is a Docker setup in `./test/docker_for_php52` - check the readme in there for more.

Changelog
---------
#### 1.5.5 - released 2018-01-05

* Add a docker setup for testing with PHP 5.2 (uses PHPUnit 3.6.12, which is the last version released compatible with PHP 5.2) [Treffynnon](https://github.com/treffynnon)

#### 1.5.4 - released 2018-01-04

* Reset Idiorm state when a cached result is returned [[fayland](https://github.com/fayland) (and [Treffynnon](https://github.com/treffynnon))] - [issue #319](https://github.com/j4mie/idiorm/issues/319)
* Fix travis builds for PHP 5.2+ (adding 7.0 and 7.1) and document support for newer PHP versions [[Treffynnon](https://github.com/treffynnon)]
* Correct PHPDoc comments for `selectMany()` [[kawausokun](https://github.com/kawausokun)] - [issue #325](github.com/j4mie/idiorm/issues/325)
* Add pdo_sqlite to the composer require-dev dependencies [[qyanu](https://github.com/qyanu)] - [issue #328](github.com/j4mie/idiorm/issues/328)

#### 1.5.3 - released 2017-03-21

* Document the `raw_execute()` method and add a note for `get_db()` in the querying documentation - [[Treffynnon](https://github.com/treffynnon)]

#### 1.5.2 - released 2016-12-14

* Fix autoincremented compound keys inserts [[lrlopez](https://github.com/lrlopez)] - [issue #233](https://github.com/j4mie/idiorm/issues/233) and [pull #235](https://github.com/j4mie/idiorm/pull/235)
* Add @method tags for magic methods [[stellis](https://github.com/stellis)] - [issue #237](https://github.com/j4mie/idiorm/issues/237)
* Ensure `is_dirty()` returns correctly when fed null or an empty string [[tentwofour](https://github.com/tentwofour)] - [issue #268](https://github.com/j4mie/idiorm/issues/268)
* Adding Code Climate badge to the readme file [[e3betht](https://github.com/e3betht)] - [issue #260](https://github.com/j4mie/idiorm/issues/260)
* Typo in navigation [[leongersen](https://github.com/leongersen)] - [issue #257](https://github.com/j4mie/idiorm/issues/257)
* Support named placeholders logging and test [[m92o](https://github.com/m92o)] - [issue #223](https://github.com/j4mie/idiorm/issues/223)
* `having_id_is()` reference undefined variable `$value` [[Treffynnon](https://github.com/treffynnon)] - [issue #224](https://github.com/j4mie/idiorm/issues/224)
* Documentation fix - ORM query output for `where_any_is()` [[uovidiu](https://github.com/uovidiu)] - [issue #306](https://github.com/j4mie/idiorm/issues/306)
* Code style fix preventing nested loops from using the same variable names [[mkkeck](https://github.com/mkkeck)] - [issue #301](https://github.com/j4mie/idiorm/issues/301)
* Document shortcomings of the built in query logger [[Treffynnon](https://github.com/treffynnon)] - [issue #307](https://github.com/j4mie/idiorm/issues/307)
* Add phpunit to dev dependencies, add `composer test` script shortcut and fix PDO mock in test bootstrap [[Treffynnon](https://github.com/treffynnon)]
* New test for multiple raw where clauses [[Treffynnon](https://github.com/treffynnon)] - [issue #236](https://github.com/j4mie/idiorm/issues/236)
* Remove PHP 5.2 from travis-ci containers to test against (**note** Idiorm still supports PHP 5.2 despite this) [[Treffynnon](https://github.com/treffynnon)]

#### 1.5.1 - released 2014-06-23

* Binding of named parameters was broken [[cainmi](https://github.com/cainmi)] - [issue #221](https://github.com/j4mie/idiorm/pull/221)

#### 1.5.0 - released 2014-06-22

* Multiple OR'ed conditions support [[lrlopez](https://github.com/lrlopez)] - [issue #201](https://github.com/j4mie/idiorm/issues/201)
* `where_id_in()` for selecting multiple records by primary key [[lrlopez](https://github.com/lrlopez)] - [issue #202](https://github.com/j4mie/idiorm/issues/202)
* Add compound primary key support [[lrlopez](https://github.com/lrlopez)] - [issue #171](https://github.com/j4mie/idiorm/issues/171)
* Add a RAW JOIN source to the query [[moiseevigor](https://github.com/moiseevigor)] - [issue #163](https://github.com/j4mie/idiorm/issues/163)
* offsetExists() should return true for null values, resolves [#181](https://github.com/j4mie/idiorm/issues/181) [[cainmi](https://github.com/cainmi)] - [issue #214](https://github.com/j4mie/idiorm/pull/214)
* Custom cache callback functions [[peter-mw](https://github.com/peter-mw)] - [issue #216](https://github.com/j4mie/idiorm/pull/216)
* Restrict null primary keys on update/delete, resolves [#203](https://github.com/j4mie/idiorm/issues/203) [[cainmi](https://github.com/cainmi)] - [issue #205](https://github.com/j4mie/idiorm/issues/205) 
* Ensure parameters treated by type correctly [[charsleysa](https://github.com/charsleysa)] & [[SneakyBobito](https://github.com/SneakyBobito)] - [issue #206](https://github.com/j4mie/idiorm/issues/206) & [issue #208](https://github.com/j4mie/idiorm/issues/208)
* Reduce the type casting on aggregate functions to allow characters [[herroffizier](https://github.com/herroffizier)] - [issue #150](https://github.com/j4mie/idiorm/issues/150)
* Prevent invalid method calls from triggering infinite recursion [[michaelward82](https://github.com/michaelward82)] - [issue #152](https://github.com/j4mie/idiorm/issues/152)
* Add time to query logging - adds query time parameter to external logger callback function [[AgelxNash](https://github.com/AgelxNash)] - [issue #180](https://github.com/j4mie/idiorm/issues/180)
* Changed database array access to ensure it's always properly setup [[falmp](https://github.com/falmp)] - [issue #159](https://github.com/j4mie/idiorm/issues/159)
* Allow unsetting the db (`ORM::set_db(null)`) to make the test work again [[borrel](https://github.com/borrel)] - [issue #160](https://github.com/j4mie/idiorm/issues/160)
* Correct [issue #176](https://github.com/j4mie/idiorm/issues/176): Ensure database setup before building select [[kendru](https://github.com/kendru)] - [issue #197](https://github.com/j4mie/idiorm/issues/197)
* Add HHVM to travis-ci build matrix [[ptarjan](https://github.com/ptarjan)] - [issue #168](https://github.com/j4mie/idiorm/issues/168)
* Improve where statement precendence documentation [[thomasahle](https://github.com/thomasahle)] - [issue #190](https://github.com/j4mie/idiorm/issues/190)
* Improve testing checks [[charsleysa](https://github.com/charsleysa)] - [issue #173](https://github.com/j4mie/idiorm/issues/173)

#### 1.4.1 - released 2013-12-12

**Patch update to remove a broken pull request** - may have consequences for users of 1.4.0 that exploited the "`find_many()` now returns an associative array with the databases primary ID as the array keys" change that was merged in 1.4.0.

* Back out pull request/issue [#133](https://github.com/j4mie/idiorm/pull/133) as it breaks backwards compatibility in previously unexpected ways (see [#162](https://github.com/j4mie/idiorm/pull/162), [#156](https://github.com/j4mie/idiorm/issues/156) and [#133](https://github.com/j4mie/idiorm/pull/133#issuecomment-29063108)) - sorry for merging this change into Idiorm - closes [issue 156](https://github.com/j4mie/idiorm/issues/156)

#### 1.4.0 - released 2013-09-05

* `find_many()` now returns an associative array with the databases primary ID as the array keys [[Surt](https://github.com/Surt)] - [issue #133](https://github.com/j4mie/idiorm/issues/133)
* Calls to `set()` and `set_expr()` return `$this` allowing them to be chained [[Surt](https://github.com/Surt)]
* Add PSR-1 compliant camelCase method calls to Idiorm (PHP 5.3+ required) [[crhayes](https://github.com/crhayes)] - [issue #108](https://github.com/j4mie/idiorm/issues/108)
* Add static method `get_config()` to access current configuration [[javierd](https://github.com/mikejestes)] - [issue #141](https://github.com/j4mie/idiorm/issues/141)
* Add logging callback functionality [[lalop](https://github.com/lalop)] - [issue #130](https://github.com/j4mie/idiorm/issues/130)
* Add support for MS SQL ``TOP`` limit style (automatically used for PDO drivers: sqlsrv, dblib and mssql) [[numkem](https://github.com/numkem)] - [issue #116](https://github.com/j4mie/idiorm/issues/116)
* Uses table aliases in `WHERE` clauses [[vicvicvic](https://github.com/vicvicvic)] - [issue #140](https://github.com/j4mie/idiorm/issues/140)
* Ignore result columns when calling an aggregate function [[tassoevan](https://github.com/tassoevan)] - [issue #120](https://github.com/j4mie/idiorm/issues/120)
* Improve documentation [[bruston](https://github.com/bruston)] - [issue #111](https://github.com/j4mie/idiorm/issues/111)
* Improve PHPDoc on `get_db()` [[mailopl](https://github.com/mailopl)] - [issue #106](https://github.com/j4mie/idiorm/issues/106)
* Improve documentation [[sjparsons](https://github.com/sjparsons)] - [issue #103](https://github.com/j4mie/idiorm/issues/103)
* Make tests/bootstrap.php HHVM compatible [[JoelMarcey](https://github.com/JoelMarcey)] - [issue #143](https://github.com/j4mie/idiorm/issues/143)
* Fix docblock [[ulrikjohansson](https://github.com/ulrikjohansson)] - [issue #147](https://github.com/j4mie/idiorm/issues/147)
* Fix incorrect variable name in querying documentation [[fridde](https://github.com/fridde)] - [issue #146](https://github.com/j4mie/idiorm/issues/146)

#### 1.3.0 - released 2013-01-31

* Documentation moved to [idiorm.rtfd.org](http://idiorm.rtfd.org) and now built using [Sphinx](http://sphinx-doc.org/)
* Add support for multiple database connections - closes [issue #15](https://github.com/j4mie/idiorm/issues/15) [[tag](https://github.com/tag)]
* Add in raw_execute - closes [issue #40](https://github.com/j4mie/idiorm/issues/40) [[tag](https://github.com/tag)]
* Add `get_last_statement()` - closes [issue #84](https://github.com/j4mie/idiorm/issues/84) [[tag](https://github.com/tag)]
* Add HAVING clause functionality - closes [issue #50](https://github.com/j4mie/idiorm/issues/50)
* Add `is_new` method - closes [issue #85](https://github.com/j4mie/idiorm/issues/85)
* Add `ArrayAccess` support to the model instances allowing property access via `$model['field']` as well as `$model->field` - [issue #51](https://github.com/j4mie/idiorm/issues/51)
* Add a result set object for collections of models that can support method chains to filter or apply actions to multiple results at once - issue [#51](https://github.com/j4mie/idiorm/issues/51) and [#22](https://github.com/j4mie/idiorm/issues/22)
* Add support for [Firebird](http://www.firebirdsql.org) with `ROWS` and `TO` result set limiting and identifier quoting [[mapner](https://github.com/mapner)] - [issue #98](https://github.com/j4mie/idiorm/issues/98)
* Fix last insert ID for PostgreSQL using RETURNING - closes issues [#62](https://github.com/j4mie/idiorm/issues/62) and [#89](https://github.com/j4mie/idiorm/issues/89) [[laacz](https://github.com/laacz)]
* Reset Idiorm after performing a query to allow for calling `count()` and then `find_many()` [[fayland](https://github.com/fayland)] - [issue #97](https://github.com/j4mie/idiorm/issues/97)
* Change Composer to use a classmap so that autoloading is better supported [[javierd](https://github.com/javiervd)] - [issue #96](https://github.com/j4mie/idiorm/issues/96)
* Add query logging to `delete_many` [[tag](https://github.com/tag)]
* Fix when using `set_expr` alone it doesn't trigger query creation - closes [issue #90](https://github.com/j4mie/idiorm/issues/90)
* Escape quote symbols in "_quote_identifier_part" - close [issue #74](https://github.com/j4mie/idiorm/issues/74)
* Fix issue with aggregate functions always returning `int` when is `float` sometimes required - closes [issue #92](https://github.com/j4mie/idiorm/issues/92)
* Move testing into PHPUnit to unify method testing and query generation testing

#### 1.2.3 - released 2012-11-28

* Fix [issue #78](https://github.com/j4mie/idiorm/issues/78) - remove use of PHP 5.3 static call

#### 1.2.2 - released 2012-11-15

* Fix bug where input parameters were sent as part-indexed, part associative

#### 1.2.1 - released 2012-11-15

* Fix minor bug caused by IdiormStringException not extending Exception

#### 1.2.0 - released 2012-11-14

* Setup composer for installation via packagist (j4mie/idiorm)
* Add `order_by_expr` method [[sandermarechal](http://github.com/sandermarechal)]
* Add support for raw queries without parameters argument [[sandermarechal](http://github.com/sandermarechal)]
* Add support to set multiple properties at once by passing an associative array to `set` method [[sandermarechal](http://github.com/sandermarechal)]
* Allow an associative array to be passed to `configure` method [[jordanlev](http://github.com/jordanlev)]
* Patch to allow empty Paris models to be saved ([[j4mie/paris](http://github.com/j4mie/paris)]) - [issue #58](https://github.com/j4mie/idiorm/issues/58)
* Add `select_many` and `select_many_expr` - closing issues [#49](https://github.com/j4mie/idiorm/issues/49) and [#69](https://github.com/j4mie/idiorm/issues/69)
* Add support for `MIN`, `AVG`, `MAX` and `SUM` - closes [issue #16](https://github.com/j4mie/idiorm/issues/16)
* Add `group_by_expr` - closes [issue #24](https://github.com/j4mie/idiorm/issues/24)
* Add `set_expr` to allow database expressions to be set as ORM properties - closes issues [#59](https://github.com/j4mie/idiorm/issues/59) and [#43](https://github.com/j4mie/idiorm/issues/43) [[brianherbert](https://github.com/brianherbert)]
* Prevent ambiguous column names when joining tables - [issue #66](https://github.com/j4mie/idiorm/issues/66) [[hellogerard](https://github.com/hellogerard)]
* Add `delete_many` method [[CBeerta](https://github.com/CBeerta)]
* Allow unsetting of ORM parameters [[CBeerta](https://github.com/CBeerta)]
* Add `find_array` to get the records as associative arrays [[Surt](https://github.com/Surt)] - closes [issue #17](https://github.com/j4mie/idiorm/issues/17)
* Fix bug in `_log_query` with `?` and `%` supplied in raw where statements etc. - closes [issue #57](https://github.com/j4mie/idiorm/issues/57) [[ridgerunner](https://github.com/ridgerunner)]

#### 1.1.1 - released 2011-01-30

* Fix bug in quoting column wildcard. j4mie/paris#12
* Small documentation improvements

#### 1.1.0 - released 2011-01-24

* Add `is_dirty` method
* Add basic query caching
* Add `distinct` method
* Add `group_by` method

#### 1.0.0 - released 2010-12-01

* Initial release
HTML5 Boilerplate for Wordpress
===============================

This theme is built on the [HTML5 Boilerplate](http://html5boilerplate.com/) by Paul Irish and Divya Manian. The sole purpose of this theme is to save developers the time it takes to apply the HTML5 Boilerplate to WordPress. The "HTML5 Boilerplate" name is used with permission from Paul Irish.

The layout is based on Bruce Lawson's [Designing a Blog with HTML5](http://html5doctor.com/designing-a-blog-with-html5/)

Instead of using only DIVs for content layout, it uses new HTML5 tags, including [header](http://html5doctor.com/the-header-element/), 
[footer](http://www.w3schools.com/html5/tag_footer.asp), 
[nav](http://www.w3schools.com/html5/tag_nav.asp), 
[article](http://www.w3schools.com/html5/tag_article.asp), 
and [section](http://html5doctor.com/the-section-element/).

It's a very bare layout, including only the base styles that come with the boilerplate and required WordPress styles, so layout is up to you. Alternatively, you could apply the methods used here to other themes.

Getting Started
---------------
1. Add the html5-boilerplate-for-wordpress folder to your wp-content/themes folder.
2. Activate the theme. WP-Admin > Appearance > Themes
3. Add some of the "Root Files" to the root directory of your website (explained below).
4. Style away, knowing that you're building on a super solid base with HTML5 awesomeness.

Root Files
----------
These files can be found in the html5-boilerplate folder in the theme (html5-boilerplate-for-wordpress/html5-boilerplate). Some of the files listed here should be (carefully) moved to the root of your site (same level as the wp-content directory). Read on for specific instructions.

### 404 Page
If you use permanlinks (WP-Admin > Settings > Permalinks), then WordPress handles any 404s with the 404.php included in the theme. If you don't use permalinks, then add the 404.html file to the root of your site.

### crossdomain.xml
If you don't know what this is, you probably don't need it.
www.adobe.com/devnet/flashplayer/articles/cross_domain_policy.html

### robots.txt
Tells all search engines that they can read and index all pages. This is handled by WordPress so you shouldn't need to move this to the root.

Root Images
-----------
These aren't included with the HTML5 Boilerplate, but links to them are, so these were created so that you don't return a 404 when the browser requests them. Better to include these or make your own, than not include any. The can be found in the images folder of the theme (html5-boilerplate-for-wordpress/images).

### favicon.ico
The favicon is the icon shown to the left of the URL at the top of your browser window.

### apple-touch-icon.png
On iPhones and iPads you can book mark a web page and have it show up on the home screen as an icon. The apple-touch-icon.png becomes this icon if used. Rounded corners and glossy finish are added by the device.

License
-------

The Unlicense (aka: public domain) http://unlicense.org
###  HTML5 Boilerplate

## CHANGELOG:

v0.9 -August 10th, 2010 - Initial release

## LICENSE:

The Unlicense (aka: public domain) http://unlicense.org

## INSTALLATION:

This is a set of files that a front-end developer can use to get started on a website, with following included:

    1. Cross-browser compatible (IE6, yeah we got that.)
    2. HTML5 ready. Use the new tags with certainty.
    3. Optimal caching and compression rules for grade-A performance
    4. Best practice site configuration defaults
    5. Think there's too much? The HTML5 Boilerplate is delete-key friendly. :)
    6. Mobile browser optimizations
    7. Progressive enhancement graceful degredation ........ yeah yeah we got that
    8. IE specific classes for maximum cross-browser control
    9. Want to write unit tests but lazy? A full, hooked up test suite is waiting for you.
    10. Javascript profiling.. in IE6 and IE7? Sure, no problem.
    11. Console.log nerfing so you won't break anyone by mistake.
    12. Never go wrong with your doctype or markup!
    13. An optimal print stylesheet, performance optimized
    14. iOS, Android, Opera Mobile-adaptable markup and CSS skeleton.
    15. IE6 pngfix baked in.
    16. jQuery, waiting for you
    

There will be two releases: a documented release, which is exactly what you see here, and a production release, with most of the descriptive comments stripped out.

