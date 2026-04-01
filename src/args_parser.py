import argparse

from config.config_loader import DEFAULT_CONFIG_PATH, DEFAULT_OUTPUT_DIR


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
    return parser.parse_args(argv)
