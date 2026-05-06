from dataclasses import dataclass
from typing import Optional


@dataclass
class FormattingContext:
    display_twaddle_string: str = ""
    internal_twaddle_string: str = ""
    needs_space: bool = False
    queued_punctuation: Optional[str] = None
