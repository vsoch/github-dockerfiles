Low Level Virtual Machine (LLVM)
================================

This directory and its subdirectories contain source code for LLVM,
a toolkit for the construction of highly optimized compilers,
optimizers, and runtime environments.

LLVM is open source software. You may freely distribute it under the terms of
the license agreement found in LICENSE.txt.

Please see the documentation provided in docs/ for further
assistance with LLVM, and in particular docs/GettingStarted.rst for getting
started with LLVM and docs/README.txt for an overview of LLVM's
documentation setup.

If you are writing a package for LLVM, see docs/Packaging.rst for our
suggestions.

# Kylin
based on llvm 5.0.1 release with ollvm, include `clang` `libcxx` `libcxxabi`, support `Objc` `NDK` and more.

wiki: [obfuscator-wiki](https://github.com/obfuscator-llvm/obfuscator/wiki)

### Build

```shell
$ git clone Kylin https://github.com/exorxw/Kylin-llvm-obfuscator.git
$ mkdir build
$ cd build
$ cmake -DCMAKE_BUILD_TYPE=Release ../Kylin/
$ make -j7
```

When the build is finished, you should have all the binaries in build/bin.

### Usage

 * `-fla` for the control flow flattening pass
 * `-sub` for the instruction substitution pass
 * `-bcf` for the bogus control flow pass

you can add your obfuscation flags to the CXXFLAGS or CFLAGS

------------------
```ruby
@INPROCEEDINGS{ieeespro2015-JunodRWM,
  author={Pascal Junod and Julien Rinaldini and Johan Wehrli and Julie Michielin},
  booktitle={Proceedings of the {IEEE/ACM} 1st International Workshop on Software Protection, {SPRO'15}, Firenze, Italy, May 19th, 2015},
  editor = {Brecht Wyseur},
  publisher = {IEEE},
  title={Obfuscator-{LLVM} -- Software Protection for the Masses},
  year={2015},
  pages={3--9},
  doi={10.1109/SPRO.2015.10},
}
```
