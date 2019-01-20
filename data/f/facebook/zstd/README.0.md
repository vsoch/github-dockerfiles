Zstandard library : usage examples
==================================

- [Simple compression](simple_compression.c) :
  Compress a single file.
  Introduces usage of : `ZSTD_compress()`

- [Simple decompression](simple_decompression.c) :
  Decompress a single file.
  Only compatible with simple compression.
  Result remains in memory.
  Introduces usage of : `ZSTD_decompress()`

- [Multiple simple compression](multiple_simple_compression.c) :
  Compress multiple files (in simple mode) in a single command line.
  Demonstrates memory preservation technique that
  minimizes malloc()/free() calls by re-using existing resources.
  Introduces usage of : `ZSTD_compressCCtx()`

- [Streaming memory usage](streaming_memory_usage.c) :
  Provides amount of memory used by streaming context.
  Introduces usage of : `ZSTD_sizeof_CStream()`

- [Streaming compression](streaming_compression.c) :
  Compress a single file.
  Introduces usage of : `ZSTD_compressStream()`

- [Multiple Streaming compression](multiple_streaming_compression.c) :
  Compress multiple files (in streaming mode) in a single command line.
  Introduces memory usage preservation technique,
  reducing impact of malloc()/free() and memset() by re-using existing resources.

- [Streaming decompression](streaming_decompression.c) :
  Decompress a single file compressed by zstd.
  Compatible with both simple and streaming compression.
  Result is sent to stdout.
  Introduces usage of : `ZSTD_decompressStream()`

- [Dictionary compression](dictionary_compression.c) :
  Compress multiple files using the same dictionary.
  Introduces usage of : `ZSTD_createCDict()` and `ZSTD_compress_usingCDict()`

- [Dictionary decompression](dictionary_decompression.c) :
  Decompress multiple files using the same dictionary.
  Result remains in memory.
  Introduces usage of : `ZSTD_createDDict()` and `ZSTD_decompress_usingDDict()`
Command Line Interface for Zstandard library
============================================

Command Line Interface (CLI) can be created using the `make` command without any additional parameters.
There are however other Makefile targets that create different variations of CLI:
- `zstd` : default CLI supporting gzip-like arguments; includes dictionary builder, benchmark, and support for decompression of legacy zstd formats
- `zstd_nolegacy` : Same as `zstd` but without support for legacy zstd formats
- `zstd-small` : CLI optimized for minimal size; no dictionary builder, no benchmark, and no support for legacy zstd formats
- `zstd-compress` : version of CLI which can only compress into zstd format
- `zstd-decompress` : version of CLI which can only decompress zstd format


#### Compilation variables
`zstd` scope can be altered by modifying the following `make` variables :

- __HAVE_THREAD__ : multithreading is automatically enabled when `pthread` is detected.
  It's possible to disable multithread support, by setting `HAVE_THREAD=0`.
  Example : `make zstd HAVE_THREAD=0`
  It's also possible to force multithread support, using `HAVE_THREAD=1`.
  In which case, linking stage will fail if neither `pthread` nor `windows.h` library can be found.
  This is useful to ensure this feature is not silently disabled.

- __ZSTD_LEGACY_SUPPORT__ : `zstd` can decompress files compressed by older versions of `zstd`.
  Starting v0.8.0, all versions of `zstd` produce frames compliant with the [specification](../doc/zstd_compression_format.md), and are therefore compatible.
  But older versions (< v0.8.0) produced different, incompatible, frames.
  By default, `zstd` supports decoding legacy formats >= v0.4.0 (`ZSTD_LEGACY_SUPPORT=4`).
  This can be altered by modifying this compilation variable.
  `ZSTD_LEGACY_SUPPORT=1` means "support all formats >= v0.1.0".
  `ZSTD_LEGACY_SUPPORT=2` means "support all formats >= v0.2.0", and so on.
  `ZSTD_LEGACY_SUPPORT=0` means _DO NOT_ support any legacy format.
  if `ZSTD_LEGACY_SUPPORT >= 8`, it's the same as `0`, since there is no legacy format after `7`.
  Note : `zstd` only supports decoding older formats, and cannot generate any legacy format.

- __HAVE_ZLIB__ : `zstd` can compress and decompress files in `.gz` format.
  This is ordered through command `--format=gzip`.
  Alternatively, symlinks named `gzip` or `gunzip` will mimic intended behavior.
  `.gz` support is automatically enabled when `zlib` library is detected at build time.
  It's possible to disable `.gz` support, by setting `HAVE_ZLIB=0`.
  Example : `make zstd HAVE_ZLIB=0`
  It's also possible to force compilation with zlib support, `using HAVE_ZLIB=1`.
  In which case, linking stage will fail if `zlib` library cannot be found.
  This is useful to prevent silent feature disabling.

- __HAVE_LZMA__ : `zstd` can compress and decompress files in `.xz` and `.lzma` formats.
  This is ordered through commands `--format=xz` and `--format=lzma` respectively.
  Alternatively, symlinks named `xz`, `unxz`, `lzma`, or `unlzma` will mimic intended behavior.
  `.xz` and `.lzma` support is automatically enabled when `lzma` library is detected at build time.
  It's possible to disable `.xz` and `.lzma` support, by setting `HAVE_LZMA=0` .
  Example : `make zstd HAVE_LZMA=0`
  It's also possible to force compilation with lzma support, using `HAVE_LZMA=1`.
  In which case, linking stage will fail if `lzma` library cannot be found.
  This is useful to prevent silent feature disabling.

- __HAVE_LZ4__ : `zstd` can compress and decompress files in `.lz4` formats.
  This is ordered through commands `--format=lz4`.
  Alternatively, symlinks named `lz4`, or `unlz4` will mimic intended behavior.
  `.lz4` support is automatically enabled when `lz4` library is detected at build time.
  It's possible to disable `.lz4` support, by setting `HAVE_LZ4=0` .
  Example : `make zstd HAVE_LZ4=0`
  It's also possible to force compilation with lz4 support, using `HAVE_LZ4=1`.
  In which case, linking stage will fail if `lz4` library cannot be found.
  This is useful to prevent silent feature disabling.

- __BACKTRACE__ : `zstd` can display a stack backtrace when execution
  generates a runtime exception. By default, this feature may be
  degraded/disabled on some platforms unless additional compiler directives are
  applied. When triaging a runtime issue, enabling this feature can provide
  more context to determine the location of the fault.
  Example : `make zstd BACKTRACE=1`


#### Aggregation of parameters
CLI supports aggregation of parameters i.e. `-b1`, `-e18`, and `-i1` can be joined into `-b1e18i1`.


#### Symlink shortcuts
It's possible to invoke `zstd` through a symlink.
When the name of the symlink has a specific value, it triggers an associated behavior.
- `zstdmt` : compress using all cores available on local system.
- `zcat` : will decompress and output target file using any of the supported formats. `gzcat` and `zstdcat` are also equivalent.
- `gzip` : if zlib support is enabled, will mimic `gzip` by compressing file using `.gz` format, removing source file by default (use `--keep` to preserve). If zlib is not supported, triggers an error.
- `xz` : if lzma support is enabled, will mimic `xz` by compressing file using `.xz` format, removing source file by default (use `--keep` to preserve). If xz is not supported, triggers an error.
- `lzma` : if lzma support is enabled, will mimic `lzma` by compressing file using `.lzma` format, removing source file by default (use `--keep` to preserve). If lzma is not supported, triggers an error.
- `lz4` : if lz4 support is enabled, will mimic `lz4` by compressing file using `.lz4` format. If lz4 is not supported, triggers an error.
- `unzstd` and `unlz4` will decompress any of the supported format.
- `ungz`, `unxz` and `unlzma` will do the same, and will also remove source file by default (use `--keep` to preserve).


#### Dictionary builder in Command Line Interface
Zstd offers a training mode, which can be used to tune the algorithm for a selected
type of data, by providing it with a few samples. The result of the training is stored
in a file selected with the `-o` option (default name is `dictionary`),
which can be loaded before compression and decompression.

Using a dictionary, the compression ratio achievable on small data improves dramatically.
These compression gains are achieved while simultaneously providing faster compression and decompression speeds.
Dictionary work if there is some correlation in a family of small data (there is no universal dictionary).
Hence, deploying one dictionary per type of data will provide the greater benefits.
Dictionary gains are mostly effective in the first few KB. Then, the compression algorithm
will rely more and more on previously decoded content to compress the rest of the file.

Usage of the dictionary builder and created dictionaries with CLI:

1. Create the dictionary : `zstd --train PathToTrainingSet/* -o dictionaryName`
2. Compress with the dictionary: `zstd FILE -D dictionaryName`
3. Decompress with the dictionary: `zstd --decompress FILE.zst -D dictionaryName`


#### Benchmark in Command Line Interface
CLI includes in-memory compression benchmark module for zstd.
The benchmark is conducted using given filenames. The files are read into memory and joined together.
It makes benchmark more precise as it eliminates I/O overhead.
Multiple filenames can be supplied, as multiple parameters, with wildcards,
or names of directories can be used as parameters with `-r` option.

The benchmark measures ratio, compressed size, compression and decompression speed.
One can select compression levels starting from `-b` and ending with `-e`.
The `-i` parameter selects minimal time used for each of tested levels.


#### Usage of Command Line Interface
The full list of options can be obtained with `-h` or `-H` parameter:
```
Usage :
      zstd [args] [FILE(s)] [-o file]

FILE    : a filename
          with no FILE, or when FILE is - , read standard input
Arguments :
 -#     : # compression level (1-19, default: 3)
 -d     : decompression
 -D file: use `file` as Dictionary
 -o file: result stored into `file` (only if 1 input file)
 -f     : overwrite output without prompting and (de)compress links
--rm    : remove source file(s) after successful de/compression
 -k     : preserve source file(s) (default)
 -h/-H  : display help/long help and exit

Advanced arguments :
 -V     : display Version number and exit
 -v     : verbose mode; specify multiple times to increase verbosity
 -q     : suppress warnings; specify twice to suppress errors too
 -c     : force write to standard output, even if it is the console
 -l     : print information about zstd compressed files
--ultra : enable levels beyond 19, up to 22 (requires more memory)
--long  : enable long distance matching (requires more memory)
--no-dictID : don't write dictID into header (dictionary compression)
--[no-]check : integrity check (default: enabled)
 -r     : operate recursively on directories
--format=gzip : compress files to the .gz format
--format=xz : compress files to the .xz format
--format=lzma : compress files to the .lzma format
--test  : test compressed file integrity
--[no-]sparse : sparse mode (default: disabled)
 -M#    : Set a memory usage limit for decompression
--      : All arguments after "--" are treated as files

Dictionary builder :
--train ## : create a dictionary from a training set of files
--train-cover[=k=#,d=#,steps=#,split=#] : use the cover algorithm with optional args
--train-fastcover[=k=#,d=#,f=#,steps=#,split=#,accel=#] : use the fastcover algorithm with optional args
--train-legacy[=s=#] : use the legacy algorithm with selectivity (default: 9)
 -o file : `file` is dictionary name (default: dictionary)
--maxdict=# : limit dictionary to specified size (default: 112640)
--dictID=# : force dictionary ID to specified value (default: random)

Benchmark arguments :
 -b#    : benchmark file(s), using # compression level (default: 3)
 -e#    : test all compression levels from -bX to # (default: 1)
 -i#    : minimum evaluation time in seconds (default: 3s)
 -B#    : cut file into independent blocks of size # (default: no block)
--priority=rt : set process priority to real-time
```

#### Restricted usage of Environment Variables
Using environment variables to set compression/decompression parameters has security implications. Therefore,
we intentionally restrict its usage. Currently, only `ZSTD_CLEVEL` is supported for setting compression level.
If the value of `ZSTD_CLEVEL` is not a valid integer, it will be ignored with a warning message.
Note that command line options will override corresponding environment variable settings.

#### Long distance matching mode
The long distance matching mode, enabled with `--long`, is designed to improve
the compression ratio for files with long matches at a large distance (up to the
maximum window size, `128 MiB`) while still maintaining compression speed.

Enabling this mode sets the window size to `128 MiB` and thus increases the memory
usage for both the compressor and decompressor. Performance in terms of speed is
dependent on long matches being found. Compression speed may degrade if few long
matches are found. Decompression speed usually improves when there are many long
distance matches.

Below are graphs comparing the compression speed, compression ratio, and
decompression speed with and without long distance matching on an ideal use
case: a tar of four versions of clang (versions `3.4.1`, `3.4.2`, `3.5.0`,
`3.5.1`) with a total size of `244889600 B`. This is an ideal use case as there
are many long distance matches within the maximum window size of `128 MiB` (each
version is less than `128 MiB`).

