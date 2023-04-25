from enum import Enum
from dataclasses import dataclass


class TokenType(Enum):
    """Enum class for token types."""
    NUMBER = 1
    PLUS = 2
    MINUS = 3
    MULTIPLY = 4
    DIVIDE = 5
    POWER = 6
    ROOT = 7
    FACTORIAL = 8
    LEFT_PAREN = 9
    RIGHT_PAREN = 10


@dataclass
class Token:
    type: TokenType
    value: str

    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value else "")

