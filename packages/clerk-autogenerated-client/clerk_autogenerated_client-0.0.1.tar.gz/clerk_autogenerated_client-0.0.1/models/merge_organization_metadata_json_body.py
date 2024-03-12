from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..livtypes import UNSET, Unset

if TYPE_CHECKING:
    from ..models.merge_organization_metadata_json_body_private_metadata import MergeOrganizationMetadataJsonBodyPrivateMetadata
    from ..models.merge_organization_metadata_json_body_public_metadata import MergeOrganizationMetadataJsonBodyPublicMetadata


T = TypeVar("T", bound="MergeOrganizationMetadataJsonBody")


@attr.s(auto_attribs=True)
class MergeOrganizationMetadataJsonBody:
    """
    Attributes:
        public_metadata (Union[Unset, MergeOrganizationMetadataJsonBodyPublicMetadata]): Metadata saved on the
            organization, that is visible to both your frontend and backend.
            The new object will be merged with the existing value.
        private_metadata (Union[Unset, MergeOrganizationMetadataJsonBodyPrivateMetadata]): Metadata saved on the
            organization that is only visible to your backend.
            The new object will be merged with the existing value.
    """

    public_metadata: Union[Unset, "MergeOrganizationMetadataJsonBodyPublicMetadata"] = UNSET
    private_metadata: Union[Unset, "MergeOrganizationMetadataJsonBodyPrivateMetadata"] = UNSET

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
        from ..models.merge_organization_metadata_json_body_private_metadata import MergeOrganizationMetadataJsonBodyPrivateMetadata
        from ..models.merge_organization_metadata_json_body_public_metadata import MergeOrganizationMetadataJsonBodyPublicMetadata

        d = src_dict.copy()
        _public_metadata = d.pop("public_metadata", UNSET)
        public_metadata: Union[Unset, MergeOrganizationMetadataJsonBodyPublicMetadata]
        if isinstance(_public_metadata, Unset):
            public_metadata = UNSET
        else:
            public_metadata = MergeOrganizationMetadataJsonBodyPublicMetadata.from_dict(_public_metadata)

        _private_metadata = d.pop("private_metadata", UNSET)
        private_metadata: Union[Unset, MergeOrganizationMetadataJsonBodyPrivateMetadata]
        if isinstance(_private_metadata, Unset):
            private_metadata = UNSET
        else:
            private_metadata = MergeOrganizationMetadataJsonBodyPrivateMetadata.from_dict(_private_metadata)

        merge_organization_metadata_json_body = cls(
            public_metadata=public_metadata,
            private_metadata=private_metadata,
        )

        return merge_organization_metadata_json_body
