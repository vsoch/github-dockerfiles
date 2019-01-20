This is where all the public-facing web stuff goes.

The www folder is where your document root should point, everything else
is not for public consumption. Note the Makefile, which creates a tmp folder
for temporary files and a templates/cache folder for use by Smarty.

Local configuration options, such as storage passwords and API identifiers for
remote services Flickr, Amazon S3, and Cloudmade, can be found in lib/init.php

You'll want to run `make` before you do anything else.
Normally, getting Modest Maps images into PHP means running a Python daemon
with ws-compose. This is an effort to close that loop, initially for Walking Papers.
This is where the heavy offline image editing happens.

poll.py is what you actually run, check the usage instructions like this:

    python poll.py --help

Note the Makefile, which grabs an implementation of SIFT and a copy
of the Modest Maps python port.

You'll want to run `make` before you do anything else.
page.php here is used by ../cairoutils.py to generate PDFs with lossily-compressed
JPEG images, something that Cairo itself does not know how to do. They are otherwise
identical to PDFs that might be generated with pycairo directly, but much smaller.  
Place licensed copies of `Helvetica.ttf` and `Helvetica-Bold.ttf` here.
BlobDetector is a minimal implementation of two-pass connected component
labeling for simple images:
    http://en.wikipedia.org/wiki/Blob_extraction#Two-pass
