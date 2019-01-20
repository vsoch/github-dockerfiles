# Build

## Build Linux amd64 executable and deb package

Requires vagrant and fpm:

    make

If you want to bump the version you should adjust the version values in both
check-graph.cabal and the Makefile.

## Build Docker container

    make docker-run

## Runtime Dependencies

    $ ldd /usr/src/graph-check/dist/build/check_graph/check_graph
    linux-vdso.so.1 =>  (0x00007ffff8518000)
    libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x00007f037f835000)
    librt.so.1 => /lib/x86_64-linux-gnu/librt.so.1 (0x00007f037f62d000)
    libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007f037f428000)
    libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007f037f20b000)
    libgmp.so.10 => /usr/lib/x86_64-linux-gnu/libgmp.so.10 (0x00007f037ef9d000)
    libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f037eca0000)
    libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f037e8e1000)
    /lib64/ld-linux-x86-64.so.2 (0x00007f037fa52000)

# Upload to S3 apt repo

Requires deb-s3

    deb-s3 upload -a amd64 --bucket knewton-apt check-graph_0.4.2_amd64.deb

The `knewton-apt` bucket is in the VPC account.

# Install

## Ubuntu

Add our apt repo, then:

    sudo apt-get install check-graph

You can also scp the deb package somewhere, run:

    sudo dpkg -i check-graph_0.4.2_amd64.deb

The first install might fail and register some packages as dependencies, which
will then be installed if you do:

    sudo apt-get install -f
    sudo dpkg -i check-graph_0.4.2_amd64.deb
