from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..livtypes import UNSET, Unset

T = TypeVar("T", bound="CreatePhoneNumberJsonBody")


@attr.s(auto_attribs=True)
class CreatePhoneNumberJsonBody:
    """
    Attributes:
        user_id (Union[Unset, str]): The ID representing the user
        phone_number (Union[Unset, str]): The new phone number. Must adhere to the E.164 standard for phone number
            format.
        verified (Union[Unset, None, bool]): When created, the phone number will be marked as verified.
        primary (Union[Unset, None, bool]): Create this phone number as the primary phone number for the user.
            Default: false, unless it is the first phone number.
    """

    user_id: Union[Unset, str] = UNSET
    phone_number: Union[Unset, str] = UNSET
    verified: Union[Unset, None, bool] = UNSET
    primary: Union[Unset, None, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id
        phone_number = self.phone_number
        verified = self.verified
        primary = self.primary

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if verified is not UNSET:
            field_dict["verified"] = verified
        if primary is not UNSET:
            field_dict["primary"] = primary

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("user_id", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        verified = d.pop("verified", UNSET)

        primary = d.pop("primary", UNSET)

        create_phone_number_json_body = cls(
            user_id=user_id,
            phone_number=phone_number,
            verified=verified,
            primary=primary,
        )

        create_phone_number_json_body.additional_properties = d
        return create_phone_number_json_body

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
