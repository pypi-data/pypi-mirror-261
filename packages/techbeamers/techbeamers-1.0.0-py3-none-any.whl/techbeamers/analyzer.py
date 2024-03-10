"""
analyzer.py by TechBeamers

This script provides a tool for analyzing Python code using PEP 8, Flake8, and MyPy.
...
"""

import sys

import argparse
from techbeamers.code_analyzer import CodeAnalyzer


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="Code Analyzer Tool", formatter_class=CustomFormatter
    )

    parser.add_argument(
        "file_path", nargs="?", help="Path to the Python file to analyze"
    )
    parser.add_argument(
        "--report-format",
        choices=["html", "txt"],
        default="html",
        help="Format for saving detailed reports (html or txt)",
    )
    parser.add_argument(
        "--analyze-pep8", action="store_true", help="Perform PEP 8 analysis"
    )
    parser.add_argument(
        "--analyze-flake8", action="store_true", help="Perform Flake8 analysis"
    )
    parser.add_argument(
        "--analyze-mypy", action="store_true", help="Perform MyPy analysis"
    )
    parser.add_argument(
        "--disable-all", action="store_true", help="Disable all analyses"
    )

    # Additional information
    additional_info = """
Customization Options:
  - Specify the path to the Python file to analyze.
  - Choose the format for saving detailed reports using --report-format.
  - Supported formats: 'html' (default) or 'txt'.
  - Use --analyze-pep8, --analyze-flake8, --analyze-mypy to on/off analyses.
  - Use --disable-all to disable all analyses.
"""

    # Apply the additional information to the help text
    parser.epilog = additional_info

    args = parser.parse_args()

    # Check if --disable-all is specified
    disable_all_arg = args.disable_all
    if disable_all_arg:
        print("All analyses are disabled.")
        sys.exit(0)

    # Check if a file path is provided as a command-line argument
    file_path_arg = args.file_path or None
    report_format_arg = args.report_format.lower()
    analyze_pep8_arg = args.analyze_pep8
    analyze_flake8_arg = args.analyze_flake8
    analyze_mypy_arg = args.analyze_mypy

    # Check if a file path is provided
    if not file_path_arg:
        print("No file selected for analysis.")
        print("Please provide the path to the Python file to analyze.")
        print("Check the available options below:\n")
        parser.print_help()
        sys.exit(1)

    # Create CodeAnalyzer instance
    analyzer = CodeAnalyzer(
        file_path_arg,
        report_format=report_format_arg,
        analyze_pep8=analyze_pep8_arg,
        analyze_flake8=analyze_flake8_arg,
        analyze_mypy=analyze_mypy_arg
    )
    analyzer.run_analysis()
    analyzer.detect_language()
    analyzer.generate_statistics()


class CustomFormatter(
    argparse.RawDescriptionHelpFormatter, argparse.ArgumentDefaultsHelpFormatter
):
    pass


if __name__ == "__main__":

    main()
 
