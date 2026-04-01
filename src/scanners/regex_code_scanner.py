import re
from pathlib import Path

from core.finding import Finding


def regex_scan_for_dangerous_functions(file_path: Path, dangerous_functions: list[str]) -> list[Finding]:
    findings: list[Finding] = []

    with file_path.open("r", encoding="utf-8", errors="ignore") as code_file:
        lines = code_file.readlines()

    for line_number, line in enumerate(lines, start=1):
        stripped_line = line.rstrip()
        for function_name in dangerous_functions:
            pattern = rf"\b{re.escape(function_name)}\s*\("
            if re.search(pattern, line):
                findings.append(
                    Finding(
                        function=function_name,
                        file_path=str(file_path),
                        line_number=line_number,
                        line_content=stripped_line,
                    )
                )

    return findings
