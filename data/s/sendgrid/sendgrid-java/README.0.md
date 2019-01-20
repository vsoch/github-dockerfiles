![SendGrid Logo](https://uiux.s3.amazonaws.com/2016-logos/email-logo%402x.png)

This folder contains various examples on using the ACCESS_SETTINGS endpoint of SendGrid with Java:

* [Retrieve a list of currently whitelisted IPs (GET /access_settings/whitelist)](GetAccessSettings.java)
* [Retrieve a specific whitelisted IP (GET /access_settings/whitelist/{rule_id})](GetIPFromAccessSettings.java)
* [Retrieve a list of currently whitelisted IPs (GET /access_settings/whitelist)](GetAccessSettingsActivity.java)
* [Remove a specific IP from the whitelist (DELETE /access_settings/whitelist/{rule_id}](DeleteIPFromAccessSettings.java)
* [Remove one or more IPs from the whitelist (DELETE /access_settings/whitelist)](DeleteAccessSettings.java)
* [Add one or more IPs to the whitelist (POST /access_settings/whitelist)](CreateAccessSettings.java)
![SendGrid Logo](https://uiux.s3.amazonaws.com/2016-logos/email-logo%402x.png)

This folder contains various examples on using the Mail Settings endpoint of SendGrid with Java:

* [Retrieve all mail settings (GET /mail_settings)](GetAllMailSettings.java)
* [Retrieve address whitelist mail settings (GET /mail_settings/address_whitelist)](GetAddressWhitelistMailSettings.java)
* [Retrieve all BCC mail settings (GET /mail_settings/bcc)](GetBCCMailSettings.java)
* [Retrieve bounce purge mail settings (GET /mail_settings/bounce_purge)](GetBouncePurgeMailSettings.java)
* [Retrieve footer mail settings (GET /mail_settings/footer)](GetFooterMailSettings.java)
* [Retrieve forward bounce mail settings (GET /mail_settings/forward_bounce)](GetForwardBounceMailSettings.java)
* [Retrieve forward spam mail settings (GET /mail_settings/forward_spam)](GetForwardSpamMailSettings.java)
* [Retrieve plain content mail settings (GET /mail_settings/plain_content)](GetPlainContentMailSettings.java)
* [Retrieve spam check mail settings (GET /mail_settings/spam_check)](GetSpamCheckMailSettings.java)
* [Retrieve legacy template mail settings (GET /mail_settings/template)](GetTemplateMailSettings.java)
* [Update address whitelist mail settings (PATCH /mail_settings/address_whitelist)](UpdateAddressWhitelist.java)
* [Update BCC mail settings (PATCH /mail_settings/bcc)](UpdateBCCMailSettings.java)
* [Update bounce purge mail settings (PATCH /mail_settings/bounce_purge)](UpdateBouncePurgeMailSettings.java)
* [Update footer mail settings (PATCH /mail_settings/footer)](UpdateFooterMailSettings.java)
* [Update forward bounce mail settings (PATCH /mail_settings/forward_bounce)](UpdateForwardBounceMailSettings.java)
* [Update forward spam mail settings (PATCH /mail_settings/forward_spam)](UpdateForwardSpamMailSettings.java)
* [Update plain content mail settings (PATCH /mail_settings/plain_content)](UpdatePlainContentMailSettings.java)
* [Update spam check mail settings (PATCH /mail_settings/spam_check)](UpdateSpamCheckMailSettings.java)
* [Update template mail settings (PATCH /mail_settings/template)](UpdateTemplateMailSettings.java)
![SendGrid Logo](https://uiux.s3.amazonaws.com/2016-logos/email-logo%402x.png)

This folder contains various examples on using the IPs endpoint of SendGrid with Java:

* [Retrieve all IP addresses (GET /ips)](RetrieveAllIPs.java)
* [Retrieve all assigned IPs (GET /ips/assigned)](RetrieveAssignedIPs.java)
* [Create an IP pool (POST /ips/pools)](CreatePool.java)
* [Retrieve all IP pools (GET /ips/pools)](RetrieveAllPools.java)
* [Update an IP pools name (PUT /ips/pools/{pool_name})](UpdatePoolName.java)
* [Retrieve all IPs in a specified pool (GET /ips/pools/{pool_name})](RetrieveIPsInPool.java)
* [Delete an IP pool. (DELETE /ips/pools/{pool_name})](DeletePool.java)
* [Add an IP address to a pool (POST /ips/pools/{pool_name}/ips)](AddToPool.java)
* [Remove an IP address from a pool (DELETE /ips/pools/{pool_name}/ips/{ip}](RemoveFromPool.java)
* [Add an IP to warmup (POST /ips/warmup)](AddToWarmup.java)
* [Retrieve all IPs currently in warmup (GET /ips/warmup)](RetrieveIPsInWarmup.java)
* [Retrieve warmup status for a specific IP address (GET /ips/warmup/{ip_address})](RetrieveWarmupStatus.java)
* [Remove an IP from warmup (DELETE /ips/warmup/{ip_address})](RemoveFromWarmup.java)
* [Retrieve all IP pools an IP address belongs to (GET /ips/{ip_address})](RetrievePoolsForIP.java)![SendGrid Logo](https://uiux.s3.amazonaws.com/2016-logos/email-logo%402x.png)

This folder contains various examples on using the SUPPRESSION endpoint of SendGrid with Java:

* [Retrieve all blocks (GET /suppression/blocks)](GetAllBlocks.java)
* [Delete blocks (DELETE /suppression/blocks)](DeleteBlocks.java)
* [Retrieve a specific block (GET /suppression/blocks/{email})](GetSpecificBlock.java)
* [Delete a specific block (DELETE /suppression/blocks/{email})](DeleteSpecificBlock.java)
* [Retrieve all bounces (GET /suppression/bounces)](GetAllBounces.java)
* [Delete bounces (DELETE /suppression/bounces)](DeleteBounces.java)
* [Retrieve a Bounce (GET /suppression/bounces/{email})](GetBounce.java)
* [Delete a bounce (DELETE /suppression/bounces/{email})](DeleteBounce.java)
* [Retrieve all invalid emails (GET /suppression/invalid_emails)](GetAllInvalidEmails.java)
* [Delete invalid emails (DELETE /suppression/invalid_emails)](DeleteInvalidEmails.java)
* [Retrieve a specific invalid email (GET /suppression/invalid_emails/{email})](GetSpecificInvalidEmail.java)
* [Delete a specific invalid email (DELETE /suppression/invalid_emails/{email})](DeleteSpecificInvalidEmail.java)
* [Retrieve a specific spam report (GET /suppression/spam_report/{email})](GetSpecificSpamReport.java)
* [Delete a specific spam report (DELETE /suppression/spam_report/{email})](DeleteSpecificSpamReport.java)
* [Retrieve all spam reports (GET /suppression/spam_reports)](GetAllSpamReports.java)
* [Delete spam reports (DELETE /suppression/spam_reports)](DeleteSpamReports.java)
* [Retrieve all global suppressions (GET /suppression/unsubscribes)](GetAllGlobalSuppressions.java)**This helper allows you to quickly and easily build a Mail object for sending email through SendGrid.**

## Dependencies

- [Jackson](https://github.com/FasterXML/jackson)

# Quick Start

Run the [example](https://github.com/sendgrid/sendgrid-java/tree/master/examples/mail) (make sure you have set your environment variable to include your SENDGRID_API_KEY).

```bash
cd examples/mail
javac -classpath ../../build/libs/sendgrid-4.2.1-jar.jar:. Example.java && java -classpath ../examples/jackson-core-2.9.5.jar:../../build/libs/sendgrid-4.1.0-jar.jar:. Example
```

## Usage

- See the [example](https://github.com/sendgrid/sendgrid-java/tree/master/examples/mail) for a complete working example.
- [Documentation](https://sendgrid.com/docs/API_Reference/Web_API_v3/Mail/overview.html)**This helper allows you to quickly and easily build a Mail object for sending email through SendGrid.**

## Dependencies

- [Jackson](https://github.com/FasterXML/jackson)

# Quick Start

Run the [example](https://github.com/sendgrid/sendgrid-java/tree/master/examples/mail) (make sure you have set your environment variable to include your SENDGRID_API_KEY).

```bash
cd examples/mail
javac -classpath ../../build/libs/sendgrid-4.2.1-jar.jar:. Example.java && java -classpath ../examples/jackson-core-2.9.5.jar:../../build/libs/sendgrid-4.1.0-jar.jar:. Example
```

## Usage

- See the [example](https://github.com/sendgrid/sendgrid-java/tree/master/examples/mail) for a complete working example.
- [Documentation](https://sendgrid.com/docs/API_Reference/Web_API_v3/Mail/overview.html)# Supported tags and respective `Dockerfile` links
 - `v1.0.0`, `latest` [(Dockerfile)](https://github.com/sendgrid/sendgrid-java/blob/master/docker/Dockerfile)

# Quick reference
Due to Oracle's JDK license, you must build this Docker image using the official Oracle image located in the Docker Store. You will need a Docker store account. Once you have an account, you must accept the Oracle license [here](https://store.docker.com/images/oracle-serverjre-8). On the command line, type `docker login` and provide your credentials. You may then build the image using this command `docker build -t sendgrid/sendgrid-java -f Dockerfile .`

 - **Where to get help:**
   [Contact SendGrid Support](https://support.sendgrid.com/hc/en-us)

 - **Where to file issues:**
   https://github.com/sendgrid/sendgrid-java/issues

 - **Where to get more info:**
   [USAGE.md](https://github.com/sendgrid/sendgrid-java/blob/master/docker/USAGE.md)

 - **Maintained by:**
   [SendGrid Inc.](https://sendgrid.com)

# Usage examples
 - Most recent version: `docker run -it sendgrid/sendgrid-java`.
 - Your own fork:
   ```sh-session
   $ git clone https://github.com/you/cool-sendgrid-java.git
   $ realpath cool-sendgrid-java
   /path/to/cool-sendgrid-java
   $ docker run -it -v /path/to/cool-sendgrid-java:/mnt/sendgrid-java sendgrid/sendgrid-java
   ```

For more detailed information, see [USAGE.md](https://github.com/sendgrid/sendgrid-java/blob/master/docker/USAGE.md).

# About

sendgrid-java is guided and supported by the SendGrid [Developer Experience Team](mailto:dx@sendgrid.com).

sendgrid-java is maintained and funded by SendGrid, Inc. The names and logos for sendgrid-java are trademarks of SendGrid, Inc.

![SendGrid Logo](https://uiux.s3.amazonaws.com/2016-logos/email-logo%402x.png)
