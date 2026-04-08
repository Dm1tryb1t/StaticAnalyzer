import argparse
from pathlib import Path

from config.config_loader import DEFAULT_CONFIG_PATH, DEFAULT_OUTPUT_DIR

def normalize_input_path(raw_path: str) -> Path:
    # print(f"[DEBUG] raw: {raw_path}")
    # print(f"[DEBUG] resolved: {Path(raw_path).expanduser().resolve(strict=False)}")
    return Path(raw_path).expanduser().resolve(strict=False)

def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Scan C/C++ files for potentially dangerous function usage.",
    )
    parser.add_argument(
        "directory",
        nargs="?",
        default=".",
        help="Directory to scan. Defaults to the current directory.",
    )
    parser.add_argument(
        "--config",
        default=str(DEFAULT_CONFIG_PATH),
        help="Path to the file with dangerous function names.",
    )
    parser.add_argument(
        "--output-dir",
        default=str(DEFAULT_OUTPUT_DIR),
        help="Directory where reports will be written.",
    )
    parser.add_argument(
        "--format",
        choices=("text", "json", "both"),
        default="both",
        help="Report format to generate.",
    )
    parser.add_argument(
        "--regex",
        action="store_true",
        help="Enable regex-based scanning.",
    )
    return parser.parse_args(argv)
