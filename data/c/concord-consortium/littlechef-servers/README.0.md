



= Steps to spin up a new portal server in aws

TODO: this information was taken from the cc-rails-portal recipe, and needs
to be updated to be more pertenant to LARA.

1. spin up a new RDS database instance
2. make a new s3 bucket to store any portal resources
3. make a new IAM user which the server can use access the s3 buckets
4. put the IAM user in the railsportal group (so they have access to the installer bucket)
5. give the IAM user permissions to access the S3 bucket specific for their resources
6. add this RDS instance to the databags/databases
7. add the S3 credentials to database/s3
8. add a new role for the server instance that has the correct settings for s3 and db
9. spin up a new ec2 instance in aws make sure it is in the same AZ as the RDS for example: if RDS is in us-east-1e then the ec2 instance should also be in us-east-1e
10. allocate a elastic ip for it
11. make sure that your RDS instance allows access from servers in your EC2 instance's security group
12. add a new entry to your .ssh/config for the host or ip address that you'll use to connect to this server
13. use littlechef to provision the new role to it
14. setup a dns entry for this particular machine to make testing easier
15. add a capistrano entry for this instance so its code and db can be updated

= Notes about setting a cc-rails-portal-server

Currently the cc-rails-portal-server uses an AWS RDS database
This is hardcoded in the templates of this cookbook.

It also uses an AWS SES smtp setup. The credentials for this are
pulled from variables somewhere...
talk to Scott to get them if you need them.
We currently only have the ability to send to concord.org email addresses through AWS SES.

It currently is using override_attributes in rails-portal-server role but it seems like it shouldn't need
to. I think there is a bug in littlechefs precedence implementation.

= We have to modify the default size of the max_allowed_packet for our RDS when importing data.

* see: http://www.eaglegenomics.com/2010/11/changing-mysql-db-parameter-on-amazon-rds-instance/
* see: http://www.liferay.com/web/guest/community/forums/-/message_boards/message/124969

<pre><code>
 rds-create-db-parameter-group bigger_max_packet --description="increase max_packet size for rites tables" --engine=MySQL5.1

 rds-create-db-parameter-group ritesportal -d "increase max_packet size for rites tables" -f mysql5.1

 rds-modify-db-parameter-group ritesportal -p "name=max_allowed_packet,value=16777216, method=immediate"

 rds-modify-db-instance rites-staging --db-parameter-group-name=ritesportal

 rds-reboot-db-instance rites-staging
<pre></code>

= Moving production data to the EC2 instance:

  <pre></code>
  mysqldump -u $DB_USER -p$DB_PASSWORD --lock-tables=false --add-drop-table --quick --extended-insert $DATABASE_NAME | mysql -C -h $RDS_NAME.$RDS_DOMAIN.us-east-1.rds.amazonaws.com -u $RDS_USER -p$RDS_PASSWORD portal
  <pre></code>

  Before running this you'll need to add the database host to the security group of the RDS instance.

= Moving production resource page attachements to AWS:

  <pre></code>
  s3cmd put --acl-public --recursive attachments s3://$BUCKET_NAME/
  <pre></code>

  If these attachments were used in activities as image links, then all of those references will need to be updated with the new url. Here is some sample code for doing this:
  - Embeddable::Xhtml.all.each{|xhtml| xhtml.content = xhtml.content.gsub(/interactions\.portal\.concord\.org\/system/, 's3.amazonaws.com/interactions-production'); xhtml.save!}; nil
  - Embeddable::VideoPlayer.all.each{|vp| next if vp.video_url.nil?; vp.video_url = vp.video_url.sub(/interactions\.portal\.concord\.org\/system/, 's3.amazonaws.com/interactions-production'); vp.save!}; nil
  - Embeddable::VideoPlayer.all.each{|vp| next if vp.image_url.nil?; vp.image_url = vp.image_url.sub(/interactions\.portal\.concord\.org\/system/, 's3.amazonaws.com/interactions-production'); vp.save!}; nil
  - Embeddable::DrawingTool.all.each{|dt| next if dt.background_image_url.nil?; dt.background_image_url = dt.background_image_url.sub(/interactions\.portal\.concord\.org\/system/, 's3.amazonaws.com/interactions-production'); dt.save!};nil

= Things to backup

* built installers
* uploaded resources. Paperclip, rails 3 and S3: http://doganberktas.com/2010/09/14/amazon-s3-and-paperclip-rails-3/
* sparks-content? I think this a checkout from github so it doesn't need to be backedup

= Things not to backup

* log this can be recovered by stoping frozen server and mounting its file system
* nces_data this is downloaded and used once so it doesn't need to be backed up
* rinet-data this is downloaded on a schedule, put in the database and then not looked at again.
* system this is only used by paperclip which is handled above
* otrunk-examples this is not really used


