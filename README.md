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

### Testing

`make test` runs package tests and generates a coverage report.  For example:

     1	$ make test
     2	...
     3	===================================== test session starts =====================================
     4	platform linux -- Python 3.7.3, pytest-5.2.1, py-1.8.0, pluggy-0.13.0
     5	rootdir: /home/reece/projects/geneoscopy/geneoscopy.pytemplate, inifile: setup.cfg, testpaths: src, tests
     6	plugins: cov-2.8.1
     7	collected 3 items
     8	 
     9	src/geneoscopy/pytemplate/utils.py .													[ 33%]
    10	tests/test_greeting.py ..																[100%]
    11	 
    12	----------- coverage: platform linux, python 3.7.3-final-0 -----------
    13	Name									Stmts	Miss  Cover	  Missing
    14	---------------------------------------------------------------------
    15	src/geneoscopy/pytemplate/__init__.py		6	   2	67%	  5-6
    16	src/geneoscopy/pytemplate/__main__.py	   33	  22	33%	  23-24, 27-29, 33-71, 81-85
    17	src/geneoscopy/pytemplate/utils.py			6	   0   100%
    18	---------------------------------------------------------------------
    19	TOTAL									   45	  24	47%

Lines 9 and 10 indicate source lines being tested. `utils.py` is
tested because it contains doctests.  `test_greeting.py` is tested
because it is in the `tests/` and begins with `test_`.

When testing, python lines are monitored for execution. If at least
one test invokes code on a particular line, it's "covered".  The
coverage section indicate the number of statement lines, number of
lines not covered by tests, percentage that is covered, and which
lines are not covered ("missing").  Generally, it's a good idea to
write tests to cover lines in the missing column.


### Command line script

This starter kit includes a command line tool,
`geneoscopy-pytemplate`.  Examples:

#### Getting help
    $ geneoscopy-pytemplate --help
    usage: geneoscopy-pytemplate [-h] [--version] [--verbose] {greet,migrate} ...
     
    geneoscopy pytemplate command-line script
     
    optional arguments:
      -h, --help       show this help message and exit
      --version, -V    show program's version number and exit
      --verbose, -v
     
    subcommands:
      {greet,migrate}
        greet          print greeting
        migrate        create/migrate database


#### Showing the version
    $ geneoscopy-pytemplate --version
    0.1.1.dev1+gbc021c3.d20191008

#### Getting help on, and using, a subcommand
	$ geneoscopy-pytemplate greet -h
	usage: geneoscopy-pytemplate greet [-h] [--lang LANG]
    
	optional arguments:
      -h, --help            show this help message and exit
      --lang LANG, -l LANG  language abbreviation (default: en)

    $ geneoscopy-pytemplate greet
    hello
    
    $ geneoscopy-pytemplate greet -l cn
    你好

#### Using a different subcommand
    $ geneoscopy-pytemplate migrate -d postgres://user:pass@localhost:5432/mydb
    2019-10-08 22:30:35  geneoscopy.pytemplate.__main__[32266] CRITICAL I'm not really doing anything with postgres://user:pass@localhost:5432/mydb!

#### Logging
The example script also includes logging.  Here's the same command as
above, but adding -v (verbose) adds INFO-level information. Another -v
gives DEBUG logging.

    $ geneoscopy-pytemplate -v migrate -d postgres://user:pass@localhost:5432/mydb
    2019-10-08 22:30:40 snafu geneoscopy.pytemplate.__main__[32305] CRITICAL I'm not really doing anything with postgres://user:pass@localhost:5432/mydb!
    2019-10-08 22:30:40 snafu geneoscopy.pytemplate.__main__[32305] INFO Connecting to postgres://user:pass@localhost:5432/mydb... success
    2019-10-08 22:30:40 snafu geneoscopy.pytemplate.__main__[32305] INFO Migrating postgres://user:pass@localhost:5432/mydb... success

### Building a package

`make bdist_wheel` builds a Python wheel archive. 
