The `firmware` package contains updated firmware files required by any
driver compiled as a module. Based on the modules included in a recent
LinuxKit kernel, copy the required firmware binaries as reported by
'modinfo'. We deliberately do *not* pick the latest version here to
prevent it being updated on kernel updates. Firmware revisions do not
change very often and we expect older and newer kernels to work with a
range of firmware binaries.

Note: The current mechanism only handles firmware blobs required by
modules and ignores firmware blobs required by drivers compiled into
the kernel. However, with the LinuxKit kernels we typically compile
all hardware drivers as modules.
The `firmware-all` package contains all firmware binaries from the
[Linux firmware
repository](https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/). It
is quite large.

For use with the LinuxKit kernel we recommend using the
[`firmware`](../firmware/) package, which only contains the firmware
binaries for which drivers are enabled.
