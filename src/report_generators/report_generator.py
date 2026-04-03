from pathlib import Path

from core.analisis_result import Analysis_result
from report_generators.json_report_generator import generate_report_json
from report_generators.text_report_generator import generate_report_txt

def write_reports(result: Analysis_result, output_format: str) -> None:
    result.findings.sort(key=lambda f: (f.file_path, f.line_number))

    if output_format in {"text", "both"}:
        generate_report_txt(
            result.findings,
            result.output_dir / "dangerous_functions_report.txt",
        )

    if output_format in {"json", "both"}:
        generate_report_json(
            result,
            result.output_dir / "dangerous_functions_report.json",
        )
