# Distance-regular graph parameter checking in Sage

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1418410.svg)](https://doi.org/10.5281/zenodo.1418410)

[![Launch in Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jaanos/sage-drg/master?filepath=index.ipynb)

A Sage package for checking the feasibility of distance-regular graph parameter sets.
A more detailed description, along with some results, is available in a [manuscript](https://arxiv.org/abs/1803.10797) currently available on arXiv.


## Contents

### `drg`

The `drg` folder contains the package source. After you make sure that Sage sees this folder, you can import it as a Python module.
```python
sage: import drg
sage: p = drg.DRGParameters([80, 63, 12], [1, 12, 60])
sage: p.check_feasible()
```

You can also give an intersection array with parameters.
```python
sage: r = var("r")
sage: fam = drg.DRGParameters([2*r^2*(2*r + 1), (2*r - 1)*(2*r^2 + r + 1), 2*r^2], [1, 2*r^2 , r*(4*r^2 - 1)])
sage: fam.check_feasible()
sage: fam1 = fam.subs(r == 1)
sage: fam1
Parameters of a distance-regular graph with intersection array {6, 4, 2; 1, 2, 3}
sage: fam2 = fam.subs(r == 2)
sage: fam2
Parameters of a distance-regular graph with intersection array {40, 33, 8; 1, 8, 30}
sage: fam2.check_feasible()
...
InfeasibleError: nonexistence by JurišićVidali12
```

### [`jupyter`](jupyter)

A collection of sample Jupyter notebooks giving some nonexistence results.


## Citing

If you use `sage-drg` in your research, please cite both the manuscript and the repository:

* J. Vidali. Using symbolic computation to prove nonexistence of distance-regular graphs. *Electron. J. Combin.*, 25(4)#P4.21, 2018. [`http://www.combinatorics.org/ojs/index.php/eljc/article/view/v25i4p21`](http://www.combinatorics.org/ojs/index.php/eljc/article/view/v25i4p21).

* J. Vidali. `jaanos/sage-drg`: `sage-drg` v0.8, 2018. [`https://github.com/jaanos/sage-drg/`](https://github.com/jaanos/sage-drg/), [`doi:10.5281/zenodo.1418410`](http://dx.doi.org/10.5281/zenodo.1418410).

```latex
@article{v18a,
    AUTHOR = {Vidali, Jano\v{s}},
     TITLE = {Using symbolic computation to prove nonexistence of distance-regular graphs},
   JOURNAL = {Electron. J. Combin.},
  FJOURNAL = {Electronic Journal of Combinatorics},
    VOLUME = {25},
    NUMBER = {4},
     PAGES = {P4.21},
      NOTE = {\url{http://www.combinatorics.org/ojs/index.php/eljc/article/view/v25i4p21}},
      YEAR = {2018},
}

@software{v18b,
   AUTHOR = {Vidali, Jano\v{s}},
    TITLE = {{\tt jaanos/sage-drg}: {\tt sage-drg} v0.8},
     NOTE = {\url{https://github.com/jaanos/sage-drg/},
             \href{http://dx.doi.org/10.5281/zenodo.1418410}{\texttt{10.5281/zenodo.1418410}}},
     YEAR = {2018},
}
```

Additionally, `sage-drg` has been used in the following research:

* A. Gavrilyuk, S. Suda and J. Vidali. On tight 4-designs in Hamming association schemes, 2018. [`arXiv:1809.07553`](http://arxiv.org/abs/1809.07553).

If you would like your research to be listed here, feel free to open an issue or pull request.
