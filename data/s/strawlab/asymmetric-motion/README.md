## Asymmetric processing of visual motion for simultaneous object and background responses ##

Please check for updated versions at [http://strawlab.org/asymmetric-motion/](http://strawlab.org/asymmetric-motion/)

### Contents ###

* tutorial-src  phenomenological model source code and explanatory text
* emd-src       physiologically based EMD model

### Supplemental Code - Quick start ###

You can either chose to run all code on your physical machine (please
refer to the README documents in the specific folder) or you can run
the code in a predefined virtual machine, where it's known to work.

For the second option please install the following programs first:

 * [Virtualbox](https://www.virtualbox.org)
 * [vagrant](http://www.vagrantup.com)

Then access this folder with your operating systems terminal (command
line) and type:

```
vagrant up
```

Wait for the above to finish, which can take a long time (about 2GB of
files need to be downloaded).

### Lauching the IPython notebook ###

After `vagrant up` finishes, your newly installed virtual machine is
running the IPython Notebook server in which you can interactively run
and edit the code. Do by visiting the following URL in your browser:
[http://localhost:8888/](http://localhost:8888/).

### Building PDF versions of the documentation ###

```
vagrant ssh
cd /vagrant/tutorial-src
make pdf-standalone
exit
```

This generates the supplemental experimental procedures text and
figures for the phenomenological model. You'll find them in the
tutorial-src folder when the program is finished.

And:

```
vagrant ssh
cd /vagrant/emd-src
python calculate_figure_data.py
python save_plots_as_pdf.py
exit
```

This generates the all figures for the EMD model. It will take a
very long time (on a single core >40 hours) when run in the virtual
machine. You'll find the generated figures in the emd-src folder after
the program is finished. It is recommended to run the EMD code on a
multi-processor machine natively (refer to the README document in the
emd-src folder).
