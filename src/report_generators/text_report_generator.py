from pathlib import Path

from core.finding import Finding


def generate_report_txt(findings: list[Finding], report_file: Path) -> None:
    report_file.parent.mkdir(parents=True, exist_ok=True)

    with report_file.open("w", encoding="utf-8") as report:
        for finding in findings:
            report.write(
                f"{finding.file_path}:{finding.line_number} -> {finding.line_content}\n"
            )
