from typing import Any, Dict, List, Optional, Type, TypeVar

import attr

from ..models.saml_connection_object import SAMLConnectionObject

T = TypeVar("T", bound="SAMLConnection")


@attr.s(auto_attribs=True)
class SAMLConnection:
    """
    Attributes:
        object_ (SAMLConnectionObject):
        id (str):
        name (str):
        domain (str):
        acs_url (str):
        sp_entity_id (str):
        active (bool):
        provider (str):
        user_count (int):
        sync_user_attributes (bool):
        created_at (int): Unix timestamp of creation.
        updated_at (int): Unix timestamp of last update.
        idp_entity_id (Optional[str]):
        idp_sso_url (Optional[str]):
        idp_certificate (Optional[str]):
    """

    object_: SAMLConnectionObject
    id: str
    name: str
    domain: str
    acs_url: str
    sp_entity_id: str
    active: bool
    provider: str
    user_count: int
    sync_user_attributes: bool
    created_at: int
    updated_at: int
    idp_entity_id: Optional[str]
    idp_sso_url: Optional[str]
    idp_certificate: Optional[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_.value

        id = self.id
        name = self.name
        domain = self.domain
        acs_url = self.acs_url
        sp_entity_id = self.sp_entity_id
        active = self.active
        provider = self.provider
        user_count = self.user_count
        sync_user_attributes = self.sync_user_attributes
        created_at = self.created_at
        updated_at = self.updated_at
        idp_entity_id = self.idp_entity_id
        idp_sso_url = self.idp_sso_url
        idp_certificate = self.idp_certificate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "id": id,
                "name": name,
                "domain": domain,
                "acs_url": acs_url,
                "sp_entity_id": sp_entity_id,
                "active": active,
                "provider": provider,
                "user_count": user_count,
                "sync_user_attributes": sync_user_attributes,
                "created_at": created_at,
                "updated_at": updated_at,
                "idp_entity_id": idp_entity_id,
                "idp_sso_url": idp_sso_url,
                "idp_certificate": idp_certificate,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        object_ = SAMLConnectionObject(d.pop("object"))

        id = d.pop("id")

        name = d.pop("name")

        domain = d.pop("domain")

        acs_url = d.pop("acs_url")

        sp_entity_id = d.pop("sp_entity_id")

        active = d.pop("active")

        provider = d.pop("provider")

        user_count = d.pop("user_count")

        sync_user_attributes = d.pop("sync_user_attributes")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        idp_entity_id = d.pop("idp_entity_id")

        idp_sso_url = d.pop("idp_sso_url")

        idp_certificate = d.pop("idp_certificate")

        saml_connection = cls(
            object_=object_,
            id=id,
            name=name,
            domain=domain,
            acs_url=acs_url,
            sp_entity_id=sp_entity_id,
            active=active,
            provider=provider,
            user_count=user_count,
            sync_user_attributes=sync_user_attributes,
            created_at=created_at,
            updated_at=updated_at,
            idp_entity_id=idp_entity_id,
            idp_sso_url=idp_sso_url,
            idp_certificate=idp_certificate,
        )

        saml_connection.additional_properties = d
        return saml_connection

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
