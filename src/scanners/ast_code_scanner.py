from pathlib import Path

from clang.cindex import Cursor, CursorKind, Index, TranslationUnit

from core.finding import Finding


def parse_source_file(file_path: Path):
    index = Index.create()
    return index.parse(
        str(file_path),
        args=[
            "-x",
            "c++",
            "-std=c++17",
        ],
        options=TranslationUnit.PARSE_DETAILED_PROCESSING_RECORD,
    )


def walk_ast(node: Cursor):
    yield node
    for child in node.get_children():
        yield from walk_ast(child)


def is_function_call(node: Cursor) -> bool:
    return node.kind == CursorKind.CALL_EXPR


def extract_function_name(node: Cursor) -> str | None:
    if node.spelling:
        return node.spelling

    for child in node.get_children():
        if child.spelling:
            return child.spelling

    return None


def get_line_content(lines: list[str], line_number: int) -> str:
    if 1 <= line_number <= len(lines):
        return lines[line_number - 1].rstrip()
    return ""


def build_finding(
    file_path: Path,
    node: Cursor,
    function_name: str,
    lines: list[str],
) -> Finding:
    line_number = node.location.line
    line_content = get_line_content(lines, line_number)

    return Finding(
        function=function_name,
        file_path=str(file_path),
        line_number=line_number,
        line_content=line_content,
    )


def is_from_current_file(node: Cursor, file_path: Path) -> bool:
    if node.location.file is None:
        return False

    try:
        node_path = Path(str(node.location.file)).resolve()
        current_path = file_path.resolve()
    except OSError:
        return False

    return node_path == current_path


def ast_scan_for_dangerous_functions(
    file_path: Path,
    dangerous_functions: list[str],
) -> list[Finding]:
    findings: list[Finding] = []

    with file_path.open("r", encoding="utf-8", errors="ignore") as source_file:
        lines = source_file.readlines()

    dangerous_set = set(dangerous_functions)

    try:
        translation_unit = parse_source_file(file_path)
    except Exception:
        return findings

    for node in walk_ast(translation_unit.cursor):
        if not is_from_current_file(node, file_path):
            continue

        if not is_function_call(node):
            continue

        function_name = extract_function_name(node)
        if function_name is None:
            continue

        if function_name not in dangerous_set:
            continue

        findings.append(build_finding(file_path, node, function_name, lines))

    return findings
