from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..livtypes import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_organization_json_body_private_metadata import CreateOrganizationJsonBodyPrivateMetadata
    from ..models.create_organization_json_body_public_metadata import CreateOrganizationJsonBodyPublicMetadata


T = TypeVar("T", bound="CreateOrganizationJsonBody")


@attr.s(auto_attribs=True)
class CreateOrganizationJsonBody:
    """
    Attributes:
        name (str): The name of the new organization
        created_by (str): The ID of the User who will become the administrator for the new organization
        private_metadata (Union[Unset, CreateOrganizationJsonBodyPrivateMetadata]): Metadata saved on the organization,
            accessible only from the Backend API
        public_metadata (Union[Unset, CreateOrganizationJsonBodyPublicMetadata]): Metadata saved on the organization,
            read-only from the Frontend API and fully accessible (read/write) from the Backend API
        slug (Union[Unset, str]): A slug for the new organization.
            Can contain only lowercase alphanumeric characters and the dash "-".
            Must be unique for the instance.
        max_allowed_memberships (Union[Unset, int]): The maximum number of memberships allowed for this organization
    """

    name: str
    created_by: str
    private_metadata: Union[Unset, "CreateOrganizationJsonBodyPrivateMetadata"] = UNSET
    public_metadata: Union[Unset, "CreateOrganizationJsonBodyPublicMetadata"] = UNSET
    slug: Union[Unset, str] = UNSET
    max_allowed_memberships: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        created_by = self.created_by
        private_metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.private_metadata, Unset):
            private_metadata = self.private_metadata.to_dict()

        public_metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.public_metadata, Unset):
            public_metadata = self.public_metadata.to_dict()

        slug = self.slug
        max_allowed_memberships = self.max_allowed_memberships

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "created_by": created_by,
            }
        )
        if private_metadata is not UNSET:
            field_dict["private_metadata"] = private_metadata
        if public_metadata is not UNSET:
            field_dict["public_metadata"] = public_metadata
        if slug is not UNSET:
            field_dict["slug"] = slug
        if max_allowed_memberships is not UNSET:
            field_dict["max_allowed_memberships"] = max_allowed_memberships

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_organization_json_body_private_metadata import CreateOrganizationJsonBodyPrivateMetadata
        from ..models.create_organization_json_body_public_metadata import CreateOrganizationJsonBodyPublicMetadata

        d = src_dict.copy()
        name = d.pop("name")

        created_by = d.pop("created_by")

        _private_metadata = d.pop("private_metadata", UNSET)
        private_metadata: Union[Unset, CreateOrganizationJsonBodyPrivateMetadata]
        if isinstance(_private_metadata, Unset):
            private_metadata = UNSET
        else:
            private_metadata = CreateOrganizationJsonBodyPrivateMetadata.from_dict(_private_metadata)

        _public_metadata = d.pop("public_metadata", UNSET)
        public_metadata: Union[Unset, CreateOrganizationJsonBodyPublicMetadata]
        if isinstance(_public_metadata, Unset):
            public_metadata = UNSET
        else:
            public_metadata = CreateOrganizationJsonBodyPublicMetadata.from_dict(_public_metadata)

        slug = d.pop("slug", UNSET)

        max_allowed_memberships = d.pop("max_allowed_memberships", UNSET)

        create_organization_json_body = cls(
            name=name,
            created_by=created_by,
            private_metadata=private_metadata,
            public_metadata=public_metadata,
            slug=slug,
            max_allowed_memberships=max_allowed_memberships,
        )

        create_organization_json_body.additional_properties = d
        return create_organization_json_body

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
