# geneoscopy.pytemplate
A starter kit for python packages based on Reece's biocommons starter kit

## Features
* namespace packages
* package version directly from tags
* pytest preconfigured, with support for doctests and coverage
* tox preconfigured
* sphinx documentation configured
* unified interface (via Makefile)
* yapf-preconfigured (`make reformat`)

## Getting started

    $ git clone git@github.com:reece/geneoscopy.pytemplate.git
    $ cd geneoscopy.pytemplate/
    $ make devready
    $ source venv/3.7/bin/activate
    $ ipython 
	In [1]: import geneoscopy.pytemplate                                                                      

	In [2]: geneoscopy.pytemplate.__version__
	Out[2]: '0.1.dev1+gbca739f'

