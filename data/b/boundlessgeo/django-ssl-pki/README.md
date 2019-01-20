# Django SSL/PKI

- Source: https://github.com/boundlessgeo/django-ssl-pki

## Description

Adds custom SSL/PKI configurations to Django applications.

## Requirements

- Django > 1.8.x, < 2.0.0
- Python = 2.7.x
- django-ordered-model = 1.4.3

See [requirements.txt](requirements.txt) for other dependencies.

## Installation

- Install the package with pip install django-exchange-pki
- Add `ordered_model` and `ssl_pki` to the `INSTALLED_APPS` in your `settings.py`
- Add to your project's `urls.py` (after `urlpatterns` defined):
  ```python
  if 'ssl_pki' in settings.INSTALLED_APPS:
      from ssl_pki.urls import urlpatterns as ssl_pki_urls
      urlpatterns += ssl_pki_urls
  ```
- Run `python manage.py migrate` to create the required tables
- Run `python manage.py collectstatic`

## Setting Options

 - `PKI_DIRECTORY = /some/path/to/directory` where PKI components for SSL configurations are stored on disk.
 - `ENFORCE_MAX_LENGTH = integer` Force max length validation on encrypted password fields, e.g. password for PKI private key, as stored in Django database.
- `SSL_DEFAULT_CONFIG = {"name": "Default: TLS-only", ...}` (TODO: add settings.py override first)
 
## How It Works

TODO: describe pattern matching and `requests` SSL adapter

## Project Integration

TODO: describe app API usage
README.rst