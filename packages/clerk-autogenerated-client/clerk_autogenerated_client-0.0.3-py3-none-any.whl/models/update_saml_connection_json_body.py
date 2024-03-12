from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..livtypes import UNSET, Unset

T = TypeVar("T", bound="UpdateSAMLConnectionJsonBody")


@attr.s(auto_attribs=True)
class UpdateSAMLConnectionJsonBody:
    """
    Attributes:
        name (Union[Unset, None, str]): The name of the new SAML Connection
        domain (Union[Unset, None, str]): The domain to use for the new SAML Connection
        idp_entity_id (Union[Unset, None, str]): The entity id as provided by the IdP
        idp_sso_url (Union[Unset, None, str]): The SSO url as provided by the IdP
        idp_certificate (Union[Unset, None, str]): The x509 certificated as provided by the IdP
        active (Union[Unset, None, bool]): Activate or de-activate the SAML Connection
        sync_user_attributes (Union[Unset, None, bool]): Controls whether to update the user's attributes in each sign-
            in
    """

    name: Union[Unset, None, str] = UNSET
    domain: Union[Unset, None, str] = UNSET
    idp_entity_id: Union[Unset, None, str] = UNSET
    idp_sso_url: Union[Unset, None, str] = UNSET
    idp_certificate: Union[Unset, None, str] = UNSET
    active: Union[Unset, None, bool] = UNSET
    sync_user_attributes: Union[Unset, None, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        domain = self.domain
        idp_entity_id = self.idp_entity_id
        idp_sso_url = self.idp_sso_url
        idp_certificate = self.idp_certificate
        active = self.active
        sync_user_attributes = self.sync_user_attributes

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if domain is not UNSET:
            field_dict["domain"] = domain
        if idp_entity_id is not UNSET:
            field_dict["idp_entity_id"] = idp_entity_id
        if idp_sso_url is not UNSET:
            field_dict["idp_sso_url"] = idp_sso_url
        if idp_certificate is not UNSET:
            field_dict["idp_certificate"] = idp_certificate
        if active is not UNSET:
            field_dict["active"] = active
        if sync_user_attributes is not UNSET:
            field_dict["sync_user_attributes"] = sync_user_attributes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        domain = d.pop("domain", UNSET)

        idp_entity_id = d.pop("idp_entity_id", UNSET)

        idp_sso_url = d.pop("idp_sso_url", UNSET)

        idp_certificate = d.pop("idp_certificate", UNSET)

        active = d.pop("active", UNSET)

        sync_user_attributes = d.pop("sync_user_attributes", UNSET)

        update_saml_connection_json_body = cls(
            name=name,
            domain=domain,
            idp_entity_id=idp_entity_id,
            idp_sso_url=idp_sso_url,
            idp_certificate=idp_certificate,
            active=active,
            sync_user_attributes=sync_user_attributes,
        )

        return update_saml_connection_json_body
