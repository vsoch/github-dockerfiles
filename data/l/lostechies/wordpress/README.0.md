<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title>WordPress &#8250; ReadMe</title>
	<link rel="stylesheet" href="wp-admin/css/install.css?ver=20100228" type="text/css" />
</head>
<body>
<h1 id="logo">
	<a href="http://wordpress.org/"><img alt="WordPress" src="wp-admin/images/wordpress-logo.png" /></a>
	<br /> Version 3.4.2
</h1>
<p style="text-align: center">Semantic Personal Publishing Platform</p>

<h1>First Things First</h1>
<p>Welcome. WordPress is a very special project to me. Every developer and contributor adds something unique to the mix, and together we create something beautiful that I'm proud to be a part of. Thousands of hours have gone into WordPress, and we're dedicated to making it better every day. Thank you for making it part of your world.</p>
<p style="text-align: right">&#8212; Matt Mullenweg</p>

<h1>Installation: Famous 5-minute install</h1>
<ol>
	<li>Unzip the package in an empty directory and upload everything.</li>
	<li>Open <span class="file"><a href="wp-admin/install.php">wp-admin/install.php</a></span> in your browser. It will take you through the process to set up a <code>wp-config.php</code> file with your database connection details.
		<ol>
			<li>If for some reason this doesn't work, don't worry. It doesn't work on all web hosts. Open up <code>wp-config-sample.php</code> with a text editor like WordPad or similar and fill in your database connection details.</li>
			<li>Save the file as <code>wp-config.php</code> and upload it.</li>
			<li>Open <span class="file"><a href="wp-admin/install.php">wp-admin/install.php</a></span> in your browser.</li>
		</ol>
	</li>
	<li>Once the configuration file is set up, the installer will set up the tables needed for your blog. If there is an error, double check your <code>wp-config.php</code> file, and try again. If it fails again, please go to the <a href="http://wordpress.org/support/" title="WordPress support">support forums</a> with as much data as you can gather.</li>
	<li><strong>If you did not enter a password, note the password given to you.</strong> If you did not provide a username, it will be <code>admin</code>.</li>
	<li>The installer should then send you to the <a href="wp-login.php">login page</a>. Sign in with the username and password you chose during the installation. If a password was generated for you, you can then click on 'Profile' to change the password.</li>
</ol>

<h1>Updating</h1>
<h2>Using the Automatic Updater</h2>
<p>If you are updating from version 2.7 or higher, you can use the automatic updater:</p>
<ol>
	<li>Open the <span class="file"><a href="wp-admin/update-core.php">wp-admin/update-core.php</a></span> in your browser and follow the instructions.</li>
	<li>You wanted more, perhaps? That's it!</li>
</ol>

<h2>Updating Manually</h2>
<ol>
	<li>Before you update anything, make sure you have backup copies of any files you may have modified such as <code>index.php</code>.</li>
	<li>Delete your old WordPress files, saving ones you've modified.</li>
	<li>Upload the new files.</li>
	<li>Point your browser to <span class="file"><a href="wp-admin/upgrade.php">/wp-admin/upgrade.php</a>.</span></li>
</ol>

<h2>Theme Template Changes</h2>
<p>If you have customized your theme templates, you may have to make some changes across major versions.</p>

<h1>Migrating from other systems</h1>
<p>WordPress can <a href="http://codex.wordpress.org/Importing_Content">import from a number of systems</a>. First you need to get WordPress installed and working as described above, before using <a href="wp-admin/import.php" title="Import to WordPress">our import tools</a>.</p>

<h1>System Requirements</h1>
<ul>
	<li><a href="http://php.net/">PHP</a> version <strong>5.2.4</strong> or higher.</li>
	<li><a href="http://www.mysql.com/">MySQL</a> version <strong>5.0</strong> or higher.</li>
</ul>

<h2>System Recommendations</h2>
<ul>
	<li>The <a href="http://httpd.apache.org/docs/2.2/mod/mod_rewrite.html">mod_rewrite</a> Apache module.</li>
	<li>A link to <a href="http://wordpress.org/">http://wordpress.org</a> on your site.</li>
</ul>

