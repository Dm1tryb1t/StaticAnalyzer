from dataclasses import asdict, dataclass


@dataclass(slots=True)
class Finding:
    function: str
    file_path: str
    line_number: int
    line_content: str

    def to_dict(self) -> dict[str, str | int]:
        return asdict(self)
