import sys
from pathlib import Path

from analysis_runner import print_analysis_summary, run_analysis
from args_parser import parse_args

def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])

    directory = Path(args.directory).resolve()
    config_path = Path(args.config).resolve()
    output_dir = Path(args.output_dir).resolve()

    result = run_analysis(directory, config_path, output_dir, args.format)
    print_analysis_summary(result)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
