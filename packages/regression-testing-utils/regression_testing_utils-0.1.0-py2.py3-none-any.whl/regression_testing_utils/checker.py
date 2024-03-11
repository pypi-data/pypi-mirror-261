import logging
import os
import sys

from rich.console import Console
from typing import Any, Dict, List, Optional

from . import constants
from .console_helper import print_yellow, print_red


console = Console()


DEFAULT_OUTDIR = os.path.join(
    constants.DEFAULT_OUTDIR_BASE,
    os.path.splitext(os.path.basename(__file__))[0],
    constants.DEFAULT_TIMESTAMP,
)


class Checker:

    def __init__(self, **kwargs):
        self.config = kwargs.get("config", None)
        self.config_file = kwargs.get("config_file", constants.DEFAULT_CONFIG_FILE)
        self.outdir = kwargs.get("outdir", DEFAULT_OUTDIR)
        self.logfile = kwargs.get("logfile", None)
        self.outfile = kwargs.get("outfile", None)
        self.verbose = kwargs.get("verbose", constants.DEFAULT_VERBOSE)

        logging.info(f"Instantiated Checker in '{os.path.abspath(__file__)}'")

    def _print_banner(self, message: str) -> None:
        print("\n=====================================")
        print(f"    {message}")
        print("=====================================")

    def validate(self, config_file: Optional[str]) -> None:
        """Check the configuration file."""
        pass

    def is_valid(self, config_file: Optional[str]) -> bool:
        """Validate the configuration file."""
        return True
