from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.email_address_object import EmailAddressObject
from ..livtypes import UNSET, Unset

if TYPE_CHECKING:
    from ..models.admin import Admin
    from ..models.identification_link import IdentificationLink
    from ..models.otp import OTP


T = TypeVar("T", bound="EmailAddress")


@attr.s(auto_attribs=True)
class EmailAddress:
    """
    Attributes:
        object_ (EmailAddressObject): String representing the object's type. Objects of the same type share the same
            value.
        email_address (str):
        reserved (bool):
        linked_to (List['IdentificationLink']):
        id (Union[Unset, str]):
        verification (Union['Admin', 'OTP', None]):
    """

    object_: EmailAddressObject
    email_address: str
    reserved: bool
    linked_to: List["IdentificationLink"]
    verification: Union["Admin", "OTP", None]
    id: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.otp import OTP

        object_ = self.object_.value

        email_address = self.email_address
        reserved = self.reserved
        linked_to = []
        for linked_to_item_data in self.linked_to:
            linked_to_item = linked_to_item_data.to_dict()

            linked_to.append(linked_to_item)

        id = self.id
        verification: Union[Dict[str, Any], None]
        if self.verification is None:
            verification = None

        elif isinstance(self.verification, OTP):
            verification = self.verification.to_dict()

        else:
            verification = self.verification.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "object": object_,
                "email_address": email_address,
                "reserved": reserved,
                "linked_to": linked_to,
                "verification": verification,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.admin import Admin
        from ..models.identification_link import IdentificationLink
        from ..models.otp import OTP

        d = src_dict.copy()
        object_ = EmailAddressObject(d.pop("object"))

        email_address = d.pop("email_address")

        reserved = d.pop("reserved")

        linked_to = []
        _linked_to = d.pop("linked_to")
        for linked_to_item_data in _linked_to:
            linked_to_item = IdentificationLink.from_dict(linked_to_item_data)

            linked_to.append(linked_to_item)

        id = d.pop("id", UNSET)

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

        email_address = cls(
            object_=object_,
            email_address=email_address,
            reserved=reserved,
            linked_to=linked_to,
            id=id,
            verification=verification,
        )

        return email_address
