from pathlib import Path

from core.finding import Finding
from report_generators.json_report_generator import generate_report_json
from report_generators.text_report_generator import generate_report_txt

def write_reports(findings: list[Finding], output_dir: Path, output_format: str) -> None:
    if output_format in {"text", "both"}:
        generate_report_txt(findings, output_dir / "dangerous_functions_report.txt")

    if output_format in {"json", "both"}:
        generate_report_json(findings, output_dir / "dangerous_functions_report.json")
