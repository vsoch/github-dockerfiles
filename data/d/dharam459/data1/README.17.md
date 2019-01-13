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
	<br /> Version 4.4.2
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
	<li><a href="http://php.net/">PHP</a> version <strong>5.2.4</strong> or higher.</li>
	<li><a href="http://www.mysql.com/">MySQL</a> version <strong>5.0</strong> or higher.</li>
</ul>

<h3>Recommendations</h3>
<ul>
	<li><a href="http://php.net/">PHP</a> version <strong>5.6</strong> or higher.</li>
	<li><a href="http://www.mysql.com/">MySQL</a> version <strong>5.6</strong> or higher.</li>
	<li>The <a href="http://httpd.apache.org/docs/2.2/mod/mod_rewrite.html">mod_rewrite</a> Apache module.</li>
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
	<li>WordPress has a robust plugin <abbr title="application programming interface">API</abbr> that makes extending the code easy. If you are a developer interested in utilizing this, see the <a href="https://codex.wordpress.org/Plugin_API" title="WordPress plugin API">plugin documentation in the Codex</a>. You shouldn&#8217;t modify any of the core code.</li>
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
* http://www.sno.phy.queensu.ca/~phil/exiftool/TagNames/Nikon.htmlIcons are generated and provided by the http://icomoon.io service.
=== Akismet ===
Contributors: matt, ryan, andy, mdawaffe, tellyworth, josephscott, lessbloat, eoigal, cfinke, automattic, jgs
Tags: akismet, comments, spam, antispam, anti-spam, anti spam, comment moderation, comment spam, contact form spam, spam comments
Requires at least: 3.2
Tested up to: 4.4.1
Stable tag: 3.1.7
License: GPLv2 or later

Akismet checks your comments against the Akismet Web service to see if they look like spam or not.

== Description ==

Akismet checks your comments against the Akismet Web service to see if they look like spam or not and lets you review the spam it catches under your blog's "Comments" admin screen.

Major features in Akismet include:

* Automatically checks all comments and filters out the ones that look like spam.
* Each comment has a status history, so you can easily see which comments were caught or cleared by Akismet and which were spammed or unspammed by a moderator.
* URLs are shown in the comment body to reveal hidden or misleading links.
* Moderators can see the number of approved comments for each user.
* A discard feature that outright blocks the worst spam, saving you disk space and speeding up your site.

PS: You'll need an [Akismet.com API key](http://akismet.com/get/) to use it.  Keys are free for personal blogs; paid subscriptions are available for businesses and commercial sites.

== Installation ==