Compression Speed vs Ratio | Decompression Speed
---------------------------|---------------------
![Compression Speed vs Ratio](https://raw.githubusercontent.com/facebook/zstd/v1.3.3/doc/images/ldmCspeed.png "Compression Speed vs Ratio") | ![Decompression Speed](https://raw.githubusercontent.com/facebook/zstd/v1.3.3/doc/images/ldmDspeed.png "Decompression Speed")

| Method | Compression ratio | Compression speed | Decompression speed  |
|:-------|------------------:|-------------------------:|---------------------------:|
| `zstd -1`   | `5.065`   | `284.8 MB/s`  | `759.3 MB/s`  |
| `zstd -5`  | `5.826`    | `124.9 MB/s`  | `674.0 MB/s`  |
| `zstd -10` | `6.504`    | `29.5 MB/s`   | `771.3 MB/s`  |
| `zstd -1 --long` | `17.426` | `220.6 MB/s` | `1638.4 MB/s` |
| `zstd -5 --long` | `19.661` | `165.5 MB/s` | `1530.6 MB/s`|
| `zstd -10 --long`| `21.949` | `75.6 MB/s` | `1632.6 MB/s`|

On this file, the compression ratio improves significantly with minimal impact
on compression speed, and the decompression speed doubles.

On the other extreme, compressing a file with few long distance matches (such as
the [Silesia compression corpus]) will likely lead to a deterioration in
compression speed (for lower levels) with minimal change in compression ratio.

The below table illustrates this on the [Silesia compression corpus].

[Silesia compression corpus]: http://sun.aei.polsl.pl/~sdeor/index.php?page=silesia

| Method | Compression ratio | Compression speed | Decompression speed  |
|:-------|------------------:|------------------:|---------------------:|
| `zstd -1`        | `2.878` | `231.7 MB/s`      | `594.4 MB/s`   |
| `zstd -1 --long` | `2.929` | `106.5 MB/s`      | `517.9 MB/s`   |
| `zstd -5`        | `3.274` | `77.1 MB/s`       | `464.2 MB/s`   |
| `zstd -5 --long` | `3.319` | `51.7 MB/s`       | `371.9 MB/s`   |
| `zstd -10`       | `3.523` | `16.4 MB/s`       | `489.2 MB/s`   |
| `zstd -10 --long`| `3.566` | `16.2 MB/s`       | `415.7 MB/s`   |


#### zstdgrep

`zstdgrep` is a utility which makes it possible to `grep` directly a `.zst` compressed file.
It's used the same way as normal `grep`, for example :
`zstdgrep pattern file.zst`

`zstdgrep` is _not_ compatible with dictionary compression.

To search into a file compressed with a dictionary,
it's necessary to decompress it using `zstd` or `zstdcat`,
and then pipe the result to `grep`. For example  :
`zstdcat -D dictionary -qc -- file.zst | grep pattern`
Zstandard library files
================================

The __lib__ directory is split into several sub-directories,
in order to make it easier to select or exclude features.


#### Building

`Makefile` script is provided, supporting [Makefile conventions](https://www.gnu.org/prep/standards/html_node/Makefile-Conventions.html#Makefile-Conventions),
including commands variables, staged install, directory variables and standard targets.
- `make` : generates both static and dynamic libraries
- `make install` : install libraries and headers in target system directories

`libzstd` default scope is pretty large, including compression, decompression, dictionary builder,
and support for decoding legacy formats >= v0.5.0.
The scope can be reduced on demand (see paragraph _modular build_).


#### Multithreading support

Multithreading is disabled by default when building with `make`.
Enabling multithreading requires 2 conditions :
- set build macro `ZSTD_MULTITHREAD` (`-DZSTD_MULTITHREAD` for `gcc`)
- for POSIX systems : compile with pthread (`-pthread` compilation flag for `gcc`)

Both conditions are automatically applied when invoking `make lib-mt` target.

When linking a POSIX program with a multithreaded version of `libzstd`,
note that it's necessary to request the `-pthread` flag during link stage.

Multithreading capabilities are exposed
via the [advanced API defined in `lib/zstd.h`](https://github.com/facebook/zstd/blob/v1.3.8/lib/zstd.h#L592).
This API is still labelled experimental,
but is expected to become "stable" in the near future.


#### API

Zstandard's stable API is exposed within [lib/zstd.h](zstd.h).


#### Advanced API

Optional advanced features are exposed via :

- `lib/common/zstd_errors.h` : translates `size_t` function results
                               into a `ZSTD_ErrorCode`, for accurate error handling.

- `ZSTD_STATIC_LINKING_ONLY` : if this macro is defined _before_ including `zstd.h`,
                          it unlocks access to the experimental API,
                          exposed in the second part of `zstd.h`.
                          All definitions in the experimental APIs are unstable,
                          they may still change in the future, or even be removed.
                          As a consequence, experimental definitions shall ___never be used with dynamic library___ !
                          Only static linking is allowed.


#### Modular build

It's possible to compile only a limited set of features within `libzstd`.
The file structure is designed to make this selection manually achievable for any build system :

- Directory `lib/common` is always required, for all variants.

- Compression source code lies in `lib/compress`

- Decompression source code lies in `lib/decompress`

- It's possible to include only `compress` or only `decompress`, they don't depend on each other.

- `lib/dictBuilder` : makes it possible to generate dictionaries from a set of samples.
        The API is exposed in `lib/dictBuilder/zdict.h`.
        This module depends on both `lib/common` and `lib/compress` .

- `lib/legacy` : makes it possible to decompress legacy zstd formats, starting from `v0.1.0`.
        This module depends on `lib/common` and `lib/decompress`.
        To enable this feature, define `ZSTD_LEGACY_SUPPORT` during compilation.
        Specifying a number limits versions supported to that version onward.
        For example, `ZSTD_LEGACY_SUPPORT=2` means : "support legacy formats >= v0.2.0".
        Conversely, `ZSTD_LEGACY_SUPPORT=0` means "do __not__ support legacy formats".
        By default, this build macro is set as `ZSTD_LEGACY_SUPPORT=5`.
        Decoding supported legacy format is a transparent capability triggered within decompression functions.
        It's also allowed to invoke legacy API directly, exposed in `lib/legacy/zstd_legacy.h`.
        Each version does also provide its own set of advanced API.
        For example, advanced API for version `v0.4` is exposed in `lib/legacy/zstd_v04.h` .

- While invoking `make libzstd`, it's possible to define build macros
        `ZSTD_LIB_COMPRESSION, ZSTD_LIB_DECOMPRESSION`, `ZSTD_LIB_DICTBUILDER`,
        and `ZSTD_LIB_DEPRECATED` as `0` to forgo compilation of the corresponding features.
        This will also disable compilation of all dependencies
        (eg. `ZSTD_LIB_COMPRESSION=0` will also disable dictBuilder).

- There are some additional build macros that can be used to minify the decoder.

  Zstandard often has more than one implementation of a piece of functionality,
  where each implementation optimizes for different scenarios. For example, the
  Huffman decoder has complementary implementations that decode the stream one
  symbol at a time or two symbols at a time. Zstd normally includes both (and
  dispatches between them at runtime), but by defining `HUF_FORCE_DECOMPRESS_X1`
  or `HUF_FORCE_DECOMPRESS_X2`, you can force the use of one or the other, avoiding
  compilation of the other. Similarly, `ZSTD_FORCE_DECOMPRESS_SEQUENCES_SHORT`
  and `ZSTD_FORCE_DECOMPRESS_SEQUENCES_LONG` force the compilation and use of
  only one or the other of two decompression implementations. The smallest
  binary is achieved by using `HUF_FORCE_DECOMPRESS_X1` and
  `ZSTD_FORCE_DECOMPRESS_SEQUENCES_SHORT`.

  For squeezing the last ounce of size out, you can also define
  `ZSTD_NO_INLINE`, which disables inlining, and `ZSTD_STRIP_ERROR_STRINGS`,
  which removes the error messages that are otherwise returned by
  `ZSTD_getErrorName`.


#### Windows : using MinGW+MSYS to create DLL

DLL can be created using MinGW+MSYS with the `make libzstd` command.
This command creates `dll\libzstd.dll` and the import library `dll\libzstd.lib`.
The import library is only required with Visual C++.
The header file `zstd.h` and the dynamic library `dll\libzstd.dll` are required to
compile a project using gcc/MinGW.
The dynamic library has to be added to linking options.
It means that if a project that uses ZSTD consists of a single `test-dll.c`
file it should be linked with `dll\libzstd.dll`. For example:
```
    gcc $(CFLAGS) -Iinclude/ test-dll.c -o test-dll dll\libzstd.dll
```
The compiled executable will require ZSTD DLL which is available at `dll\libzstd.dll`.


#### Deprecated API

Obsolete API on their way out are stored in directory `lib/deprecated`.
At this stage, it contains older streaming prototypes, in `lib/deprecated/zbuff.h`.
These prototypes will be removed in some future version.
Consider migrating code towards supported streaming API exposed in `zstd.h`.


#### Miscellaneous

The other files are not source code. There are :

 - `BUCK` : support for `buck` build system (https://buckbuild.com/)
 - `Makefile` : `make` script to build and install zstd library (static and dynamic)
 - `README.md` : this file
 - `dll/` : resources directory for Windows compilation
 - `libzstd.pc.in` : script for `pkg-config` (used in `make install`)
ZSTD Windows binary package
====================================

#### The package contents

- `zstd.exe`                  : Command Line Utility, supporting gzip-like arguments
- `dll\libzstd.dll`           : The ZSTD dynamic library (DLL)
- `dll\libzstd.lib`           : The import library of the ZSTD dynamic library (DLL) for Visual C++
- `example\`                  : The example of usage of the ZSTD library
- `include\`                  : Header files required by the ZSTD library
- `static\libzstd_static.lib` : The static ZSTD library (LIB)


#### Usage of Command Line Interface

Command Line Interface (CLI) supports gzip-like arguments.
By default CLI takes an input file and compresses it to an output file:
```
    Usage: zstd [arg] [input] [output]
```
The full list of commands for CLI can be obtained with `-h` or `-H`. The ratio can
be improved with commands from `-3` to `-16` but higher levels also have slower
compression. CLI includes in-memory compression benchmark module with compression
levels starting from `-b` and ending with `-e` with iteration time of `-i` seconds.
CLI supports aggregation of parameters i.e. `-b1`, `-e18`, and `-i1` can be joined
into `-b1e18i1`.


#### The example of usage of static and dynamic ZSTD libraries with gcc/MinGW

Use `cd example` and `make` to build `fullbench-dll` and `fullbench-lib`.
`fullbench-dll` uses a dynamic ZSTD library from the `dll` directory.
`fullbench-lib` uses a static ZSTD library from the `lib` directory.


#### Using ZSTD DLL with gcc/MinGW

The header files from `include\` and the dynamic library `dll\libzstd.dll`
are required to compile a project using gcc/MinGW.
The dynamic library has to be added to linking options.
It means that if a project that uses ZSTD consists of a single `test-dll.c`
file it should be linked with `dll\libzstd.dll`. For example:
```
    gcc $(CFLAGS) -Iinclude\ test-dll.c -o test-dll dll\libzstd.dll
```
The compiled executable will require ZSTD DLL which is available at `dll\libzstd.dll`.


#### The example of usage of static and dynamic ZSTD libraries with Visual C++

Open `example\fullbench-dll.sln` to compile `fullbench-dll` that uses a
dynamic ZSTD library from the `dll` directory. The solution works with Visual C++
2010 or newer. When one will open the solution with Visual C++ newer than 2010
then the solution will upgraded to the current version.


#### Using ZSTD DLL with Visual C++

The header files from `include\` and the import library `dll\libzstd.lib`
are required to compile a project using Visual C++.

1. The path to header files should be added to `Additional Include Directories` that can
   be found in project properties `C/C++` then `General`.
2. The import library has to be added to `Additional Dependencies` that can
   be found in project properties `Linker` then `Input`.
   If one will provide only the name `libzstd.lib` without a full path to the library
   the directory has to be added to `Linker\General\Additional Library Directories`.

The compiled executable will require ZSTD DLL which is available at `dll\libzstd.dll`.
### Summary

`adapt` is a new compression tool targeted at optimizing performance across network connections and pipelines. The tool is aimed at sensing network speeds and adapting compression level based on network or pipe speeds.
In situations where the compression level does not appropriately match the network/pipe speed, compression may be bottlenecking the entire pipeline or the files may not be compressed as much as they potentially could be, therefore losing efficiency. It also becomes quite impractical to manually measure and set an optimalcompression level (which could potentially change over time). 

### Using `adapt`

In order to build and use the tool, you can simply run `make adapt` in the `adaptive-compression` directory under `contrib`. This will generate an executable available for use. Another possible method of installation is running `make install`, which will create and install the binary as the command `zstd-adaptive`.

Similar to many other compression utilities, `zstd-adaptive` can be invoked by using the following format:

`zstd-adaptive [options] [file(s)]`

Supported options for the above format are described below. 

`zstd-adaptive` also supports reading from `stdin` and writing to `stdout`, which is potentially more useful. By default, if no files are given, `zstd-adaptive` reads from and writes to standard I/O. Therefore, you can simply insert it within a pipeline like so:

`cat FILE | zstd-adaptive | ssh "cat - > tmp.zst"`

If a file is provided, it is also possible to force writing to stdout using the `-c` flag like so:

`zstd-adaptive -c FILE | ssh "cat - > tmp.zst"`

Several options described below can be used to control the behavior of `zstd-adaptive`. More specifically, using the `-l#` and `-u#` flags will will set upper and lower bounds so that the compression level will always be within that range. The `-i#` flag can also be used to change the initial compression level. If an initial compression level is not provided, the initial compression level will be chosen such that it is within the appropriate range (it becomes equal to the lower bound). 

### Options
`-oFILE` : write output to `FILE`

`-i#`    : provide initial compression level (must within the appropriate bounds)

`-h`     : display help/information

`-f`     : force the compression level to stay constant

`-c`     : force write to `stdout`

`-p`     : hide progress bar

`-q`     : quiet mode -- do not show progress bar or other information

`-l#`    : set a lower bound on the compression level (default is 1)

`-u#`    : set an upper bound on the compression level (default is 22)
### Benchmarking / Test results
#### Artificial Tests
These artificial tests were run by using the `pv` command line utility in order to limit pipe speeds (25 MB/s read and 5 MB/s write limits were chosen to mimic severe throughput constraints). A 40 GB backup file was sent through a pipeline, compressed, and written out to a file. Compression time, size, and ratio were computed. Data for `zstd -15` was excluded from these tests because the test runs quite long.

<table>
<tr><th> 25 MB/s read limit </th></tr>
<tr><td>

| Compressor Name | Ratio | Compressed Size | Compression Time |
|:----------------|------:|----------------:|-----------------:| 
| zstd -3         | 2.108 |       20.718 GB |      29m 48.530s |
| zstd-adaptive   | 2.230 |       19.581 GB |      29m 48.798s |

</td><tr>
</table>

<table>
<tr><th> 5 MB/s write limit </th></tr>
<tr><td>

| Compressor Name | Ratio | Compressed Size | Compression Time |
|:----------------|------:|----------------:|-----------------:| 
| zstd -3         | 2.108 |       20.718 GB |   1h 10m 43.076s |
| zstd-adaptive   | 2.249 |       19.412 GB |   1h 06m 15.577s |

</td></tr>
</table>

The commands used for this test generally followed the form:

`cat FILE | pv -L 25m -q | COMPRESSION | pv -q > tmp.zst # impose 25 MB/s read limit`

`cat FILE | pv -q | COMPRESSION | pv -L 5m -q > tmp.zst  # impose 5 MB/s write limit`

#### SSH Tests

The following tests were performed by piping a relatively large backup file (approximately 80 GB) through compression and over SSH to be stored on a server. The test data includes statistics for time and compressed size  on `zstd` at several compression levels, as well as `zstd-adaptive`. The data highlights the potential advantages that `zstd-adaptive` has over using a low static compression level and the negative imapcts that using an excessively high static compression level can have on
pipe throughput.

| Compressor Name | Ratio | Compressed Size | Compression Time |
|:----------------|------:|----------------:|-----------------:|
| zstd -3         | 2.212 |       32.426 GB |   1h 17m 59.756s |
| zstd -15        | 2.374 |       30.213 GB |   2h 56m 59.441s |
| zstd-adaptive   | 2.315 |       30.993 GB |   1h 18m 52.860s |

The commands used for this test generally followed the form: 

`cat FILE | COMPRESSION | ssh dev "cat - > tmp.zst"`
## Project Support Notice

The VS2005 Project directory has been moved to the contrib directory in order to indicate that it will no longer be supported.
largeNbDicts
=====================

`largeNbDicts` is a benchmark test tool
dedicated to the specific scenario of
dictionary decompression using a very large number of dictionaries.
When dictionaries are constantly changing, they are always "cold",
suffering from increased latency due to cache misses.

The tool is created in a bid to investigate performance for this scenario,
and experiment mitigation techniques.

Command line :
```
largeNbDicts [Options] filename(s)

Options :
-r           : recursively load all files in subdirectories (default: off)
-B#          : split input into blocks of size # (default: no split)
-#           : use compression level # (default: 3)
-D #         : use # as a dictionary (default: create one)
-i#          : nb benchmark rounds (default: 6)
--nbDicts=#  : set nb of dictionaries to # (default: one per block)
-h           : help (this text)
```
# Parallel Zstandard (PZstandard)

Parallel Zstandard is a Pigz-like tool for Zstandard.
It provides Zstandard format compatible compression and decompression that is able to utilize multiple cores.
It breaks the input up into equal sized chunks and compresses each chunk independently into a Zstandard frame.
It then concatenates the frames together to produce the final compressed output.
Pzstandard will write a 12 byte header for each frame that is a skippable frame in the Zstandard format, which tells PZstandard the size of the next compressed frame.
PZstandard supports parallel decompression of files compressed with PZstandard.
When decompressing files compressed with Zstandard, PZstandard does IO in one thread, and decompression in another.

## Usage

PZstandard supports the same command line interface as Zstandard, but also provides the `-p` option to specify the number of threads.
Dictionary mode is not currently supported.

Basic usage

    pzstd input-file -o output-file -p num-threads -#          # Compression
    pzstd -d input-file -o output-file -p num-threads          # Decompression

PZstandard also supports piping and fifo pipes

    cat input-file | pzstd -p num-threads -# -c > /dev/null

For more options

    pzstd --help

PZstandard tries to pick a smart default number of threads if not specified (displayed in `pzstd --help`).
If this number is not suitable, during compilation you can define `PZSTD_NUM_THREADS` to the number of threads you prefer.

## Benchmarks

As a reference, PZstandard and Pigz were compared on an Intel Core i7 @ 3.1 GHz, each using 4 threads, with the [Silesia compression corpus](http://sun.aei.polsl.pl/~sdeor/index.php?page=silesia).

Compression Speed vs Ratio with 4 Threads | Decompression Speed with 4 Threads
------------------------------------------|-----------------------------------
![Compression Speed vs Ratio](images/Cspeed.png "Compression Speed vs Ratio") | ![Decompression Speed](images/Dspeed.png "Decompression Speed")

The test procedure was to run each of the following commands 2 times for each compression level, and take the minimum time.

    time pzstd -# -p 4    -c silesia.tar     > silesia.tar.zst
    time pzstd -d -p 4    -c silesia.tar.zst > /dev/null

    time pigz  -# -p 4 -k -c silesia.tar     > silesia.tar.gz
    time pigz  -d -p 4 -k -c silesia.tar.gz  > /dev/null

PZstandard was tested using compression levels 1-19, and Pigz was tested using compression levels 1-9.
Pigz cannot do parallel decompression, it simply does each of reading, decompression, and writing on separate threads.

## Tests

Tests require that you have [gtest](https://github.com/google/googletest) installed.
Set `GTEST_INC` and `GTEST_LIB` in `Makefile` to specify the location of the gtest headers and libraries.
Alternatively, run `make googletest`, which will clone googletest and build it.
Run `make tests && make check` to run tests.
Random Dictionary Builder

### Permitted Arguments:
Input File/Directory (in=fileName): required; file/directory used to build dictionary; if directory, will operate recursively for files inside directory; can include multiple files/directories, each following "in="
Output Dictionary (out=dictName): if not provided, default to defaultDict
Dictionary ID (dictID=#): nonnegative number; if not provided, default to 0
Maximum Dictionary Size (maxdict=#): positive number; in bytes, if not provided, default to 110KB
Size of Randomly Selected Segment (k=#): positive number; in bytes; if not provided, default to 200

###Running Test:
make test


###Usage:
To build a random dictionary with the provided arguments: make ARG= followed by arguments


### Examples:
make ARG="in=../../../lib/dictBuilder out=dict100 dictID=520"
make ARG="in=../../../lib/dictBuilder in=../../../lib/compress"
FastCover Dictionary Builder

### Permitted Arguments:
Input File/Directory (in=fileName): required; file/directory used to build dictionary; if directory, will operate recursively for files inside directory; can include multiple files/directories, each following "in="
Output Dictionary (out=dictName): if not provided, default to fastCoverDict
Dictionary ID (dictID=#): nonnegative number; if not provided, default to 0
Maximum Dictionary Size (maxdict=#): positive number; in bytes, if not provided, default to 110KB
Size of Selected Segment (k=#): positive number; in bytes; if not provided, default to 200
Size of Dmer (d=#): either 6 or 8; if not provided, default to 8
Number of steps (steps=#): positive number, if not provided, default to 32
Percentage of samples used for training(split=#): positive number; if not provided, default to 100


###Running Test:
make test


###Usage:
To build a FASTCOVER dictionary with the provided arguments: make ARG= followed by arguments
If k or d is not provided, the optimize version of FASTCOVER is run.

### Examples:
make ARG="in=../../../lib/dictBuilder out=dict100 dictID=520"
make ARG="in=../../../lib/dictBuilder in=../../../lib/compress"
Benchmarking Dictionary Builder

### Permitted Argument:
Input File/Directory (in=fileName): required; file/directory used to build dictionary; if directory, will operate recursively for files inside directory; can include multiple files/directories, each following "in="

###Running Test:
make test

###Usage:
Benchmark given input files: make ARG= followed by permitted arguments

### Examples:
make ARG="in=../../../lib/dictBuilder in=../../../lib/compress"

###Benchmarking Result:
- First Cover is optimize cover, second Cover uses optimized d and k from first one.
- For every f value of fastCover, the first one is optimize fastCover and the second one uses optimized d and k from first one. This is run for accel values from 1 to 10.
- Fourth column is chosen d and fifth column is chosen k

github:
NODICT       0.000004       2.999642        
RANDOM       0.024560       8.791189        
LEGACY       0.727109       8.173529        
COVER       40.565676       10.652243        8          1298
COVER       3.608284       10.652243        8          1298
FAST f=15 a=1       4.181024       10.570882        8          1154
FAST f=15 a=1       0.040788       10.570882        8          1154
FAST f=15 a=2       3.548352       10.574287        6          1970
FAST f=15 a=2       0.035535       10.574287        6          1970
FAST f=15 a=3       3.287364       10.613950        6          1010
FAST f=15 a=3       0.032182       10.613950        6          1010
FAST f=15 a=4       3.184976       10.573883        6          1058
FAST f=15 a=4       0.029878       10.573883        6          1058
FAST f=15 a=5       3.045513       10.580640        8          1154
FAST f=15 a=5       0.022162       10.580640        8          1154
FAST f=15 a=6       3.003296       10.583677        6          1010
FAST f=15 a=6       0.028091       10.583677        6          1010
FAST f=15 a=7       2.952655       10.622551        6          1106
FAST f=15 a=7       0.02724       10.622551        6          1106
FAST f=15 a=8       2.945674       10.614657        6          1010
FAST f=15 a=8       0.027264       10.614657        6          1010
FAST f=15 a=9       3.153439       10.564018        8          1154
FAST f=15 a=9       0.020635       10.564018        8          1154
FAST f=15 a=10       2.950416       10.511454        6          1010
FAST f=15 a=10       0.026606       10.511454        6          1010
FAST f=16 a=1       3.970029       10.681035        8          1154
FAST f=16 a=1       0.038188       10.681035        8          1154
FAST f=16 a=2       3.422892       10.484978        6          1874
FAST f=16 a=2       0.034702       10.484978        6          1874
FAST f=16 a=3       3.215836       10.632631        8          1154
FAST f=16 a=3       0.026084       10.632631        8          1154
FAST f=16 a=4       3.081353       10.626533        6          1106
FAST f=16 a=4       0.030032       10.626533        6          1106
FAST f=16 a=5       3.041241       10.545027        8          1922
FAST f=16 a=5       0.022882       10.545027        8          1922
FAST f=16 a=6       2.989390       10.638284        6          1874
FAST f=16 a=6       0.028308       10.638284        6          1874
FAST f=16 a=7       3.001581       10.797136        6          1106
FAST f=16 a=7       0.027479       10.797136        6          1106
FAST f=16 a=8       2.984107       10.658356        8          1058
FAST f=16 a=8       0.021099       10.658356        8          1058
FAST f=16 a=9       2.925788       10.523869        6          1010
FAST f=16 a=9       0.026905       10.523869        6          1010
FAST f=16 a=10       2.889605       10.745841        6          1874
FAST f=16 a=10       0.026846       10.745841        6          1874
FAST f=17 a=1       4.031953       10.672080        8          1202
FAST f=17 a=1       0.040658       10.672080        8          1202
FAST f=17 a=2       3.458107       10.589352        8          1106
FAST f=17 a=2       0.02926       10.589352        8          1106
FAST f=17 a=3       3.291189       10.662714        8          1154
FAST f=17 a=3       0.026531       10.662714        8          1154
FAST f=17 a=4       3.154950       10.549456        8          1346
FAST f=17 a=4       0.024991       10.549456        8          1346
FAST f=17 a=5       3.092271       10.541670        6          1202
FAST f=17 a=5       0.038285       10.541670        6          1202
FAST f=17 a=6       3.166146       10.729112        6          1874
FAST f=17 a=6       0.038217       10.729112        6          1874
FAST f=17 a=7       3.035467       10.810485        6          1106
FAST f=17 a=7       0.036655       10.810485        6          1106
FAST f=17 a=8       3.035668       10.530532        6          1058
FAST f=17 a=8       0.037715       10.530532        6          1058
FAST f=17 a=9       2.987917       10.589802        8          1922
FAST f=17 a=9       0.02217       10.589802        8          1922
FAST f=17 a=10       2.981647       10.722579        8          1106
FAST f=17 a=10       0.021948       10.722579        8          1106
FAST f=18 a=1       4.067144       10.634943        8          1154
FAST f=18 a=1       0.041386       10.634943        8          1154
FAST f=18 a=2       3.507377       10.546230        6          1970
FAST f=18 a=2       0.037572       10.546230        6          1970
FAST f=18 a=3       3.323015       10.648061        8          1154
FAST f=18 a=3       0.028306       10.648061        8          1154
FAST f=18 a=4       3.216735       10.705402        6          1010
FAST f=18 a=4       0.030755       10.705402        6          1010
FAST f=18 a=5       3.175794       10.588154        8          1874
FAST f=18 a=5       0.025315       10.588154        8          1874
FAST f=18 a=6       3.127459       10.751104        8          1106
FAST f=18 a=6       0.023897       10.751104        8          1106
FAST f=18 a=7       3.083017       10.780402        6          1106
FAST f=18 a=7       0.029158       10.780402        6          1106
FAST f=18 a=8       3.069700       10.547226        8          1346
FAST f=18 a=8       0.024046       10.547226        8          1346
FAST f=18 a=9       3.056591       10.674759        6          1010
FAST f=18 a=9       0.028496       10.674759        6          1010
FAST f=18 a=10       3.063588       10.737578        8          1106
FAST f=18 a=10       0.023033       10.737578        8          1106
FAST f=19 a=1       4.164041       10.650333        8          1154
FAST f=19 a=1       0.042906       10.650333        8          1154
FAST f=19 a=2       3.585409       10.577066        6          1058
FAST f=19 a=2       0.038994       10.577066        6          1058
FAST f=19 a=3       3.439643       10.639403        8          1154
FAST f=19 a=3       0.028427       10.639403        8          1154
FAST f=19 a=4       3.268869       10.554410        8          1298
FAST f=19 a=4       0.026866       10.554410        8          1298
FAST f=19 a=5       3.238225       10.615109        6          1010
FAST f=19 a=5       0.03078       10.615109        6          1010
FAST f=19 a=6       3.199558       10.609782        6          1874
FAST f=19 a=6       0.030099       10.609782        6          1874
FAST f=19 a=7       3.132395       10.794753        6          1106
FAST f=19 a=7       0.028964       10.794753        6          1106
FAST f=19 a=8       3.148446       10.554842        8          1298
FAST f=19 a=8       0.024277       10.554842        8          1298
FAST f=19 a=9       3.108324       10.668763        6          1010
FAST f=19 a=9       0.02896       10.668763        6          1010
FAST f=19 a=10       3.159863       10.757347        8          1106
FAST f=19 a=10       0.023351       10.757347        8          1106
FAST f=20 a=1       4.462698       10.661788        8          1154
FAST f=20 a=1       0.047174       10.661788        8          1154
FAST f=20 a=2       3.820269       10.678612        6          1106
FAST f=20 a=2       0.040807       10.678612        6          1106
FAST f=20 a=3       3.644955       10.648424        8          1154
FAST f=20 a=3       0.031398       10.648424        8          1154
FAST f=20 a=4       3.546257       10.559756        8          1298
FAST f=20 a=4       0.029856       10.559756        8          1298
FAST f=20 a=5       3.485248       10.646637        6          1010
FAST f=20 a=5       0.033756       10.646637        6          1010
FAST f=20 a=6       3.490438       10.775824        8          1106
FAST f=20 a=6       0.028338       10.775824        8          1106
FAST f=20 a=7       3.631289       10.801795        6          1106
FAST f=20 a=7       0.035228       10.801795        6          1106
FAST f=20 a=8       3.758936       10.545116        8          1346
FAST f=20 a=8       0.027495       10.545116        8          1346
FAST f=20 a=9       3.707024       10.677454        6          1010
FAST f=20 a=9       0.031326       10.677454        6          1010
FAST f=20 a=10       3.586593       10.756017        8          1106
FAST f=20 a=10       0.027122       10.756017        8          1106
FAST f=21 a=1       5.701396       10.655398        8          1154
FAST f=21 a=1       0.067744       10.655398        8          1154
FAST f=21 a=2       5.270542       10.650743        6          1106
FAST f=21 a=2       0.052999       10.650743        6          1106
FAST f=21 a=3       4.945294       10.652380        8          1154
FAST f=21 a=3       0.052678       10.652380        8          1154
FAST f=21 a=4       4.894079       10.543185        8          1298
FAST f=21 a=4       0.04997       10.543185        8          1298
FAST f=21 a=5       4.785417       10.630321        6          1010
FAST f=21 a=5       0.045294       10.630321        6          1010
FAST f=21 a=6       4.789381       10.664477        6          1874
FAST f=21 a=6       0.046578       10.664477        6          1874
FAST f=21 a=7       4.302955       10.805179        6          1106
FAST f=21 a=7       0.041205       10.805179        6          1106
FAST f=21 a=8       4.034630       10.551211        8          1298
FAST f=21 a=8       0.040121       10.551211        8          1298
FAST f=21 a=9       4.523868       10.799114        6          1010
FAST f=21 a=9       0.043592       10.799114        6          1010
FAST f=21 a=10       4.760736       10.750255        8          1106
FAST f=21 a=10       0.043483       10.750255        8          1106
FAST f=22 a=1       6.743064       10.640537        8          1154
FAST f=22 a=1       0.086967       10.640537        8          1154
FAST f=22 a=2       6.121739       10.626638        6          1970
FAST f=22 a=2       0.066337       10.626638        6          1970
FAST f=22 a=3       5.248851       10.640688        8          1154
FAST f=22 a=3       0.054935       10.640688        8          1154
FAST f=22 a=4       5.436579       10.588333        8          1298
FAST f=22 a=4       0.064113       10.588333        8          1298
FAST f=22 a=5       5.812815       10.652653        6          1010
FAST f=22 a=5       0.058189       10.652653        6          1010
FAST f=22 a=6       5.745472       10.666437        6          1874
FAST f=22 a=6       0.057188       10.666437        6          1874
FAST f=22 a=7       5.716393       10.806911        6          1106
FAST f=22 a=7       0.056       10.806911        6          1106
FAST f=22 a=8       5.698799       10.530784        8          1298
FAST f=22 a=8       0.0583       10.530784        8          1298
FAST f=22 a=9       5.710533       10.777391        6          1010
FAST f=22 a=9       0.054945       10.777391        6          1010
FAST f=22 a=10       5.685395       10.745023        8          1106
FAST f=22 a=10       0.056526       10.745023        8          1106
FAST f=23 a=1       7.836923       10.638828        8          1154
FAST f=23 a=1       0.099522       10.638828        8          1154
FAST f=23 a=2       6.627834       10.631061        6          1970
FAST f=23 a=2       0.066769       10.631061        6          1970
FAST f=23 a=3       5.602533       10.647288        8          1154
FAST f=23 a=3       0.064513       10.647288        8          1154
FAST f=23 a=4       6.005580       10.568747        8          1298
FAST f=23 a=4       0.062022       10.568747        8          1298
FAST f=23 a=5       5.481816       10.676921        6          1010
FAST f=23 a=5       0.058959       10.676921        6          1010
FAST f=23 a=6       5.460444       10.666194        6          1874
FAST f=23 a=6       0.057687       10.666194        6          1874
FAST f=23 a=7       5.659822       10.800377        6          1106
FAST f=23 a=7       0.06783       10.800377        6          1106
FAST f=23 a=8       6.826940       10.522167        8          1298
FAST f=23 a=8       0.070533       10.522167        8          1298
FAST f=23 a=9       6.804757       10.577799        8          1682
FAST f=23 a=9       0.069949       10.577799        8          1682
FAST f=23 a=10       6.774933       10.742093        8          1106
FAST f=23 a=10       0.068395       10.742093        8          1106
FAST f=24 a=1       8.444110       10.632783        8          1154
FAST f=24 a=1       0.094357       10.632783        8          1154
FAST f=24 a=2       7.289578       10.631061        6          1970
FAST f=24 a=2       0.098515       10.631061        6          1970
FAST f=24 a=3       8.619780       10.646289        8          1154
FAST f=24 a=3       0.098041       10.646289        8          1154
FAST f=24 a=4       8.508455       10.555199        8          1298
FAST f=24 a=4       0.093885       10.555199        8          1298
FAST f=24 a=5       8.471145       10.674363        6          1010
FAST f=24 a=5       0.088676       10.674363        6          1010
FAST f=24 a=6       8.426727       10.667228        6          1874
FAST f=24 a=6       0.087247       10.667228        6          1874
FAST f=24 a=7       8.356826       10.803027        6          1106
FAST f=24 a=7       0.085835       10.803027        6          1106
FAST f=24 a=8       6.756811       10.522049        8          1298
FAST f=24 a=8       0.07107       10.522049        8          1298
FAST f=24 a=9       6.548169       10.571882        8          1682
FAST f=24 a=9       0.0713       10.571882        8          1682
FAST f=24 a=10       8.238079       10.736453        8          1106
FAST f=24 a=10       0.07004       10.736453        8          1106


hg-commands:
NODICT       0.000005       2.425276        
RANDOM       0.046332       3.490331        
LEGACY       0.720351       3.911682        
COVER       45.507731       4.132653        8          386
COVER       1.868810       4.132653        8          386
FAST f=15 a=1       4.561427       3.866894        8          1202
FAST f=15 a=1       0.048946       3.866894        8          1202
FAST f=15 a=2       3.574462       3.892119        8          1538
FAST f=15 a=2       0.033677       3.892119        8          1538
FAST f=15 a=3       3.230227       3.888791        6          1346
FAST f=15 a=3       0.034312       3.888791        6          1346
FAST f=15 a=4       3.042388       3.899739        8          1010
FAST f=15 a=4       0.024307       3.899739        8          1010
FAST f=15 a=5       2.800148       3.896220        8          818
FAST f=15 a=5       0.022331       3.896220        8          818
FAST f=15 a=6       2.706518       3.882039        8          578
FAST f=15 a=6       0.020955       3.882039        8          578
FAST f=15 a=7       2.701820       3.885430        6          866
FAST f=15 a=7       0.026074       3.885430        6          866
FAST f=15 a=8       2.604445       3.906932        8          1826
FAST f=15 a=8       0.021789       3.906932        8          1826
FAST f=15 a=9       2.598568       3.870324        6          1682
FAST f=15 a=9       0.026004       3.870324        6          1682
FAST f=15 a=10       2.575920       3.920783        8          1442
FAST f=15 a=10       0.020228       3.920783        8          1442
FAST f=16 a=1       4.630623       4.001430        8          770
FAST f=16 a=1       0.047497       4.001430        8          770
FAST f=16 a=2       3.674721       3.974431        8          1874
FAST f=16 a=2       0.035761       3.974431        8          1874
FAST f=16 a=3       3.338384       3.978703        8          1010
FAST f=16 a=3       0.029436       3.978703        8          1010
FAST f=16 a=4       3.004412       3.983035        8          1010
FAST f=16 a=4       0.025744       3.983035        8          1010
FAST f=16 a=5       2.881892       3.987710        8          770
FAST f=16 a=5       0.023211       3.987710        8          770
FAST f=16 a=6       2.807410       3.952717        8          1298
FAST f=16 a=6       0.023199       3.952717        8          1298
FAST f=16 a=7       2.819623       3.994627        8          770
FAST f=16 a=7       0.021806       3.994627        8          770
FAST f=16 a=8       2.740092       3.954032        8          1826
FAST f=16 a=8       0.0226       3.954032        8          1826
FAST f=16 a=9       2.682564       3.969879        6          1442
FAST f=16 a=9       0.026324       3.969879        6          1442
FAST f=16 a=10       2.657959       3.969755        8          674
FAST f=16 a=10       0.020413       3.969755        8          674
FAST f=17 a=1       4.729228       4.046000        8          530
FAST f=17 a=1       0.049703       4.046000        8          530
FAST f=17 a=2       3.764510       3.991519        8          1970
FAST f=17 a=2       0.038195       3.991519        8          1970
FAST f=17 a=3       3.416992       4.006296        6          914
FAST f=17 a=3       0.036244       4.006296        6          914
FAST f=17 a=4       3.145626       3.979182        8          1970
FAST f=17 a=4       0.028676       3.979182        8          1970
FAST f=17 a=5       2.995070       4.050070        8          770
FAST f=17 a=5       0.025707       4.050070        8          770
FAST f=17 a=6       2.911833       4.040024        8          770
FAST f=17 a=6       0.02453       4.040024        8          770
FAST f=17 a=7       2.894796       4.015884        8          818
FAST f=17 a=7       0.023956       4.015884        8          818
FAST f=17 a=8       2.789962       4.039303        8          530
FAST f=17 a=8       0.023219       4.039303        8          530
FAST f=17 a=9       2.787625       3.996762        8          1634
FAST f=17 a=9       0.023651       3.996762        8          1634
FAST f=17 a=10       2.754796       4.005059        8          1058
FAST f=17 a=10       0.022537       4.005059        8          1058
FAST f=18 a=1       4.779117       4.038214        8          242
FAST f=18 a=1       0.048814       4.038214        8          242
FAST f=18 a=2       3.829753       4.045768        8          722
FAST f=18 a=2       0.036541       4.045768        8          722
FAST f=18 a=3       3.495053       4.021497        8          770
FAST f=18 a=3       0.032648       4.021497        8          770
FAST f=18 a=4       3.221395       4.039623        8          770
FAST f=18 a=4       0.027818       4.039623        8          770
FAST f=18 a=5       3.059369       4.050414        8          530
FAST f=18 a=5       0.026296       4.050414        8          530
FAST f=18 a=6       3.019292       4.010714        6          962
FAST f=18 a=6       0.031104       4.010714        6          962
FAST f=18 a=7       2.949322       4.031439        6          770
FAST f=18 a=7       0.030745       4.031439        6          770
FAST f=18 a=8       2.876425       4.032088        6          386
FAST f=18 a=8       0.027407       4.032088        6          386
FAST f=18 a=9       2.850958       4.053372        8          674
FAST f=18 a=9       0.023799       4.053372        8          674
FAST f=18 a=10       2.884352       4.020148        8          1730
FAST f=18 a=10       0.024401       4.020148        8          1730
FAST f=19 a=1       4.815669       4.061203        8          674
FAST f=19 a=1       0.051425       4.061203        8          674
FAST f=19 a=2       3.951356       4.013822        8          1442
FAST f=19 a=2       0.039968       4.013822        8          1442
FAST f=19 a=3       3.554682       4.050425        8          722
FAST f=19 a=3       0.032725       4.050425        8          722
FAST f=19 a=4       3.242585       4.054677        8          722
FAST f=19 a=4       0.028194       4.054677        8          722
FAST f=19 a=5       3.105909       4.064524        8          818
FAST f=19 a=5       0.02675       4.064524        8          818
FAST f=19 a=6       3.059901       4.036857        8          1250
FAST f=19 a=6       0.026396       4.036857        8          1250
FAST f=19 a=7       3.016151       4.068234        6          770
FAST f=19 a=7       0.031501       4.068234        6          770
FAST f=19 a=8       2.962902       4.077509        8          530
FAST f=19 a=8       0.023333       4.077509        8          530
FAST f=19 a=9       2.899607       4.067328        8          530
FAST f=19 a=9       0.024553       4.067328        8          530
FAST f=19 a=10       2.950978       4.059901        8          434
FAST f=19 a=10       0.023852       4.059901        8          434
FAST f=20 a=1       5.259834       4.027579        8          1634
FAST f=20 a=1       0.061123       4.027579        8          1634
FAST f=20 a=2       4.382150       4.025093        8          1634
FAST f=20 a=2       0.048009       4.025093        8          1634
FAST f=20 a=3       4.104323       4.060842        8          530
FAST f=20 a=3       0.040965       4.060842        8          530
FAST f=20 a=4       3.853340       4.023504        6          914
FAST f=20 a=4       0.041072       4.023504        6          914
FAST f=20 a=5       3.728841       4.018089        6          1634
FAST f=20 a=5       0.037469       4.018089        6          1634
FAST f=20 a=6       3.683045       4.069138        8          578
FAST f=20 a=6       0.028011       4.069138        8          578
FAST f=20 a=7       3.726973       4.063160        8          722
FAST f=20 a=7       0.028437       4.063160        8          722
FAST f=20 a=8       3.555073       4.057690        8          386
FAST f=20 a=8       0.027588       4.057690        8          386
FAST f=20 a=9       3.551095       4.067253        8          482
FAST f=20 a=9       0.025976       4.067253        8          482
FAST f=20 a=10       3.490127       4.068518        8          530
FAST f=20 a=10       0.025971       4.068518        8          530
FAST f=21 a=1       7.343816       4.064945        8          770
FAST f=21 a=1       0.085035       4.064945        8          770
FAST f=21 a=2       5.930894       4.048206        8          386
FAST f=21 a=2       0.067349       4.048206        8          386
FAST f=21 a=3       6.770775       4.063417        8          578
FAST f=21 a=3       0.077104       4.063417        8          578
FAST f=21 a=4       6.889409       4.066761        8          626
FAST f=21 a=4       0.0717       4.066761        8          626
FAST f=21 a=5       6.714896       4.051813        8          914
FAST f=21 a=5       0.071026       4.051813        8          914
FAST f=21 a=6       6.539890       4.047263        8          1922
FAST f=21 a=6       0.07127       4.047263        8          1922
FAST f=21 a=7       6.511052       4.068373        8          482
FAST f=21 a=7       0.065467       4.068373        8          482
FAST f=21 a=8       6.458788       4.071597        8          482
FAST f=21 a=8       0.063817       4.071597        8          482
FAST f=21 a=9       6.377591       4.052905        8          434
FAST f=21 a=9       0.063112       4.052905        8          434
FAST f=21 a=10       6.360752       4.047773        8          530
FAST f=21 a=10       0.063606       4.047773        8          530
FAST f=22 a=1       10.523471       4.040812        8          962
FAST f=22 a=1       0.14214       4.040812        8          962
FAST f=22 a=2       9.454758       4.059396        8          914
FAST f=22 a=2       0.118343       4.059396        8          914
FAST f=22 a=3       9.043197       4.043019        8          1922
FAST f=22 a=3       0.109798       4.043019        8          1922
FAST f=22 a=4       8.716261       4.044819        8          770
FAST f=22 a=4       0.099687       4.044819        8          770
FAST f=22 a=5       8.529472       4.070576        8          530
FAST f=22 a=5       0.093127       4.070576        8          530
FAST f=22 a=6       8.424241       4.070565        8          722
FAST f=22 a=6       0.093703       4.070565        8          722
FAST f=22 a=7       8.403391       4.070591        8          578
FAST f=22 a=7       0.089763       4.070591        8          578
FAST f=22 a=8       8.285221       4.089171        8          530
FAST f=22 a=8       0.087716       4.089171        8          530
FAST f=22 a=9       8.282506       4.047470        8          722
FAST f=22 a=9       0.089773       4.047470        8          722
FAST f=22 a=10       8.241809       4.064151        8          818
FAST f=22 a=10       0.090413       4.064151        8          818
FAST f=23 a=1       12.389208       4.051635        6          530
FAST f=23 a=1       0.147796       4.051635        6          530
FAST f=23 a=2       11.300910       4.042835        6          914
FAST f=23 a=2       0.133178       4.042835        6          914
FAST f=23 a=3       10.879455       4.047415        8          626
FAST f=23 a=3       0.129571       4.047415        8          626
FAST f=23 a=4       10.522718       4.038269        6          914
FAST f=23 a=4       0.118121       4.038269        6          914
FAST f=23 a=5       10.348043       4.066884        8          434
FAST f=23 a=5       0.112098       4.066884        8          434
FAST f=23 a=6       10.238630       4.048635        8          1010
FAST f=23 a=6       0.120281       4.048635        8          1010
FAST f=23 a=7       10.213255       4.061809        8          530
FAST f=23 a=7       0.1121       4.061809        8          530
FAST f=23 a=8       10.107879       4.074104        8          818
FAST f=23 a=8       0.116544       4.074104        8          818
FAST f=23 a=9       10.063424       4.064811        8          674
FAST f=23 a=9       0.109045       4.064811        8          674
FAST f=23 a=10       10.035801       4.054918        8          530
FAST f=23 a=10       0.108735       4.054918        8          530
FAST f=24 a=1       14.963878       4.073490        8          722
FAST f=24 a=1       0.206344       4.073490        8          722
FAST f=24 a=2       13.833472       4.036100        8          962
FAST f=24 a=2       0.17486       4.036100        8          962
FAST f=24 a=3       13.404631       4.026281        6          1106
FAST f=24 a=3       0.153961       4.026281        6          1106
FAST f=24 a=4       13.041164       4.065448        8          674
FAST f=24 a=4       0.155509       4.065448        8          674
FAST f=24 a=5       12.879412       4.054636        8          674
FAST f=24 a=5       0.148282       4.054636        8          674
FAST f=24 a=6       12.773736       4.081376        8          530
FAST f=24 a=6       0.142563       4.081376        8          530
FAST f=24 a=7       12.711310       4.059834        8          770
FAST f=24 a=7       0.149321       4.059834        8          770
FAST f=24 a=8       12.635459       4.052050        8          1298
FAST f=24 a=8       0.15095       4.052050        8          1298
FAST f=24 a=9       12.558104       4.076516        8          722
FAST f=24 a=9       0.144361       4.076516        8          722
FAST f=24 a=10       10.661348       4.062137        8          818
FAST f=24 a=10       0.108232       4.062137        8          818


hg-changelog:
NODICT       0.000017       1.377590        
RANDOM       0.186171       2.097487        
LEGACY       1.670867       2.058907        
COVER       173.561948       2.189685        8          98
COVER       4.811180       2.189685        8          98
FAST f=15 a=1       18.685906       2.129682        8          434
FAST f=15 a=1       0.173376       2.129682        8          434
FAST f=15 a=2       12.928259       2.131890        8          482
FAST f=15 a=2       0.102582       2.131890        8          482
FAST f=15 a=3       11.132343       2.128027        8          386
FAST f=15 a=3       0.077122       2.128027        8          386
FAST f=15 a=4       10.120683       2.125797        8          434
FAST f=15 a=4       0.065175       2.125797        8          434
FAST f=15 a=5       9.479092       2.127697        8          386
FAST f=15 a=5       0.057905       2.127697        8          386
FAST f=15 a=6       9.159523       2.127132        8          1682
FAST f=15 a=6       0.058604       2.127132        8          1682
FAST f=15 a=7       8.724003       2.129914        8          434
FAST f=15 a=7       0.0493       2.129914        8          434
FAST f=15 a=8       8.595001       2.127137        8          338
FAST f=15 a=8       0.0474       2.127137        8          338
FAST f=15 a=9       8.356405       2.125512        8          482
FAST f=15 a=9       0.046126       2.125512        8          482
FAST f=15 a=10       8.207111       2.126066        8          338
FAST f=15 a=10       0.043292       2.126066        8          338
FAST f=16 a=1       18.464436       2.144040        8          242
FAST f=16 a=1       0.172156       2.144040        8          242
FAST f=16 a=2       12.844825       2.148171        8          194
FAST f=16 a=2       0.099619       2.148171        8          194
FAST f=16 a=3       11.082568       2.140837        8          290
FAST f=16 a=3       0.079165       2.140837        8          290
FAST f=16 a=4       10.066749       2.144405        8          386
FAST f=16 a=4       0.068411       2.144405        8          386
FAST f=16 a=5       9.501121       2.140720        8          386
FAST f=16 a=5       0.061316       2.140720        8          386
FAST f=16 a=6       9.179332       2.139478        8          386
FAST f=16 a=6       0.056322       2.139478        8          386
FAST f=16 a=7       8.849438       2.142412        8          194
FAST f=16 a=7       0.050493       2.142412        8          194
FAST f=16 a=8       8.810919       2.143454        8          434
FAST f=16 a=8       0.051304       2.143454        8          434
FAST f=16 a=9       8.553900       2.140339        8          194
FAST f=16 a=9       0.047285       2.140339        8          194
FAST f=16 a=10       8.398027       2.143130        8          386
FAST f=16 a=10       0.046386       2.143130        8          386
FAST f=17 a=1       18.644657       2.157192        8          98
FAST f=17 a=1       0.173884       2.157192        8          98
FAST f=17 a=2       13.071242       2.159830        8          146
FAST f=17 a=2       0.10388       2.159830        8          146
FAST f=17 a=3       11.332366       2.153654        6          194
FAST f=17 a=3       0.08983       2.153654        6          194
FAST f=17 a=4       10.362413       2.156813        8          242
FAST f=17 a=4       0.070389       2.156813        8          242
FAST f=17 a=5       9.808159       2.155098        6          338
FAST f=17 a=5       0.072661       2.155098        6          338
FAST f=17 a=6       9.451165       2.153845        6          146
FAST f=17 a=6       0.064959       2.153845        6          146
FAST f=17 a=7       9.163097       2.155424        6          242
FAST f=17 a=7       0.064323       2.155424        6          242
FAST f=17 a=8       9.047276       2.156640        8          242
FAST f=17 a=8       0.053382       2.156640        8          242
FAST f=17 a=9       8.807671       2.152396        8          146
FAST f=17 a=9       0.049617       2.152396        8          146
FAST f=17 a=10       8.649827       2.152370        8          146
FAST f=17 a=10       0.047849       2.152370        8          146
FAST f=18 a=1       18.809502       2.168116        8          98
FAST f=18 a=1       0.175226       2.168116        8          98
FAST f=18 a=2       13.756502       2.170870        6          242
FAST f=18 a=2       0.119507       2.170870        6          242
FAST f=18 a=3       12.059748       2.163094        6          98
FAST f=18 a=3       0.093912       2.163094        6          98
FAST f=18 a=4       11.410294       2.172372        8          98
FAST f=18 a=4       0.073048       2.172372        8          98
FAST f=18 a=5       10.560297       2.166388        8          98
FAST f=18 a=5       0.065136       2.166388        8          98
FAST f=18 a=6       10.071390       2.162672        8          98
FAST f=18 a=6       0.059402       2.162672        8          98
FAST f=18 a=7       10.084214       2.166624        6          194
FAST f=18 a=7       0.073276       2.166624        6          194
FAST f=18 a=8       9.953226       2.167454        8          98
FAST f=18 a=8       0.053659       2.167454        8          98
FAST f=18 a=9       8.982461       2.161593        6          146
FAST f=18 a=9       0.05955       2.161593        6          146
FAST f=18 a=10       8.986092       2.164373        6          242
FAST f=18 a=10       0.059135       2.164373        6          242
FAST f=19 a=1       18.908277       2.176021        8          98
FAST f=19 a=1       0.177316       2.176021        8          98
FAST f=19 a=2       13.471313       2.176103        8          98
FAST f=19 a=2       0.106344       2.176103        8          98
FAST f=19 a=3       11.571406       2.172812        8          98
FAST f=19 a=3       0.083293       2.172812        8          98
FAST f=19 a=4       10.632775       2.177770        6          146
FAST f=19 a=4       0.079864       2.177770        6          146
FAST f=19 a=5       10.030190       2.175574        6          146
FAST f=19 a=5       0.07223       2.175574        6          146
FAST f=19 a=6       9.717818       2.169997        8          98
FAST f=19 a=6       0.060049       2.169997        8          98
FAST f=19 a=7       9.397531       2.172770        8          146
FAST f=19 a=7       0.057188       2.172770        8          146
FAST f=19 a=8       9.281061       2.175822        8          98
FAST f=19 a=8       0.053711       2.175822        8          98
FAST f=19 a=9       9.165242       2.169849        6          146
FAST f=19 a=9       0.059898       2.169849        6          146
FAST f=19 a=10       9.048763       2.173394        8          98
FAST f=19 a=10       0.049757       2.173394        8          98
FAST f=20 a=1       21.166917       2.183923        6          98
FAST f=20 a=1       0.205425       2.183923        6          98
FAST f=20 a=2       15.642753       2.182349        6          98
FAST f=20 a=2       0.135957       2.182349        6          98
FAST f=20 a=3       14.053730       2.173544        6          98
FAST f=20 a=3       0.11266       2.173544        6          98
FAST f=20 a=4       15.270019       2.183656        8          98
FAST f=20 a=4       0.107892       2.183656        8          98
FAST f=20 a=5       15.497927       2.174661        6          98
FAST f=20 a=5       0.100305       2.174661        6          98
FAST f=20 a=6       13.973505       2.172391        8          98
FAST f=20 a=6       0.087565       2.172391        8          98
FAST f=20 a=7       14.083296       2.172443        8          98
FAST f=20 a=7       0.078062       2.172443        8          98
FAST f=20 a=8       12.560048       2.175581        8          98
FAST f=20 a=8       0.070282       2.175581        8          98
FAST f=20 a=9       13.078645       2.173975        6          146
FAST f=20 a=9       0.081041       2.173975        6          146
FAST f=20 a=10       12.823328       2.177778        8          98
FAST f=20 a=10       0.074522       2.177778        8          98
FAST f=21 a=1       29.825370       2.183057        6          98
FAST f=21 a=1       0.334453       2.183057        6          98
FAST f=21 a=2       29.476474       2.182752        8          98
FAST f=21 a=2       0.286602       2.182752        8          98
FAST f=21 a=3       25.937186       2.175867        8          98
FAST f=21 a=3       0.17626       2.175867        8          98
FAST f=21 a=4       20.413865       2.179780        8          98
FAST f=21 a=4       0.206085       2.179780        8          98
FAST f=21 a=5       20.541889       2.178328        6          146
FAST f=21 a=5       0.199157       2.178328        6          146
FAST f=21 a=6       21.090670       2.174443        6          146
FAST f=21 a=6       0.190645       2.174443        6          146
FAST f=21 a=7       20.221569       2.177384        6          146
FAST f=21 a=7       0.184278       2.177384        6          146
FAST f=21 a=8       20.322357       2.179456        6          98
FAST f=21 a=8       0.178458       2.179456        6          98
FAST f=21 a=9       20.683912       2.174396        6          146
FAST f=21 a=9       0.190829       2.174396        6          146
FAST f=21 a=10       20.840865       2.174905        8          98
FAST f=21 a=10       0.172515       2.174905        8          98
FAST f=22 a=1       36.822827       2.181612        6          98
FAST f=22 a=1       0.437389       2.181612        6          98
FAST f=22 a=2       30.616902       2.183142        8          98
FAST f=22 a=2       0.324284       2.183142        8          98
FAST f=22 a=3       28.472482       2.178130        8          98
FAST f=22 a=3       0.236538       2.178130        8          98
FAST f=22 a=4       25.847028       2.181878        8          98
FAST f=22 a=4       0.263744       2.181878        8          98
FAST f=22 a=5       27.095881       2.180775        8          98
FAST f=22 a=5       0.24988       2.180775        8          98
FAST f=22 a=6       25.939172       2.170916        8          98
FAST f=22 a=6       0.240033       2.170916        8          98
FAST f=22 a=7       27.064194       2.177849        8          98
FAST f=22 a=7       0.242383       2.177849        8          98
FAST f=22 a=8       25.140221       2.178216        8          98
FAST f=22 a=8       0.237601       2.178216        8          98
FAST f=22 a=9       25.505283       2.177455        6          146
FAST f=22 a=9       0.223217       2.177455        6          146
FAST f=22 a=10       24.529362       2.176705        6          98
FAST f=22 a=10       0.222876       2.176705        6          98
FAST f=23 a=1       39.127310       2.183006        6          98
FAST f=23 a=1       0.417338       2.183006        6          98
FAST f=23 a=2       32.468161       2.183524        6          98
FAST f=23 a=2       0.351645       2.183524        6          98
FAST f=23 a=3       31.577620       2.172604        6          98
FAST f=23 a=3       0.319659       2.172604        6          98
FAST f=23 a=4       30.129247       2.183932        6          98
FAST f=23 a=4       0.307239       2.183932        6          98
FAST f=23 a=5       29.103376       2.183529        6          146
FAST f=23 a=5       0.285533       2.183529        6          146
FAST f=23 a=6       29.776045       2.174367        8          98
FAST f=23 a=6       0.276846       2.174367        8          98
FAST f=23 a=7       28.940407       2.178022        6          146
FAST f=23 a=7       0.274082       2.178022        6          146
FAST f=23 a=8       29.256009       2.179462        6          98
FAST f=23 a=8       0.26949       2.179462        6          98
FAST f=23 a=9       29.347312       2.170407        8          98
FAST f=23 a=9       0.265034       2.170407        8          98
FAST f=23 a=10       29.140081       2.171762        8          98
FAST f=23 a=10       0.259183       2.171762        8          98
FAST f=24 a=1       44.871179       2.182115        6          98
FAST f=24 a=1       0.509433       2.182115        6          98
FAST f=24 a=2       38.694867       2.180549        8          98
FAST f=24 a=2       0.406695       2.180549        8          98
FAST f=24 a=3       38.363769       2.172821        8          98
FAST f=24 a=3       0.359581       2.172821        8          98
FAST f=24 a=4       36.580797       2.184142        8          98
FAST f=24 a=4       0.340614       2.184142        8          98
FAST f=24 a=5       33.125701       2.183301        8          98
FAST f=24 a=5       0.324874       2.183301        8          98
FAST f=24 a=6       34.776068       2.173019        6          146
FAST f=24 a=6       0.340397       2.173019        6          146
FAST f=24 a=7       34.417625       2.176561        6          146
FAST f=24 a=7       0.308223       2.176561        6          146
FAST f=24 a=8       35.470291       2.182161        6          98
FAST f=24 a=8       0.307724       2.182161        6          98
FAST f=24 a=9       34.927252       2.172682        6          146
FAST f=24 a=9       0.300598       2.172682        6          146
FAST f=24 a=10       33.238355       2.173395        6          98
FAST f=24 a=10       0.249916       2.173395        6          98


hg-manifest:
NODICT       0.000004       1.866377        
RANDOM       0.696346       2.309436        
LEGACY       7.064527       2.506977        
COVER       876.312865       2.582528        8          434
COVER       35.684533       2.582528        8          434
FAST f=15 a=1       76.618201       2.404013        8          1202
FAST f=15 a=1       0.700722       2.404013        8          1202
FAST f=15 a=2       49.213058       2.409248        6          1826
FAST f=15 a=2       0.473393       2.409248        6          1826
FAST f=15 a=3       41.753197       2.409677        8          1490
FAST f=15 a=3       0.336848       2.409677        8          1490
FAST f=15 a=4       38.648295       2.407996        8          1538
FAST f=15 a=4       0.283952       2.407996        8          1538
FAST f=15 a=5       36.144936       2.402895        8          1874
FAST f=15 a=5       0.270128       2.402895        8          1874
FAST f=15 a=6       35.484675       2.394873        8          1586
FAST f=15 a=6       0.251637       2.394873        8          1586
FAST f=15 a=7       34.280599       2.397311        8          1778
FAST f=15 a=7       0.23984       2.397311        8          1778
FAST f=15 a=8       32.122572       2.396089        6          1490
FAST f=15 a=8       0.251508       2.396089        6          1490
FAST f=15 a=9       29.909842       2.390092        6          1970
FAST f=15 a=9       0.251233       2.390092        6          1970
FAST f=15 a=10       30.102938       2.400086        6          1682
FAST f=15 a=10       0.23688       2.400086        6          1682
FAST f=16 a=1       67.750401       2.475460        6          1346
FAST f=16 a=1       0.796035       2.475460        6          1346
FAST f=16 a=2       52.812027       2.480860        6          1730
FAST f=16 a=2       0.480384       2.480860        6          1730
FAST f=16 a=3       44.179259       2.469304        8          1970
FAST f=16 a=3       0.332657       2.469304        8          1970
FAST f=16 a=4       37.612728       2.478208        6          1970
FAST f=16 a=4       0.32498       2.478208        6          1970
FAST f=16 a=5       35.056222       2.475568        6          1298
FAST f=16 a=5       0.302824       2.475568        6          1298
FAST f=16 a=6       34.713012       2.486079        8          1730
FAST f=16 a=6       0.24755       2.486079        8          1730
FAST f=16 a=7       33.713687       2.477180        6          1682
FAST f=16 a=7       0.280358       2.477180        6          1682
FAST f=16 a=8       31.571412       2.475418        8          1538
FAST f=16 a=8       0.241241       2.475418        8          1538
FAST f=16 a=9       31.608069       2.478263        8          1922
FAST f=16 a=9       0.241764       2.478263        8          1922
FAST f=16 a=10       31.358002       2.472263        8          1442
FAST f=16 a=10       0.221661       2.472263        8          1442
FAST f=17 a=1       66.185775       2.536085        6          1346
FAST f=17 a=1       0.713549       2.536085        6          1346
FAST f=17 a=2       50.365000       2.546105        8          1298
FAST f=17 a=2       0.467846       2.546105        8          1298
FAST f=17 a=3       42.712843       2.536250        8          1298
FAST f=17 a=3       0.34047       2.536250        8          1298
FAST f=17 a=4       39.514227       2.535555        8          1442
FAST f=17 a=4       0.302989       2.535555        8          1442
FAST f=17 a=5       35.189292       2.524925        8          1202
FAST f=17 a=5       0.273451       2.524925        8          1202
FAST f=17 a=6       35.791683       2.523466        8          1202
FAST f=17 a=6       0.268261       2.523466        8          1202
FAST f=17 a=7       37.416136       2.526625        6          1010
FAST f=17 a=7       0.277558       2.526625        6          1010
FAST f=17 a=8       37.084707       2.533274        6          1250
FAST f=17 a=8       0.285104       2.533274        6          1250
FAST f=17 a=9       34.183814       2.532765        8          1298
FAST f=17 a=9       0.235133       2.532765        8          1298
FAST f=17 a=10       31.149235       2.528722        8          1346
FAST f=17 a=10       0.232679       2.528722        8          1346
FAST f=18 a=1       72.942176       2.559857        6          386
FAST f=18 a=1       0.718618       2.559857        6          386
FAST f=18 a=2       51.690440       2.559572        8          290
FAST f=18 a=2       0.403978       2.559572        8          290
FAST f=18 a=3       45.344908       2.561040        8          962
FAST f=18 a=3       0.357205       2.561040        8          962
FAST f=18 a=4       39.804522       2.558446        8          1010
FAST f=18 a=4       0.310526       2.558446        8          1010
FAST f=18 a=5       38.134888       2.561811        8          626
FAST f=18 a=5       0.273743       2.561811        8          626
FAST f=18 a=6       35.091890       2.555518        8          722
FAST f=18 a=6       0.260135       2.555518        8          722
FAST f=18 a=7       34.639523       2.562938        8          290
FAST f=18 a=7       0.234294       2.562938        8          290
FAST f=18 a=8       36.076431       2.563567        8          1586
FAST f=18 a=8       0.274075       2.563567        8          1586
FAST f=18 a=9       36.376433       2.560950        8          722
FAST f=18 a=9       0.240106       2.560950        8          722
FAST f=18 a=10       32.624790       2.559340        8          578
FAST f=18 a=10       0.234704       2.559340        8          578
FAST f=19 a=1       70.513761       2.572441        8          194
FAST f=19 a=1       0.726112       2.572441        8          194
FAST f=19 a=2       59.263032       2.574560        8          482
FAST f=19 a=2       0.451554       2.574560        8          482
FAST f=19 a=3       51.509594       2.571546        6          194
FAST f=19 a=3       0.393014       2.571546        6          194
FAST f=19 a=4       55.393906       2.573386        8          482
FAST f=19 a=4       0.38819       2.573386        8          482
FAST f=19 a=5       43.201736       2.567589        8          674
FAST f=19 a=5       0.292155       2.567589        8          674
FAST f=19 a=6       42.911687       2.572666        6          434
FAST f=19 a=6       0.303988       2.572666        6          434
FAST f=19 a=7       44.687591       2.573613        6          290
FAST f=19 a=7       0.308721       2.573613        6          290
FAST f=19 a=8       37.372868       2.571039        6          194
FAST f=19 a=8       0.287137       2.571039        6          194
FAST f=19 a=9       36.074230       2.566473        6          482
FAST f=19 a=9       0.280721       2.566473        6          482
FAST f=19 a=10       33.731720       2.570306        8          194
FAST f=19 a=10       0.224073       2.570306        8          194
FAST f=20 a=1       79.670634       2.581146        6          290
FAST f=20 a=1       0.899986       2.581146        6          290
FAST f=20 a=2       58.827141       2.579782        8          386
FAST f=20 a=2       0.602288       2.579782        8          386
FAST f=20 a=3       51.289004       2.579627        8          722
FAST f=20 a=3       0.446091       2.579627        8          722
FAST f=20 a=4       47.711068       2.581508        8          722
FAST f=20 a=4       0.473007       2.581508        8          722
FAST f=20 a=5       47.402929       2.578062        6          434
FAST f=20 a=5       0.497131       2.578062        6          434
FAST f=20 a=6       54.797102       2.577365        8          482
FAST f=20 a=6       0.515061       2.577365        8          482
FAST f=20 a=7       51.370877       2.583050        8          386
FAST f=20 a=7       0.402878       2.583050        8          386
FAST f=20 a=8       51.437931       2.574875        6          242
FAST f=20 a=8       0.453094       2.574875        6          242
FAST f=20 a=9       44.105456       2.576700        6          242
FAST f=20 a=9       0.456633       2.576700        6          242
FAST f=20 a=10       44.447580       2.578305        8          338
FAST f=20 a=10       0.409121       2.578305        8          338
FAST f=21 a=1       113.031686       2.582449        6          242
FAST f=21 a=1       1.456971       2.582449        6          242
FAST f=21 a=2       97.700932       2.582124        8          194
FAST f=21 a=2       1.072078       2.582124        8          194
FAST f=21 a=3       96.563648       2.585479        8          434
FAST f=21 a=3       0.949528       2.585479        8          434
FAST f=21 a=4       90.597813       2.582366        6          386
FAST f=21 a=4       0.76944       2.582366        6          386
FAST f=21 a=5       86.815980       2.579043        8          434
FAST f=21 a=5       0.858167       2.579043        8          434
FAST f=21 a=6       91.235820       2.578378        8          530
FAST f=21 a=6       0.684274       2.578378        8          530
FAST f=21 a=7       84.392788       2.581243        8          386
FAST f=21 a=7       0.814386       2.581243        8          386
FAST f=21 a=8       82.052310       2.582547        8          338
FAST f=21 a=8       0.822633       2.582547        8          338
FAST f=21 a=9       74.696074       2.579319        8          194
FAST f=21 a=9       0.811028       2.579319        8          194
FAST f=21 a=10       76.211170       2.578766        8          290
FAST f=21 a=10       0.809715       2.578766        8          290
FAST f=22 a=1       138.976871       2.580478        8          194
FAST f=22 a=1       1.748932       2.580478        8          194
FAST f=22 a=2       120.164097       2.583633        8          386
FAST f=22 a=2       1.333239       2.583633        8          386
FAST f=22 a=3       111.986474       2.582566        6          194
FAST f=22 a=3       1.305734       2.582566        6          194
FAST f=22 a=4       108.548148       2.583068        6          194
FAST f=22 a=4       1.314026       2.583068        6          194
FAST f=22 a=5       103.173017       2.583495        6          290
FAST f=22 a=5       1.228664       2.583495        6          290
FAST f=22 a=6       108.421262       2.582349        8          530
FAST f=22 a=6       1.076773       2.582349        8          530
FAST f=22 a=7       103.284127       2.581022        8          386
FAST f=22 a=7       1.112117       2.581022        8          386
FAST f=22 a=8       96.330279       2.581073        8          290
FAST f=22 a=8       1.109303       2.581073        8          290
FAST f=22 a=9       97.651348       2.580075        6          194
FAST f=22 a=9       0.933032       2.580075        6          194
FAST f=22 a=10       101.660621       2.584886        8          194
FAST f=22 a=10       0.796823       2.584886        8          194
FAST f=23 a=1       159.322978       2.581474        6          242
FAST f=23 a=1       2.015878       2.581474        6          242
FAST f=23 a=2       134.331775       2.581619        8          194
FAST f=23 a=2       1.545845       2.581619        8          194
FAST f=23 a=3       127.724552       2.579888        6          338
FAST f=23 a=3       1.444496       2.579888        6          338
FAST f=23 a=4       126.077675       2.578137        6          242
FAST f=23 a=4       1.364394       2.578137        6          242
FAST f=23 a=5       124.914027       2.580843        8          338
FAST f=23 a=5       1.116059       2.580843        8          338
FAST f=23 a=6       122.874153       2.577637        6          338
FAST f=23 a=6       1.164584       2.577637        6          338
FAST f=23 a=7       123.099257       2.582715        6          386
FAST f=23 a=7       1.354042       2.582715        6          386
FAST f=23 a=8       122.026753       2.577681        8          194
FAST f=23 a=8       1.210966       2.577681        8          194
FAST f=23 a=9       121.164312       2.584599        6          290
FAST f=23 a=9       1.174859       2.584599        6          290
FAST f=23 a=10       117.462222       2.580358        8          194
FAST f=23 a=10       1.075258       2.580358        8          194
FAST f=24 a=1       169.539659       2.581642        6          194
FAST f=24 a=1       1.916804       2.581642        6          194
FAST f=24 a=2       160.539270       2.580421        6          290
FAST f=24 a=2       1.71087       2.580421        6          290
FAST f=24 a=3       155.455874       2.580449        6          242
FAST f=24 a=3       1.60307       2.580449        6          242
FAST f=24 a=4       147.630320       2.582953        6          338
FAST f=24 a=4       1.396364       2.582953        6          338
FAST f=24 a=5       133.767428       2.580589        6          290
FAST f=24 a=5       1.19933       2.580589        6          290
FAST f=24 a=6       146.437535       2.579453        8          194
FAST f=24 a=6       1.385405       2.579453        8          194
FAST f=24 a=7       147.227507       2.584155        8          386
FAST f=24 a=7       1.48942       2.584155        8          386
FAST f=24 a=8       138.005773       2.584115        8          194
FAST f=24 a=8       1.352       2.584115        8          194
FAST f=24 a=9       141.442625       2.582902        8          290
FAST f=24 a=9       1.39647       2.582902        8          290
FAST f=24 a=10       142.157446       2.582701        8          434
FAST f=24 a=10       1.498889       2.582701        8          434
# Linux Kernel Patch

There are four pieces, the `xxhash` kernel module, the `zstd_compress` and `zstd_decompress` kernel modules, the BtrFS patch, and the SquashFS patch.
The patches are based off of the linux kernel master branch.

## xxHash kernel module

* The patch is located in `xxhash.diff`.
* The header is in `include/linux/xxhash.h`.
* The source is in `lib/xxhash.c`.
* `test/XXHashUserLandTest.cpp` contains tests for the patch in userland by mocking the kernel headers.
  I tested the tests by commenting a line of of each branch in `xxhash.c` one line at a time, and made sure the tests failed.
  It can be run with the following commands:
  ```
  cd test && make googletest && make XXHashUserLandTest && ./XXHashUserLandTest
  ```
* I also benchmarked the `xxhash` module against upstream xxHash, and made sure that they ran at the same speed.

## Zstd Kernel modules

* The (large) patch is located in `zstd.diff`, which depends on `xxhash.diff`.
* The header is in `include/linux/zstd.h`.
* It is split up into `zstd_compress` and `zstd_decompress`, which can be loaded independently.
* Source files are in `lib/zstd/`.
* `lib/Kconfig` and `lib/Makefile` need to be modified by applying `lib/Kconfig.diff` and `lib/Makefile.diff` respectively.
  These changes are also included in the `zstd.diff`.
* `test/UserlandTest.cpp` contains tests for the patch in userland by mocking the kernel headers.
  It can be run with the following commands:
  ```
  cd test && make googletest && make UserlandTest && ./UserlandTest
  ```

## BtrFS

* The patch is located in `btrfs.diff`.
* Additionally `fs/btrfs/zstd.c` is provided as a source for convenience.
* The patch seems to be working, it doesn't crash the kernel, and compresses at speeds and ratios that are expected.
  It could still use some more testing for fringe features, like printing options.

### Benchmarks

Benchmarks run on a Ubuntu 14.04 with 2 cores and 4 GiB of RAM.
The VM is running on a Macbook Pro with a 3.1 GHz Intel Core i7 processor,
16 GB of ram, and a SSD.
The kernel running was built from the master branch with the patch.

The compression benchmark is copying 10 copies of the
unzipped [silesia corpus](http://mattmahoney.net/dc/silesia.html) into a BtrFS
filesystem mounted with `-o compress-force={none, lzo, zlib, zstd}`.
The decompression benchmark is timing how long it takes to `tar` all 10 copies
into `/dev/null`.
The compression ratio is measured by comparing the output of `df` and `du`.
See `btrfs-benchmark.sh` for details.

| Algorithm | Compression ratio | Compression speed | Decompression speed |
|-----------|-------------------|-------------------|---------------------|
| None      | 0.99              | 504 MB/s          | 686 MB/s            |
| lzo       | 1.66              | 398 MB/s          | 442 MB/s            |
| zlib      | 2.58              | 65 MB/s           | 241 MB/s            |
| zstd 1    | 2.57              | 260 MB/s          | 383 MB/s            |
| zstd 3    | 2.71              | 174 MB/s          | 408 MB/s            |
| zstd 6    | 2.87              | 70 MB/s           | 398 MB/s            |
| zstd 9    | 2.92              | 43 MB/s           | 406 MB/s            |
| zstd 12   | 2.93              | 21 MB/s           | 408 MB/s            |
| zstd 15   | 3.01              | 11 MB/s           | 354 MB/s            |


## SquashFS

* The patch is located in `squashfs.diff`
* Additionally `fs/squashfs/zstd_wrapper.c` is provided as a source for convenience.
* The patch has been tested on the master branch of the kernel.

### Benchmarks

Benchmarks run on a Ubuntu 14.04 with 2 cores and 4 GiB of RAM.
The VM is running on a Macbook Pro with a 3.1 GHz Intel Core i7 processor,
16 GB of ram, and a SSD.
The kernel running was built from the master branch with the patch.

The compression benchmark is the file tree from the SquashFS archive found in the
Ubuntu 16.10 desktop image (ubuntu-16.10-desktop-amd64.iso).
The compression benchmark uses mksquashfs with the default block size (128 KB)
and various compression algorithms/compression levels.
`xz` and `zstd` are also benchmarked with 256 KB blocks.
The decompression benchmark is timing how long it takes to `tar` the file tree
into `/dev/null`.
See `squashfs-benchmark.sh` for details.

| Algorithm      | Compression ratio | Compression speed | Decompression speed |
|----------------|-------------------|-------------------|---------------------|
| gzip           | 2.92              |   15 MB/s         | 128 MB/s            |
| lzo            | 2.64              |  9.5 MB/s         | 217 MB/s            |
| lz4            | 2.12              |   94 MB/s         | 218 MB/s            |
| xz             | 3.43              |  5.5 MB/s         |  35 MB/s            |
| xz 256 KB      | 3.53              |  5.4 MB/s         |  40 MB/s            |
| zstd 1         | 2.71              |   96 MB/s         | 210 MB/s            |
| zstd 5         | 2.93              |   69 MB/s         | 198 MB/s            |
| zstd 10        | 3.01              |   41 MB/s         | 225 MB/s            |
| zstd 15        | 3.13              | 11.4 MB/s         | 224 MB/s            |
| zstd 16 256 KB | 3.24              |  8.1 MB/s         | 210 MB/s            |
gen_html - a program for automatic generation of zstd manual 
============================================================

#### Introduction

This simple C++ program generates a single-page HTML manual from `zstd.h`.

The format of recognized comment blocks is following:
- comments of type `/*!` mean: this is a function declaration; switch comments with declarations
- comments of type `/**` and `/*-` mean: this is a comment; use a `<H2>` header for the first line
- comments of type `/*=` and `/**=` mean: use a `<H3>` header and show also all functions until first empty line
- comments of type `/*X` where `X` is different from above-mentioned are ignored

Moreover:
- `ZSTDLIB_API` is removed to improve readability
- `typedef` are detected and included even if uncommented
- comments of type `/**<` and `/*!<` are detected and only function declaration is highlighted (bold)


#### Usage

The program requires 3 parameters:
```
gen_html [zstd_version] [input_file] [output_html]
```

To compile program and generate zstd manual we have used: 
```
make
./gen_html.exe 1.1.1 ../../lib/zstd.h zstd_manual.html
```

## Requirement

The `Dockerfile` script requires a version of `docker` >= 17.05

## Installing docker

The officiel docker install docs use a ppa with a modern version available:
https://docs.docker.com/install/linux/docker-ce/ubuntu/

## How to run

`docker build -t zstd .`

## test

```
echo foo | docker run -i --rm zstd | docker run -i --rm zstd zstdcat
foo
```
Programs and scripts for automated testing of Zstandard
=======================================================

This directory contains the following programs and scripts:
- `datagen` : Synthetic and parametrable data generator, for tests
- `fullbench`  : Precisely measure speed for each zstd inner functions
- `fuzzer`  : Test tool, to check zstd integrity on target platform
- `paramgrill` : parameter tester for zstd
- `test-zstd-speed.py` : script for testing zstd speed difference between commits
- `test-zstd-versions.py` : compatibility test between zstd versions stored on Github (v0.1+)
- `zbufftest`  : Test tool to check ZBUFF (a buffered streaming API) integrity
- `zstreamtest` : Fuzzer test tool for zstd streaming API
- `legacy` : Test tool to test decoding of legacy zstd frames
- `decodecorpus` : Tool to generate valid Zstandard frames, for verifying decoder implementations


#### `test-zstd-versions.py` - script for testing zstd interoperability between versions

This script creates `versionsTest` directory to which zstd repository is cloned.
Then all tagged (released) versions of zstd are compiled.
In the following step interoperability between zstd versions is checked.


#### `test-zstd-speed.py` - script for testing zstd speed difference between commits

This script creates `speedTest` directory to which zstd repository is cloned.
Then it compiles all branches of zstd and performs a speed benchmark for a given list of files (the `testFileNames` parameter).
After `sleepTime` (an optional parameter, default 300 seconds) seconds the script checks repository for new commits.
If a new commit is found it is compiled and a speed benchmark for this commit is performed.
The results of the speed benchmark are compared to the previous results.
If compression or decompression speed for one of zstd levels is lower than `lowerLimit` (an optional parameter, default 0.98) the speed benchmark is restarted.
If second results are also lower than `lowerLimit` the warning e-mail is send to recipients from the list (the `emails` parameter).

Additional remarks:
- To be sure that speed results are accurate the script should be run on a "stable" target system with no other jobs running in parallel
- Using the script with virtual machines can lead to large variations of speed results
- The speed benchmark is not performed until computers' load average is lower than `maxLoadAvg` (an optional parameter, default 0.75)
- The script sends e-mails using `mutt`; if `mutt` is not available it sends e-mails without attachments using `mail`; if both are not available it only prints a warning


The example usage with two test files, one e-mail address, and with an additional message:
```
./test-zstd-speed.py "silesia.tar calgary.tar" "email@gmail.com" --message "tested on my laptop" --sleepTime 60
```

To run the script in background please use:
```
nohup ./test-zstd-speed.py testFileNames emails &
```

The full list of parameters:
```
positional arguments:
  testFileNames         file names list for speed benchmark
  emails                list of e-mail addresses to send warnings

optional arguments:
  -h, --help            show this help message and exit
  --message MESSAGE     attach an additional message to e-mail
  --lowerLimit LOWERLIMIT
                        send email if speed is lower than given limit
  --maxLoadAvg MAXLOADAVG
                        maximum load average to start testing
  --lastCLevel LASTCLEVEL
                        last compression level for testing
  --sleepTime SLEEPTIME
                        frequency of repository checking in seconds
```

#### `decodecorpus` - tool to generate Zstandard frames for decoder testing
Command line tool to generate test .zst files.

This tool will generate .zst files with checksums,
as well as optionally output the corresponding correct uncompressed data for
extra verfication.

Example:
```
./decodecorpus -ptestfiles -otestfiles -n10000 -s5
```
will generate 10,000 sample .zst files using a seed of 5 in the `testfiles` directory,
with the zstd checksum field set,
as well as the 10,000 original files for more detailed comparison of decompression results.

```
./decodecorpus -t -T1mn
```
will choose a random seed, and for 1 minute,
generate random test frames and ensure that the
zstd library correctly decompresses them in both simple and streaming modes.

#### `paramgrill` - tool for generating compression table parameters and optimizing parameters on file given constraints

Full list of arguments
```
 -T#          : set level 1 speed objective
 -B#          : cut input into blocks of size # (default : single block)
 -S           : benchmarks a single run (example command: -Sl3w10h12)
    w# - windowLog
    h# - hashLog
    c# - chainLog
    s# - searchLog
    l# - minMatch
    t# - targetLength
    S# - strategy
    L# - level
 --zstd=      : Single run, parameter selection syntax same as zstdcli with more parameters
                    (Added forceAttachDictionary / fadt)
                    When invoked with --optimize, this represents the sample to exceed.
 --optimize=  : find parameters to maximize compression ratio given parameters
                    Can use all --zstd= commands to constrain the type of solution found in addition to the following constraints
    cSpeed=   : Minimum compression speed
    dSpeed=   : Minimum decompression speed
    cMem=     : Maximum compression memory
    lvl=      : Searches for solutions which are strictly better than that compression lvl in ratio and cSpeed,
    stc=      : When invoked with lvl=, represents percentage slack in ratio/cSpeed allowed for a solution to be considered (Default 100%)
              : In normal operation, represents percentage slack in choosing viable starting strategy selection in choosing the default parameters
                    (Lower value will begin with stronger strategies) (Default 90%)
    speedRatio=   (accepts decimals)
              : determines value of gains in speed vs gains in ratio
                    when determining overall winner (default 5 (1% ratio = 5% speed)).
    tries=    : Maximum number of random restarts on a single strategy before switching (Default 5)
                    Higher values will make optimizer run longer, more chances to find better solution.
    memLog    : Limits the log of the size of each memotable (1 per strategy). Will use hash tables when state space is larger than max size.
                    Setting memLog = 0 turns off memoization
 --display=   : specifiy which parameters are included in the output
                    can use all --zstd parameter names and 'cParams' as a shorthand for all parameters used in ZSTD_compressionParameters
                    (Default: display all params available)
 -P#          : generated sample compressibility (when no file is provided)
 -t#          : Caps runtime of operation in seconds (default : 99999 seconds (about 27 hours ))
 -v           : Prints Benchmarking output
 -D           : Next argument dictionary file
 -s           : Benchmark all files separately
 -q           : Quiet, repeat for more quiet
                  -q Prints parameters + results whenever a new best is found
                  -qq Only prints parameters whenever a new best is found, prints final parameters + results
                  -qqq Only print final parameters + results
                  -qqqq Only prints final parameter set in the form --zstd=
 -v           : Verbose, cancels quiet, repeat for more volume
                  -v Prints all candidate parameters and results

```
 Any inputs afterwards are treated as files to benchmark.
# Fuzzing

Each fuzzing target can be built with multiple engines.
Zstd provides a fuzz corpus for each target that can be downloaded with
the command:

```
make corpora
```

It will download each corpus into `./corpora/TARGET`.

## fuzz.py

`fuzz.py` is a helper script for building and running fuzzers.
Run `./fuzz.py -h` for the commands and run `./fuzz.py COMMAND -h` for
command specific help.

### Generating Data

`fuzz.py` provides a utility to generate seed data for each fuzzer.

```
make -C ../tests decodecorpus
./fuzz.py gen TARGET
```

By default it outputs 100 samples, each at most 8KB into `corpora/TARGET-seed`,
but that can be configured with the `--number`, `--max-size-log` and `--seed`
flags.

### Build
It respects the usual build environment variables `CC`, `CFLAGS`, etc.
The environment variables can be overridden with the corresponding flags
`--cc`, `--cflags`, etc.
The specific fuzzing engine is selected with `LIB_FUZZING_ENGINE` or
`--lib-fuzzing-engine`, the default is `libregression.a`.
It has flags that can easily set up sanitizers `--enable-{a,ub,m}san`, and
coverage instrumentation `--enable-coverage`.
It sets sane defaults which can be overriden with flags `--debug`,
`--enable-ubsan-pointer-overlow`, etc.
Run `./fuzz.py build -h` for help.

### Running Fuzzers

`./fuzz.py` can run `libfuzzer`, `afl`, and `regression` tests.
See the help of the relevant command for options.
Flags not parsed by `fuzz.py` are passed to the fuzzing engine.
The command used to run the fuzzer is printed for debugging.

## LibFuzzer

```
# Build libfuzzer if necessary
make libFuzzer
# Build the fuzz targets
./fuzz.py build all --enable-coverage --enable-asan --enable-ubsan --lib-fuzzing-engine Fuzzer/libFuzzer.a --cc clang --cxx clang++
# OR equivalently
CC=clang CXX=clang++ LIB_FUZZING_ENGINE=Fuzzer/libFuzzer.a ./fuzz.py build all --enable-coverage --enable-asan --enable-ubsan
# Run the fuzzer
./fuzz.py libfuzzer TARGET -max_len=8192 -jobs=4
```

where `TARGET` could be `simple_decompress`, `stream_round_trip`, etc.

### MSAN

Fuzzing with `libFuzzer` and `MSAN` will require building a C++ standard library
and libFuzzer with MSAN.
`fuzz.py` respects the environment variables / flags `MSAN_EXTRA_CPPFLAGS`,
`MSAN_EXTRA_CFLAGS`, `MSAN_EXTRA_CXXFLAGS`, `MSAN_EXTRA_LDFLAGS` to easily pass
the extra parameters only for MSAN.

## AFL

The default `LIB_FUZZING_ENGINE` is `libregression.a`, which produces a binary
that AFL can use.

```
# Build the fuzz targets
CC=afl-clang CXX=afl-clang++ ./fuzz.py build all --enable-asan --enable-ubsan
# Run the fuzzer without a memory limit because of ASAN
./fuzz.py afl TARGET -m none
```

## Regression Testing

The regression rest supports the `all` target to run all the fuzzers in one
command.

```
CC=clang CXX=clang++ ./fuzz.py build all --enable-asan --enable-ubsan
./fuzz.py regression all
CC=clang CXX=clang++ ./fuzz.py build all --enable-msan
./fuzz.py regression all
```
Zstandard Documentation
=======================

This directory contains material defining the Zstandard format,
as well as detailed instructions to use `zstd` library.

__`zstd_manual.html`__ : Documentation of `zstd.h` API, in html format.
Click on this link: [http://zstd.net/zstd_manual.html](http://zstd.net/zstd_manual.html)
to display documentation of latest release in readable format within a browser.

__`zstd_compression_format.md`__ : This document defines the Zstandard compression format.
Compliant decoders must adhere to this document,
and compliant encoders must generate data that follows it.

Should you look for ressources to develop your own port of Zstandard algorithm,
you may find the following ressources useful :

__`educational_decoder`__ : This directory contains an implementation of a Zstandard decoder,
compliant with the Zstandard compression format.
It can be used, for example, to better understand the format,
or as the basis for a separate implementation of Zstandard decoder.

[__`decode_corpus`__](https://github.com/facebook/zstd/tree/dev/tests#decodecorpus---tool-to-generate-zstandard-frames-for-decoder-testing) :
This tool, stored in `/tests` directory, is able to generate random valid frames,
which is useful if you wish to test your decoder and verify it fully supports the specification.
Educational Decoder
===================

`zstd_decompress.c` is a self-contained implementation in C99 of a decoder,
according to the [Zstandard format specification].
While it does not implement as many features as the reference decoder,
such as the streaming API or content checksums, it is written to be easy to
follow and understand, to help understand how the Zstandard format works.
It's laid out to match the [format specification],
so it can be used to understand how complex segments could be implemented.
It also contains implementations of Huffman and FSE table decoding.

[Zstandard format specification]: https://github.com/facebook/zstd/blob/dev/doc/zstd_compression_format.md
[format specification]: https://github.com/facebook/zstd/blob/dev/doc/zstd_compression_format.md

`harness.c` provides a simple test harness around the decoder:

    harness <input-file> <output-file> [dictionary]

As an additional resource to be used with this decoder,
see the `decodecorpus` tool in the [tests] directory.
It generates valid Zstandard frames that can be used to verify
a Zstandard decoder implementation.
Note that to use the tool to verify this decoder implementation,
the --content-size flag should be set,
as this decoder does not handle streaming decoding,
and so it must know the decompressed size in advance.

[tests]: https://github.com/facebook/zstd/blob/dev/tests/
Zstandard wrapper for zlib
================================

The main objective of creating a zstd wrapper for [zlib](http://zlib.net/) is to allow a quick and smooth transition to zstd for projects already using zlib.

#### Required files

To build the zstd wrapper for zlib the following files are required:
- zlib.h
- a static or dynamic zlib library
- zlibWrapper/zstd_zlibwrapper.h
- zlibWrapper/zstd_zlibwrapper.c
- zlibWrapper/gz*.c files (gzclose.c, gzlib.c, gzread.c, gzwrite.c)
- zlibWrapper/gz*.h files (gzcompatibility.h, gzguts.h)
- a static or dynamic zstd library

The first two files are required by all projects using zlib and they are not included with the zstd distribution.
The further files are supplied with the zstd distribution.


#### Embedding the zstd wrapper within your project

Let's assume that your project that uses zlib is compiled with:
```gcc project.o -lz```

To compile the zstd wrapper with your project you have to do the following:
- change all references with `#include "zlib.h"` to `#include "zstd_zlibwrapper.h"`
- compile your project with `zstd_zlibwrapper.c`, `gz*.c` and a static or dynamic zstd library

The linking should be changed to:
```gcc project.o zstd_zlibwrapper.o gz*.c -lz -lzstd```


#### Enabling zstd compression within your project

After embedding the zstd wrapper within your project the zstd library is turned off by default.
Your project should work as before with zlib. There are two options to enable zstd compression:
- compilation with `-DZWRAP_USE_ZSTD=1` (or using `#define ZWRAP_USE_ZSTD 1` before `#include "zstd_zlibwrapper.h"`)
- using the `void ZWRAP_useZSTDcompression(int turn_on)` function (declared in `#include "zstd_zlibwrapper.h"`)

During decompression zlib and zstd streams are automatically detected and decompressed using a proper library.
This behavior can be changed using `ZWRAP_setDecompressionType(ZWRAP_FORCE_ZLIB)` what will make zlib decompression slightly faster.


#### Example
We have take the file `test/example.c` from [the zlib library distribution](http://zlib.net/) and copied it to [zlibWrapper/examples/example.c](examples/example.c).
After compilation and execution it shows the following results: 
```
zlib version 1.2.8 = 0x1280, compile flags = 0x65
uncompress(): hello, hello!
gzread(): hello, hello!
gzgets() after gzseek:  hello!
inflate(): hello, hello!
large_inflate(): OK
after inflateSync(): hello, hello!
inflate with dictionary: hello, hello!
```
Then we have changed `#include "zlib.h"` to `#include "zstd_zlibwrapper.h"`, compiled the [example.c](examples/example.c) file
with `-DZWRAP_USE_ZSTD=1` and linked with additional `zstd_zlibwrapper.o gz*.c -lzstd`.
We were forced to turn off the following functions: `test_flush`, `test_sync` which use currently unsupported features.
After running it shows the following results:
```
zlib version 1.2.8 = 0x1280, compile flags = 0x65
uncompress(): hello, hello!
gzread(): hello, hello!
gzgets() after gzseek:  hello!
inflate(): hello, hello!
large_inflate(): OK
inflate with dictionary: hello, hello!
```
The script used for compilation can be found at [zlibWrapper/Makefile](Makefile).


#### The measurement of performace of Zstandard wrapper for zlib

The zstd distribution contains a tool called `zwrapbench` which can measure speed and ratio of zlib, zstd, and the wrapper.
The benchmark is conducted using given filenames or synthetic data if filenames are not provided.
The files are read into memory and processed independently.
It makes benchmark more precise as it eliminates I/O overhead. 
Many filenames can be supplied as multiple parameters, parameters with wildcards or names of directories can be used as parameters with the -r option.
One can select compression levels starting from `-b` and ending with `-e`. The `-i` parameter selects minimal time used for each of tested levels.
With `-B` option bigger files can be divided into smaller, independently compressed blocks. 
The benchmark tool can be compiled with `make zwrapbench` using [zlibWrapper/Makefile](Makefile).


#### Improving speed of streaming compression

During streaming compression the compressor never knows how big is data to compress.
Zstandard compression can be improved by providing size of source data to the compressor. By default streaming compressor assumes that data is bigger than 256 KB but it can hurt compression speed on smaller data. 
The zstd wrapper provides the `ZWRAP_setPledgedSrcSize()` function that allows to change a pledged source size for a given compression stream.
The function will change zstd compression parameters what may improve compression speed and/or ratio.
It should be called just after `deflateInit()`or `deflateReset()` and before `deflate()` or `deflateSetDictionary()`. The function is only helpful when data is compressed in blocks. There will be no change in case of `deflateInit()` or `deflateReset()`  immediately followed by `deflate(strm, Z_FINISH)`
as this case is automatically detected.


#### Reusing contexts

The ordinary zlib compression of two files/streams allocates two contexts:
- for the 1st file calls `deflateInit`, `deflate`, `...`, `deflate`, `defalateEnd`
- for the 2nd file calls `deflateInit`, `deflate`, `...`, `deflate`, `defalateEnd`

The speed of compression can be improved with reusing a single context with following steps:
- initialize the context with `deflateInit`
- for the 1st file call `deflate`, `...`, `deflate`
- for the 2nd file call `deflateReset`, `deflate`, `...`, `deflate`
- free the context with `deflateEnd`

To check the difference we made experiments using `zwrapbench -ri6b6` with zstd and zlib compression (both at level 6).
The input data was decompressed git repository downloaded from https://github.com/git/git/archive/master.zip which contains 2979 files.
The table below shows that reusing contexts has a minor influence on zlib but it gives improvement for zstd.
In our example (the last 2 lines) it gives 4% better compression speed and 5% better decompression speed.

| Compression type                                  | Compression | Decompress.| Compr. size | Ratio |
| ------------------------------------------------- | ------------| -----------| ----------- | ----- |
| zlib 1.2.8                                        |  30.51 MB/s | 219.3 MB/s |     6819783 | 3.459 |
| zlib 1.2.8 not reusing a context                  |  30.22 MB/s | 218.1 MB/s |     6819783 | 3.459 |
| zlib 1.2.8 with zlibWrapper and reusing a context |  30.40 MB/s | 218.9 MB/s |     6819783 | 3.459 |
| zlib 1.2.8 with zlibWrapper not reusing a context |  30.28 MB/s | 218.1 MB/s |     6819783 | 3.459 |
| zstd 1.1.0 using ZSTD_CCtx                        |  68.35 MB/s | 430.9 MB/s |     6868521 | 3.435 |
| zstd 1.1.0 using ZSTD_CStream                     |  66.63 MB/s | 422.3 MB/s |     6868521 | 3.435 |
| zstd 1.1.0 with zlibWrapper and reusing a context |  54.01 MB/s | 403.2 MB/s |     6763482 | 3.488 |
| zstd 1.1.0 with zlibWrapper not reusing a context |  51.59 MB/s | 383.7 MB/s |     6763482 | 3.488 |


#### Compatibility issues
After enabling zstd compression not all native zlib functions are supported. When calling unsupported methods they put error message into `strm->msg` and return Z_STREAM_ERROR.

Supported methods:
- deflateInit
- deflate (with exception of Z_FULL_FLUSH, Z_BLOCK, and Z_TREES)
- deflateSetDictionary
- deflateEnd
- deflateReset
- deflateBound
- inflateInit
- inflate
- inflateSetDictionary
- inflateReset
- inflateReset2
- compress
- compress2
- compressBound
- uncompress
- gzip file access functions

Ignored methods (they do nothing):
- deflateParams

Unsupported methods:
- deflateCopy
- deflateTune
- deflatePending
- deflatePrime
- deflateSetHeader
- inflateGetDictionary
- inflateCopy
- inflateSync
- inflatePrime
- inflateMark
- inflateGetHeader
- inflateBackInit
- inflateBack
- inflateBackEnd
Projects for various integrated development environments (IDE)
==============================================================

#### Included projects

The following projects are included with the zstd distribution:
- `cmake` - CMake project contributed by Artyom Dymchenko
- `VS2005` - Visual Studio 2005 Project (this project has been moved to the contrib directory and will no longer be supported)
- `VS2008` - Visual Studio 2008 project
- `VS2010` - Visual Studio 2010 project (which also works well with Visual Studio 2012, 2013, 2015)
- `VS_scripts` - command line scripts prepared for Visual Studio compilation without IDE


#### How to compile zstd with Visual Studio

1. Install Visual Studio e.g. VS 2015 Community Edition (it's free).
2. Download the latest version of zstd from https://github.com/facebook/zstd/releases
3. Decompress ZIP archive.
4. Go to decompressed directory then to `projects` then `VS2010` and open `zstd.sln`
5. Visual Studio will ask about converting VS2010 project to VS2015 and you should agree.
6. Change `Debug` to `Release` and if you have 64-bit Windows change also `Win32` to `x64`.
7. Press F7 on keyboard or select `BUILD` from the menu bar and choose `Build Solution`.
8. If compilation will be fine a compiled executable will be in `projects\VS2010\bin\x64\Release\zstd.exe`


#### Projects available within zstd.sln

The Visual Studio solution file `visual\VS2010\zstd.sln` contains many projects that will be compiled to the
`visual\VS2010\bin\$(Platform)_$(Configuration)` directory. For example `zstd` set to `x64` and
`Release` will be compiled to `visual\VS2010\bin\x64_Release\zstd.exe`. The solution file contains the
following projects:

- `zstd` : Command Line Utility, supporting gzip-like arguments
- `datagen` : Synthetic and parametrable data generator, for tests
- `fullbench`  : Precisely measure speed for each zstd inner functions
- `fuzzer` : Test tool, to check zstd integrity on target platform 
- `libzstd` : A static ZSTD library compiled to `libzstd_static.lib`
- `libzstd-dll` : A dynamic ZSTD library (DLL) compiled to `libzstd.dll` with the import library `libzstd.lib`
- `fullbench-dll` : The fullbench program compiled with the import library; the executable requires ZSTD DLL


#### Using ZSTD DLL with Microsoft Visual C++ project

The header file `lib\zstd.h` and the import library
`visual\VS2010\bin\$(Platform)_$(Configuration)\libzstd.lib` are required to compile
a project using Visual C++.

1. The path to header files should be added to `Additional Include Directories` that can
   be found in Project Properties of Visual Studio IDE in the `C/C++` Property Pages on the `General` page.
2. The import library has to be added to `Additional Dependencies` that can
   be found in Project Properties in the `Linker` Property Pages on the `Input` page.
   If one will provide only the name `libzstd.lib` without a full path to the library
   then the directory has to be added to `Linker\General\Additional Library Directories`.

The compiled executable will require ZSTD DLL which is available at
`visual\VS2010\bin\$(Platform)_$(Configuration)\libzstd.dll`. 
Command line scripts for Visual Studio compilation without IDE
==============================================================

Here are a few command lines for reference :

### Build with Visual Studio 2013 for msvcr120.dll

Running the following command will build both the `Release Win32` and `Release x64` versions:
```batch
build.VS2013.cmd
```
The result of each build will be in the corresponding `bin\Release\{ARCH}\` folder.

If you want to only need one architecture:
- Win32: `build.generic.cmd VS2013 Win32 Release v120`
- x64: `build.generic.cmd VS2013 x64 Release v120`

If you want a Debug build:
- Win32: `build.generic.cmd VS2013 Win32 Debug v120`
- x64: `build.generic.cmd VS2013 x64 Debug v120`

### Build with Visual Studio 2015 for msvcr140.dll

Running the following command will build both the `Release Win32` and `Release x64` versions:
```batch
build.VS2015.cmd
```
The result of each build will be in the corresponding `bin\Release\{ARCH}\` folder.

If you want to only need one architecture:
- Win32: `build.generic.cmd VS2015 Win32 Release v140`
- x64: `build.generic.cmd VS2015 x64 Release v140`

If you want a Debug build:
- Win32: `build.generic.cmd VS2015 Win32 Debug v140`
- x64: `build.generic.cmd VS2015 x64 Debug v140`

### Build with Visual Studio 2015 for msvcr120.dll

This capability is offered through `build.generic.cmd` using proper arguments:

**For Win32**
```batch
build.generic.cmd VS2015 Win32 Release v120
```
The result of the build will be in the `bin\Release\Win32\` folder.

**For x64**
```batch
build.generic.cmd VS2015 x64 Release v120
```
The result of the build will be in the `bin\Release\x64\` folder.

If you want Debug builds, replace `Release` with `Debug`.

### Build with Visual Studio 2017

`build.VS2017.cmd`, contributed by [@HaydnTrigg](https://github.com/HaydnTrigg),
will build both the `Release Win32` and `Release x64` versions
of the first VS2017 variant it finds, in this priority order :
Enterprise > Professional > Community

Alternatively, it's possible to target a specific version,
using appropriate script, such as `build.VS2017Enterprise.cmd` for example.
Meson build system for zstandard
================================

Meson is a build system designed to optimize programmer productivity.
It aims to do this by providing simple, out-of-the-box support for
modern software development tools and practices, such as unit tests,
coverage reports, Valgrind, CCache and the like.

This Meson build system is provided with no guarantee and maintained
by Dima Krasner \<dima@dimakrasner.com\>.

It outputs one `libzstd`, either shared or static, depending on
`default_library` option.

## How to build

`cd` to this meson directory (`build/meson`)

```sh
meson --buildtype=release -Dbuild_{programs,contrib}=true builddir
cd builddir
ninja             # to build
ninja install     # to install
```

You might want to install it in staging directory:

```sh
DESTDIR=./staging ninja install
```

To configure build options, use:

```sh
meson configure
```

See [man meson(1)](https://manpages.debian.org/testing/meson/meson.1.en.html).
# Cmake contributions

Contributions to the cmake build configurations are welcome. Please
use case sensitivity that matches modern (ie. cmake version 2.6 and above)
conventions of using lower-case for commands, and upper-case for
varibles.

# CMake Style Recommendations

## Indent all code correctly, i.e. the body of

 * if/else/endif
 * foreach/endforeach
 * while/endwhile
 * macro/endmacro
 * function/endfunction

Use spaces for indenting, 2, 3 or 4 spaces preferably. Use the same amount of
spaces for indenting as is used in the rest of the file. Do not use tabs.

## Upper/lower casing

Most important: use consistent upper- or lowercasing within one file !

In general, the all-lowercase style is preferred.

So, this is recommended:

```
add_executable(foo foo.c)
```

These forms are discouraged

```
ADD_EXECUTABLE(bar bar.c)
Add_Executable(hello hello.c)
aDd_ExEcUtAbLe(blub blub.c)
```

## End commands
To make the code easier to read, use empty commands for endforeach(), endif(),
endfunction(), endmacro() and endwhile(). Also, use empty else() commands.

For example, do this:

```
if(FOOVAR)
   some_command(...)
else()
   another_command(...)
endif()
```

and not this:

```
if(BARVAR)
   some_other_command(...)
endif(BARVAR)
```

## Other resources for best practices

`https://cmake.org/cmake/help/latest/manual/cmake-developer.7.html#modules`
