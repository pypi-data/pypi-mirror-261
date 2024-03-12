from typing import TYPE_CHECKING, Any, Dict, Optional, Type, TypeVar, Union

import attr

from ..models.saml_status import SAMLStatus
from ..models.saml_strategy import SAMLStrategy
from ..livtypes import UNSET, Unset

if TYPE_CHECKING:
    from ..models.clerk_error import ClerkError


T = TypeVar("T", bound="SAML")


@attr.s(auto_attribs=True)
class SAML:
    """
    Attributes:
        status (SAMLStatus):
        strategy (SAMLStrategy):
        expire_at (int):
        external_verification_redirect_url (Optional[str]):
        error (Union[Unset, None, ClerkError]):
        attempts (Union[Unset, None, int]):
    """

    status: SAMLStatus
    strategy: SAMLStrategy
    expire_at: int
    external_verification_redirect_url: Optional[str]
    error: Union[Unset, None, "ClerkError"] = UNSET
    attempts: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        strategy = self.strategy.value

        expire_at = self.expire_at
        external_verification_redirect_url = self.external_verification_redirect_url
        error: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict() if self.error else None

        attempts = self.attempts

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "status": status,
                "strategy": strategy,
                "expire_at": expire_at,
                "external_verification_redirect_url": external_verification_redirect_url,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if attempts is not UNSET:
            field_dict["attempts"] = attempts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.clerk_error import ClerkError

        d = src_dict.copy()
        status = SAMLStatus(d.pop("status"))

        strategy = SAMLStrategy(d.pop("strategy"))

        expire_at = d.pop("expire_at")

        external_verification_redirect_url = d.pop("external_verification_redirect_url")

        _error = d.pop("error", UNSET)
        error: Union[Unset, None, ClerkError]
        if _error is None:
            error = None
        elif isinstance(_error, Unset):
            error = UNSET
        else:
            error = ClerkError.from_dict(_error)

        attempts = d.pop("attempts", UNSET)

        saml = cls(
            status=status,
            strategy=strategy,
            expire_at=expire_at,
            external_verification_redirect_url=external_verification_redirect_url,
            error=error,
            attempts=attempts,
        )

        return saml
