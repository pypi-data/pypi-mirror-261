from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.web_3_signature_nonce import Web3SignatureNonce
from ..models.web_3_signature_status import Web3SignatureStatus
from ..models.web_3_signature_strategy import Web3SignatureStrategy
from ..livtypes import UNSET, Unset

T = TypeVar("T", bound="Web3Signature")


@attr.s(auto_attribs=True)
class Web3Signature:
    """
    Attributes:
        status (Web3SignatureStatus):
        strategy (Web3SignatureStrategy):
        nonce (Web3SignatureNonce):
        attempts (Union[Unset, None, int]):
        expire_at (Union[Unset, None, int]):
    """

    status: Web3SignatureStatus
    strategy: Web3SignatureStrategy
    nonce: Web3SignatureNonce
    attempts: Union[Unset, None, int] = UNSET
    expire_at: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        strategy = self.strategy.value

        nonce = self.nonce.value

        attempts = self.attempts
        expire_at = self.expire_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "status": status,
                "strategy": strategy,
                "nonce": nonce,
            }
        )
        if attempts is not UNSET:
            field_dict["attempts"] = attempts
        if expire_at is not UNSET:
            field_dict["expire_at"] = expire_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = Web3SignatureStatus(d.pop("status"))

        strategy = Web3SignatureStrategy(d.pop("strategy"))

        nonce = Web3SignatureNonce(d.pop("nonce"))

        attempts = d.pop("attempts", UNSET)

        expire_at = d.pop("expire_at", UNSET)

        web_3_signature = cls(
            status=status,
            strategy=strategy,
            nonce=nonce,
            attempts=attempts,
            expire_at=expire_at,
        )

        return web_3_signature
