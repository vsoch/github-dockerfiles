django-mailman is a simple way to manage one or more mailman mailing lists which are not installed on your server.
It uses the webinterface to subscribe or unsubscribe a mailinglist member.
Additional you are able to request a list of all subscribed members for a specific mailing list.

==Requirements==

`django-mailman` is tested and works with mailman version 2.1.5.
It's possible that mailman also works with the 2.1.x series, but I guess it wouldn't work with the 3.x series which is under development at the moment

`django-mailman` requires Django 1.0 or later.

==Configuration==

First of all, you must add this project to your list of `INSTALLED_APPS` in `settings.py`:

{{{
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    ...
    'django_mailman',
    ...
)
}}}

Run `manage.py syncdb`.  This creates the appropriate tables in your database that are necessary for operation.

==Usage==

from django_mailman.models import List

===Create new List===

list_name = 'testlist'
list_pwd = 'pwd'
list_email = 'testlist@mydomain.com'
list_url = 'http://mailman.listdomain.com'
list_encoding = 'iso-8859-1' # must match the encoding of your mailman installation

list = List(name=list_name, password=list_pwd, email=list_email,
    main_url=list_url, encoding=list_encoding)

===Subscribe new member===

list.subscribe('membername@maildomain.com', 'first-name', 'last-name')

===Unsubscribe member===

list.unsubscribe('membername@maildomain.com')

===Show a list of all subscribed members===

list.get_all_members()

This method will return a list of all members in the following format:
[[u'first-name last-name', u'membername@maildomain.com']]

===Admin Moderation Url===

If you would like to provide some functionality to log into your mailman moderation area you could request the complete url from your list.

list.get_admin_moderation_url()
Running via Docker
=================

```
docker run -t -i \
  -v /path/lot/local/settings/folder:/config \
  -e LOCAL_SETTINGS=/config/local_settings.py \
  quay.io/acmuiuc/liquid
```
