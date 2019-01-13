To build this images:
1) Add the following files to the "dockerfile_copy" directory:
- jboss-bpmsuite-6.2.0.GA-deployable-eap6.x.zip
- jboss-bpmsuite-6.2.0.GA-maven-repository.zip
- jboss-bpmsuite-6.2.0.GA-supplementary-tools.zip
2) Run the "prebuild-prepare.sh" script, which will create a PostgreSQL EAP module ZIP.
3) Run "build_image.sh".

