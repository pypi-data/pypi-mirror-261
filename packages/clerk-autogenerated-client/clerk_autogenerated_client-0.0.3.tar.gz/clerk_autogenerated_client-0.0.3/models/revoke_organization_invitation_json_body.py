from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="RevokeOrganizationInvitationJsonBody")


@attr.s(auto_attribs=True)
class RevokeOrganizationInvitationJsonBody:
    """
    Attributes:
        requesting_user_id (str): The ID of the user that revokes the invitation.
            Must be an administrator in the organization.
    """

    requesting_user_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        requesting_user_id = self.requesting_user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requesting_user_id": requesting_user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        requesting_user_id = d.pop("requesting_user_id")

        revoke_organization_invitation_json_body = cls(
            requesting_user_id=requesting_user_id,
        )

        revoke_organization_invitation_json_body.additional_properties = d
        return revoke_organization_invitation_json_body

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
