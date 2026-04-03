from dataclasses import dataclass
from pathlib import Path

from core.finding import Finding


@dataclass(slots=True)
class Analysis_result:
    directory: Path
    output_dir: Path
    scanned_files: list[Path]
    findings: list[Finding]

    @property
    def scanned_files_count(self) -> int:
        return len(self.scanned_files)

    def add_scanned_file(self, file_path: Path) -> None:
        self.scanned_files.append(file_path)

    def extend_findings(self, findings: list[Finding]) -> None:
        self.findings.extend(findings)
