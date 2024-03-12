from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.create_organization_membership_json_body_role import CreateOrganizationMembershipJsonBodyRole

T = TypeVar("T", bound="CreateOrganizationMembershipJsonBody")


@attr.s(auto_attribs=True)
class CreateOrganizationMembershipJsonBody:
    """
    Attributes:
        user_id (str): The ID of the user that will be added as a member in the organization.
            The user needs to exist in the same instance as the organization and must not be a member of the given
            organization already.
        role (CreateOrganizationMembershipJsonBodyRole): The role that the new member will have in the organization.
    """

    user_id: str
    role: CreateOrganizationMembershipJsonBodyRole
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id
        role = self.role.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_id": user_id,
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("user_id")

        role = CreateOrganizationMembershipJsonBodyRole(d.pop("role"))

        create_organization_membership_json_body = cls(
            user_id=user_id,
            role=role,
        )

        create_organization_membership_json_body.additional_properties = d
        return create_organization_membership_json_body

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
