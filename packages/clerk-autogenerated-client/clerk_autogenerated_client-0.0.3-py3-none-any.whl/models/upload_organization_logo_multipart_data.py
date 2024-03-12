from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar

import attr

from ..livtypes import File, Unset

T = TypeVar("T", bound="UploadOrganizationLogoMultipartData")


@attr.s(auto_attribs=True)
class UploadOrganizationLogoMultipartData:
    """
    Attributes:
        uploader_user_id (str): Should be the ID of a member with an "admin" role in the organization.
        file (File):
    """

    uploader_user_id: str
    file: File
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uploader_user_id = self.uploader_user_id
        file = self.file.to_tuple()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uploader_user_id": uploader_user_id,
                "file": file,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        uploader_user_id = (
            self.uploader_user_id if isinstance(self.uploader_user_id, Unset) else (None, str(self.uploader_user_id).encode(), "text/plain")
        )
        file = self.file.to_tuple()

        field_dict: Dict[str, Any] = {}
        field_dict.update({key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()})
        field_dict.update(
            {
                "uploader_user_id": uploader_user_id,
                "file": file,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uploader_user_id = d.pop("uploader_user_id")

        file = File(payload=BytesIO(d.pop("file")))

        upload_organization_logo_multipart_data = cls(
            uploader_user_id=uploader_user_id,
            file=file,
        )

        upload_organization_logo_multipart_data.additional_properties = d
        return upload_organization_logo_multipart_data

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
