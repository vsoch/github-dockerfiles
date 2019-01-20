# Supplemental Information - Phenomenological Model #

The tutorial for the phenomenological model can be viewed and
generated in various different formats. It's recommended to run
everything in the virtual machine defined in our
[Vagrantfile](https://github.com/strawlab/asymmetric-motion/blob/master/Vagrantfile).
Everything is described in detail there.

If you intend to run it on your own machine, you need to
fulfill the following requirements:

## Requirements ##


### Generate figures only ###

Make sure you have the following installed:

 * Python version >=2.7.3, <3.x
 * numpy >=1.7.1
 * matplotlib >=1.3.0
 * sympy >=0.7.1.rc1
 * scipy >=0.9.0

Generate the figures with:
```
python phenomenological_model_tutorial_code.py
```

Display the figure interactively with:
```
python phenomenological_model_tutorial_code.py --show
```


### Generate the PDF from the markdown file ###

You need to have everything installed to create the figures.
And you need additional packages. If you are on _Ubuntu 14.04_,
install the following packages:

 * texlive-fonts-recommended
 * texlive-latex-extra
 * texlive-latex-base
 * inkscape
 * pandoc
 * jq

For other distributions check with your package-manager.
Make sure that your _pandoc_ version is >=1.11.

Then just run:
```
make pdf-standalone
```


### Generate and run the ipython notebook ###

You need to have everything installed to generate the PDF.
And you need additional packages. If you are on _Ubuntu 14.04_,
install the following packages:

 * ipython
 * ipython-notebook

For other distributions check with your package-manager.
Make sure that your _ipython_ version is >=1.0.0.

To generate the ipython notebook and launch the ipython notebook
server, run:
```
make ipynb
ipython notebook
```

Your default browser will open up and display the notebook.

# Supplemental Information - physiological model #

All figures based on simulations with the EMD model can be generated
with this code.  It will run in the virtual machine defined in our
[Vagrantfile](https://github.com/strawlab/asymmetric-motion/blob/master/Vagrantfile).
Everything is described in detail there.

We recommend running this code natively on a multiprocessor machine
with all required packages installed.

On a 24 core (2x Intel(R) Xeon(R) CPU E5-2630 v2 @ 2.60GHz)
machine generating all data takes about 3 hours.

If you intend to run it on your own machine, you need to
fulfill the following requirements:


## Requirements ##


### Generate figures ###

Make sure you have the following installed:

 * Python version >=2.7.3, <3.x
 * numpy >=1.7.1
 * matplotlib >=1.3.0
 * h5py >=2.0.1
 * scipy >=0.9.0
 * progressbar >=2.3

Generate figure data with:
```
python calculate_figure_data.py
```

When the figure data is calculated, display the figures interactively with:
```
python plot_figure3B_bottom.py
python plot_figure3B_top.py
python plot_figureS3.py
```

