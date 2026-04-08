import json
from pathlib import Path

from core.analysis_result import AnalysisResult


def generate_report_json(result: AnalysisResult, report_file: Path) -> None:
    report_file.parent.mkdir(parents=True, exist_ok=True)

    payload = {
        "summary": {
            "total_files_scanned": result.scanned_files_count,
            "potentially_dangerous_calls": len(result.findings),
            "files_with_potentially_dangerous_calls": len(
                {finding.file_path for finding in result.findings}
            ),
        },
        "scanned_files": [str(file_path) for file_path in result.scanned_files],
        "findings": [finding.to_dict() for finding in result.findings],
    }

    with report_file.open("w", encoding="utf-8") as report:
        json.dump(payload, report, indent=2, ensure_ascii=False)
        report.write("\n")
