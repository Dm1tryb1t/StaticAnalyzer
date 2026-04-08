# StaticAnalyzer

## Overview

`StaticAnalyzer` is a lightweight static analyzer for C and C++ projects.
It scans source and header files, searches for calls to potentially dangerous
functions, and generates reports in text and JSON formats.

The project currently supports two scanning modes:

- AST-based analysis through `clang.cindex`
- regex-based analysis as a simpler fallback

At the moment, AST scanning is the default mode. Regex scanning can be enabled
explicitly through the CLI.

## Supported Files

The analyzer scans files with these extensions:

- `.c`
- `.cpp`
- `.cc`
- `.h`
- `.hpp`

## Detected Functions

The list of dangerous functions is loaded from
`src/config/dangerous_functions.txt`.

By default, the config contains:

- `strcpy`
- `gets`
- `sprintf`
- `system`

You can replace this list with your own config file through `--config`.

## Project Structure

```text
src/
|- main.py
|- analysis_runner.py
|- args_parser.py
|- config/
|  |- config_loader.py
|  `- dangerous_functions.txt
|- core/
|  |- analysis_result.py
|  `- finding.py
|- report_generators/
|  |- report_generator.py
|  |- text_report_generator.py
|  `- json_report_generator.py
`- scanners/
   |- ast_code_scanner.py
   |- directory_scanner.py
   `- regex_code_scanner.py
```

## How It Works

1. `src/main.py` parses CLI arguments and normalizes paths.
2. `src/analysis_runner.py` creates `AnalysisResult`.
3. The analyzer loads dangerous function names from config.
4. `src/scanners/directory_scanner.py` collects supported source files.
5. Each file is scanned either:
   - through AST in `src/scanners/ast_code_scanner.py`, or
   - through regex in `src/scanners/regex_code_scanner.py`
6. Findings and scanned files are accumulated inside `AnalysisResult`.
7. Reports are generated into the output directory.

## Installation

Install Python dependencies:

```sh
pip install -r requirements.txt
```

For AST scanning, Python package `clang` is not enough by itself. You also need
an installed LLVM/Clang distribution with `libclang`.

On Windows with MSYS2 UCRT64, a typical setup is:

```sh
pacman -S mingw-w64-ucrt-x86_64-python mingw-w64-ucrt-x86_64-clang
```

If `clang.cindex` cannot find `libclang`, configure the path in code with
`clang.cindex.Config.set_library_file(...)`.

## Usage

Run the analyzer from the project root:

```sh
python src/main.py
```

Scan a specific directory:

```sh
python src/main.py path/to/project
```

Use regex scanning instead of AST scanning:

```sh
python src/main.py path/to/project --regex
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

Show help:

```sh
python src/main.py --help
```

## Output

By default, reports are written to `reports/`:

- `reports/dangerous_functions_report.txt`
- `reports/dangerous_functions_report.json`

### Text Report

Each line has this format:

```text
path/to/file:line_number -> line_content
```

### JSON Report

The JSON report contains:

- `summary.total_files_scanned`
- `summary.potentially_dangerous_calls`
- `summary.files_with_potentially_dangerous_calls`
- `scanned_files`
- `findings`

Each finding contains:

- `function`
- `file_path`
- `line_number`
- `line_content`

## Current Limitations

- AST scanning depends on a working local `libclang` installation.
- The current AST parser setup uses a simple generic C++ configuration.
- Regex mode may produce false positives in comments and string literals.
- The analyzer does not perform control-flow or data-flow analysis.
- The analyzer only checks direct function-name matches from the config.
- The project still has a few rough edges unrelated to naming, such as basic AST configuration and missing automated tests.

## Future Improvements

- Add automatic fallback from AST mode to regex mode when `libclang` is unavailable.
- Improve AST parsing for mixed C and C++ projects.
- Distinguish function categories or severity levels in findings.
- Add filtering by path, extension, and ignored directories.
- Add deduplication rules for repeated findings.
- Add tests for CLI parsing, directory scanning, AST scanning, regex scanning, and report generation.
- Add CI checks for linting, test execution, and sample report validation.