<h1>Online Resources</h1>
<p>If you have any questions that aren't addressed in this document, please take advantage of WordPress' numerous online resources:</p>
<dl>
	<dt><a href="http://codex.wordpress.org/">The WordPress Codex</a></dt>
		<dd>The Codex is the encyclopedia of all things WordPress. It is the most comprehensive source of information for WordPress available.</dd>
	<dt><a href="http://wordpress.org/news/">The WordPress Blog</a></dt>
		<dd>This is where you'll find the latest updates and news related to WordPress. Recent WordPress news appears in your administrative dashboard by default.</dd>
	<dt><a href="http://planet.wordpress.org/">WordPress Planet</a></dt>
		<dd>The WordPress Planet is a news aggregator that brings together posts from WordPress blogs around the web.</dd>
	<dt><a href="http://wordpress.org/support/">WordPress Support Forums</a></dt>
		<dd>If you've looked everywhere and still can't find an answer, the support forums are very active and have a large community ready to help. To help them help you be sure to use a descriptive thread title and describe your question in as much detail as possible.</dd>
	<dt><a href="http://codex.wordpress.org/IRC">WordPress <abbr title="Internet Relay Chat">IRC</abbr> Channel</a></dt>
		<dd>There is an online chat channel that is used for discussion among people who use WordPress and occasionally support topics. The above wiki page should point you in the right direction. (<a href="irc://irc.freenode.net/wordpress">irc.freenode.net #wordpress</a>)</dd>
</dl>

<h1><abbr title="eXtensible Markup Language">XML</abbr>-<abbr title="Remote Procedure Call">RPC</abbr> and Atom Interface</h1>
<p>You can post to your WordPress blog with tools like <a href="http://download.live.com/writer">Windows Live Writer</a>, <a href="http://illuminex.com/ecto/">Ecto</a>, <a href="http://bloggar.com/">w.bloggar</a>, <a href="http://radio.userland.com/">Radio Userland</a> (which means you can use Radio's email-to-blog feature), <a href="http://www.newzcrawler.com/">NewzCrawler</a>, and other tools that support the blogging <abbr title="application programming interface">API</abbr>s! :) You can read more about <a href="http://codex.wordpress.org/XML-RPC_Support"><abbr>XML</abbr>-<abbr>RPC</abbr> support on the Codex</a>.</p>

<h1>Post via Email</h1>
<p>You can post from an email client! To set this up go to your &quot;Writing&quot; options screen and fill in the connection details for your secret <abbr title="Post Office Protocol version 3">POP3</abbr> account. Then you need to set up <code>wp-mail.php</code> to execute periodically to check the mailbox for new posts. You can do it with <a href="http://en.wikipedia.org/wiki/Cron">cron</a>-jobs, or if your host doesn't support it you can look into the various website-monitoring services, and make them check your <code>wp-mail.php</code> <abbr title="Uniform Resource Locator">URL</abbr>.</p>
<p>Posting is easy: Any email sent to the address you specify will be posted, with the subject as the title. It is best to keep the address discrete. The script will <em>delete</em> emails that are successfully posted.</p>

<h1>User Roles</h1>
<p>We introduced a very flexible roles system in version 2.0. You can <a href="http://codex.wordpress.org/Roles_and_Capabilities" title="WordPress roles and capabilities">read more about Roles and Capabilities on the Codex</a>.</p>

<h1>Final Notes</h1>
<ul>
	<li>If you have any suggestions, ideas, or comments, or if you (gasp!) found a bug, join us in the <a href="http://wordpress.org/support/">Support Forums</a>.</li>
	<li>WordPress has a robust plugin <abbr title="application programming interface">API</abbr> that makes extending the code easy. If you are a developer interested in utilizing this, see the <a href="http://codex.wordpress.org/Plugin_API" title="WordPress plugin API">plugin documentation in the Codex</a>. You shouldn't modify any of the core code.</li>
</ul>

<h1>Share the Love</h1>
<p>WordPress has no multi-million dollar marketing campaign or celebrity sponsors, but we do have something even better&#8212;you. If you enjoy WordPress please consider telling a friend, setting it up for someone less knowledgable than yourself, or writing the author of a media article that overlooks us.</p>

<p>WordPress is the official continuation of <a href="http://cafelog.com/">b2/caf&#233;log</a>, which came from Michel V. The work has been continued by the <a href="http://wordpress.org/about/">WordPress developers</a>. If you would like to support WordPress, please consider <a href="http://wordpress.org/donate/" title="Donate to WordPress">donating</a>.</p>

<h1>License</h1>
<p>WordPress is free software, and is released under the terms of the <abbr title="GNU General Public License">GPL</abbr> version 2 or (at your option) any later version. See <a href="license.txt">license.txt</a>.</p>

</body>
</html>
=== Disqus Comment System ===
Contributors: disqus, alexkingorg, crowdfavorite, zeeg, tail, thetylerhayes, ryanv12
Tags: comments, threaded, email, notification, spam, avatars, community, profile, widget, disqus
Requires at least: 3.2
Tested up to: 4.5
Stable tag: 2.85

The Disqus comment system replaces your WordPress comment system with your comments hosted and powered by Disqus.

== Description ==

Disqus, pronounced "discuss", is a service and tool for web comments and
discussions. Disqus makes commenting easier and more interactive,
while connecting websites and commenters across a thriving discussion
community.

The Disqus for WordPress plugin seamlessly integrates using the Disqus API and by syncing with WordPress comments.

= Disqus for WordPress =

* Uses the Disqus API
* Comments indexable by search engines (SEO-friendly)
* Support for importing existing comments
* Auto-sync (backup) of comments with Disqus and WordPress database

= Disqus Features =

* Threaded comments and replies
* Notifications and reply by email
* Subscribe and RSS options
* Aggregated comments and social mentions
* Powerful moderation and admin tools
* Full spam filtering, blacklists and whitelists
* Support for Disqus community widgets
* Connected with a large discussion community
* Increased exposure and readership

== Installation ==

**NOTE: It is recommended that you [backup your database](http://codex.wordpress.org/Backing_Up_Your_Database) before installing the plugin.**

1. Unpack archive to this archive to the 'wp-content/plugins/' directory inside
   of WordPress

  * Maintain the directory structure of the archive (all extracted files
    should exist in 'wp-content/plugins/disqus-comment-system/'

2. From your blog administration, click on Comments to change settings
   (WordPress 2.0 users can find the settings under Options > Disqus.)

= More documentation =

Go to [https://disqus.com/help/wordpress](https://disqus.com/help/wordpress)

== Screenshots ==

1. Disqus Comments
2. Discovery Box (part of Disqus Comments)
3. Moderation Interface

== Changelog ==

= 2.85 =

* Fixes deprecation warnings on sites running PHP7
* Removes a javascript alert from the admin

= 2.84 =

* Fixes a bug where the comment count won't work on some themes

= 2.83 =

* Fix errors when using SSO and rendering javascript inline

= 2.82 =

* Fix PHP errors when there are no comments to sync
* Adds a new option to render Disqus javascript directly in page markup

= 2.81 =

* Fix for automatic comment syncing
* Make sure all markup validates for HTML5

= 2.80 =

* Move all scripts to separate files instead of rendering them in php
* Added a hook to attach custom functions to disqus_config in javascript
* Fixed exporting bug introduced in 2.78 (Thanks to mkilian)
* Numerous small compatibility and security enhancements

= 2.79 =

* Reinstate changes removed by 2.78

= 2.78 =

* Security fixes
* Compatibility for Wordpress version 4.0

= 2.77 =

* Fixes login by email issue
* Make sure Disqus is enabled after installation
* Additional security fixes

= 2.76 =

* Security fixes (Thanks to Nik Cubrilovic, Alexander Concha and Marc-Alexandre Montpas)
* Bump tested Wordpress version to 3.9.1
* Remove obsolete SSO button uploader
* Enable 'Output javascript in footer' by default during installation
* Fix for 'Reset' function not completely working the first time

= 2.75 =

* Bump supported WordPress version to 3.8.
* Properly encode site name for SSO login button.
* Increased timeout for comment exporter to 60 seconds.
* Use https: for admin pages
* Miscellaneous bug fixes and improvements.

= 2.74 =

* Updated settings UI
* Add filter hook for setting custom Disqus language
* For WP >= 3.5, use new media uploader
* Disable internal Wordpress commenting if Disqus is enabled (thanks Artem Russakovskii)
* Cleaned up installation and configuration flow
* Added link to WP backup guide in README
* Fix admin bar comments link
* Added a check to avoid a missing key notice when WP_DEBUG=TRUE (thanks Jason Lengstorf)
* Prevent 404 errors for embed.js from being reported by Google Webmaster Tools (missed in 2.73 README)

= 2.73 =

* Apply CDATA patch from Wordpress 3.4 to dsq_export_wxr_cdata() (thanks Artem
  Russakovskii for the patch).
* Added Single Sign-On log-in button and icon to options (only for sites using SSO)
* Output user website if set in SSO payload
* Added plugin activation statuses to debug info
* Bump supported WordPress version to 3.4.1
* Fixed issue where disqus_dupecheck won't properly uninstall
* Load second count.js (output-in-footer version) reference via SSL too
* Added screenshots

= 2.72 =

* Load count.js via SSL when page is accessed via HTTPS
* Fixed styling issue with Disqus admin.

= 2.71 =

* Fixed issue where embed wasn't using SSL if page was loaded via HTTPS
* Fixed issue with syncing where to user's without a display_name would
  revert back to Anonymous (really this time).
* Fixed issue where Google Webmaster Tools would incorrectly report 404s.
* Fixed issue with Disqus admin display issues.

= 2.70 =

* Properly uninstall disqus_dupecheck index when uninstalling plugin.
* Fixed issue with syncing where to user's without a display_name would
  revert back to Anonymous.
* Fixed issue where IP addresses weren't being synced properly.
* Allow non-Administrators (e.g., editors) to see Disqus Moderate panel
  inline (fixes GH-3)

= 2.69 =

* Bumped version number.

= 2.68 =

* Removed debugging information from web requests in CLI scripts (thanks
  Ryan Dewhurst for the report).
* Reduced sync lock time to 1 hour.
* Fixed an issue which was not allowing pending posts (for sync) to clear.
* Fixed an issue with CLI scripts when used with certain caching plugins.

= 2.67 =

* Bumped synchronization timer delays to 5 minutes.
* wp-cli.php now requires php_sapi_name to be set to 'cli' for execution.
* Fixed a bug with imported comments not storing the correct relative date.
* Added a lock for dsq_sync_forum, which can be overriden in the command line script
  with the --force tag.
* dsq_sync_forum will now handle all pending post metadata updates (formerly a separate
  cron task, dsq_sync_post).

= 2.66 =

* Fixed issue with jQuery usage which conflicted with updated jQuery version.

= 2.65 =

* Corrected a bug that was causing posts to not appear due to invalid references.

= 2.64 =

* Added an option to disable Disqus without deactivating the plugin.
* Added a second check for comment sync to prevent stampede race conditions in WP cron.

= 2.63 =

* Added command line script to import comments from DISQUS (scripts/import-comments.php).
* Added command line script to export comments to DISQUS (scripts/export-comments.php).
* The exporter will now only do one post at a time.
* The exporter now only sends required attributes to DISQUS.
* Moved media into its own directory.

= 2.62 =

* Changed legacy query to use = operator instead of LIKE so it can be indexed.

= 2.61 =

* Fixed an issue which was causing invalid information to be presented in RSS feeds.

= 2.60 =

* Added support for new Single Sign-On (API version 3.0).
* Improved support for legacy Single Sign-On.

= 2.55 =

* Added support for get_comments_number in templates.

= 2.54 =

* Updated URL to forum moderation.

= 2.53 =

* Fixed an issue with fsockopen and GET requests (only affects certain users).

= 2.52 =

* Fixed issue with Disqus-API package not getting updated (only affecting PHP4).

= 2.51 =

* Added CDATA comments for JavaScript.
* Syncing comments will now restore missing thread information from old imports.
* Install and uninstall processes have been improved.
* Fixed an issue in PHP4 with importing comments.
* Fixed an issue that could cause duplicate comments in some places.
* Added an option to remove existing imported comments when importing.

= 2.50 =

* Added missing file.

= 2.49 =

* Database usage has been optimized for storing comment meta data.

You can perform this migration automatically by visiting Comments -> Disqus, or if
you have a large database, you may do this by hand:

CREATE INDEX disqus_dupecheck ON `wp_commentmeta` (meta_key, meta_value(11));
INSERT INTO `wp_options` (blog_id, option_name, option_value, autoload) VALUES (0, 'disqus_version', '2.49', 'yes') ON DUPLICATE KEY UPDATE option_value = VALUES(option_value);

= 2.48 =

* Comment synchronization has been optimized to be a single call per-site.
* disqus.css will now only load when displaying comments

= 2.47 =

* Fixed a security hole with comment importing.
* Reverted ability to use default template comments design.
* Comments will now store which version they were imported under.
* Added an option to disable server side rendering.

= 2.46 =

* Better debugging information for export errors.
* Added the ability to manual import Disqus comments into Wordpress.
* Added thread_identifier support to exports.
* Cleaned up API error messages.
* Fixed a bug which was causing the import process to not grab only the latest set of comments.
* Added an option to disable automated synchronization with Disqus.

= 2.45 =

* Comments should now store thread information as well as certain other meta data.
* Optimize get_thread polling to only pull comments which aren't stored properly.

= 2.44 =

* Fixed JavaScript response for comments sync call.
* Comments are now marked as closed while showing the embed (fixes showing default respond form).

= 2.43 =

* Fixed a JavaScript syntax error which would cause linting to fail.
* Correct an issue that was causing comments.php to throw a syntax error under some configurations.

= 2.42 =

* Correct a bug with saving disqus_user_api_key (non-critical).
* Added settings to Debug Information.
* Adjusting all includes to use absolute paths.
* Adjusted JSON usage to solve a problem for some clients.

= 2.41 =

* Correct a bug with double urlencoding titles.

= 2.40 =

* Comments are now synced with Disqus as a delayed asynchronous cron event.
* Comment count code has been updated to use the new widget. (Comment counts
  must be linked to get tracked within "the loop" now).
* API bindings have been migrated to the generic 1.1 Disqus API.
* Pages will now properly update their permalink with Disqus when it changes. This is
  done within the sync event above.
* There is now a Debug Information pane under Advanced to assist with support requests.
* When Disqus is unreachable it will fallback to the theme's built-in comment display.
* Legacy mode is no longer available.
* The plugin management interface can now be localized.
* The plugin is now valid HTML5.

== Support ==

* Visit https://disqus.com/help/wordpress for help documentation.

* Visit https://help.disqus.com for help from our support team.
=== JSFiddle Shortcode ===
Contributors: wvega
Donate link: http://wvega.com/
Tags: jsfiddle
Requires at least: 3.2.1
Tested up to: 4.5
Stable tag: 1.1.0

Allows to easily embed Fiddles using a small shortcode.

== Description ==

## Usage:

`[jsfiddle url="http://jsfiddle.net/wvega/UupFu/" height="300px" include="result,html,js,css" font-color="39464E" menu-background-color="FFFFFF" code-background-color="f3f5f6" accent-color="1C90F3"]`

* All attributes are optional.
* `url` is the URL of the fiddle you want to embed, with or without trailing slash.
* `include` can be any combination of `result, html, js and css`, separated by commas; the tabs in the embedded fiddle will follow the order specified with the `include` attribute.
* `font-color` is the color used for the name of the tabs.
* `menu-background-color` is the color used for the background of the tabs.
* `code-background-color` is the color used for the background of the area where the code and results are shown.
* `accent-color` is the color of the indicator shown below the active tab.

## Result:

`<iframe style="width: 100%; height: 300px" src="http://jsfiddle.net/wvega/UupFu/embedded/result,html,js,css/?fontColor=39464E&menuColor=FFFFFF&bodyColor=f3f5f6&accentColor=1C90F3"></iframe>`

<iframe style="width: 100%; height: 300px" src="http://jsfiddle.net/wvega/UupFu/embedded/result,html,js,css/?fontColor=39464E&menuColor=FFFFFF&bodyColor=f3f5f6&accentColor=1C90F3"></iframe>

== Installation ==

1. Extract the plugin files to the `/wp-content/plugins/` directory.
1. Activate the plugin through the 'Plugins' menu in WordPress
1. Use `[jsfiddle]` in your post content.

== Frequently Asked Questions ==

== Screenshots ==

1. A JSFiddle embedded in a post using the plugin.

== Changelog ==

= 1.1.0 =

- Add support for font-color, menu-background-color, code-background-color and accent-color attributes.

= 1.0.1 =

- Tested up to WordPress 4.4-beta1.

= 1.0.0 =

- Fix PHP Deprecated notice.

= 0.1 =

- First release.

== Upgrade Notice ==
﻿=== Author Avatars List ===
Contributors: pbearne, bforchhammer
Donate link: https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=MZTZ5S8MGF75C&lc=CA&item_name=Wordpress%20Development%20%2f%20Paul%20Bearne&item_number=AuthorAvatarsList%20Plugin&currency_code=CAD&bn=PP%2dDonationsBF%3abtn_donateCC_LG%2egif%3aNonHosted
Tags: Avatar, Author, BuddyPress, xprofile, Comment, Editor, Image, Multisite, Photo, Picture, Profile, Shortcode, Random, Sidebar, Thumbnail, User, Widget, Wpmu, BBPress, co-authors
Requires at least: 3.0
Tested up to: 4.6
Stable tag: 1.9.8
License: GPLv2 or later
License URI: http://www.gnu.org/licenses/gpl-2.0.html

Display lists of user avatars using widgets or shortcodes.

== Description ==

This plugin makes it easy to *display lists of user avatars*, grouped by user roles, on your (multiuser) site. It also allows you to *insert single avatars* for blog users or any email address into a post or page - great for displaying an image of someone you're talking about.

It makes use of built in WordPress (core) functions to retrieve user information and get avatars.

Avatar lists can be inserted into your sidebar by adding a widget or into posts/pages by using a [shortcode](http://authoravatars.wordpress.com/documentation/authoravatars-shortcode/). The plugin comes with a tinymce editor plugin which makes inserting shortcodes very easy.

Please help with the plugin Translations at https://translate.wordpress.org/projects/wp-plugins/author-avatars.

Both the shortcode and widget can be configured to:

*   Show a custom title (widget only)
*   Only show specific user groups and/or hide certain users
*   Limit the number of users shown
*   Change the sort order of users or show in random order
*   Adjust the size of user avatars
*   Optionally show a user's name or biography
*   Show users from the current blog, all blogs or a selection of blogs (on WPMU/Multisite)
*   Group users by their blog (when showing from multiple blogs), and show the blog name above each grouping.
*   Support users from Co-Author Plus, Ultimate Member, BBpress and BuddyPress (xprofile)
*   Limit the number of avatars per page for large sets by adding a page_size to the shortcode e.g. "page_size=30" (shortcode only)

Additionaly, single user avatars can be inserted using the [show_avatar shortcode](http://authoravatars.wordpress.com/documentation/show_avatar-shortcode/) and configured to:

*   Adjust the size of the user avatar.
*   Align the avatar left, centered or right.

Please report bugs and provide feedback in the [wordpress support forum](http://wordpress.org/tags/author-avatars?forum_id=10#postform).

**Plugin support:** In 2011, Ben stepped down as maintainer of the Plugin, handing over ownership to co-author Paul Bearne, who continues to provide support and drive the development of new features.

== Installation ==

1. Upload the `author-avatars` folder to the `/wp-content/plugins/` directory
1. Activate the plugin through the 'Plugins' menu in WordPress
1. Enable and configure the widget as usual on the Design / Widgets page.

[Look at this page](https://authoravatars.wordpress.com/documentation/authoravatars-shortcode/) to find out how to use the [authoravatars] shortcode.

You can find information for developers [on this page](http://authoravatars.wordpress.com/documentation/developers-guide/).

== Upgrade Notice ==

<strong>Breaking change in 1.8.0 </strong> in CSS *.multiwidget_author_avatars* is now *.widget_author_avatars*. This is caused by a library change  in-order to support the jetpack visibility option.<br />
If you have added CSS to your theme you may have to update it for this upgrade (do a find and replace).

== Screenshots ==

1. Very simple set up of the widget on an empty blog.
2. The Widget configuration panel.
3. Examples of what the <code>[authoravatars]</code> shortcode can do.
4. Shortcode helper available from the WYSIWYG editor on the edit post page.
5. List of users with name and biography

== Changelog ==

= 1.9.8 =
Added Filter aa_user_raw_list

= 1.9.7 =
Added filter aa_user_show_last_post_query
Added the ability to use any URL in the profile contact section as a link
Added the ability for user_link to accept a comma-separated list as fall through if a URL is not found in first selection
Added contact_links to the short-code

= 1.9.6 =
readme update
removed php 4 constructors

= 1.9.5 =
Added sorting by white list values

= 1.9.4 =
Added white list for users

= 1.9.3 =
renamed function causing redeclare error

= 1.9.2 =
Added aa_user_show_last_post_type filter to allow setting of post type for last post link
added defaulted to author page if no last post is returned

= 1.9 =
fixed problem with WP 4.4 and widgets not saving
Add help translate link

= 1.8.8 =
set the page count to start at 1 not 0
Added support for UM profiles links


= 1.8.7 =
replaced parent::WP_Widget()  with parent::__construct to remove php 4 constructors
remove extract( $args, EXTR_SKIP and replaced with direct extracts
Added user id to CSS
Fixed Co_Author Plus listings

= 1.8.6.6 =
Added Hungarian Translation (by Otto Radics: Webmenedzser.hu - http://www.webmenedzser.hu)

= 1.8.6.5 =
Added filter (aa_user_level_for_editor) to allow control of who can see the tinyMCE editor button
Added last_post_filter option to link options
Fix the truncating of bio in single avatars
Changed AA in filter names to aa

= 1.8.6.4 =
Fixed a problem with upgrading if you had bios

= 1.8.6.3 =
Set the bios to maintain line breaks

= 1.8.6.2 =
Fixed the random order if not logged in

= 1.8.6.1 =
deploy script failed to add new file

= 1.8.6.0 =
* added the ability to truncate bio
* added support for BuddyPress xprofile
* add filter to post count number @props Andrew Minion


= 1.8.4.2 =
* Whitespace reformat
* removed trailing php closing from files

= 1.8.4.1 =
* Fix mixed limmint cache ID


= 1.8.4 =
* Added Ukrainian Translation (by Michael Yunat:  Get Voip - http://getvoip.com)
* Fixes around the cache id
* Replaced Deprecated : is_site_admin() with  is_super_admin()
* Fixed path to tinyMCE js files reomved hardcoded path
* fix static call when starting class

= 1.8.3 =
* added a tile to the span arond the image.
* disabled / delete the transit cache for logged in users to help clear them.
= 1.8.2 =
* change the caching to use transits for SQL calls with a 1 hour refesh
= 1.8.1 =
* Added support for tinyMCE version 4 ready for WordPress 3.9
= 1.8.0 =
* Replaced the pre 2.6 wordpres widget code with the current widget API calls to enable visablity setting
* CSS changed .multiwidget_author_avatars changed to .widget_author_avatars. This was caused by the widget API update
* Added expemently support for Co-Author Pluss Plugin - the post count does not work for linked account - will take a patch that fixs it :-)
* Moved the display option to the right column to make more room for roles
* Split 'Recent Activity' and 'BudyPress last activity' (only shows when buddypress running) to septerate options in the advance ordering option
* Split / removed 'Recent Activity' into sitewide (pages / custom page types / posts) and just posts (any old shortcode will call just posts)

= 1.7.1 =
* bubfix removed an extra ' in a SQL select in get_user_last_activity() function. Thanks to "basaja" for the bug report.

= 1.7.0 =
* Added Local User select to Single Avatar Shortcode creator
* Replaced wp_specialchars() with esc_html()
* Added BBPRESS_post_count as shortcode dispaly and sort options
* Added show_email to shortcode display option
* Added some translation updates
* Fixed issue with TniyMCE breaking when using HTTPS
* And a few other tidy ups
* Added SQL fliter to only fetch the users for the rolls being requested rather than all users
* Added caching to the main get_users function which will use an object cache if turned on

= 1.6.3 =
* Wraped ordering code in "remove_accents" functions to to replace Uni-code accents with non unicode versions so sort works as expected.
* Increased height of TinyMCE popup so content shows with scroll bars.
* Replaced text donate links with image link.

= 1.6.2 =
* Added display options for single Avatar options
* Added donation link

= 1.6.1 =
* Fixed a bug that stoped the loading of default CSS sheet for the plugin that I added a bug in in 1.6

= 1.6.0 =
* Added the option to link to BBpress profile in the link to the shortcode and generator  user_link=bbpress_memberpage
* Fixed bug - the the shortcode generator was shown up in the tinyMCE edit if it was loaded on a page (BBpress forum posts) the popup was 404'ing so add a $pagenow != 'index.php' to make sure we are in the addmin section
* Fixed bug causing the RTL layout to break

= 1.5.1 =
*  Added  Hindi language (by Love Chandel:  Outshine Solutions - http://outshinesolutions.com)

= 1.5 =
*  Added Paging to the short code
*  Added  Romanian language (by Alexander Ovsov:  Web Hosting Geeks - http://webhostinggeeks.com)

= 1.4 =
*   Fix a bug in the js code for the short-code generator in the tinyMCE editor.
*   It wasn't possible to set the show name / post count / biography options.

= 1.2 =
*   Added Italian translation (by Nata Strazda)

= 1.1 =
*   Added fix for buddypress which was using thumb instead of full versions of images.
*   Added support for network admin area (new in WP 3.1)
*   Added dutch translation by René (wpwebshop)
*   Fixed bug with min_post_count in shortcode

= 1.0 =
*   Fixed a number of styling issues
*   Fixed bug with capabilities (Wordpress 3 multisite)
*   Removed deprecated functions

= 0.9 =
*   Fixed compatibility with WordPress 3.0 (and its new multisite feature)
*   Fixed BuddyPress integration
*   Added feature to show avatars of commentators
*   Added feature to sort by firstname or lastname

= 0.8 =
*   Added feature to show a user's biography next to the avatar
*   Added feature to limit shown users by a minimum number of posts
*   Added feature to show a user's number of posts
*   Added Italian translation (by Gianni Diurno)

= 0.7.4 =
*   Fixed javascript issues with widget settings page and shortcode wizard in WordPress 2.8
*   Fixed support for translations
*   Added German translation
*   Added feature to sort by recent user activity (requires Buddypress)

= 0.7.3 =
*   Added filters to allow modification of userlist templates
*   Added "BuddyPress? Member Page" to the list of pages which a user can be linked to
*   Changed get_avatar() call so that it works with buddypress

= 0.7.2 =
*   Fixed a spelling mistake which prevented the plugin from loading

= 0.7.1 =
*   Improved inline function documentation
*   Fixed bug which caused a faulty name attribute for checkbox lists with only one choice. Now the "show name" option is working as exptected again.
*   Removed by-reference variable which causes PHP 4 parse errors

= 0.7 =
*   Removed invalid characters from uninstall.php (fixes uninstall behaviour).
*   New feature to link users to their website or blog (wpmu).
*   Added new feature to allow specification of a sort direction for sorted user lists.
*   Changed string-based sorting to case-insensitive (strcmp -> strcasecmp).
*   Added feature to sort users by date of registration.
*   Optimised UserList filtering.
*   Fixed numeric sorting issues (user_id and post count)
*   Added "order by number of posts" feature
*   Removed user role from avatar title.

= 0.6.2 =
*   Fixed bug which caused the plugin to crash in PHP 4.
*   Added uninstall.php to remove plugin related data when the plugin is deleted.

= 0.6.1 =
*   Fixed bug which caused other tinymce plugins to stop working.
*   Improved way of detecting a wpmu install.

= 0.6 =
*   Implementation of tinymce plugin.
*   Removed personalised jquery ui script and added just the packed ui.resizable.
*   Changed script and stylesheet handling (using register&enqueue functions with proper dependencies).
*   Refactored the "resizable avatar preview" script code into separate file.
*   FormHelper: Added option to generate textareas.
*   FormHelper: Added option to show expanded choice fields "inline".
*   Added improved function for cleaning up a value to be used as html id attribute.
*   AuthorAvatarsForm: added methods to ease generation of tabs and two-column panes.
*   AuthorAvatarsForm: added new renderField methods for shortcode type, email and alignment (used in show_avatar wizard).
*   Various Documentation updates and cleanups.
*   Refactored widget form field generation into new AuthorAvatarsForm.class.php to ease devevlopment of shortcode wizard.
*   Refactored form field generation code into new FormHelper.class.php.
*   Fixed size and position of blog selection box on sitewide admin page. Changed the name of is_wpmu() function to safer name AA_is_wpmu().
*   Removed "Group by blogs" checkbox for users without the blog selection filter.

= 0.5.1 =
*   Fixed method chaining error that caused a critical syntax error on PHP 4

= 0.5 =
*    Added "show_avatar" shortcode
*    Small MultiWidget fix by [Dan Cole](http://blog.firetree.net/2008/11/30/wordpress-multi-widget/#comment-24976)
*    Refactored [show_avatar] shortcode into new file ShowAvatarShortcode.class.php to keep it all nice and tidy.
*    Added basic blog filtering feature.
*    Added classes for settings and sitewide admin
*    Added sitewide setting for the blog filter
*    Updated update mechanism in AuthorAvatars.class.php
*    Added "Group by blog" feature

= 0.4 =
*    Added new [shortcode](http://authoravatars.wordpress.com/documentation/authoravatars-shortcode/) feature.
*    Fixed small bug in update procedure (version 0.1 to 0.2)

= 0.3 =
*    Fixed error that broke some javascript on "edit post" pages in wordpress 2.7

= 0.2 =
*    Widget: added avatar preview image to the control panel
*    Widget: added option to link the user/avatar to their respective "author page"
*    Widget: hiddenusers also allows user ids now (e.g. 1 for "admin")
*    Refactored the plugin to use [Alex Tingle's "MultiWidget" class](http://blog.firetree.net/2008/11/30/wordpress-multi-widget/)

== Frequently asked questions ==

= Shortcode, huh? =

A shortcode is a tag like <code>[authoravatars]</code> which you can insert into a page or post to display a list of users on that post/page. You can read more about shortcodes in general in the wordpress codex, for example [here](http://codex.wordpress.org/Using_the_gallery_shortcode) or [here](http://codex.wordpress.org/Shortcode_API).

= How do I use the author avatar shortcode? =

As of version 0.6 the plugin comes with a tinymce plugin which makes it very easy to insert shortcode(s).

If you'd like to do it manually it's still simple: just add <code>[authoravatars]</code> into your post and hit save! There's a large number of [parameters](http://authoravatars.wordpress.com/documentation/authoravatars-shortcode/) available.

The plugin comes with two shortcodes: <code>[authoravatars]</code> for lists of avatars and <code>[show_avatar]</code> for single avatars.

= I can't get my widget to show users from multiple blogs! =

Make sure you have enabled the "blog filter" in Site Admin / Author Avatars for the blog on which you are trying to use this feature on. By default this is only enabled for the root blog (blog id = 1).

And you are running [Wordpress MU](http://mu.wordpress.org/) (or respectively WordPress 3 in multi-site mode), right?

= Can I upload custom pictures for users? =

No, the Author Avatars List plugin only provides ways of <strong>displaying</strong> user avatars.

The plugin uses the Wordpress Core Template function <code>get_avatar()</code> to retrieve the actual avatar images. In order to display custom images you need to look for plugins which use/override WordPress' avatar features and provide respective upload features...

Have a look at the [User Photo](http://wordpress.org/extend/plugins/user-photo/) Plugin (turn on option "Override Avatar with User Photo") or the [Add Local Avatar](http://wordpress.org/extend/plugins/add-local-avatar/) Plugin.

= I get a "404 Page not found" error when I click on the avatar of a user! =

This can happens when you've choosen to link users to their "author page" and the user has not written any posts on a blog. There are two things that you should do in this situation:

1. To prevent the 404 page from showing up install the [Show authors without posts](http://wordpress.org/extend/plugins/show-authors-without-posts/) Plugin. This forces WordPress to always show the user page if the user exists.

2. If not already there add a custom user/author template to your theme. Otherwise if a user has no posts their user page is going to be quite empty by default...
You can find a [tutorial](http://codex.wordpress.org/Author_Templates) on Author Templates as well as a [Sample Template File](http://codex.wordpress.org/Author_Templates#Sample_Template_File) in the WordPress Codex.

= Can I use html in user biographies? =

Wordpress Core unfortunately strips all html from the user biography field when entered. Install the plugin [Weasel's HTML Bios](http://wordpress.org/extend/plugins/weasels-html-bios/) if you want to use html...

= How can I change the styling of the avatar lists? =

The styling of the widget is controlled by the styles defined in [css/widgets.css](http://plugins.trac.wordpress.org/browser/author-avatars/trunk/css/widget.css), avatars on posts/pages (using the shortcode) are styled by code in [css/shortcode.css](http://plugins.trac.wordpress.org/browser/author-avatars/trunk/css/shortcode.css).

You can override the styles in that file by copying a style block to your theme's `style.css` and adjusting respectively. For example add the following to remove the padding from avatars displayed in a widget:

`html .widget_author_avatars .author-list .user {
  padding: 0;
}`

demo edit=== Google Analyticator ===
Contributors: noahkagan
Tags: google analytics plugin, stats, statistics, google, analytics, dashboard, google analytics, tracking, widget, marketing,pageviews,visits, web stats, javascript
Requires at least: 3.2
Tested up to: 4.4.2
Stable tag: 6.4.9.7
License: GPLv2 or later
License URI: http://www.gnu.org/licenses/gpl-2.0.html

Easily view your Google Analytics and real-time statistics inside WordPress! Makes it super simple to add your tracking code too.

== Description ==

Google Analyticator makes it super easy to view Google Analytics within your WordPress dashboard. This eliminates the need to edit your template code to begin logging. Google Analyticator also includes several widgets for displaying Analytics data in the admin and on your blog.

One of the most popular WordPress plugins for Google Analytics! Over 3.5+ million downloads.

Check out our other plugin for getting more traffic [here](http://bit.ly/1PhVdpI).


= Features =

Google Analyticator Has the Following Features:

- Supports Universal (analytics.js) and traditional analytics (ga.js)
- Includes an admin dashboard widget that displays a graph of the last 30 days of visitors, a summary of site usage, the top pages, the top referrers, and the top searches
- Includes a widget that can be used to display visitor stat information on the front-end
- Supports outbound link tracking of all links on the page, including links not managed by WordPress
- Supports download link tracking
- Shortcodes to show off your Google Analytics stats publicly
- Supports event tracking with outbound links / downloads instead of the old pageview tracking method
- Support site speed tracking
- Allows hiding of Administrator visits without affecting Google Analytics' site overlay feature
- Supports any advanced tracking code Google provides
- Installs easily - unlike other plugins, the user doesn't even have to know their Analytics UID
- Provides complete control over options; disable any feature if needed
- Supports localization - get the settings page in your language of choice
- Ability to hide Google UID dropdown
- Translations - Polish, Turkish, Dutch and Spanish


A big thank you from the whole community to [Ronald](http://ronaldheft.com/) for all the hard work he put into this plugin.

We also would like to thank our translators:

Polish - Michał Mleczko from http://michalmleczko.waw.pl/
Turkish - Cansın Çağan Acarer from http://www.35pixel.com/

== Installation ==

1. Install the plugin and activate it.
2. Click to connect to Google Analytics and login.
3. Copy and paste your Google Authentication code and hit Save and Continue.
4. Choose the Analytics Account you want in the drop down.
5. Enable Google Analytics logging. 
6. Scroll to the bottom and save.
7. Then go to your Dashboard to see your stats.

== Frequently Asked Questions ==

If you receive an error after authenticating, refresh the page, and it will work properly. This is a known issue, and we are working with Google to resolve it.

For any support issues, please use the official WordPress support forums.

== Screenshots ==

1. An example of the admin dashboard widget displaying stats pulled from Google Analytics.
2. The top half of the settings page.
3. The configuration options for the front-end widget.
4. An example of a front-end widget configuration.
5. An example of a front-end widget configuration.
6. An example of a front-end widget configuration.


== Changelog ==

= 6.4.9.7 =
* Minor code cleanup changes.

= 6.4.9.6 =
* Resolve XSS vuln

= 6.4.9.5 =
* Remove notice from Dashboard

= 6.4.9.4 =
* Fix CSRF vulnerability on reset page

= 6.4.9.3 =
* Re-enable [analytics] shortcode with fix

= 6.4.9.2 =
* Temporarily disable [analytics] shortcode to fix a bug
 
= 6.4.9.1 =
* Added [analytics-counter] shortcode so you can display the page view counter widget anywhere

= 6.4.9 =
* Added [analytics] shortcode so you can add show off your analytics publicly

= 6.4.8 =
* Bug fix: anonymizeIP
* Reduced Memory Usage for dashboard
* Added Turkish, Spanish and Dutch
* Check token fix widget authentication
* Added Remarketing, Demographics and Interests reports for universal
* Changed Google API Client on setting of default path
* Fixes bugs

= 6.4.7.3 =
* Bug fix: Test data left in place of Domain name / UID dropdown

= 6.4.7.2 =
* Ability to hide Google UID dropdown
* Bug fix: rename stats_init to ganalyticator_stats_init
* Bug fix: Moved analyticsSnippet from line 1110 to line 1111
* Bug fix: added condition for empty href reported by @Jesin A http://wordpress.org/support/topic/bug-external-trackingjs-interferes-with-some-themes?replies=1
* Added Polish Translation from @mleczakm http://wordpress.org/support/topic/localization-translation

= 6.4.7 =
* Add missing Google PHP API classes

= 6.4.6 =
* Introduce Demographics and Interests support
* Enhanced Link attribution support
* added Universal Tracking (analytics.js) option
* Fixed sidebar Ad background for wp 3.8
* Used Custom Dimensions as replacement of Custom Variables for analytics.js

= 6.4.5 =
* Introduce Remarketing support
* Introduce Option to remove tracking on wp-login.
* Add link to Analytics training and option to remove.

= 6.4.4.3 =
* Bug fix: Duplicate data sometimes showing
* Bug fix: Flotr jQuery library clash with WooCommerce.

= 6.4.4.2 =
* Updated graph to not show current day as stats are incomplete.

= 6.4.4.1 =
* Update caused random Google error. Removed problem code.

= 6.4.4 =
* Added point tooltip. 
* removed jquery.sparkline.min.js
* added jquery.flot.min.js
* added 30 days, 60 days and yesterday selection
* removed line google-analytics-summary-widget.php line 222
* Use un-minified JS if script debug on. Props simonwheatley

= 6.4.3 =
* Fixes over strict validation on one field where not required causing PHP Errors. Thanks for head start jeremyclarke. 

= 6.4.2 =
* Fixes potential XSS security issue in admin - RECOMMENDED UPDATE. 

= 6.4.1 =
* Re-wrote caching on admin dashboard panel. Caches results for 6 hours, and speeds up display significantly using WordPress caching. 
* Added prevention on URI Class (Google) clashing. 

= 6.4 =
* Added better caching of dashboard widget.
* Added better error handling with Google API calls. Prevents breaking widget section if an error is found. 
* Updated Google API files to latest version (0.6.0)
* Added filter to prevent IDs being passed to google with 'ga:' appended twice (legacy user bug)
* Removed SiteSpeed option - done automatically with Google Analytics now.
* Changed some config options with Google API to try help any prev users with re-auth issues. 

= 6.3.4 =
* Missing admin_url() causing issues with sub-directory installs.
* Legacy code removed causing API errors with old ga_profileid variable conflicting.
* Added Google App ID To tracking ID as supplied by Google Analytics team. This is just for Google's own reporting. We do not get access to any of your data.
* Added support for users who wont want to authenticate with Google, but just use tracking code

= 6.3.3 =
* Using the admin_url() function for internal links. Should help people with WP installed in a sub directory.
* Added all vars to reset function to delete / deauthorize from Google.

= 6.3.2 =
* Based on user issues. Improved error handling from Google APIs (some more to go)
* Removed Javascript box on activation due to user issues
* Protected URITemplateParser class from being re-declared
* Added Reset option on plugin screen to allow re-authentication

= 6.3.1 =
* Small bug on upgrades patched

= 6.3 =
* Updated to authenticate with the new Google API

= 6.2 =
* Adds a new option for site speed tracking (enabled by default).
* Replaces deprecated tracking code _setVar with _setCustomVar.
* Improves the account select dropdown by organizing the accounts. Props bluntly.
* Prevents post preview pages from being tracked and skewing stats.

= 6.1.3 =
* Fixes a Javascript error on the WordPress login page.
* Improves profile id logic to hopefully fix dashboard errors for the people that experience them.
* Fixes PHP warnings on the dashboard widget with really old Analytics accounts.

= 6.1.2 =
* Fixes deprecated warnings when wp_debug is enabled.
* Fixes tracking code issues when trying to disabled certain user roles.
* Improves plugin security.

= 6.1.1 =
* Due to many questions about tracking code placement, [an FAQ article](http://forums.ronaldheft.com/viewtopic.php?f=5&t=967) has been written to address these placement questions. If you have any questions, this is a recommended read.
* Corrects issues related to selecting user roles to exclude from tracking / seeing the dashboard widget.
* Cleans up the display of user role names for WordPress versions below WordPress 3.0.
* Updates the included jQuary Sparkline library to 1.5.1, thus adding support for viewing the dashboard graph in all versions of Internet Explorer.
* Adds two hooks, google_analyticator_extra_js_before and google_analyticator_extra_js_after, enabling other WordPress plugins to insert additional tracking code.

= 6.1 =
* Prepares Google Analyticator for WordPress 3.0 compatibility.
* Updates the async tracking snippet to the latest version provided by Google. This new update solves issues with IE7 and IE6, and fixes all problems related to the snippet being placed in the <head> section of a page. You can rest easy knowing that async tracking in the <head> is completely compatible with IE now.
* Adds an html comment to the page header when tracking code is hidden due to the user admin level. This should make is less confusing for new Google Analyticator users, wondering if their tracking code is visible to the world.
* Adds a setting to specify a specific profile ID. This will help users with multiple Analytics profiles, by allowing them to specify which profile to use with the dashboard widget.
* Revamps the disable tracking settings. Now uses user roles and provides more fine grain control. If you use something other than the default, be sure to visit the settings page to ensure your settings are correct.
* Adds a new setting providing fine grain control over who can see the dashboard widget.
* Fixes the disappearing UID box bug when not authenticated.

= 6.0.2 =
* Updates the async tracking snippet to the latest version provided by Google.
* Improves the error message when failing to authenticate with Google, pointing users to a FAQ article to resolve their issues.

= 6.0.1 =
* Adds a missing closing quote on setVar - admin. If you use this option, update ASAP to prevent Javascript from breaking.

= 6.0 =
* Switches current tracking script (ga.js) to the new awesome async tracking script. In laymen's terms: updates to the latest tracking code, the tracking script will load faster, and tracking will be more reliable. If you use custom tracking code, be sure to migrate that code to the new async tracking methods.
* Removes settings made obsolete due to the new async tracking (footer tracking and http/https).
* Fixes the (not set) pages in the Top Pages section of the dashboard widget. Pages containing the title (not set) will be combined with the correct page and corresponding title. Note that I am still trying to get this bug fixed in the Google Analytics API; this is just a hold over until the bug is fixed.
* Adds a link to Google Analytics on the dashboard widget for quick access to view full stat reports.
* Fixes a Javascript error that prevented the dashboard widget from collapsing.
* Corrects a uid undefined error message that appeared if error reporting was set too high.
* Updates the included jQuery sparklines plugin to the latest version, 1.4.3.
* Adds an experimental function to retrieve page visitors stats for theme developers. This function is not final and only provided for advanced users who know what they're doing. Future versions will improve on the code already in place. Find the get_analytics_visits_by_page in google-analyticator.php to learn how to use. Use at your own risk.
* Fixes several security flaws identified during a recent security audit of Google Analyticator.
* Removes references to Spiral Web Consulting. Google Analyticator is now being developed exclusively by Ronald Heft.

= 5.3.2 =
* Prepares Google Analyticator for WordPress 2.9 compatibility.

= 5.3.1 =
* Corrects a fatal error on the settings page under WordPress 2.7.

= 5.3 =
* Converts API data call to AJAX to reduce the memory needed on page loads.
* Removes memory_limit alterations, since the default amount should be enough now.
* Disables the summary dashboard widget for non-admins, as defined by the admin level setting on Google Analyticator's settings page.

= 5.2.1 =
* Corrects a potential html sanitation vulnerability with text retrieved from the Google Analytics API.

= 5.2 =
* Adds support for deauthorizing with Google Analytics.
* Increases checks on the memory limit and now prevents the memory intensive functionality from running if there is insufficient memory.
* Adds authentication compatibility modes for users having issues with cURL and PHP Streams.
* Improves detection of Google Accounts that are not linked to Analytics accounts.
* Improves detection of accounts without stats.
* Cleans up the authentication URL, preventing the malformed URL error that Google would sometimes display.
* Removes hosted Google accounts from Google's authentication page.
* Adds an error message to the settings page if Google authentication fails.

= 5.1 =
* Fixes the broken/frozen error on the Dashboard introduced in Google Analyticator 5.0.
* Fixes an Internal Server Error received on the settings page under IIS servers.
* Adds an option to completely disable the included widgets.
* Removes the outbound and download prefixes from the Javascript if event tracking is enabled.
* Fixes a bug where the settings page always thought the Google account was authenticated.
* Prevents the Google API from even attempting to connect to Google's servers if the account is not authenticated.
* Increases the checks on returned Google API data to prevent unexpected states.
* Adds missing localized string to settings title.
* Removes the Google authentication and widgets from WordPress 2.7 due to compatibility issues. Users wishing to authenticate and use the widgets should upgrade to WordPress 2.8.
* Prevents PHP warnings from displaying on the dashboard summary widget when an Analytics account is new and does not have a history of data.

= 5.0 =
* Adds a new admin dashboard widget that displays a graph of the last 30 days of visitors, a summary of site usage, the top pages, the top referrers, and the top searches.
* Changes the Google authentication method to AuthSub. This removes the Google username / password requirement. **Users who had previously entered their username / password in the settings page will need to revisit the settings page and authenticate for the widget to continue to function.**
* Adds support for automatically retrieving an Analytics account's UID if Google Analyticator is authenticated with Google.
* Updates the Google Analytics API class to use the WordPress HTTP API, thus removing cURL as a core requirement for the widget.
* Updates the UID setting help to remove old urchin.js references and provide additional help for finding a UID.
* Prepares all strings for localization. 

= 4.3.4 =
* Fixes a bug that was breaking the save button on the settings page in IE.
* Prevents the widget from grabbing Analytics data earlier January 1, 2005.
* Fixes an incorrect default state for the event tracking option.
* Adds the date range used for widget data in an HTML comment to prevent misrepresented stats.

= 4.3.3 =
* Corrects XHTML validator errors present in the stat widget.
* Removes some stray code.

= 4.3.2 =
* Adds support for WordPress' new changelog readme.txt standard. Version information is now available from within the plugin updater.
* Enhances the links on the plugin page. Adds a settings, FAQ, and support link.

= 4.3.1 =
* Fixes a bug that broke the widget page when a username was not entered in settings.

= 4.3 =
* Adds support for event tracking of outbound links and downloads. This is the new, recommended way to track outbound links and downloads with Analytics. Event tracking is enabled by default, so users wishing to keep using the old method should disable this option immediately. See our FAQ for more information.
* Prevents files that are stored on external servers from being tracked as both a download and an external link.
* Corrects a file extension case sensitivity issue that prevented certain download links from being tracked.
* Includes a minified version of the outbound/download tracking javascript instead of the full code.
* Fixes a text size inconstancy on the settings page.

= 4.2.3 =
* Improves error reporting with API authentication.

= 4.2.2 =
* Fixes a bug in IE8 that would not allow the widget to display in the admin properly.

= 4.2.1 =
* Fixes an issue where stable versions of WordPress 2.8 were not using the new widget API.
* Changes SimplePie include to use WordPress' version if possible, since SimplePie is included in WordPress 2.8.
* Adds version number to the Google Analyticator comment.

= 4.2 =
* Adds support for the WordPress 2.8 widget API.
* Removes Google Analyticator comment in the header that if footer tracking is enabled.

= 4.1.1 =
* Adds support for tracking code in the footer with Adsense integration.
* Corrects the widget image location for users with WordPress installed in a sub-directory.
* Prevents Google API calls when widget information is not configured.
* Supports WordPress 2.8.

= 4.1 =
* Fixes a bug that was causing the Stats Widget to display "0" in every instance.
* Adds functionality to allow a custom timeframe to be configured for the visitors widget.
* Adds a function to enable use of the widget for users not using WordPress widgets.
* Adds an option to output the code needed to link Analytics and Adsense accounts.

= 4.0.1 =
* Disables stat widget if cURL does not exist.

= 4.0 =
* Adds Google Analytics API support.
* Adds a widget that will use your Google Analytics stats to display a visitor counter on your front-end.
* Adds functionality to make widget highly customizable in regards to color and text.

= 3.0.3 =
* Fixes a Javascript error on pages that have links without href tags.

= 3.0.2 =
* Improves display of external/download links in Google Analytics (strips http/https from url).
* Fixes a PHP warning message being displayed on pages with error reporting enabled.

= 3.01 =
* Adds an option to disable admin tracking by either removing the tracking code or setting a variable.
* Removes the external tracking code from back-end admin pages that was causing conflicts with other plugins.

= 3.0 =
* Google Analyticator is now supported by Spiral Web Consulting.
* Corrects bugs preventing both external and download link tracking from working.
* Adds settings to configure the external and download link tracking prefixes.
* Changes the way disabling admin tracking works. Now uses a line of code instead of removing the tracking code altogether. This will allow features like the site overlay to work.

= 2.40 =
* Replaces the PHP-based external tracking solution with a jQuery-based one.

= 2.3 =
* Updates the Analytics script to match a change by Google. This should resolve the undefined _gat errors.

= 2.24 =
* Fixes comment author issues once and for all.
* Fixes a SVN merge issue that prevented people from getting the last update.

= 2.23 =
* Reverting last version as it caused issues.

= 2.22 =
* Improves comment author regex causing some issues in WordPress 2.7. Thanks to jdub.

= 2.21 =
* Adds WordPress 2.7 support.

= 2.2 =
* Adds an option to specify the GA script location instead of relying on Google’s auto detect code. This may resolve the _gat is undefined errors.

= 2.14 =
* Stops the external link tracking code from appearing in feeds, breaking feed validation.
* Adds compatibility for a very rare few users who could not save options.

= 2.13 =
* Stops the external link tracking code from appearing in feeds, breaking feed validation.

= 2.12 =
* Applies the new administrator level selection to outbound tracking (I forgot to that in the last release).
* Fixes a potential plugin conflict.

= 2.11 =
* Adds an option to change what Google Analyticator considers a WordPress administrator.

= 2.1 =
* Fixes a bug preventing options from being saved under WordPress 2.5.
* Updates option page to comply with WordPress 2.5 user interface changes.
* Note: Users of WordPress 2.3 may wish to stay on 2.02 as the UI will look ‘weird’ under 2.3.

= 2.02 =
* Corrects potential XHTML validation issues with external link tracking.

= 2.01 =
* Corrects XHTML validation issues with ga.js.

= 2.0 =
* Adds support for the latest version of Google Analytics’ tracking code (ga.js).
* Reverts external link/download tracking method back to writing the tracking code in the HTML source, due to the previous Javascript library no longer being support. Users of previous Google Analyticator versions may safely delete ga_external-links.js.
* Slightly modified the way extra code is handled. There are now two sections (before tracker initialization and after tracker initialization) to handle ga.js’ extra functions. Refer to Google Analytics’ support documentation for use of these sections.

= 1.54 =
* Corrects problem where certain installation of WordPress do not have the user level value.

= 1.53 =
* Finally fixes the “Are you sure?” bug some users experience.

= 1.52 =
* Addresses compatibility issue with other JavaScript plugins.

= 1.5 =
* Now using JavaScript solution for keeping track of external links instead of the current URL rewrite method. JavaScript library is courtesy of Terenzani.it.
* Note: Google Analyticator is now in a folder. If upgrading from a version less than 1.5, delete google-analyticator.php from your /wp-content/plugins/ folder before proceeding.

= 1.42 =
* Fixes a bug where outbound link tracking would be disabled if the tracking code was in the footer.

= 1.41 =
* Added an option to insert the tracking code in the footer instead of the header.

= 1.4 =
* Adds support for download tracking.

= 1.31 =
* Fixes a small bug with backslashes in the additional tracking code box.

= 1.3 =
* WordPress 2.0 beta is now supported.
* Missing options page bug is finally fixed.

= 1.2 =
* Added support for outbound links.

= 1.12 =
* Fixing missing option button page bug.

= 1.11 =
* Fixed a bug where options page would sometimes not display.

= 1.1 =
* Added an option to disable administrator logging.
* Added an option to add any additional tracking code that Google has.

= 1.0 =
* Initial release.

== Upgrade Notice ==

= 6.1.1 =

Bug fix release. If you're having trouble accessing the settings page or use Internet Explorer, this is a recommended update.

= 6.1 =

Recommended update. Highlights include WordPress 3.0 support, updated async tracking code, dashboard stats by Analytics profile, more control over who gets tracked, and more control over who can see the dashboard widget. Settings have changed, so revisit the settings to verify.=== Embed GitHub Gist ===
Contributors: dflydev
Tags: github, gist, source, syntax, highlight, highlighter, embed
Requires at least: 2.8.6
Tested up to: 3.5
Stable tag: 0.13

Embed GitHub Gists into WordPress.

== Description ==

This project is available for forking on GitHub:

 * https://github.com/dflydev/embed-github-gist

Embed [GitHub](http://github.com/) [Gists](http://gist.github.com) into
WordPress. Provides a shortcode for posts and pages but also has the ability
to embed by hand in the event that a Gist needs to be embedded somewhere in
the page that does not pass through the shortcode filters.

Examples:

`[gist id=546764]`
`[gist id=546764 file=file.txt]`
`[gist id=546764 file=file.txt bump=1]`
`[gist]http://gist.github.com/546764[/gist]`


Cache is implemented with the Transients API to minimize delay on loading
content. Default TTL (time to live) is 86400 seconds or one day.

= Upcoming features: =

* Option for setting default TTL
* Option to bypass cache entirely
* Implement admin interface to control options

== Installation ==

1. Download the plugin zip file
1. Unzip contents of plugin zip file
1. Upload the embed-github-gist directory to the `/wp-content/plugins/` directory
1. Activate the plugin through the 'Plugins' menu in WordPress
1. Start using the plugin by adding Gists to posts!

== Frequently Asked Questions ==

= How can I fix rate limit exceded errors? =

Define EMBED_GISTHUB_USERNAME and EMBED_GISTHUB_PASSWORD in wp-settings.php.

= Can the cache be broken? =

Yes. Use a unique bump value to force cache to update. For instance, if you have
the following:

`[gist id=546764]`

The cache can be broken by specifying a bump value:

`[gist id=546764 bump=1]`

To break the cache again later, change to a new unique bump value:

`[gist id=546764 bump=2]`

= Can I change the TTL on a Gist-by-Gist basis? =

Yes. Specify a TTL (in seconds) like this:

`[gist id=546764 ttl=3600]`

= Can I embed a Gist outside of a post or a page? =

Yes.

`<?php echo embed_github_gist(546764); ?>`

= Can I display a specific file from my gist? =

Ues. You can use the `file` parameter:

`[gist id=546764 file=file.txt]`

== Screenshots ==

No screenshots now!

== Changelog ==

= 0.13 =
 * Looks at EMBED_GISTHUB_USERNAME and EMBED_GISTHUB_PASSWORD for API requests

= 0.12 =
 * Bump release ("same as 0.11")
 * Added upgrade notes

= 0.11 =
 * Updated to account for recent changes to Gist.

= 0.10 =
 * Bump release ("same as 0.9")

= 0.9 =
 * Fix js link bug. Thanks to wrightlabs.

= 0.8 =
 * Better handle SSL errors. Thanks to gabesumner and CaioProiete.

= 0.7 =
 * Edit to also include $file in cache key (thanks https://github.com/troufster)

= 0.6 =
 * Embed stylesheet is now cached locally by default
 * Fixed small file-bug when using json

= 0.5 =
 * Updates from oncletom (change default settings, works with new HTTPS URL from Gist)

= 0.4 =
 * Bump release ("same as 0.2")

= 0.3 =
 * Bump release ("same as 0.2")

= 0.2 =
 * Added to support passing a Gist URL as the content of the [gist] shortcode.

= 0.1 =
* First release.

== Upgrade Notice ==

= 0.13 =
Now looks for EMBED_GISTHUB_USERNAME and EMBED_GISTHUB_PASSWORD

= 0.12 =
= 0.11 =
Now defaults to not embedding HTML directly.
Now requires json_decode to be available.

= 0.5 =
Now defaults to using cache and embedding HTML directly.

= 0.4 =
No changes from previous release.

= 0.3 =
No changes from previous release.

= 0.2 =
Should have no negative impact.

= 0.1 =
First release.
=== Unfiltered MU ===
Contributors: mdawaffe, donncha, automattic
Tags: embed, iframe, html, script, object, unfiltered_html, WPMU
Tested up to: 3.0
Stable tag: 1.3.1
Requires at least: 2.9.2

This WordPress MU/WordPress 3.0 multisite plugin gives blog Administrators and Editors the ability to post whatever HTML they want. "Evil" tags will not be stripped.

== Description ==

Unfiltered MU gives Administrators and Editors the `unfiltered_html` capability.  This prevents WordPress MU/WordPress 3.0 multisite from stripping `<iframe>`, `<embed>`, etc. from these users' posts. Authors and Contributors do not get this capability for security reasons.

The plugin can either be used globally for your entire MU site, or it can be applied on a blog-by-blog basis.

For WordPress MU or WordPress 3.0 multisite only. Regular WordPress already offers this feature and does not need this plugin.

Warning! This is a very dangerous plugin to activate if you have untrusted users on your site. Any user could add Javascript code to steal the login cookies of any visitor who runs a blog on the same site. The rogue user can then inpersonate any of those users and wreak havoc. If all you want is to display videos on your WordPress MU blogs, use the native [Embed Support](http://codex.wordpress.org/Embeds), [Viper's Video Quicktags](http://wordpress.org/extend/plugins/vipers-video-quicktags/) or any of the other [video plugins](http://wordpress.org/extend/plugins/tags/video) on WordPress.org.
If you use this plugin your site will be hacked in one way or another if you allow anonymous users on the Internet to create blogs on your site. It's very dangerous.

Are you still 100% sure you want to use this plugin? 

== Installation ==

If you want to enable this feature on *all* blogs on your MU site:

 1. Place the `unfiltered-mu.php` file in your `wp-content/mu-plugins/` directory.  That's it.  Removing the plugin will remove the capability.

If you want to enable this feature on a *blog-by-blog* basis:

 1. Place the `unfiltered-mu.php` file in your `wp-content/plugins/` directory.
 2. Activate this plugin for those blogs on which you want this feature enabled or enable it sitewide with the "network activate" feature. Deactivating the plugin will remove the capablitiy for that blog.
=== Prettify For WordPress ===
Contributors: joshl, jaredharbour
Tags: prettify, code, syntax highlighting, themekit
Requires at least: 3.0
Tested up to: 3.1
Stable tag: 1.0.1

Easily add Google Code Prettify to your WordPress site. Customize the coloring with easy with options powered by ThemeKit For WordPress.

== Description ==

Prettify is a WordPress plugin that automatically embeds the required javascript for Google Code Prettify. It also includes a preview of what your code will look like and the ability to customize the look by installing [ThemeKit For WordPress](http://wordpress.org/extend/plugins/themekit/). ThemeKit For WordPress is also on WordPress.org.

If you prefer you can run the plugin without ThemeKit and it will just use the default Prettify styles.

Features include:

* ThemeKit ready.
* Easy to use syntax and styling. 
* Same syntax highlighter as [css-tricks.com](http://css-tricks.com).

== Installation ==

1. Install Prettify For WordPress either via the WordPress.org plugin directory, or by uploading the files to your server
2. After activating Prettify you will be able to use the default styling.
3. If you would like the custom styler then you will also need [ThemeKit For WordPress](http://wordpress.org/extend/plugins/themekit/)
3. That's it.  You're ready to go!
4. Enjoy your syntax highlighter.


== Frequently Asked Questions ==

=Nothing Yet...=

== Screenshots ==

1. Main part of the settings screen
2. Pre tag styling options
3. Prettify embedded in a theme.


== Changelog ==

= 1.0.1 =
* Resolved issue that would cause a fatal error in prettify-wordpress.php - Parse error: syntax error, unexpected T_FUNCTION in /wp-content/plugins/prettify-wordpress/prettify-wordpress.php on line 42

= 1.0 =
* Initial release
=== Enhanced Text Widget ===
Contributors: bostondv
Donate link: http://pomelodesign.com/donate/
Tags: widget, clickable, linkable, linked title, text, php, javascript, flash, linked title text, linked, text widget, php widget, link widget title, bare widget, widget shortcodes, enhanced text, better text widget, simple, html widget, css
Requires at least: 3.6
Tested up to: 4.3
Stable tag: 1.4.5
License: MIT
License URI: http://opensource.org/licenses/MIT

An enhanced version of the text widget that supports Text, HTML, CSS, JavaScript, Flash, Shortcodes and PHP with linkable widget title.

== Description ==

An enhanced version of the default text widget where you may have Text, HTML, CSS, JavaScript, Flash, Shortcodes and/or PHP as content with linkable widget title.

= Options =

* Title
* Title URL
* Widget CSS class
* Content supports Text, HTML, CSS, JavaScript, Flash, Shortcodes, and PHP
* Option to not display a title
* Option to open Title URL in new window
* Option to automatically add paragraphs to content
* Option to not output before/after_widget/title (bare widget)

= More Information =

* For help use [wordpress.org](http://wordpress.org/support/plugin/enhanced-text-widget/)
* Fork or contribute on [Github](https://github.com/bostondv/enhanced-text-widget/)
* Visit [our website](http://pomelodesign.com/) for more
* Follow me on [Twitter](http://twitter.com/bostondv/)
* View my other [WordPress Plugins](http://profiles.wordpress.org/bostondv/)

= Support =

Did you enjoy this plugin? Please [donate to support ongoing development](http://pomelodesign.com/donate/). Your contribution would be greatly appreciated.

== Installation ==

1. Download and extract the zip archive
2. Upload `enhanced-text-widget` folder to `/wp-content/plugins/`
3. Activate the plugin through the 'Plugins' menu in WordPress
4. Add the widget to a sidebar and configure the options as desired

== Frequently Asked Questions ==

Nothing right now.

== Screenshots ==

1. Widget options

== Upgrade Notice ==

= 1.3.4 =
This adds option to hide the title

= 1.2 =
This adds option to display bare text (no before/after widget/title elements are shown).

= 1.1 =
This adds a CSS class parameter to each widget.

= 1.0 =
This is the initial release.

== Changelog ==

= 1.4.5 =
* Adds option to hide empty widgets

= 1.4.4 =
* Updates tested to 4.0
* Updates license to GPLv3
* Minor code refactoring

= 1.4.3 =
* Adds Italian translation

= 1.4.2 =
* Removes widget caching
* Fixes issue with multiline PHP code

= 1.4 =
* Display text field in monospace font
* Code refactoring

= 1.3.4 =
* This adds option to hide the title
* Tested up to 3.5.1

= 1.3.3 =
* Fixes "Do not output before/after_widget/title" option
* Code cleanup

= 1.3.2 =
* Bug fixes

= 1.3 =
* Fixed debug warnings
* Fixed code merge issue

= 1.2 =
* This adds option to display bare text (no before/after widget/title elements are shown).

= 1.1 =
* Adds css class parameter that wraps widget.

= 1.0 =
* First release.=== Akismet ===
Contributors: matt, ryan, andy, mdawaffe, tellyworth, josephscott, lessbloat, eoigal, cfinke, automattic, jgs
Tags: akismet, comments, spam, antispam, anti-spam, anti spam, comment moderation, comment spam, contact form spam, spam comments
Requires at least: 3.2
Tested up to: 4.5.2
Stable tag: 3.1.11
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

PS: You'll need an [Akismet.com API key](https://akismet.com/get/) to use it.  Keys are free for personal blogs; paid subscriptions are available for businesses and commercial sites.

== Installation ==

Upload the Akismet plugin to your blog, Activate it, then enter your [Akismet.com API key](https://akismet.com/get/).

1, 2, 3: You're done!

== Changelog ==

= 3.1.11 =
*Release Date - 12 May 2016*

* Fixed a bug that could cause the "Check for Spam" button to skip some comments.
* Fixed a bug that could prevent some spam submissions from being sent to Akismet.
* Updated all links to use https:// when possible.
* Disabled Akismet debug logging unless WP_DEBUG and WP_DEBUG_LOG are both enabled.

= 3.1.10 =
*Release Date - 1 April 2016*

* Fixed a bug that could cause comments caught as spam to be placed in the Pending queue.
* Fixed a bug that could have resulted in comments that were caught by the core WordPress comment blacklist not to have a corresponding History entry.
* Fixed a bug that could have caused avoidable PHP warnings in the error log.

= 3.1.9 =
*Release Date - 28 March 2016*

* Add compatibility with Jetpack so that Jetpack can automatically configure Akismet settings when appropriate.
* Fixed a bug preventing some comment data from being sent to Akismet.

= 3.1.8 =
*Release Date - 4 March 2016*

* Fixed a bug preventing Akismet from being used with some plugins that rewrite admin URLs.
* Reduced the amount of bandwidth used on Akismet API calls
* Reduced the amount of space Akismet uses in the database
* Fixed a bug that could cause comments caught as spam to be placed in the Pending queue.

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
=== Add Post Footer ===
Contributors: freetime
Donate link: http://www.freetimefoto.com/add_post_footer_plugin_wordpress
Tags: post footer, advertisment, related post, tags
Requires at least: 2.0.2
Tested up to: 2.6.3
Stable tag: 1.1

Add Post Footer automatically add any custom paragraph, html code, ad code, technorati tags and/or related links list to the end of every posts.

== Description ==

Add Post Footer Plugin is very flexible and easy to use. The global options can be customized via wordpress admin option panel. Moreover the global options can override by adding special custom field to each post you want to customize its configuration individually. This will allow you to disable the appearance of some option or even add special code or paragraph for particular post. Please refer to instruction below in this page for detailed instruction.
Add Post Footer Plugin also embedded with improved [SimpleTags plugin](http://www.broobles.com/scripts/simpletags/), originally developed by Broobles, that can retrieve the tag that mark by [tag] and [tags] tag from the post any automatically generate tag list at the end of the post. The improved SimpleTags function in Add Post Footer Plugin also allow you to easily customized Technorati tags list label via wp-admin.
Please refer to the tips and addtional info provided at the [Add Post Footer Page](http://www.freetimefoto.com/add_post_footer_plugin_manual).

== Installation ==

   1. Unpack file package using your favorite zip software.
   2. Upload .php file to your wordpress plugin directory on your server.
   3. Login to wordpress admin and go to plugin tab and activate Add Post Footer Plugin.
   4. Go to Option => Add Post Footer tab to config the plugin option.

For SimpleTags user: You have to disable the original SimpleTags Plugin in order to show Technorati tags at the nd of the post. Otherwise the tag list will appear before Add footer section.

== Upgrade ==

Upgrade Add Post Footer is easy, just replace plugin file (add_post_footer.php) in plugin directory with new version. No need to re-config any options in "Post Footer" option tab. 

== Add Post Footer Plugin Configuration Panel ==

You can config the default appearance of your post footer generate by Add Post Footer Plugin in the option tab in your wp-admin (wp-admin => option => Post Footer).

###Ad. Code:

This section will allow you config the appearance of your ad from any ad network. The plugin are originally design for Chitika RPU ad, because it's easily to blended in with the post. But it also compatible with any other leading ad network script such as google adsense or widgetbucks. Just copy and paste your ad code to Ad code text area to define the default ad code. It's also possible to add any other text paragraph, html code or java script to this section.
All the options in each post can be override by adding special custom field **key: apf_ad_code** and use following value.

    * Value = 0: to turn off the ad for that post.
    * Value = 1: to turn on the ad, even if the option is turn off in config page.
    * Value = "Any Text or Code": this will add the text or code you enter in value field instead of the ad code you enter in config page.

(Please refer to Custom Field section below for detailed instruction).

**Ad Code: Options**

    * Add Ad before Related Post: The default value is "Yes", the Ad code will show as first block when Add Post Footer generate the footer. If you select "No" the Related Articles List will appear first and then your ad code.
    * Add following Ad. code to the end of post: The default value is "Yes", the Ad code will show in every post. Select "No" if you want to turn off the ad. You can also override this option for particular post by adding special custom field key: apf_ad_code and Value: 0 to turn off the ad or 1 to turn on .
    * Ad Code Script: The default ad code for every post. You can add special code for the post by using custom field key: apf_ad_code and enter your custom ad code in value field.

###Related Post List:

The Add Post Footer plugin can query related post and generate to the list to appear at the end of the post. Add Post Footer plugin will query recent post by post category. and listed it under the header you define. You can also specify maximum post that will be show in the list in this section.
To omitted the relates post list to show by adding custom field **key: "apf_relate_post"** and **Value: 0**. Or enter **Value: 1** to force related post list to show if it been turning off in config page.
You can also customize style of the related post list adding **"#apf_post_footer"** and **"li.apf_post_footer"** to your main CSS file. Please refer to example css file (apf.css) that include in download package.

**Related Post List: Options**

    * Add related post list: Default is "Yes". Change to "No" if you do not want to show related post list.
    * Maximum number of post in the list: The maximum number of posts allowed to shoe it the list. The default value is 5 posts.
    * The header text for post list: Enter the header for the related post list. This text will be between <h4> tag. If you didn't enter anything, the default label ("Related Articles:") will be use as header.

###Optional Text:

This section is similar to ad code section, you can add any text paragraph, html code or script (for example sponsor paragraph or credit) . This section will appear just before technorati tag.
You can also add special text for particular post by enter your paragraph to value field of custom field key: "apf_option_txt". This section is completely optional you can leave it blank to turn it off. And use custom field describe above to add the text to some post you need.

###Technorati Tags:

This option is improved version of SimpleTags plugin, originally developed by Broobles. If it turn on it will add tag list at the end of the post. The tags is retrieve form the post by using [tag] and [tags] tag. Please refer to [SimpleTags plugin page](http://www.broobles.com/scripts/simpletags/) for detailed instruction of adding tag to your post.
The Add Post Footer plugin is fully compatible with original SimpleTags plugin. We have add admin page that allow you to define label for your tag list and also option to turn it off. You can also add class simpletags (.simpletags) in your style sheet t style your tag list. The example of css are already include in apf.css found in download package.

**Know issue for SimpleTags User:** The SimpleTags user may need to deactivate original SimpleTags and use SimpleTags function in Add Post Footer plugin instead, in order to place the tag list appear as last section in the post. If both plugin are activate the Technorati Tags list will appear before Add Post Footer section.

**Technorati Tags: Options**

    * Show Technorati Tags to the end of post:  Default is "Yes". Change to "No" if you do not want to show Technorati Tags list.
    * The label for the tag list: Enter label for the tag list. You can use <b> or <em> tag to style your label (for example "<b>Technorati Tags: </b>". The default value is "blank". If you didn't enter any thing only tag list will appear without label.

###Addtional Option:

**Show Footer Every Where**
Change this option to "Yes" to force the plug-in to show the footer everywhere the posts are call. Otherwise they will show only in single post (default). 
Please use this option with caution. Showing the post with footer in index page may not display correctly. This will depend on your wordpress theme you are using.



###Custom Field:

Add Post Footer Plugin use several special custom field to override the plugin setting for each post. You can add custom field to the post in Write/Edit Post page in wordpress admin. You will find custom field just below trackback section in the page. Please refer to wordpress codex: using custom field for detailed instruction on adding post's custom field. Please not that you can use more than 1 key with only 1 value for each key in each post.

	**Key:** apf_ad_code **Value:** 0 	
	force to not showing "Ad code" section for specific post.

	**Key:** apf_ad_code **Value:** 1 	
	force to show Ad code for specific post even the "Add following Ad. code to the end of post:" option in config page is "No".

	**Key:** apf_ad_code **Value:** Text or HTML code 	
	Replace the ad code by value you enter in "Value" field

	**Key:** apf_relate_post **Value:** 0 	
	force to not showing the "Related Post link" for specific post.

	**Key:** apf_relate_post **Value:** 1 	
	force to showing the "Related Post link" for specific post. even the "Add related post list:" option in config page is "No".

	**Key:** apf_option_txt **Value:** Text or HTML code 	
	Add optional text or html code to specific post. Add Post Footer plugin will use text or html code in value field to show in the post. This option will work even you leave the optional text in config page blank.

###License

This project is released under the terms of the GNU GENERAL PUBLIC LICENSE

###Change Log:
    * Version 1.1 (18/11/2008) 
	- Add function to force the footer to show every where the post are call (show only in single post in previous version).
	- Revise admin page format for wordpress 2.5 and later
    * Version 1.0.1 (14/04/2008) 
	- Bug Fix for Related Post Function
    * Version 1.0 (28/02/2008) - Initial release
    

Please refer to the tips and addtional info provided at the [Add Post Footer Page](http://www.freetimefoto.com/add_post_footer_plugin_wordpress).
=== WP-Markdown ===
Contributors: stephenharris
Donate link: http://www.stephenharris.info
Tags: markdown, formatting,prettify,syntax highlighter,code
Requires at least: 3.1
Tested up to: 3.6
Stable tag: 1.5.1

Allows Markdown to be enabled in posts, comments and bbPress forums. 


== Description ==
This plug-in allows you to write posts (of any post type) using the Markdown syntax. The plug-in converts the Markdown into HTML prior to saving the post. When editing a post, the plug-in converts
it back into Markdown syntax. 

The plug-in also allows you to enable Markdown in **comments** and **BBPress forums**. In these instances the plug-in adds a toolbar, and preview of the processed Markdown with [Prettify](http://code.google.com/p/google-code-prettify/) syntax highlighter applied (similiar to that used in the Stack Exchange websites such as [WordPress Stack Exchange](http://wordpress.stackexchange.com/)).

WP-Markdown stores the processed HTML, so deactivating the plug-in will not affect your posts, comments or bbPress forums.

== Installation ==

Installation is standard and straight forward. 

1. Upload `markdown` folder (and all it's contents!) to the `/wp-content/plugins/` directory
1. Activate the plugin through the 'Plugins' menu in WordPress
1. Go to your Settings > Writing page and enable markdown for the appropriate post types and comments.


== Frequently Asked Questions ==

= How do I use Markdown syntax? =
For information on how to use Markdown sytnax pleae read: [Markdown: syntax](http://daringfireball.net/projects/markdown/syntax).

= What happens to the post content if I uninstall the plug-in? =
The plug-in uses Markdown to generate the appropriate HTML prior to the post saving to the database. When you edit a post, it is converted back to Markdown syntax. 
Once the plug-in is uninstalled you'll simply rever to editing the posts' HTML.

= How do I embed content? =
A clean install of WordPress allows you to (for example) include a YouTube url on a seperate line, whereupon it will automatically embed the video. This is not possible with WP-MarkDown installed (*I tried - I broke more things. But if you manage it, feel free to make a pull-request: https://github.com/stephenharris/WP-MarkDown*). 

You'll need  to use the `[embed]` shortcode.

= How do I prevent a bit of the page being parsed as MarkDown? =
Enclose it in a `div` tag. It'll be ignored.

= How do I allow the contents of a `div` tag to be parsed as MarkDown? =
Use `<div markdown="1">`.

== Screenshots ==

1. The Markdown toolbar and previewer on a bbPress forum
2. Plug-in settings, located at the bottom of the Writing settings page
3. The Markdown toolbar and previewer on a comment form
4. Example of Markdown syntax
5. The output of the example Markdown


== Changelog ==

= 1.5.1 =
* Addresses issues with (since withdrawn) 1.5 version

= 1.5 =
* Handle tables. See[#35](https://github.com/stephenharris/WP-MarkDown/issues/35)
* Apply responsive layout issue. See[#31](https://github.com/stephenharris/WP-MarkDown/issues/31)
* Use compressed prettify.js
* Fixed bug with lists not being escaped
* Fix textdomain. Change to 'wp-markdown'. Add pot.
* Fixes incompatability issues with bbPress.

= 1.4 =
* Fixes issue with consecutive shortcodes.
* Fixes editing bbPress topics/replies on the front end corrupts MarkDown. See [#25](https://github.com/stephenharris/WP-MarkDown/issues/25)

= 1.3 =
* Apply kses and balance tags after MD->HTML conversion. See[#23](https://github.com/stephenharris/WP-MarkDown/issues/23)
* Compress scripts and minify icon sprite. See [#7](https://github.com/stephenharris/WP-MarkDown/issues/7)
* Adds 'more' tag to MarkDown editor. 
* Adds support for iframes. See [#22](https://github.com/stephenharris/WP-MarkDown/issues/22).
* Fixes bug with underscores in shortcodes.
* Adds support for tbody, tfoot and thead tags
* Refactoring including renaming of plug-in style & script handles.

= 1.2 =
* Fixes problems with images nested inside links. See [#12](https://github.com/stephenharris/WP-MarkDown/issues/12)
* Ensure prettify is loaded, if needed, on home page. See [#6](https://github.com/stephenharris/WP-MarkDown/issues/6)
* Updated Markdownify
* Updated Prettify 

= 1.1.6 =

* Removes the wpautop/unwpautop functions. If using oembed, use embed shortcodes.
* Adds public wrapper functions.
* Remove bbPress front-end tinymce editor if using MarkDown


= 1.1.5 =

* Fixes bug introduced in 1.1.4 where line breaks are stripped (affects code blocks).


= 1.1.4 =

* Fixes bug where oembed would not work. Thanks ot Michael & Vinicius
* Adds a filters for MarkDown 'help' text: `wpmarkdown_help_text`
* Support for MarkDown extra (currently not supported in pagedown previewer)


= 1.1.3 =

* Stable with WordPress 3.4
* Fixed bug relating title attributes for links and images


= 1.1.2 =

* Fixed bug relating to comments by logged out users


= 1.1.1 =

* Fixed backslash bug


= 1.1 =

* Added option to replace TinyMCE with Markdown help bar on post editor


= 1.0 =

* Initial release




== Upgrade Notice ==

= 1.1.5 =
If you have upgraded to 1.1.4, please upgrade to 1.1.5. This release fixes a bug introduced in 1.1.4 (see http://wordpress.org/support/topic/plugin-wp-markdown-breaks-oembed-support)

= 1.1 =
* Added option to enable  the Markdown help bar on the backend post editor. Simple check Markdown help bar for 'Post editor' in the settings.
# WP-Markdown #
**Contributors:** stephenharris  
**Donate link:** http://www.stephenharris.info  
**Tags:** markdown, formatting,prettify,syntax highlighter,code  
**Requires at least:** 3.1  
**Tested up to:** 3.6  
**Stable tag:** 1.5.1  

Allows Markdown to be enabled in posts, comments and bbPress forums. 


## Description ##
This plug-in allows you to write posts (of any post type) using the Markdown syntax. The plug-in converts the Markdown into HTML prior to saving the post. When editing a post, the plug-in converts
it back into Markdown syntax. 

The plug-in also allows you to enable Markdown in **comments** and **BBPress forums**. In these instances the plug-in adds a toolbar, and preview of the processed Markdown with [Prettify](http://code.google.com/p/google-code-prettify/) syntax highlighter applied (similiar to that used in the Stack Exchange websites such as [WordPress Stack Exchange](http://wordpress.stackexchange.com/)).

WP-Markdown stores the processed HTML, so deactivating the plug-in will not affect your posts, comments or bbPress forums.

## Installation ##

Installation is standard and straight forward. 

1. Upload `markdown` folder (and all it's contents!) to the `/wp-content/plugins/` directory
1. Activate the plugin through the 'Plugins' menu in WordPress
1. Go to your Settings > Writing page and enable markdown for the appropriate post types and comments.


## Frequently Asked Questions ##

### How do I use Markdown syntax? ###
**For information on how to use Markdown sytnax pleae read:** [Markdown: syntax](http://daringfireball.net/projects/markdown/syntax).  

### What happens to the post content if I uninstall the plug-in? ###
The plug-in uses Markdown to generate the appropriate HTML prior to the post saving to the database. When you edit a post, it is converted back to Markdown syntax. 
Once the plug-in is uninstalled you'll simply rever to editing the posts' HTML.

### How do I embed content? ###
**A clean install of WordPress allows you to (for example) include a YouTube url on a seperate line, whereupon it will automatically embed the video. This is not possible with WP-MarkDown installed (*I tried - I broke more things. But if you manage it, feel free to make a pull-request:** https://github.com/stephenharris/WP-MarkDown*).   

You'll need  to use the `[embed]` shortcode.

### How do I prevent a bit of the page being parsed as MarkDown? ###
Enclose it in a `div` tag. It'll be ignored.

### How do I allow the contents of a `div` tag to be parsed as MarkDown? ###
Use `<div markdown="1">`.

## Screenshots ##

### 1. The Markdown toolbar and previewer on a bbPress forum ###
![The Markdown toolbar and previewer on a bbPress forum](http://s.wordpress.org/extend/plugins/wp-markdown/screenshot-1.png)

### 2. Plug-in settings, located at the bottom of the Writing settings page ###
![Plug-in settings, located at the bottom of the Writing settings page](http://s.wordpress.org/extend/plugins/wp-markdown/screenshot-2.png)

### 3. The Markdown toolbar and previewer on a comment form ###
![The Markdown toolbar and previewer on a comment form](http://s.wordpress.org/extend/plugins/wp-markdown/screenshot-3.png)

### 4. Example of Markdown syntax ###
![Example of Markdown syntax](http://s.wordpress.org/extend/plugins/wp-markdown/screenshot-4.png)

### 5. The output of the example Markdown ###
![The output of the example Markdown](http://s.wordpress.org/extend/plugins/wp-markdown/screenshot-5.png)



## Changelog ##

### 1.5.1 ###
* Addresses issues with (since withdrawn) 1.5 version

### 1.5 ###
* Handle tables. See[#35](https://github.com/stephenharris/WP-MarkDown/issues/35)
* Apply responsive layout issue. See[#31](https://github.com/stephenharris/WP-MarkDown/issues/31)
* Use compressed prettify.js
* Fixed bug with lists not being escaped
* Fix textdomain. Change to 'wp-markdown'. Add pot.
* Fixes incompatability issues with bbPress.

### 1.4 ###
* Fixes issue with consecutive shortcodes.
* Fixes editing bbPress topics/replies on the front end corrupts MarkDown. See [#25](https://github.com/stephenharris/WP-MarkDown/issues/25)

### 1.3 ###
* Apply kses and balance tags after MD->HTML conversion. See[#23](https://github.com/stephenharris/WP-MarkDown/issues/23)
* Compress scripts and minify icon sprite. See [#7](https://github.com/stephenharris/WP-MarkDown/issues/7)
* Adds 'more' tag to MarkDown editor. 
* Adds support for iframes. See [#22](https://github.com/stephenharris/WP-MarkDown/issues/22).
* Fixes bug with underscores in shortcodes.
* Adds support for tbody, tfoot and thead tags
* Refactoring including renaming of plug-in style & script handles.

### 1.2 ###
* Fixes problems with images nested inside links. See [#12](https://github.com/stephenharris/WP-MarkDown/issues/12)
* Ensure prettify is loaded, if needed, on home page. See [#6](https://github.com/stephenharris/WP-MarkDown/issues/6)
* Updated Markdownify
* Updated Prettify 

### 1.1.6 ###

* Removes the wpautop/unwpautop functions. If using oembed, use embed shortcodes.
* Adds public wrapper functions.
* Remove bbPress front-end tinymce editor if using MarkDown


### 1.1.5 ###

* Fixes bug introduced in 1.1.4 where line breaks are stripped (affects code blocks).


### 1.1.4 ###

* Fixes bug where oembed would not work. Thanks ot Michael & Vinicius
* Adds a filters for MarkDown 'help' text: `wpmarkdown_help_text`
* Support for MarkDown extra (currently not supported in pagedown previewer)


### 1.1.3 ###

* Stable with WordPress 3.4
* Fixed bug relating title attributes for links and images


### 1.1.2 ###

* Fixed bug relating to comments by logged out users


### 1.1.1 ###

* Fixed backslash bug


### 1.1 ###

* Added option to replace TinyMCE with Markdown help bar on post editor


### 1.0 ###

* Initial release




## Upgrade Notice ##

### 1.1.5 ###
If you have upgraded to 1.1.4, please upgrade to 1.1.5. This release fixes a bug introduced in 1.1.4 (see http://wordpress.org/support/topic/plugin-wp-markdown-breaks-oembed-support)

### 1.1 ###
* Added option to enable  the Markdown help bar on the backend post editor. Simple check Markdown help bar for 'Post editor' in the settings.
=== Jekyll Exporter ===
Contributors: benbalter
Tags: jekyll, github, github pages, yaml, export
Requires at least: 4.4
Tested up to: 4.6.0
Stable tag: 2.2.3
License: GPLv3 or later
License URI: http://www.gnu.org/licenses/gpl-3.0.html

== Features ==

* Converts all posts, pages, and settings from WordPress for use in Jekyll
* Export what your users see, not what the database stores (runs post content through `the_content` filter prior to export, allowing third-party plugins to modify the output)
* Converts all `post_content` to Markdown Extra (using Markdownify)
* Converts all `post_meta` and fields within the `wp_posts` table to YAML front matter for parsing by Jekyll
* Generates a `_config.yml` with all settings in the `wp_options` table
* Outputs a single zip file with `_config.yml`, pages, and `_posts` folder containing `.md` files for each post in the proper Jekyll naming convention
* No settings. Just a single click.

== Usage ==

1. Place plugin in `/wp-content/plugins/` folder
2. Activate plugin in WordPress dashboard
3. Select `Export to Jekyll` from the `Tools` menu

== More information ==

See [the full documentation](https://ben.balter.com/wordpress-to-jekyll-exporter):

* [Changelog](changelog.md)
* [Command-line-usage](command-line-usage.md)
* [Custom post types](custom-post-types.md)
* [Developing locally](developing-locally.md)
* [Minimum required PHP version](required-php-version.md)


== Changelog ==

[View Past Releases](https://github.com/benbalter/wordpress-to-jekyll-exporter/releases)


== Command-line Usage ==

If you're having trouble with your web server timing out before the export is complete, or if you just like terminal better, you may enjoy the command-line tool.

It works just like the plugin, but produces the zipfile on STDOUT:

```
php jekyll-export-cli.php > jekyll-export.zip
```

If using this method, you must run first `cd` into the wordpress-to-jekyll-exporter directory.

Alternatively, if you have [WP-CLI](http://wp-cli.org) installed, you can run:

```
wp jekyll-export > export.zip
```

The WP-CLI version will provide greater compatibility for alternate WordPress environments, such as when `wp-content` isn't in the usual location.


== Custom post types ==

To export custom post types, you'll need to add a filter to do the following:

```php
add_filter( 'jekyll_export_post_types', array('posts', 'pages', 'you-custom-post-type') );
```

The custom post type will be exported as a Jekyll collection. You'll need to initialize it in the resulting Jekyll site's `_config.yml`.


== Developing locally ==

= Prerequisites =
1. `sudo apt-get update`
1. `sudo apt install composer`
1. `sudo apt install php7.0-xml`
1. `sudo apt install php7.0-mysql`
1. `sudo apt install php7.0-zip`
1. `sudo apt install php-mbstring`
1. `sudo apt install subversion`
1. `sudo apt install mysql-server`
1. `sudo apt install php-pear`
1. `sudo pear install PHP_CodeSniffer`

= Bootstrap & Setup =
1. `git clone https://github.com/benbalter/wordpress-to-jekyll-exporter`
2. `cd wordpress-to-jekyll-exporter`
3. `script/bootstrap`
4. `script/setup`

= Running tests =
`script/cibuild`


== Minimum required PHP version ==

Many shared hosts may use an outdated version of PHP by default. **WordPress to Jekyll Export requires PHP 5.6 or greater.**

If you get an error message that looks like `unexpected T_STRING`, `unexpected '['` or `expecting T_CONSTANT_ENCAPSED_STRING`, you need to update your PHP version. In a shared hosting environment, you should be able to change the version of PHP used by simply toggling the setting in the host's control panel.

PHP 5.4 lost support from the PHP project itself in 2015. You'll need to be running at least PHP 5.5 which adds namespace support (the reason it's breaking), but I'd recommend at least 5.6 (or the latest your host supports) as it's the oldest supported version: <https://en.wikipedia.org/wiki/PHP#Release_history>
# WordPress to Jekyll Exporter

One-click WordPress plugin that converts all posts, pages, taxonomies, metadata, and settings to Markdown and YAML which can be dropped into Jekyll.

[![Build Status](https://travis-ci.org/benbalter/wordpress-to-jekyll-exporter.svg?branch=master)](https://travis-ci.org/benbalter/wordpress-to-jekyll-exporter)

## A Note

Many shared hosts may use an outdated version of PHP by default. **WordPress to Jekyll Export requires PHP 5.5 or greater.**

If you get an error message that looks like `unexpected T_STRING`, `unexpected '['` or `expecting T_CONSTANT_ENCAPSED_STRING`, you need to update your PHP version. In a shared hosting environment, you should be able to change the version of PHP used by simply toggling the setting in the host's control panel.

PHP 5.4 lost support from the PHP project itself in 2015. You'll need to be running at least PHP 5.5 which adds namespace support (the reason it's breaking), but I'd recommend at least 5.6 (or the latest your host supports) as it's the oldest supported version: <https://en.wikipedia.org/wiki/PHP#Release_history>

## Features

* Converts all posts, pages, and settings from WordPress for use in Jekyll
* Export what your users see, not what the database stores (runs post content through `the_content` filter prior to export, allowing third-party plugins to modify the output)
* Converts all `post_content` to Markdown Extra (using Markdownify)
* Converts all `post_meta` and fields within the `wp_posts` table to YAML front matter for parsing by Jekyll
* Generates a `_config.yml` with all settings in the `wp_options` table
* Outputs a single zip file with `_config.yml`, pages, and `_posts` folder containing `.md` files for each post in the proper Jekyll naming convention
* No settings. Just a single click.

## Usage

1. Place plugin in `/wp-content/plugins/` folder
2. Activate plugin in WordPress dashboard
3. Select `Export to Jekyll` from the `Tools` menu

## Command-line Usage

If you're having trouble with your web server timing out before the export is complete, or if you just like terminal better, you may enjoy the command-line tool.

It works just like the plugin, but produces the zipfile on STDOUT:

```
php jekyll-export-cli.php > jekyll-export.zip
```

If using this method, you must run first `cd` into the wordpress-to-jekyll-exporter directory.

Alternatively, if you have [WP-CLI](http://wp-cli.org) installed, you can run:

```
wp jekyll-export > export.zip
```

The WP-CLI version will provide greater compatibility for alternate WordPress environments, such as when `wp-content` isn't in the usual location.

## Custom post types

To export custom post types, you'll need to add a filter to do the following:

```php
add_filter( 'jekyll_export_post_types', array('posts', 'pages', 'you-custom-post-type') );
```

The custom post type will be exported as a Jekyll collection. You'll need to initialize it in the resulting Jekyll site's `_config.yml`.

## Changelog

[View Past Releases](https://github.com/benbalter/wordpress-to-jekyll-exporter/releases)

## Developing locally

1. `git clone https://github.com/benbalter/wordpress-to-jekyll-exporter`
2. `cd wordpress-to-jekyll-exporter`
3. `script/bootstrap`
4. `script/setup`

To run tests

`script/cibuild`

## License

The project is licensed under the GPLv3 or later
=== WP Static HTML Output ===
Contributors: leonstafford
Donate link: https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=NHEV6WLYJ6QWQ
Tags: static,html,export,performance,security,portable
Requires at least: 3.2
Tested up to: 4.9.1
Stable tag: 2.1

Allows you to leverage WordPress as a great CMS, but benefit from the speed, security and portability that a static website provides.

== Description ==

= Features =

 * generates a standalone, static html copy of your whole WordPress website
 * auto-deploy to local folder, FTP, S3, Dropbox or GitHub
 * one site to unlimited export targets
 * specify extra files to include in the output (ie, dynamically loaded assets)
 * desktop notifications alert you to when exports are complete
 * multi-language support (English/Japanese currently)

This plugin produces a static HTML version of your wordpress install, incredibly useful for anyone who would like the publishing power of wordpress but whose webhost doesn't allow dynamic PHP driven sites - such as Dropbox. You can run your development site on a different domain or offline, and the plugin will change all relevant URLs when you publish your site. It's a simple but powerful plugin, and after hitting the publish button, the plugin will output a ZIP file of your entire site, ready to upload straight to it's new home. 

= Limitations =

 * The nature of a static site implies that any dynamic elements of your wordpress install that reply upon Wordpress plugins or internal functions to operate dynamically will no longer work. Significantly, this means comments. You can workaround this by including a non-Wordpress version of an external comments provider into your theme code, such as the Disqus comment system. Any page elements that rely upon Javascript will function normally. 
 * inability to correctly capture some relative links in posts
 * inability to detect assets dynamically loaded via javascript after page load, these will need to specified separately (but will work)

= Similar plugins =

Having issues with this plugin? I try to support any issues via the official support forum or email, but if you want to try some other plugins for static export, give these a go:

 * [Simply Static](https://wordpress.org/plugins/simply-static/)

= Planned upgrades =

 * re-write export to relative URLs
 * progress meter to show % of .ZIP creation
 * realtime logs visible during / saved after export
 * speed improvements for large sites
 * selectively export only changed pages since last output
 * increase 1-click deployment options

Developed by [**Leon Stafford**](http://leonstafford.github.io). If you have any questions about this plugin's usage, installation or development, please email me at: [leon.stafford@mac.com](mailto:leon.stafford@mac.com)

== Installation ==

= via WP Admin panel =

1. Go to Plugins > Add New
2. Search for "WP Static HTML Output"
3. Click on the Install Now button
4. Activate the plugin and find it under the Tools menu

= manual installation =

1. Upload the static-html-output directory to the `/wp-content/plugins/` directory
2. Activate the plugin through the 'Plugins' menu in WordPress
3. Access the plugin settings from the "Tools" menu

= via WP CLI =

1. `wp --allow-root plugin install static-html-output-plugin --activate`


== Frequently Asked Questions ==

= Where can I publish my static site to? =

Anywhere that allows HTML files to be uploaded, ie:

 * GitHub/GitLab/BitBucket Pages (GitHub API integration now included)
 * S3 / CloudFront
 * Dropbox

= My comments don't work anymore! = 

See the readme. In brief: you can't use dynamic WordPress functions such as comments on a static site. Use an external comments provider such as Disqus, or live without them.

== Screenshots ==

1. The main interface
2. The main interface (Japanese)

== Changelog ==

= 2.1 =

 * Bugfix: don't hang on failures
 * Bugfix: fix option to retain files on server after export
 * Feature: 1-click publishing to a Netlify static site
 * Feature: view server log on failure


= 2.0 =

Critical bug fixes and a shiny new feature!

 * Bugfix: Dropbox export once again working after they killed version 1 of their API
 * Bugfix: Amazon S3 publishing fixed after bug introduced in 1.9
 * Feature: 1-click publishing to a GitHub Pages static site

Thanks to a user donation for funding the development work to get GitHub Pages exporting added as a new feature. I was also able to merge some recently contributed code from @patrickdk77, fixing the recent issues with AWS S3 and CloudFront. Finally, I couldn't make a new release without fixing the Dropbox export functionality - unbeknowst to me, they had killed version 1 of their API in September, breaking the functionality in this plugin, along with many other apps. 

= 1.9 =

 * Bugfix: Plugin now works on PHP 5.3

Though this is no longer an officially supported PHP version, many of this plugin's users are running PHP 5.3 or earlier. This fix should once again allow them to use the plugin, which has not been possible for them since about version 1.2. If you are one of these affected users, please now upgrade and enjoy all the new useful features!

= 1.8 =

 * Bugfix: improved URL rewriting

Plugin now ensures that formatted versions of your site's URL, ie //mydomain.com or http:\/\/mydomain.com\/ or the https/http equivalent are detected and rewritten to your target Base URL. The rewriting should now also work within CSS and JavaScript files. 

= 1.7 =

 * Bugfix: index.html contents empty for some users' themes/setups
 * Bugfix: remove PHP short open tags for better compatibility

= 1.6 =

 * Additional URLs now work again! Much needed bugfix.

= 1.5 =

 * bugfix for Dropbox export function not exporting all files

= 1.4 =

 * add Dropbox export option
 * fix bug some users encountered with 1.3 release

= 1.3 =

 * reduce plugin download size

= 1.2.2 =

 * supports Amazon Web Service's S3 as an export option

= 1.2.1 =

 * unlimited export targets
 * desktop notifications alert you when all exports are completed (no more staring at the screen)

= 1.2.0 =

 * 1-click generation and exporting to an FTP server
 * improved user experience when saving and exporting sites (no more white screen of boredom!)

= 1.1.3 =

* Now able to choose whether to strip unneeded meta tags from generated source code.
* Improved layout for config/export screen.
* Better feedback to user when system requirements are not met

= 1.1.2 =

* Version bump for supporting latest WP (4.7)

= 1.1.1 =

Added Features
 
* Updated author URL

Removed Features
 
* Premium options for One-Click publishing to provided hosting and domain

= 1.1.0 =

Added Features
 
* Premium options for One-Click publishing to provided hosting and domain

= 1.0.9 =

Added Features
 
* Japanese localization added (ja_UTF) 

= 1.0.8 =

Added Features
 
* long-awaited FTP transfer option integrated with basic functionality 
* option to save generated static HTML files on server

= 1.0.7 =

Fixed bug introduced with previous version. Applied following modifications contributed by Brian Coca (https://github.com/bcoca):

Added Features
 
* zip is now written atomically (write tmp file first, then rename to zip) which now allows polling scripts to only deal with completed zip file.
* username and blog id are now part of the file name. For auditing and handling 
multi site exports.

Bug fixes
 
* . and .. special directory entries are now ignored
* dirname is checked before access avoiding uninitialized warning 

= 1.0.6 =

Added shortcut to Settings page with Plugin Action Links   

= 1.0.5 =

Added link to relevant Settings page when permalinks structure is not set.  

= 1.0.4 =

Added a timeout value to URL request which was breaking for slow sites

= 1.0.3 =

Altered main codebase to fix recursion bug and endless loop. Essential upgrade. 

= 1.0.2 =
 
Initial release to Wordpress community

== Upgrade Notice ==

= 2.1 =

 * Bugfix: don't hang on failures
 * Bugfix: fix option to retain files on server after export
 * Feature: 1-click publishing to a Netlify static site
 * Feature: view server log on failure

= 2.0 =

Critical bug fixes and a shiny new feature!

 * Bugfix: Dropbox export once again working after they killed version 1 of their API
 * Bugfix: Amazon S3 publishing fixed after bug introduced in 1.9
 * Feature: 1-click publishing to a GitHub Pages static site

Thanks to a user donation for funding the development work to get GitHub Pages exporting added as a new feature. I was also able to merge some recently contributed code from @patrickdk77, fixing the recent issues with AWS S3 and CloudFront. Finally, I couldn't make a new release without fixing the Dropbox export functionality - unbeknowst to me, they had killed version 1 of their API in September, breaking the functionality in this plugin, along with many other apps. 

Please contact me to report any bugs or request new features. Thanks again for your support of this plugin!

= 1.9 =

Critical update for many users~!

 * Bugfix: Plugin now works on PHP 5.3

Though this is no longer an officially supported PHP version, many of this plugin's users are running PHP 5.3 or earlier. This fix should once again allow them to use the plugin, which has not been possible for them since about version 1.2. If you are one of these affected users, please now upgrade and enjoy all the new useful features!

= 1.8 =

 * Bugfix: improved URL rewriting

Plugin now ensures that formatted versions of your site's URL, ie //mydomain.com or http:\/\/mydomain.com\/ or the https/http equivalent are detected and rewritten to your target Base URL. The rewriting should now also work within CSS and JavaScript files. 

= 1.7 =

 * Bugfix: index.html contents empty for some users' themes/setups
 * Bugfix: remove PHP short open tags for better compatibility

= 1.6 =

 * Additional URLs now work again! Much needed bugfix. Recommended upgrade.

= 1.5 =

 * bugfix for Dropbox export function not exporting all files

= 1.4 =

 * add Dropbox export option
 * fix bug some users encountered with 1.3 release

= 1.3 =

From this update on, will only do major point increases, ie 1.3, 1.4, vs 1.3.1, 1.3.2. This is due to way WP plugin directory only reports usage stats across major version numbers.

 * reduce plugin download size

= 1.2.2 =

 * supports Amazon Web Service's S3 as an export option

= 1.2.1 =

This update brings much desired multiple export targets. Please note, it will need you to enter your settings again as the guts of the plugin changed quite a bit and a settings migration didn't make the cut.

 * unlimited export targets
 * desktop notifications alert you when all exports are completed (no more staring at the screen)

= 1.2.0 =

Good to be back into developing the plugin again. This release brings some good functionality, though may be some bugs. If so, please contact me to fix: lionhive@gmail.com Cheers, Leon

 * 1-click generation and exporting to an FTP server
 * improved user experience when saving and exporting sites (no more white screen of boredom!)

= 1.1.2 =

Minor version bump after compatibility checking with latest WordPress (4.7).

= 1.1.0 =
Premium VIP subscription option added, providing static optimized hosting and a domain for your website.
[![Codeship Status for tightenco/collect](https://codeship.com/projects/7a88b780-04ee-0134-0d48-3e31f9e0f6b8/status?branch=master)](https://codeship.com/projects/154325)

![](https://raw.githubusercontent.com/tightenco/collect/master/collect-logo.png)

# Collect - Illuminate Collections

Import [Laravel's Collections](https://laravel.com/docs/collections) into non-Laravel packages easily, without needing to require the entire `Illuminate\Support` package. ([Why not pull `Illuminate\Support` in framework-agnostic packages](https://yuloh.github.io/2016/dont-use-illuminate-support/))

Written by Taylor Otwell as a part of Laravel's [Illuminate/Support](https://github.com/illuminate/support) package, Collect is just the code from Support needed in order to use Collections on their own.

Lovingly split by Matt Stauffer for [Tighten Co.](http://tighten.co/), with a kick in the butt to finally do it from [@assertchris](https://github.com/assertchris).

## Installation

With [Composer](https://getcomposer.org):

```bash
composer require tightenco/collect
```


## FAQ
 - **Will this develop independently from Illuminate's Collections?**  
    No. Right now it's split manually, but the goal is for it shortly to be split automatically to keep it in sync with Laravel's Collections, even mirroring the release numbers.
 - **Why is the package `tightenco/collect` instead of `illuminate/collect`?**  
    It's not an official Laravel package so we don't want to use the Packagist namespace reserved by Laravel packages. One day `Collection` may be extracted from `illuminate/support` to a new package. If so, we'll deprecate this package and point to the core version.
 - **Why not just use an array?**  
    What a great question. [Tighten alum Adam Wathan has a book about that.](http://adamwathan.me/refactoring-to-collections/)
=== User Bio Widget ===
Tags: widget, bio, user bio, author bio, gravatar
Requires at least: 2.8
Tested up to: 3.0
Stable tag: 0.2

Easily display the "Biographical Info", and Gravatar, of any author's user profile in your blog's sidebar. Compatible with the Multi-Site functionality.

== Description ==

This widget will easily allow you to display the "Biographical Info" of any blog author's user profile in the sidebar. It allows you to choose from multiple authors/users on the blog, if your blog does, in fact, have multiple authors. Subscribers are excluded for obvious reasons (Contributors, Authors, Editors, and Administrators are included).

Additionally, the widget grants the ability to display the selected author's Gravatar, with multiple size and alignment options available.

Please submit any bug reports, support questions, or requests <a href="http://anthonybubel.com/contact">here</a>.

== Installation ==

1. Upload `user-bio-widget.php` to the `/wp-content/plugins/` directory.
1. Activate the plugin through the 'Plugins -> Installed' menu in your dashboard.
1. Add the 'User Bio' Widget to your sidebar via 'Appearance -> Widgets' in your dashboard.

== Frequently Asked Questions ==

= How can I style the Gravatar image? =

You can add and customize the following CSS within your theme's primary stylesheet/CSS file (normally style.css):

.ub-grav img {
***These are just some example properties you can use***
border: 2px solid #eeeeee;
padding: 3px;
}

= Are subscribers included? =

No. Only contributors, authors, editors, and administrators (i.e. any user able to actually create posts).

= What's a Gravatar? =

A Gravatar is a Globally Recognized Avatar (i.e. your user picture/icon). You can upload one via <a href="http://gravatar.com">http://gravatar.com</a> (it will be attached to your e-mail address).

= Can I only display my Gravatar with the widget? =

Yes; simply leave your "Biographical Info" section (in your user profile) blank, and configure the widget to display your Gravatar.

= If an author doesn't have a Gravatar uploaded, and they configure the widget to display a Gravatar, which image is used? =

The default image is determined by the 'Default Avatar' setting found in your dashboard under Settings -> Discussion.

= I have a Gravatar configured, but it's not appearing. What's up? =

For the Gravatar to appear, you must have the 'Show Avatars' option under Settings -> Discussion set to 'Show Avatars'. Also, please check your 'Maximum Rating' setting and compare it with your own Gravatar's rating.

== Changelog ==

= 0.2 =
* Adds compatibility with the WordPress 3.0 Multi-Site feature.
* Adds a configuration option for displaying only the Gravatar image (with no bio text).
* Updates the message displayed if no bio information is entered in the author's profile.
* Adds some additional styling to the "Gravatar Options" section in the widget's configuration panel.
* Slightly modifies the default styling of the Gravatar image.
    

  

<!DOCTYPE html>
<html>
  <head>
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="chrome=1">
        <title>wp-content/plugins/multisite-recent-blogs-widget/readme.txt at master from btompkins/CodeBetter.Com-Wordpress - GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />

    <link href="https://d3nwyuy0nl342s.cloudfront.net/059ebbfb26cc3f47e727f59297076b08fac34c23/stylesheets/bundle_common.css" media="screen" rel="stylesheet" type="text/css" />
<link href="https://d3nwyuy0nl342s.cloudfront.net/059ebbfb26cc3f47e727f59297076b08fac34c23/stylesheets/bundle_github.css" media="screen" rel="stylesheet" type="text/css" />
    

    <script type="text/javascript">
      if (typeof console == "undefined" || typeof console.log == "undefined")
        console = { log: function() {} }
    </script>
    <script type="text/javascript" charset="utf-8">
      var GitHub = {
        assetHost: 'https://d3nwyuy0nl342s.cloudfront.net'
      }
      var github_user = null
      
    </script>
    <script src="https://d3nwyuy0nl342s.cloudfront.net/059ebbfb26cc3f47e727f59297076b08fac34c23/javascripts/jquery/jquery-1.4.2.min.js" type="text/javascript"></script>
    <script src="https://d3nwyuy0nl342s.cloudfront.net/059ebbfb26cc3f47e727f59297076b08fac34c23/javascripts/bundle_common.js" type="text/javascript"></script>
<script src="https://d3nwyuy0nl342s.cloudfront.net/059ebbfb26cc3f47e727f59297076b08fac34c23/javascripts/bundle_github.js" type="text/javascript"></script>


    
    <script type="text/javascript" charset="utf-8">
      GitHub.spy({
        repo: "btompkins/CodeBetter.Com-Wordpress"
      })
    </script>

    
  <link href="https://github.com/btompkins/CodeBetter.Com-Wordpress/commits/master.atom" rel="alternate" title="Recent Commits to CodeBetter.Com-Wordpress:master" type="application/atom+xml" />

        <meta name="description" content="CodeBetter.Com Wordpress Source" />
    <script type="text/javascript">
      GitHub.nameWithOwner = GitHub.nameWithOwner || "btompkins/CodeBetter.Com-Wordpress";
      GitHub.currentRef = 'master';
      GitHub.commitSHA = "6d4a407f607b8b580d5cbc78544ef5798a9c3bfd";
      GitHub.currentPath = 'wp-content/plugins/multisite-recent-blogs-widget/readme.txt';
      GitHub.masterBranch = "master";

      
    </script>
  

        <script type="text/javascript">
      var _gaq = _gaq || [];
      _gaq.push(['_setAccount', 'UA-3769691-2']);
      _gaq.push(['_setDomainName', 'none']);
      _gaq.push(['_trackPageview']);
      (function() {
        var ga = document.createElement('script');
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        ga.setAttribute('async', 'true');
        document.documentElement.firstChild.appendChild(ga);
      })();
    </script>

    
  </head>

  

  <body class="logged_out page-blob">
    

    

    

    

    

    <div class="subnavd" id="main">
      <div id="header" class="true">
        
          <a class="logo boring" href="https://github.com">
            <img alt="github" class="default" src="https://d3nwyuy0nl342s.cloudfront.net/images/modules/header/logov3.png" />
            <!--[if (gt IE 8)|!(IE)]><!-->
            <img alt="github" class="hover" src="https://d3nwyuy0nl342s.cloudfront.net/images/modules/header/logov3-hover.png" />
            <!--<![endif]-->
          </a>
        
        
        <div class="topsearch">
  
    <ul class="nav logged_out">
      <li class="pricing"><a href="/plans">Pricing and Signup</a></li>
      <li class="explore"><a href="/explore">Explore GitHub</a></li>
      <li class="features"><a href="/features">Features</a></li>
      <li class="blog"><a href="/blog">Blog</a></li>
      <li class="login"><a href="/login?return_to=https://github.com/btompkins/CodeBetter.Com-Wordpress/blob/master/wp-content/plugins/multisite-recent-blogs-widget/readme.txt">Login</a></li>
    </ul>
  
</div>

      </div>

      
      
        
    <div class="site">
      <div class="pagehead repohead vis-public    instapaper_ignore readability-menu">

      

      <div class="title-actions-bar">
        <h1>
          <a href="/btompkins">btompkins</a> / <strong><a href="https://github.com/btompkins/CodeBetter.Com-Wordpress">CodeBetter.Com-Wordpress</a></strong>
          
          
        </h1>

        
    <ul class="actions">
      

      
        <li class="for-owner" style="display:none"><a href="https://github.com/btompkins/CodeBetter.Com-Wordpress/admin" class="minibutton btn-admin "><span><span class="icon"></span>Admin</span></a></li>
        <li>
          <a href="/btompkins/CodeBetter.Com-Wordpress/toggle_watch" class="minibutton btn-watch " id="watch_button" onclick="var f = document.createElement('form'); f.style.display = 'none'; this.parentNode.appendChild(f); f.method = 'POST'; f.action = this.href;var s = document.createElement('input'); s.setAttribute('type', 'hidden'); s.setAttribute('name', 'authenticity_token'); s.setAttribute('value', '953c7e1808637de776390f6e7e4c8eeb2c03e730'); f.appendChild(s);f.submit();return false;" style="display:none"><span><span class="icon"></span>Watch</span></a>
          <a href="/btompkins/CodeBetter.Com-Wordpress/toggle_watch" class="minibutton btn-watch " id="unwatch_button" onclick="var f = document.createElement('form'); f.style.display = 'none'; this.parentNode.appendChild(f); f.method = 'POST'; f.action = this.href;var s = document.createElement('input'); s.setAttribute('type', 'hidden'); s.setAttribute('name', 'authenticity_token'); s.setAttribute('value', '953c7e1808637de776390f6e7e4c8eeb2c03e730'); f.appendChild(s);f.submit();return false;" style="display:none"><span><span class="icon"></span>Unwatch</span></a>
        </li>
        
          
            <li class="for-notforked" style="display:none"><a href="/btompkins/CodeBetter.Com-Wordpress/fork" class="minibutton btn-fork " id="fork_button" onclick="var f = document.createElement('form'); f.style.display = 'none'; this.parentNode.appendChild(f); f.method = 'POST'; f.action = this.href;var s = document.createElement('input'); s.setAttribute('type', 'hidden'); s.setAttribute('name', 'authenticity_token'); s.setAttribute('value', '953c7e1808637de776390f6e7e4c8eeb2c03e730'); f.appendChild(s);f.submit();return false;"><span><span class="icon"></span>Fork</span></a></li>
            <li class="for-hasfork" style="display:none"><a href="#" class="minibutton btn-fork " id="your_fork_button"><span><span class="icon"></span>Your Fork</span></a></li>
          

          
        
      
      
      <li class="repostats">
        <ul class="repo-stats">
          <li class="watchers"><a href="/btompkins/CodeBetter.Com-Wordpress/watchers" title="Watchers" class="tooltipped downwards">1</a></li>
          <li class="forks"><a href="/btompkins/CodeBetter.Com-Wordpress/network" title="Forks" class="tooltipped downwards">1</a></li>
        </ul>
      </li>
    </ul>

      </div>

        
  <ul class="tabs">
    <li><a href="https://github.com/btompkins/CodeBetter.Com-Wordpress" class="selected" highlight="repo_source">Source</a></li>
    <li><a href="https://github.com/btompkins/CodeBetter.Com-Wordpress/commits/master" highlight="repo_commits">Commits</a></li>
    <li><a href="/btompkins/CodeBetter.Com-Wordpress/network" highlight="repo_network">Network</a></li>
    <li><a href="/btompkins/CodeBetter.Com-Wordpress/pulls" highlight="repo_pulls">Pull Requests (0)</a></li>

    

    
      
      <li><a href="/btompkins/CodeBetter.Com-Wordpress/issues" highlight="issues">Issues (3)</a></li>
    

            
    <li><a href="/btompkins/CodeBetter.Com-Wordpress/graphs" highlight="repo_graphs">Graphs</a></li>

    <li class="contextswitch nochoices">
      <span class="toggle leftwards" >
        <em>Branch:</em>
        <code>master</code>
      </span>
    </li>
  </ul>

  <div style="display:none" id="pl-description"><p><em class="placeholder">click here to add a description</em></p></div>
  <div style="display:none" id="pl-homepage"><p><em class="placeholder">click here to add a homepage</em></p></div>

  <div class="subnav-bar">
  
  <ul>
    <li>
      
      <a href="/btompkins/CodeBetter.Com-Wordpress/branches" class="dropdown">Switch Branches (1)</a>
      <ul>
        
          
            <li><strong>master &#x2713;</strong></li>
            
      </ul>
    </li>
    <li>
      <a href="#" class="dropdown defunct">Switch Tags (0)</a>
      
    </li>
    <li>
    
    <a href="/btompkins/CodeBetter.Com-Wordpress/branches" class="manage">Branch List</a>
    
    </li>
  </ul>
</div>

  
  
  
  
  
  



        
    <div id="repo_details" class="metabox clearfix">
      <div id="repo_details_loader" class="metabox-loader" style="display:none">Sending Request&hellip;</div>

        <a href="/btompkins/CodeBetter.Com-Wordpress/downloads" class="download-source" id="download_button" title="Download source, tagged packages and binaries."><span class="icon"></span>Downloads</a>

      <div id="repository_desc_wrapper">
      <div id="repository_description" rel="repository_description_edit">
        
          <p>CodeBetter.Com Wordpress Source
            <span id="read_more" style="display:none">&mdash; <a href="#readme">Read more</a></span>
          </p>
        
      </div>

      <div id="repository_description_edit" style="display:none;" class="inline-edit">
        <form action="/btompkins/CodeBetter.Com-Wordpress/admin/update" method="post"><div style="margin:0;padding:0"><input name="authenticity_token" type="hidden" value="953c7e1808637de776390f6e7e4c8eeb2c03e730" /></div>
          <input type="hidden" name="field" value="repository_description">
          <input type="text" class="textfield" name="value" value="CodeBetter.Com Wordpress Source">
          <div class="form-actions">
            <button class="minibutton"><span>Save</span></button> &nbsp; <a href="#" class="cancel">Cancel</a>
          </div>
        </form>
      </div>

      
      <div class="repository-homepage" id="repository_homepage" rel="repository_homepage_edit">
        <p><a href="http://" rel="nofollow"></a></p>
      </div>

      <div id="repository_homepage_edit" style="display:none;" class="inline-edit">
        <form action="/btompkins/CodeBetter.Com-Wordpress/admin/update" method="post"><div style="margin:0;padding:0"><input name="authenticity_token" type="hidden" value="953c7e1808637de776390f6e7e4c8eeb2c03e730" /></div>
          <input type="hidden" name="field" value="repository_homepage">
          <input type="text" class="textfield" name="value" value="">
          <div class="form-actions">
            <button class="minibutton"><span>Save</span></button> &nbsp; <a href="#" class="cancel">Cancel</a>
          </div>
        </form>
      </div>
      </div>
      <div class="rule "></div>
            <div id="url_box" class="url-box">
        <ul class="clone-urls">
          
            
            <li id="http_clone_url"><a href="https://github.com/btompkins/CodeBetter.Com-Wordpress.git" data-permissions="Read-Only">HTTP</a></li>
            <li id="public_clone_url"><a href="git://github.com/btompkins/CodeBetter.Com-Wordpress.git" data-permissions="Read-Only">Git Read-Only</a></li>
          
          
        </ul>
        <input type="text" spellcheck="false" id="url_field" class="url-field" />
              <span style="display:none" id="url_box_clippy"></span>
      <span id="clippy_tooltip_url_box_clippy" class="clippy-tooltip tooltipped" title="copy to clipboard">
      <object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000"
              width="14"
              height="14"
              class="clippy"
              id="clippy" >
      <param name="movie" value="https://d3nwyuy0nl342s.cloudfront.net/flash/clippy.swf?v5"/>
      <param name="allowScriptAccess" value="always" />
      <param name="quality" value="high" />
      <param name="scale" value="noscale" />
      <param NAME="FlashVars" value="id=url_box_clippy&amp;copied=&amp;copyto=">
      <param name="bgcolor" value="#FFFFFF">
      <param name="wmode" value="opaque">
      <embed src="https://d3nwyuy0nl342s.cloudfront.net/flash/clippy.swf?v5"
             width="14"
             height="14"
             name="clippy"
             quality="high"
             allowScriptAccess="always"
             type="application/x-shockwave-flash"
             pluginspage="http://www.macromedia.com/go/getflashplayer"
             FlashVars="id=url_box_clippy&amp;copied=&amp;copyto="
             bgcolor="#FFFFFF"
             wmode="opaque"
      />
      </object>
      </span>

        <p id="url_description">This URL has <strong>Read+Write</strong> access</p>
      </div>
    </div>

    <div class="frame frame-center tree-finder" style="display:none">
      <div class="breadcrumb">
        <b><a href="/btompkins/CodeBetter.Com-Wordpress">CodeBetter.Com-Wordpress</a></b> /
        <input class="tree-finder-input" type="text" name="query" autocomplete="off" spellcheck="false">
      </div>

      
        <div class="octotip">
          <p>
            <a href="/btompkins/CodeBetter.Com-Wordpress/dismiss-tree-finder-help" class="dismiss js-dismiss-tree-list-help" title="Hide this notice forever">Dismiss</a>
            <strong>Octotip:</strong> You've activated the <em>file finder</em> by pressing <span class="kbd">t</span>
            Start typing to filter the file list. Use <span class="kbd badmono">↑</span> and <span class="kbd badmono">↓</span> to navigate,
            <span class="kbd">enter</span> to view files.
          </p>
        </div>
      

      <table class="tree-browser" cellpadding="0" cellspacing="0">
        <tr class="js-header"><th>&nbsp;</th><th>name</th></tr>
        <tr class="js-no-results no-results" style="display: none">
          <th colspan="2">No matching files</th>
        </tr>
        <tbody class="js-results-list">
        </tbody>
      </table>
    </div>

    <div id="jump-to-line" style="display:none">
      <h2>Jump to Line</h2>
      <form>
        <input class="textfield" type="text">
        <div class="full-button">
          <button type="submit" class="classy">
            <span>Go</span>
          </button>
        </div>
      </form>
    </div>


        

      </div><!-- /.pagehead -->

      

  





<script type="text/javascript">
  GitHub.downloadRepo = '/btompkins/CodeBetter.Com-Wordpress/archives/master'
  GitHub.revType = "master"

  GitHub.controllerName = "blob"
  GitHub.actionName     = "show"
  GitHub.currentAction  = "blob#show"

  

  
</script>






<div class="flash-messages"></div>


  <div id="commit">
    <div class="group">
        
  <div class="envelope commit">
    <div class="human">
      
        <div class="message"><pre><a href="/btompkins/CodeBetter.Com-Wordpress/commit/6d4a407f607b8b580d5cbc78544ef5798a9c3bfd">Add wp-config to gitignore</a> </pre></div>
      

      <div class="actor">
        <div class="gravatar">
          
          <img src="https://secure.gravatar.com/avatar/b9a9f2e092b6cfd8483c38a0b66b1f83?s=140&d=https://d3nwyuy0nl342s.cloudfront.net%2Fimages%2Fgravatars%2Fgravatar-140.png" alt="" width="30" height="30"  />
        </div>
        <div class="name">brendan <span>(author)</span></div>
        <div class="date">
          <abbr class="relatize" title="2011-02-22 12:51:53">Tue Feb 22 12:51:53 -0800 2011</abbr>
        </div>
      </div>

      

    </div>
    <div class="machine">
      <span>c</span>ommit&nbsp;&nbsp;<a href="/btompkins/CodeBetter.Com-Wordpress/commit/6d4a407f607b8b580d5cbc78544ef5798a9c3bfd" hotkey="c">6d4a407f607b8b580d5c</a><br />
      <span>t</span>ree&nbsp;&nbsp;&nbsp;&nbsp;<a href="/btompkins/CodeBetter.Com-Wordpress/tree/6d4a407f607b8b580d5cbc78544ef5798a9c3bfd/wp-content" hotkey="t">3d60e391b92e67001c44</a><br />
      
        <span>p</span>arent&nbsp;
        
        <a href="/btompkins/CodeBetter.Com-Wordpress/tree/decf874d4da6ea3da5ea7e4e9cb79a89f95116d9/wp-content" hotkey="p">decf874d4da6ea3da5ea</a>
      

    </div>
  </div>

    </div>
  </div>



  <div id="slider">

  

    <div class="breadcrumb" data-path="wp-content/plugins/multisite-recent-blogs-widget/readme.txt/">
      <b><a href="/btompkins/CodeBetter.Com-Wordpress/tree/6d4a407f607b8b580d5cbc78544ef5798a9c3bfd">CodeBetter.Com-Wordpress</a></b> / <a href="/btompkins/CodeBetter.Com-Wordpress/tree/6d4a407f607b8b580d5cbc78544ef5798a9c3bfd/wp-content">wp-content</a> / <a href="/btompkins/CodeBetter.Com-Wordpress/tree/6d4a407f607b8b580d5cbc78544ef5798a9c3bfd/wp-content/plugins">plugins</a> / <a href="/btompkins/CodeBetter.Com-Wordpress/tree/6d4a407f607b8b580d5cbc78544ef5798a9c3bfd/wp-content/plugins/multisite-recent-blogs-widget">multisite-recent-blogs-widget</a> / readme.txt       <span style="display:none" id="clippy_597">wp-content/plugins/multisite-recent-blogs-widget/readme.txt</span>
      
      <object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000"
              width="110"
              height="14"
              class="clippy"
              id="clippy" >
      <param name="movie" value="https://d3nwyuy0nl342s.cloudfront.net/flash/clippy.swf?v5"/>
      <param name="allowScriptAccess" value="always" />
      <param name="quality" value="high" />
      <param name="scale" value="noscale" />
      <param NAME="FlashVars" value="id=clippy_597&amp;copied=copied!&amp;copyto=copy to clipboard">
      <param name="bgcolor" value="#FFFFFF">
      <param name="wmode" value="opaque">
      <embed src="https://d3nwyuy0nl342s.cloudfront.net/flash/clippy.swf?v5"
             width="110"
             height="14"
             name="clippy"
             quality="high"
             allowScriptAccess="always"
             type="application/x-shockwave-flash"
             pluginspage="http://www.macromedia.com/go/getflashplayer"
             FlashVars="id=clippy_597&amp;copied=copied!&amp;copyto=copy to clipboard"
             bgcolor="#FFFFFF"
             wmode="opaque"
      />
      </object>
      

    </div>

    <div class="frames">
      <div class="frame frame-center" data-path="wp-content/plugins/multisite-recent-blogs-widget/readme.txt/">
        
          <ul class="big-actions">
            
            <li><a class="file-edit-link minibutton" href="/btompkins/CodeBetter.Com-Wordpress/file-edit/__current_ref__/wp-content/plugins/multisite-recent-blogs-widget/readme.txt"><span>Edit this file</span></a></li>
          </ul>
        

        <div id="files">
          <div class="file">
            <div class="meta">
              <div class="info">
                <span class="icon"><img alt="Txt" height="16" src="https://d3nwyuy0nl342s.cloudfront.net/images/icons/txt.png" width="16" /></span>
                <span class="mode" title="File Mode">100644</span>
                
                  <span>65 lines (43 sloc)</span>
                
                <span>1.826 kb</span>
              </div>
              <ul class="actions">
                <li><a href="/btompkins/CodeBetter.Com-Wordpress/raw/master/wp-content/plugins/multisite-recent-blogs-widget/readme.txt" id="raw-url">raw</a></li>
                
                  <li><a href="/btompkins/CodeBetter.Com-Wordpress/blame/master/wp-content/plugins/multisite-recent-blogs-widget/readme.txt">blame</a></li>
                
                <li><a href="/btompkins/CodeBetter.Com-Wordpress/commits/master/wp-content/plugins/multisite-recent-blogs-widget/readme.txt">history</a></li>
              </ul>
            </div>
            
  <div class="data type-text">
    
      <table cellpadding="0" cellspacing="0">
        <tr>
          <td>
            <pre class="line_numbers"><span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
</pre>
          </td>
          <td width="100%">
            
              
                <div class="highlight"><pre><div class='line' id='LC1'>=== Multisite Recent Posts Widget ===</div><div class='line' id='LC2'>Contributors: copperblade</div><div class='line' id='LC3'>Donate link: http://bitfreedom.com/</div><div class='line' id='LC4'>Tags: recent posts, widget, wpmu</div><div class='line' id='LC5'>Requires at least: 3.0</div><div class='line' id='LC6'>Tested up to: 3.0.1</div><div class='line' id='LC7'>Stable tag: 1.1</div><div class='line' id='LC8'><br/></div><div class='line' id='LC9'>Creates a widget to show a list of the most recent posts across a WordPress MU installation.  It shows the most recent post from each blog.  This plugin is based on the work of many authors.</div><div class='line' id='LC10'><br/></div><div class='line' id='LC11'>== Description ==</div><div class='line' id='LC12'><br/></div><div class='line' id='LC13'>Creates a widget to show a list of the most recent posts across a WordPress MU installation.  It shows the most recent post from each blog.  This plugin is based on the work of many authors.</div><div class='line' id='LC14'><br/></div><div class='line' id='LC15'>This works on previous versions of WPMU, but not on previous versions of WordPress (where it doesn&#39;t make sense).</div><div class='line' id='LC16'><br/></div><div class='line' id='LC17'><br/></div><div class='line' id='LC18'>== Installation ==</div><div class='line' id='LC19'><br/></div><div class='line' id='LC20'>1. Upload `wpmu-recent-posts-widget.php` to the `/wp-content/plugins/` directory</div><div class='line' id='LC21'>2. Activate the plugin through the &#39;Plugins&#39; menu in WordPress</div><div class='line' id='LC22'>3. Add the WPMU Recent Posts widget under &#39;Appearance-&gt;Widgets&#39;</div><div class='line' id='LC23'><br/></div><div class='line' id='LC24'>== Frequently Asked Questions ==</div><div class='line' id='LC25'><br/></div><div class='line' id='LC26'>= What about foo bar? =</div><div class='line' id='LC27'><br/></div><div class='line' id='LC28'>Answer to foo bar dilemma.</div><div class='line' id='LC29'><br/></div><div class='line' id='LC30'>== Screenshots ==</div><div class='line' id='LC31'><br/></div><div class='line' id='LC32'>1. Widget options</div><div class='line' id='LC33'><br/></div><div class='line' id='LC34'>== Changelog ==</div><div class='line' id='LC35'><br/></div><div class='line' id='LC36'>= 1.1 =</div><div class='line' id='LC37'>* Bugfix on base prefix</div><div class='line' id='LC38'><br/></div><div class='line' id='LC39'>= 1.0 =</div><div class='line' id='LC40'>* Added widget options</div><div class='line' id='LC41'>* No. of days set to &lt;= 0 will not limit by time</div><div class='line' id='LC42'><br/></div><div class='line' id='LC43'>= 0.4 =</div><div class='line' id='LC44'>* Widgetized</div><div class='line' id='LC45'>* Set default parameters</div><div class='line' id='LC46'>* Removed default new posts of new blogs from results</div><div class='line' id='LC47'>* Thanks to:  http://lonewolf-online.net/computers/wordpress/create-widgets/</div><div class='line' id='LC48'><br/></div><div class='line' id='LC49'>= 0.3.2 =</div><div class='line' id='LC50'>* Author: G. Morehouse</div><div class='line' id='LC51'>* Author URI: http://wiki.evernex.com/index.php?title=Wordpress_MU_sitewide_recent_posts_plugin</div><div class='line' id='LC52'><br/></div><div class='line' id='LC53'>= 0.3.1 =</div><div class='line' id='LC54'>* Author: Sven Laqua</div><div class='line' id='LC55'>* Author URI: http://www.sl-works.de/</div><div class='line' id='LC56'><br/></div><div class='line' id='LC57'>= 0.3 =</div><div class='line' id='LC58'>* Author: Ron Rennick</div><div class='line' id='LC59'>* Author URI: http://atypicalhomeschool.net/</div><div class='line' id='LC60'><br/></div><div class='line' id='LC61'><br/></div><div class='line' id='LC62'>== Options ==</div><div class='line' id='LC63'>* Number of posts to show - list this many posts.</div><div class='line' id='LC64'>* Number of days to limit - only go back this number of days to get posts.  Set to -1 for no limit (default).</div><div class='line' id='LC65'><br/></div></pre></div>
              
            
          </td>
        </tr>
      </table>
    
  </div>


          </div>
        </div>
      </div>
    </div>
  

  </div>


<div class="frame frame-loading" style="display:none;">
  <img src="https://d3nwyuy0nl342s.cloudfront.net/images/modules/ajax/big_spinner_336699.gif" height="32" width="32">
</div>

    </div>
  
      
    </div>

    <div id="footer" class="clearfix">
      <div class="site">
        <div class="sponsor">
          <a href="http://www.rackspace.com" class="logo">
            <img alt="Dedicated Server" height="36" src="https://d3nwyuy0nl342s.cloudfront.net/images/modules/footer/rackspace_logo.png?v2" width="38" />
          </a>
          Powered by the <a href="http://www.rackspace.com ">Dedicated
          Servers</a> and<br/> <a href="http://www.rackspacecloud.com">Cloud
          Computing</a> of Rackspace Hosting<span>&reg;</span>
        </div>

        <ul class="links">
          <li class="blog"><a href="https://github.com/blog">Blog</a></li>
          <li><a href="/login/multipass?to=http%3A%2F%2Fsupport.github.com">Support</a></li>
          <li><a href="https://github.com/training">Training</a></li>
          <li><a href="http://jobs.github.com">Job Board</a></li>
          <li><a href="http://shop.github.com">Shop</a></li>
          <li><a href="https://github.com/contact">Contact</a></li>
          <li><a href="http://develop.github.com">API</a></li>
          <li><a href="http://status.github.com">Status</a></li>
        </ul>
        <ul class="sosueme">
          <li class="main">&copy; 2011 <span id="_rrt" title="0.04121s from fe4.rs.github.com">GitHub</span> Inc. All rights reserved.</li>
          <li><a href="/site/terms">Terms of Service</a></li>
          <li><a href="/site/privacy">Privacy</a></li>
          <li><a href="https://github.com/security">Security</a></li>
        </ul>
      </div>
    </div><!-- /#footer -->

    
      
      
        <!-- current locale:  -->
        <div class="locales instapaper_ignore readability-footer">
          <div class="site">

            <ul class="choices clearfix limited-locales">
              <li><span class="current">English</span></li>
              
                  <li><a rel="nofollow" href="?locale=de">Deutsch</a></li>
              
                  <li><a rel="nofollow" href="?locale=fr">Français</a></li>
              
                  <li><a rel="nofollow" href="?locale=ja">日本語</a></li>
              
                  <li><a rel="nofollow" href="?locale=pt-BR">Português (BR)</a></li>
              
                  <li><a rel="nofollow" href="?locale=ru">Русский</a></li>
              
                  <li><a rel="nofollow" href="?locale=zh">中文</a></li>
              
              <li class="all"><a href="#" class="minibutton btn-forward js-all-locales"><span><span class="icon"></span>See all available languages</span></a></li>
            </ul>

            <div class="all-locales clearfix">
              <h3>Your current locale selection: <strong>English</strong>. Choose another?</h3>
              
              
                <ul class="choices">
                  
                      <li><a rel="nofollow" href="?locale=en">English</a></li>
                  
                      <li><a rel="nofollow" href="?locale=af">Afrikaans</a></li>
                  
                      <li><a rel="nofollow" href="?locale=ca">Català</a></li>
                  
                      <li><a rel="nofollow" href="?locale=cs">Čeština</a></li>
                  
                      <li><a rel="nofollow" href="?locale=de">Deutsch</a></li>
                  
                </ul>
              
                <ul class="choices">
                  
                      <li><a rel="nofollow" href="?locale=es">Español</a></li>
                  
                      <li><a rel="nofollow" href="?locale=fr">Français</a></li>
                  
                      <li><a rel="nofollow" href="?locale=hr">Hrvatski</a></li>
                  
                      <li><a rel="nofollow" href="?locale=hu">Magyar</a></li>
                  
                      <li><a rel="nofollow" href="?locale=id">Indonesia</a></li>
                  
                </ul>
              
                <ul class="choices">
                  
                      <li><a rel="nofollow" href="?locale=it">Italiano</a></li>
                  
                      <li><a rel="nofollow" href="?locale=ja">日本語</a></li>
                  
                      <li><a rel="nofollow" href="?locale=nl">Nederlands</a></li>
                  
                      <li><a rel="nofollow" href="?locale=no">Norsk</a></li>
                  
                      <li><a rel="nofollow" href="?locale=pl">Polski</a></li>
                  
                </ul>
              
                <ul class="choices">
                  
                      <li><a rel="nofollow" href="?locale=pt-BR">Português (BR)</a></li>
                  
                      <li><a rel="nofollow" href="?locale=ru">Русский</a></li>
                  
                      <li><a rel="nofollow" href="?locale=sr">Српски</a></li>
                  
                      <li><a rel="nofollow" href="?locale=sv">Svenska</a></li>
                  
                      <li><a rel="nofollow" href="?locale=zh">中文</a></li>
                  
                </ul>
              
            </div>

          </div>
          <div class="fade"></div>
        </div>
      
    

    <script>window._auth_token = "953c7e1808637de776390f6e7e4c8eeb2c03e730"</script>
    

<div id="keyboard_shortcuts_pane" class="instapaper_ignore readability-extra" style="display:none">
  <h2>Keyboard Shortcuts <small><a href="#" class="js-see-all-keyboard-shortcuts">(see all)</a></small></h2>

  <div class="columns threecols">
    <div class="column first">
      <h3>Site wide shortcuts</h3>
      <dl class="keyboard-mappings">
        <dt>s</dt>
        <dd>Focus site search</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>?</dt>
        <dd>Bring up this help dialog</dd>
      </dl>
    </div><!-- /.column.first -->

    <div class="column middle" style='display:none'>
      <h3>Commit list</h3>
      <dl class="keyboard-mappings">
        <dt>j</dt>
        <dd>Move selected down</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>k</dt>
        <dd>Move selected up</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>t</dt>
        <dd>Open tree</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>p</dt>
        <dd>Open parent</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>c <em>or</em> o <em>or</em> enter</dt>
        <dd>Open commit</dd>
      </dl>
    </div><!-- /.column.first -->

    <div class="column last" style='display:none'>
      <h3>Pull request list</h3>
      <dl class="keyboard-mappings">
        <dt>j</dt>
        <dd>Move selected down</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>k</dt>
        <dd>Move selected up</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>o <em>or</em> enter</dt>
        <dd>Open issue</dd>
      </dl>
    </div><!-- /.columns.last -->

  </div><!-- /.columns.equacols -->

  <div style='display:none'>
    <div class="rule"></div>

    <h3>Issues</h3>

    <div class="columns threecols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt>j</dt>
          <dd>Move selected down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>k</dt>
          <dd>Move selected up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>x</dt>
          <dd>Toggle select target</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>o <em>or</em> enter</dt>
          <dd>Open issue</dd>
        </dl>
      </div><!-- /.column.first -->
      <div class="column middle">
        <dl class="keyboard-mappings">
          <dt>I</dt>
          <dd>Mark selected as read</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>U</dt>
          <dd>Mark selected as unread</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>e</dt>
          <dd>Close selected</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>y</dt>
          <dd>Remove selected from view</dd>
        </dl>
      </div><!-- /.column.middle -->
      <div class="column last">
        <dl class="keyboard-mappings">
          <dt>c</dt>
          <dd>Create issue</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>l</dt>
          <dd>Create label</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>i</dt>
          <dd>Back to inbox</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>u</dt>
          <dd>Back to issues</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>/</dt>
          <dd>Focus issues search</dd>
        </dl>
      </div>
    </div>
  </div>

  <div style='display:none'>
    <div class="rule"></div>

    <h3>Network Graph</h3>
    <div class="columns equacols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt><span class="badmono">←</span> <em>or</em> h</dt>
          <dd>Scroll left</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">→</span> <em>or</em> l</dt>
          <dd>Scroll right</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">↑</span> <em>or</em> k</dt>
          <dd>Scroll up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">↓</span> <em>or</em> j</dt>
          <dd>Scroll down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>t</dt>
          <dd>Toggle visibility of head labels</dd>
        </dl>
      </div><!-- /.column.first -->
      <div class="column last">
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">←</span> <em>or</em> shift h</dt>
          <dd>Scroll all the way left</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">→</span> <em>or</em> shift l</dt>
          <dd>Scroll all the way right</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">↑</span> <em>or</em> shift k</dt>
          <dd>Scroll all the way up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">↓</span> <em>or</em> shift j</dt>
          <dd>Scroll all the way down</dd>
        </dl>
      </div><!-- /.column.last -->
    </div>
  </div>

  <div >
    <div class="rule"></div>

    <h3>Source Code Browsing</h3>
    <div class="columns threecols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt>t</dt>
          <dd>Activates the file finder</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>l</dt>
          <dd>Jump to line</dd>
        </dl>
      </div>
    </div>
  </div>

</div>
    

    <!--[if IE 8]>
    <script type="text/javascript" charset="utf-8">
      $(document.body).addClass("ie8")
    </script>
    <![endif]-->

    <!--[if IE 7]>
    <script type="text/javascript" charset="utf-8">
      $(document.body).addClass("ie7")
    </script>
    <![endif]-->

    
    <script type='text/javascript'></script>
    
  </body>
</html>

Google APIs Client Library for PHP
=====================================

== Description
The Google API Client Library enables you to work with Google APIs such as Google+, Drive, Tasks, or Latitude on your server.

Requirements:
  PHP 5.2.x or higher [http://www.php.net/]
  PHP Curl extension [http://www.php.net/manual/en/intro.curl.php]
  PHP JSON extension [http://php.net/manual/en/book.json.php]

Project page:
  http://code.google.com/p/google-api-php-client

OAuth 2 instructions:
  http://code.google.com/p/google-api-php-client/wiki/OAuth2

Report a defect or feature request here:
  http://code.google.com/p/google-api-php-client/issues/entry

Subscribe to project updates in your feed reader:
  http://code.google.com/feeds/p/google-api-php-client/updates/basic

Supported sample applications:
  http://code.google.com/p/google-api-php-client/wiki/Samples

== Basic Example
  <?php
  require_once 'path/to/src/Google_Client.php';
  require_once 'path/to/src/contrib/apiBooksService.php';

  $client = new Google_Client();
  $service = new Google_BooksService($client);

  $optParams = array('filter' => 'free-ebooks');
  $results = $service->volumes->listVolumes('Henry David Thoreau', $optParams);

  foreach ($results['items'] as $item) {
    print($item['volumeInfo']['title'] . '<br>');
  }
# Pygments VIM Styles

A collection of famous VIM theme, fixed and converted to pygments CSS.
Feel free to fork and add your favorite theme using the guide below!

Included until now:

[DARK BACKGROUND]

- desert
- mustang
- no_quarter
- peaksea
- railscasts
- rdark
- slate
- wombat
- freya   (Thanks to github.com/underhilllabs)
- inkpot  (Thanks to github.com/underhilllabs)

[LIGHT BACKGROUND]

- nuvola

### Convert your VIM styles
These CSS have been generated using the following script:

- https://github.com/honza/vim2pygments
- http://honza.ca/2011/02/how-to-convert-vim-colorschemes-to-pygments-themes

### Themes
- Wombat: http://www.vim.org/scripts/script.php?script_id=1778

- Mustang: http://hcalves.deviantart.com/art/Mustang-Vim-Colorscheme-98974484

- Other VIM themes are part of the Color Sampler Pack http://www.vim.org/scripts/script.php?script_id=625 (originally from vim.sf.net )

### Example

![Screenshot](https://github.com/uraimo/pygments-vimstyles/raw/master/screen.png)
# Enhanced Text Widget

An enhanced version of the default text widget where you may have Text, HTML, CSS, JavaScript, Flash, Shortcodes and/or PHP as content with linkable widget title.

## Options

* Title
* Title URL
* Widget CSS class
* Content supports Text, HTML, CSS, JavaScript, Flash, Shortcodes, and PHP
* Option to not display a title
* Option to open Title URL in new window
* Option to automatically add paragraphs to content
* Option to not output before/after_widget/title (bare widget)

## More Information

* For help use [wordpress.org](http://wordpress.org/support/plugin/enhanced-text-widget/)
* Fork or contribute on [Github](https://github.com/bostondv/enhanced-text-widget/)
* Visit [our website](http://pomelodesign.com/) for more
* Follow me on [Twitter](http://twitter.com/bostondv/)
* View my other [WordPress Plugins](http://profiles.wordpress.org/bostondv/)

## Support

Did you enjoy this plugin? Please [donate to support ongoing development](http://pomelodesign.com/donate/). Your contribution would be greatly appreciated.

## Installation

1. Download and extract the zip archive
2. Upload `enhanced-text-widget` folder to `/wp-content/plugins/`
3. Activate the plugin through the 'Plugins' menu in WordPress
4. Add the widget to a sidebar and configure the options as desired

## Upgrade Notice

### 1.3.4
This adds option to hide the title

### 1.2
This adds option to display bare text (no before/after widget/title elements are shown).

### 1.1
This adds a CSS class parameter to each widget.

### 1.0
This is the initial release.

## Changelog ==

### 1.4.5
* Adds option to hide empty widgets

### 1.4.4
* Updates tested to 4.0
* Updates license to GPLv3
* Minor code refactoring

### 1.4.3
* Adds Italian translation

### 1.4.2
* Removes widget caching
* Fixes issue with multiline PHP code

### 1.4
* Display text field in monospace font
* Code refactoring

### 1.3.4
* This adds option to hide the title
* Tested up to 3.5.1

### 1.3.3
* Fixes "Do not output before/after_widget/title" option
* Code cleanup

### 1.3.2
* Bug fixes

### 1.3
* Fixed debug warnings
* Fixed code merge issue

### 1.2
* This adds option to display bare text (no before/after widget/title elements are shown).

### 1.1
* Adds css class parameter that wraps widget.

### 1.0
* First release.

## About

Written by Boston Dell-Vandenberg of [Pomelo Design](http://www.pomelodesign.com). Pomelo Design is a web and mobile app development agency based in Toronto, Canada.JSON Lint
=========

[![Build Status](https://secure.travis-ci.org/Seldaek/jsonlint.png)](http://travis-ci.org/Seldaek/jsonlint)

Usage
-----

```php
use Seld\JsonLint\JsonParser;

$parser = new JsonParser();
    
// returns null if it's valid json, or a ParsingException object.
$parser->lint($json);

// Call getMessage() on the exception object to get
// a well formatted error message error like this

// Parse error on line 2:
// ... "key": "value"    "numbers": [1, 2, 3]
// ----------------------^
// Expected one of: 'EOF', '}', ':', ',', ']'

// Call getDetails() on the exception to get more info.

// returns parsed json, like json_decode() does, but slower, throws
// exceptions on failure.
$parser->parse($json);
```

Installation
------------

For a quick install with Composer use:

    $ composer require seld/jsonlint

JSON Lint can easily be used within another app if you have a
[PSR-4](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-4-autoloader.md)
autoloader, or it can be installed through [Composer](https://getcomposer.org/)
for use as a CLI util.
Once installed via Composer you can run the following command to lint a json file or URL:

    $ bin/jsonlint file.json

Requirements
------------

- PHP 5.3+
- [optional] PHPUnit 3.5+ to execute the test suite (phpunit --version)

Submitting bugs and feature requests
------------------------------------

Bugs and feature request are tracked on [GitHub](https://github.com/Seldaek/jsonlint/issues)

Author
------

Jordi Boggiano - <j.boggiano@seld.be> - <http://twitter.com/seldaek>

License
-------

JSON Lint is licensed under the MIT License - see the LICENSE file for details

Acknowledgements
----------------

This library is a port of the JavaScript [jsonlint](https://github.com/zaach/jsonlint) library.
#
#    S P Y C
#      a simple php yaml class
#
# Load this README!
# >> $readme = Spyc::YAMLLoad('README');
#
--- %YAML:1.1
title: Spyc -- a Simple PHP YAML Class
version: 0.5.1
authors: [chris wanstrath (chris@ozmm.org), vlad andersen (vlad.andersen@gmail.com)]
websites: [http://www.yaml.org, http://spyc.sourceforge.net]
license: [MIT License, http://www.opensource.org/licenses/mit-license.php]
copyright: "(c) 2005-2006 Chris Wanstrath, 2006-2011 Vlad Andersen"
tested on: [php 5.2.x]

installation: >
  Copy Spyc.php to a directory you can
  access with your YAML-ready PHP script.

  That's it!

about: >
  From www.yaml.org:

  "YAML(tm) (rhymes with 'camel') is a human-friendly, cross language,
  Unicode based data serialization language designed around the common
  native data structures of agile programming languages. It is broadly
  useful for programming needs ranging from configuration files to
  Internet messaging to object persistence to data auditing. Together
  with the Unicode standard for characters, the YAML specification provides
  all the information necessary to understand YAML Version 1.1 and to
  creating programs that process YAML information.

  YAML(tm) is a balance of the following design goals:
    - YAML documents are very readable by humans.
    - YAML interacts well with scripting languages.
    - YAML uses host languages' native data structures.
    - YAML has a consistent information model.
    - YAML enables stream-based processing.
    - YAML is expressive and extensible.
    - YAML is easy to implement."

  YAML makes a lot of sense.  It's easy to use, easy to learn, and cool.
  As the lucky stiff named why once said, "YAML is a beacon of light."

  If you're new to YAML, may we suggest YAML In Five Minutes:
    - http://yaml.kwiki.org/?YamlInFiveMinutes

  If you don't have five minutes, realize that this README is a completely
  valid YAML document.  Dig in, load this or any YAML file into an array
  with Spyc and see how easy it is to translate friendly text into usable
  data.

  The purpose of Spyc is to provide a pure PHP alternative to Syck, a
  simple API for loading and dumping YAML documents, a YAML loader which
  understands a usable subset of the YAML spec, and to further spread
  the glory of YAML to the PHP masses.

  If you're at all hesitant ("usable subset of YAML?!"), navigate
  http://yaml.org/start.html.  Spyc completely understands the YAML
  document shown there, a document which has features way beyond the
  scope of what normal config files might require.  Try it for yourself,
  and then start enjoying the peace of mind YAML brings to your life.

meat and a few potatoes:
  - concept: Loading a YAML document into PHP
    brief: >
      $yaml will become an array of all the data in wicked.yaml
    code: |

      include('Spyc.php');

      $yaml = Spyc::YAMLLoad('wicked.yaml');

  - concept: Loading a YAML string into PHP
    brief: >
      $array will look like this:
        array('A YAML','document in a','string')
    code: |

      include('Spyc.php');

      $yaml  = '- A YAML\n- document in a\n- string.';
      $array = Spyc::YAMLLoad($yaml);

  - concept: Dumping a PHP array to YAML
    brief: >
      $yaml will become a string of a YAML document created from
      $array.
    code: |

      include('Spyc.php');

      $array['name']  = 'chris';
      $array['sport'] = 'curbing';

      $yaml = Spyc::YAMLDump($array);

prior art:
  - who: [Brian Ingerson, Clark Evans, Oren Ben-Kiki]
    why?: >
      The YAML spec is really a piece of work, and these guys
      did a great job on it.  A simple and elegant language like
      YAML was a long time coming and it's refreshing to know
      such able minded individuals took the task to heart and
      executed it with cunning and strength.  In addition to
      their various noteworthy contributions to YAML parsers
      and related projects, YAML.pm's README is a treasure trove
      of information for knowledge seekers.  Thanks, guys.

  - who: why the lucky stiff
    why?: >
      As the author of Syck, the code used in Ruby for the language's
      YAML class and methods, why is indirectly (directly?) responsible
      for my first exposure to YAML (as a config file in a Ruby web-app)
      and the countless hours I spent playing with this sheik new data
      format afterwards.  Syck's README is a YAML file and thus the
      inspiration for this file and, even, this very piece of software.

  - who: Steve Howell
    why?: >
      Python's YAML implementation.  PyYAML's README file is also YAML,
      so it too inspired the YAML format of this README file.

  - who: [Rasmus Lerdorf, Zeev Suraski, Andi Gutmans, et al]
    why?: >
      PHP is great at what it does best.  It's also paid a lot of my bills.
      Thanks.

bugs:
  report: >
    Please see Spyc's Sourceforge project page for information on reporting bugs.
  speed: >
    This implementation was not designed for speed.  Rather, it
    was designed for those who need a pure PHP implementation of
    a YAML parser and who are not overly concerned with performance.
    If you want speed, check out Syck.
  depth: >
    This parser is by no means a comprehensive YAML parser.  For supported
    features and future plans, check the website.
  unicode: >
    YAML is supposed to be unicode, but for now we're just using ASCII.
    PHP has crappy unicode support but who knows what the future holds.

resources:
  - http://www.yaml.org
  - http://www.yaml.org/spec/
  - http://yaml.kwiki.org/?YamlInFiveMinutes
  - http://www.whytheluckystiff.net/syck/
  - http://yaml4r.sourceforge.net/cookbook/

thanks:
  - Adam Wood
  - Daniel Ferreira
  - Aaron Jensen
  - Mike Thornton
  - Fabien Potencier
  - Mustafa Kumas
# WordPress to Jekyll Exporter

One-click WordPress plugin that converts all posts, pages, taxonomies, metadata, and settings to Markdown and YAML which can be dropped into Jekyll.

[![Build Status](https://travis-ci.org/benbalter/wordpress-to-jekyll-exporter.svg?branch=master)](https://travis-ci.org/benbalter/wordpress-to-jekyll-exporter)

View plugin in [the WordPress plugin directory](https://wordpress.org/plugins/jekyll-exporter/).

## Features

* Converts all posts, pages, and settings from WordPress for use in Jekyll
* Export what your users see, not what the database stores (runs post content through `the_content` filter prior to export, allowing third-party plugins to modify the output)
* Converts all `post_content` to Markdown Extra (using Markdownify)
* Converts all `post_meta` and fields within the `wp_posts` table to YAML front matter for parsing by Jekyll
* Generates a `_config.yml` with all settings in the `wp_options` table
* Outputs a single zip file with `_config.yml`, pages, and `_posts` folder containing `.md` files for each post in the proper Jekyll naming convention
* No settings. Just a single click.

## Usage

1. Place plugin in `/wp-content/plugins/` folder
2. Activate plugin in WordPress dashboard
3. Select `Export to Jekyll` from the `Tools` menu

## More information

See [the full documentation](https://ben.balter.com/wordpress-to-jekyll-exporter):

* [Changelog](changelog.md)
* [Command-line-usage](command-line-usage.md)
* [Custom post types](custom-post-types.md)
* [Developing locally](developing-locally.md)
* [Minimum required PHP version](required-php-version.md)
OptionsResolver Component
=========================

The OptionsResolver component is `array_replace` on steroids. It allows you to
create an options system with required options, defaults, validation (type,
value), normalization and more.

Resources
---------

  * [Documentation](https://symfony.com/doc/current/components/options_resolver.html)
  * [Contributing](https://symfony.com/doc/current/contributing/index.html)
  * [Report issues](https://github.com/symfony/symfony/issues) and
    [send Pull Requests](https://github.com/symfony/symfony/pulls)
    in the [main Symfony repository](https://github.com/symfony/symfony)
# clue/stream-filter [![Build Status](https://travis-ci.org/clue/php-stream-filter.svg?branch=master)](https://travis-ci.org/clue/php-stream-filter)

A simple and modern approach to stream filtering in PHP

**Table of contents**

* [Why?](#why)
* [Usage](#usage)
  * [append()](#append)
  * [prepend()](#prepend)
  * [fun()](#fun)
  * [remove()](#remove)
* [Install](#install)
* [Tests](#tests)
* [License](#license)

## Why?

PHP's stream filtering system is great!

It offers very powerful stream filtering options and comes with a useful set of built-in filters.
These filters can be used to easily and efficiently perform various transformations on-the-fly, such as:

* read from a gzip'ed input file,
* transcode from ISO-8859-1 (Latin1) to UTF-8,
* write to a bzip output file
* and much more.

But let's face it:
Its API is [*difficult to work with*](http://php.net/manual/en/php-user-filter.filter.php)
and its documentation is [*subpar*](http://stackoverflow.com/questions/27103269/what-is-a-bucket-brigade).
This combined means its powerful features are often neglected.

This project aims to make these features more accessible to a broader audience.
* **Lightweight, SOLID design** -
  Provides a thin abstraction that is [*just good enough*](http://en.wikipedia.org/wiki/Principle_of_good_enough)
  and does not get in your way.
  Custom filters require trivial effort.
* **Good test coverage** -
  Comes with an automated tests suite and is regularly tested in the *real world*

## Usage

This lightweight library consists only of a few simple functions.
All functions reside under the `Clue\StreamFilter` namespace.

The below examples assume you use an import statement similar to this:

```php
use Clue\StreamFilter as Filter;

Filter\append(…);
```

Alternatively, you can also refer to them with their fully-qualified name:

```php
\Clue\StreamFilter\append(…);
```

### append()

The `append($stream, $callback, $read_write = STREAM_FILTER_ALL)` function can be used to
append a filter callback to the given stream.

Each stream can have a list of filters attached.
This function appends a filter to the end of this list.

This function returns a filter resource which can be passed to [`remove()`](#remove).
If the given filter can not be added, it throws an `Exception`.

The `$stream` can be any valid stream resource, such as:

```php
$stream = fopen('demo.txt', 'w+');
```

The `$callback` should be a valid callable function which accepts an individual chunk of data
and should return the updated chunk:

```php
$filter = Filter\append($stream, function ($chunk) {
    // will be called each time you read or write a $chunk to/from the stream
    return $chunk;
});
```

As such, you can also use native PHP functions or any other `callable`:

```php
Filter\append($stream, 'strtoupper');

// will write "HELLO" to the underlying stream
fwrite($stream, 'hello');
```

If the `$callback` accepts invocation without parameters, then this signature
will be invoked once ending (flushing) the filter:

```php
Filter\append($stream, function ($chunk = null) {
    if ($chunk === null) {
        // will be called once ending the filter
        return 'end';
    }
    // will be called each time you read or write a $chunk to/from the stream
    return $chunk;
});

fclose($stream);
```

> Note: Legacy PHP versions (PHP < 5.4) do not support passing additional data
from the end signal handler if the stream is being closed.

If your callback throws an `Exception`, then the filter process will be aborted.
In order to play nice with PHP's stream handling, the `Exception` will be
transformed to a PHP warning instead:

```php
Filter\append($stream, function ($chunk) {
    throw new \RuntimeException('Unexpected chunk');
});

// raises an E_USER_WARNING with "Error invoking filter: Unexpected chunk"
fwrite($stream, 'hello');
```

The optional `$read_write` parameter can be used to only invoke the `$callback` when either writing to the stream or only when reading from the stream:

```php
Filter\append($stream, function ($chunk) {
    // will be called each time you write to the stream
    return $chunk;
}, STREAM_FILTER_WRITE);

Filter\append($stream, function ($chunk) {
    // will be called each time you read from the stream
    return $chunk;
}, STREAM_FILTER_READ);
```

> Note that once a filter has been added to stream, the stream can no longer be passed to
> [`stream_select()`](http://php.net/manual/en/function.stream-select.php)
> (and family).
>
> > Warning: stream_select(): cannot cast a filtered stream on this system in {file} on line {line}
>
> This is due to limitations of PHP's stream filter support, as it can no longer reliably
> tell when the underlying stream resource is actually ready.
> As an alternative, consider calling `stream_select()` on the unfiltered stream and
> then pass the unfiltered data through the [`fun()`](#fun) function.

### prepend()

The `prepend($stream, $callback, $read_write = STREAM_FILTER_ALL)` function can be used to
prepend a filter callback to the given stream.

Each stream can have a list of filters attached.
This function prepends a filter to the start of this list.

This function returns a filter resource which can be passed to [`remove()`](#remove).
If the given filter can not be added, it throws an `Exception`.

```php
$filter = Filter\prepend($stream, function ($chunk) {
    // will be called each time you read or write a $chunk to/from the stream
    return $chunk;
});
```

Except for the position in the list of filters, this function behaves exactly
like the [`append()`](#append) function.
For more details about its behavior, see also the [`append()`](#append) function.

### fun()

The `fun($filter, $parameters = null)` function can be used to
create a filter function which uses the given built-in `$filter`.

PHP comes with a useful set of [built-in filters](http://php.net/manual/en/filters.php).
Using `fun()` makes accessing these as easy as passing an input string to filter
and getting the filtered output string.

```php
$fun = Filter\fun('string.rot13');

assert('grfg' === $fun('test'));
assert('test' === $fun($fun('test'));
```

Please note that not all filter functions may be available depending on installed
PHP extensions and the PHP version in use.
In particular, [HHVM](http://hhvm.com/) may not offer the same filter functions
or parameters as Zend PHP.
Accessing an unknown filter function will result in a `RuntimeException`:

```php
Filter\fun('unknown'); // throws RuntimeException
```

Some filters may accept or require additional filter parameters – most
filters do not require filter parameters.
If given, the optional `$parameters` argument will be passed to the
underlying filter handler as-is.
In particular, note how *not passing* this parameter at all differs from
explicitly passing a `null` value (which many filters do not accept).
Please refer to the individual filter definition for more details.
For example, the `string.strip_tags` filter can be invoked like this:

```php
$fun = Filter\fun('string.strip_tags', '<a><b>');

$ret = $fun('<b>h<br>i</b>');
assert('<b>hi</b>' === $ret);
```

Under the hood, this function allocates a temporary memory stream, so it's
recommended to clean up the filter function after use.
Also, some filter functions (in particular the
[zlib compression filters](http://php.net/manual/en/filters.compression.php))
may use internal buffers and may emit a final data chunk on close.
The filter function can be closed by invoking without any arguments:

```php
$fun = Filter\fun('zlib.deflate');

$ret = $fun('hello') . $fun('world') . $fun();
assert('helloworld' === gzinflate($ret));
```

The filter function must not be used anymore after it has been closed.
Doing so will result in a `RuntimeException`:

```php
$fun = Filter\fun('string.rot13');
$fun();

$fun('test'); // throws RuntimeException
```

> Note: If you're using the zlib compression filters, then you should be wary
about engine inconsistencies between different PHP versions and HHVM.
These inconsistencies exist in the underlying PHP engines and there's little we
can do about this in this library.
[Our test suite](tests/) contains several test cases that exhibit these issues.
If you feel some test case is missing or outdated, we're happy to accept PRs! :)

### remove()

The `remove($filter)` function can be used to
remove a filter previously added via [`append()`](#append) or [`prepend()`](#prepend).

```php
$filter = Filter\append($stream, function () {
    // …
});
Filter\remove($filter);
```

## Install

The recommended way to install this library is [through Composer](https://getcomposer.org).
[New to Composer?](https://getcomposer.org/doc/00-intro.md)

This will install the latest supported version:

```bash
$ composer require clue/stream-filter:^1.4
```

See also the [CHANGELOG](CHANGELOG.md) for details about version upgrades.

This project aims to run on any platform and thus does not require any PHP
extensions and supports running on legacy PHP 5.3 through current PHP 7+ and
HHVM.
It's *highly recommended to use PHP 7+* for this project.
Older PHP versions may suffer from a number of inconsistencies documented above.

## Tests

To run the test suite, you first need to clone this repo and then install all
dependencies [through Composer](http://getcomposer.org):

```bash
$ composer install
```

To run the test suite, go to the project root and run:

```bash
$ php vendor/bin/phpunit
```

## License

MIT
# PHP GitHub API

[![Build Status](https://travis-ci.org/KnpLabs/php-github-api.svg?branch=master)](https://travis-ci.org/KnpLabs/php-github-api)
[![StyleCI](https://styleci.io/repos/3948501/shield?style=flat)](https://styleci.io/repos/3948501)

A simple Object Oriented wrapper for GitHub API, written with PHP5.

Uses [GitHub API v3](http://developer.github.com/v3/) & supports [GitHub API v4](http://developer.github.com/v4). The object API (v3) is very similar to the RESTful API.

## Features

* Light and fast thanks to lazy loading of API classes
* Extensively tested and documented

## Requirements

* PHP >= 5.6
* [Guzzle](https://github.com/guzzle/guzzle) library,
* (optional) PHPUnit to run tests.

## Install

Via Composer:

```bash
$ composer require knplabs/github-api php-http/guzzle6-adapter
```

Why `php-http/guzzle6-adapter`? We are decoupled from any HTTP messaging client with help by [HTTPlug](http://httplug.io/). Read about clients in our [docs](doc/customize.md).


## Using Laravel?

[Laravel GitHub](https://github.com/GrahamCampbell/Laravel-GitHub) by [Graham Campbell](https://github.com/GrahamCampbell) might interest you.

## Basic usage of `php-github-api` client

```php
<?php

// This file is generated by Composer
require_once __DIR__ . '/vendor/autoload.php';

$client = new \Github\Client();
$repositories = $client->api('user')->repositories('ornicar');
```

From `$client` object, you can access to all GitHub.

## Cache usage

This example uses the PSR6 cache pool [redis-adapter](https://github.com/php-cache/redis-adapter). See http://www.php-cache.com/ for alternatives.

```php
<?php

// This file is generated by Composer
require_once __DIR__ . '/vendor/autoload.php';

use Cache\Adapter\Redis\RedisCachePool;

$client = new \Redis();
$client->connect('127.0.0.1', 6379);
// Create a PSR6 cache pool
$pool = new RedisCachePool($client);

$client = new \Github\Client();
$client->addCache($pool);

// Do some request

// Stop using cache
$client->removeCache();
```

Using cache, the client will get cached responses if resources haven't changed since last time,
**without** reaching the `X-Rate-Limit` [imposed by github](http://developer.github.com/v3/#rate-limiting).


## Documentation

See the [`doc` directory](doc/) for more detailed documentation.

## License

`php-github-api` is licensed under the MIT License - see the LICENSE file for details

## Credits

### Sponsored by

[![KnpLabs Team](http://knplabs.com/front/images/knp-labs-logo.png)](http://knplabs.com)

### Contributors

- Thanks to [Thibault Duplessis aka. ornicar](http://github.com/ornicar) for his first version of this library.
- Thanks to [Joseph Bielawski aka. stloyd](http://github.com/stloyd) for his contributions and support.
- Thanks to [noloh](http://github.com/noloh) for his contribution on the Object API.
- Thanks to [bshaffer](http://github.com/bshaffer) for his contribution on the Repo API.
- Thanks to [Rolf van de Krol](http://github.com/rolfvandekrol) for his countless contributions.
- Thanks to [Nicolas Pastorino](http://github.com/jeanvoye) for his contribution on the Pull Request API.
- Thanks to [Edoardo Rivello](http://github.com/erivello) for his contribution on the Gists API.
- Thanks to [Miguel Piedrafita](https://github.com/m1guelpf) for his contribution to the v4 & Apps API.

Thanks to GitHub for the high quality API and documentation.
PSR Cache
=========

This repository holds all interfaces defined by
[PSR-6](http://www.php-fig.org/psr/psr-6/).

Note that this is not a Cache implementation of its own. It is merely an
interface that describes a Cache implementation. See the specification for more 
details.
PSR Http Message
================

This repository holds all interfaces/classes/traits related to
[PSR-7](http://www.php-fig.org/psr/psr-7/).

Note that this is not a HTTP message implementation of its own. It is merely an
interface that describes a HTTP message. See the specification for more details.

Usage
-----

We'll certainly need some stuff in here.# Guzzle 6 HTTP Adapter

[![Latest Version](https://img.shields.io/github/release/php-http/guzzle6-adapter.svg?style=flat-square)](https://github.com/php-http/guzzle6-adapter/releases)
[![Software License](https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square)](LICENSE)
[![Build Status](https://img.shields.io/travis/php-http/guzzle6-adapter.svg?style=flat-square)](https://travis-ci.org/php-http/guzzle6-adapter)
[![Code Coverage](https://img.shields.io/scrutinizer/coverage/g/php-http/guzzle6-adapter.svg?style=flat-square)](https://scrutinizer-ci.com/g/php-http/guzzle6-adapter)
[![Quality Score](https://img.shields.io/scrutinizer/g/php-http/guzzle6-adapter.svg?style=flat-square)](https://scrutinizer-ci.com/g/php-http/guzzle6-adapter)
[![Total Downloads](https://img.shields.io/packagist/dt/php-http/guzzle6-adapter.svg?style=flat-square)](https://packagist.org/packages/php-http/guzzle6-adapter)

**Guzzle 6 HTTP Adapter.**


## Install

Via Composer

``` bash
$ composer require php-http/guzzle6-adapter
```


## Documentation

Please see the [official documentation](http://docs.php-http.org/en/latest/clients/guzzle6-adapter.html).


## Testing

First launch the http server:

```bash
$ ./vendor/bin/http_test_server > /dev/null 2>&1 &
```

Then the test suite:

``` bash
$ composer test
```


## Contributing

Please see our [contributing guide](http://docs.php-http.org/en/latest/development/contributing.html).


## Security

If you discover any security related issues, please contact us at [security@php-http.org](mailto:security@php-http.org).


## Credits

Thanks to [David de Boer](https://github.com/ddeboer) for implementing this adapter.


## License

The MIT License (MIT). Please see [License File](LICENSE) for more information.
# HTTP Client Common

[![Latest Version](https://img.shields.io/github/release/php-http/client-common.svg?style=flat-square)](https://github.com/php-http/client-common/releases)
[![Software License](https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square)](LICENSE)
[![Build Status](https://img.shields.io/travis/php-http/client-common.svg?style=flat-square)](https://travis-ci.org/php-http/client-common)
[![Code Coverage](https://img.shields.io/scrutinizer/coverage/g/php-http/client-common.svg?style=flat-square)](https://scrutinizer-ci.com/g/php-http/client-common)
[![Quality Score](https://img.shields.io/scrutinizer/g/php-http/client-common.svg?style=flat-square)](https://scrutinizer-ci.com/g/php-http/client-common)
[![Total Downloads](https://img.shields.io/packagist/dt/php-http/client-common.svg?style=flat-square)](https://packagist.org/packages/php-http/client-common)

**Common HTTP Client implementations and tools for HTTPlug.**


## Install

Via Composer

``` bash
$ composer require php-http/client-common
```


## Usage

This package provides common tools for HTTP Clients:

- BatchClient to handle sending requests in parallel
- A convenience client with HTTP method names as class methods
- Emulator, decorator layers for sync/async clients


## Documentation

Please see the [official documentation](http://docs.php-http.org/en/latest/components/client-common.html).


## Testing

``` bash
$ composer test
```


## Contributing

Please see our [contributing guide](http://docs.php-http.org/en/latest/development/contributing.html).


## Security

If you discover any security related issues, please contact us at [security@php-http.org](mailto:security@php-http.org).


## License

The MIT License (MIT). Please see [License File](LICENSE) for more information.
# Promise

[![Latest Version](https://img.shields.io/github/release/php-http/promise.svg?style=flat-square)](https://github.com/php-http/promise/releases)
[![Software License](https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square)](LICENSE)
[![Build Status](https://img.shields.io/travis/php-http/promise.svg?style=flat-square)](https://travis-ci.org/php-http/promise)
[![Code Coverage](https://img.shields.io/scrutinizer/coverage/g/php-http/promise.svg?style=flat-square)](https://scrutinizer-ci.com/g/php-http/promise)
[![Quality Score](https://img.shields.io/scrutinizer/g/php-http/promise.svg?style=flat-square)](https://scrutinizer-ci.com/g/php-http/promise)
[![Total Downloads](https://img.shields.io/packagist/dt/php-http/promise.svg?style=flat-square)](https://packagist.org/packages/php-http/promise)

**Promise used for asynchronous HTTP requests.**

**Note:** This will eventually be removed/deprecated and replaced with the upcoming Promise PSR.


## Install

Via Composer

``` bash
$ composer require php-http/promise
```


## Documentation

Please see the [official documentation](http://docs.php-http.org).


## Testing

``` bash
$ composer test
```


## Contributing

Please see our [contributing guide](http://docs.php-http.org/en/latest/development/contributing.html).


## Security

If you discover any security related issues, please contact us at [security@httplug.io](mailto:security@httplug.io)
or [security@php-http.org](mailto:security@php-http.org).


## License

The MIT License (MIT). Please see [License File](LICENSE) for more information.
# HTTPlug Discovery

[![Latest Version](https://img.shields.io/github/release/php-http/discovery.svg?style=flat-square)](https://github.com/php-http/discovery/releases)
[![Software License](https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square)](LICENSE)
[![Build Status](https://img.shields.io/travis/php-http/discovery.svg?style=flat-square)](https://travis-ci.org/php-http/discovery)
[![Code Coverage](https://img.shields.io/scrutinizer/coverage/g/php-http/discovery.svg?style=flat-square)](https://scrutinizer-ci.com/g/php-http/discovery)
[![Quality Score](https://img.shields.io/scrutinizer/g/php-http/discovery.svg?style=flat-square)](https://scrutinizer-ci.com/g/php-http/discovery)
[![Total Downloads](https://img.shields.io/packagist/dt/php-http/discovery.svg?style=flat-square)](https://packagist.org/packages/php-http/discovery)

**Finds installed HTTPlug implementations and PSR-7 message factories.**


## Install

Via Composer

``` bash
$ composer require php-http/discovery
```


## Documentation

Please see the [official documentation](http://php-http.readthedocs.org/en/latest/discovery.html).


## Testing

``` bash
$ composer test
```


## Contributing

Please see our [contributing guide](http://docs.php-http.org/en/latest/development/contributing.html).


## Security

If you discover any security related issues, please contact us at [security@php-http.org](mailto:security@php-http.org).


## License

The MIT License (MIT). Please see [License File](LICENSE) for more information.
# HTTPlug

[![Latest Version](https://img.shields.io/github/release/php-http/httplug.svg?style=flat-square)](https://github.com/php-http/httplug/releases)
[![Software License](https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square)](LICENSE)
[![Build Status](https://img.shields.io/travis/php-http/httplug.svg?style=flat-square)](https://travis-ci.org/php-http/httplug)
[![Code Coverage](https://img.shields.io/scrutinizer/coverage/g/php-http/httplug.svg?style=flat-square)](https://scrutinizer-ci.com/g/php-http/httplug)
[![Quality Score](https://img.shields.io/scrutinizer/g/php-http/httplug.svg?style=flat-square)](https://scrutinizer-ci.com/g/php-http/httplug)
[![Total Downloads](https://img.shields.io/packagist/dt/php-http/httplug.svg?style=flat-square)](https://packagist.org/packages/php-http/httplug)

[![Slack Status](http://slack.httplug.io/badge.svg)](http://slack.httplug.io)
[![Email](https://img.shields.io/badge/email-team@httplug.io-blue.svg?style=flat-square)](mailto:team@httplug.io)

**HTTPlug, the HTTP client abstraction for PHP.**


## Install

Via Composer

``` bash
$ composer require php-http/httplug
```


## Intro

This is the contract package for HTTP Client.
Use it to create HTTP Clients which are interoperable and compatible with [PSR-7](http://www.php-fig.org/psr/psr-7/).

This library is the official successor of the [ivory http adapter](https://github.com/egeloen/ivory-http-adapter).


## Documentation

Please see the [official documentation](http://docs.php-http.org).


## Testing

``` bash
$ composer test
```


## Contributing

Please see our [contributing guide](http://docs.php-http.org/en/latest/development/contributing.html).


## Security

If you discover any security related issues, please contact us at [security@php-http.org](mailto:security@php-http.org).


## License

The MIT License (MIT). Please see [License File](LICENSE) for more information.
# HTTP Message

[![Latest Version](https://img.shields.io/github/release/php-http/message.svg?style=flat-square)](https://github.com/php-http/message/releases)
[![Software License](https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square)](LICENSE)
[![Build Status](https://img.shields.io/travis/php-http/message.svg?style=flat-square)](https://travis-ci.org/php-http/message)
[![Code Coverage](https://img.shields.io/scrutinizer/coverage/g/php-http/message.svg?style=flat-square)](https://scrutinizer-ci.com/g/php-http/message)
[![Quality Score](https://img.shields.io/scrutinizer/g/php-http/message.svg?style=flat-square)](https://scrutinizer-ci.com/g/php-http/message)
[![Total Downloads](https://img.shields.io/packagist/dt/php-http/message.svg?style=flat-square)](https://packagist.org/packages/php-http/message)

**HTTP Message related tools.**


## Install

Via Composer

``` bash
$ composer require php-http/message
```


## Intro

This package contains various PSR-7 tools which might be useful in an HTTP workflow:

- Authentication method implementations
- Various Stream encoding tools
- Message decorators
- Message factory implementations for Guzzle PSR-7 and Diactoros
- Cookie implementation
- Request matchers


## Documentation

Please see the [official documentation](http://docs.php-http.org/en/latest/message.html).


## Testing

``` bash
$ composer test
```


## Contributing

Please see our [contributing guide](http://docs.php-http.org/en/latest/development/contributing.html).

## Cretids

Thanks to [Cuzzle](https://github.com/namshi/cuzzle) for inpiration for the `CurlCommandFormatter`.

## Security

If you discover any security related issues, please contact us at [security@php-http.org](mailto:security@php-http.org).


## License

The MIT License (MIT). Please see [License File](LICENSE) for more information.
# Cache Plugin

[![Latest Version](https://img.shields.io/github/release/php-http/cache-plugin.svg?style=flat-square)](https://github.com/php-http/cache-plugin/releases)
[![Software License](https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square)](LICENSE)
[![Build Status](https://img.shields.io/travis/php-http/cache-plugin.svg?style=flat-square)](https://travis-ci.org/php-http/cache-plugin)
[![Code Coverage](https://img.shields.io/scrutinizer/coverage/g/php-http/cache-plugin.svg?style=flat-square)](https://scrutinizer-ci.com/g/php-http/cache-plugin)
[![Quality Score](https://img.shields.io/scrutinizer/g/php-http/cache-plugin.svg?style=flat-square)](https://scrutinizer-ci.com/g/php-http/cache-plugin)
[![Total Downloads](https://img.shields.io/packagist/dt/php-http/cache-plugin.svg?style=flat-square)](https://packagist.org/packages/php-http/cache-plugin)

**PSR-6 Cache plugin for HTTPlug.**


## Install

Via Composer

``` bash
$ composer require php-http/cache-plugin
```


## Documentation

Please see the [official documentation](http://docs.php-http.org/en/latest/plugins/cache.html).


## Testing

``` bash
$ composer test
```


## Contributing

Please see our [contributing guide](http://docs.php-http.org/en/latest/development/contributing.html).


## Security

If you discover any security related issues, please contact us at [security@php-http.org](mailto:security@php-http.org).


## License

The MIT License (MIT). Please see [License File](LICENSE) for more information.
# PSR-7 Message Factory

[![Latest Version](https://img.shields.io/github/release/php-http/message-factory.svg?style=flat-square)](https://github.com/php-http/message-factory/releases)
[![Software License](https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square)](LICENSE)
[![Total Downloads](https://img.shields.io/packagist/dt/php-http/message-factory.svg?style=flat-square)](https://packagist.org/packages/php-http/message-factory)

**Factory interfaces for PSR-7 HTTP Message.**


## Install

Via Composer

``` bash
$ composer require php-http/message-factory
```


## Documentation

Please see the [official documentation](http://php-http.readthedocs.org/en/latest/message-factory/).


## Contributing

Please see [CONTRIBUTING](CONTRIBUTING.md) and [CONDUCT](CONDUCT.md) for details.


## Security

If you discover any security related issues, please contact us at [security@php-http.org](mailto:security@php-http.org).


## License

The MIT License (MIT). Please see [License File](LICENSE) for more information.
# PSR-7 Message Implementation

This repository contains a full [PSR-7](http://www.php-fig.org/psr/psr-7/)
message implementation, several stream decorators, and some helpful
functionality like query string parsing.


[![Build Status](https://travis-ci.org/guzzle/psr7.svg?branch=master)](https://travis-ci.org/guzzle/psr7)


# Stream implementation

This package comes with a number of stream implementations and stream
decorators.


## AppendStream

`GuzzleHttp\Psr7\AppendStream`

Reads from multiple streams, one after the other.

```php
use GuzzleHttp\Psr7;

$a = Psr7\stream_for('abc, ');
$b = Psr7\stream_for('123.');
$composed = new Psr7\AppendStream([$a, $b]);

$composed->addStream(Psr7\stream_for(' Above all listen to me'));

echo $composed; // abc, 123. Above all listen to me.
```


## BufferStream

`GuzzleHttp\Psr7\BufferStream`

Provides a buffer stream that can be written to fill a buffer, and read
from to remove bytes from the buffer.

This stream returns a "hwm" metadata value that tells upstream consumers
what the configured high water mark of the stream is, or the maximum
preferred size of the buffer.

```php
use GuzzleHttp\Psr7;

// When more than 1024 bytes are in the buffer, it will begin returning
// false to writes. This is an indication that writers should slow down.
$buffer = new Psr7\BufferStream(1024);
```


## CachingStream

The CachingStream is used to allow seeking over previously read bytes on
non-seekable streams. This can be useful when transferring a non-seekable
entity body fails due to needing to rewind the stream (for example, resulting
from a redirect). Data that is read from the remote stream will be buffered in
a PHP temp stream so that previously read bytes are cached first in memory,
then on disk.

```php
use GuzzleHttp\Psr7;

$original = Psr7\stream_for(fopen('http://www.google.com', 'r'));
$stream = new Psr7\CachingStream($original);

$stream->read(1024);
echo $stream->tell();
// 1024

$stream->seek(0);
echo $stream->tell();
// 0
```


## DroppingStream

`GuzzleHttp\Psr7\DroppingStream`

Stream decorator that begins dropping data once the size of the underlying
stream becomes too full.

```php
use GuzzleHttp\Psr7;

// Create an empty stream
$stream = Psr7\stream_for();

// Start dropping data when the stream has more than 10 bytes
$dropping = new Psr7\DroppingStream($stream, 10);

$dropping->write('01234567890123456789');
echo $stream; // 0123456789
```


## FnStream

`GuzzleHttp\Psr7\FnStream`

Compose stream implementations based on a hash of functions.

Allows for easy testing and extension of a provided stream without needing
to create a concrete class for a simple extension point.

```php

use GuzzleHttp\Psr7;

$stream = Psr7\stream_for('hi');
$fnStream = Psr7\FnStream::decorate($stream, [
    'rewind' => function () use ($stream) {
        echo 'About to rewind - ';
        $stream->rewind();
        echo 'rewound!';
    }
]);

$fnStream->rewind();
// Outputs: About to rewind - rewound!
```


## InflateStream

`GuzzleHttp\Psr7\InflateStream`

Uses PHP's zlib.inflate filter to inflate deflate or gzipped content.

This stream decorator skips the first 10 bytes of the given stream to remove
the gzip header, converts the provided stream to a PHP stream resource,
then appends the zlib.inflate filter. The stream is then converted back
to a Guzzle stream resource to be used as a Guzzle stream.


## LazyOpenStream

`GuzzleHttp\Psr7\LazyOpenStream`

Lazily reads or writes to a file that is opened only after an IO operation
take place on the stream.

```php
use GuzzleHttp\Psr7;

$stream = new Psr7\LazyOpenStream('/path/to/file', 'r');
// The file has not yet been opened...

echo $stream->read(10);
// The file is opened and read from only when needed.
```


## LimitStream

`GuzzleHttp\Psr7\LimitStream`

LimitStream can be used to read a subset or slice of an existing stream object.
This can be useful for breaking a large file into smaller pieces to be sent in
chunks (e.g. Amazon S3's multipart upload API).

```php
use GuzzleHttp\Psr7;

$original = Psr7\stream_for(fopen('/tmp/test.txt', 'r+'));
echo $original->getSize();
// >>> 1048576

// Limit the size of the body to 1024 bytes and start reading from byte 2048
$stream = new Psr7\LimitStream($original, 1024, 2048);
echo $stream->getSize();
// >>> 1024
echo $stream->tell();
// >>> 0
```


## MultipartStream

`GuzzleHttp\Psr7\MultipartStream`

Stream that when read returns bytes for a streaming multipart or
multipart/form-data stream.


## NoSeekStream

`GuzzleHttp\Psr7\NoSeekStream`

NoSeekStream wraps a stream and does not allow seeking.

```php
use GuzzleHttp\Psr7;

$original = Psr7\stream_for('foo');
$noSeek = new Psr7\NoSeekStream($original);

echo $noSeek->read(3);
// foo
var_export($noSeek->isSeekable());
// false
$noSeek->seek(0);
var_export($noSeek->read(3));
// NULL
```


## PumpStream

`GuzzleHttp\Psr7\PumpStream`

Provides a read only stream that pumps data from a PHP callable.

When invoking the provided callable, the PumpStream will pass the amount of
data requested to read to the callable. The callable can choose to ignore
this value and return fewer or more bytes than requested. Any extra data
returned by the provided callable is buffered internally until drained using
the read() function of the PumpStream. The provided callable MUST return
false when there is no more data to read.


## Implementing stream decorators

Creating a stream decorator is very easy thanks to the
`GuzzleHttp\Psr7\StreamDecoratorTrait`. This trait provides methods that
implement `Psr\Http\Message\StreamInterface` by proxying to an underlying
stream. Just `use` the `StreamDecoratorTrait` and implement your custom
methods.

For example, let's say we wanted to call a specific function each time the last
byte is read from a stream. This could be implemented by overriding the
`read()` method.

```php
use Psr\Http\Message\StreamInterface;
use GuzzleHttp\Psr7\StreamDecoratorTrait;

class EofCallbackStream implements StreamInterface
{
    use StreamDecoratorTrait;

    private $callback;

    public function __construct(StreamInterface $stream, callable $cb)
    {
        $this->stream = $stream;
        $this->callback = $cb;
    }

    public function read($length)
    {
        $result = $this->stream->read($length);

        // Invoke the callback when EOF is hit.
        if ($this->eof()) {
            call_user_func($this->callback);
        }

        return $result;
    }
}
```

This decorator could be added to any existing stream and used like so:

```php
use GuzzleHttp\Psr7;

$original = Psr7\stream_for('foo');

$eofStream = new EofCallbackStream($original, function () {
    echo 'EOF!';
});

$eofStream->read(2);
$eofStream->read(1);
// echoes "EOF!"
$eofStream->seek(0);
$eofStream->read(3);
// echoes "EOF!"
```


## PHP StreamWrapper

You can use the `GuzzleHttp\Psr7\StreamWrapper` class if you need to use a
PSR-7 stream as a PHP stream resource.

Use the `GuzzleHttp\Psr7\StreamWrapper::getResource()` method to create a PHP
stream from a PSR-7 stream.

```php
use GuzzleHttp\Psr7\StreamWrapper;

$stream = GuzzleHttp\Psr7\stream_for('hello!');
$resource = StreamWrapper::getResource($stream);
echo fread($resource, 6); // outputs hello!
```


# Function API

There are various functions available under the `GuzzleHttp\Psr7` namespace.


## `function str`

`function str(MessageInterface $message)`

Returns the string representation of an HTTP message.

```php
$request = new GuzzleHttp\Psr7\Request('GET', 'http://example.com');
echo GuzzleHttp\Psr7\str($request);
```


## `function uri_for`

`function uri_for($uri)`

This function accepts a string or `Psr\Http\Message\UriInterface` and returns a
UriInterface for the given value. If the value is already a `UriInterface`, it
is returned as-is.

```php
$uri = GuzzleHttp\Psr7\uri_for('http://example.com');
assert($uri === GuzzleHttp\Psr7\uri_for($uri));
```


## `function stream_for`

`function stream_for($resource = '', array $options = [])`

Create a new stream based on the input type.

Options is an associative array that can contain the following keys:

* - metadata: Array of custom metadata.
* - size: Size of the stream.

This method accepts the following `$resource` types:

- `Psr\Http\Message\StreamInterface`: Returns the value as-is.
- `string`: Creates a stream object that uses the given string as the contents.
- `resource`: Creates a stream object that wraps the given PHP stream resource.
- `Iterator`: If the provided value implements `Iterator`, then a read-only
  stream object will be created that wraps the given iterable. Each time the
  stream is read from, data from the iterator will fill a buffer and will be
  continuously called until the buffer is equal to the requested read size.
  Subsequent read calls will first read from the buffer and then call `next`
  on the underlying iterator until it is exhausted.
- `object` with `__toString()`: If the object has the `__toString()` method,
  the object will be cast to a string and then a stream will be returned that
  uses the string value.
- `NULL`: When `null` is passed, an empty stream object is returned.
- `callable` When a callable is passed, a read-only stream object will be
  created that invokes the given callable. The callable is invoked with the
  number of suggested bytes to read. The callable can return any number of
  bytes, but MUST return `false` when there is no more data to return. The
  stream object that wraps the callable will invoke the callable until the
  number of requested bytes are available. Any additional bytes will be
  buffered and used in subsequent reads.

```php
$stream = GuzzleHttp\Psr7\stream_for('foo');
$stream = GuzzleHttp\Psr7\stream_for(fopen('/path/to/file', 'r'));

$generator function ($bytes) {
    for ($i = 0; $i < $bytes; $i++) {
        yield ' ';
    }
}

$stream = GuzzleHttp\Psr7\stream_for($generator(100));
```


## `function parse_header`

`function parse_header($header)`

Parse an array of header values containing ";" separated data into an array of
associative arrays representing the header key value pair data of the header.
When a parameter does not contain a value, but just contains a key, this
function will inject a key with a '' string value.


## `function normalize_header`

`function normalize_header($header)`

Converts an array of header values that may contain comma separated headers
into an array of headers with no comma separated values.


## `function modify_request`

`function modify_request(RequestInterface $request, array $changes)`

Clone and modify a request with the given changes. This method is useful for
reducing the number of clones needed to mutate a message.

The changes can be one of:

- method: (string) Changes the HTTP method.
- set_headers: (array) Sets the given headers.
- remove_headers: (array) Remove the given headers.
- body: (mixed) Sets the given body.
- uri: (UriInterface) Set the URI.
- query: (string) Set the query string value of the URI.
- version: (string) Set the protocol version.


## `function rewind_body`

`function rewind_body(MessageInterface $message)`

Attempts to rewind a message body and throws an exception on failure. The body
of the message will only be rewound if a call to `tell()` returns a value other
than `0`.


## `function try_fopen`

`function try_fopen($filename, $mode)`

Safely opens a PHP stream resource using a filename.

When fopen fails, PHP normally raises a warning. This function adds an error
handler that checks for errors and throws an exception instead.


## `function copy_to_string`

`function copy_to_string(StreamInterface $stream, $maxLen = -1)`

Copy the contents of a stream into a string until the given number of bytes
have been read.


## `function copy_to_stream`

`function copy_to_stream(StreamInterface $source, StreamInterface $dest, $maxLen = -1)`

Copy the contents of a stream into another stream until the given number of
bytes have been read.


## `function hash`

`function hash(StreamInterface $stream, $algo, $rawOutput = false)`

Calculate a hash of a Stream. This method reads the entire stream to calculate
a rolling hash (based on PHP's hash_init functions).


## `function readline`

`function readline(StreamInterface $stream, $maxLength = null)`

Read a line from the stream up to the maximum allowed buffer length.


## `function parse_request`

`function parse_request($message)`

Parses a request message string into a request object.


## `function parse_response`

`function parse_response($message)`

Parses a response message string into a response object.


## `function parse_query`

`function parse_query($str, $urlEncoding = true)`

Parse a query string into an associative array.

If multiple values are found for the same key, the value of that key value pair
will become an array. This function does not parse nested PHP style arrays into
an associative array (e.g., `foo[a]=1&foo[b]=2` will be parsed into
`['foo[a]' => '1', 'foo[b]' => '2']`).


## `function build_query`

`function build_query(array $params, $encoding = PHP_QUERY_RFC3986)`

Build a query string from an array of key value pairs.

This function can use the return value of parse_query() to build a query string.
This function does not modify the provided keys when an array is encountered
(like http_build_query would).


## `function mimetype_from_filename`

`function mimetype_from_filename($filename)`

Determines the mimetype of a file by looking at its extension.


## `function mimetype_from_extension`

`function mimetype_from_extension($extension)`

Maps a file extensions to a mimetype.


# Additional URI Methods

Aside from the standard `Psr\Http\Message\UriInterface` implementation in form of the `GuzzleHttp\Psr7\Uri` class,
this library also provides additional functionality when working with URIs as static methods.

## URI Types

An instance of `Psr\Http\Message\UriInterface` can either be an absolute URI or a relative reference.
An absolute URI has a scheme. A relative reference is used to express a URI relative to another URI,
the base URI. Relative references can be divided into several forms according to
[RFC 3986 Section 4.2](https://tools.ietf.org/html/rfc3986#section-4.2):

- network-path references, e.g. `//example.com/path`
- absolute-path references, e.g. `/path`
- relative-path references, e.g. `subpath`

The following methods can be used to identify the type of the URI.

### `GuzzleHttp\Psr7\Uri::isAbsolute`

`public static function isAbsolute(UriInterface $uri): bool`

Whether the URI is absolute, i.e. it has a scheme.

### `GuzzleHttp\Psr7\Uri::isNetworkPathReference`

`public static function isNetworkPathReference(UriInterface $uri): bool`

Whether the URI is a network-path reference. A relative reference that begins with two slash characters is
termed an network-path reference.

### `GuzzleHttp\Psr7\Uri::isAbsolutePathReference`

`public static function isAbsolutePathReference(UriInterface $uri): bool`

Whether the URI is a absolute-path reference. A relative reference that begins with a single slash character is
termed an absolute-path reference.

### `GuzzleHttp\Psr7\Uri::isRelativePathReference`

`public static function isRelativePathReference(UriInterface $uri): bool`

Whether the URI is a relative-path reference. A relative reference that does not begin with a slash character is
termed a relative-path reference.

### `GuzzleHttp\Psr7\Uri::isSameDocumentReference`

`public static function isSameDocumentReference(UriInterface $uri, UriInterface $base = null): bool`

Whether the URI is a same-document reference. A same-document reference refers to a URI that is, aside from its
fragment component, identical to the base URI. When no base URI is given, only an empty URI reference
(apart from its fragment) is considered a same-document reference.

## URI Components

Additional methods to work with URI components.

### `GuzzleHttp\Psr7\Uri::isDefaultPort`

`public static function isDefaultPort(UriInterface $uri): bool`

Whether the URI has the default port of the current scheme. `Psr\Http\Message\UriInterface::getPort` may return null
or the standard port. This method can be used independently of the implementation.

### `GuzzleHttp\Psr7\Uri::composeComponents`

`public static function composeComponents($scheme, $authority, $path, $query, $fragment): string`

Composes a URI reference string from its various components according to
[RFC 3986 Section 5.3](https://tools.ietf.org/html/rfc3986#section-5.3). Usually this method does not need to be called
manually but instead is used indirectly via `Psr\Http\Message\UriInterface::__toString`.

### `GuzzleHttp\Psr7\Uri::fromParts`

`public static function fromParts(array $parts): UriInterface`

Creates a URI from a hash of [`parse_url`](http://php.net/manual/en/function.parse-url.php) components.


### `GuzzleHttp\Psr7\Uri::withQueryValue`

`public static function withQueryValue(UriInterface $uri, $key, $value): UriInterface`

Creates a new URI with a specific query string value. Any existing query string values that exactly match the
provided key are removed and replaced with the given key value pair. A value of null will set the query string
key without a value, e.g. "key" instead of "key=value".


### `GuzzleHttp\Psr7\Uri::withoutQueryValue`

`public static function withoutQueryValue(UriInterface $uri, $key): UriInterface`

Creates a new URI with a specific query string value removed. Any existing query string values that exactly match the
provided key are removed.

## Reference Resolution

`GuzzleHttp\Psr7\UriResolver` provides methods to resolve a URI reference in the context of a base URI according
to [RFC 3986 Section 5](https://tools.ietf.org/html/rfc3986#section-5). This is for example also what web browsers
do when resolving a link in a website based on the current request URI.

### `GuzzleHttp\Psr7\UriResolver::resolve`

`public static function resolve(UriInterface $base, UriInterface $rel): UriInterface`

Converts the relative URI into a new URI that is resolved against the base URI.

### `GuzzleHttp\Psr7\UriResolver::removeDotSegments`

`public static function removeDotSegments(string $path): string`

Removes dot segments from a path and returns the new path according to
[RFC 3986 Section 5.2.4](https://tools.ietf.org/html/rfc3986#section-5.2.4).

### `GuzzleHttp\Psr7\UriResolver::relativize`

`public static function relativize(UriInterface $base, UriInterface $target): UriInterface`

Returns the target URI as a relative reference from the base URI. This method is the counterpart to resolve():

```php
(string) $target === (string) UriResolver::resolve($base, UriResolver::relativize($base, $target))
```

One use-case is to use the current request URI as base URI and then generate relative links in your documents
to reduce the document size or offer self-contained downloadable document archives.

```php
$base = new Uri('http://example.com/a/b/');
echo UriResolver::relativize($base, new Uri('http://example.com/a/b/c'));  // prints 'c'.
echo UriResolver::relativize($base, new Uri('http://example.com/a/x/y'));  // prints '../x/y'.
echo UriResolver::relativize($base, new Uri('http://example.com/a/b/?q')); // prints '?q'.
echo UriResolver::relativize($base, new Uri('http://example.org/a/b/'));   // prints '//example.org/a/b/'.
```

## Normalization and Comparison

`GuzzleHttp\Psr7\UriNormalizer` provides methods to normalize and compare URIs according to
[RFC 3986 Section 6](https://tools.ietf.org/html/rfc3986#section-6).

### `GuzzleHttp\Psr7\UriNormalizer::normalize`

`public static function normalize(UriInterface $uri, $flags = self::PRESERVING_NORMALIZATIONS): UriInterface`

Returns a normalized URI. The scheme and host component are already normalized to lowercase per PSR-7 UriInterface.
This methods adds additional normalizations that can be configured with the `$flags` parameter which is a bitmask
of normalizations to apply. The following normalizations are available:

- `UriNormalizer::PRESERVING_NORMALIZATIONS`

    Default normalizations which only include the ones that preserve semantics.

- `UriNormalizer::CAPITALIZE_PERCENT_ENCODING`

    All letters within a percent-encoding triplet (e.g., "%3A") are case-insensitive, and should be capitalized.

    Example: `http://example.org/a%c2%b1b` → `http://example.org/a%C2%B1b`

- `UriNormalizer::DECODE_UNRESERVED_CHARACTERS`

    Decodes percent-encoded octets of unreserved characters. For consistency, percent-encoded octets in the ranges of
    ALPHA (%41–%5A and %61–%7A), DIGIT (%30–%39), hyphen (%2D), period (%2E), underscore (%5F), or tilde (%7E) should
    not be created by URI producers and, when found in a URI, should be decoded to their corresponding unreserved
    characters by URI normalizers.

    Example: `http://example.org/%7Eusern%61me/` → `http://example.org/~username/`

- `UriNormalizer::CONVERT_EMPTY_PATH`

    Converts the empty path to "/" for http and https URIs.

    Example: `http://example.org` → `http://example.org/`

- `UriNormalizer::REMOVE_DEFAULT_HOST`

    Removes the default host of the given URI scheme from the URI. Only the "file" scheme defines the default host
    "localhost". All of `file:/myfile`, `file:///myfile`, and `file://localhost/myfile` are equivalent according to
    RFC 3986.

    Example: `file://localhost/myfile` → `file:///myfile`

- `UriNormalizer::REMOVE_DEFAULT_PORT`

    Removes the default port of the given URI scheme from the URI.

    Example: `http://example.org:80/` → `http://example.org/`

- `UriNormalizer::REMOVE_DOT_SEGMENTS`

    Removes unnecessary dot-segments. Dot-segments in relative-path references are not removed as it would
    change the semantics of the URI reference.

    Example: `http://example.org/../a/b/../c/./d.html` → `http://example.org/a/c/d.html`

- `UriNormalizer::REMOVE_DUPLICATE_SLASHES`

    Paths which include two or more adjacent slashes are converted to one. Webservers usually ignore duplicate slashes
    and treat those URIs equivalent. But in theory those URIs do not need to be equivalent. So this normalization
    may change the semantics. Encoded slashes (%2F) are not removed.

    Example: `http://example.org//foo///bar.html` → `http://example.org/foo/bar.html`

- `UriNormalizer::SORT_QUERY_PARAMETERS`

    Sort query parameters with their values in alphabetical order. However, the order of parameters in a URI may be
    significant (this is not defined by the standard). So this normalization is not safe and may change the semantics
    of the URI.

    Example: `?lang=en&article=fred` → `?article=fred&lang=en`

### `GuzzleHttp\Psr7\UriNormalizer::isEquivalent`

`public static function isEquivalent(UriInterface $uri1, UriInterface $uri2, $normalizations = self::PRESERVING_NORMALIZATIONS): bool`

Whether two URIs can be considered equivalent. Both URIs are normalized automatically before comparison with the given
`$normalizations` bitmask. The method also accepts relative URI references and returns true when they are equivalent.
This of course assumes they will be resolved against the same base URI. If this is not the case, determination of
equivalence or difference of relative references does not mean anything.
Guzzle, PHP HTTP client
=======================

[![Build Status](https://travis-ci.org/guzzle/guzzle.svg?branch=master)](https://travis-ci.org/guzzle/guzzle)

Guzzle is a PHP HTTP client that makes it easy to send HTTP requests and
trivial to integrate with web services.

- Simple interface for building query strings, POST requests, streaming large
  uploads, streaming large downloads, using HTTP cookies, uploading JSON data,
  etc...
- Can send both synchronous and asynchronous requests using the same interface.
- Uses PSR-7 interfaces for requests, responses, and streams. This allows you
  to utilize other PSR-7 compatible libraries with Guzzle.
- Abstracts away the underlying HTTP transport, allowing you to write
  environment and transport agnostic code; i.e., no hard dependency on cURL,
  PHP streams, sockets, or non-blocking event loops.
- Middleware system allows you to augment and compose client behavior.

```php
$client = new \GuzzleHttp\Client();
$res = $client->request('GET', 'https://api.github.com/repos/guzzle/guzzle');
echo $res->getStatusCode();
// 200
echo $res->getHeaderLine('content-type');
// 'application/json; charset=utf8'
echo $res->getBody();
// '{"id": 1420053, "name": "guzzle", ...}'

// Send an asynchronous request.
$request = new \GuzzleHttp\Psr7\Request('GET', 'http://httpbin.org');
$promise = $client->sendAsync($request)->then(function ($response) {
    echo 'I completed! ' . $response->getBody();
});
$promise->wait();
```

## Help and docs

- [Documentation](http://guzzlephp.org/)
- [Stack Overflow](http://stackoverflow.com/questions/tagged/guzzle)
- [Gitter](https://gitter.im/guzzle/guzzle)


## Installing Guzzle

The recommended way to install Guzzle is through
[Composer](http://getcomposer.org).

```bash
# Install Composer
curl -sS https://getcomposer.org/installer | php
```

Next, run the Composer command to install the latest stable version of Guzzle:

```bash
php composer.phar require guzzlehttp/guzzle
```

After installing, you need to require Composer's autoloader:

```php
require 'vendor/autoload.php';
```

You can then later update Guzzle using composer:

 ```bash
composer.phar update
 ```


## Version Guidance

| Version | Status     | Packagist           | Namespace    | Repo                | Docs                | PSR-7 | PHP Version |
|---------|------------|---------------------|--------------|---------------------|---------------------|-------|-------------|
| 3.x     | EOL        | `guzzle/guzzle`     | `Guzzle`     | [v3][guzzle-3-repo] | [v3][guzzle-3-docs] | No    | >= 5.3.3    |
| 4.x     | EOL        | `guzzlehttp/guzzle` | `GuzzleHttp` | [v4][guzzle-4-repo] | N/A                 | No    | >= 5.4      |
| 5.x     | Maintained | `guzzlehttp/guzzle` | `GuzzleHttp` | [v5][guzzle-5-repo] | [v5][guzzle-5-docs] | No    | >= 5.4      |
| 6.x     | Latest     | `guzzlehttp/guzzle` | `GuzzleHttp` | [v6][guzzle-6-repo] | [v6][guzzle-6-docs] | Yes   | >= 5.5      |

[guzzle-3-repo]: https://github.com/guzzle/guzzle3
[guzzle-4-repo]: https://github.com/guzzle/guzzle/tree/4.x
[guzzle-5-repo]: https://github.com/guzzle/guzzle/tree/5.3
[guzzle-6-repo]: https://github.com/guzzle/guzzle
[guzzle-3-docs]: http://guzzle3.readthedocs.org/en/latest/
[guzzle-5-docs]: http://guzzle.readthedocs.org/en/5.3/
[guzzle-6-docs]: http://guzzle.readthedocs.org/en/latest/
# Guzzle Promises

[Promises/A+](https://promisesaplus.com/) implementation that handles promise
chaining and resolution iteratively, allowing for "infinite" promise chaining
while keeping the stack size constant. Read [this blog post](https://blog.domenic.me/youre-missing-the-point-of-promises/)
for a general introduction to promises.

- [Features](#features)
- [Quick start](#quick-start)
- [Synchronous wait](#synchronous-wait)
- [Cancellation](#cancellation)
- [API](#api)
  - [Promise](#promise)
  - [FulfilledPromise](#fulfilledpromise)
  - [RejectedPromise](#rejectedpromise)
- [Promise interop](#promise-interop)
- [Implementation notes](#implementation-notes)


# Features

- [Promises/A+](https://promisesaplus.com/) implementation.
- Promise resolution and chaining is handled iteratively, allowing for
  "infinite" promise chaining.
- Promises have a synchronous `wait` method.
- Promises can be cancelled.
- Works with any object that has a `then` function.
- C# style async/await coroutine promises using
  `GuzzleHttp\Promise\coroutine()`.


# Quick start

A *promise* represents the eventual result of an asynchronous operation. The
primary way of interacting with a promise is through its `then` method, which
registers callbacks to receive either a promise's eventual value or the reason
why the promise cannot be fulfilled.


## Callbacks

Callbacks are registered with the `then` method by providing an optional 
`$onFulfilled` followed by an optional `$onRejected` function.


```php
use GuzzleHttp\Promise\Promise;

$promise = new Promise();
$promise->then(
    // $onFulfilled
    function ($value) {
        echo 'The promise was fulfilled.';
    },
    // $onRejected
    function ($reason) {
        echo 'The promise was rejected.';
    }
);
```

*Resolving* a promise means that you either fulfill a promise with a *value* or
reject a promise with a *reason*. Resolving a promises triggers callbacks
registered with the promises's `then` method. These callbacks are triggered
only once and in the order in which they were added.


## Resolving a promise

Promises are fulfilled using the `resolve($value)` method. Resolving a promise
with any value other than a `GuzzleHttp\Promise\RejectedPromise` will trigger
all of the onFulfilled callbacks (resolving a promise with a rejected promise
will reject the promise and trigger the `$onRejected` callbacks).

```php
use GuzzleHttp\Promise\Promise;

$promise = new Promise();
$promise
    ->then(function ($value) {
        // Return a value and don't break the chain
        return "Hello, " . $value;
    })
    // This then is executed after the first then and receives the value
    // returned from the first then.
    ->then(function ($value) {
        echo $value;
    });

// Resolving the promise triggers the $onFulfilled callbacks and outputs
// "Hello, reader".
$promise->resolve('reader.');
```


## Promise forwarding

Promises can be chained one after the other. Each then in the chain is a new
promise. The return value of a promise is what's forwarded to the next
promise in the chain. Returning a promise in a `then` callback will cause the
subsequent promises in the chain to only be fulfilled when the returned promise
has been fulfilled. The next promise in the chain will be invoked with the
resolved value of the promise.

```php
use GuzzleHttp\Promise\Promise;

$promise = new Promise();
$nextPromise = new Promise();

$promise
    ->then(function ($value) use ($nextPromise) {
        echo $value;
        return $nextPromise;
    })
    ->then(function ($value) {
        echo $value;
    });

// Triggers the first callback and outputs "A"
$promise->resolve('A');
// Triggers the second callback and outputs "B"
$nextPromise->resolve('B');
```

## Promise rejection

When a promise is rejected, the `$onRejected` callbacks are invoked with the
rejection reason.

```php
use GuzzleHttp\Promise\Promise;

$promise = new Promise();
$promise->then(null, function ($reason) {
    echo $reason;
});

$promise->reject('Error!');
// Outputs "Error!"
```

## Rejection forwarding

If an exception is thrown in an `$onRejected` callback, subsequent
`$onRejected` callbacks are invoked with the thrown exception as the reason.

```php
use GuzzleHttp\Promise\Promise;

$promise = new Promise();
$promise->then(null, function ($reason) {
    throw new \Exception($reason);
})->then(null, function ($reason) {
    assert($reason->getMessage() === 'Error!');
});

$promise->reject('Error!');
```

You can also forward a rejection down the promise chain by returning a
`GuzzleHttp\Promise\RejectedPromise` in either an `$onFulfilled` or
`$onRejected` callback.

```php
use GuzzleHttp\Promise\Promise;
use GuzzleHttp\Promise\RejectedPromise;

$promise = new Promise();
$promise->then(null, function ($reason) {
    return new RejectedPromise($reason);
})->then(null, function ($reason) {
    assert($reason === 'Error!');
});

$promise->reject('Error!');
```

If an exception is not thrown in a `$onRejected` callback and the callback
does not return a rejected promise, downstream `$onFulfilled` callbacks are
invoked using the value returned from the `$onRejected` callback.

```php
use GuzzleHttp\Promise\Promise;
use GuzzleHttp\Promise\RejectedPromise;

$promise = new Promise();
$promise
    ->then(null, function ($reason) {
        return "It's ok";
    })
    ->then(function ($value) {
        assert($value === "It's ok");
    });

$promise->reject('Error!');
```

# Synchronous wait

You can synchronously force promises to complete using a promise's `wait`
method. When creating a promise, you can provide a wait function that is used
to synchronously force a promise to complete. When a wait function is invoked
it is expected to deliver a value to the promise or reject the promise. If the
wait function does not deliver a value, then an exception is thrown. The wait
function provided to a promise constructor is invoked when the `wait` function
of the promise is called.

```php
$promise = new Promise(function () use (&$promise) {
    $promise->resolve('foo');
});

// Calling wait will return the value of the promise.
echo $promise->wait(); // outputs "foo"
```

If an exception is encountered while invoking the wait function of a promise,
the promise is rejected with the exception and the exception is thrown.

```php
$promise = new Promise(function () use (&$promise) {
    throw new \Exception('foo');
});

$promise->wait(); // throws the exception.
```

Calling `wait` on a promise that has been fulfilled will not trigger the wait
function. It will simply return the previously resolved value.

```php
$promise = new Promise(function () { die('this is not called!'); });
$promise->resolve('foo');
echo $promise->wait(); // outputs "foo"
```

Calling `wait` on a promise that has been rejected will throw an exception. If
the rejection reason is an instance of `\Exception` the reason is thrown.
Otherwise, a `GuzzleHttp\Promise\RejectionException` is thrown and the reason
can be obtained by calling the `getReason` method of the exception.

```php
$promise = new Promise();
$promise->reject('foo');
$promise->wait();
```

> PHP Fatal error:  Uncaught exception 'GuzzleHttp\Promise\RejectionException' with message 'The promise was rejected with value: foo'


## Unwrapping a promise

When synchronously waiting on a promise, you are joining the state of the
promise into the current state of execution (i.e., return the value of the
promise if it was fulfilled or throw an exception if it was rejected). This is
called "unwrapping" the promise. Waiting on a promise will by default unwrap
the promise state.

You can force a promise to resolve and *not* unwrap the state of the promise
by passing `false` to the first argument of the `wait` function:

```php
$promise = new Promise();
$promise->reject('foo');
// This will not throw an exception. It simply ensures the promise has
// been resolved.
$promise->wait(false);
```

When unwrapping a promise, the resolved value of the promise will be waited
upon until the unwrapped value is not a promise. This means that if you resolve
promise A with a promise B and unwrap promise A, the value returned by the
wait function will be the value delivered to promise B.

**Note**: when you do not unwrap the promise, no value is returned.


# Cancellation

You can cancel a promise that has not yet been fulfilled using the `cancel()`
method of a promise. When creating a promise you can provide an optional
cancel function that when invoked cancels the action of computing a resolution
of the promise.


# API


## Promise

When creating a promise object, you can provide an optional `$waitFn` and
`$cancelFn`. `$waitFn` is a function that is invoked with no arguments and is
expected to resolve the promise. `$cancelFn` is a function with no arguments
that is expected to cancel the computation of a promise. It is invoked when the
`cancel()` method of a promise is called.

```php
use GuzzleHttp\Promise\Promise;

$promise = new Promise(
    function () use (&$promise) {
        $promise->resolve('waited');
    },
    function () {
        // do something that will cancel the promise computation (e.g., close
        // a socket, cancel a database query, etc...)
    }
);

assert('waited' === $promise->wait());
```

A promise has the following methods:

- `then(callable $onFulfilled, callable $onRejected) : PromiseInterface`
  
  Appends fulfillment and rejection handlers to the promise, and returns a new promise resolving to the return value of the called handler.

- `otherwise(callable $onRejected) : PromiseInterface`
  
  Appends a rejection handler callback to the promise, and returns a new promise resolving to the return value of the callback if it is called, or to its original fulfillment value if the promise is instead fulfilled.

- `wait($unwrap = true) : mixed`

  Synchronously waits on the promise to complete.
  
  `$unwrap` controls whether or not the value of the promise is returned for a
  fulfilled promise or if an exception is thrown if the promise is rejected.
  This is set to `true` by default.

- `cancel()`

  Attempts to cancel the promise if possible. The promise being cancelled and
  the parent most ancestor that has not yet been resolved will also be
  cancelled. Any promises waiting on the cancelled promise to resolve will also
  be cancelled.

- `getState() : string`

  Returns the state of the promise. One of `pending`, `fulfilled`, or
  `rejected`.

- `resolve($value)`

  Fulfills the promise with the given `$value`.

- `reject($reason)`

  Rejects the promise with the given `$reason`.


## FulfilledPromise

A fulfilled promise can be created to represent a promise that has been
fulfilled.

```php
use GuzzleHttp\Promise\FulfilledPromise;

$promise = new FulfilledPromise('value');

// Fulfilled callbacks are immediately invoked.
$promise->then(function ($value) {
    echo $value;
});
```


## RejectedPromise

A rejected promise can be created to represent a promise that has been
rejected.

```php
use GuzzleHttp\Promise\RejectedPromise;

$promise = new RejectedPromise('Error');

// Rejected callbacks are immediately invoked.
$promise->then(null, function ($reason) {
    echo $reason;
});
```


# Promise interop

This library works with foreign promises that have a `then` method. This means
you can use Guzzle promises with [React promises](https://github.com/reactphp/promise)
for example. When a foreign promise is returned inside of a then method
callback, promise resolution will occur recursively.

```php
// Create a React promise
$deferred = new React\Promise\Deferred();
$reactPromise = $deferred->promise();

// Create a Guzzle promise that is fulfilled with a React promise.
$guzzlePromise = new \GuzzleHttp\Promise\Promise();
$guzzlePromise->then(function ($value) use ($reactPromise) {
    // Do something something with the value...
    // Return the React promise
    return $reactPromise;
});
```

Please note that wait and cancel chaining is no longer possible when forwarding
a foreign promise. You will need to wrap a third-party promise with a Guzzle
promise in order to utilize wait and cancel functions with foreign promises.


## Event Loop Integration

In order to keep the stack size constant, Guzzle promises are resolved
asynchronously using a task queue. When waiting on promises synchronously, the
task queue will be automatically run to ensure that the blocking promise and
any forwarded promises are resolved. When using promises asynchronously in an
event loop, you will need to run the task queue on each tick of the loop. If
you do not run the task queue, then promises will not be resolved.

You can run the task queue using the `run()` method of the global task queue
instance.

```php
// Get the global task queue
$queue = \GuzzleHttp\Promise\queue();
$queue->run();
```

For example, you could use Guzzle promises with React using a periodic timer:

```php
$loop = React\EventLoop\Factory::create();
$loop->addPeriodicTimer(0, [$queue, 'run']);
```

*TODO*: Perhaps adding a `futureTick()` on each tick would be faster?


# Implementation notes


## Promise resolution and chaining is handled iteratively

By shuffling pending handlers from one owner to another, promises are
resolved iteratively, allowing for "infinite" then chaining.

```php
<?php
require 'vendor/autoload.php';

use GuzzleHttp\Promise\Promise;

$parent = new Promise();
$p = $parent;

for ($i = 0; $i < 1000; $i++) {
    $p = $p->then(function ($v) {
        // The stack size remains constant (a good thing)
        echo xdebug_get_stack_depth() . ', ';
        return $v + 1;
    });
}

$parent->resolve(0);
var_dump($p->wait()); // int(1000)

```

When a promise is fulfilled or rejected with a non-promise value, the promise
then takes ownership of the handlers of each child promise and delivers values
down the chain without using recursion.

When a promise is resolved with another promise, the original promise transfers
all of its pending handlers to the new promise. When the new promise is
eventually resolved, all of the pending handlers are delivered the forwarded
value.


## A promise is the deferred.

Some promise libraries implement promises using a deferred object to represent
a computation and a promise object to represent the delivery of the result of
the computation. This is a nice separation of computation and delivery because
consumers of the promise cannot modify the value that will be eventually
delivered.

One side effect of being able to implement promise resolution and chaining
iteratively is that you need to be able for one promise to reach into the state
of another promise to shuffle around ownership of handlers. In order to achieve
this without making the handlers of a promise publicly mutable, a promise is
also the deferred value, allowing promises of the same parent class to reach
into and modify the private properties of promises of the same type. While this
does allow consumers of the value to modify the resolution or rejection of the
deferred, it is a small price to pay for keeping the stack size constant.

```php
$promise = new Promise();
$promise->then(function ($value) { echo $value; });
// The promise is the deferred value, so you can deliver a value to it.
$promise->resolve('foo');
// prints "foo"
```
# AWS SDK for PHP

[![@awsforphp on Twitter](http://img.shields.io/badge/twitter-%40awsforphp-blue.svg?style=flat)](https://twitter.com/awsforphp)
[![Total Downloads](https://img.shields.io/packagist/dt/aws/aws-sdk-php.svg?style=flat)](https://packagist.org/packages/aws/aws-sdk-php)
[![Build Status](https://img.shields.io/travis/aws/aws-sdk-php.svg?style=flat)](https://travis-ci.org/aws/aws-sdk-php)
[![Apache 2 License](https://img.shields.io/packagist/l/aws/aws-sdk-php.svg?style=flat)](http://aws.amazon.com/apache-2-0/)
[![Code Climate](https://codeclimate.com/github/aws/aws-sdk-php/badges/gpa.svg)](https://codeclimate.com/github/aws/aws-sdk-php)
[![Gitter](https://badges.gitter.im/Join Chat.svg)](https://gitter.im/aws/aws-sdk-php?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

The **AWS SDK for PHP** enables PHP developers to use [Amazon Web Services][aws]
in their PHP code, and build robust applications and software using services
like Amazon S3, Amazon DynamoDB, Amazon Glacier, etc. You can get started in
minutes by [installing the SDK through Composer][docs-installation] or by
downloading a single zip or phar file from our [latest release][latest-release].

## Resources

* [User Guide][docs-guide] – For in-depth getting started and usage information
* [API Docs][docs-api] – For operations, parameters, responses, and examples
* [Blog][sdk-blog] – Tips & tricks, articles, and announcements
* [Sample Project][sdk-sample] - A quick, sample project to help get you started
* [Forum][sdk-forum] – Ask questions, get help, and give feedback
* [Issues][sdk-issues] – Report issues and submit pull requests
  (see [Apache 2.0 License][sdk-license])
* [@awsforphp][sdk-twitter] – Follow us on Twitter
* [Building Apps with Version 3 of the AWS SDK for PHP](http://youtu.be/STrtR89f5Pc) video from AWS
  re:Invent 2014

## Features

* Provides easy-to-use HTTP clients for all supported AWS
  [services][docs-services], [regions][docs-rande], and authentication
  protocols.
* Is built for PHP 5.3.3+ and is compliant with [PSR-0], [PSR-1], and [PSR-2].
* Is easy to install through [Composer][install-packagist], or by downloading
  the phar or zip file of our [latest release][latest-release].
* Is built on [Guzzle v3][guzzle], and utilizes many of its features, including
  persistent connections, parallel requests, events and plugins
  (via [Symfony2 EventDispatcher][symfony2-events]), service descriptions,
  [over-the-wire logging][docs-wire-logging], caching, flexible batching, and
  request retrying with truncated exponential backoff.
* Provides convenience features including easy response pagination via
  [Iterators][docs-iterators], resource [Waiters][docs-waiters], and simple
  [modelled responses][docs-models].
* Allows you to [sync local directories to Amazon S3 buckets][docs-s3-sync].
* Provides a [multipart uploader tool][docs-s3-multipart] for Amazon S3 and
  Amazon Glacier that can be paused and resumed.
* Provides an [Amazon S3 Stream Wrapper][docs-streamwrapper], so that you can
  use PHP's native file handling functions to interact with your S3 buckets and
  objects like a local filesystem.
* Provides the [Amazon DynamoDB Session Handler][docs-ddbsh] for easily scaling
  sessions on a fast, NoSQL database.
* Automatically uses [IAM Instance Profile Credentials][aws-iam-credentials] on
  configured Amazon EC2 instances.

## Getting Started

1. **Sign up for AWS** – Before you begin, you need to
   [sign up for an AWS account][docs-signup] and retrieve your AWS credentials.
1. **Minimum requirements** – To run the SDK, your system will need to meet the
   [minimum requirements][docs-requirements], including having **PHP 5.3.3+**
   compiled with the cURL extension and cURL 7.16.2+ compiled with OpenSSL and
   zlib.
1. **Install the SDK** – Using [Composer] is the recommended way to install the
   AWS SDK for PHP. The SDK is available via [Packagist] under the
   [`aws/aws-sdk-php`][install-packagist] package. Please see the
   [Installation section of the User Guide][docs-installation] for more
   detailed information about installing the SDK through Composer and other
   means.
1. **Using the SDK** – The best way to become familiar with how to use the SDK
   is to read the [User Guide][docs-guide]. The
   [Getting Started Guide][docs-quickstart] will help you become familiar with
   the basic concepts, and there are also specific guides for each of the
   [supported services][docs-services].

## Quick Example

### Upload a File to Amazon S3

```php
<?php
require 'vendor/autoload.php';

use Aws\S3\S3Client;
use Aws\S3\Exception\S3Exception;

// Instantiate an S3 client
$s3 = S3Client::factory();

// Upload a publicly accessible file. The file size, file type, and MD5 hash
// are automatically calculated by the SDK.
try {
    $s3->putObject(array(
        'Bucket' => 'my-bucket',
        'Key'    => 'my-object',
        'Body'   => fopen('/path/to/file', 'r'),
        'ACL'    => 'public-read',
    ));
} catch (S3Exception $e) {
    echo "There was an error uploading the file.\n";
}
```

You can also use the even easier `upload()` method, which will automatically do
either single or multipart uploads, as needed.

```php
try {
    $resource = fopen('/path/to/file', 'r');
    $s3->upload('my-bucket', 'my-object', $resource, 'public-read');
} catch (S3Exception $e) {
    echo "There was an error uploading the file.\n";
}
```

### More Examples

* [Get an object from Amazon S3 and save it to a file][example-s3-getobject]
* [Upload a large file to Amazon S3 in parts][example-s3-multipart]
* [Put an item in your Amazon DynamoDB table][example-dynamodb-putitem]
* [Send a message to your Amazon SQS queue][example-sqs-sendmessage]
* Please browse the [User Guide][docs-guide] and [API docs][docs-api] or check
  out our [AWS SDK Development Blog][sdk-blog] for even more examples and
  tutorials.

### Related Projects

* [AWS Service Provider for Laravel][mod-laravel]
* [AWS SDK ZF2 Module][mod-zf2]
* [AWS Service Provider for Silex][mod-silex]
* [Guzzle v3][guzzle-docs] – PHP HTTP client and framework
* Other [AWS SDKs & Tools][aws-tools] (e.g., js, cli, ruby, python, java, etc.)

[sdk-website]: http://aws.amazon.com/sdkforphp
[sdk-forum]: https://forums.aws.amazon.com/forum.jspa?forumID=80
[sdk-issues]: https://github.com/aws/aws-sdk-php/issues
[sdk-license]: http://aws.amazon.com/apache2.0/
[sdk-blog]: http://blogs.aws.amazon.com/php
[sdk-twitter]: https://twitter.com/awsforphp
[sdk-sample]: http://aws.amazon.com/developers/getting-started/php

[install-packagist]: https://packagist.org/packages/aws/aws-sdk-php
[latest-release]: https://github.com/aws/aws-sdk-php/releases/latest

[docs-api]: http://docs.aws.amazon.com/aws-sdk-php/v2/api/index.html
[docs-guide]: http://docs.aws.amazon.com/aws-sdk-php/v2/guide/index.html
[docs-contribution]: https://github.com/aws/aws-sdk-php/blob/master/CONTRIBUTING.md
[docs-performance]: http://docs.aws.amazon.com/aws-sdk-php/v2/guide/performance.html
[docs-migration]: http://docs.aws.amazon.com/aws-sdk-php/v2/guide/migration-guide.html
[docs-signup]: http://docs.aws.amazon.com/aws-sdk-php/v2/guide/awssignup.html
[docs-requirements]: http://docs.aws.amazon.com/aws-sdk-php/v2/guide/requirements.html
[docs-installation]: http://docs.aws.amazon.com/aws-sdk-php/v2/guide/installation.html
[docs-quickstart]: http://docs.aws.amazon.com/aws-sdk-php/v2/guide/quick-start.html
[docs-iterators]: http://docs.aws.amazon.com/aws-sdk-php/v2/guide/quick-start.html#iterators
[docs-waiters]: http://docs.aws.amazon.com/aws-sdk-php/v2/guide/feature-waiters.html
[docs-models]: http://docs.aws.amazon.com/aws-sdk-php/v2/guide/feature-models.html
[docs-exceptions]: http://docs.aws.amazon.com/aws-sdk-php/v2/guide/quick-start.html#error-handling
[docs-wire-logging]: http://docs.aws.amazon.com/aws-sdk-php/v2/guide/faq.html#how-can-i-see-what-data-is-sent-over-the-wire
[docs-services]: http://docs.aws.amazon.com/aws-sdk-php/v2/guide/index.html#supported-services
[docs-ddbsh]: http://docs.aws.amazon.com/aws-sdk-php/v2/guide/feature-dynamodb-session-handler.html
[docs-rande]: http://docs.aws.amazon.com/general/latest/gr/rande.html
[docs-streamwrapper]: http://docs.aws.amazon.com/aws-sdk-php/v2/guide/service-s3.html#amazon-s3-stream-wrapper
[docs-s3-sync]: http://blogs.aws.amazon.com/php/post/Tx2W9JAA7RXVOXA/Syncing-Data-with-Amazon-S3
[docs-s3-multipart]: http://docs.aws.amazon.com/aws-sdk-php/v2/guide/service-s3.html#uploading-large-files-using-multipart-uploads

[aws]: http://aws.amazon.com
[aws-iam-credentials]: http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UsingIAM.html#UsingIAMrolesWithAmazonEC2Instances
[aws-tools]: http://aws.amazon.com/tools
[guzzle]: https://github.com/guzzle/guzzle3
[guzzle-docs]: https://guzzle3.readthedocs.org
[composer]: http://getcomposer.org
[packagist]: http://packagist.org
[psr-0]: https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-0.md
[psr-1]: https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-1-basic-coding-standard.md
[psr-2]: https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-2-coding-style-guide.md
[symfony2-events]: http://symfony.com/doc/2.3/components/event_dispatcher/introduction.html

[example-sqs-sendmessage]: http://docs.aws.amazon.com/aws-sdk-php/v2/guide/service-sqs.html#sending-messages
[example-s3-getobject]: http://docs.aws.amazon.com/aws-sdk-php/v2/guide/service-s3.html#saving-objects-to-a-file
[example-s3-multipart]: http://docs.aws.amazon.com/aws-sdk-php/v2/guide/service-s3.html#uploading-large-files-using-multipart-uploads
[example-dynamodb-putitem]: http://docs.aws.amazon.com/aws-sdk-php/v2/guide/service-dynamodb.html#adding-items

[mod-laravel]: https://github.com/aws/aws-sdk-php-laravel
[mod-zf2]: https://github.com/aws/aws-sdk-php-zf2
[mod-silex]: https://github.com/aws/aws-sdk-php-silex
Dropbox SDK v2 for PHP
======================================================
[![Latest Stable Version](https://poser.pugx.org/kunalvarma05/dropbox-php-sdk/v/stable?format=flat-square)](https://packagist.org/packages/kunalvarma05/dropbox-php-sdk)
[![Build Status](https://img.shields.io/travis/kunalvarma05/dropbox-php-sdk.svg?style=flat-square)](https://travis-ci.org/kunalvarma05/dropbox-php-sdk)
[![Quality Score](https://img.shields.io/scrutinizer/g/kunalvarma05/dropbox-php-sdk.svg?style=flat-square)](https://scrutinizer-ci.com/g/kunalvarma05/dropbox-php-sdk)
[![Total Downloads](https://img.shields.io/packagist/dt/kunalvarma05/dropbox-php-sdk.svg?style=flat-square)](https://packagist.org/packages/kunalvarma05/dropbox-php-sdk)
[![StyleCI](https://styleci.io/repos/61913555/shield?branch=master)](https://styleci.io/repos/61913555)
[![License](https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square)](https://packagist.org/packages/kunalvarma05/dropbox-php-sdk)


An unofficial PHP SDK to work with the [Dropbox API v2](https://www.dropbox.com/developers/documentation/http/documentation).

<img src="https://cloud.githubusercontent.com/assets/893057/13731118/b7cf0e4e-e987-11e5-942f-13c53d65da35.png">


## Get Started
Head over to the [**Getting Started**](https://github.com/kunalvarma05/dropbox-php-sdk/wiki/Getting-Started) Wiki section to Install and Get started.


## API Docs
[**View API Docs**](https://kunalvarma05.github.io/dropbox-php-sdk/)


## License
Dropbox PHP Client is licensed under The MIT License (MIT).
PSR Http Message
================

This repository holds all interfaces/classes/traits related to
[PSR-7](http://www.php-fig.org/psr/psr-7/).

Note that this is not a HTTP message implementation of its own. It is merely an
interface that describes a HTTP message. See the specification for more details.

Usage
-----

We'll certainly need some stuff in here.# PSR-7 Message Implementation

This repository contains a full [PSR-7](http://www.php-fig.org/psr/psr-7/)
message implementation, several stream decorators, and some helpful
functionality like query string parsing.


[![Build Status](https://travis-ci.org/guzzle/psr7.svg?branch=master)](https://travis-ci.org/guzzle/psr7)


# Stream implementation

This package comes with a number of stream implementations and stream
decorators.


## AppendStream

`GuzzleHttp\Psr7\AppendStream`

Reads from multiple streams, one after the other.

```php
use GuzzleHttp\Psr7;

$a = Psr7\stream_for('abc, ');
$b = Psr7\stream_for('123.');
$composed = new Psr7\AppendStream([$a, $b]);

$composed->addStream(Psr7\stream_for(' Above all listen to me'));

echo $composed; // abc, 123. Above all listen to me.
```


## BufferStream

`GuzzleHttp\Psr7\BufferStream`

Provides a buffer stream that can be written to fill a buffer, and read
from to remove bytes from the buffer.

This stream returns a "hwm" metadata value that tells upstream consumers
what the configured high water mark of the stream is, or the maximum
preferred size of the buffer.

```php
use GuzzleHttp\Psr7;

// When more than 1024 bytes are in the buffer, it will begin returning
// false to writes. This is an indication that writers should slow down.
$buffer = new Psr7\BufferStream(1024);
```


## CachingStream

The CachingStream is used to allow seeking over previously read bytes on
non-seekable streams. This can be useful when transferring a non-seekable
entity body fails due to needing to rewind the stream (for example, resulting
from a redirect). Data that is read from the remote stream will be buffered in
a PHP temp stream so that previously read bytes are cached first in memory,
then on disk.

```php
use GuzzleHttp\Psr7;

$original = Psr7\stream_for(fopen('http://www.google.com', 'r'));
$stream = new Psr7\CachingStream($original);

$stream->read(1024);
echo $stream->tell();
// 1024

$stream->seek(0);
echo $stream->tell();
// 0
```


## DroppingStream

`GuzzleHttp\Psr7\DroppingStream`

Stream decorator that begins dropping data once the size of the underlying
stream becomes too full.

```php
use GuzzleHttp\Psr7;

// Create an empty stream
$stream = Psr7\stream_for();

// Start dropping data when the stream has more than 10 bytes
$dropping = new Psr7\DroppingStream($stream, 10);

$dropping->write('01234567890123456789');
echo $stream; // 0123456789
```


## FnStream

`GuzzleHttp\Psr7\FnStream`

Compose stream implementations based on a hash of functions.

Allows for easy testing and extension of a provided stream without needing
to create a concrete class for a simple extension point.

```php

use GuzzleHttp\Psr7;

$stream = Psr7\stream_for('hi');
$fnStream = Psr7\FnStream::decorate($stream, [
    'rewind' => function () use ($stream) {
        echo 'About to rewind - ';
        $stream->rewind();
        echo 'rewound!';
    }
]);

$fnStream->rewind();
// Outputs: About to rewind - rewound!
```


## InflateStream

`GuzzleHttp\Psr7\InflateStream`

Uses PHP's zlib.inflate filter to inflate deflate or gzipped content.

This stream decorator skips the first 10 bytes of the given stream to remove
the gzip header, converts the provided stream to a PHP stream resource,
then appends the zlib.inflate filter. The stream is then converted back
to a Guzzle stream resource to be used as a Guzzle stream.


## LazyOpenStream

`GuzzleHttp\Psr7\LazyOpenStream`

Lazily reads or writes to a file that is opened only after an IO operation
take place on the stream.

```php
use GuzzleHttp\Psr7;

$stream = new Psr7\LazyOpenStream('/path/to/file', 'r');
// The file has not yet been opened...

echo $stream->read(10);
// The file is opened and read from only when needed.
```


## LimitStream

`GuzzleHttp\Psr7\LimitStream`

LimitStream can be used to read a subset or slice of an existing stream object.
This can be useful for breaking a large file into smaller pieces to be sent in
chunks (e.g. Amazon S3's multipart upload API).

```php
use GuzzleHttp\Psr7;

$original = Psr7\stream_for(fopen('/tmp/test.txt', 'r+'));
echo $original->getSize();
// >>> 1048576

// Limit the size of the body to 1024 bytes and start reading from byte 2048
$stream = new Psr7\LimitStream($original, 1024, 2048);
echo $stream->getSize();
// >>> 1024
echo $stream->tell();
// >>> 0
```


## MultipartStream

`GuzzleHttp\Psr7\MultipartStream`

Stream that when read returns bytes for a streaming multipart or
multipart/form-data stream.


## NoSeekStream

`GuzzleHttp\Psr7\NoSeekStream`

NoSeekStream wraps a stream and does not allow seeking.

```php
use GuzzleHttp\Psr7;

$original = Psr7\stream_for('foo');
$noSeek = new Psr7\NoSeekStream($original);

echo $noSeek->read(3);
// foo
var_export($noSeek->isSeekable());
// false
$noSeek->seek(0);
var_export($noSeek->read(3));
// NULL
```


## PumpStream

`GuzzleHttp\Psr7\PumpStream`

Provides a read only stream that pumps data from a PHP callable.

When invoking the provided callable, the PumpStream will pass the amount of
data requested to read to the callable. The callable can choose to ignore
this value and return fewer or more bytes than requested. Any extra data
returned by the provided callable is buffered internally until drained using
the read() function of the PumpStream. The provided callable MUST return
false when there is no more data to read.


## Implementing stream decorators

Creating a stream decorator is very easy thanks to the
`GuzzleHttp\Psr7\StreamDecoratorTrait`. This trait provides methods that
implement `Psr\Http\Message\StreamInterface` by proxying to an underlying
stream. Just `use` the `StreamDecoratorTrait` and implement your custom
methods.

For example, let's say we wanted to call a specific function each time the last
byte is read from a stream. This could be implemented by overriding the
`read()` method.

```php
use Psr\Http\Message\StreamInterface;
use GuzzleHttp\Psr7\StreamDecoratorTrait;

class EofCallbackStream implements StreamInterface
{
    use StreamDecoratorTrait;

    private $callback;

    public function __construct(StreamInterface $stream, callable $cb)
    {
        $this->stream = $stream;
        $this->callback = $cb;
    }

    public function read($length)
    {
        $result = $this->stream->read($length);

        // Invoke the callback when EOF is hit.
        if ($this->eof()) {
            call_user_func($this->callback);
        }

        return $result;
    }
}
```

This decorator could be added to any existing stream and used like so:

```php
use GuzzleHttp\Psr7;

$original = Psr7\stream_for('foo');

$eofStream = new EofCallbackStream($original, function () {
    echo 'EOF!';
});

$eofStream->read(2);
$eofStream->read(1);
// echoes "EOF!"
$eofStream->seek(0);
$eofStream->read(3);
// echoes "EOF!"
```


## PHP StreamWrapper

You can use the `GuzzleHttp\Psr7\StreamWrapper` class if you need to use a
PSR-7 stream as a PHP stream resource.

Use the `GuzzleHttp\Psr7\StreamWrapper::getResource()` method to create a PHP
stream from a PSR-7 stream.

```php
use GuzzleHttp\Psr7\StreamWrapper;

$stream = GuzzleHttp\Psr7\stream_for('hello!');
$resource = StreamWrapper::getResource($stream);
echo fread($resource, 6); // outputs hello!
```


# Function API

There are various functions available under the `GuzzleHttp\Psr7` namespace.


## `function str`

`function str(MessageInterface $message)`

Returns the string representation of an HTTP message.

```php
$request = new GuzzleHttp\Psr7\Request('GET', 'http://example.com');
echo GuzzleHttp\Psr7\str($request);
```


## `function uri_for`

`function uri_for($uri)`

This function accepts a string or `Psr\Http\Message\UriInterface` and returns a
UriInterface for the given value. If the value is already a `UriInterface`, it
is returned as-is.

```php
$uri = GuzzleHttp\Psr7\uri_for('http://example.com');
assert($uri === GuzzleHttp\Psr7\uri_for($uri));
```


## `function stream_for`

`function stream_for($resource = '', array $options = [])`

Create a new stream based on the input type.

Options is an associative array that can contain the following keys:

* - metadata: Array of custom metadata.
* - size: Size of the stream.

This method accepts the following `$resource` types:

- `Psr\Http\Message\StreamInterface`: Returns the value as-is.
- `string`: Creates a stream object that uses the given string as the contents.
- `resource`: Creates a stream object that wraps the given PHP stream resource.
- `Iterator`: If the provided value implements `Iterator`, then a read-only
  stream object will be created that wraps the given iterable. Each time the
  stream is read from, data from the iterator will fill a buffer and will be
  continuously called until the buffer is equal to the requested read size.
  Subsequent read calls will first read from the buffer and then call `next`
  on the underlying iterator until it is exhausted.
- `object` with `__toString()`: If the object has the `__toString()` method,
  the object will be cast to a string and then a stream will be returned that
  uses the string value.
- `NULL`: When `null` is passed, an empty stream object is returned.
- `callable` When a callable is passed, a read-only stream object will be
  created that invokes the given callable. The callable is invoked with the
  number of suggested bytes to read. The callable can return any number of
  bytes, but MUST return `false` when there is no more data to return. The
  stream object that wraps the callable will invoke the callable until the
  number of requested bytes are available. Any additional bytes will be
  buffered and used in subsequent reads.

```php
$stream = GuzzleHttp\Psr7\stream_for('foo');
$stream = GuzzleHttp\Psr7\stream_for(fopen('/path/to/file', 'r'));

$generator function ($bytes) {
    for ($i = 0; $i < $bytes; $i++) {
        yield ' ';
    }
}

$stream = GuzzleHttp\Psr7\stream_for($generator(100));
```


## `function parse_header`

`function parse_header($header)`

Parse an array of header values containing ";" separated data into an array of
associative arrays representing the header key value pair data of the header.
When a parameter does not contain a value, but just contains a key, this
function will inject a key with a '' string value.


## `function normalize_header`

`function normalize_header($header)`

Converts an array of header values that may contain comma separated headers
into an array of headers with no comma separated values.


## `function modify_request`

`function modify_request(RequestInterface $request, array $changes)`

Clone and modify a request with the given changes. This method is useful for
reducing the number of clones needed to mutate a message.

The changes can be one of:

- method: (string) Changes the HTTP method.
- set_headers: (array) Sets the given headers.
- remove_headers: (array) Remove the given headers.
- body: (mixed) Sets the given body.
- uri: (UriInterface) Set the URI.
- query: (string) Set the query string value of the URI.
- version: (string) Set the protocol version.


## `function rewind_body`

`function rewind_body(MessageInterface $message)`

Attempts to rewind a message body and throws an exception on failure. The body
of the message will only be rewound if a call to `tell()` returns a value other
than `0`.


## `function try_fopen`

`function try_fopen($filename, $mode)`

Safely opens a PHP stream resource using a filename.

When fopen fails, PHP normally raises a warning. This function adds an error
handler that checks for errors and throws an exception instead.


## `function copy_to_string`

`function copy_to_string(StreamInterface $stream, $maxLen = -1)`

Copy the contents of a stream into a string until the given number of bytes
have been read.


## `function copy_to_stream`

`function copy_to_stream(StreamInterface $source, StreamInterface $dest, $maxLen = -1)`

Copy the contents of a stream into another stream until the given number of
bytes have been read.


## `function hash`

`function hash(StreamInterface $stream, $algo, $rawOutput = false)`

Calculate a hash of a Stream. This method reads the entire stream to calculate
a rolling hash (based on PHP's hash_init functions).


## `function readline`

`function readline(StreamInterface $stream, $maxLength = null)`

Read a line from the stream up to the maximum allowed buffer length.


## `function parse_request`

`function parse_request($message)`

Parses a request message string into a request object.


## `function parse_response`

`function parse_response($message)`

Parses a response message string into a response object.


## `function parse_query`

`function parse_query($str, $urlEncoding = true)`

Parse a query string into an associative array.

If multiple values are found for the same key, the value of that key value pair
will become an array. This function does not parse nested PHP style arrays into
an associative array (e.g., `foo[a]=1&foo[b]=2` will be parsed into
`['foo[a]' => '1', 'foo[b]' => '2']`).


## `function build_query`

`function build_query(array $params, $encoding = PHP_QUERY_RFC3986)`

Build a query string from an array of key value pairs.

This function can use the return value of parse_query() to build a query string.
This function does not modify the provided keys when an array is encountered
(like http_build_query would).


## `function mimetype_from_filename`

`function mimetype_from_filename($filename)`

Determines the mimetype of a file by looking at its extension.


## `function mimetype_from_extension`

`function mimetype_from_extension($extension)`

Maps a file extensions to a mimetype.


# Additional URI Methods

Aside from the standard `Psr\Http\Message\UriInterface` implementation in form of the `GuzzleHttp\Psr7\Uri` class,
this library also provides additional functionality when working with URIs as static methods.

## URI Types

An instance of `Psr\Http\Message\UriInterface` can either be an absolute URI or a relative reference.
An absolute URI has a scheme. A relative reference is used to express a URI relative to another URI,
the base URI. Relative references can be divided into several forms according to
[RFC 3986 Section 4.2](https://tools.ietf.org/html/rfc3986#section-4.2):

- network-path references, e.g. `//example.com/path`
- absolute-path references, e.g. `/path`
- relative-path references, e.g. `subpath`

The following methods can be used to identify the type of the URI.

### `GuzzleHttp\Psr7\Uri::isAbsolute`

`public static function isAbsolute(UriInterface $uri): bool`

Whether the URI is absolute, i.e. it has a scheme.

### `GuzzleHttp\Psr7\Uri::isNetworkPathReference`

`public static function isNetworkPathReference(UriInterface $uri): bool`

Whether the URI is a network-path reference. A relative reference that begins with two slash characters is
termed an network-path reference.

### `GuzzleHttp\Psr7\Uri::isAbsolutePathReference`

`public static function isAbsolutePathReference(UriInterface $uri): bool`

Whether the URI is a absolute-path reference. A relative reference that begins with a single slash character is
termed an absolute-path reference.

### `GuzzleHttp\Psr7\Uri::isRelativePathReference`

`public static function isRelativePathReference(UriInterface $uri): bool`

Whether the URI is a relative-path reference. A relative reference that does not begin with a slash character is
termed a relative-path reference.

### `GuzzleHttp\Psr7\Uri::isSameDocumentReference`

`public static function isSameDocumentReference(UriInterface $uri, UriInterface $base = null): bool`

Whether the URI is a same-document reference. A same-document reference refers to a URI that is, aside from its
fragment component, identical to the base URI. When no base URI is given, only an empty URI reference
(apart from its fragment) is considered a same-document reference.

## URI Components

Additional methods to work with URI components.

### `GuzzleHttp\Psr7\Uri::isDefaultPort`

`public static function isDefaultPort(UriInterface $uri): bool`

Whether the URI has the default port of the current scheme. `Psr\Http\Message\UriInterface::getPort` may return null
or the standard port. This method can be used independently of the implementation.

### `GuzzleHttp\Psr7\Uri::composeComponents`

`public static function composeComponents($scheme, $authority, $path, $query, $fragment): string`

Composes a URI reference string from its various components according to
[RFC 3986 Section 5.3](https://tools.ietf.org/html/rfc3986#section-5.3). Usually this method does not need to be called
manually but instead is used indirectly via `Psr\Http\Message\UriInterface::__toString`.

### `GuzzleHttp\Psr7\Uri::fromParts`

`public static function fromParts(array $parts): UriInterface`

Creates a URI from a hash of [`parse_url`](http://php.net/manual/en/function.parse-url.php) components.


### `GuzzleHttp\Psr7\Uri::withQueryValue`

`public static function withQueryValue(UriInterface $uri, $key, $value): UriInterface`

Creates a new URI with a specific query string value. Any existing query string values that exactly match the
provided key are removed and replaced with the given key value pair. A value of null will set the query string
key without a value, e.g. "key" instead of "key=value".


### `GuzzleHttp\Psr7\Uri::withoutQueryValue`

`public static function withoutQueryValue(UriInterface $uri, $key): UriInterface`

Creates a new URI with a specific query string value removed. Any existing query string values that exactly match the
provided key are removed.

## Reference Resolution

`GuzzleHttp\Psr7\UriResolver` provides methods to resolve a URI reference in the context of a base URI according
to [RFC 3986 Section 5](https://tools.ietf.org/html/rfc3986#section-5). This is for example also what web browsers
do when resolving a link in a website based on the current request URI.

### `GuzzleHttp\Psr7\UriResolver::resolve`

`public static function resolve(UriInterface $base, UriInterface $rel): UriInterface`

Converts the relative URI into a new URI that is resolved against the base URI.

### `GuzzleHttp\Psr7\UriResolver::removeDotSegments`

`public static function removeDotSegments(string $path): string`

Removes dot segments from a path and returns the new path according to
[RFC 3986 Section 5.2.4](https://tools.ietf.org/html/rfc3986#section-5.2.4).

### `GuzzleHttp\Psr7\UriResolver::relativize`

`public static function relativize(UriInterface $base, UriInterface $target): UriInterface`

Returns the target URI as a relative reference from the base URI. This method is the counterpart to resolve():

```php
(string) $target === (string) UriResolver::resolve($base, UriResolver::relativize($base, $target))
```

One use-case is to use the current request URI as base URI and then generate relative links in your documents
to reduce the document size or offer self-contained downloadable document archives.

```php
$base = new Uri('http://example.com/a/b/');
echo UriResolver::relativize($base, new Uri('http://example.com/a/b/c'));  // prints 'c'.
echo UriResolver::relativize($base, new Uri('http://example.com/a/x/y'));  // prints '../x/y'.
echo UriResolver::relativize($base, new Uri('http://example.com/a/b/?q')); // prints '?q'.
echo UriResolver::relativize($base, new Uri('http://example.org/a/b/'));   // prints '//example.org/a/b/'.
```

## Normalization and Comparison

`GuzzleHttp\Psr7\UriNormalizer` provides methods to normalize and compare URIs according to
[RFC 3986 Section 6](https://tools.ietf.org/html/rfc3986#section-6).

### `GuzzleHttp\Psr7\UriNormalizer::normalize`

`public static function normalize(UriInterface $uri, $flags = self::PRESERVING_NORMALIZATIONS): UriInterface`

Returns a normalized URI. The scheme and host component are already normalized to lowercase per PSR-7 UriInterface.
This methods adds additional normalizations that can be configured with the `$flags` parameter which is a bitmask
of normalizations to apply. The following normalizations are available:

- `UriNormalizer::PRESERVING_NORMALIZATIONS`

    Default normalizations which only include the ones that preserve semantics.

- `UriNormalizer::CAPITALIZE_PERCENT_ENCODING`

    All letters within a percent-encoding triplet (e.g., "%3A") are case-insensitive, and should be capitalized.

    Example: `http://example.org/a%c2%b1b` → `http://example.org/a%C2%B1b`

- `UriNormalizer::DECODE_UNRESERVED_CHARACTERS`

    Decodes percent-encoded octets of unreserved characters. For consistency, percent-encoded octets in the ranges of
    ALPHA (%41–%5A and %61–%7A), DIGIT (%30–%39), hyphen (%2D), period (%2E), underscore (%5F), or tilde (%7E) should
    not be created by URI producers and, when found in a URI, should be decoded to their corresponding unreserved
    characters by URI normalizers.

    Example: `http://example.org/%7Eusern%61me/` → `http://example.org/~username/`

- `UriNormalizer::CONVERT_EMPTY_PATH`

    Converts the empty path to "/" for http and https URIs.

    Example: `http://example.org` → `http://example.org/`

- `UriNormalizer::REMOVE_DEFAULT_HOST`

    Removes the default host of the given URI scheme from the URI. Only the "file" scheme defines the default host
    "localhost". All of `file:/myfile`, `file:///myfile`, and `file://localhost/myfile` are equivalent according to
    RFC 3986.

    Example: `file://localhost/myfile` → `file:///myfile`

- `UriNormalizer::REMOVE_DEFAULT_PORT`

    Removes the default port of the given URI scheme from the URI.

    Example: `http://example.org:80/` → `http://example.org/`

- `UriNormalizer::REMOVE_DOT_SEGMENTS`

    Removes unnecessary dot-segments. Dot-segments in relative-path references are not removed as it would
    change the semantics of the URI reference.

    Example: `http://example.org/../a/b/../c/./d.html` → `http://example.org/a/c/d.html`

- `UriNormalizer::REMOVE_DUPLICATE_SLASHES`

    Paths which include two or more adjacent slashes are converted to one. Webservers usually ignore duplicate slashes
    and treat those URIs equivalent. But in theory those URIs do not need to be equivalent. So this normalization
    may change the semantics. Encoded slashes (%2F) are not removed.

    Example: `http://example.org//foo///bar.html` → `http://example.org/foo/bar.html`

- `UriNormalizer::SORT_QUERY_PARAMETERS`

    Sort query parameters with their values in alphabetical order. However, the order of parameters in a URI may be
    significant (this is not defined by the standard). So this normalization is not safe and may change the semantics
    of the URI.

    Example: `?lang=en&article=fred` → `?article=fred&lang=en`

### `GuzzleHttp\Psr7\UriNormalizer::isEquivalent`

`public static function isEquivalent(UriInterface $uri1, UriInterface $uri2, $normalizations = self::PRESERVING_NORMALIZATIONS): bool`

Whether two URIs can be considered equivalent. Both URIs are normalized automatically before comparison with the given
`$normalizations` bitmask. The method also accepts relative URI references and returns true when they are equivalent.
This of course assumes they will be resolved against the same base URI. If this is not the case, determination of
equivalence or difference of relative references does not mean anything.
Guzzle, PHP HTTP client
=======================

[![Build Status](https://travis-ci.org/guzzle/guzzle.svg?branch=master)](https://travis-ci.org/guzzle/guzzle)

Guzzle is a PHP HTTP client that makes it easy to send HTTP requests and
trivial to integrate with web services.

- Simple interface for building query strings, POST requests, streaming large
  uploads, streaming large downloads, using HTTP cookies, uploading JSON data,
  etc...
- Can send both synchronous and asynchronous requests using the same interface.
- Uses PSR-7 interfaces for requests, responses, and streams. This allows you
  to utilize other PSR-7 compatible libraries with Guzzle.
- Abstracts away the underlying HTTP transport, allowing you to write
  environment and transport agnostic code; i.e., no hard dependency on cURL,
  PHP streams, sockets, or non-blocking event loops.
- Middleware system allows you to augment and compose client behavior.

```php
$client = new \GuzzleHttp\Client();
$res = $client->request('GET', 'https://api.github.com/repos/guzzle/guzzle');
echo $res->getStatusCode();
// 200
echo $res->getHeaderLine('content-type');
// 'application/json; charset=utf8'
echo $res->getBody();
// '{"id": 1420053, "name": "guzzle", ...}'

// Send an asynchronous request.
$request = new \GuzzleHttp\Psr7\Request('GET', 'http://httpbin.org');
$promise = $client->sendAsync($request)->then(function ($response) {
    echo 'I completed! ' . $response->getBody();
});
$promise->wait();
```

## Help and docs

- [Documentation](http://guzzlephp.org/)
- [Stack Overflow](http://stackoverflow.com/questions/tagged/guzzle)
- [Gitter](https://gitter.im/guzzle/guzzle)


## Installing Guzzle

The recommended way to install Guzzle is through
[Composer](http://getcomposer.org).

```bash
# Install Composer
curl -sS https://getcomposer.org/installer | php
```

Next, run the Composer command to install the latest stable version of Guzzle:

```bash
php composer.phar require guzzlehttp/guzzle
```

After installing, you need to require Composer's autoloader:

```php
require 'vendor/autoload.php';
```

You can then later update Guzzle using composer:

 ```bash
composer.phar update
 ```


## Version Guidance

| Version | Status     | Packagist           | Namespace    | Repo                | Docs                | PSR-7 | PHP Version |
|---------|------------|---------------------|--------------|---------------------|---------------------|-------|-------------|
| 3.x     | EOL        | `guzzle/guzzle`     | `Guzzle`     | [v3][guzzle-3-repo] | [v3][guzzle-3-docs] | No    | >= 5.3.3    |
| 4.x     | EOL        | `guzzlehttp/guzzle` | `GuzzleHttp` | [v4][guzzle-4-repo] | N/A                 | No    | >= 5.4      |
| 5.x     | Maintained | `guzzlehttp/guzzle` | `GuzzleHttp` | [v5][guzzle-5-repo] | [v5][guzzle-5-docs] | No    | >= 5.4      |
| 6.x     | Latest     | `guzzlehttp/guzzle` | `GuzzleHttp` | [v6][guzzle-6-repo] | [v6][guzzle-6-docs] | Yes   | >= 5.5      |

[guzzle-3-repo]: https://github.com/guzzle/guzzle3
[guzzle-4-repo]: https://github.com/guzzle/guzzle/tree/4.x
[guzzle-5-repo]: https://github.com/guzzle/guzzle/tree/5.3
[guzzle-6-repo]: https://github.com/guzzle/guzzle
[guzzle-3-docs]: http://guzzle3.readthedocs.org/en/latest/
[guzzle-5-docs]: http://guzzle.readthedocs.org/en/5.3/
[guzzle-6-docs]: http://guzzle.readthedocs.org/en/latest/
# Guzzle Promises

[Promises/A+](https://promisesaplus.com/) implementation that handles promise
chaining and resolution iteratively, allowing for "infinite" promise chaining
while keeping the stack size constant. Read [this blog post](https://blog.domenic.me/youre-missing-the-point-of-promises/)
for a general introduction to promises.

- [Features](#features)
- [Quick start](#quick-start)
- [Synchronous wait](#synchronous-wait)
- [Cancellation](#cancellation)
- [API](#api)
  - [Promise](#promise)
  - [FulfilledPromise](#fulfilledpromise)
  - [RejectedPromise](#rejectedpromise)
- [Promise interop](#promise-interop)
- [Implementation notes](#implementation-notes)


# Features

- [Promises/A+](https://promisesaplus.com/) implementation.
- Promise resolution and chaining is handled iteratively, allowing for
  "infinite" promise chaining.
- Promises have a synchronous `wait` method.
- Promises can be cancelled.
- Works with any object that has a `then` function.
- C# style async/await coroutine promises using
  `GuzzleHttp\Promise\coroutine()`.


# Quick start

A *promise* represents the eventual result of an asynchronous operation. The
primary way of interacting with a promise is through its `then` method, which
registers callbacks to receive either a promise's eventual value or the reason
why the promise cannot be fulfilled.


## Callbacks

Callbacks are registered with the `then` method by providing an optional 
`$onFulfilled` followed by an optional `$onRejected` function.


```php
use GuzzleHttp\Promise\Promise;

$promise = new Promise();
$promise->then(
    // $onFulfilled
    function ($value) {
        echo 'The promise was fulfilled.';
    },
    // $onRejected
    function ($reason) {
        echo 'The promise was rejected.';
    }
);
```

*Resolving* a promise means that you either fulfill a promise with a *value* or
reject a promise with a *reason*. Resolving a promises triggers callbacks
registered with the promises's `then` method. These callbacks are triggered
only once and in the order in which they were added.


## Resolving a promise

Promises are fulfilled using the `resolve($value)` method. Resolving a promise
with any value other than a `GuzzleHttp\Promise\RejectedPromise` will trigger
all of the onFulfilled callbacks (resolving a promise with a rejected promise
will reject the promise and trigger the `$onRejected` callbacks).

```php
use GuzzleHttp\Promise\Promise;

$promise = new Promise();
$promise
    ->then(function ($value) {
        // Return a value and don't break the chain
        return "Hello, " . $value;
    })
    // This then is executed after the first then and receives the value
    // returned from the first then.
    ->then(function ($value) {
        echo $value;
    });

// Resolving the promise triggers the $onFulfilled callbacks and outputs
// "Hello, reader".
$promise->resolve('reader.');
```


## Promise forwarding

Promises can be chained one after the other. Each then in the chain is a new
promise. The return value of a promise is what's forwarded to the next
promise in the chain. Returning a promise in a `then` callback will cause the
subsequent promises in the chain to only be fulfilled when the returned promise
has been fulfilled. The next promise in the chain will be invoked with the
resolved value of the promise.

```php
use GuzzleHttp\Promise\Promise;

$promise = new Promise();
$nextPromise = new Promise();

$promise
    ->then(function ($value) use ($nextPromise) {
        echo $value;
        return $nextPromise;
    })
    ->then(function ($value) {
        echo $value;
    });

// Triggers the first callback and outputs "A"
$promise->resolve('A');
// Triggers the second callback and outputs "B"
$nextPromise->resolve('B');
```

## Promise rejection

When a promise is rejected, the `$onRejected` callbacks are invoked with the
rejection reason.

```php
use GuzzleHttp\Promise\Promise;

$promise = new Promise();
$promise->then(null, function ($reason) {
    echo $reason;
});

$promise->reject('Error!');
// Outputs "Error!"
```

## Rejection forwarding

If an exception is thrown in an `$onRejected` callback, subsequent
`$onRejected` callbacks are invoked with the thrown exception as the reason.

```php
use GuzzleHttp\Promise\Promise;

$promise = new Promise();
$promise->then(null, function ($reason) {
    throw new \Exception($reason);
})->then(null, function ($reason) {
    assert($reason->getMessage() === 'Error!');
});

$promise->reject('Error!');
```

You can also forward a rejection down the promise chain by returning a
`GuzzleHttp\Promise\RejectedPromise` in either an `$onFulfilled` or
`$onRejected` callback.

```php
use GuzzleHttp\Promise\Promise;
use GuzzleHttp\Promise\RejectedPromise;

$promise = new Promise();
$promise->then(null, function ($reason) {
    return new RejectedPromise($reason);
})->then(null, function ($reason) {
    assert($reason === 'Error!');
});

$promise->reject('Error!');
```

If an exception is not thrown in a `$onRejected` callback and the callback
does not return a rejected promise, downstream `$onFulfilled` callbacks are
invoked using the value returned from the `$onRejected` callback.

```php
use GuzzleHttp\Promise\Promise;
use GuzzleHttp\Promise\RejectedPromise;

$promise = new Promise();
$promise
    ->then(null, function ($reason) {
        return "It's ok";
    })
    ->then(function ($value) {
        assert($value === "It's ok");
    });

$promise->reject('Error!');
```

# Synchronous wait

You can synchronously force promises to complete using a promise's `wait`
method. When creating a promise, you can provide a wait function that is used
to synchronously force a promise to complete. When a wait function is invoked
it is expected to deliver a value to the promise or reject the promise. If the
wait function does not deliver a value, then an exception is thrown. The wait
function provided to a promise constructor is invoked when the `wait` function
of the promise is called.

```php
$promise = new Promise(function () use (&$promise) {
    $promise->resolve('foo');
});

// Calling wait will return the value of the promise.
echo $promise->wait(); // outputs "foo"
```

If an exception is encountered while invoking the wait function of a promise,
the promise is rejected with the exception and the exception is thrown.

```php
$promise = new Promise(function () use (&$promise) {
    throw new \Exception('foo');
});

$promise->wait(); // throws the exception.
```

Calling `wait` on a promise that has been fulfilled will not trigger the wait
function. It will simply return the previously resolved value.

```php
$promise = new Promise(function () { die('this is not called!'); });
$promise->resolve('foo');
echo $promise->wait(); // outputs "foo"
```

Calling `wait` on a promise that has been rejected will throw an exception. If
the rejection reason is an instance of `\Exception` the reason is thrown.
Otherwise, a `GuzzleHttp\Promise\RejectionException` is thrown and the reason
can be obtained by calling the `getReason` method of the exception.

```php
$promise = new Promise();
$promise->reject('foo');
$promise->wait();
```

> PHP Fatal error:  Uncaught exception 'GuzzleHttp\Promise\RejectionException' with message 'The promise was rejected with value: foo'


## Unwrapping a promise

When synchronously waiting on a promise, you are joining the state of the
promise into the current state of execution (i.e., return the value of the
promise if it was fulfilled or throw an exception if it was rejected). This is
called "unwrapping" the promise. Waiting on a promise will by default unwrap
the promise state.

You can force a promise to resolve and *not* unwrap the state of the promise
by passing `false` to the first argument of the `wait` function:

```php
$promise = new Promise();
$promise->reject('foo');
// This will not throw an exception. It simply ensures the promise has
// been resolved.
$promise->wait(false);
```

When unwrapping a promise, the resolved value of the promise will be waited
upon until the unwrapped value is not a promise. This means that if you resolve
promise A with a promise B and unwrap promise A, the value returned by the
wait function will be the value delivered to promise B.

**Note**: when you do not unwrap the promise, no value is returned.


# Cancellation

You can cancel a promise that has not yet been fulfilled using the `cancel()`
method of a promise. When creating a promise you can provide an optional
cancel function that when invoked cancels the action of computing a resolution
of the promise.


# API


## Promise

When creating a promise object, you can provide an optional `$waitFn` and
`$cancelFn`. `$waitFn` is a function that is invoked with no arguments and is
expected to resolve the promise. `$cancelFn` is a function with no arguments
that is expected to cancel the computation of a promise. It is invoked when the
`cancel()` method of a promise is called.

```php
use GuzzleHttp\Promise\Promise;

$promise = new Promise(
    function () use (&$promise) {
        $promise->resolve('waited');
    },
    function () {
        // do something that will cancel the promise computation (e.g., close
        // a socket, cancel a database query, etc...)
    }
);

assert('waited' === $promise->wait());
```

A promise has the following methods:

- `then(callable $onFulfilled, callable $onRejected) : PromiseInterface`
  
  Appends fulfillment and rejection handlers to the promise, and returns a new promise resolving to the return value of the called handler.

- `otherwise(callable $onRejected) : PromiseInterface`
  
  Appends a rejection handler callback to the promise, and returns a new promise resolving to the return value of the callback if it is called, or to its original fulfillment value if the promise is instead fulfilled.

- `wait($unwrap = true) : mixed`

  Synchronously waits on the promise to complete.
  
  `$unwrap` controls whether or not the value of the promise is returned for a
  fulfilled promise or if an exception is thrown if the promise is rejected.
  This is set to `true` by default.

- `cancel()`

  Attempts to cancel the promise if possible. The promise being cancelled and
  the parent most ancestor that has not yet been resolved will also be
  cancelled. Any promises waiting on the cancelled promise to resolve will also
  be cancelled.

- `getState() : string`

  Returns the state of the promise. One of `pending`, `fulfilled`, or
  `rejected`.

- `resolve($value)`

  Fulfills the promise with the given `$value`.

- `reject($reason)`

  Rejects the promise with the given `$reason`.


## FulfilledPromise

A fulfilled promise can be created to represent a promise that has been
fulfilled.

```php
use GuzzleHttp\Promise\FulfilledPromise;

$promise = new FulfilledPromise('value');

// Fulfilled callbacks are immediately invoked.
$promise->then(function ($value) {
    echo $value;
});
```


## RejectedPromise

A rejected promise can be created to represent a promise that has been
rejected.

```php
use GuzzleHttp\Promise\RejectedPromise;

$promise = new RejectedPromise('Error');

// Rejected callbacks are immediately invoked.
$promise->then(null, function ($reason) {
    echo $reason;
});
```


# Promise interop

This library works with foreign promises that have a `then` method. This means
you can use Guzzle promises with [React promises](https://github.com/reactphp/promise)
for example. When a foreign promise is returned inside of a then method
callback, promise resolution will occur recursively.

```php
// Create a React promise
$deferred = new React\Promise\Deferred();
$reactPromise = $deferred->promise();

// Create a Guzzle promise that is fulfilled with a React promise.
$guzzlePromise = new \GuzzleHttp\Promise\Promise();
$guzzlePromise->then(function ($value) use ($reactPromise) {
    // Do something something with the value...
    // Return the React promise
    return $reactPromise;
});
```

Please note that wait and cancel chaining is no longer possible when forwarding
a foreign promise. You will need to wrap a third-party promise with a Guzzle
promise in order to utilize wait and cancel functions with foreign promises.


## Event Loop Integration

In order to keep the stack size constant, Guzzle promises are resolved
asynchronously using a task queue. When waiting on promises synchronously, the
task queue will be automatically run to ensure that the blocking promise and
any forwarded promises are resolved. When using promises asynchronously in an
event loop, you will need to run the task queue on each tick of the loop. If
you do not run the task queue, then promises will not be resolved.

You can run the task queue using the `run()` method of the global task queue
instance.

```php
// Get the global task queue
$queue = \GuzzleHttp\Promise\queue();
$queue->run();
```

For example, you could use Guzzle promises with React using a periodic timer:

```php
$loop = React\EventLoop\Factory::create();
$loop->addPeriodicTimer(0, [$queue, 'run']);
```

*TODO*: Perhaps adding a `futureTick()` on each tick would be faster?


# Implementation notes


## Promise resolution and chaining is handled iteratively

By shuffling pending handlers from one owner to another, promises are
resolved iteratively, allowing for "infinite" then chaining.

```php
<?php
require 'vendor/autoload.php';

use GuzzleHttp\Promise\Promise;

$parent = new Promise();
$p = $parent;

for ($i = 0; $i < 1000; $i++) {
    $p = $p->then(function ($v) {
        // The stack size remains constant (a good thing)
        echo xdebug_get_stack_depth() . ', ';
        return $v + 1;
    });
}

$parent->resolve(0);
var_dump($p->wait()); // int(1000)

```

When a promise is fulfilled or rejected with a non-promise value, the promise
then takes ownership of the handlers of each child promise and delivers values
down the chain without using recursion.

When a promise is resolved with another promise, the original promise transfers
all of its pending handlers to the new promise. When the new promise is
eventually resolved, all of the pending handlers are delivered the forwarded
value.


## A promise is the deferred.

Some promise libraries implement promises using a deferred object to represent
a computation and a promise object to represent the delivery of the result of
the computation. This is a nice separation of computation and delivery because
consumers of the promise cannot modify the value that will be eventually
delivered.

One side effect of being able to implement promise resolution and chaining
iteratively is that you need to be able for one promise to reach into the state
of another promise to shuffle around ownership of handlers. In order to achieve
this without making the handlers of a promise publicly mutable, a promise is
also the deferred value, allowing promises of the same parent class to reach
into and modify the private properties of promises of the same type. While this
does allow consumers of the value to modify the resolution or rejection of the
deferred, it is a small price to pay for keeping the stack size constant.

```php
$promise = new Promise();
$promise->then(function ($value) { echo $value; });
// The promise is the deferred value, so you can deliver a value to it.
$promise->resolve('foo');
// prints "foo"
```
# Easy WordPress VMs with Vagrant and Ansible

This bundle of files automates the process of automatically creating and provisioning local virtual machines with a complete, running instance of WordPress. Such things are useful for local development and testing things like plugins and themes on a "clean" WordPress install.

## Prerequisites

To make use of these files, you'll need to have the following prerequisites installed on your workstation:

* [VirtualBox](https://www.virtualbox.org/)
* [Vagrant](http://www.vagrantup.com/)
* [Ansible](https://www.ansible.com/)

Any Vagrant-based VM needs to start with a Vagrant "box" file -- a canned image of a base system that Vagrant can use as the starting point for further customization. **By default, these scripts use the official Vagrant image distributed by Ubuntu of the 64-bit version of Ubuntu 14.04 LTS, "Trusty Tahr," so you do not need to download or install anything further if you are satisfied with that version.** As of this writing (September 16, 2014) that file is [distributed here](https://vagrantcloud.com/ubuntu/boxes/trusty64).

If you want to build your VM from a different version or distro, check [Vagrant Cloud](https://vagrantcloud.com/discover/featured) or [cloud-images.ubuntu.com/vagrant](http://cloud-images.ubuntu.com) to find the URL of a box you wish to use. If you wish to use a box other than the default, just install the box (if it's not hosted at Vagrant Cloud) and update the Vagrantfile to point to the particular box you wish to use.

Note that these scripts were designed for use with Ubuntu, so they make use of the apt packaging manager and other conventions Debian-derived distributions share (filesystem locations, configuration file structure, etc.). This means they will only work properly out of the box with Debian Linux or Debian-derived distributions such as Ubuntu. If you use Red Hat/CentOS/Fedora, or another distribution that uses a different package manager, consult the Ansible documentation for instructions on how to modify the setup.yml file to change the apt commands to those for your particular package manager and modify file locations so they map to the appropriate places for your distro.

## What It Does

Together with the prerequisites listed above, the scripts contained herein will let you create a new VM with a simple `vagrant up` that:

* Is configured with a static IP address on your local LAN (default 192.168.50.50) so you don't need to constantly be looking up new DHCP-assigned addresses each time it restarts
* Has a complete MySQL 5 setup (client and server) installed
* Has a complete Apache 2 setup installed (with mod_rewrite)
* Has a complete PHP5 setup (both mod_php and CLI versions) installed, with the following modules:
    * php5-curl
    * php5-gd
    * php5-imagick
    * php5-mysql
    * php5-sqlite
    * php5-xcache
    * php5-xmlrpc
    * php5-xdebug (ready for remote debugging on port 10000; use the IDE key "vagrant")
* Installs the latest version of the WordPress software in /vagrant, so you can work with local files via your favorite editor/IDE; sets up symlink to it at /var/www/wordpress`so Apache can find it
* Has a MySQL database (name: "wordpress") and database user (name: "user_wp"; password: "wordpress") for WordPress to make use of
* Has a configuration file in `/root/.my.cnf` to allow the root user to log into MySQL as root without needing to enter a username or password
* Has an Apache virtual host configured and enabled to serve WordPress

So, once the box is provisioned, all you need to do is go to 192.168.50.50 in your browser to begin the famous WordPress 5-minute install.

## Getting Started

To begin, create an empty directory and clone the files in this repository into it.

Then just run the command `vagrant up` and your VM should bootstrap itself into existence, ready to work with. 

[More information on working with Vagrant VMs, including how to shell into a running VM and shut it down safely, is available in the Vagrant documentation.](http://docs.vagrantup.com/v2/getting-started/index.html)

## Customization/Configuration

**If you use the default box, no configuration should be required to get up and running.** However, in the file named `Vagrantfile`, you *may* wish to change the following:

* If you want to use an IP address other than 192.168.50.50, replace that address with the one you wish to use in two places:
    * `Vagrantfile`, on line 9
    * `vagrant-inventory`, on line 2

Finally, it's not necessary in most common use scenarios, but if for some reason you wish to change the configuration of the Apache virtual host or the MySQL configuration for the root user, you can find the templates used to generate those configuration files in the `templates` subdirectory.

If you wish to modify or extend the basic logic that provisions the system -- add new packages, say -- all that logic is in the file `setup.yml`. This file is an Ansible "playbook," so you can make use of any of Ansible's modules or features there. For more information on how to work with Ansible playbooks, refer to their ["Intro to Playbooks"](http://docs.ansible.com/ansible/playbooks_intro.html) document. [A complete reference of all modules available within an Ansible playbook](http://docs.ansible.com/ansible/modules_by_category.html) is also available.

## License

These files are copyright 2014, Jason Lefkowitz.

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.
