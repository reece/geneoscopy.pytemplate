"""geneoscopy pytemplate command-line script"""


# python imports first
import argparse
import logging
import sys

# then external imports
import coloredlogs

# then imports from this package
from . import __version__
from .utils import greeting


# module-level logger for use within any function
_logger = logging.getLogger(__name__)


def logtest():
    _logger.debug("")
    _logger.info("")
    _logger.warning("")
    _logger.critical("")


def cli_greet(opts):
    _logger.info(f"Greeting in {opts.lang}")
    print(greeting(opts.lang))

def cli_migrate(opts):
    _logger.critical(f"I'm not really doing anything with {opts.db_uri}!")
    _logger.info(f"Connecting to {opts.db_uri}... success")
    _logger.info(f"Migrating {opts.db_uri}... success")


def parse_args(argv):
    ap = argparse.ArgumentParser(
        description=__doc__,  # refers to first line triple-quoted string
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        )
    ap.add_argument("--version", "-V",
                    action="version",
                    version=__version__)
    ap.add_argument("--verbose", "-v",
                    action="count",
                    default=0)

    sub_p = ap.add_subparsers(
        title="subcommands"
    )
    
    # greet subcommand
    greet_p = sub_p.add_parser("greet",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        help="print greeting")
    greet_p.add_argument(
        "--lang", "-l",
        help="language abbreviation",
        default="en"
        )
    greet_p.set_defaults(func=cli_greet)

    # migrate subcommand
    migrate_p = sub_p.add_parser("migrate",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        help="create/migrate database")
    migrate_p.add_argument(
        "--db-uri", "-d",
        required=True,
        help="database URI e.g., postgres://user:pass@localhost:5432/mydb",
        )
    migrate_p.set_defaults(func=cli_migrate)

    opts = ap.parse_args(argv)

    # reset logging level based on --verbose
    if opts.verbose >= 2:
        _logger.setLevel(10)
    elif opts.verbose == 1:
        _logger.setLevel(20)
    for handler in logging.getLogger().handlers:
        handler.setLevel(_logger.level)

    try:
        func = opts.func
    except AttributeError:
        # The user didn't provide a subcommand.
        _logger.debug("No subcommand provided")
        ap.print_help()
    else:
        func(opts)


def main(argv=None):
    """top-level function that corresponds to command-line executable

    By constructing as a separate function, one could (in principle),
    write tests of the `main()` routine

    """
    coloredlogs.install(level="WARNING")
    if not argv:
        _logger.debug("Using command-line arguments")
        argv = sys.argv[1:]
    opts = parse_args(argv)


if __name__ == "__main__":
    main(sys.argv[1:])
    
