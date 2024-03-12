from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..livtypes import UNSET, Unset

T = TypeVar("T", bound="UpdatePhoneNumberJsonBody")


@attr.s(auto_attribs=True)
class UpdatePhoneNumberJsonBody:
    """
    Attributes:
        verified (Union[Unset, None, bool]): The phone number will be marked as verified.
        primary (Union[Unset, None, bool]): Set this phone number as the primary phone number for the user.
    """

    verified: Union[Unset, None, bool] = UNSET
    primary: Union[Unset, None, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        verified = self.verified
        primary = self.primary

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if verified is not UNSET:
            field_dict["verified"] = verified
        if primary is not UNSET:
            field_dict["primary"] = primary

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        verified = d.pop("verified", UNSET)

        primary = d.pop("primary", UNSET)

        update_phone_number_json_body = cls(
            verified=verified,
            primary=primary,
        )

        update_phone_number_json_body.additional_properties = d
        return update_phone_number_json_body

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
