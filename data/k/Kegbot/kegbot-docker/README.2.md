# Kegbot Server Docker Container

A container that runs the Kegbot application server (gunicorn) and
task queue (Celery).

## Environment Variables

* `KEGBOT_DEBUG`: If present and evalutes to `True`, enables `DEBUG` mode in
  Kegbot settings.  Default: `False`.

