"""Compare two sorted review files line-by-line and column-by-column."""
import click
import logging
import os
import pathlib
import sys
import yaml

from typing import Optional
from rich.console import Console

from . import constants
from console_helper import print_yellow
from file_utils import check_infile_status
from evaluator import Evaluator

DEFAULT_IGNORE_COLUMNS = False

DEFAULT_OUTDIR = os.path.join(
    constants.DEFAULT_OUTDIR_BASE,
    os.path.splitext(os.path.basename(__file__))[0],
    constants.DEFAULT_TIMESTAMP
)

DEFAULT_OUTFILE = os.path.join(
    DEFAULT_OUTDIR,
    os.path.splitext(os.path.basename(__file__))[0] + '.diff.txt'
)


error_console = Console(stderr=True, style="bold red")

console = Console()

def validate_verbose(ctx, param, value):
    """Validate the validate option.

    Args:
        ctx (Context): The click context.
        param (str): The parameter.
        value (bool): The value.

    Returns:
        bool: The value.
    """

    if value is None:
        click.secho("--verbose was not specified and therefore was set to 'True'", fg='yellow')
        return constants.DEFAULT_VERBOSE
    return value


@click.command()
@click.option('--config_file', type=click.Path(exists=True), help=f"Optional: The configuration file for this project - default is '{constants.DEFAULT_CONFIG_FILE}'")
@click.option('--file1', help="Required: The first sorted review file (.tsv)")
@click.option('--file2', help="Required: The second sorted review file (.tsv)")
@click.option('--file_format', type=click.Choice(['csv', 'tsv']), help="Required: The file format of the output file to be evaluated against expected version")
@click.option('--ignore_columns', is_flag=True, help=f"Optional: Ignore columns specified in --ignore_columns_str - default is '{DEFAULT_IGNORE_COLUMNS}'")
@click.option('--ignore_columns_str', help="Optional: comma-separated list of column headers wrapped in quotes")
@click.option('--logfile', help="Optional: The log file")
@click.option('--outdir', help=f"Optional: The output directory where logfile and default output file will be written - default is '{DEFAULT_OUTDIR}'")
@click.option('--outfile', help=f"Optional: The output file to which differences will be written to - default is '{DEFAULT_OUTFILE}'")
@click.option('--verbose', is_flag=True, help=f"Will print more info to STDOUT - default is '{constants.DEFAULT_VERBOSE}'.", callback=validate_verbose)
def main(
    config_file: str,
    file1: str,
    file2: str,
    file_format: str,
    ignore_columns: Optional[bool],
    ignore_columns_str: Optional[str],
    logfile: Optional[str],
    outdir: Optional[str],
    outfile: Optional[str],
    verbose: Optional[bool]
):
    """Compare two sorted review files line-by-line and column-by-column."""

    error_ctr = 0

    if file1 is None:
        error_console.print("--file1 was not specified")
        error_ctr += 1

    if file2 is None:
        error_console.print("--file2 was not specified")
        error_ctr += 1

    if error_ctr > 0:
        error_console.print("Required command-line arguments were not provided")
        sys.exit(1)

    check_infile_status(file1)
    check_infile_status(file2)

    if config_file is None:
        config_file = constants.DEFAULT_CONFIG_FILE
        print_yellow(f"--config_file was not specified and therefore was set to '{config_file}'")

    check_infile_status(config_file, "yaml")

    if ignore_columns is None:
        ignore_columns = DEFAULT_IGNORE_COLUMNS
        print_yellow(f"--ignore_columns was not specified and therefore was set to '{ignore_columns}'")


    if outdir is None:
        outdir = DEFAULT_OUTDIR
        print_yellow(f"--outdir was not specified and therefore was set to '{outdir}'")

    if not os.path.exists(outdir):
        pathlib.Path(outdir).mkdir(parents=True, exist_ok=True)
        print_yellow(f"Created output directory '{outdir}'")

    if logfile is None:
        logfile = os.path.join(
            outdir,
            os.path.splitext(os.path.basename(__file__))[0] + '.log'
        )
        print_yellow(f"--logfile was not specified and therefore was set to '{logfile}'")

    if outfile is None:
        outfile = DEFAULT_OUTFILE
        print_yellow(f"--outfile was not specified and therefore was set to '{outfile}'")

    if ignore_columns:
        if ignore_columns_str is None:
            error_console.print("--ignore_columns was specified but --ignore_columns_str was not specified")
            sys.exit(-1)

    logging.basicConfig(
        filename=logfile,
        format=constants.DEFAULT_LOGGING_FORMAT,
        level=constants.DEFAULT_LOGGING_LEVEL,
    )


    logging.info(f"Will load contents of config file '{config_file}'")
    config = yaml.safe_load(pathlib.Path(config_file).read_text())

    if file_format is None or file_format == "":
        if "file_format" not in config:
            error_console.print(f"--file_format is required and could not be found in the configuration file '{config_file}'")
            sys.exit(1)
        else:
            file_format = config["file_format"]
            print_yellow(f"Setting file format to '{file_format}'")


    evaluator = Evaluator(
        config=config,
        config_file=config_file,
        file1=file1,
        file2=file2,
        file_format=file_format,
        ignore_columns=ignore_columns,
        ignore_columns_str=ignore_columns_str,
        logfile=logfile,
        outdir=outdir,
        outfile=outfile,
        verbose=verbose,
    )

    if file_format.lower() == "csv":
        evaluator.compare_csv_files()
    elif file_format.lower() == "tsv":
        evaluator.compare_tsv_files()
    else:
        error_console.print(f"The file format '{file_format}' is not supported")
        sys.exit(1)

    if verbose:
        console.print(f"The log file is '{logfile}'")
        console.print(f"[bold green]Execution of '{os.path.abspath(__file__)}' completed")


if __name__ == "__main__":
    main()
