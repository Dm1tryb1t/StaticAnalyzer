# StaticAnalyzer

## Overview

A simple regex-based static analysis tool for detecting potentially dangerous C/C++ functions.

⚠️ This is a lightweight implementation that does **not distinguish between code, comments, and string literals**, which may lead to false positives.

---

## Detected Functions

The scanner searches for the following potentially dangerous functions:

* `strcpy`
* `gets`
* `sprintf`
* `system`

---

## Output

The scan results are saved to:

```
reports/dangerous_functions_report.txt
```

Each entry has the following format:

```
path/to/file:line_number -> line_content
```

---

## Usage

Run the scanner from the project root directory:

```sh
python ./src/scanner/dangerous_function_scanner.py path/to/project/dir
```

If no directory is specified, the current directory will be scanned:

```sh
python ./src/scanner/dangerous_function_scanner.py
```

---

## Limitations

* Uses regex-based pattern matching (no AST analysis)
* May produce false positives in:

  * comments
  * string literals
* Does not analyze data flow or context

---

## Future Improvements

* Add AST-based analysis
* Reduce false positives
* Support more dangerous patterns
* Add structured output (e.g., JSON)
* Improve CLI interface
