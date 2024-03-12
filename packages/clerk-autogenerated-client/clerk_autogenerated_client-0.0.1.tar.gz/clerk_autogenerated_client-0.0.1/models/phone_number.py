from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.phone_number_object import PhoneNumberObject
from ..livtypes import UNSET, Unset

if TYPE_CHECKING:
    from ..models.admin import Admin
    from ..models.identification_link import IdentificationLink
    from ..models.otp import OTP


T = TypeVar("T", bound="PhoneNumber")


@attr.s(auto_attribs=True)
class PhoneNumber:
    """
    Attributes:
        object_ (PhoneNumberObject): String representing the object's type. Objects of the same type share the same
            value.
        phone_number (str):
        reserved (bool):
        linked_to (List['IdentificationLink']):
        id (Union[Unset, str]):
        reserved_for_second_factor (Union[Unset, bool]):
        default_second_factor (Union[Unset, bool]):
        verification (Union['Admin', 'OTP', None]):
        backup_codes (Union[Unset, None, List[str]]):
    """

    object_: PhoneNumberObject
    phone_number: str
    reserved: bool
    linked_to: List["IdentificationLink"]
    verification: Union["Admin", "OTP", None]
    id: Union[Unset, str] = UNSET
    reserved_for_second_factor: Union[Unset, bool] = UNSET
    default_second_factor: Union[Unset, bool] = UNSET
    backup_codes: Union[Unset, None, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.otp import OTP

        object_ = self.object_.value

        phone_number = self.phone_number
        reserved = self.reserved
        linked_to = []
        for linked_to_item_data in self.linked_to:
            linked_to_item = linked_to_item_data.to_dict()

            linked_to.append(linked_to_item)

        id = self.id
        reserved_for_second_factor = self.reserved_for_second_factor
        default_second_factor = self.default_second_factor
        verification: Union[Dict[str, Any], None]
        if self.verification is None:
            verification = None

        elif isinstance(self.verification, OTP):
            verification = self.verification.to_dict()

        else:
            verification = self.verification.to_dict()

        backup_codes: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.backup_codes, Unset):
            if self.backup_codes is None:
                backup_codes = None
            else:
                backup_codes = self.backup_codes

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "object": object_,
                "phone_number": phone_number,
                "reserved": reserved,
                "linked_to": linked_to,
                "verification": verification,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if reserved_for_second_factor is not UNSET:
            field_dict["reserved_for_second_factor"] = reserved_for_second_factor
        if default_second_factor is not UNSET:
            field_dict["default_second_factor"] = default_second_factor
        if backup_codes is not UNSET:
            field_dict["backup_codes"] = backup_codes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.admin import Admin
        from ..models.identification_link import IdentificationLink
        from ..models.otp import OTP

        d = src_dict.copy()
        object_ = PhoneNumberObject(d.pop("object"))

        phone_number = d.pop("phone_number")

        reserved = d.pop("reserved")

        linked_to = []
        _linked_to = d.pop("linked_to")
        for linked_to_item_data in _linked_to:
            linked_to_item = IdentificationLink.from_dict(linked_to_item_data)

            linked_to.append(linked_to_item)

        id = d.pop("id", UNSET)

        reserved_for_second_factor = d.pop("reserved_for_second_factor", UNSET)

        default_second_factor = d.pop("default_second_factor", UNSET)

        def _parse_verification(data: object) -> Union["Admin", "OTP", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verification_type_0 = OTP.from_dict(data)

                return verification_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            verification_type_1 = Admin.from_dict(data)

            return verification_type_1

        verification = _parse_verification(d.pop("verification"))

        backup_codes = cast(List[str], d.pop("backup_codes", UNSET))

        phone_number = cls(
            object_=object_,
            phone_number=phone_number,
            reserved=reserved,
            linked_to=linked_to,
            id=id,
            reserved_for_second_factor=reserved_for_second_factor,
            default_second_factor=default_second_factor,
            verification=verification,
            backup_codes=backup_codes,
        )

        return phone_number
