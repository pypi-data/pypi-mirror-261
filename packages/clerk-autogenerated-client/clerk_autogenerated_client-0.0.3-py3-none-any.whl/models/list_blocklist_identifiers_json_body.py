from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="ListBlocklistIdentifiersJsonBody")


@attr.s(auto_attribs=True)
class ListBlocklistIdentifiersJsonBody:
    """
    Attributes:
        identifier (str): The identifier to be added in the block-list.
            This can be an email address, a phone number or a web3 wallet.
    """

    identifier: str

    def to_dict(self) -> Dict[str, Any]:
        identifier = self.identifier

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "identifier": identifier,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        identifier = d.pop("identifier")

        list_blocklist_identifiers_json_body = cls(
            identifier=identifier,
        )

        return list_blocklist_identifiers_json_body
