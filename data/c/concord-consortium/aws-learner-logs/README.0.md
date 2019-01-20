# AWS Learner Logs

## Components

### Converter

The `converter` folder contains a set of scripts to convert the Postgres log data to gzipped .json files on S3.

Here are the setup steps to use the scripts:

1. You don't need to clear existing data in the `aws-log-manager/processed-logs` bucket/folder in S3 as any existing files will be overwritten (and files created via the Kinesis Firehose will remain)
2. Provision $80 Node.js Lightsail box as "log-manager-import" in us-east-1.
4. ssh into Lighsail box via web admin
    - `sudo apt-get install postgresql postgresql-contrib`
    - `sudo -i -u postgres`
    - `psql`
    - `\password postgres` (set to password for postgres user to "postgres")
    - `\q` (quits psql)
    - `createdb log_manager`
    - `exit`  (should now be "bitnami" again)
    - `sudo snap install heroku --classic`
    - `heroku login` (then login as your user)
    - `heroku pg:backups:capture --app cc-log-manager`
    - `heroku pg:backups:download --app cc-log-manager`
    - `pg_restore --verbose --clean --jobs=2 --no-acl --no-owner -h   localhost -U postgres -d log_manager latest.dump`
    - WAIT A LONG TIME (1 HOUR?)
    - `git clone https://github.com/concord-consortium/aws-learner-logs`
    - `cd aws-learner-logs`
    - `npm install`
    - create `.env` file in `aws-learner-logs` (see contents below)
    - TODO: add section about attaching storage and setting symlink to `processed-logs`
    - `cd converter`
    - `node ./create-json.js` (this will create files in `./processed-logs`)
    - WAIT ABOUT 1 MINUTE PER 1 MILLION ROWS
    - `node ./create-gz.js` (this will upload the files to S3)
5. Delete Lightsail instance

### Site

The site is a express app that presents a simple json based query interface copied from the existing log manager.  The site is login protected using OAuth login to the portal.  You must be an admin on the portal to use the app once logged in.

### .env file

This file contains a set of environment variables defaults.  You can either create this file with the appropriate variables and values or just set the environent variables before invoking either the converter scripts or starting the site up.

```
SITE_PORT=5000
SITE_SESSION_SECRET=<ENTER RANDOM STRING HERE>

AWS_ACCESS_KEY_ID=<ENTER KEY HERE>
AWS_SECRET_ACCESS_KEY=<ENTER SECRET KEY HERE>
AWS_DEFAULT_REGION=us-east-1

SITE_ROOT_URL=https://aws-learner-logs.concord.org/

PORTAL_ROOT_URL=https://learn.concord.org/
PORTAL_AUTH_CLIENT_ID=<ENTER PORTAL CLIENT ID HERE>
PORTAL_AUTH_CLIENT_SECRET=<ENTER PORTAL CLIENT SECRET HERE>

ATHENA_OUTPUT_BUCKET=aws-athena-query-results-612297603577-us-east-1
ATHENA_OUTPUT_FOLDER=aws-learner-logs
```


