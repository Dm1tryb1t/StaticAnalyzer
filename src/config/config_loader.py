from pathlib import Path

DEFAULT_OUTPUT_DIR = Path(__file__).resolve().parent.parent.parent / "reports"
DEFAULT_CONFIG_PATH = Path(__file__).resolve().parent / "dangerous_functions.txt"


def load_dangerous_functions(config_path: Path) -> list[str]:
    with config_path.open("r", encoding="utf-8") as config_file:
        content = config_file.read()

    functions = [item.strip() for item in content.split() if item.strip()]
    return sorted(set(functions))
