import os
import sys
import re
from pathlib import Path

DANGEROUS_FUNCTIONS = [
    'strcpy', 
    'gets',
    'sprintf',
    'system'
]

def scan_for_dangerous_functions(file_path : Path) -> list[str]:
    report_entries : list[str] = []

    lines : list[str] = []

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as code_file:
        lines = code_file.readlines()

    for line_number, line in enumerate(lines, start=1):
        for func in DANGEROUS_FUNCTIONS:
            if re.search(rf"\b{re.escape(func)}\s*\(", line):
                report_entries.append(f"{file_path}:{line_number} -> {line.strip()}")

    return report_entries

def generate_report(entries: list[str], report_file: Path) -> None:
    with open(report_file, 'a') as report:
        for entry in entries:
            report.write(entry + '\n')

def scan_and_report(file_path: Path, report_file: Path) -> None:
    entries = scan_for_dangerous_functions(file_path)
    if entries:
        generate_report(entries, report_file)

def scan_directory(directory: Path, report_file: Path) -> None:
    with open(report_file, 'w'):
        pass  # Clear the report file
    
    for dirpath, _, files in os.walk(directory):
        for file in files:
            if Path(file).suffix in {'.c', '.cpp'}:
                file_path = Path(dirpath) / file
                scan_and_report(file_path, report_file)
    
    print(f"Scan complete. Report saved to {report_file}")

def main() -> None:
    directory = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
    report_file = Path('reports', 'dangerous_functions_report.txt')

    scan_directory(directory, report_file)

if __name__ == "__main__":
    main()
