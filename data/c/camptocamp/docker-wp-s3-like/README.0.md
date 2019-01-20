=== WP Offload S3 Lite ===
Contributors: bradt, deliciousbrains
Tags: uploads, amazon, s3, amazon s3, mirror, admin, media, cdn, cloudfront
Requires at least: 4.4
Tested up to: 4.7.3
Stable tag: 1.1.6
License: GPLv3

Copies files to Amazon S3 as they are uploaded to the Media Library. Optionally configure Amazon CloudFront for faster delivery.

== Description ==

https://www.youtube.com/watch?v=_PVybEGaRXc

This plugin automatically copies images, videos, documents, and any other media added through WordPress' media uploader to [Amazon S3](http://aws.amazon.com/s3/). It then automatically replaces the URL to each media file with their respective Amazon S3 URL or, if you have configured [Amazon CloudFront](http://aws.amazon.com/cloudfront/), the respective CloudFront URL. Image thumbnails are also copied to Amazon S3 and delivered through S3/CloudFront.

Uploading files *directly* to your Amazon S3 account is not currently supported by this plugin. They are uploaded to your server first, then copied to Amazon S3. There is an option to automatically remove the files from your server once they are copied to Amazon S3 however.

If you're adding this plugin to a site that's been around for a while, your existing media files will not be copied or served from Amazon S3. Only newly uploaded files will be copied and served from Amazon S3. The pro upgrade has an upload tool to handle existing media files.

**PRO Upgrade with Email Support and More Features**

