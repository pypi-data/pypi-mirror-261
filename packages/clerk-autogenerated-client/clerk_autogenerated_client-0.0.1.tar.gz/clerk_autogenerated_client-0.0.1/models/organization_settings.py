from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.organization_settings_object import OrganizationSettingsObject
from ..livtypes import UNSET, Unset

T = TypeVar("T", bound="OrganizationSettings")


@attr.s(auto_attribs=True)
class OrganizationSettings:
    """
    Attributes:
        object_ (OrganizationSettingsObject): String representing the object's type. Objects of the same type share the
            same value.
        enabled (bool):
        max_allowed_memberships (int):
        admin_delete_enabled (Union[Unset, bool]): The default for whether an admin can delete an organization with the
            Frontend API.
    """

    object_: OrganizationSettingsObject
    enabled: bool
    max_allowed_memberships: int
    admin_delete_enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_.value

        enabled = self.enabled
        max_allowed_memberships = self.max_allowed_memberships
        admin_delete_enabled = self.admin_delete_enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "enabled": enabled,
                "max_allowed_memberships": max_allowed_memberships,
            }
        )
        if admin_delete_enabled is not UNSET:
            field_dict["admin_delete_enabled"] = admin_delete_enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        object_ = OrganizationSettingsObject(d.pop("object"))

        enabled = d.pop("enabled")

        max_allowed_memberships = d.pop("max_allowed_memberships")

        admin_delete_enabled = d.pop("admin_delete_enabled", UNSET)

        organization_settings = cls(
            object_=object_,
            enabled=enabled,
            max_allowed_memberships=max_allowed_memberships,
            admin_delete_enabled=admin_delete_enabled,
        )

        organization_settings.additional_properties = d
        return organization_settings

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
