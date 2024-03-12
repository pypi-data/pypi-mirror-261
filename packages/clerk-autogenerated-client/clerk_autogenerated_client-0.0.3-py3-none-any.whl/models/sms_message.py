from typing import TYPE_CHECKING, Any, Dict, Optional, Type, TypeVar, Union

import attr

from ..models.sms_message_object import SMSMessageObject
from ..livtypes import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sms_message_data import SMSMessageData


T = TypeVar("T", bound="SMSMessage")


@attr.s(auto_attribs=True)
class SMSMessage:
    """
    Attributes:
        object_ (SMSMessageObject):
        id (str):
        from_phone_number (str):
        to_phone_number (str):
        message (str):
        status (str):
        delivered_by_clerk (bool):
        slug (Union[Unset, None, str]):
        phone_number_id (Optional[str]):
        user_id (Union[Unset, None, str]):
        data (Union[Unset, None, SMSMessageData]):
    """

    object_: SMSMessageObject
    id: str
    from_phone_number: str
    to_phone_number: str
    message: str
    status: str
    delivered_by_clerk: bool
    phone_number_id: Optional[str]
    slug: Union[Unset, None, str] = UNSET
    user_id: Union[Unset, None, str] = UNSET
    data: Union[Unset, None, "SMSMessageData"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_.value

        id = self.id
        from_phone_number = self.from_phone_number
        to_phone_number = self.to_phone_number
        message = self.message
        status = self.status
        delivered_by_clerk = self.delivered_by_clerk
        slug = self.slug
        phone_number_id = self.phone_number_id
        user_id = self.user_id
        data: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict() if self.data else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "object": object_,
                "id": id,
                "from_phone_number": from_phone_number,
                "to_phone_number": to_phone_number,
                "message": message,
                "status": status,
                "delivered_by_clerk": delivered_by_clerk,
                "phone_number_id": phone_number_id,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sms_message_data import SMSMessageData

        d = src_dict.copy()
        object_ = SMSMessageObject(d.pop("object"))

        id = d.pop("id")

        from_phone_number = d.pop("from_phone_number")

        to_phone_number = d.pop("to_phone_number")

        message = d.pop("message")

        status = d.pop("status")

        delivered_by_clerk = d.pop("delivered_by_clerk")

        slug = d.pop("slug", UNSET)

        phone_number_id = d.pop("phone_number_id")

        user_id = d.pop("user_id", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, None, SMSMessageData]
        if _data is None:
            data = None
        elif isinstance(_data, Unset):
            data = UNSET
        else:
            data = SMSMessageData.from_dict(_data)

        sms_message = cls(
            object_=object_,
            id=id,
            from_phone_number=from_phone_number,
            to_phone_number=to_phone_number,
            message=message,
            status=status,
            delivered_by_clerk=delivered_by_clerk,
            slug=slug,
            phone_number_id=phone_number_id,
            user_id=user_id,
            data=data,
        )

        return sms_message
