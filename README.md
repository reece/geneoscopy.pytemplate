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

### Clone and setup

    $ git clone git@github.com:reece/geneoscopy.pytemplate.git
    $ cd geneoscopy.pytemplate/
    $ make devready
    $ source venv/3.7/bin/activate

### Tag a release

	$ git tag 0.1.0
	$ ipython
	In [1]: import geneoscopy.pytemplate
	In [2]: geneoscopy.pytemplate.__version__
	Out[2]: '0.1.0'

Notice that the version is pulled automatically from the tag. As soon
as a change is made to this README (or any file in the repo), the
version is updated automatically.

	In [1]: import geneoscopy.pytemplate
	In [2]: geneoscopy.pytemplate.__version__
	Out[2]: '0.1.1.dev0+gbedcaee.d20191007'

This version indicates that we are developing toward the 0.1.1
release.  `dev0` indicates that we're 0 commits from that the last
tagged release.  The remainder is a unique tag for the current state
of the directory. 

The advantage of this method is that git tags and python package
versions are guaranteed to be in sync. Furthermore, it also guarantees
that PEP440 (version string formats) is used, which is required for
downstream packaging tools.
