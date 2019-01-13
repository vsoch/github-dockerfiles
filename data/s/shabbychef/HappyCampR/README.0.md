```{r setup,include=FALSE}
# set the knitr options ... for everyone!
# if you unset this, then vignette build bonks. oh, joy.
#opts_knit$set(progress=TRUE)
opts_knit$set(eval.after='fig.cap')
# for a package vignette, you do want to echo.
# opts_chunk$set(echo=FALSE,warning=FALSE,message=FALSE)
opts_chunk$set(warning=FALSE,message=FALSE)
#opts_chunk$set(results="asis")
opts_chunk$set(cache=TRUE,cache.path="cache/")

#opts_chunk$set(fig.path="github_extra/figure/",dev=c("pdf","cairo_ps"))
#opts_chunk$set(fig.path="github_extra/figure/",dev=c("png","pdf"))
opts_chunk$set(fig.path="github_extra/figure/",dev=c("png"))
opts_chunk$set(fig.width=5,fig.height=4,dpi=64)

# doing this means that png files are made of figures;
# the savings is small, and it looks like shit:
#opts_chunk$set(fig.path="figure/",dev=c("png","pdf","cairo_ps"))
#opts_chunk$set(fig.width=4,fig.height=4)
# for figures? this is sweave-specific?
#opts_knit$set(eps=TRUE)

# this would be for figures:
#opts_chunk$set(out.width='.8\\textwidth')
# for text wrapping:
options(width=64,digits=2)
opts_chunk$set(size="small")
opts_chunk$set(tidy=TRUE,tidy.opts=list(width.cutoff=50,keep.blank.line=TRUE))

#HappyCampR.meta <- packageDescription('HappyCampR')
```

# HappyCampR

[![Build Status](https://travis-ci.org/shabbychef/HappyCampR.png)](https://travis-ci.org/shabbychef/HappyCampR)
[![codecov.io](http://codecov.io/github/shabbychef/HappyCampR/coverage.svg?branch=master)](http://codecov.io/github/shabbychef/HappyCampR?branch=master)
[![CRAN](http://www.r-pkg.org/badges/version/HappyCampR)](http://cran.rstudio.com/package=HappyCampR) 
[![Downloads](http://cranlogs.r-pkg.org/badges/HappyCampR?color=brightgreen)](http://www.r-pkg.org/pkg/HappyCampR)

HappyCampR.

-- Steven E. Pav, shabbychef@gmail.com

## Installation

This package may be installed from CRAN; the latest version may be
found on [github](https://www.github.com/shabbychef/HappyCampR "HappyCampR")
via devtools, or installed via [drat](https://github.com/eddelbuettel/drat "drat"):

```{r install,eval=FALSE,echo=TRUE}
if (require(devtools)) {
	# latest greatest
	install_github('shabbychef/HappyCampR')
}
# via drat:
if (require(drat)) {
	drat:::add('shabbychef')
	install.packages('HappyCampR')
}
```

# Basic Usage

```{r tryit,eval=FALSE,echo=TRUE}
requre(HappyCampR)
```
