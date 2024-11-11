from dataclasses import dataclass

@dataclass
class DemoResponse:
    message: str
    data: dict
    status: int