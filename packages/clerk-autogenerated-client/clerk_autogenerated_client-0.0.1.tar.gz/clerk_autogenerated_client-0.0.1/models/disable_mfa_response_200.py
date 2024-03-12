from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..livtypes import UNSET, Unset

T = TypeVar("T", bound="DisableMFAResponse200")


@attr.s(auto_attribs=True)
class DisableMFAResponse200:
    """
    Attributes:
        user_id (Union[Unset, str]):
    """

    user_id: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("user_id", UNSET)

        disable_mfa_response_200 = cls(
            user_id=user_id,
        )

        return disable_mfa_response_200
