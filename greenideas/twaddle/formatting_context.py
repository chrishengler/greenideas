from dataclasses import dataclass
from typing import Optional


@dataclass
class FormattingContext:
    value: str = ""
    needs_space: bool = False
    queued_punctuation: Optional[str] = None
