from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="SvixURL")


@attr.s(auto_attribs=True)
class SvixURL:
    """
    Attributes:
        svix_url (str):
    """

    svix_url: str

    def to_dict(self) -> Dict[str, Any]:
        svix_url = self.svix_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "svix_url": svix_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        svix_url = d.pop("svix_url")

        svix_url = cls(
            svix_url=svix_url,
        )

        return svix_url
