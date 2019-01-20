ContentTranslation is a tool that allows editors to translate pages from
one language to another with the help of machine translation and other
translation tools.

This is deployment repository of server component of ContentTranslation.

Layout
------
* config.yaml - symlink to src/config.dev.yaml file.

* node_modules - node.js dependencies, updated with ``npm install``.

* package.json - symlink to src/package.json file.

* scap - Configuration files for WMF production deployment.

* src - cxserver js code as submodule.

How to
------

Update
======
To update node_modules:

```
npm install
```

To update src to latest cxserver master:

```
git submodule -q foreach git pull -q origin master
```

If checking out first time, do:

```
git submodule init
```

```
git submodule update --init --recursive
```

Submit changes
==============
Do not directly submit changes other than in scap directory, which is used for
production configuration update in WMF.

To update cxserver/deploy, use following command in cxserver repository. This
will automatically submit change in Gerrit.

```
./server.js build --deploy-repo --force --review
```