Upload the Akismet plugin to your blog, Activate it, then enter your [Akismet.com API key](http://akismet.com/get/).

1, 2, 3: You're done!

== Changelog ==

= 3.1.7 =
*Release Date - 4 January 2016*

* Added documentation for the 'akismet_comment_nonce' filter.
* The post-install activation button is now accessible to screen readers and keyboard-only users.
* Fixed a bug that was preventing the "Remove author URL" feature from working in WordPress 4.4

= 3.1.6 =
*Release Date - 14 December 2015*

* Improve the notices shown after activating Akismet.
* Update some strings to allow for the proper plural forms in all languages.

= 3.1.5 =
*Release Date - 13 October 2015*

* Closes a potential XSS vulnerability.

= 3.1.4 =
*Release Date - 24 September 2015*

* Fixed a bug that was preventing some users from automatically connecting using Jetpack if they didn't have a current Akismet subscription.
* Fixed a bug that could cause comments caught as spam to be placed in the Pending queue.
* Error messages and instructions have been simplified to be more understandable.
* Link previews are enabled for all links inside comments, not just the author's website link.

= 3.1.3 =
*Release Date - 6 July 2015*

* Notify users when their account status changes after previously being successfully set up. This should help any users who are seeing blank Akismet settings screens.

= 3.1.2 =
*Release Date - 7 June 2015*

* Reduced the amount of space Akismet uses in the commentmeta table.
* Fixed a bug where some comments with quotes in the author name weren't getting history entries
* Pre-emptive security improvements to ensure that the Akismet plugin can't be used by attackers to compromise a WordPress installation.
* Better UI for the key entry field: allow whitespace to be included at the beginning or end of the key and strip it out automatically when the form is submitted.
* When deactivating the plugin, notify the Akismet API so the site can be marked as inactive.
* Clearer error messages.

= 3.1.1 =
*Release Date - 17th March, 2015*

* Improvements to the "Remove comment author URL" JavaScript
* Include the pingback pre-check from the 2.6 branch.

= 3.1 =
*Release Date - 11th March, 2015*

* Use HTTPS by default for all requests to Akismet.
* Fix for a situation where Akismet might strip HTML from a comment.

= 3.0.4 =
*Release Date - 11th December, 2014*

* Fix to make .htaccess compatible with Apache 2.4.
* Fix to allow removal of https author URLs.
* Fix to avoid stripping part of the author URL when removing and re-adding.
* Removed the "Check for Spam" button from the "Trash" and "Approved" queues, where it would have no effect.
* Allow automatic API key configuration when Jetpack is installed and connected to a WordPress.com account

= 3.0.3 =
*Release Date - 3rd November, 2014*

* Fix for sending the wrong data to delete_comment action that could have prevented old spam comments from being deleted.
* Added a filter to disable logging of Akismet debugging information.
* Added a filter for the maximum comment age when deleting old spam comments.
* Added a filter for the number per batch when deleting old spam comments.
* Removed the "Check for Spam" button from the Spam folder.

= 3.0.2 =
*Release Date - 18th August, 2014*

* Performance improvements.
* Fixed a bug that could truncate the comment data being sent to Akismet for checking.

= 3.0.1 =
*Release Date - 9th July, 2014*

* Removed dependency on PHP's fsockopen function
* Fix spam/ham reports to work when reported outside of the WP dashboard, e.g., from Notifications or the WP app
* Remove jQuery dependency for comment form JavaScript
* Remove unnecessary data from some Akismet comment meta
* Suspended keys will now result in all comments being put in moderation, not spam.

= 3.0.0 =
*Release Date - 15th April, 2014*

* Move Akismet to Settings menu
* Drop Akismet Stats menu
* Add stats snapshot to Akismet settings
* Add Akismet subscription details and status to Akismet settings
* Add contextual help for each page
* Improve Akismet setup to use Jetpack to automate plugin setup
* Fix "Check for Spam" to use AJAX to avoid page timing out
* Fix Akismet settings page to be responsive
* Drop legacy code
* Tidy up CSS and Javascript
* Replace the old discard setting with a new "discard pervasive spam" feature.

= 2.6.0 =
*Release Date - 18th March, 2014*

* Add ajax paging to the check for spam button to handle large volumes of comments
* Optimize javascript and add localization support 
* Fix bug in link to spam comments from right now dashboard widget
* Fix bug with deleting old comments to avoid timeouts dealing with large volumes of comments
* Include X-Pingback-Forwarded-For header in outbound WordPress pingback verifications
* Add pre-check for pingbacks, to stop spam before an outbound verification request is made

= 2.5.9 =
*Release Date - 1st August, 2013*

* Update 'Already have a key' link to redirect page rather than depend on javascript
* Fix some non-translatable strings to be translatable
* Update Activation banner in plugins page to redirect user to Akismet config page

= 2.5.8 =
*Release Date - 20th January, 2013*

* Simplify the activation process for new users
* Remove the reporter_ip parameter
* Minor preventative security improvements

= 2.5.7 =
*Release Date - 13th December, 2012*

* FireFox Stats iframe preview bug
* Fix mshots preview when using https
* Add .htaccess to block direct access to files
* Prevent some PHP notices
* Fix Check For Spam return location when referrer is empty
* Fix Settings links for network admins
* Fix prepare() warnings in WP 3.5

= 2.5.6 =
*Release Date - 26th April, 2012*

* Prevent retry scheduling problems on sites where wp_cron is misbehaving
* Preload mshot previews
* Modernize the widget code
* Fix a bug where comments were not held for moderation during an error condition
* Improve the UX and display when comments are temporarily held due to an error
* Make the Check For Spam button force a retry when comments are held due to an error
* Handle errors caused by an invalid key
* Don't retry comments that are too old
* Improve error messages when verifying an API key

= 2.5.5 =
*Release Date - 11th January, 2012*

* Add nonce check for comment author URL remove action
* Fix the settings link

= 2.5.4 =
*Release Date - 5th January, 2012*

* Limit Akismet CSS and Javascript loading in wp-admin to just the pages that need it
* Added author URL quick removal functionality
* Added mShot preview on Author URL hover
* Added empty index.php to prevent directory listing
* Move wp-admin menu items under Jetpack, if it is installed
* Purge old Akismet comment meta data, default of 15 days

= 2.5.3 = 
*Release Date - 8th Febuary, 2011*

* Specify the license is GPL v2 or later
* Fix a bug that could result in orphaned commentmeta entries
* Include hotfix for WordPress 3.0.5 filter issue

= 2.5.2 =
*Release Date - 14th January, 2011*

* Properly format the comment count for author counts
* Look for super admins on multisite installs when looking up user roles
* Increase the HTTP request timeout
* Removed padding for author approved count
* Fix typo in function name
* Set Akismet stats iframe height to fixed 2500px.  Better to have one tall scroll bar than two side by side.

= 2.5.1 =
*Release Date - 17th December, 2010*

* Fix a bug that caused the "Auto delete" option to fail to discard comments correctly
* Remove the comment nonce form field from the 'Akismet Configuration' page in favor of using a filter, akismet_comment_nonce
* Fixed padding bug in "author" column of posts screen
* Added margin-top to "cleared by ..." badges on dashboard
* Fix possible error when calling akismet_cron_recheck()
* Fix more PHP warnings
* Clean up XHTML warnings for comment nonce
* Fix for possible condition where scheduled comment re-checks could get stuck
* Clean up the comment meta details after deleting a comment
* Only show the status badge if the comment status has been changed by someone/something other than Akismet
* Show a 'History' link in the row-actions
* Translation fixes
* Reduced font-size on author name
* Moved "flagged by..." notification to top right corner of comment container and removed heavy styling
* Hid "flagged by..." notification while on dashboard

= 2.5.0 =
*Release Date - 7th December, 2010*

* Track comment actions under 'Akismet Status' on the edit comment screen
* Fix a few remaining deprecated function calls ( props Mike Glendinning ) 
* Use HTTPS for the stats IFRAME when wp-admin is using HTTPS
* Use the WordPress HTTP class if available
* Move the admin UI code to a separate file, only loaded when needed
* Add cron retry feature, to replace the old connectivity check
* Display Akismet status badge beside each comment
* Record history for each comment, and display it on the edit page
* Record the complete comment as originally submitted in comment_meta, to use when reporting spam and ham
* Highlight links in comment content
* New option, "Show the number of comments you've approved beside each comment author."
* New option, "Use a nonce on the comment form."

= 2.4.0 =
*Release Date - 23rd August, 2010*

* Spell out that the license is GPLv2
* Fix PHP warnings
* Fix WordPress deprecated function calls
* Fire the delete_comment action when deleting comments
* Move code specific for older WP versions to legacy.php
* General code clean up

= 2.3.0 =
*Release Date - 5th June, 2010*

* Fix "Are you sure" nonce message on config screen in WPMU
* Fix XHTML compliance issue in sidebar widget
* Change author link; remove some old references to WordPress.com accounts
* Localize the widget title (core ticket #13879)

= 2.2.9 =
*Release Date - 2nd June, 2010*

* Eliminate a potential conflict with some plugins that may cause spurious reports

= 2.2.8 =
*Release Date - 27th May, 2010*

* Fix bug in initial comment check for ipv6 addresses
* Report comments as ham when they are moved from spam to moderation
* Report comments as ham when clicking undo after spam
* Use transition_comment_status action when available instead of older actions for spam/ham submissions
* Better diagnostic messages when PHP network functions are unavailable
* Better handling of comments by logged-in users

= 2.2.7 =
*Release Date - 17th December, 2009*

* Add a new AKISMET_VERSION constant
* Reduce the possibility of over-counting spam when another spam filter plugin is in use
* Disable the connectivity check when the API key is hard-coded for WPMU

= 2.2.6 =
*Release Date - 20th July, 2009*

* Fix a global warning introduced in 2.2.5
* Add changelog and additional readme.txt tags
* Fix an array conversion warning in some versions of PHP
* Support a new WPCOM_API_KEY constant for easier use with WordPress MU

= 2.2.5 =
*Release Date - 13th July, 2009*

* Include a new Server Connectivity diagnostic check, to detect problems caused by firewalls

= 2.2.4 =
*Release Date - 3rd June, 2009*

* Fixed a key problem affecting the stats feature in WordPress MU
* Provide additional blog information in Akismet API calls
=== Twenty Fifteen ===
Contributors: the WordPress team
Requires at least: WordPress 4.1
Tested up to: WordPress 4.5-trunk
Version: 1.4
License: GPLv2 or later
License URI: http://www.gnu.org/licenses/gpl-2.0.html
Tags: black, blue, gray, pink, purple, white, yellow, dark, light, two-columns, left-sidebar, fixed-layout, responsive-layout, accessibility-ready, custom-background, custom-colors, custom-header, custom-menu, editor-style, featured-images, microformats, post-formats, rtl-language-support, sticky-post, threaded-comments, translation-ready

== Description ==
Our 2015 default theme is clean, blog-focused, and designed for clarity. Twenty Fifteen's simple, straightforward typography is readable on a wide variety of screen sizes, and suitable for multiple languages. We designed it using a mobile-first approach, meaning your content takes center-stage, regardless of whether your visitors arrive by smartphone, tablet, laptop, or desktop computer.

* Mobile-first, Responsive Layout
* Custom Colors
* Custom Header
* Social Links
* Menu Description
* Post Formats
* The GPL v2.0 or later license. :) Use it to make something cool.

For more information about Twenty Fifteen please go to https://codex.wordpress.org/Twenty_Fifteen.

== Installation ==

1. In your admin panel, go to Appearance -> Themes and click the 'Add New' button.
2. Type in Twenty Fifteen in the search form and press the 'Enter' key on your keyboard.
3. Click on the 'Activate' button to use your new theme right away.
4. Go to https://codex.wordpress.org/Twenty_Fifteen for a guide on how to customize this theme.
5. Navigate to Appearance > Customize in your admin panel and customize to taste.

== Copyright ==

Twenty Fifteen WordPress Theme, Copyright 2014-2015 WordPress.org & Automattic.com
Twenty Fifteen is distributed under the terms of the GNU GPL

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

Twenty Fifteen Theme bundles the following third-party resources:

HTML5 Shiv v3.7.0, Copyright 2014 Alexander Farkas
Licenses: MIT/GPL2
Source: https://github.com/aFarkas/html5shiv

Genericons icon font, Copyright 2013-2015 Automattic.com
License: GNU GPL, Version 2 (or later)
Source: http://www.genericons.com

== Changelog ==

= 1.4 =
* Released: December 8, 2015

https://codex.wordpress.org/Twenty_Fifteen_Theme_Changelog#Version_1.4

= 1.3 =
* Released: August 18, 2015

https://codex.wordpress.org/Twenty_Fifteen_Theme_Changelog#Version_1.3

= 1.2 =
* Released: May 6, 2015

https://codex.wordpress.org/Twenty_Fifteen_Theme_Changelog#Version_1.2

= 1.1 =
* Released: April 23, 2015

https://codex.wordpress.org/Twenty_Fifteen_Theme_Changelog#Version_1.1

= 1.0 =
* Released: December 18, 2014

Initial release
=== Twenty Fourteen ===
Contributors: the WordPress team
Requires at least: WordPress 3.6
Tested up to: WordPress 4.5-trunk
Stable tag: 1.6
License: GPLv2 or later
License URI: http://www.gnu.org/licenses/gpl-2.0.html
Tags: black, green, white, light, dark, two-columns, three-columns, left-sidebar, right-sidebar, fixed-layout, responsive-layout, custom-background, custom-header, custom-menu, editor-style, featured-images, flexible-header, full-width-template, microformats, post-formats, rtl-language-support, sticky-post, theme-options, translation-ready, accessibility-ready

== Description ==
In 2014, our default theme lets you create a responsive magazine website with a sleek, modern design. Feature your favorite homepage content in either a grid or a slider. Use the three widget areas to customize your website, and change your content's layout with a full-width page template and a contributor page to show off your authors. Creating a magazine website with WordPress has never been easier.

For more information about Twenty Fourteen please go to https://codex.wordpress.org/Twenty_Fourteen.

== Installation ==

1. In your admin panel, go to Appearance -> Themes and click the 'Add New' button.
2. Type in Twenty Fourteen in the search form and press the 'Enter' key in your keyboard.
3. Click on the 'Activate' button to use your new theme right away.
4. Go to https://codex.wordpress.org/Twenty_Fourteen for a guide to customize this theme.
5. Navigate to Appearance > Customize in your admin panel.

== Copyright ==

Twenty Fourteen WordPress Theme, Copyright 2013-2015 WordPress.org & Automattic.com
Twenty Fourteen is Distributed under the terms of the GNU GPL

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

Twenty Fourteen Theme is derived from the Further Theme, Copyright 2013 Takashi Irie
Further Theme is distributed under the terms of the GNU GPL

Twenty Fourteen Theme bundles the following third-party resources:

HTML5 Shiv v3.7.0, Copyright 2014 Alexander Farkas
Licenses: MIT/GPL2
Source: https://github.com/aFarkas/html5shiv

Genericons icon font, Copyright 2013-2015 Automattic.com
License: GNU GPL, Version 2 (or later)
Source: http://www.genericons.com

== Changelog ==

= 1.6 =
* Released: December 8, 2015

https://codex.wordpress.org/Twenty_Fourteen_Theme_Changelog#Version_1.6

= 1.5 =
* Released: August 18, 2015

https://codex.wordpress.org/Twenty_Fourteen_Theme_Changelog#Version_1.5

= 1.4 =
* Released: April 23, 2015

https://codex.wordpress.org/Twenty_Fourteen_Theme_Changelog#Version_1.4

= 1.3 =
* Released: December 18, 2014

https://codex.wordpress.org/Twenty_Fourteen_Theme_Changelog#Version_1.3

= 1.2 =
* Released: September 4, 2014

https://codex.wordpress.org/Twenty_Fourteen_Theme_Changelog#Version_1.2

= 1.1 =
* Released: May 8, 2014

https://codex.wordpress.org/Twenty_Fourteen_Theme_Changelog#Version_1.1

= 1.0 =
* Released: December 12, 2013

Initial release.
=== Twenty Sixteen ===
Contributors: the WordPress team
Requires at least: WordPress 4.4
Tested up to: WordPress 4.4
Version: 1.1
License: GPLv2 or later
License URI: http://www.gnu.org/licenses/gpl-2.0.html
Tags: black, blue, gray, green, white, yellow, dark, light, one-column, two-columns, right-sidebar, fixed-layout, responsive-layout, accessibility-ready, custom-background, custom-colors, custom-header, custom-menu, editor-style, featured-images, flexible-header, microformats, post-formats, rtl-language-support, sticky-post, threaded-comments, translation-ready

== Description ==
Twenty Sixteen is a modernized take on an ever-popular WordPress layout — the horizontal masthead with an optional right sidebar that works perfectly for blogs and websites. It has custom color options with beautiful default color schemes, a harmonious fluid grid using a mobile-first approach, and impeccable polish in every detail. Twenty Sixteen will make your WordPress look beautiful everywhere.

* Mobile-first, Responsive Layout
* Custom Colors
* Custom Header
* Social Links
* Post Formats
* The GPL v2.0 or later license. :) Use it to make something cool.

