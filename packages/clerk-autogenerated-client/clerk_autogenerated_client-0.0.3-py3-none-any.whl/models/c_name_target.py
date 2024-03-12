from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="CNameTarget")


@attr.s(auto_attribs=True)
class CNameTarget:
    """
    Attributes:
        host (str):
        value (str):
    """

    host: str
    value: str

    def to_dict(self) -> Dict[str, Any]:
        host = self.host
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "host": host,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        host = d.pop("host")

        value = d.pop("value")

        c_name_target = cls(
            host=host,
            value=value,
        )

        return c_name_target
