from enum import Enum


class EmailObject(str, Enum):
    EMAIL = "email"

    def __str__(self) -> str:
        return str(self.value)
