import logging
import os
import sys

import xlsxwriter

from datetime import datetime
from rich.console import Console
from typing import Any, Dict, List, Optional

from . import constants
from .console_helper import print_yellow, print_red


console = Console()

DEFAULT_TEST_MODE = True

DEFAULT_OUTDIR = os.path.join(
    constants.DEFAULT_OUTDIR_BASE,
    os.path.splitext(os.path.basename(__file__))[0],
    constants.DEFAULT_TIMESTAMP,
)

# The default boolean value for whether to ignore columns
# specified in the DEFAULT_IGNORE_COLUMNS_STR.
# Note that the value in the configuration file
# "ignore_columns" will override this value.
DEFAULT_IGNORE_COLUMNS = False

# The default list of columns to be ignored.
# Note that the value in the configuration file
# "ignore_columns_str" will override this value.
DEFAULT_IGNORE_COLUMNS_STR = []

# The line number that the header starts on
DEFAULT_HEADER_LINE_NUMBER = 1

# The line number that the records start on
DEFAULT_RECORDS_START_LINE_NUMBER = 2

# The maximum number of columns
DEFAULT_MAX_COLUMN_COUNT = 0


class Evaluator:

    def __init__(self, **kwargs):
        self.config = kwargs.get("config", None)
        self.config_file = kwargs.get("config_file", constants.DEFAULT_CONFIG_FILE)
        self.file1 = kwargs.get("file1", None)
        self.file2 = kwargs.get("file2", None)
        self.file_format = kwargs.get("file_format", None)
        self.outdir = kwargs.get("outdir", DEFAULT_OUTDIR)
        self.outfile = kwargs.get("outfile", None)
        self.logfile = kwargs.get("logfile", None)
        self.test_mode = kwargs.get("test_mode", DEFAULT_TEST_MODE)
        self.verbose = kwargs.get("verbose", constants.DEFAULT_VERBOSE)

        self.ignore_columns_lookup = {}

        self.ignore_columns = kwargs.get("ignore_columns", None)
        if self.ignore_columns is None or self.ignore_columns == "":
            self._set_ignore_columns()

        if self.ignore_columns:
            # Some columns are to be ignored.
            self.ignore_columns_str = kwargs.get("ignore_columns_str", None)
            if self.ignore_columns_str is None or self.ignore_columns_str == "":
                self._set_ignore_columns_str()
            else:
                # User-specified comma-separated list of columns to ignore.
                self._load_ignore_columns_from_str()
        else:
            logging.info("Looks like no columns are to be ignored")

        self.header_line_number = kwargs.get("header_line_number", None)
        if self.header_line_number is None or self.header_line_number == "":
            self._set_header_line_number()

        self.max_column_count = kwargs.get("max_column_count", None)
        if self.max_column_count is None or self.max_column_count == "":
            self._set_max_column_count()

        self.records_start_line_number = kwargs.get("records_start_line_number", None)
        if self.records_start_line_number is None or self.records_start_line_number == "":
            self._set_records_start_line_number()

        # Tally the number of differences found.
        self._diff_count = 0

        # Store the differences found.
        self._differences = []

        logging.info(f"Instantiated Evaluator in '{os.path.abspath(__file__)}'")

    def _set_header_line_number(self) -> None:
        self.header_line_number = self.config.get("header_line_number", None)
        if self.header_line_number is None or self.header_line_number == "":
            self.header_line_number = DEFAULT_HEADER_LINE_NUMBER
            logging.info(f"Could not find header line number in the configuration file '{self.config_file}' so set to default '{self.header_line_number}'")

    def _set_ignore_columns(self) -> None:
        self.ignore_columns = self.config.get("ignore_columns", None)
        if self.ignore_columns is None or self.ignore_columns == "":
            self.ignore_columns = DEFAULT_IGNORE_COLUMNS
            logging.info(f"Could not find ignore_columns in the configuration file '{self.config_file}' so set to default '{self.ignore_columns}'")

    def _set_ignore_columns_str(self) -> None:
        self.ignore_columns_str = self.config.get("ignore_columns_str", None)
        if self.ignore_columns_str is None or self.ignore_columns_str == "":
            self.ignore_columns_str = DEFAULT_IGNORE_COLUMNS_STR
            logging.info(f"Could not find ignore_columns_str in the configuration file '{self.config_file}' so set to default '{self.ignore_columns_str}'")
        else:
            self._load_ignore_columns_from_list()

    def _load_ignore_columns_from_list(self) -> None:
        for column in self.ignore_columns_str:
            self.ignore_columns_lookup[column.strip()] = True
        logging.info("Loaded ignore columns lookup from a list")

    def _load_ignore_columns_from_str(self) -> None:
        columns = self.ignore_columns_str.split(",")
        for column in columns:
            self.ignore_columns_lookup[column.strip()] = True
        logging.info("Loaded ignore columns lookup from a comma-separated list string")

    def _set_max_column_count(self) -> None:
        self.max_column_count = self.config.get("max_column_count", None)
        if self.max_column_count is None or self.max_column_count == "":
            self.max_column_count = DEFAULT_MAX_COLUMN_COUNT
            logging.info(f"Could not find max column count in the configuration file '{self.config_file}' so set to default '{self.max_column_count}'")

    def _set_records_start_line_number(self) -> None:
        self.records_start_line_number = self.config.get("records_start_line_number", None)
        if self.records_start_line_number is None or self.records_start_line_number == "":
            self.records_start_line_number = DEFAULT_RECORDS_START_LINE_NUMBER
            logging.info(f"Could not find records start line number in the configuration file '{self.config_file}' so set to default '{self.records_start_line_number}'")

    def compare_csv_files(
            self,
            file1: str,
            file2: str,
            outfile: Optional[str] = None
        ) -> None:
        """Compare contents of two comma-separated files."""
        if file1 is not None:
            self.file1 = file1
        if file2 is not None:
            self.file2 = file2

        if outfile is None:
            outfile = self._derive_outfile()

        self.file_format = "csv"
        self._compare_files()

    def compare_tsv_files(
            self,
            file1: str,
            file2: str,
            outfile: Optional[str] = None
        ) -> None:
        """Compare contents of two tab-delimited files."""
        if file1 is not None:
            self.file1 = file1
        if file2 is not None:
            self.file2 = file2

        if outfile is None:
            outfile = self._derive_outfile()

        self.file_format = "tsv"
        self._compare_files()

    def _derive_outfile(self) -> str:
        if self.outfile is None:
            outfile = os.path.join(self.outdir, "diff_report.txt")
            logging.info(f"Derived outfile '{outfile}'")
            self.outfile = outfile
        return self.outfile

    def _generate_diff_report(self) -> None:

        lookup = self._get_column_number_to_column_letters_lookup()

        with open(self.outfile, 'w') as of:
            of.write(f"## method-created: {os.path.abspath(__file__)}\n")
            of.write(f"## date-created: {str(datetime.today().strftime('%Y-%m-%d-%H%M%S'))}\n")
            of.write(f"## created-by: {os.environ.get('USER')}\n")
            of.write(f"## file 1: {self.file1}\n")
            of.write(f"## file 2: {self.file2}\n")
            of.write(f"## file-format: {self.file_format}\n")
            of.write(f"## logfile: {self.logfile}\n")
            of.write(f"## Number of differences: {self._diff_count}\n")

            of.write("Line #\tColumn Name\tColumn #\tColumn Letter\tValue in File 1\tValue in File 2\n")

            for diff in self._differences:
                excel_column_letters = lookup[diff[2]]
                of.write(f"{diff[0]}\t{diff[1]}\t{diff[2]}\t{excel_column_letters}\t{diff[3]}\t{diff[4]}\n")

        logging.info(f"Wrote '{self._diff_count}' differences to report file '{self.outfile}'")
        if self.verbose:
            console.print(f"Wrote '{self._diff_count}' differences to report file '{self.outfile}'")

    def _get_column_number_to_column_letters_lookup(self, max_column_number: Optional[int] = None) -> Dict[int, str]:
        """Get a lookup of column numbers to column letters.

        Args:
            max_column_number (int, optional): The maximum number of columns. Defaults to DEFAULT_MAX_COLUMN_COUNT.

        Returns:
            Dict[int, str]: The lookup of column numbers to column letters.
        """
        if max_column_number is None:
            max_column_number = self.max_column_count

        column_numbers = [x for x in range(max_column_number)]
        lookup = {}
        for column_number in column_numbers:
            column_letter = xlsxwriter.utility.xl_col_to_name(column_number)
            column_number += 1
            logging.debug(f"Converted column number '{column_number}' to column letter '{column_letter}'")
            lookup[column_number] = column_letter
        return lookup

    def _read_file(self, file_path: str):
        """Read a tab-delimited file and return its content as a list of lists.

        Args:
            file_path (str): The path to the file to be read.
        """
        logging.info(f"Will attempt to read file '{file_path}'")
        if self.verbose:
            console.print(f"Will attempt to read file '{file_path}'")

        with open(file_path, 'r', encoding="latin-1") as file:
            lines = file.readlines()

        header = lines[self.header_line_number].strip().split('\t')
        header_index_to_name_lookup = {}
        header_name_to_index_lookup = {}

        for i, h in enumerate(header):
            header_index_to_name_lookup[i] = h
            header_name_to_index_lookup[h] = i

        data = [line.strip().split('\t') for line in lines[self.records_start_line_number:]]

        return header, header_index_to_name_lookup, header_name_to_index_lookup, data

    def _get_ignore_columns_lookup(self, ignore_columns_str: str) -> Dict[str, bool]:
        logging.info(f"Will ignore columns: {ignore_columns_str}")
        if self.verbose:
            console.print(f"Will ignore columns: {ignore_columns_str}")

        ignore_columns_lookup = {}
        columns = ignore_columns_str.split(",")
        for column in columns:
            ignore_columns_lookup[column.strip()] = True
        return ignore_columns_lookup

    def _compare_files(self) -> None:
        """Compare two tab-delimited files and store differences."""
        file1_path = self.file1
        file2_path = self.file2

        header1, header_index_to_name_lookup1, header_name_to_index_lookup1, data1 = self._read_file(file1_path)
        header2, header_index_to_name_lookup2, header_name_to_index_lookup2, data2 = self._read_file(file2_path)

        logging.info("Going to compare contents of the two files now")
        if self.verbose:
            console.print("Going to compare contents of the two files now")

        max_rows = max(len(data1), len(data2))

        max_max_columns = 0

        for i in range(1, max_rows + 1):
            if i <= len(data1):
                row1 = data1[i - 1]
            else:
                row1 = [""] * len(header1)

            if i <= len(data2):
                row2 = data2[i - 1]
            else:
                row2 = [""] * len(header2)

            max_columns = max(len(row1), len(row2))
            if max_columns > max_max_columns:
                max_max_columns = max_columns

            # max_columns = 59

            for j in range(0, max_columns):

                cell1 = row1[j] if j < len(row1) else ""
                cell2 = row2[j] if j < len(row2) else ""

                if cell1 != cell2:
                    if (self.ignore_columns and
                        j in header_index_to_name_lookup1 and
                        header_index_to_name_lookup1[j] in self.ignore_columns_lookup):
                        logging.info(f"Found differences in cell 1 '{cell1}' and cell 2 '{cell2}' but will ignore")
                        continue
                    # logging.info(f"i '{i}' j '{j}' max_columns '{max_columns}' max_rows '{max_rows}' cell1 '{cell1}' cell2 '{cell2}'")
                    self._differences.append((
                        i,
                        header1[j] if j < len(header1) else header2[j],
                        j + 1,
                        cell1,
                        cell2)
                        )
                    self._diff_count += 1

        self.max_column_count = max_max_columns

        if self._diff_count > 0:
            print_red(f"{self._diff_count} differences found")
            logging.info(f"{self._diff_count} differences found")
            self._generate_diff_report()
        else:
            console.print("[bold green]No differences found.[/]")
            logging.info("No differences found.")

