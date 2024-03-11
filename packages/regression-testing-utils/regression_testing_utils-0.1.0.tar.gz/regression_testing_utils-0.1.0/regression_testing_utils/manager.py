import logging
import os
import sys

from rich.console import Console
from rich.table import Table
from typing import Any, Dict, List, Optional

from . import constants
from .console_helper import print_yellow, print_red
from .checker import Checker
from .file_utils import check_infile_status

from .evaluator import Evaluator

console = Console()

DEFAULT_TEST_MODE = False

DEFAULT_OUTDIR = os.path.join(
    constants.DEFAULT_OUTDIR_BASE,
    os.path.splitext(os.path.basename(__file__))[0],
    constants.DEFAULT_TIMESTAMP,
)


class Manager:

    def __init__(self, **kwargs):
        self.config = kwargs.get("config", None)
        self.config_file = kwargs.get("config_file", constants.DEFAULT_CONFIG_FILE)
        self.file_format = kwargs.get("file_format", None)
        self.outdir = kwargs.get("outdir", DEFAULT_OUTDIR)
        self.logfile = kwargs.get("logfile", None)
        self.outfile = kwargs.get("outfile", None)
        self.test_mode = kwargs.get("test_mode", None)
        self.verbose = kwargs.get("verbose", constants.DEFAULT_VERBOSE)

        if self.file_format is None:
            self.file_format = self.config.get("file_format", None)
            if self.file_format is None:
                raise Exception(f"The file format is not defined in the configuration file '{self.config_file}'")
            logging.info(f"Setting file format to '{self.file_format}'")

        self.checker = Checker(**kwargs)

        logging.info(f"Instantiated Manager in '{os.path.abspath(__file__)}'")

    def _print_banner(self, message: str) -> None:
        if self.config["use_rich_table"]:
            table = Table(
                show_header=False,
                header_style='bold #2070b2',
                title='[bold][/]'
            )

            table.add_column("", justify='center')
            table.add_row(f'[bold]{message}[/]')

            console.print(table)

        else:
            print("\n=====================================")
            print(f"    {message}")
            print("=====================================")



    def check_config(self, config_file: Optional[str]) -> int:
        """Check the configuration file."""
        self.checker.validate(config_file)

    def run_tests(self) -> int:
        """Run regression tests."""
        if not self.checker.is_valid(self.config_file):
            print_red(f"The configuration file '{self.config_file}' is not valid")
            sys.exit(1)

        if "workflow" not in self.config:
            raise Exception(f"The configuration file '{self.config_file}' does not contain a 'workflow' section")

        if "stages" not in self.config["workflow"]:
            raise Exception(f"The 'stages' section does not exist in the 'workflow' section of the configuration file '{self.config_file}'")

        if "test_mode" in self.config["workflow"] and self.test_mode is None:
            self.test_mode = self.config["workflow"]["test_mode"]
            if self.test_mode is None or self.test_mode == "":
                self.test_mode = DEFAULT_TEST_MODE

        # TODO: add support for name and description of workflow
        for stage in self.config["workflow"]["stages"]:
            self._perform_stage(stage)

    def _perform_stage(self, stage: Dict[str, Any]) -> None:
        if "stage_name" not in stage:
            raise Exception(f"The stage '{stage}' does not contain a 'stage_name' section")
        stage_name = stage["stage_name"]

        if stage_name.lower() == "evaluation":
            self._perform_evaluation(stage_name, stage["commands"])
        else:
            self._print_banner(f"Running stage '{stage_name}'")
            if "commands" not in stage:
                raise Exception(f"The stage '{stage_name}' does not contain a 'commands' section")

            self._perform_commands(stage_name, stage["commands"])

    def _perform_commands(self, stage_name: str, commands: List[str]) -> None:
        for c in commands:
            desc = c.get("desc", "N/A")
            command = c.get("command", None)

            if command is None or command == "":
                raise Exception(f"The command '{command}' is not defined (description '{desc}' in stage '{stage_name}')")

            self._perform_command(command)

    def _perform_command(self, command: str) -> None:

        if '%TIMESTAMP%' in command:
            logging.info(f"Will replace '%TIMESTAMP%' with '{constants.DEFAULT_TIMESTAMP}' in command '{command}'")
            command = command.replace('%TIMESTAMP%', constants.DEFAULT_TIMESTAMP)

        print_yellow(f"Will attempt to execute '{command}'")
        logging.info(f"Will attempt to execute '{command}'")
        if not self.test_mode:
            os.system(command)
        else:
            print_yellow(f"Test mode is enabled - will not execute '{command}'")

    def _perform_evaluation(self, stage_name: str, commands: List[str]) -> None:

        for c in commands:
            desc = c.get("desc", "N/A")

            if "evaluator" in c:
                self._execute_evaluator(stage_name, c)
            else:
                command = c.get("command", None)
                if command is None or command == "":
                    raise Exception(f"The command '{command}' is not defined (description '{desc}' in stage '{stage_name}')")
                self._perform_command(command)

    def _execute_evaluator(
            self,
            stage_name: str,
            command: Dict[str, Any]
        ) -> None:
        if "args" not in command:
            raise Exception(f"The evaluator section in stage '{stage_name}' does not contain an 'args' section")

        file_format = None
        if "file_format" in command["args"]:
            file_format = command["args"]["file_format"]
            if file_format is None or file_format == "":
                raise Exception(f"The file format is not defined in the configuration file '{self.config_file}'")
        else:
            file_format = self.config.get("file_format", None)
            if file_format is None or file_format == "":
                raise Exception(f"The file format is not defined in the configuration file '{self.config_file}'")

        if "file1" not in command["args"]:
            raise Exception(f"The evaluator section in stage '{stage_name}' does not contain a 'file1' section")

        file1 = command["args"]["file1"]

        if '%TIMESTAMP%' in file1:
            logging.info(f"Will replace '%TIMESTAMP%' with '{constants.DEFAULT_TIMESTAMP}' in file1 '{file1}'")
            file1 = file1.replace('%TIMESTAMP%', constants.DEFAULT_TIMESTAMP)

        check_infile_status(file1, file_format)


        if "file2" not in command["args"]:
            raise Exception(f"The evaluator section in stage '{stage_name}' does not contain a 'file2' section")

        file2 = command["args"]["file2"]

        if '%TIMESTAMP%' in file2:
            logging.info(f"Will replace '%TIMESTAMP%' with '{constants.DEFAULT_TIMESTAMP}' in file2 '{file2}'")
            file2 = file2.replace('%TIMESTAMP%', constants.DEFAULT_TIMESTAMP)

        check_infile_status(file1, file_format)

        outfile = None
        if "outfile" in command["args"]:
            outfile = command["args"]["outfile"]
            if '%TIMESTAMP%' in outfile:
                logging.info(f"Will replace '%TIMESTAMP%' with '{constants.DEFAULT_TIMESTAMP}' in outfile '{outfile}'")
                outfile = outfile.replace('%TIMESTAMP%', constants.DEFAULT_TIMESTAMP)

        evaluator = Evaluator(
            config=self.config,
            config_file=self.config_file,
            file1=file1,
            file2=file2,
            file_format=file_format,
            outdir=self.outdir,
            outfile=outfile,
            logfile=self.logfile,
            test_mode=self.test_mode,
            verbose=self.verbose,
        )

        if file_format.lower() == "tsv":
            evaluator.compare_tsv_files(
                file1=file1,
                file2=file2,
            )
        elif file_format.lower() == "csv":
            evaluator.compare_csv_files(
                file1=file1,
                file2=file2,
            )
        else:
            raise Exception(f"The file format '{file_format}' is not supported")
