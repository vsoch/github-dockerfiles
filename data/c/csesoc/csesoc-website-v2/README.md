# csesoc-website-v2

## Developing

#### Dependencies
You will need

- OpenLDAP
- [pipenv](https://github.com/pypa/pipenv). Pipenv takes care of installing and managing Python dependencies.

#### Pre-Running
**Set Envvars**
You will need to set the environment vars for local development

```
cp .env.example.sh .env.sh
vim .env.sh

# Add envvars to the local environment
source .env.sh
```

**Initialize the DB**
The database for the website is stored in `data/soc-website.db` so we only need to run syncdb
```bash
$ sqlite3 data/soc-website.db < initial.sql
```

#### Running
```
pipenv run python manage.py runserver
```

## Building & Pushing a New Container
```
# Build the container
docker build -t csesoc/soc-website-v2

# Push the container
docker push csesoc/soc-website-v2
```

## Deployment
This project is setup for deployment in a Docker Container.

### Volumes:
 - `/app/data`: Data directory for the app. Contains media & sqlite db

### Ports:
The container exposes the server on port 8080.

### Environment:
You need to specify the environment vars outlined in `.env.example.sh`

```
# Run the container
docker run --rm -it --name soc-website -p 8080:8080 \
  -v $PWD/data:/app/data \
  -e SECRET_KEY="" \
  -e NEVERCACHE_KEY="" \
  -e STRIPE_PKEY="" \
  -e STRIPE_SKEY="" \
  csesoc/soc-website-v2
```

## Using the CMS front end

### How to log in
If you're not connected to uniwide, anything you type in the log in field will make you log in as admin. If you're on uniwide, you need to make your own users.

### Editing the front end
When you log in as admin, you can see that you can edit things directly from the front end. To add a new page, go to [localhost:8000/admin](localhost:8000/admin). There's a really nice interface which is more or less intiutive to use. Keep in mind that any changes you make here won't be added to the git repo (it saves on your local database).
 
### Features that don't work locally
Some features of the website won't work locally because they require a user key or something similar. The following features are:
* LDAP Authentication
* Teams
* Timetable importer

## Using the Django back end
PSA: Use 4 space SPACE INDENTATION! This is Python! Whitespace is important!

You can do most things through the front end now that we're using Mezzanine, but if you need any complicated features, you still need to use the back end. The easiest way to get start is to go through a [Django tutorial](https://docs.djangoproject.com/en/dev/intro/tutorial01). Otherwise, here's a rough rundown of how to add a new feature to the website.

### Registering the feature
In the app/ folder, add a folder with the app name. In that file, add a file called \_\_init__.py (just leave it empty). Open up settings.py and got to
```python
INSTALLED_APPS = (
    'app.theme',
    'app.sponsors',
    ...
)
```
and add the line:
```python
INSTALLED_APPS = (
    'app.theme',
    'app.<app_name>',
    ...
)
```
### Creating database table
```bash
$ python manage.py schemamigration <app_name> initial --initial
```
This should create a new folder in app/<app_name>/ called migrations and a new file called 0001_initial.py. In that file, you need to add the fields in. It should look something like:
```python
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'Feature'
        db.create_table(u'merch_hoodie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('field1', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('field2', self.gf('django.db.models.fields.DecimalField')(max_length=8)),
            ('field3', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'feature', ['Feature'])

    def backwards(self, orm):
        # Deleting model 'Feature'
        db.delete_table(u'feature')

    models = {
        u'app.feature': {
            'Meta': {'object_name': 'Feature'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'field1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'field2': ('django.db.models.fields.DecimalField', [], {'max_length': '8'}),
            'field3': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
        }
    }

    complete_apps = ['feature']
)
```
PSA: PLEASE SPECIFY A BACKWARDS METHOD
To run the migration, run:
```bash
$ python manage.py migrate <app_name>
```
### Adding models
In the folder app/<app_name>/, add a file called models.py. It should look like this:
```python
from django.db import models

class Feature(models.Model):
   fiedl1 = models.CharField(max_length=100)
   field2 = models.DecimalField(max_length=8)
   field3 = models.EmailField(max_length=75)
```
### Adding views
In the folder app/<app_name>/, add a file called views.py. It should look like this:
```python
from django.shortcuts import render_to_response, redirect
from models import Feature
from django.template import RequestContext

def method(request):
    if request.method == 'POST':
        # Do stuff with POST request
        return render_to_response('feature/post.html', context_instance=RequestContext(request))
    else:
        # Do stuff with GET request
        return redirect('/feature')
```
The first argument of render_to_response points to a template in app/theme/templates/. So make a folder called <app_name> in app/theme/templates/ and add a html template. It should look like:
```html
{% extends 'base.html' %}

{% block meta_title %}Page Title{% endblock %}

{% block main %}

<!-- CONTENT HERE -->

{% endblock %}
```
### Adding routing
Open up urls.py and go to the tuple:
```python
urlpatterns = patterns("",
    url(r'^signin/?$', direct_to_template, {'template': 'auth/login.html'}, name='signin'),
    url(r'^zlogin/?$', 'app.auth.views.signin'),
    ...
```
You need to add a path to which the page can be accessed. Something like:
```python
urlpatterns = patterns("",
    url(r'^signin/?$', direct_to_template, {'template': 'auth/login.html'}, name='signin'),
    url(r'^zlogin/?$', 'app.auth.views.signin'),
    url(r'^featyre/?$', 'app.feature.views.method'),
    ...
```
```

### Adding an admin page:
In the folder app/<app_name>/, add a file called admin.py. It should look like this:
```python
from django.contrib import admin
from app.feature.models import Feature

class FeatureAdmin(admin.ModelAdmin):
    list_filter = ('field1','field2','field3')
    list_display = ('field1','field2','field3')

admin.site.register(Feature, FeatureAdmin)

```
### Adding tests
In the folder app/<app_name>/, add a file called test.py. It should look like this:
```python
from django.test import TestCase

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
```
To run tests, run:
```bash
$ python manage.py test
```
