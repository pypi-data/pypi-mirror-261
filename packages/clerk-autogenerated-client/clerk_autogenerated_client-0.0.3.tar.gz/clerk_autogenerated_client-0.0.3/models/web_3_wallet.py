from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..models.web_3_wallet_object import Web3WalletObject
from ..livtypes import UNSET, Unset

if TYPE_CHECKING:
    from ..models.admin import Admin
    from ..models.web_3_signature import Web3Signature


T = TypeVar("T", bound="Web3Wallet")


@attr.s(auto_attribs=True)
class Web3Wallet:
    """
    Attributes:
        object_ (Web3WalletObject): String representing the object's type. Objects of the same type share the same
            value.
        web3_wallet (str):
        id (Union[Unset, str]):
        verification (Union['Admin', 'Web3Signature', None]):
    """

    object_: Web3WalletObject
    web3_wallet: str
    verification: Union["Admin", "Web3Signature", None]
    id: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.web_3_signature import Web3Signature

        object_ = self.object_.value

        web3_wallet = self.web3_wallet
        id = self.id
        verification: Union[Dict[str, Any], None]
        if self.verification is None:
            verification = None

        elif isinstance(self.verification, Web3Signature):
            verification = self.verification.to_dict()

        else:
            verification = self.verification.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "object": object_,
                "web3_wallet": web3_wallet,
                "verification": verification,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.admin import Admin
        from ..models.web_3_signature import Web3Signature

        d = src_dict.copy()
        object_ = Web3WalletObject(d.pop("object"))

        web3_wallet = d.pop("web3_wallet")

        id = d.pop("id", UNSET)

        def _parse_verification(data: object) -> Union["Admin", "Web3Signature", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verification_type_0 = Web3Signature.from_dict(data)

                return verification_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            verification_type_1 = Admin.from_dict(data)

            return verification_type_1

        verification = _parse_verification(d.pop("verification"))

        web_3_wallet = cls(
            object_=object_,
            web3_wallet=web3_wallet,
            id=id,
            verification=verification,
        )

        return web_3_wallet
