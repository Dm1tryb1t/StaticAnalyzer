from dataclasses import dataclass
from pathlib import Path

from config.config_loader import load_dangerous_functions
from config.finding import Finding
from report_generators.report_generator import write_reports
from scanners.directory_scanner import scan_directory
from scanners.regex_code_scanner import regex_scan_for_dangerous_functions


@dataclass(slots=True)
class AnalysisResult:
    directory: Path
    output_dir: Path
    findings: list[Finding]


def collect_findings(directory: Path, dangerous_functions: list[str]) -> list[Finding]:
    findings: list[Finding] = []

    for file_path in scan_directory(directory):
        findings.extend(
            regex_scan_for_dangerous_functions(file_path, dangerous_functions)
        )

    return findings


def run_analysis(directory: Path, config_path: Path, output_dir: Path, output_format: str) -> AnalysisResult:
    dangerous_functions = load_dangerous_functions(config_path)
    findings = collect_findings(directory, dangerous_functions)
    write_reports(findings, output_dir, output_format)
    return AnalysisResult(directory=directory, output_dir=output_dir, findings=findings)


def print_analysis_summary(result: AnalysisResult) -> None:
    print(f"Scanned directory: {result.directory}")
    print(f"Found {len(result.findings)} potentially dangerous call(s).")
    print(f"Reports saved to: {result.output_dir}")
