from pathlib import Path
import os

def scan_directory(directory: Path) -> list[Path]:
    file_paths: list[Path] = []
    
    for dirpath, _, files in os.walk(directory):
        for file in files:
            if Path(file).suffix in {'.c', '.cpp'}:
                file_path = Path(dirpath) / file
                file_paths.append(file_path)

    return file_paths
