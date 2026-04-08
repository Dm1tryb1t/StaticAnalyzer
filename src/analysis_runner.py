from pathlib import Path

from config.config_loader import load_dangerous_functions
from core.analysis_result import AnalysisResult
from core.finding import Finding
from report_generators.report_generator import write_reports
from scanners.directory_scanner import scan_directory
from scanners.regex_code_scanner import regex_scan_for_dangerous_functions

from scanners.ast_code_scanner import ast_scan_for_dangerous_functions

def build_analysis_result(directory: Path, output_dir: Path) -> AnalysisResult:
    return AnalysisResult(
        directory=directory,
        output_dir=output_dir,
        scanned_files=[],
        findings=[],
    )


def collect_findings(result: AnalysisResult, dangerous_functions: list[str], regex_enabled: bool) -> None:
    for file_path in scan_directory(result.directory):
        result.add_scanned_file(file_path)
        result.extend_findings(
            regex_scan_for_dangerous_functions(file_path, dangerous_functions) if regex_enabled
            else ast_scan_for_dangerous_functions(file_path, dangerous_functions)
        )


def run_analysis(directory: Path, config_path: Path, output_dir: Path, output_format: str, regex_enabled: bool) -> AnalysisResult:
    dangerous_functions = load_dangerous_functions(config_path)
    result = build_analysis_result(directory, output_dir)
    collect_findings(result, dangerous_functions, regex_enabled)
    write_reports(result, output_format)
    return result


def print_analysis_summary(result: AnalysisResult) -> None:
    print(f"Scanned directory: {result.directory}")
    print(f"Scanned files: {result.scanned_files_count}")
    print(f"Found {len(result.findings)} potentially dangerous call(s).")
    print(f"Reports saved to: {result.output_dir}")
