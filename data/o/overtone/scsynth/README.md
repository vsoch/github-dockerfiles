[![Clojars Project](https://img.shields.io/clojars/v/overtone/scsynth.svg)](https://clojars.org/overtone/scsynth) [![Clojars Project](https://img.shields.io/clojars/v/overtone/scsynth-extras.svg)](https://clojars.org/overtone/scsynth-extras)

# This repository hosts the native os-specific library files of libscsynth and sc-plugins for overtone

Linux notes:
libscsynth needs libsndfile which in turn needs ogg/flac etc,
java-jna and java-jni can only provide shared libraries that they
load themselves. To help jna to load libscsynth, other than loading
each .so file individually, to set rpath to libscsynth and libsndfile,
this will work fine and in parallel to LD_LIBRARY_PATH.
JACK(libjack) still needs to be installed.

```
patchelf --set-rpath native/linux/x86_64 native/linux/x86_64/libsndfile.so.1
patchelf --set-rpath native/linux/x86_64 native/linux/x86_64/libscsynth.so
patchelf --set-rpath native/linux/x86_64 native/linux/x86_64/plugins/DiskIO_UGens.so

# scsynth-extras files:
patchelf --set-rpath native/linux/x86_64 native/linux/x86_64/plugins/PitchDetection.so
patchelf --set-rpath native/linux/x86_64 native/linux/x86_64/plugins/NCAnalysisUGens.so

```

NixOs notes:
if you're running on NixOs, you'll most likely encounter
```
java.lang.UnsatisfiedLinkError: libjack.so.0: cannot open shared object file: No such file or directory
```
you'll need to install libjack globally
```
nix-env -i libjack2
```
then and add your user-local lib directory to LD_LIBRARY_PATH (for example in ~/.bashrc)
```
export LD_LIBRARY_PATH=~/.nix-profile/lib:$LD_LIBRARY_PATH
```

patchelf useage:
  --set-rpath <rpath> <file-location>
  --set-soname <new-soname> <file-location>
  --replace-needed <new-dep-name> <old-dep-name> <file-location>
  
