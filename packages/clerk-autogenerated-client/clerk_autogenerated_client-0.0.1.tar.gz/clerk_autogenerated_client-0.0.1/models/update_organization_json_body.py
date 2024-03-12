from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..livtypes import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_organization_json_body_private_metadata import UpdateOrganizationJsonBodyPrivateMetadata
    from ..models.update_organization_json_body_public_metadata import UpdateOrganizationJsonBodyPublicMetadata


T = TypeVar("T", bound="UpdateOrganizationJsonBody")


@attr.s(auto_attribs=True)
class UpdateOrganizationJsonBody:
    """
    Attributes:
        public_metadata (Union[Unset, UpdateOrganizationJsonBodyPublicMetadata]): Metadata saved on the organization,
            that is visible to both your frontend and backend.
        private_metadata (Union[Unset, UpdateOrganizationJsonBodyPrivateMetadata]): Metadata saved on the organization
            that is only visible to your backend.
        name (Union[Unset, None, str]): The new name of the organization
        slug (Union[Unset, None, str]): The new slug of the organization, which needs to be unique in the instance
        max_allowed_memberships (Union[Unset, None, int]): The maximum number of memberships allowed for this
            organization
        admin_delete_enabled (Union[Unset, None, bool]): If true, an admin can delete this organization with the
            Frontend API.
    """

    public_metadata: Union[Unset, "UpdateOrganizationJsonBodyPublicMetadata"] = UNSET
    private_metadata: Union[Unset, "UpdateOrganizationJsonBodyPrivateMetadata"] = UNSET
    name: Union[Unset, None, str] = UNSET
    slug: Union[Unset, None, str] = UNSET
    max_allowed_memberships: Union[Unset, None, int] = UNSET
    admin_delete_enabled: Union[Unset, None, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        public_metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.public_metadata, Unset):
            public_metadata = self.public_metadata.to_dict()

        private_metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.private_metadata, Unset):
            private_metadata = self.private_metadata.to_dict()

        name = self.name
        slug = self.slug
        max_allowed_memberships = self.max_allowed_memberships
        admin_delete_enabled = self.admin_delete_enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if public_metadata is not UNSET:
            field_dict["public_metadata"] = public_metadata
        if private_metadata is not UNSET:
            field_dict["private_metadata"] = private_metadata
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if max_allowed_memberships is not UNSET:
            field_dict["max_allowed_memberships"] = max_allowed_memberships
        if admin_delete_enabled is not UNSET:
            field_dict["admin_delete_enabled"] = admin_delete_enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.update_organization_json_body_private_metadata import UpdateOrganizationJsonBodyPrivateMetadata
        from ..models.update_organization_json_body_public_metadata import UpdateOrganizationJsonBodyPublicMetadata

        d = src_dict.copy()
        _public_metadata = d.pop("public_metadata", UNSET)
        public_metadata: Union[Unset, UpdateOrganizationJsonBodyPublicMetadata]
        if isinstance(_public_metadata, Unset):
            public_metadata = UNSET
        else:
            public_metadata = UpdateOrganizationJsonBodyPublicMetadata.from_dict(_public_metadata)

        _private_metadata = d.pop("private_metadata", UNSET)
        private_metadata: Union[Unset, UpdateOrganizationJsonBodyPrivateMetadata]
        if isinstance(_private_metadata, Unset):
            private_metadata = UNSET
        else:
            private_metadata = UpdateOrganizationJsonBodyPrivateMetadata.from_dict(_private_metadata)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        max_allowed_memberships = d.pop("max_allowed_memberships", UNSET)

        admin_delete_enabled = d.pop("admin_delete_enabled", UNSET)

        update_organization_json_body = cls(
            public_metadata=public_metadata,
            private_metadata=private_metadata,
            name=name,
            slug=slug,
            max_allowed_memberships=max_allowed_memberships,
            admin_delete_enabled=admin_delete_enabled,
        )

        return update_organization_json_body
