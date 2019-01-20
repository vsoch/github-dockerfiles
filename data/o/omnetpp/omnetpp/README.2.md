Build with:

$ docker build -t omnetpp/distrobuild-base:ubuntu18.04-macos11-180705 .
Copy here

 - the 'tools' directory containing the Windows and macOS toolchains (i.e. in ./tools/170717/...)
 - 'omnetpp-repo' bare repository as a base to be able to pre-load and cache maven artifacts.
   $ git clone -n REPO_URL omnetpp

NOTE: you need to rebuild this image whenever the Windows/macOS toolchain or Eclipse is updated

build the image with:

$ docker build -t omnetpp/distrobuild:eclipse480-tools180301-181214 .
