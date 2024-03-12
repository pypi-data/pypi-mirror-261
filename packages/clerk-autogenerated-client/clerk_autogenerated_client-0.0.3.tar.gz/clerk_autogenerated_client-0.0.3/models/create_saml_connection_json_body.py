from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..livtypes import UNSET, Unset

T = TypeVar("T", bound="CreateSAMLConnectionJsonBody")


@attr.s(auto_attribs=True)
class CreateSAMLConnectionJsonBody:
    """
    Attributes:
        name (str): The name to use as a label for this SAML Connection
        domain (str): The domain of your organization. Sign in flows using an email with this domain, will use this SAML
            Connection.
        idp_entity_id (Union[Unset, None, str]): The Entity ID as provided by the IdP
        idp_sso_url (Union[Unset, None, str]): The Single-Sign On URL as provided by the IdP
        idp_certificate (Union[Unset, None, str]): The X.509 certificate as provided by the IdP
    """

    name: str
    domain: str
    idp_entity_id: Union[Unset, None, str] = UNSET
    idp_sso_url: Union[Unset, None, str] = UNSET
    idp_certificate: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        domain = self.domain
        idp_entity_id = self.idp_entity_id
        idp_sso_url = self.idp_sso_url
        idp_certificate = self.idp_certificate

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "domain": domain,
            }
        )
        if idp_entity_id is not UNSET:
            field_dict["idp_entity_id"] = idp_entity_id
        if idp_sso_url is not UNSET:
            field_dict["idp_sso_url"] = idp_sso_url
        if idp_certificate is not UNSET:
            field_dict["idp_certificate"] = idp_certificate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        domain = d.pop("domain")

        idp_entity_id = d.pop("idp_entity_id", UNSET)

        idp_sso_url = d.pop("idp_sso_url", UNSET)

        idp_certificate = d.pop("idp_certificate", UNSET)

        create_saml_connection_json_body = cls(
            name=name,
            domain=domain,
            idp_entity_id=idp_entity_id,
            idp_sso_url=idp_sso_url,
            idp_certificate=idp_certificate,
        )

        return create_saml_connection_json_body
