from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.domain_object import DomainObject
from ..livtypes import UNSET, Unset

if TYPE_CHECKING:
    from ..models.c_name_target import CNameTarget


T = TypeVar("T", bound="Domain")


@attr.s(auto_attribs=True)
class Domain:
    """
    Attributes:
        object_ (DomainObject):
        id (str):
        name (str):
        is_satellite (bool):
        frontend_api_url (str):
        development_origin (str):
        accounts_portal_url (Union[Unset, None, str]): Null for satellite domains.
        proxy_url (Union[Unset, None, str]):
        cname_targets (Union[Unset, None, List['CNameTarget']]):
    """

    object_: DomainObject
    id: str
    name: str
    is_satellite: bool
    frontend_api_url: str
    development_origin: str
    accounts_portal_url: Union[Unset, None, str] = UNSET
    proxy_url: Union[Unset, None, str] = UNSET
    cname_targets: Union[Unset, None, List["CNameTarget"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_.value

        id = self.id
        name = self.name
        is_satellite = self.is_satellite
        frontend_api_url = self.frontend_api_url
        development_origin = self.development_origin
        accounts_portal_url = self.accounts_portal_url
        proxy_url = self.proxy_url
        cname_targets: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.cname_targets, Unset):
            if self.cname_targets is None:
                cname_targets = None
            else:
                cname_targets = []
                for cname_targets_item_data in self.cname_targets:
                    cname_targets_item = cname_targets_item_data.to_dict()

                    cname_targets.append(cname_targets_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "id": id,
                "name": name,
                "is_satellite": is_satellite,
                "frontend_api_url": frontend_api_url,
                "development_origin": development_origin,
            }
        )
        if accounts_portal_url is not UNSET:
            field_dict["accounts_portal_url"] = accounts_portal_url
        if proxy_url is not UNSET:
            field_dict["proxy_url"] = proxy_url
        if cname_targets is not UNSET:
            field_dict["cname_targets"] = cname_targets

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.c_name_target import CNameTarget

        d = src_dict.copy()
        object_ = DomainObject(d.pop("object"))

        id = d.pop("id")

        name = d.pop("name")

        is_satellite = d.pop("is_satellite")

        frontend_api_url = d.pop("frontend_api_url")

        development_origin = d.pop("development_origin")

        accounts_portal_url = d.pop("accounts_portal_url", UNSET)

        proxy_url = d.pop("proxy_url", UNSET)

        cname_targets = []
        _cname_targets = d.pop("cname_targets", UNSET)
        for cname_targets_item_data in _cname_targets or []:
            cname_targets_item = CNameTarget.from_dict(cname_targets_item_data)

            cname_targets.append(cname_targets_item)

        domain = cls(
            object_=object_,
            id=id,
            name=name,
            is_satellite=is_satellite,
            frontend_api_url=frontend_api_url,
            development_origin=development_origin,
            accounts_portal_url=accounts_portal_url,
            proxy_url=proxy_url,
            cname_targets=cname_targets,
        )

        domain.additional_properties = d
        return domain

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
