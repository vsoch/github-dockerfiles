This folder should be empty in source control, except for this file.  This is where generated files such as the celery beat pidfile or the celery beat task database are stored.  Please use it to store any other such generated files so we don't end up with a confusing .gitignore or cluttered clones.
For setup instructions, see the main README.md file of this repository.

Alembic is configured to handle database migrations for the wikimetrics database.  Autogeneration of migrations is supported.  The  general workflow is:

````
$ # make some changes to the models in wikimetrics.models
$ alembic revision --autogenerate -m "Short description of your change"
$ # confirm the file added to database_migrations/versions/ does what you want
$ alembic upgrade head
````

At this point your local database is up to date with your models and the proper alembic scripts have been added.  From a database point of view, you're ready to submit your change.
