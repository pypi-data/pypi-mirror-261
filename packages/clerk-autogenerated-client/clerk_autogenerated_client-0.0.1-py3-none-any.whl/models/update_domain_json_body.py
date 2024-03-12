from typing import Any, Dict, Optional, Type, TypeVar

import attr

T = TypeVar("T", bound="UpdateDomainJsonBody")


@attr.s(auto_attribs=True)
class UpdateDomainJsonBody:
    """
    Attributes:
        proxy_url (Optional[str]): The full URL of the proxy that will forward requests to Clerk's Frontend API.
    """

    proxy_url: Optional[str]

    def to_dict(self) -> Dict[str, Any]:
        proxy_url = self.proxy_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "proxy_url": proxy_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        proxy_url = d.pop("proxy_url")

        update_domain_json_body = cls(
            proxy_url=proxy_url,
        )

        return update_domain_json_body
