import sys
from pathlib import Path

from analysis_runner import print_analysis_summary, run_analysis
from args_parser import parse_args, normalize_input_path

def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])

    directory = normalize_input_path(args.directory)
    config_path = normalize_input_path(args.config)
    output_dir = normalize_input_path(args.output_dir)

    result = run_analysis(directory, config_path, output_dir, args.format)
    print_analysis_summary(result)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
