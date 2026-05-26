"""Employee Management System - Main entry point.

Usage:
    python main.py input.txt output.txt
"""
import sys

from command_parser import CommandParser
from command_factory import build_command
from employee_store import EmployeeStore


def print_usage():
    print("Input / output format is txt file. Read input file and generate output file.")
    print("Usage : python main.py input.txt output.txt")


def main():
    if len(sys.argv) < 3:
        print_usage()
        print("Wrong arguments count", file=sys.stderr)
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    # Read input file
    try:
        with open(input_filename, "r", encoding="utf-8") as f:
            lines = [line.rstrip("\n").rstrip("\r") for line in f.readlines()]
    except FileNotFoundError:
        raise ValueError(f"Input file {input_filename} does NOT exist")

    parser = CommandParser()
    store = EmployeeStore()
    output_buffer = []

    for line in lines:
        if not line.strip():
            continue
        try:
            token_group = parser.parse(line)
            command = build_command(token_group)
            result = command.execute(store)
            output_buffer.extend(result)
        except Exception as e:
            output_buffer.append(f"wrong command : {line}")

    # Write output file
    with open(output_filename, "w", encoding="utf-8") as f:
        for out_line in output_buffer:
            f.write(out_line + "\n")


if __name__ == "__main__":
    main()
