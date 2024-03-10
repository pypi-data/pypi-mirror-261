"""
code_analyzer.py Tool by TechBeamers

This script provides a tool for analyzing Python code using PEP 8, Flake8, and MyPy.
...
"""

import importlib
import os
import sys

import html

from contextlib import redirect_stdout
import io


__version__ = "1.0.0"


class CodeAnalyzer:
    """
    This class provides a tool for analyzing Python code using
    PEP 8, Flake8, and MyPy.
    ...
    """

    def __init__(
        self,
        file_path=None,
        report_format="html",
        pycodestyle_options=None,
        analyze_pep8=True,
        analyze_flake8=True,
        analyze_mypy=True,
    ):
        """
        Initialize the CodeAnalyzer instance.

        :param file_path: Path to the Python file to analyze.
        :param report_format: Format for saving detailed reports (html or txt).
        :param pycodestyle_options: Options for the pycodestyle module.
        :param analyze_pep8: Perform PEP 8 analysis.
        :param analyze_flake8: Perform Flake8 analysis.
        :param analyze_mypy: Perform MyPy analysis.
        """
        self.file_path = file_path or ""
        self.report_format = report_format.lower()
        self.pycodestyle_options = pycodestyle_options
        self.pep8_flag = analyze_pep8
        self.flake8_flag = analyze_flake8
        self.mypy_flag = analyze_mypy
        self.install_pycodestyle()
        self.install_flake8()
        self.install_mypy()

    def get_current_file(self):
        return os.path.abspath(__file__)

    def install_flake8(self):
        if self.flake8_flag:
            self.install_module("flake8", "Flake8")

    def install_mypy(self):
        if self.mypy_flag:
            self.install_module("mypy", "mypy")

    def install_pycodestyle(self):
        if self.pep8_flag:
            self.install_module("pycodestyle", "pycodestyle")

    def install_module(self, module_name: str, display_name: str) -> None:
        try:
            importlib.import_module(module_name)
        except ImportError:
            install = input(
                f"The '{module_name}' module is not installed. "
                f"Would you like to install it now? (y/n): "
            ).lower()

            if install == "y":
                os.system(f"pip install {module_name}")
            else:
                print(
                    f"Warning: '{module_name}' is not installed. "
                    f"{display_name} analysis will not be performed."
                )

    def analyze_pep8(self):
        if not self.pep8_flag:
            return None

        try:
            pycode = importlib.import_module("pycodestyle")

            checker = pycode.Checker(self.file_path, options=self.pycodestyle_options)

            with io.StringIO() as f:
                with redirect_stdout(f):
                    checker.check_all()

                out = f.getvalue().splitlines()
                error_messages = [line.strip() for line in out if line.strip()]
                return error_messages

        except ImportError as e:
            # Log the error or handle it according to your needs
            print(f"Error: pycodestyle module not found. {e}")
            return None

    def analyze_flake8(self):
        if not self.flake8_flag:
            return None

        try:
            # Replace with the actual path to your Flake8 executable
            flake8_executable = "flake8"
            command = f"{flake8_executable} {self.file_path}"

            # Print the command being executed
            print("\nRunning Flake8 analysis...")

            with os.popen(command) as process:
                flake8_output = process.read()

            return flake8_output.splitlines()

        except Exception as e:
            print(f"Exception: {e}")
            return None

    def analyze_mypy(self):
        if not self.mypy_flag:
            return None

        try:
            # Replace with the actual path to your MyPy executable
            mypy_executable = "mypy"
            command = f"{mypy_executable} {self.file_path}"

            # Print the command being executed
            print("\nRunning MyPy analysis...")

            with os.popen(command) as process:
                mypy_output = process.read()

            # Exclude messages indicating the number of errors found
            mypy_lines = mypy_output.splitlines()
            mypy_results = [
                line for line in mypy_lines if not line.startswith("Found ")
            ]

            return mypy_results

        except Exception as e:
            print(f"Exception: {e}")
            return None

    def run_analysis(self):
        # Check if the file exists
        if not os.path.exists(self.file_path):
            msg = "=" * (
                len("Error: Please check the file not found -")
                + len(self.file_path)
                + 1
            )
            print(msg)
            print("Error: Please check the file not found -", self.file_path)
            print(msg)
            sys.exit(1)

        # Check if any analysis option is specified
        if not any([self.pep8_flag, self.flake8_flag, self.mypy_flag]):
            underline = "=" * 30
            print(f"\n{underline}")
            print("No analysis option is specified.")
            print(underline)
            return

        print(f"\nAnalyzing file: {self.file_path}")

        # Pycodestyle analysis (formerly PEP 8)
        pycodestyle_results = self.analyze_pep8()
        self.print_analysis_results("pycodestyle", pycodestyle_results)

        # Flake8 analysis
        flake8_results = self.analyze_flake8()
        self.print_analysis_results("Flake8", flake8_results)

        # mypy analysis
        mypy_results = self.analyze_mypy()
        self.print_analysis_results("mypy", mypy_results)

        # If no analysis tools are installed, display a message
        if all(
            result is None
            for result in (pycodestyle_results, flake8_results, mypy_results)
        ) or all(
            result == []
            for result in (pycodestyle_results, flake8_results, mypy_results)
        ):
            underline = "=" * 30
            print(f"\n{underline}")
            print("No analysis tools installed. " "Please install at least one tool.")
            print(underline)

    def generate_statistics(self):
        if not os.path.exists(self.file_path):
            print(
                f"Error: Please check the file '{self.file_path}' " f"does not exist."
            )
            return

        with open(self.file_path, "r", encoding="utf-8") as file:
            code_content = file.read()

        lines = code_content.split("\n")
        total_lines = len(lines)
        blank_lines = sum(1 for line in lines if not line.strip())
        comments = sum(1 for line in lines if line.strip().startswith("#"))

        print("\nCode Statistics:")
        # Adjust the number based on label length
        print("=" * 15)
        print(f"Total Lines: {total_lines}")
        print(f"Blank Lines: {blank_lines}")
        print(f"Comment Lines: {comments}")
        print()

    def print_analysis_results(self, tool_name, results):
        summary = []

        if results is not None:
            if isinstance(results, list):
                if results:
                    for issue in results:
                        summary.append(f"  - {html.escape(issue)}")
                    summary.append(f"\n{len(results)} issues found.")
                else:
                    summary.append("Success: No issues found")
            elif isinstance(results, str):
                summary.append(f"  - {html.escape(results)}")
            else:
                summary.append("Unexpected result format.")
        else:
            if tool_name.lower() == "pycodestyle" and not self.pep8_flag:
                return  # Skip messages for pycodestyle if not selected
            elif tool_name.lower() == "flake8" and not self.flake8_flag:
                return  # Skip messages for Flake8 if not selected
            elif tool_name.lower() == "mypy" and not self.mypy_flag:
                return  # Skip messages for mypy if not selected

            summary.append(
                f"Warning: {tool_name} is not installed. {tool_name} "
                f"analysis will not be performed."
            )

        # Write a detailed report
        self.save_detailed_report(tool_name, results)
        self.generate_text_report(tool_name, results)

    def generate_text_report(self, tool_name, results):
        print(f"\n{tool_name} Results:")
        print("=" * len(f"{tool_name} Results:"))
        if isinstance(results, list):
            for line in results:
                print(line)
        elif isinstance(results, str):
            print(results)
        else:
            print("Unexpected result format.")

    def save_detailed_report(self, tool_name, results):
        if self.report_format == "html":
            self.save_html_report(tool_name, results)
        elif self.report_format == "txt":
            self.save_txt_report(tool_name, results)
        else:
            print(
                "Invalid report format specified. " "Supported formats: 'html', 'txt'"
            )

    def save_html_report(self, tool_name, results):
        report_file_path = f"{self.file_path}_report_{tool_name.lower()}.html"
        with open(report_file_path, "w", encoding="utf-8") as report_file:
            report_file.write("<html><body>")
            report_file.write(f"<h2>{tool_name} Detailed Report</h2>")
            report_file.write("<ul>")
            if isinstance(results, list):  # Add this check
                for line in results:
                    report_file.write(f"<li>{html.escape(line)}</li>")
            report_file.write("</ul>")
            report_file.write("</body></html>")

        print(f"Detailed HTML report saved to: {report_file_path}")

    def save_txt_report(self, tool_name, results):
        report_file_path = f"{self.file_path}_report_{tool_name.lower()}.txt"
        with open(report_file_path, "w", encoding="utf-8") as report_file:
            # Write an underlined pattern for labels in the TXT report
            report_file.write("=" * (len(tool_name) + 17) + "\n")
            report_file.write(f"{tool_name} Detailed Report\n")
            report_file.write("=" * (len(tool_name) + 17) + "\n")

            if isinstance(results, list):
                for line in results:
                    report_file.write(f"{line}\n")

        print(f"Detailed TXT report saved to: {report_file_path}")

    def detect_language(self):
        _, extension = os.path.splitext(self.file_path)
        language = "Python" if extension == ".py" else "Unknown"
        print(f"\nDetected Language: {language}")
        print("=" * len(f"Detected Language: {language}"))


