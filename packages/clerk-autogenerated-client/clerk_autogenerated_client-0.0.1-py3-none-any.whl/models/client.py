from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, cast

import attr

from ..models.client_object import ClientObject

if TYPE_CHECKING:
    from ..models.session import Session


T = TypeVar("T", bound="Client")


@attr.s(auto_attribs=True)
class Client:
    """
    Attributes:
        object_ (ClientObject): String representing the object's type. Objects of the same type share the same value.
        id (str): String representing the identifier of the session.
        session_ids (List[str]):
        sessions (List['Session']):
        updated_at (int): Unix timestamp of last update.
        created_at (int): Unix timestamp of creation.
        sign_in_id (Optional[str]):
        sign_up_id (Optional[str]):
        last_active_session_id (Optional[str]): Last active session_id.
    """

    object_: ClientObject
    id: str
    session_ids: List[str]
    sessions: List["Session"]
    updated_at: int
    created_at: int
    sign_in_id: Optional[str]
    sign_up_id: Optional[str]
    last_active_session_id: Optional[str]

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_.value

        id = self.id
        session_ids = self.session_ids

        sessions = []
        for sessions_item_data in self.sessions:
            sessions_item = sessions_item_data.to_dict()

            sessions.append(sessions_item)

        updated_at = self.updated_at
        created_at = self.created_at
        sign_in_id = self.sign_in_id
        sign_up_id = self.sign_up_id
        last_active_session_id = self.last_active_session_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "object": object_,
                "id": id,
                "session_ids": session_ids,
                "sessions": sessions,
                "updated_at": updated_at,
                "created_at": created_at,
                "sign_in_id": sign_in_id,
                "sign_up_id": sign_up_id,
                "last_active_session_id": last_active_session_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.session import Session

        d = src_dict.copy()
        object_ = ClientObject(d.pop("object"))

        id = d.pop("id")

        session_ids = cast(List[str], d.pop("session_ids"))

        sessions = []
        _sessions = d.pop("sessions")
        for sessions_item_data in _sessions:
            sessions_item = Session.from_dict(sessions_item_data)

            sessions.append(sessions_item)

        updated_at = d.pop("updated_at")

        created_at = d.pop("created_at")

        sign_in_id = d.pop("sign_in_id")

        sign_up_id = d.pop("sign_up_id")

        last_active_session_id = d.pop("last_active_session_id")

        client = cls(
            object_=object_,
            id=id,
            session_ids=session_ids,
            sessions=sessions,
            updated_at=updated_at,
            created_at=created_at,
            sign_in_id=sign_in_id,
            sign_up_id=sign_up_id,
            last_active_session_id=last_active_session_id,
        )

        return client
