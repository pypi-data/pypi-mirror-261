from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="UpdateOAuthApplicationJsonBody")


@attr.s(auto_attribs=True)
class UpdateOAuthApplicationJsonBody:
    """
    Attributes:
        name (str): The new name of the OAuth application
        callback_url (str): The new callback URL of the OAuth application
    """

    name: str
    callback_url: str

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        callback_url = self.callback_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "callback_url": callback_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        callback_url = d.pop("callback_url")

        update_o_auth_application_json_body = cls(
            name=name,
            callback_url=callback_url,
        )

        return update_o_auth_application_json_body
