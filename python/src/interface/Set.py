from typing import Any, Iterator

class Set:
    def __init__(self, *args, **kwargs) -> None:
        ...

    def build(self, x) -> None:
        ...

    def len(self) -> int:
        ...

    def find(self, x: Any) -> bool:
        ...

    def insert(self, x: Any) -> None:
        ...

    def delete(self, x: Any) -> None:
        ...

    def iter_ord(self) -> Iterator:
        ...

    def find_min(self) -> Any:
        ...

    def find_max(self) -> Any:
        ...

    def find_next(self, x: Any) -> Any:
        ...

    def find_prev(self, x: Any) -> Any:
        ...