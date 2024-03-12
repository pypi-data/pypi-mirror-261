from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="VerifyPasswordJsonBody")


@attr.s(auto_attribs=True)
class VerifyPasswordJsonBody:
    """
    Attributes:
        password (str): The user password to verify
    """

    password: str

    def to_dict(self) -> Dict[str, Any]:
        password = self.password

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "password": password,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        password = d.pop("password")

        verify_password_json_body = cls(
            password=password,
        )

        return verify_password_json_body
