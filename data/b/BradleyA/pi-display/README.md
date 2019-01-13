# pi-display

This repository contains shell scripts and python for RaspBerry Pi display project.  The displays are Pimoroni Blinkt, Scroll-pHAT, and Scroll-pHAT-HD connected to Raspberry Pi 3 using Triple GPIO Multiplexing Expansion Board. 

 <img id="image_respberry_scroll-phat" src="images/IMG_3247.JPG" width="450" >

----> ![Click this link, then click 'view raw' to see board running](images/IMG_3246.MOV)

#### WARNING: These instructions are incomplete. Consider them as notes quickly drafted on a napkin rather than proper documentation!

#### If you like this repository, select in the upper-right corner, star, thank you.
#### To watch future updates in this repository select in the upper-right corner, the "Watch" list, and select Watching.

 * [scrollphat](https://github.com/BradleyA/pi-display/tree/master/scrollphat) 
 * [scrollphathd](https://github.com/BradleyA/pi-display/tree/master/scrollphathd)
 * [blinkt](https://github.com/BradleyA/pi-display-board/tree/master/blinkt)
 
### Architecture

<img id="pi-display architecture" src="images/pi-display-architecture.png" width="900" >
 
<img id="image_respberry_setup" src="images/IMG_2803.JPG" width="450" >

I need to get this to work and completed then some cleanup before it is shareable and documented . . .


### Install

### Clone

To install, change directory to the location you want to download the scripts. Use git to pull or clone these scripts into the directory. If you do not have git then enter; "sudo apt-get install git". On the github page of this script use the "HTTPS clone URL" with the 'git clone' command.

    git clone https://github.com/BradleyA/pi-display
    cd pi-display
   
### System OS script tested

 * Ubuntu 16.04.3-5 LTS (armv7l)

### Design Principles
 * Have a simple setup process and a minimal learning curve
 * Be usable as non-root
 * Be easy to install and configure

## License
MIT License

Copyright (c) 2019  Bradley Allen

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
