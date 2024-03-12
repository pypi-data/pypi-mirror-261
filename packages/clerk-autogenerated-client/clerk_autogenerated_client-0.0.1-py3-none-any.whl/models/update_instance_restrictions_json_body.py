from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..livtypes import UNSET, Unset

T = TypeVar("T", bound="UpdateInstanceRestrictionsJsonBody")


@attr.s(auto_attribs=True)
class UpdateInstanceRestrictionsJsonBody:
    """
    Attributes:
        allowlist (Union[Unset, None, bool]):
        blocklist (Union[Unset, None, bool]):
    """

    allowlist: Union[Unset, None, bool] = UNSET
    blocklist: Union[Unset, None, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        allowlist = self.allowlist
        blocklist = self.blocklist

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if allowlist is not UNSET:
            field_dict["allowlist"] = allowlist
        if blocklist is not UNSET:
            field_dict["blocklist"] = blocklist

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        allowlist = d.pop("allowlist", UNSET)

        blocklist = d.pop("blocklist", UNSET)

        update_instance_restrictions_json_body = cls(
            allowlist=allowlist,
            blocklist=blocklist,
        )

        return update_instance_restrictions_json_body
