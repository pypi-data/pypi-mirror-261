from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="VerifyTOTPJsonBody")


@attr.s(auto_attribs=True)
class VerifyTOTPJsonBody:
    """
    Attributes:
        code (str): The TOTP or backup code to verify
    """

    code: str

    def to_dict(self) -> Dict[str, Any]:
        code = self.code

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "code": code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code")

        verify_totp_json_body = cls(
            code=code,
        )

        return verify_totp_json_body
