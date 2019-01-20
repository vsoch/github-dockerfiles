This directory & related items are for temporary demo purposes.  If they somehow manage to find their
way into your branch, feel free to remove them:
 - templates (this directory)
 - urls.py: url(r'^one-shot-demo/?$', login_required(OneShotImportDemoView.as_view()))
 - views.py: OneShotImportDemoView
 This directory is used to store static assets for your project. User media files
(FileFields/ImageFields) are not stored here.

The convention for this directory is:

 * css/ — stores CSS files
 * js/ — stores Javascript files
 * img/ — stores image files
