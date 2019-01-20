Okay, this is my weird way of doing React development in Django.  It's
been documented elsewhere, but I just wanted to note the steps here so
it's as clear as possible.

To start developing on the JS side, do:

   ./scripts/link.sh

This creates symlinks from this repo's JS files to the react
repository, which are automatically up to date with the sources as
long as you have `make dev` running in the econplayground.js repo.


When you want to update the JS build on production, remove this
symlinks like this:

  git checkout -- .

In the econplayground.js repo, run `make build`. Then do:

  ./scripts/update-build.sh
  git add .
  git commit -m "update js build"
  git push