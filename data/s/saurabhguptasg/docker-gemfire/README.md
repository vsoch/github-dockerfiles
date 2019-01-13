docker-gemfire
==============

gemfire dockerfile

How to use these files
* get the gemfire .zip distribution
* unzip the file and remove all extraneous items (documentation, sample code, etc.) (Let's call the directory `Pivotal_GemFire_800_b48398_Linux_min`)
* run the tar command: `tar -cf Pivotal_GemFire_800_b48398_Linux_min.tar Pivotal_GemFire_800_b48398_Linux_min/`
* the above tar file can now be used to build the base image: copy it into the gemfire-base directory

first build a base image (from the gemfire-base directory):
`docker build -t pivotal/gemfire-base .`

the new image will now be in your local store:
`docker images`
if the above list is too long, you can `grep` for `pivotal`

now switch to the gemfire-locator directory and build the locator image:
`docker build -t pivotal/gemfire-locator`

the new image will now be in your local store:
`docker images`
if the above list is too long, you can `grep` for `pivotal`

run the locator:
`docker run -p 10335:11222 -d pivotal/gemfire-locator`
This will run the locator image and map it to the port 11222 on the host machine

you can now start gfsh from your host machine (if you have it installed there already):
`gfsh`
at the gfsh command, set the following:
`connect --locator=localhost[11222]`

you can then see gfsh connect to the locator, and can issue this command to see all the members:
`list members`
for output like:

`  Name   | Id                                                `
` -------- | -------------------------------------------------`
` locator1 | SaurabhGuptaMBP(locator1:79225:locator)<v0>:29532`

 ### NOTE: the server `Dockerfile` is not done yet :)
 you can shut down the locator from gfsh