= Steps to spin up a new portal server in aws

1. spin up a new RDS database instance
2. make a new s3 bucket to store any portal resources
3. make a new IAM user which the server can use access the s3 buckets
4. put the IAM user in the railsportal group (so they have access to the installer bucket)
5. give the IAM user permissions to access the S3 bucket specific for their resources
6. add this RDS instance to the databags/databases
7. add the S3 credentials to database/s3
8. add a new role for the server instance that has the correct settings for s3 and db
9. spin up a new ec2 instance in aws make sure it is in the same AZ as the RDS for example: if RDS is in us-east-1e then the ec2 instance should also be in us-east-1e
10. allocate a elastic ip for it
11. make sure that your RDS instance allows access from servers in your EC2 instance's security group
12. add a new entry to your .ssh/config for the host or ip address that you'll use to connect to this server
13. use littlechef to provision the new role to it
14. setup a dns entry for this particular machine to make testing easier
15. add a capistrano entry for this instance so its code and db can be updated

= Notes about setting a cc-rails-portal-server

Currently the cc-rails-portal-server uses an AWS RDS database
This is hardcoded in the templates of this cookbook.

It also uses an AWS SES smtp setup. The credentials for this are
pulled from variables somewhere...
talk to Scott to get them if you need them.
We currently only have the ability to send to concord.org email addresses through AWS SES.

It currently is using override_attributes in rails-portal-server role but it seems like it shouldn't need
to. I think there is a bug in littlechefs precedence implementation.

= We have to modify the default size of the max_allowed_packet for our RDS when importing data.
 
* see: http://www.eaglegenomics.com/2010/11/changing-mysql-db-parameter-on-amazon-rds-instance/
* see: http://www.liferay.com/web/guest/community/forums/-/message_boards/message/124969

<pre><code>
 rds-create-db-parameter-group bigger_max_packet --description="increase max_packet size for rites tables" --engine=MySQL5.1

 rds-create-db-parameter-group ritesportal -d "increase max_packet size for rites tables" -f mysql5.1
 
 rds-modify-db-parameter-group ritesportal -p "name=max_allowed_packet,value=16777216, method=immediate"
 
 rds-modify-db-instance rites-staging --db-parameter-group-name=ritesportal
 
 rds-reboot-db-instance rites-staging
<pre></code>

= Moving production data to the EC2 instance:
  
  <pre></code>
  mysqldump -u $DB_USER -p$DB_PASSWORD --lock-tables=false --add-drop-table --quick --extended-insert $DATABASE_NAME | mysql -C -h $RDS_NAME.$RDS_DOMAIN.us-east-1.rds.amazonaws.com -u $RDS_USER -p$RDS_PASSWORD portal
  <pre></code>

  Before running this you'll need to add the database host to the security group of the RDS instance.

= Moving production resource page attachements to AWS:

  <pre></code>
  s3cmd put --acl-public --recursive attachments s3://$BUCKET_NAME/
  <pre></code>

  If these attachments were used in activities as image links, then all of those references will need to be updated with the new url. Here is some sample code for doing this:
  - Embeddable::Xhtml.all.each{|xhtml| xhtml.content = xhtml.content.gsub(/interactions\.portal\.concord\.org\/system/, 's3.amazonaws.com/interactions-production'); xhtml.save!}; nil
  - Embeddable::VideoPlayer.all.each{|vp| next if vp.video_url.nil?; vp.video_url = vp.video_url.sub(/interactions\.portal\.concord\.org\/system/, 's3.amazonaws.com/interactions-production'); vp.save!}; nil
  - Embeddable::VideoPlayer.all.each{|vp| next if vp.image_url.nil?; vp.image_url = vp.image_url.sub(/interactions\.portal\.concord\.org\/system/, 's3.amazonaws.com/interactions-production'); vp.save!}; nil
  - Embeddable::DrawingTool.all.each{|dt| next if dt.background_image_url.nil?; dt.background_image_url = dt.background_image_url.sub(/interactions\.portal\.concord\.org\/system/, 's3.amazonaws.com/interactions-production'); dt.save!};nil

= Things to backup

* built installers
* uploaded resources. Paperclip, rails 3 and S3: http://doganberktas.com/2010/09/14/amazon-s3-and-paperclip-rails-3/
* sparks-content? I think this a checkout from github so it doesn't need to be backedup

= Things not to backup

* log this can be recovered by stoping frozen server and mounting its file system
* nces_data this is downloaded and used once so it doesn't need to be backed up
* rinet-data this is downloaded on a schedule, put in the database and then not looked at again.
* system this is only used by paperclip which is handled above
* otrunk-examples this is not really used


