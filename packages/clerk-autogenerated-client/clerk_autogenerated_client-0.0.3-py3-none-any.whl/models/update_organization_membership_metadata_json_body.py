from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..livtypes import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_organization_membership_metadata_json_body_private_metadata import (
        UpdateOrganizationMembershipMetadataJsonBodyPrivateMetadata,
    )
    from ..models.update_organization_membership_metadata_json_body_public_metadata import UpdateOrganizationMembershipMetadataJsonBodyPublicMetadata


T = TypeVar("T", bound="UpdateOrganizationMembershipMetadataJsonBody")


@attr.s(auto_attribs=True)
class UpdateOrganizationMembershipMetadataJsonBody:
    """
    Attributes:
        public_metadata (Union[Unset, UpdateOrganizationMembershipMetadataJsonBodyPublicMetadata]): Metadata saved on
            the organization membership, that is visible to both your frontend and backend.
            The new object will be merged with the existing value.
        private_metadata (Union[Unset, UpdateOrganizationMembershipMetadataJsonBodyPrivateMetadata]): Metadata saved on
            the organization membership that is only visible to your backend.
            The new object will be merged with the existing value.
    """

    public_metadata: Union[Unset, "UpdateOrganizationMembershipMetadataJsonBodyPublicMetadata"] = UNSET
    private_metadata: Union[Unset, "UpdateOrganizationMembershipMetadataJsonBodyPrivateMetadata"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        public_metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.public_metadata, Unset):
            public_metadata = self.public_metadata.to_dict()

        private_metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.private_metadata, Unset):
            private_metadata = self.private_metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if public_metadata is not UNSET:
            field_dict["public_metadata"] = public_metadata
        if private_metadata is not UNSET:
            field_dict["private_metadata"] = private_metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.update_organization_membership_metadata_json_body_private_metadata import (
            UpdateOrganizationMembershipMetadataJsonBodyPrivateMetadata,
        )
        from ..models.update_organization_membership_metadata_json_body_public_metadata import (
            UpdateOrganizationMembershipMetadataJsonBodyPublicMetadata,
        )

        d = src_dict.copy()
        _public_metadata = d.pop("public_metadata", UNSET)
        public_metadata: Union[Unset, UpdateOrganizationMembershipMetadataJsonBodyPublicMetadata]
        if isinstance(_public_metadata, Unset):
            public_metadata = UNSET
        else:
            public_metadata = UpdateOrganizationMembershipMetadataJsonBodyPublicMetadata.from_dict(_public_metadata)

        _private_metadata = d.pop("private_metadata", UNSET)
        private_metadata: Union[Unset, UpdateOrganizationMembershipMetadataJsonBodyPrivateMetadata]
        if isinstance(_private_metadata, Unset):
            private_metadata = UNSET
        else:
            private_metadata = UpdateOrganizationMembershipMetadataJsonBodyPrivateMetadata.from_dict(_private_metadata)

        update_organization_membership_metadata_json_body = cls(
            public_metadata=public_metadata,
            private_metadata=private_metadata,
        )

        return update_organization_membership_metadata_json_body
