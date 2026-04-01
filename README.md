# StaticAnalyzer

## Overview

`StaticAnalyzer` is a small regex-based static analyzer for C/C++ source files.
It scans `.c` and `.cpp` files, searches for calls to potentially dangerous
functions, and generates reports in text and/or JSON format.

The project is intentionally simple: it does not build an AST and does not try
to understand program semantics. The current implementation is focused on a
clear structure and configurable regex checks.

## How It Works

1. `src/main.py` acts as a thin entry point.
2. Arguments are parsed in `src/args_parser.py`.
3. Dangerous function names are loaded from `src/config/dangerous_functions.txt`.
4. The analyzer scans the target directory for `.c` and `.cpp` files.
5. Each file is checked with regex patterns.
6. Findings are written to text and/or JSON reports.

## Detected Functions

By default, the analyzer checks the functions listed in
`src/config/dangerous_functions.txt`:

- `strcpy`
- `gets`
- `sprintf`
- `system`

You can extend or replace this list with your own config file.

## Output

Reports are written to the `reports` directory by default:

- `reports/dangerous_functions_report.txt`
- `reports/dangerous_functions_report.json`

### Text Report Format

Each line has the following structure:

```text
path/to/file:line_number -> line_content
```

### JSON Report Format

The JSON report contains:

- `summary.total_findings`
- `summary.total_files`
- `findings` array with:
  - `function`
  - `file_path`
  - `line_number`
  - `line_content`

## Usage

Run the analyzer from the project root:

```sh
python src/main.py
```

Scan a specific directory:

```sh
python src/main.py path/to/project
```

Generate only a text report:

```sh
python src/main.py path/to/project --format text
```

Generate only a JSON report:

```sh
python src/main.py path/to/project --format json
```

Use a custom config file:

```sh
python src/main.py path/to/project --config path/to/functions.txt
```

Write reports to a custom directory:

```sh
python src/main.py path/to/project --output-dir path/to/reports
```

Show CLI help:

```sh
python src/main.py --help
```

## Project Structure

```text
src/
├── main.py
├── analysis_runner.py
├── args_parser.py
├── config/
│   ├── config_loader.py
│   └── dangerous_functions.txt
├── core/
│   └── finding.py
├── report_generators/
│   ├── report_generator.py
│   ├── text_report_generator.py
│   └── json_report_generator.py
└── scanners/
    ├── directory_scanner.py
    └── regex_code_scanner.py
```

## Limitations

- The analyzer uses regex only.
- It does not distinguish between code, comments, and string literals.
- It may produce false positives.
- It does not analyze control flow or data flow.
- It currently scans only `.c` and `.cpp` files.

## Future Improvements

- Ignore matches inside comments and string literals.
- Add severity or category metadata for findings.
- Support more dangerous functions and pattern groups.
- Add filtering by file extension and ignore paths.
- Add unit tests for CLI, scanning, and report generation.
- Improve path/package consistency across the project.
- Add optional AST-based analysis for more accurate checks.
