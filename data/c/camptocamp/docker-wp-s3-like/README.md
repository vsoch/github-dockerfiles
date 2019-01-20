# Summary

Wordpress docker image containing plugins to store media files on a S3-like bucket.
Note that this is just for testing purpose and some operations must be done
manually on the first run of the container.


# Build the image

To create the image, execute the following command in the docker-wp-s3-like folder.

    docker build -t camptocamp/wp-s3-like:1.0 .


# Setup

First go to the wordpress page and as requested setup an username and password for
the administrator.

Next, the keys for accessing the S3 storage must be entered in the *wp-config.php*
file. Entries are already setup in the end of the file with empty values. Just set
the right values for DBI_AWS_ACCESS_KEY_ID and DBI_AWS_SECRET_ACCESS_KEY. This can
be done into a docker console. Note that *vim* and *emacs* are already installed in
this image.

Then, the following plugins must be enabled manually.

 - Amazon Web Service
 - WP Offload S3 Lite
 - S3-Like Storage Endpoint

To do this, login into Wordpress as an administrator and go to "Plugins -> Installed plugins".

Finally, you can choose or create a new bucket to store the media files. You can do
this under "AWS -> S3 and CloudFront" settings page.
