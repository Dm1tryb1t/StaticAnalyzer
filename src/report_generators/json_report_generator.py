import json
from pathlib import Path

from config.finding import Finding


def generate_report_json(findings: list[Finding], report_file: Path) -> None:
    report_file.parent.mkdir(parents=True, exist_ok=True)

    payload = {
        "summary": {
            "total_findings": len(findings),
            "total_files": len({finding.file_path for finding in findings}),
        },
        "findings": [finding.to_dict() for finding in findings],
    }

    with report_file.open("w", encoding="utf-8") as report:
        json.dump(payload, report, indent=2, ensure_ascii=False)
        report.write("\n")
