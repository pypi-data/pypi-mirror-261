from typing import TYPE_CHECKING, Any, Dict, Optional, Type, TypeVar, Union

import attr

from ..models.saml_account_object import SAMLAccountObject
from ..livtypes import UNSET, Unset

if TYPE_CHECKING:
    from ..models.saml import SAML


T = TypeVar("T", bound="SAMLAccount")


@attr.s(auto_attribs=True)
class SAMLAccount:
    """
    Attributes:
        id (str):
        object_ (SAMLAccountObject): String representing the object's type. Objects of the same type share the same
            value.
        provider (str):
        active (bool):
        email_address (str):
        first_name (Union[Unset, None, str]):
        last_name (Union[Unset, None, str]):
        provider_user_id (Union[Unset, None, str]):
        verification (Optional[SAML]):
    """

    id: str
    object_: SAMLAccountObject
    provider: str
    active: bool
    email_address: str
    verification: Optional["SAML"]
    first_name: Union[Unset, None, str] = UNSET
    last_name: Union[Unset, None, str] = UNSET
    provider_user_id: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        object_ = self.object_.value

        provider = self.provider
        active = self.active
        email_address = self.email_address
        first_name = self.first_name
        last_name = self.last_name
        provider_user_id = self.provider_user_id
        verification = self.verification.to_dict() if self.verification else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "object": object_,
                "provider": provider,
                "active": active,
                "email_address": email_address,
                "verification": verification,
            }
        )
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if provider_user_id is not UNSET:
            field_dict["provider_user_id"] = provider_user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.saml import SAML

        d = src_dict.copy()
        id = d.pop("id")

        object_ = SAMLAccountObject(d.pop("object"))

        provider = d.pop("provider")

        active = d.pop("active")

        email_address = d.pop("email_address")

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        provider_user_id = d.pop("provider_user_id", UNSET)

        _verification = d.pop("verification")
        verification: Optional[SAML]
        if _verification is None:
            verification = None
        else:
            verification = SAML.from_dict(_verification)

        saml_account = cls(
            id=id,
            object_=object_,
            provider=provider,
            active=active,
            email_address=email_address,
            first_name=first_name,
            last_name=last_name,
            provider_user_id=provider_user_id,
            verification=verification,
        )

        return saml_account
