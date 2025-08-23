from dataclasses import dataclass
from typing import Generic
from typing import TypeVar

T = TypeVar('T')

@dataclass
class Mt5Result(Generic[T]):
    has_error : bool
    message : str
    result_code : int
    result : T | None


