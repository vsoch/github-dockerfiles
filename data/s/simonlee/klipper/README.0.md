This directory contains external library code.

The cmsis directory contains code from:
  https://github.com/ARM-software/CMSIS_5
version 5.3.0 (49ac527aa7406cecbba46d4d3bdbc7f60c6c6d42). Contents
taken from the CMSIS/Core/Include/ directory.

The sam3x directory contains code from the
Atmel.SAM3X_DFP.1.0.50.atpack zip file found at:
  http://packs.download.atmel.com/
version 1.0.50 (extracted on 20180725). It has been modified to
compile with gcc's LTO feature. See sam3x.patch for the modifications.

The samd21 directory contains code from the
Atmel.SAMD21_DFP.1.3.304.atpack zip file found at:
  http://packs.download.atmel.com/
version 1.3.304 (extracted on 20180725). It has been modified to
compile with gcc's LTO feature and to work with chips that have a
bootloader. See samd21.patch for the modifications.

The cmsis-sam4e8e directory contains code from the
Atmel.SAM4E_DFP.1.1.57.atpack zip file found at:
  http://packs.download.atmel.com/
version 1.1.57 (extracted on 20180806). It has been modified to compile
with gcc's LTO feature. Also, some AFEC register RW accesses have been modified
to comply with the SAM4E datasheet. Finally, the interrupt vector table has
been slightly modified to allow the code to run. See cmsis-sam4e8e.patch for the modifications.

The lpc176x directory contains code from the mbed project:
  https://github.com/ARMmbed/mbed-os
version mbed-os-5.8.3 (c05d72c3c005fbb7e92c3994c32bda45218ae7fe).
Contents taken from the targets/TARGET_NXP/TARGET_LPC176X/ directory.
It has been modified to compile with gcc's LTO feature and to use
appropriate clock speeds on the LPC1768 and LPC1769. See lpc176x.patch
for the modifications.

The cmsis-stm32f1 and the hal-stm32f1 directories contain code from
STMicroelectronics:
  http://www.st.com/en/embedded-software/stm32cubef1.html
version 1.6.0 (extracted 20180330).

The hub-ctrl directory contains code from:
  https://github.com/codazoda/hub-ctrl.c/
revision 42095e522859059e8a5f4ec05c1e3def01a870a9.

The bossac directory contains code from:
  https://github.com/shumatech/BOSSA
version 1.9 (b176eeef918fc810045c832348590595120187b4).

The pru_rpmsg directory contains code from:
  https://github.com/dinuxbg/pru-gcc-examples
revision 425a42d82006cf0aa24be27b483d2f6a41607489. The code is taken
from the repo's hc-sr04-range-sensor directory. It has been modified
so that the IEP definitions compile correctly. See pru_rpmsg.patch for
the modifications.
Welcome to the Klipper documentation. The
[overview document](Overview.md) is a good starting point.