For more information about Twenty Sixteen please go to https://codex.wordpress.org/Twenty_Sixteen.

== Installation ==

1. In your admin panel, go to Appearance -> Themes and click the 'Add New' button.
2. Type in Twenty Sixteen in the search form and press the 'Enter' key on your keyboard.
3. Click on the 'Activate' button to use your new theme right away.
4. Go to https://codex.wordpress.org/Twenty_Sixteen for a guide on how to customize this theme.
5. Navigate to Appearance > Customize in your admin panel and customize to taste.

== Copyright ==

Twenty Sixteen WordPress Theme, Copyright 2014-2015 WordPress.org
Twenty Sixteen is distributed under the terms of the GNU GPL

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

Twenty Sixteen Theme bundles the following third-party resources:

HTML5 Shiv v3.7.0, Copyright 2014 Alexander Farkas
Licenses: MIT/GPL2
Source: https://github.com/aFarkas/html5shiv

Genericons icon font, Copyright 2013-2015 Automattic.com
License: GNU GPL, Version 2 (or later)
Source: http://www.genericons.com

Image used in screenshot.png: A photo by Austin Schmid (https://unsplash.com/schmidy/), licensed under Creative Commons Zero(http://creativecommons.org/publicdomain/zero/1.0/)

== Notes ==

Only the default and dark color schemes are accessibility ready.
=== Zues ===

Contributors: dannycooper
Tags: light, white, one-column, two-columns, responsive-layout, featured-images, full-width-template, rtl-language-support, threaded-comments, custom-menu, custom-header, custom-background

Version: 1.0.6
Requires at least: 4.0
Tested up to: 4.4.2
Stable tag: 1.0.5
License: GPLv2 or later
License URI: http://www.gnu.org/licenses/gpl-2.0.html

== Description ==

Zues is a minimal WordPress theme that can be used as a standalone theme, or as a framework to build something even better.

== Installation ==

1. In your admin panel, go to Appearance > Themes and click the Add New button.
2. Click Upload and Choose File, then select the theme's .zip file. Click Install Now.
3. Click Activate to use your new theme right away.

== Frequently Asked Questions ==

= Does this theme support any plugins? =

Zues includes support for Infinite Scroll in Jetpack.

Zues has been tested with the following plugins:

* Contact Form 7

== Changelog ==

= 1.0.6 - March 8, 2016 =
* ADDED: attr.php attribution
* REMOVE: favicon.ico
* REMOVE: add_editor_style()

= 1.0.5 - February 27, 2016 =
* FIX: Repeating pagination on archive pages

= 1.0.4 - February 26, 2016 =
* ADDED: Lightweight responsive Navigation
* ADDED: Credits to readme.txt
* FIX: placement of wp_head()
* FIX: prefix constants in zues-framework/init.php
* REMOVE: empty functions.php
* REMOVE: unused customizer folder
* REMOVE: hard-coded favicon

= 1.0.3 - February 1, 2016 =
* ADDED: Conditional loading of libraries
* REMOVE: Invalid CSS
* REMOVE: Undefined function calls
* FIX: select elements max-width: 100%
* FIX: Inconsistent wp_nav_menu display
* FIX: Call if( have_posts() ) before while( have_posts() )
* FIX: Typo in comments.php </section>
* FIX: Incorrectly echoing search string in search-header.php

= 1.0.1 - January 28, 2016 =
* Fixed 'zies' text domain
* Added initial documentation to hooks/filters
* Fixed screenshot size (1200px x 900px)

= 1.0 - November 1, 2015 =
* Initial release

== Credits ==

Zues WordPress Theme bundles the following third-party resources:

* normalize.css, (C) 2012-2016 Nicolas Gallagher and Jonathan Neal, [MIT](http://opensource.org/licenses/MIT)
 * Source: http://necolas.github.io/normalize.css/

* superfish.js , (C) 2013 jQuery Foundation and other contributors, [MIT](http://opensource.org/licenses/MIT)
 * Source: http://users.tpg.com.au/j_birch/plugins/superfish/

* jquery.tinyNav.js, (C) 2011-2014 Viljami Salminen, [MIT](http://opensource.org/licenses/MIT)
 * Source: http://tinynav.viljamis.com/

* FontAwesome, (C) Dave Gandy, [SIL OFL 1.1, MIT](http://fontawesome.io/license/)
 * Source: http://fontawesome.io/

* Customizer_Library, (C) Devin Price, [GPL-2](http://opensource.org/licenses/gpl-2.0.php)
 * Source: https://github.com/devinsays/customizer-library

* TGM-Plugin-Activation, (C) 2011 Thomas Griffin, [GPL-2](http://opensource.org/licenses/gpl-2.0.php)
 * Source: https://github.com/TGMPA/TGM-Plugin-Activation

 * Hybrid Core - functions-attr.php, (C) 2008-2015 Justin Tadlock, [GPL-2](http://opensource.org/licenses/gpl-2.0.php)
  * Source: https://github.com/justintadlock/hybrid-core/blob/3.0/inc/functions-attr.php
## Genericons

Genericons are vector icons embedded in a webfont designed to be clean and simple keeping with a generic aesthetic.

Use genericons for instant HiDPI, to change icon colors on the fly, or even with CSS effects such as drop-shadows or gradients!


### Usage

To use it, place the `font` folder in your stylesheet directory and enqueue the genericons.css file. Now you can create an icon like this:

```
.my-icon:before {
	content: '\f101';
	font: normal 16px/1 'Genericons';
	display: inline-block;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
}
```

This will output a comment icon before every element with the class "my-icon". The `content: '\f101';` part of this CSS is easily copied from the helper tool at http://genericons.com/, or `example.html` in the `font` directory.

You can also use the bundled example.css if you'd rather insert the icons using HTML tags.


### Notes

**Photoshop mockups**

The `Genericons.ttf` file found in the `font` directory can be placed in your system fonts folder and used Photoshop or other graphics apps if you like.

If you're using Genericons in your Photoshop mockups, please remember to delete the old version of the font from Font Book, and grab the new one from the zip file. This also affects using it in your webdesigns: if you have an old version of the font installed locally, that's the font that'll be used in your website as well, so if you're missing icons, check for old versions of the font on your system.

**Pixel grid**

Genericons has been designed for a 16x16px grid. That means it'll look sharp at font-size: 16px exactly. It'll also be crisp at multiples thereof, such as 32px or 64px. It'll look reasonably crisp at in-between font sizes such as 24px or 48px, but not quite as crisp as 16 or 32. Please don't set the font-size to 17px, though, that'll just look terrible blurry.

**Antialiasing**

If you keep intact the `-webkit-font-smoothing: antialiased;` and `-moz-osx-font-smoothing: grayscale;` CSS properties. That'll make the icons look their best possible, in Firefox and WebKit based browsers.

**optimizeLegibility**

Note: On Android browsers with version 4.2, 4.3, and probably later, Genericons will simply not show up if you're using the CSS property "text-rendering" set to "optimizeLegibility.

**Updates**

We don't often update icons, but do very carefully when we get good feedback suggesting improvements. Please be mindful if you upgrade, and check that the updated icons behave as you intended.


### Changelog

**3.2**

A number of new icons and a couple of quick updates. 

* New: Activity
* New: HTML anchor
* New: Bug
* New: Download
* New: Handset
* New: Microphone
* New: Minus
* New: Plus
* New: Move
* New: Rating stars, empty, half, full
* New: Shuffle
* New: video camera
* New: Spotify
* New: Twitch
* Update: Fixed geometry in Edit icon
* Update: Updated Foursquare icon

Twitch and Spotify mark the last social icons that will be added to Genericons.
Future social icons will have to happen in a separate font. 

**3.1**

Genericons is now generated using a commandline tool called FontCustom. This makes it far easier to add new icons to the font, but the switch means the download zip now has a different layout, fonts have different filenames, there's now no .otf font included (but the .ttf should suffice), and the font now has slightly different metrics. I've taken great care to ensure this new version should work as a drop-in replacement, but please be mindful and test carefully if you choose to upgrade.

* Per feedback, the baked-in 16px width and height has been removed from the helper CSS. It wasn't really necessary (the glyph itself has these dimensions naturally), and it caused some headaches.
* Base64 encoding is now included by default in the helper CSS. This makes it drop-in easy to get Genericons working in Firefox even when using a CDN. 
* Title attribute on website tool.
* New: Website.
* New: Ellipsis.
* New: Foursquare.
* New: X-post.
* New: Sitemap.
* New: Hierarchy.
* New: Paintbrush.
* Updated: Show and Hide icons were updated for clarity.

**3.0.3**

Bunch of updates mostly.

* Two new icons, Dropbox and Fullscreen.
* Updates to all icons containing an exclamation mark.
* Updates to Image and Quote.
* Nicer "Share" icon.
* Bigger default Linkedin icon.

**3.0.2**

A slew of new stuff and updates.

* Social icons: Skype, Digg, Reddit, Stumbleupon, Pocket.
* New generic icons: heart, lock and print.
* New editing icons: code, bold, italic, image
* New interaction icons: subscribe, unsubscribe, subscribed, reply all, reply, flag.
* The hyperlink icon has been updated to be clearer, chunkier.
* The "home" icon has been updated for style, size and clarity.
* The email icon has been updated for style and clarity, and to fit with the new subscribe icons.
* The document icon has been updated for style.
* The "pin" icon has been updated for style and clarity.
* The Twitter icon has been scaled down to fit with the other social icons.

**3.0.1**

Mostly maintenance. 

* Fixed an issue with the example page that showed an old "top" icon instead of the actual NEW "refresh" icon.
* Added inverse Google+ and Path.
* Replaced tabs with spaces in the helper CSS.
* Changed the Genericons.com copy/paste tool to serve span's instead of div's for casual icon insertion. It's being converted to "inline-block" anyway.

**3.0**

Mainly maintenance and a few new icons.

* Fast forward, rewind, PollDaddy, Notice, Info, Help, Portfolio
* Updated the feed icon. It's a bit smaller now for consistency, the previous one was rather big.
* So, the previous version numbering, 2.09, wasn't very PHP version compare friendly. So from now on it'll be 3.0, 3.1 etc. Props Ipstenu.
* Genericons.com now has a mini release blog.
* The CSS has prettier formatting, props Konstantin Obenland.

**2.09**

Updated Facebook icon to new version. Updated Instagram logo to use new one-color version. Updated Google+ icon to use same radius as Instagram and Facebook. Added a bunch of new icons, cog, unapprove, cart, media player buttons, tablet, send to tablet.                                            

**2.06**

Included Base64 encoded version. This is necessary for Genericons to work with CDNs in Firefox. Firefox blocks fonts linked from a different domain. A CDN (typically s.example.com) usually puts the font on a subdomain, and is hence blocked in Firefox.

**2.05**

Added a bunch of new icons, including upload to cloud, download to cloud, many more.

**2.0**

Initial public release
  ___  ____  __ _  ____  ____  __  ___  __   __ _  ____ 
 / __)(  __)(  ( \(  __)(  _ \(  )/ __)/  \ (  ( \/ ___)
( (_ \ ) _) /    / ) _)  )   / )(( (__(  O )/    /\___ \
 \___/(____)\_)__)(____)(__\_)(__)\___)\__/ \_)__)(____/


Genericons are vector icons embedded in a webfont designed to be clean and simple keeping with a generic aesthetic.

Use genericons for instant HiDPI, to change icon colors on the fly, or even with CSS effects such as drop-shadows or gradients!


_  _ ____ ____ ____ ____ 
|  | [__  |__| | __ |___ 
|__| ___] |  | |__] |___ 


To use it, place the font folder in your stylesheet directory and paste this in your CSS file:

/* =Genericons, thanks to FontSquirrel.com for conversion!
-------------------------------------------------------------- */
@font-face {
    font-family: 'Genericons';
    src: url('font/genericons-regular-webfont.eot');
    src: url('font/genericons-regular-webfont.eot?#iefix') format('embedded-opentype'),
         url('font/genericons-regular-webfont.woff') format('woff'),
         url('font/genericons-regular-webfont.ttf') format('truetype'),
         url('font/genericons-regular-webfont.svg#genericonsregular') format('svg');
    font-weight: normal;
    font-style: normal;

}

Note: the above only works if you don't use a CDN. If you do, or don't know what that is, you should use the syntax that's embedded in genericons.css.

From then on, you can create an icon like this:

.my-icon:before {
	content: '\f101';
	display: inline-block;
	-webkit-font-smoothing: antialiased;
	font: normal 16px/1 'Genericons';
	vertical-align: top;
}

This will output a comment icon before every element with the class "my-icon". The "content: '\f101';" part of this CSS is easily copied from the helper tool at http://genericons.com/

You can also use the bundled example.css if you'd rather insert the icons using HTML tags.


_  _ ____ ___ ____ ____ 
|\ | |  |  |  |___ [__  
| \| |__|  |  |___ ___]


Photoshop mockups:

Genericons-Regular.otf found in the root directory of this zip has not been web-font-ified. So you can drop it in your system fonts folder and use the font in Photoshop if you like.

For those of you using Genericons in your Photoshop mockup, remember to delete the old version of the font from Font Book, and grab the new one from the zip file. This also affects using it in your webdesigns: if you have an old version of the font installed locally, that's the font that'll be used in your website as well, so if you're missing icons, check for old versions of the font on your system.

Pixel grid:

Note that Genericons has been designed for a 16x16 pixel grid. That means it'll look sharp at font-size: 16px exactly. It'll also be crisp at multiples thereof, such as 32px or 64px. It'll also look reasonably crisp at in-between font sizes such as 24px or 48px, but not quite as crisp as 16 or 32. Please don't set the font-size to 17px, though, that'll just look terrible.

Also note the CSS property "-webkit-font-smoothing: antialiased". That makes the icons look great in WebKit browsers. Please see http://noscope.com/2012/font-smoothing for more info.

Updates:

We don't often update icons, but do very carefully when we get good feedback suggesting improvements. Please be mindful if you upgrade, and check that the updated icons behave as you intended.



____ _  _ ____ _  _ ____ ____ _    ____ ____ 
|    |__| |__| |\ | | __ |___ |    |  | | __ 
|___ |  | |  | | \| |__] |___ |___ |__| |__] 

V3.0.3:
Bunch of updates mostly.
- Two new icons, Dropbox and Fullscreen.
- Updates to all icons containing an exclamation mark.
- Updates to Image and Quote.
- Nicer "Share" icon.
- Bigger default Linkedin icon.

V3.0.2: 
A slew of new stuff and updates.
- Social icons: Skype, Digg, Reddit, Stumbleupon, Pocket.
- New generic icons: heart, lock and print.
- New editing icons: code, bold, italic, image
- New interaction icons: subscribe, unsubscribe, subscribed, reply all, reply, flag.
- The hyperlink icon has been updated to be clearer, chunkier.
- The "home" icon has been updated for style, size and clarity.
- The email icon has been updated for style and clarity, and to fit with the new subscribe icons.
- The document icon has been updated for style.
- The "pin" icon has been updated for style and clarity.
- The Twitter icon has been scaled down to fit with the other social icons.

V3.0.1: 
Mostly maintenance. 
- Fixed an issue with the example page that showed an old "top" icon instead of the actual NEW "refresh" icon.
- Added inverse Google+ and Path.
- Replaced tabs with spaces in the helper CSS.
- Changed the Genericons.com copy/paste tool to serve span's instead of div's for casual icon insertion. It's being converted to "inline-block" anyway.

V3.0:
Mainly maintenance and a few new icons.
- Fast forward, rewind, PollDaddy, Notice, Info, Help, Portfolio
- Updated the feed icon. It's a bit smaller now for consistency, the previous one was rather big.
- So, the previous version numbering, 2.09, wasn't very PHP version compare friendly. So from now on it'll be 3.0, 3.1 etc. Props Ipstenu.
- Genericons.com now has a mini release blog.
- The CSS has prettier formatting, props Konstantin Obenland.

V2.09:
Updated Facebook icon to new version. Updated Instagram logo to use new one-color version. Updated Google+ icon to use same radius as Instagram and Facebook. Added a bunch of new icons, cog, unapprove, cart, media player buttons, tablet, send to tablet.                                            

V2.06:
Included Base64 encoded version. This is necessary for Genericons to work with CDNs in Firefox. Firefox blocks fonts linked from a different domain. A CDN (typically s.example.com) usually puts the font on a subdomain, and is hence blocked in Firefox.

V2.05:
Added a bunch of new icons, including upload to cloud, download to cloud, many more.

V2:
Initial public release# Genericons

Genericons are vector icons embedded in a webfont designed to be clean and simple keeping with a generic aesthetic.

Use genericons for instant HiDPI, to change icon colors on the fly, or even with CSS effects such as drop-shadows or gradients!


## Usage

To use it, place the `genericons` folder in your stylesheet directory and enqueue the genericons.css file. Now you can create an icon like this:

```
.my-icon:before {
	content: '\f101';
	font: normal 16px/1 'Genericons';
	display: inline-block;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
}
```

This will output a comment icon before every element with the class "my-icon". The `content: '\f101';` part of this CSS is easily copied from the helper tool at http://genericons.com/, or `example.html` in the `font` directory.

You can also use the bundled example.css if you'd rather insert the icons using HTML tags.


## Building your own Genericons

In the `source` directory, you'll find all Genericons source icons in SVG format. This will allow you to bake your own flavor of Genericons using a tool such as FontCustom (http://fontcustom.com) or Fontello (http://fontello.com). Perhaps you need more logos than are available in the base Genericons package? Just add those logos and bake your own expanded set. Maybe you need just a few of the icons Genericons provides, but would like to trim the fat? Remove the ones you won't need!


### FontCustom instructions

FontCustom is a powerful commandline tool which which bakes icon fonts from the SVG source files. It's the tool Genericons is built on, and it provides highly accurate and perfectly crisp icons, *provided all SVGs have the same pixel height*.

It's not that hard to use, and once it's installed you'll never think of icon-fonts the same way again. Seriously, you should try it. Icon fonts for everyone!

1. Install FontCustom. Follow the instructions on the website: http://fontcustom.com/
2. In the `source` directory from the Genericons download, open the file called `fontcustom.yml` in a text editor. Customize the `font_name` and `css_selector`.
3. Open a terminal. Browse to the `source` directory. Type `fontcustom compile`.

You'll now receive a brand new subdirectory called `fontcustom-webfont`. Inside here you'll find your very own flavor of Genericons, with only the icons you want, including a handy example page that'll help you copy/paste the necessary glyphs or CSS values. 

*Please note*: In the source directory, there's a hidden file called `.fontcustom-manifest.json`. This file is auto-generated by the FontCustom tool, and holds codepoints (unicode addresses) for every glyph, so its address doesn't change when you add or remove icons. If you feel the need to "start fresh" with the unicode addresses, you should delete this file. 


### Fontello instructions

Fontello is very easy to use. Just drop the SVG files of the icons you want onto their website and download the font. The downside is that Fontello seems to ignore the 16px pixelgrid, so you'll end up with fuzzy icons. Buyer beware.


## Notes

**Photoshop mockups**

The `Genericons.ttf` file can be placed in your system fonts folder and used Photoshop or other graphics apps if you like.

If you're using Genericons in your Photoshop mockups, please remember to delete the old version of the font from Font Book, and grab the new one from the zip file. This also affects using it in your webdesigns: if you have an old version of the font installed locally, that's the font that'll be used in your website as well, so if you're missing icons, check for old versions of the font on your system.

**Pixel grid**

Genericons has been designed for a 16x16px grid. That means it'll look sharp at font-size: 16px exactly. It'll also be crisp at multiples thereof, such as 32px or 64px. It'll look reasonably crisp at in-between font sizes such as 24px or 48px, but not quite as crisp as 16 or 32. Please don't set the font-size to 17px, though, that'll just look terrible blurry.

**Antialiasing**

If you keep intact the `-webkit-font-smoothing: antialiased;` and `-moz-osx-font-smoothing: grayscale;` CSS properties. That'll make the icons look their best possible, in Firefox and WebKit based browsers.

**optimizeLegibility**

Note: On Android browsers with version 4.2, 4.3, and probably later, Genericons will simply not show up if you're using the CSS property "text-rendering" set to "optimizeLegibility.

**Updates**

We don't often update icons, but do very carefully when we get good feedback suggesting improvements. Please be mindful if you upgrade, and check that the updated icons behave as you intended.

**Base64 encoding**

By default, Genericons ships with a stylesheet that includes a base64 encoded version of the font. This is to sidestep issues with cross-origin requests for fonts, that happen when a stylesheet loads a font that's stored on a different domain or subdomain. This is very common when using caching plugins.

Base64 encoding comes with a 25% filesize overhead compared to just loading the WOFF file directly. If you know that you won't be loading fonts across domains, or have the ability to edit your server config files to allow it, you can get slightly faster performance by loading Genericons without the base64 encoding. Simply edit `genericons.css` and edit the `@font-face` declaration to match this:

```
@font-face {
	font-family: 'Genericons';
		src: url('Genericons.woff') format('woff'),
		url('Genericons.ttf') format('truetype'),
		url('Genericons.svg#genericonsregular') format('svg');
	font-weight: normal;
	font-style: normal;
}
```



## Changelog

**3.4.1**

* IE8 support restored.

**3.4**

* Updated: Update Google Plus icon to new geometric version. This also *retires* the "alt" version, so *please be mindful if you choose to update, make sure you use the `f206` glyph, not the `f218` glyph, as it no longer exists!
* New: Added helper rotation classes to the base CSS, thanks to geminorum. Apply `genericon-rotate-90` to rotate 90 degrees, -180, -270. Or `genericon-flip-horizontal` or -vertical. 

*Again, it is important if you choose to update to this version, make sure you're not using `genericon-googleplus-alt` or unicode character `f218`, as that has been retired! Use `genericon-googleplus` and glyph `f206` instead!*

**3.3.1**

Security Hardening: Remove Genericons example.html file. Please visit genericons.com instead.

**3.3**

The Open Source release.

You can now build your own flavors of Genericons with all the SVGs provided. 


**3.2**

A number of new icons and a couple of quick updates. 

* New: Activity
* New: HTML anchor
* New: Bug
* New: Download
* New: Handset
* New: Microphone
* New: Minus
* New: Plus
* New: Move
* New: Rating stars, empty, half, full
* New: Shuffle
* New: video camera
* New: Spotify
* New: Twitch
* Update: Fixed geometry in Edit icon
* Update: Updated Foursquare icon
* IE8 bugfix, slipstreamed into this. 

Twitch and Spotify mark the last social icons that will be added to Genericons.
Future social icons will have to happen in a separate font. 

**3.1**

Genericons is now generated using a commandline tool called FontCustom. This makes it far easier to add new icons to the font, but the switch means the download zip now has a different layout, fonts have different filenames, there's now no .otf font included (but the .ttf should suffice), and the font now has slightly different metrics. I've taken great care to ensure this new version should work as a drop-in replacement, but please be mindful and test carefully if you choose to upgrade.

* Per feedback, the baked-in 16px width and height has been removed from the helper CSS. It wasn't really necessary (the glyph itself has these dimensions naturally), and it caused some headaches.
* Base64 encoding is now included by default in the helper CSS. This makes it drop-in easy to get Genericons working in Firefox even when using a CDN. 
* Title attribute on website tool.
* New: Website.
* New: Ellipsis.
* New: Foursquare.
* New: X-post.
* New: Sitemap.
* New: Hierarchy.
* New: Paintbrush.
* Updated: Show and Hide icons were updated for clarity.

**3.0.3**

Bunch of updates mostly.

* Two new icons, Dropbox and Fullscreen.
* Updates to all icons containing an exclamation mark.
* Updates to Image and Quote.
* Nicer "Share" icon.
* Bigger default Linkedin icon.

**3.0.2**

A slew of new stuff and updates.

* Social icons: Skype, Digg, Reddit, Stumbleupon, Pocket.
* New generic icons: heart, lock and print.
* New editing icons: code, bold, italic, image
* New interaction icons: subscribe, unsubscribe, subscribed, reply all, reply, flag.
* The hyperlink icon has been updated to be clearer, chunkier.
* The "home" icon has been updated for style, size and clarity.
* The email icon has been updated for style and clarity, and to fit with the new subscribe icons.
* The document icon has been updated for style.
* The "pin" icon has been updated for style and clarity.
* The Twitter icon has been scaled down to fit with the other social icons.

**3.0.1**

Mostly maintenance. 

* Fixed an issue with the example page that showed an old "top" icon instead of the actual NEW "refresh" icon.
* Added inverse Google+ and Path.
* Replaced tabs with spaces in the helper CSS.
* Changed the Genericons.com copy/paste tool to serve span's instead of div's for casual icon insertion. It's being converted to "inline-block" anyway.

**3.0**

Mainly maintenance and a few new icons.

* Fast forward, rewind, PollDaddy, Notice, Info, Help, Portfolio
* Updated the feed icon. It's a bit smaller now for consistency, the previous one was rather big.
* So, the previous version numbering, 2.09, wasn't very PHP version compare friendly. So from now on it'll be 3.0, 3.1 etc. Props Ipstenu.
* Genericons.com now has a mini release blog.
* The CSS has prettier formatting, props Konstantin Obenland.

**2.09**

Updated Facebook icon to new version. Updated Instagram logo to use new one-color version. Updated Google+ icon to use same radius as Instagram and Facebook. Added a bunch of new icons, cog, unapprove, cart, media player buttons, tablet, send to tablet.                                            

**2.06**

Included Base64 encoded version. This is necessary for Genericons to work with CDNs in Firefox. Firefox blocks fonts linked from a different domain. A CDN (typically s.example.com) usually puts the font on a subdomain, and is hence blocked in Firefox.

**2.05**

Added a bunch of new icons, including upload to cloud, download to cloud, many more.

**2.0**

Initial public release
# Customizer Library

A helpful library for working with the WordPress customizer.

## About

The customizer allows WordPress developers to add options for themes and plugins, but it should be easier to work with.  This library abstracts out some of the complexity.

Instead of adding options to the $wp_customize object directly, developers can just define an array of controls and sections and pass it to the Customizer_Library class.

To see how this works in practice, please see the [Customizer Library Demo](https://github.com/devinsays/customizer-library-demo) theme.

The Customizer Library adds sections, settings and controls to the customizer based on the array that gets passed to it.  There is default sanitization for all options (though you're still welcome to pass a sanitize_callback).  All options are also saved by default as theme_mods (though look for a future update to make this more flexible).

At the moment there is only one custom control (for textarea), but look for additional controls as the library matures.

The Customizer Library includes additional classes and helper functions for creating inline styles and loading Google fonts.  These functions and classes were developed by [The Theme Foundry](https://thethemefoundry.com/) for their theme [Make](https://thethemefoundry.com/wordpress-themes/make/) and I've found them quite useful in my own projects.  However, I'm considering moving them into seperate modules in order to make the core library as focused as possible.  Feedback on this is welcome.

## Installation

The [Customizer Library](https://github.com/devinsays/customizer-library) can be included in your own projects git submodule if you'd like to be able to pull down changes.  To include it in your own projects the same way, navigate to the directory and use:

`git submodule add git@github.com:devinsays/customizer-library customizer-library`

## Options

The Customizer Library currently supports these options:

* Checkbox
* Select
* Radio
* Upload
* Image
* Color
* Text
* URL
* Range
* Textarea
* Select (Typography)

### Sections

Sections are convenient ways to group controls in the customizer.

Customizer Sections can be defined like this:

~~~php
// Example Section

$sections[] = array(
	'id' => 'example', // Required
	'title' => __( 'Example Section', 'zues' ), // Required
	'priority' => '30', // Optional
	'description' => 'Example description', // Optional
	'panel' => 'panel_id' // optional, and it requires WP >= 4.0
);
~~~

### Panels

Panels are a convenient way to group your different sections.

Here's an example that adds a panel, a section to the panel, and then a text option to that section:

~~~php
// Panel Example
$panel = 'panel';

$panels[] = array(
	'id' => $panel,
	'title' => __( 'Panel Examples', 'zues' ),
	'priority' => '100'
);

$section = 'panel-section';

$sections[] = array(
	'id' => $section,
	'title' => __( 'Panel Section', 'zues' ),
	'priority' => '10',
	'panel' => $panel
);

$options['example-panel-text'] = array(
	'id' => 'example-panel-text',
	'label'   => __( 'Example Text Input', 'zues' ),
	'section' => $section,
	'type'    => 'text',
);
~~~

The Customizer_Library uses the core function `$wp_customize->add_panel( $id, $args );` to add panels, and all the same $args are available. See [codex](https://developer.wordpress.org/reference/classes/wp_customize_manager/add_panel/).

### Text

~~~php
$options['example-text'] = array(
	'id' => 'example-text',
	'label'   => __( 'Example Text Input', 'zues' ),
	'section' => $section,
	'type'    => 'text',
);
~~~

### URL

~~~php
$options['example-url'] = array(
	'id' => 'example-url',
	'label'   => __( 'Example URL Input', 'zues' ),
	'section' => $section,
	'type'    => 'url',
);
~~~

### Checkbox

~~~php
$options['example-checkbox'] = array(
	'id' => 'example-checkbox',
	'label'   => __( 'Example Checkbox', 'zues' ),
	'section' => $section,
	'type'    => 'checkbox',
	'default' => 0,
);
~~~

### Select

~~~php
$choices = array(
	'choice-1' => 'Choice One',
	'choice-2' => 'Choice Two',
	'choice-3' => 'Choice Three'
);

$options['example-select'] = array(
	'id' => 'example-select',
	'label'   => __( 'Example Select', 'zues' ),
	'section' => $section,
	'type'    => 'select',
	'choices' => $choices,
	'default' => 'choice-1'
);
~~~

### Drop Down Pages

$options['example-dropdown-pages'] = array(
	'id' => 'example-dropdown-pages',
	'label'   => __( 'Example Drop Down Pages', 'zues' ),
	'section' => $section,
	'type'    => 'dropdown-pages',
	'default' => ''
);
~~~

### Radio

~~~php
$choices = array(
	'choice-1' => 'Choice One',
	'choice-2' => 'Choice Two',
	'choice-3' => 'Choice Three'
);

$options['example-radio'] = array(
	'id' => 'example-radio',
	'label'   => __( 'Example Radio', 'zues' ),
	'section' => $section,
	'type'    => 'radio',
	'choices' => $choices,
	'default' => 'choice-1'
);
~~~

### Upload

~~~php
$options['example-upload'] = array(
	'id' => 'example-upload',
	'label'   => __( 'Example Upload', 'zues' ),
	'section' => $section,
	'type'    => 'upload',
	'default' => '',
);
~~~

### Color

~~~php
$options['example-color'] = array(
	'id' => 'example-color',
	'label'   => __( 'Example Color', 'zues' ),
	'section' => $section,
	'type'    => 'color',
	'default' => $color // hex
);
~~~


### Textarea

~~~php
$options['example-textarea'] = array(
	'id' => 'example-textarea',
	'label'   => __( 'Example Textarea', 'zues' ),
	'section' => $section,
	'type'    => 'textarea',
	'default' => __( 'Example textarea text.', 'zues'),
);
~~~

### Select (Typography)

~~~php
$options['example-font'] = array(
	'id' => 'example-font',
	'label'   => __( 'Example Font', 'zues' ),
	'section' => $section,
	'type'    => 'select',
	'choices' => customizer_library_get_font_choices(),
	'default' => 'Monoton'
);
~~~

### Range

~~~php
$options['example-range'] = array(
	'id' => 'example-range',
	'label'   => __( 'Example Range Input', 'zues' ),
	'section' => $section,
	'type'    => 'range',
	'input_attrs' => array(
        'min'   => 0,
        'max'   => 10,
        'step'  => 1,
        'style' => 'color: #0a0',
	)
);
~~~

### Content

~~~php
$options['example-content'] = array(
	'id' => 'example-content',
	'label' => __( 'Example Content', 'zues' ),
	'section' => $section,
	'type' => 'content',
	'content' => '<p>' . __( 'Content to output. Use <a href="#">HTML</a> if you like.', 'zues' ) . '</p>',
	'description' => __( 'Optional: Example Description.', 'zues' )
);
~~~

### Pass $options to Customizer Library

After all the options and sections are defined, load them with the Customizer Library:

~~~php
// Adds the sections to the $options array
$options['sections'] = $sections;

$customizer_library = Customizer_Library::Instance();
$customizer_library->add_options( $options );
~~~

### Demo

A full working example can be found here:
https://github.com/devinsays/customizer-library-demo/blob/master/inc/customizer-options.php

## Styles

The Customizer Library has a helper class to output inline styles.  This code was originally developed by [The Theme Foundry](https://thethemefoundry.com/) for use in [Make](https://thethemefoundry.com/wordpress-themes/make/).  To see how it works, see "inc/styles.php".

CSS selector(s) and value are passed to Customizer_Library_Styles class like this:

~~~php
Customizer_Library_Styles()->add( array(
	'selectors' => array(
		'.primary'
	),
	'declarations' => array(
		'color' => $color
	)
) );
~~~

#### Media Queries

Media queries can also be be used with Customizer_Library_Styles.  Here's an example for outputting logo-image-2x on high resolution devices.

~~~php
$setting = 'logo-image-2x';
$mod = get_theme_mod( $setting, false );

if ( $mod ) {

	Customizer_Library_Styles()->add( array(
		'selectors' => array(
			'.logo'
		),
		'declarations' => array(
			'background-image' => 'url(' . $mod . ')'
		),
		'media' => '(-webkit-min-device-pixel-ratio: 1.3),(-o-min-device-pixel-ratio: 2.6/2),(min--moz-device-pixel-ratio: 1.3),(min-device-pixel-ratio: 1.3),(min-resolution: 1.3dppx)'
	) );

}
~~~



## Fonts

The Customizer Library has a helper functions to output font stacks and load inline fonts.  This code was also developed by [The Theme Foundry](https://thethemefoundry.com/) for use in [Make](https://thethemefoundry.com/wordpress-themes/make/).  You can see an example of font enqueing in "inc/mods.php":

~~~php
function demo_fonts() {

	// Font options
	$fonts = array(
		get_theme_mod( 'primary-font', customizer_library_get_default( 'primary-font' ) ),
		get_theme_mod( 'secondary-font', customizer_library_get_default( 'secondary-font' ) )
	);

	$font_uri = customizer_library_get_google_font_uri( $fonts );

	// Load Google Fonts
	wp_enqueue_style( 'demo_fonts', $font_uri, array(), null, 'screen' );

}
add_action( 'wp_enqueue_scripts', 'demo_fonts' );
~~~

Fonts can be used in inline styles like this:

~~~php
// Primary Font
$setting = 'primary-font';
$mod = get_theme_mod( $setting, customizer_library_get_default( $setting ) );
$stack = customizer_library_get_font_stack( $mod );

if ( $mod != customizer_library_get_default( $setting ) ) {

	Customizer_Library_Styles()->add( array(
		'selectors' => array(
			'.primary'
		),
		'declarations' => array(
			'font-family' => $stack
		)
	) );

}
~~~

## Change Log

Development
===

* Enhancement: Content option (for help text, HTML output, etc.)

1.3.0
===

* Enhancement: Add text input option
* Enhancement: Sort system fonts and webfonts within dropdown
* Enhancement: Add Panels Support, from WP 4.0
* Enhancement: Add support for "url" type
* Enhancement: Add support for "range" type
* Enhancement: Add support for "dropdown-pages" type
* Update: Change how setting parameters are added

1.2.0
===

* Enhancement: Allow setting parameters
* Update: Refactor interface loop

1.1.0
===

* Bugfix: customizer.js enqueue relative to library
* Enhancement: Use new textarea control from core

1.0.0
===

* Public Release