* Upload existing Media Library to Amazon S3
* Control Amazon S3 files from the Media Library
* [Assets addon](https://deliciousbrains.com/wp-offload-s3/?utm_source=wordpress.org&utm_medium=web&utm_content=desc&utm_campaign=os3-free-plugin#assets-addon) - Serve your CSS & JS from Amazon S3/CloudFront
* [WooCommerce addon](https://deliciousbrains.com/wp-offload-s3/?utm_source=wordpress.org&utm_medium=web&utm_content=desc&utm_campaign=os3-free-plugin#woocommerce-addon)
* [Easy Digital Downloads addon](https://deliciousbrains.com/wp-offload-s3/?utm_source=wordpress.org&utm_medium=web&utm_content=desc&utm_campaign=os3-free-plugin#edd-addon)
* PriorityExpert&trade; email support

[Compare pro vs free &rarr;](http://deliciousbrains.com/wp-offload-s3/upgrade/?utm_source=wordpress.org&utm_medium=web&utm_content=desc&utm_campaign=os3-free-plugin)

The video below runs through the pro upgrade features...

https://www.youtube.com/watch?v=55xNGnbJ_CY

*This plugin has been completely rewritten, but was originally a fork of
[Amazon S3 for WordPress with CloudFront](http://wordpress.org/extend/plugins/tantan-s3-cloudfront/)
which is a fork of [Amazon S3 for WordPress](http://wordpress.org/extend/plugins/tantan-s3/), also known as tantan-s3.*

== Installation ==

1. Install the required [Amazon Web Services plugin](http://wordpress.org/extend/plugins/amazon-web-services/) using WordPress' built-in installer
2. Follow the instructions to setup your AWS access keys
3. Install this plugin using WordPress' built-in installer
4. Access the *S3 and CloudFront* option under *AWS* and configure

== Frequently Asked Questions ==

= What are the minimum requirements? =

You can see the minimum requirements [here](https://deliciousbrains.com/wp-offload-s3/pricing/?utm_source=wordpress.org&utm_medium=web&utm_content=desc&utm_campaign=os3-free-plugin#requirements).

== Screenshots ==

1. Choosing/creating a bucket
2. Settings screen

== Upgrade Notice ==

= 1.1 =
This is a major change, which ensures S3 URLs are no longer saved in post content. Instead, local URLs are filtered on page generation and replaced with the S3 version. If you depend on the S3 URLs being stored in post content you will need to make modifications to support this version.

= 0.6 =
This version requires PHP 5.3.3+ and the Amazon Web Services plugin

== Changelog ==

= WP Offload S3 Lite 1.1.6 - 2017-03-13 =
* New: Compatibility with [Advanced Custom Fields](https://wordpress.org/plugins/advanced-custom-fields/)
* New: `as3cf_filter_post_local_to_s3` and `as3cf_filter_post_s3_to_local` filters added for filtering S3 URLs in custom content
* Improvement: Ensure files uploaded using `media_handle_sideload` have unique filename on S3 when 'Remove Files From Server' enabled
* Bug fix: Files uploaded to S3 with empty filenames when the filename started with non-latin characters
* Bug fix: Audio files with private ACL not working with WordPress's default media player
* Bug fix: S3 API version not passed to S3 client
* Bug fix: Content added to text widgets via the Customizer not saved
* Bug fix: Original file not removed locally when cropped via the Customizer and 'Remove Files From Server' enabled
* Bug fix: Incorrect Media Library URLs saved to the database when WordPress installed in a subdirectory

= WP Offload S3 Lite 1.1.5 - 2017-01-12 =
* Improvement: Filter custom CSS - S3 URLs will no longer be saved to the database
* Bug fix: PDF previews have incorrect MIME type
* Bug fix: Original PDF not removed from S3 on attachment delete when image previews exist

= WP Offload S3 Lite 1.1.4 - 2016-12-13 =
* New: Upgrade routine to replace all S3 URLs in post excerpts with local URLs
* Improvement: Performance improvements
* Improvement: Allow expires time to be filtered for private content using the `as3cf_expires` filter
* Bug fix: Image `srcset` not correctly applied when file names contain special characters

= WP Offload S3 Lite 1.1.3 - 2016-11-28 =
* Bug fix: Private URL signing params stripped in some circumstances
* Improvement: Performance improvements for URL filtering, especially on large sites

= WP Offload S3 Lite 1.1.2 - 2016-11-02 =
* Improvement: Better content filtering support for third party plugins and themes
* Bug fix: PHP Warning: Division by zero

= WP Offload S3 Lite 1.1.1 - 2016-10-17 =
* New: Filter post excerpts - S3 URLs will no longer be saved to the database
* Bug fix: PHP 5.3 Fatal error: Using $this when not in object context
* Bug fix: Query string parameters incorrectly encoded for Media Library items

= WP Offload S3 Lite 1.1 - 2016-09-29 =
* New: Filter post content. S3 URLs will no longer be saved to the database
* New: Upgrade routine to replace all S3 URLs in content with local URLs
* New: Support for theme custom logos
* New: Control the ACL for intermediate image sizes using the `as3cf_upload_acl_sizes` filter
* Bug fix: File names containing special characters double encoded
* Bug fix: `srcset` not working for file names containing special characters
* Bug fix: Incorrect placeholder text for 'Path' option
* Bug fix: Objects in root of bucket not deleted when removed from the Media Library
* Bug fix: No longer use deprecated functions in WordPress 4.6
* Bug fix: Don't delete local file when 'Remove Files From Server' enabled and upload to S3 fails

= WP Offload S3 Lite 1.0.5 - 2016-09-01 =
* New: Compatibility with WordPress 4.6
* Improvement: No longer delete plugin data on uninstall. Manual removal possible, as per this [doc](https://deliciousbrains.com/wp-offload-s3/doc/uninstall/)

= WP Offload S3 Lite 1.0.4 - 2016-05-30 =
* New: Now using simpler Force HTTPS setting, removed redundant Always Use HTTP setting
* New: `as3cf_cloudfront_path_parts` filter allows changing served CloudFront path (useful when distribution pulls subdirectory)
* Improvement: Better compatibility with non-standard notices from other plugins and themes
* Improvement: Added basic auth and proxy info to diagnostic info
* Improvement: Added `allow_url_fopen` status to diagnostic info
* Improvement: Added memory usage to diagnostic info
* Improvement: Ensure notice text is 800px or less in width
* Improvement: Reduced database queries on settings screen
* Bug fix: Properly handle _wp_attachment_data metadata when it is a serialized WP_Error

= WP Offload S3 Lite 1.0.3 - 2016-03-23 =
* Bug fix: Don't replace srcset URLs when Rewrite File URLs option disabled
* Bug fix: Fatal error: Cannot redeclare as3cf_get_secure_attachment_url()

= WP Offload S3 Lite 1.0.2 - 2016-03-08 =
* Bug fix: Uninstall would run even if pro plugin installed

= WP Offload S3 Lite 1.0.1 - 2016-03-08 =
* Bug fix: Fatal error on plugin activation
* Bug fix: Unable to activate Pro upgrade

= WP Offload S3 Lite 1.0 - 2016-03-07 =
* New: Plugin renamed to "WP Offload S3 Lite"
* New: Define any and all settings with a constant in wp-config.php
* New: Documentation links for each setting
* Improvement: Simplified domain setting UI
* Improvement: Far future expiration header set by default
* Improvement: Newly created bucket now immediately appears in the bucket list
* Improvement: Cleanup user meta on uninstall
* Improvement: WP Retina 2x integration removed
* Bug fix: Year/Month folder structure on S3 not created if the 'Organise my uploads into month and year-based folders' WordPress setting is disabled
* Bug fix: Responsive srcset PHP notices
* Bug fix: Compatibility addon notices displayed to non-admin users
* Bug fix: Potential PHP fatal error in MySQL version check in diagnostic log
* Bug fix: Missing image library notices displaying before plugin is setup

= WP Offload S3 0.9.12 - 2016-02-03 =
* Improvement: Compatibility with WP Offload S3 Assets 1.1
* Bug fix: Object versioned responsive images in post content not working when served from S3 on WordPress 4.4+

= WP Offload S3 0.9.11 - 2015-12-19 =
* Bug fix: Responsive images in post content not working when served from S3
* Bug fix: Responsive images using wrong image size when there are multiple images with the same width

= WP Offload S3 0.9.10 - 2015-11-26 =
* Improvement: Support for responsive images in WP 4.4
* Bug fix: Incorrect file path for intermediate image size files uploaded to S3 with no prefix
* Bug fix: Thumbnail previews return 404 error during image edit screen due to character encoding

= WP Offload S3 0.9.9 - 2015-11-12 =
* Improvement: Improve wording of compatibility notices
* Improvement: Compatibility with Easy Digital Downloads 1.0.1 and WooCommerce 1.0.3 addons
* Improvement: Better determine available memory for background processes
* Bug fix: URL previews incorrect due to stripping `/` characters
* Bug fix: PHP Warning: stream_wrapper_register(): Protocol s3:// is already defined
* Bug fix: PHP Fatal error:  Call to undefined method WP_Error::get()

= WP Offload S3 0.9.8 - 2015-11-02 =
* Bug fix: Attachment URLs containing query string parameters incorrectly encoded

= WP Offload S3 0.9.7 - 2015-10-26 =
* Improvement: Improve compatibility with third party plugins when the _Remove Files From Server_ option is enabled
* Improvement: Fix inconsistent spacing on the WP Offload S3 settings screen
* Improvement: Validate _CloudFront or custom domain_ input field
* Improvement: Link to current S3 bucket added to WP Offload S3 settings screen
* Improvement: Show notice when neither GD or Imagick image libraries are not installed
* Improvement: Supply Cache-Control header to S3 when the _Far Future Expiration Header_ option is enabled
* Improvement: Additional information added to _Diagnostic Information_
* Improvement: Added warning when _Remove Files From Server_ option is enabled
* Improvement: Filter added to allow additional image versions to be uploaded to S3
* Bug fix: File size not stored in _wp_attachment_metadata_ when _Remove Files From Server_ option is enabled
* Bug fix: Uploads on Multisite installs allowed after surpassing upload limit
* Bug fix: Site icon in WordPress customizer returns 404
* Bug fix: Image versions remain locally and on S3 after deletion, when the file name contains characters which require escaping
* Bug fix: Files with the same file name overwritten when __Remove Files From Server_ option is enabled
* Bug fix: Cron tasks incorrectly scheduled due to passing the wrong time to `wp_schedule_event`
* Bug fix: Default options not shown in the UI after first install

= WP Offload S3 0.9.6 - 2015-10-01 =
* Improvement: Update text domains for translate.wordpress.org integration

= WP Offload S3 0.9.5 - 2015-09-01 =
* Bug fix: Fatal error: Cannot use object of type WP_Error as array

= WP Offload S3 0.9.4 - 2015-08-27 =
* New: Update all existing attachments with missing file sizes when the 'Remove Files From Server' option is enabled (automatically runs in the background)
* Improvement: Show when constants are used to set bucket and region options
* Improvement: Don't show compatibility notices on plugin update screen
* Improvement: On Multisite installs don't call `restore_current_blog()` on successive loop iterations
* Bug fix: 'Error getting URL preview' alert shown when enter key pressed on settings screen
* Bug fix: Unable to crop header images when the 'Remove Files From Server' option is enabled
* Bug fix: Incorrect storage space shown on Multisite installs when the 'Remove Files From Server' option is enabled
* Bug fix: Upload attempted to non existent bucket when defined by constant
* Bug fix: 'SignatureDoesNotMatch' error shown when using signed URLs with bucket names containing '.' characters

= WP Offload S3 0.9.3 - 2015-08-17 =
* New: Pro upgrade sidebar
* Bug fix: Create buckets in US standard region causing S3 URLs to 404 errors

= WP Offload S3 0.9.2 - 2015-07-29 =
* Bug fix: Accidentally released the sidebar for after we launch the pro version

= WP Offload S3 0.9.1 - 2015-07-29 =
* Improvement: Access denied sample IAM policy replaced with link to [Quick Start Guide](https://deliciousbrains.com/wp-offload-s3/doc/quick-start-guide/)
* Improvement: Access denied messages on bucket selection or bucket creation now link to [Quick Start Guide](https://deliciousbrains.com/wp-offload-s3/doc/quick-start-guide/)
* Improvement: Object expires time can now be filtered using the `as3cf_object_meta` filter
* Bug fix: Error not always shown when S3 bucket inaccessible due to incorrect permissions
* Bug fix: Permission checks fail when S3 bucket is in a non-default region and defined by `AS3CF_BUCKET` constant
* Bug fix: Restore `as3cf_get_attached_file_copy_back_to_local` filter
* Bug fix: Image versions not uploaded to S3 when an edited image is restored
* Bug fix: Original image version not deleted from server when _Remove Files From Server_ option enabled
* Bug fix: Media library items with non-ascii characters in the file name are not removed from S3
* Bug fix: Compatibility notices shown on plugin install pages
* Bug fix: WordPress footer overlaps WP Offload S3 sidebar
* Bug fix: Upon initial setup the settings changed alert shows when no settings have changed

= WP Offload S3 0.9 - 2015-07-08 =
* New: Plugin rebranded to WP Offload S3
* New: Support tab added to _Offload S3_ screen containing diagnostic information
* New: Compatibility with the [Media Replace](https://wordpress.org/plugins/enable-media-replace/) plugin
* New: Select bucket region when creating a new bucket
* New: Toggle switches redesigned
* Improvement: Compatibility with release candidate of Pro plugin
* Improvement: Example IAM policy more secure
* Improvement: Set default bucket region using the `AS3CF_REGION` constant
* Improvement: Added `as3cf_object_meta` filter for developers
* Improvement: Bucket selection moved to modal window
* Improvement: Don't allow bucket names to contain invalid characters on creation
* Improvement: More verbose error messages on bucket selection
* Improvement: Settings link added to plugin row on _Plugins_ screen
* Improvement: Object versioning enabled by default
* Improvement: Uninstall routines added
* Improvement: JavaScript coding standards
* Improvement: Cache result when checking S3 bucket permissions
* Bug fix: Bucket region errors result in blank WP Offload S3 screen
* Bug fix: Editing an image when _Remove Files From Server_ option is enabled results in error
* Bug fix: Metadata upgrade procedure triggered on new installs
* Bug fix: File URLs when uploaded to a subdirectory result in incorrect S3 URLs
* Bug fix: Errors logged when trying to delete non-existent HiDPI images
* Bug fix: SignatureDoesNotMatch errors on regions with v4 authentication
* Bug fix: Customizer background image not editable
* Bug fix: Error when creating buckets with US Standard region
* Bug fix: Notices appearing incorrectly on some admin screens
* Bug fix: Subsite upload paths repeated on multisite installs
* Bug fix: Handle multisite installs where `BLOG_ID_CURRENT_SITE` is not 1

= WP Offload S3 0.8.2 - 2015-01-31 =
* New: Input bucket in settings to avoid listing all buckets
* New: Specify bucket with 'AS3CF_BUCKET' constant
* Improvement: Compatibility with beta release of Pro plugin
* Bug Fix: Incorrect file prefix in S3 permission check

= WP Offload S3 0.8.1 - 2015-01-19 =
* Bug Fix: Permission problems on installs running on EC2s
* Bug Fix: Blank settings page due to WP_Error on S3 permission check
* Bug Fix: Warning: strtolower() expects parameter 1 to be string, object given
* Bug Fix: Region post meta update running on subsites of Multisite installs

= WP Offload S3 0.8 - 2015-01-10 =
* New: Redesigned settings UI
* Improvement: SSL setting can be fully controlled, HTTPS for urls always, based on request or never
* Improvement: Download files from S3 that are not found on server when running Regenerate Thumbnails plugin
* Improvement: When calling `get_attached_file()` and file is missing from server, return S3 URL
* Improvement: Code cleanup to WordPress coding standards
* Bug Fix: Files for all subsites going into the same S3 folder on multisite installs setup prior to WP 3.5
* Bug Fix: 'attempting to access local file system' error for some installs

= WP Offload S3 0.7.2 - 2014-12-11 =
* Bug: Some buckets in the EU region causing permission and HTTP errors
* Bug: Undefined variable: message in view/error.php also causing white screens

= WP Offload S3 0.7.1 - 2014-12-05 =
* Bug: Read-only error on settings page sometimes false positive

= WP Offload S3 0.7 - 2014-12-04 =
* New: Proper S3 region subdomain in URLs for buckets not in the US Standard region (e.g. https://s3-us-west-2.amazonaws.com/...)
* New: Update all existing attachment meta with bucket region (automatically runs in the background)
* New: Get secure URL for different image sizes (iamzozo)
* New: S3 bucket can be set with constant in wp-config.php (dberube)
* New: Filter for allowing/disallowing file types: `as3cf_allowed_mime_types`
* New: Filter to cancel upload to S3 for any reason: `as3cf_pre_update_attachment_metadata`
* New: Sidebar with email opt-in
* Improvement: Show warning when S3 policy is read-only
* Improvement: Tooltip added to clarify option
* Improvement: Move object versioning option to make it clear it does not require CloudFront
* Improvement: By default only allow file types in `get_allowed_mime_types()` to be uploaded to S3
* Improvement: Compatibility with WPML Media plugin
* Bug Fix: Edited images not removed on S3 when restoring image and IMAGE_EDIT_OVERWRITE true
* Bug Fix: File names with certain characters broken not working
* Bug Fix: Edited image uploaded to incorrect month folder
* Bug Fix: When creating a new bucket the bucket select box appears empty on success
* Bug Fix: SSL not working in regions other than US Standard
* Bug Fix: 'Error uploading' and 'Error removing local file' messages when editing an image
* Bug Fix: Upload and delete failing when bucket is non-US-region and bucket name contains dot
* Bug Fix: S3 file overwritten when file with same name uploaded and local file removed (dataferret)
* Bug Fix: Manually resized images not uploaded (gmauricio)

= WP Offload S3 0.6.1 - 2013-09-21 =
* WP.org download of Amazon Web Services plugin is giving a 404 Not Found, so directing people to download from Github instead

= WP Offload S3 0.6 - 2013-09-20 =
* Complete rewrite
* Now requires PHP 5.3.3+
* Now requires the [Amazon Web Services plugin](http://wordpress.org/extend/plugins/amazon-web-services/) which contains the latest PHP libraries from Amazon
* Now works with multisite
* New Option: Custom S3 object path
* New Option: Always serve files over https (SSL)
* New Option: Enable object versioning by appending a timestamp to the S3 file path
* New Option: Remove uploaded file from local filesystem once it has been copied to S3
* New Option: Copy any HiDPI (@2x) images to S3 (works with WP Retina 2x plugin)

= WP Offload S3 0.5 - 2013-01-29 =
* Forked [Amazon S3 for WordPress with CloudFront](http://wordpress.org/extend/plugins/tantan-s3-cloudfront/)
* Cleaned up the UI to fit with today's WP UI
* Fixed issues causing error messages when WP_DEBUG is on
* [Delete files on S3 when deleting WP attachment](https://github.com/deliciousbrains/wp-amazon-s3-and-cloudfront/commit/e777cd49a4b6999f999bd969241fb24cbbcece60)
* [Added filter to the get_attachment_url function](https://github.com/deliciousbrains/wp-amazon-s3-and-cloudfront/commit/bbe1aed5c2ae900e9ba1b16ba6806c28ab8e2f1c)
* [Added function to get a temporary, secure download URL for private files](https://github.com/deliciousbrains/wp-amazon-s3-and-cloudfront/commit/11f46ec2714d34907009e37ad3b97f4421aefed3)
=== Amazon Web Services ===
Contributors: bradt, deliciousbrains
Tags: amazon, amazon web services
Requires at least: 4.4
Tested up to: 4.7.3
Stable tag: 1.0.2
License: GPLv3

Houses the Amazon Web Services (AWS) PHP libraries and manages access keys. Required by other AWS plugins.

== Description ==

This plugin is required by other plugins, which use its libraries and its settings to connect to AWS services. Currently, there are only two plugins that require this plugin:

* [WP Offload S3 Lite](http://wordpress.org/plugins/amazon-s3-and-cloudfront/)
* [WP Offload S3](https://deliciousbrains.com/wp-offload-s3/)

= Requirements =

* PHP version 5.3.3 or greater
* PHP cURL library 7.16.2 or greater
* cURL compiled with OpenSSL and zlib
* curl_multi_exec enabled

== Installation ==

1. Use WordPress' built-in installer
2. A new AWS menu will appear in the side menu

== Screenshots ==

1. Settings screen

== Changelog ==

= 1.0.2 - 2017-03-13 =
* New: AWS SDK updated to 2.8.31
* New: London and Montreal regions added

= 1.0.1 - 2016-12-13 =
* New: Mumbai and Seoul regions added

= 1.0 - 2016-09-29 =
* Improvement: Compatibility with WP Offload S3 Lite 1.1
* Improvement: Compatibility with WP Offload S3 1.2

= 0.3.7 - 2016-09-01 =
* Improvement: No longer delete plugin data on uninstall. Manual removal possible, as per this [doc](https://deliciousbrains.com/wp-offload-s3/doc/uninstall/).

= 0.3.6 - 2016-05-30 =
* Improvement: Now checks that the `curl_multi_exec` function is available.

= 0.3.5 - 2016-03-07 =
* Improvement: Support for `DBI_` prefixed constants to avoid conflicts with other plugins
* Improvement: Redesign of the Addons page
* Improvement: Compatibility with WP Offload S3 Lite 1.0
* Improvement: Compatibility with WP Offload S3 1.1

= 0.3.4 - 2015-11-02 =
* Improvement: Compatibility with WP Offload S3 Pro 1.0.3

= 0.3.3 - 2015-10-26 =
* Improvement: Updated Amazon SDK to version 2.8.18
* Improvement: Fix inconsistent notice widths on _Access Keys_ screen
* New: WP Offload S3 Pro addons (Enable Media Replace, Meta Slider, WPML) added to the _Addons_ screen

= 0.3.2 - 2015-08-26 =
* New: WP Offload S3 Pro upgrade and addons added to the _Addons_ screen

= 0.3.1 - 2015-07-29 =
* Bug fix: Style inconsistencies on the _Addons_ screen

= 0.3 - 2015-07-08 =
* New: Support for [IAM Roles on Amazon EC2](https://deliciousbrains.com/wp-offload-s3/doc/iam-roles/) using the `AWS_USE_EC2_IAM_ROLE` constant
* New: Redesigned _Access Keys_ and _Addons_ screens
* Improvement: _Settings_ menu item renamed to _Access Keys_
* Improvement: _Access Keys_ link added to plugin row on _Plugins_ screen
* Improvement: Activate addons directly from within _Addons_ screen
* Improvement: [Quick Start Guide](https://deliciousbrains.com/wp-offload-s3/doc/quick-start-guide/) documentation

= 0.2.2 - 2015-01-19 =
* Bug Fix: Reverting AWS client config of region and signature

= 0.2.1 - 2015-01-10 =
* New: AWS SDK updated to 2.7.13
* New: Translation ready
* Improvement: Code cleanup to WordPress coding standards
* Improvement: Settings notice UI aligned with WordPress style
* Bug: Error if migrating keys over from old Amazon S3 and CloudFront plugin settings

= 0.2 - 2014-12-04 =
* New: AWS SDK updated to 2.6.16
* New: Set the region for the AWS client by defining `AWS_REGION` in your wp-config.php
* New: Composer file for Packagist support
* Improvement: Base plugin class performance of installed version
* Improvement: Base plugin class accessor for various properties
* Improvement: Addon plugin modal now responsive
* Improvement: Better menu icon
* Improvement: Code formatting to WordPress standards

= 0.1 - 2013-09-20 =
* First release
# WP Offload S3 Lite #
**Contributors:** bradt, deliciousbrains  
**Tags:** uploads, amazon, s3, amazon s3, mirror, admin, media, cdn, cloudfront  
**Requires at least:** 4.4  
**Tested up to:** 4.7.3  
**Stable tag:** 1.1.6  
**License:** GPLv3  

Copies files to Amazon S3 as they are uploaded to the Media Library. Optionally configure Amazon CloudFront for faster delivery.

## Description ##

https://www.youtube.com/watch?v=_PVybEGaRXc

This plugin automatically copies images, videos, documents, and any other media added through WordPress' media uploader to [Amazon S3](http://aws.amazon.com/s3/). It then automatically replaces the URL to each media file with their respective Amazon S3 URL or, if you have configured [Amazon CloudFront](http://aws.amazon.com/cloudfront/), the respective CloudFront URL. Image thumbnails are also copied to Amazon S3 and delivered through S3/CloudFront.

Uploading files *directly* to your Amazon S3 account is not currently supported by this plugin. They are uploaded to your server first, then copied to Amazon S3. There is an option to automatically remove the files from your server once they are copied to Amazon S3 however.

If you're adding this plugin to a site that's been around for a while, your existing media files will not be copied or served from Amazon S3. Only newly uploaded files will be copied and served from Amazon S3. The pro upgrade has an upload tool to handle existing media files.

**PRO Upgrade with Email Support and More Features**

* Upload existing Media Library to Amazon S3
* Control Amazon S3 files from the Media Library
* [Assets addon](https://deliciousbrains.com/wp-offload-s3/?utm_source=wordpress.org&utm_medium=web&utm_content=desc&utm_campaign=os3-free-plugin#assets-addon) - Serve your CSS & JS from Amazon S3/CloudFront
* [WooCommerce addon](https://deliciousbrains.com/wp-offload-s3/?utm_source=wordpress.org&utm_medium=web&utm_content=desc&utm_campaign=os3-free-plugin#woocommerce-addon)
* [Easy Digital Downloads addon](https://deliciousbrains.com/wp-offload-s3/?utm_source=wordpress.org&utm_medium=web&utm_content=desc&utm_campaign=os3-free-plugin#edd-addon)
* PriorityExpert&trade; email support

[Compare pro vs free &rarr;](http://deliciousbrains.com/wp-offload-s3/upgrade/?utm_source=wordpress.org&utm_medium=web&utm_content=desc&utm_campaign=os3-free-plugin)

The video below runs through the pro upgrade features...

https://www.youtube.com/watch?v=55xNGnbJ_CY

*This plugin has been completely rewritten, but was originally a fork of
[Amazon S3 for WordPress with CloudFront](http://wordpress.org/extend/plugins/tantan-s3-cloudfront/)
which is a fork of [Amazon S3 for WordPress](http://wordpress.org/extend/plugins/tantan-s3/), also known as tantan-s3.*

## Installation ##

1. Install the required [Amazon Web Services plugin](http://wordpress.org/extend/plugins/amazon-web-services/) using WordPress' built-in installer
2. Follow the instructions to setup your AWS access keys
3. Install this plugin using WordPress' built-in installer
4. Access the *S3 and CloudFront* option under *AWS* and configure

## Frequently Asked Questions ##

### What are the minimum requirements? ###

You can see the minimum requirements [here](https://deliciousbrains.com/wp-offload-s3/pricing/?utm_source=wordpress.org&utm_medium=web&utm_content=desc&utm_campaign=os3-free-plugin#requirements).

## Screenshots ##

### 1. Choosing/creating a bucket ###
![Choosing/creating a bucket](https://raw.githubusercontent.com/deliciousbrains/wp-wp-offload-s3-lite/assets/screenshot-1.png)

### 2. Settings screen ###
![Settings screen](https://raw.githubusercontent.com/deliciousbrains/wp-wp-offload-s3-lite/assets/screenshot-2.png)


## Upgrade Notice ##

### 1.1 ###
This is a major change, which ensures S3 URLs are no longer saved in post content. Instead, local URLs are filtered on page generation and replaced with the S3 version. If you depend on the S3 URLs being stored in post content you will need to make modifications to support this version.

### 0.6 ###
This version requires PHP 5.3.3+ and the Amazon Web Services plugin

## Changelog ##

### WP Offload S3 Lite 1.1.6 - 2017-03-13 ###
* New: Compatibility with [Advanced Custom Fields](https://wordpress.org/plugins/advanced-custom-fields/)
* New: `as3cf_filter_post_local_to_s3` and `as3cf_filter_post_s3_to_local` filters added for filtering S3 URLs in custom content
* Improvement: Ensure files uploaded using `media_handle_sideload` have unique filename on S3 when 'Remove Files From Server' enabled
* Bug fix: Files uploaded to S3 with empty filenames when the filename started with non-latin characters
* Bug fix: Audio files with private ACL not working with WordPress's default media player
* Bug fix: S3 API version not passed to S3 client
* Bug fix: Content added to text widgets via the Customizer not saved
* Bug fix: Original file not removed locally when cropped via the Customizer and 'Remove Files From Server' enabled
* Bug fix: Incorrect Media Library URLs saved to the database when WordPress installed in a subdirectory

### WP Offload S3 Lite 1.1.5 - 2017-01-12 ###
* Improvement: Filter custom CSS - S3 URLs will no longer be saved to the database
* Bug fix: PDF previews have incorrect MIME type
* Bug fix: Original PDF not removed from S3 on attachment delete when image previews exist

### WP Offload S3 Lite 1.1.4 - 2016-12-13 ###
* New: Upgrade routine to replace all S3 URLs in post excerpts with local URLs
* Improvement: Performance improvements
* Improvement: Allow expires time to be filtered for private content using the `as3cf_expires` filter
* Bug fix: Image `srcset` not correctly applied when file names contain special characters

### WP Offload S3 Lite 1.1.3 - 2016-11-28 ###
* Bug fix: Private URL signing params stripped in some circumstances
* Improvement: Performance improvements for URL filtering, especially on large sites

### WP Offload S3 Lite 1.1.2 - 2016-11-02 ###
* Improvement: Better content filtering support for third party plugins and themes
* Bug fix: PHP Warning: Division by zero

### WP Offload S3 Lite 1.1.1 - 2016-10-17 ###
* New: Filter post excerpts - S3 URLs will no longer be saved to the database
* Bug fix: PHP 5.3 Fatal error: Using $this when not in object context
* Bug fix: Query string parameters incorrectly encoded for Media Library items

### WP Offload S3 Lite 1.1 - 2016-09-29 ###
* New: Filter post content. S3 URLs will no longer be saved to the database
* New: Upgrade routine to replace all S3 URLs in content with local URLs
* New: Support for theme custom logos
* New: Control the ACL for intermediate image sizes using the `as3cf_upload_acl_sizes` filter
* Bug fix: File names containing special characters double encoded
* Bug fix: `srcset` not working for file names containing special characters
* Bug fix: Incorrect placeholder text for 'Path' option
* Bug fix: Objects in root of bucket not deleted when removed from the Media Library
* Bug fix: No longer use deprecated functions in WordPress 4.6
* Bug fix: Don't delete local file when 'Remove Files From Server' enabled and upload to S3 fails

### WP Offload S3 Lite 1.0.5 - 2016-09-01 ###
* New: Compatibility with WordPress 4.6
* Improvement: No longer delete plugin data on uninstall. Manual removal possible, as per this [doc](https://deliciousbrains.com/wp-offload-s3/doc/uninstall/)

### WP Offload S3 Lite 1.0.4 - 2016-05-30 ###
* New: Now using simpler Force HTTPS setting, removed redundant Always Use HTTP setting
* New: `as3cf_cloudfront_path_parts` filter allows changing served CloudFront path (useful when distribution pulls subdirectory)
* Improvement: Better compatibility with non-standard notices from other plugins and themes
* Improvement: Added basic auth and proxy info to diagnostic info
* Improvement: Added `allow_url_fopen` status to diagnostic info
* Improvement: Added memory usage to diagnostic info
* Improvement: Ensure notice text is 800px or less in width
* Improvement: Reduced database queries on settings screen
* Bug fix: Properly handle _wp_attachment_data metadata when it is a serialized WP_Error

### WP Offload S3 Lite 1.0.3 - 2016-03-23 ###
* Bug fix: Don't replace srcset URLs when Rewrite File URLs option disabled
* Bug fix: Fatal error: Cannot redeclare as3cf_get_secure_attachment_url()

### WP Offload S3 Lite 1.0.2 - 2016-03-08 ###
* Bug fix: Uninstall would run even if pro plugin installed

### WP Offload S3 Lite 1.0.1 - 2016-03-08 ###
* Bug fix: Fatal error on plugin activation
* Bug fix: Unable to activate Pro upgrade

### WP Offload S3 Lite 1.0 - 2016-03-07 ###
* New: Plugin renamed to "WP Offload S3 Lite"
* New: Define any and all settings with a constant in wp-config.php
* New: Documentation links for each setting
* Improvement: Simplified domain setting UI
* Improvement: Far future expiration header set by default
* Improvement: Newly created bucket now immediately appears in the bucket list
* Improvement: Cleanup user meta on uninstall
* Improvement: WP Retina 2x integration removed
* Bug fix: Year/Month folder structure on S3 not created if the 'Organise my uploads into month and year-based folders' WordPress setting is disabled
* Bug fix: Responsive srcset PHP notices
* Bug fix: Compatibility addon notices displayed to non-admin users
* Bug fix: Potential PHP fatal error in MySQL version check in diagnostic log
* Bug fix: Missing image library notices displaying before plugin is setup

### WP Offload S3 0.9.12 - 2016-02-03 ###
* Improvement: Compatibility with WP Offload S3 Assets 1.1
* Bug fix: Object versioned responsive images in post content not working when served from S3 on WordPress 4.4+

### WP Offload S3 0.9.11 - 2015-12-19 ###
* Bug fix: Responsive images in post content not working when served from S3
* Bug fix: Responsive images using wrong image size when there are multiple images with the same width

### WP Offload S3 0.9.10 - 2015-11-26 ###
* Improvement: Support for responsive images in WP 4.4
* Bug fix: Incorrect file path for intermediate image size files uploaded to S3 with no prefix
* Bug fix: Thumbnail previews return 404 error during image edit screen due to character encoding

### WP Offload S3 0.9.9 - 2015-11-12 ###
* Improvement: Improve wording of compatibility notices
* Improvement: Compatibility with Easy Digital Downloads 1.0.1 and WooCommerce 1.0.3 addons
* Improvement: Better determine available memory for background processes
* Bug fix: URL previews incorrect due to stripping `/` characters
* Bug fix: PHP Warning: stream_wrapper_register(): Protocol s3:// is already defined
* Bug fix: PHP Fatal error:  Call to undefined method WP_Error::get()

### WP Offload S3 0.9.8 - 2015-11-02 ###
* Bug fix: Attachment URLs containing query string parameters incorrectly encoded

### WP Offload S3 0.9.7 - 2015-10-26 ###
* Improvement: Improve compatibility with third party plugins when the _Remove Files From Server_ option is enabled
* Improvement: Fix inconsistent spacing on the WP Offload S3 settings screen
* Improvement: Validate _CloudFront or custom domain_ input field
* Improvement: Link to current S3 bucket added to WP Offload S3 settings screen
* Improvement: Show notice when neither GD or Imagick image libraries are not installed
* Improvement: Supply Cache-Control header to S3 when the _Far Future Expiration Header_ option is enabled
* Improvement: Additional information added to _Diagnostic Information_
* Improvement: Added warning when _Remove Files From Server_ option is enabled
* Improvement: Filter added to allow additional image versions to be uploaded to S3
* Bug fix: File size not stored in _wp_attachment_metadata_ when _Remove Files From Server_ option is enabled
* Bug fix: Uploads on Multisite installs allowed after surpassing upload limit
* Bug fix: Site icon in WordPress customizer returns 404
* Bug fix: Image versions remain locally and on S3 after deletion, when the file name contains characters which require escaping
* Bug fix: Files with the same file name overwritten when __Remove Files From Server_ option is enabled
* Bug fix: Cron tasks incorrectly scheduled due to passing the wrong time to `wp_schedule_event`
* Bug fix: Default options not shown in the UI after first install

### WP Offload S3 0.9.6 - 2015-10-01 ###
* Improvement: Update text domains for translate.wordpress.org integration

### WP Offload S3 0.9.5 - 2015-09-01 ###
* Bug fix: Fatal error: Cannot use object of type WP_Error as array

### WP Offload S3 0.9.4 - 2015-08-27 ###
* New: Update all existing attachments with missing file sizes when the 'Remove Files From Server' option is enabled (automatically runs in the background)
* Improvement: Show when constants are used to set bucket and region options
* Improvement: Don't show compatibility notices on plugin update screen
* Improvement: On Multisite installs don't call `restore_current_blog()` on successive loop iterations
* Bug fix: 'Error getting URL preview' alert shown when enter key pressed on settings screen
* Bug fix: Unable to crop header images when the 'Remove Files From Server' option is enabled
* Bug fix: Incorrect storage space shown on Multisite installs when the 'Remove Files From Server' option is enabled
* Bug fix: Upload attempted to non existent bucket when defined by constant
* Bug fix: 'SignatureDoesNotMatch' error shown when using signed URLs with bucket names containing '.' characters

### WP Offload S3 0.9.3 - 2015-08-17 ###
* New: Pro upgrade sidebar
* Bug fix: Create buckets in US standard region causing S3 URLs to 404 errors

### WP Offload S3 0.9.2 - 2015-07-29 ###
* Bug fix: Accidentally released the sidebar for after we launch the pro version

### WP Offload S3 0.9.1 - 2015-07-29 ###
* Improvement: Access denied sample IAM policy replaced with link to [Quick Start Guide](https://deliciousbrains.com/wp-offload-s3/doc/quick-start-guide/)
* Improvement: Access denied messages on bucket selection or bucket creation now link to [Quick Start Guide](https://deliciousbrains.com/wp-offload-s3/doc/quick-start-guide/)
* Improvement: Object expires time can now be filtered using the `as3cf_object_meta` filter
* Bug fix: Error not always shown when S3 bucket inaccessible due to incorrect permissions
* Bug fix: Permission checks fail when S3 bucket is in a non-default region and defined by `AS3CF_BUCKET` constant
* Bug fix: Restore `as3cf_get_attached_file_copy_back_to_local` filter
* Bug fix: Image versions not uploaded to S3 when an edited image is restored
* Bug fix: Original image version not deleted from server when _Remove Files From Server_ option enabled
* Bug fix: Media library items with non-ascii characters in the file name are not removed from S3
* Bug fix: Compatibility notices shown on plugin install pages
* Bug fix: WordPress footer overlaps WP Offload S3 sidebar
* Bug fix: Upon initial setup the settings changed alert shows when no settings have changed

### WP Offload S3 0.9 - 2015-07-08 ###
* New: Plugin rebranded to WP Offload S3
* New: Support tab added to _Offload S3_ screen containing diagnostic information
* New: Compatibility with the [Media Replace](https://wordpress.org/plugins/enable-media-replace/) plugin
* New: Select bucket region when creating a new bucket
* New: Toggle switches redesigned
* Improvement: Compatibility with release candidate of Pro plugin
* Improvement: Example IAM policy more secure
* Improvement: Set default bucket region using the `AS3CF_REGION` constant
* Improvement: Added `as3cf_object_meta` filter for developers
* Improvement: Bucket selection moved to modal window
* Improvement: Don't allow bucket names to contain invalid characters on creation
* Improvement: More verbose error messages on bucket selection
* Improvement: Settings link added to plugin row on _Plugins_ screen
* Improvement: Object versioning enabled by default
* Improvement: Uninstall routines added
* Improvement: JavaScript coding standards
* Improvement: Cache result when checking S3 bucket permissions
* Bug fix: Bucket region errors result in blank WP Offload S3 screen
* Bug fix: Editing an image when _Remove Files From Server_ option is enabled results in error
* Bug fix: Metadata upgrade procedure triggered on new installs
* Bug fix: File URLs when uploaded to a subdirectory result in incorrect S3 URLs
* Bug fix: Errors logged when trying to delete non-existent HiDPI images
* Bug fix: SignatureDoesNotMatch errors on regions with v4 authentication
* Bug fix: Customizer background image not editable
* Bug fix: Error when creating buckets with US Standard region
* Bug fix: Notices appearing incorrectly on some admin screens
* Bug fix: Subsite upload paths repeated on multisite installs
* Bug fix: Handle multisite installs where `BLOG_ID_CURRENT_SITE` is not 1

### WP Offload S3 0.8.2 - 2015-01-31 ###
* New: Input bucket in settings to avoid listing all buckets
* New: Specify bucket with 'AS3CF_BUCKET' constant
* Improvement: Compatibility with beta release of Pro plugin
* Bug Fix: Incorrect file prefix in S3 permission check

### WP Offload S3 0.8.1 - 2015-01-19 ###
* Bug Fix: Permission problems on installs running on EC2s
* Bug Fix: Blank settings page due to WP_Error on S3 permission check
* Bug Fix: Warning: strtolower() expects parameter 1 to be string, object given
* Bug Fix: Region post meta update running on subsites of Multisite installs

### WP Offload S3 0.8 - 2015-01-10 ###
* New: Redesigned settings UI
* Improvement: SSL setting can be fully controlled, HTTPS for urls always, based on request or never
* Improvement: Download files from S3 that are not found on server when running Regenerate Thumbnails plugin
* Improvement: When calling `get_attached_file()` and file is missing from server, return S3 URL
* Improvement: Code cleanup to WordPress coding standards
* Bug Fix: Files for all subsites going into the same S3 folder on multisite installs setup prior to WP 3.5
* Bug Fix: 'attempting to access local file system' error for some installs

### WP Offload S3 0.7.2 - 2014-12-11 ###
* Bug: Some buckets in the EU region causing permission and HTTP errors
* Bug: Undefined variable: message in view/error.php also causing white screens

### WP Offload S3 0.7.1 - 2014-12-05 ###
* Bug: Read-only error on settings page sometimes false positive

### WP Offload S3 0.7 - 2014-12-04 ###
* New: Proper S3 region subdomain in URLs for buckets not in the US Standard region (e.g. https://s3-us-west-2.amazonaws.com/...)
* New: Update all existing attachment meta with bucket region (automatically runs in the background)
* New: Get secure URL for different image sizes (iamzozo)
* New: S3 bucket can be set with constant in wp-config.php (dberube)
* New: Filter for allowing/disallowing file types: `as3cf_allowed_mime_types`
* New: Filter to cancel upload to S3 for any reason: `as3cf_pre_update_attachment_metadata`
* New: Sidebar with email opt-in
* Improvement: Show warning when S3 policy is read-only
* Improvement: Tooltip added to clarify option
* Improvement: Move object versioning option to make it clear it does not require CloudFront
* Improvement: By default only allow file types in `get_allowed_mime_types()` to be uploaded to S3
* Improvement: Compatibility with WPML Media plugin
* Bug Fix: Edited images not removed on S3 when restoring image and IMAGE_EDIT_OVERWRITE true
* Bug Fix: File names with certain characters broken not working
* Bug Fix: Edited image uploaded to incorrect month folder
* Bug Fix: When creating a new bucket the bucket select box appears empty on success
* Bug Fix: SSL not working in regions other than US Standard
* Bug Fix: 'Error uploading' and 'Error removing local file' messages when editing an image
* Bug Fix: Upload and delete failing when bucket is non-US-region and bucket name contains dot
* Bug Fix: S3 file overwritten when file with same name uploaded and local file removed (dataferret)
* Bug Fix: Manually resized images not uploaded (gmauricio)

### WP Offload S3 0.6.1 - 2013-09-21 ###
* WP.org download of Amazon Web Services plugin is giving a 404 Not Found, so directing people to download from Github instead

### WP Offload S3 0.6 - 2013-09-20 ###
* Complete rewrite
* Now requires PHP 5.3.3+
* Now requires the [Amazon Web Services plugin](http://wordpress.org/extend/plugins/amazon-web-services/) which contains the latest PHP libraries from Amazon
* Now works with multisite
* New Option: Custom S3 object path
* New Option: Always serve files over https (SSL)
* New Option: Enable object versioning by appending a timestamp to the S3 file path
* New Option: Remove uploaded file from local filesystem once it has been copied to S3
* New Option: Copy any HiDPI (@2x) images to S3 (works with WP Retina 2x plugin)

### WP Offload S3 0.5 - 2013-01-29 ###
* Forked [Amazon S3 for WordPress with CloudFront](http://wordpress.org/extend/plugins/tantan-s3-cloudfront/)
* Cleaned up the UI to fit with today's WP UI
* Fixed issues causing error messages when WP_DEBUG is on
* [Delete files on S3 when deleting WP attachment](https://github.com/deliciousbrains/wp-amazon-s3-and-cloudfront/commit/e777cd49a4b6999f999bd969241fb24cbbcece60)
* [Added filter to the get_attachment_url function](https://github.com/deliciousbrains/wp-amazon-s3-and-cloudfront/commit/bbe1aed5c2ae900e9ba1b16ba6806c28ab8e2f1c)
* [Added function to get a temporary, secure download URL for private files](https://github.com/deliciousbrains/wp-amazon-s3-and-cloudfront/commit/11f46ec2714d34907009e37ad3b97f4421aefed3)
# Amazon Web Services #
**Contributors:** bradt, deliciousbrains  
**Tags:** amazon, amazon web services  
**Requires at least:** 4.4  
**Tested up to:** 4.7.3  
**Stable tag:** 1.0.2  
**License:** GPLv3  

Houses the Amazon Web Services (AWS) PHP libraries and manages access keys. Required by other AWS plugins.

## Description ##

This plugin is required by other plugins, which use its libraries and its settings to connect to AWS services. Currently, there are only two plugins that require this plugin:

* [WP Offload S3 Lite](http://wordpress.org/plugins/amazon-s3-and-cloudfront/)
* [WP Offload S3](https://deliciousbrains.com/wp-offload-s3/)

### Requirements ###

* PHP version 5.3.3 or greater
* PHP cURL library 7.16.2 or greater
* cURL compiled with OpenSSL and zlib
* curl_multi_exec enabled

## Installation ##

1. Use WordPress' built-in installer
2. A new AWS menu will appear in the side menu

## Screenshots ##

### 1. Settings screen ###
![Settings screen](https://raw.githubusercontent.com/deliciousbrains/wp-amazon-web-services/assets/screenshot-1.png)


## Changelog ##

### 1.0.2 - 2017-03-13 ###
* New: AWS SDK updated to 2.8.31
* New: London and Montreal regions added

### 1.0.1 - 2016-12-13 ###
* New: Mumbai and Seoul regions added

### 1.0 - 2016-09-29 ###
* Improvement: Compatibility with WP Offload S3 Lite 1.1
* Improvement: Compatibility with WP Offload S3 1.2

### 0.3.7 - 2016-09-01 ###
* Improvement: No longer delete plugin data on uninstall. Manual removal possible, as per this [doc](https://deliciousbrains.com/wp-offload-s3/doc/uninstall/).

### 0.3.6 - 2016-05-30 ###
* Improvement: Now checks that the `curl_multi_exec` function is available.

### 0.3.5 - 2016-03-07 ###
* Improvement: Support for `DBI_` prefixed constants to avoid conflicts with other plugins
* Improvement: Redesign of the Addons page
* Improvement: Compatibility with WP Offload S3 Lite 1.0
* Improvement: Compatibility with WP Offload S3 1.1

### 0.3.4 - 2015-11-02 ###
* Improvement: Compatibility with WP Offload S3 Pro 1.0.3

### 0.3.3 - 2015-10-26 ###
* Improvement: Updated Amazon SDK to version 2.8.18
* Improvement: Fix inconsistent notice widths on _Access Keys_ screen
* New: WP Offload S3 Pro addons (Enable Media Replace, Meta Slider, WPML) added to the _Addons_ screen

### 0.3.2 - 2015-08-26 ###
* New: WP Offload S3 Pro upgrade and addons added to the _Addons_ screen

### 0.3.1 - 2015-07-29 ###
* Bug fix: Style inconsistencies on the _Addons_ screen

### 0.3 - 2015-07-08 ###
* New: Support for [IAM Roles on Amazon EC2](https://deliciousbrains.com/wp-offload-s3/doc/iam-roles/) using the `AWS_USE_EC2_IAM_ROLE` constant
* New: Redesigned _Access Keys_ and _Addons_ screens
* Improvement: _Settings_ menu item renamed to _Access Keys_
* Improvement: _Access Keys_ link added to plugin row on _Plugins_ screen
* Improvement: Activate addons directly from within _Addons_ screen
* Improvement: [Quick Start Guide](https://deliciousbrains.com/wp-offload-s3/doc/quick-start-guide/) documentation

### 0.2.2 - 2015-01-19 ###
* Bug Fix: Reverting AWS client config of region and signature

### 0.2.1 - 2015-01-10 ###
* New: AWS SDK updated to 2.7.13
* New: Translation ready
* Improvement: Code cleanup to WordPress coding standards
* Improvement: Settings notice UI aligned with WordPress style
* Bug: Error if migrating keys over from old Amazon S3 and CloudFront plugin settings

### 0.2 - 2014-12-04 ###
* New: AWS SDK updated to 2.6.16
* New: Set the region for the AWS client by defining `AWS_REGION` in your wp-config.php
* New: Composer file for Packagist support
* Improvement: Base plugin class performance of installed version
* Improvement: Base plugin class accessor for various properties
* Improvement: Addon plugin modal now responsive
* Improvement: Better menu icon
* Improvement: Code formatting to WordPress standards

### 0.1 - 2013-09-20 ###
* First release
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
