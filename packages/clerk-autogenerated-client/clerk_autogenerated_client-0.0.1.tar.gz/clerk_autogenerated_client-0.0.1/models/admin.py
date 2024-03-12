from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.admin_status import AdminStatus
from ..models.admin_strategy import AdminStrategy
from ..livtypes import UNSET, Unset

T = TypeVar("T", bound="Admin")


@attr.s(auto_attribs=True)
class Admin:
    """
    Attributes:
        status (AdminStatus):
        strategy (AdminStrategy):
        attempts (Union[Unset, None, int]):
        expire_at (Union[Unset, None, int]):
    """

    status: AdminStatus
    strategy: AdminStrategy
    attempts: Union[Unset, None, int] = UNSET
    expire_at: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        strategy = self.strategy.value

        attempts = self.attempts
        expire_at = self.expire_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "status": status,
                "strategy": strategy,
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
        status = AdminStatus(d.pop("status"))

        strategy = AdminStrategy(d.pop("strategy"))

        attempts = d.pop("attempts", UNSET)

        expire_at = d.pop("expire_at", UNSET)

        admin = cls(
            status=status,
            strategy=strategy,
            attempts=attempts,
            expire_at=expire_at,
        )

        return admin
