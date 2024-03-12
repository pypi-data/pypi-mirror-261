from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..livtypes import UNSET, Unset

T = TypeVar("T", bound="UpdateInstanceOrganizationSettingsJsonBody")


@attr.s(auto_attribs=True)
class UpdateInstanceOrganizationSettingsJsonBody:
    """
    Attributes:
        enabled (Union[Unset, None, bool]):
        max_allowed_memberships (Union[Unset, None, int]):
        admin_delete_enabled (Union[Unset, None, bool]):
    """

    enabled: Union[Unset, None, bool] = UNSET
    max_allowed_memberships: Union[Unset, None, int] = UNSET
    admin_delete_enabled: Union[Unset, None, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        max_allowed_memberships = self.max_allowed_memberships
        admin_delete_enabled = self.admin_delete_enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if max_allowed_memberships is not UNSET:
            field_dict["max_allowed_memberships"] = max_allowed_memberships
        if admin_delete_enabled is not UNSET:
            field_dict["admin_delete_enabled"] = admin_delete_enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        max_allowed_memberships = d.pop("max_allowed_memberships", UNSET)

        admin_delete_enabled = d.pop("admin_delete_enabled", UNSET)

        update_instance_organization_settings_json_body = cls(
            enabled=enabled,
            max_allowed_memberships=max_allowed_memberships,
            admin_delete_enabled=admin_delete_enabled,
        )

        return update_instance_organization_settings_json_body
