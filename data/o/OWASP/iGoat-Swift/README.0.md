This folder contains some sample formatters that may be helpful.

Feel free to change them, extend them, or use them as the basis for your own custom formatter(s).

More information about creating your own custom formatters can be found on the wiki:
https://github.com/CocoaLumberjack/CocoaLumberjack/wiki/CustomFormatters

===============================================================================
iGoat Server
-------------------------------------------------------------------------------

ABOUT

This file contains a very simple web server used by iGoat in some of
its exercises. It is a special purpose web server for very specific
purposes, not anything for general purpose use. It takes a specially
constructed input from iGoat, and responds back with information
needed by iGoat.

REQUIREMENTS

Most of what you'll need to run the server already comes with the default OS X
install (Ruby, etc.), but there are a few external gem requirements, which you
can install with the following command:

sudo gem install sinatra json

RUNNING

Simply invoke the igoat-server.rb script from the Terminal...

./igoat-server.rb

Ctrl-C to quit.

FURTHER DETAILS

See the comments in the script itself for ports, endpoints, etc.

And of course: ken@krvw.com, sean@krvw.com

******************************************************************************

 This file is part of iGoat, an Open Web Application Security
 Project tool. For details, please see http://www.owasp.org

 Copyright(c) 2013 KRvW Associates, LLC (http://www.krvw.com)
 The iGoat project is principally sponsored by KRvW Associates, LLC
 Project Leader, Kenneth R. van Wyk (ken@krvw.com)
 Lead Developer: Sean Eidemiller (sean@krvw.com)

 iGoat is free software; you may redistribute it and/or modify it
 under the terms of the GNU General Public License as published by
 the Free Software Foundation; version 3.

 iGoat is distributed in the hope it will be useful, but WITHOUT ANY
 WARRANTY; without even the implied warranty of MERCHANTABILITY or
 FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public
 License for more details.

 You should have received a copy of the GNU General Public License
 along with this program; if not, write to the Free Software
 Foundation, Inc. 59 Temple Place, suite 330, Boston, MA 02111-1307
 USA.

 Source Code: http://code.google.com/p/owasp-igoat/
 Project Home: https://www.owasp.org/index.php/OWASP_iGoat_Project

******************************************************************************
