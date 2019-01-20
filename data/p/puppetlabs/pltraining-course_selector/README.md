## Course Selector for Puppet Education VMs

This module installs and manages the course_selector script that we use for putting starter code on to the Puppetlabs Education VMs.

Because that code needs to dynamically update, the module will actually pull the lastest master branch from github when the script runs.  This is done via the file `file/scripts/update.pp` and may need to be refactored in the future.
