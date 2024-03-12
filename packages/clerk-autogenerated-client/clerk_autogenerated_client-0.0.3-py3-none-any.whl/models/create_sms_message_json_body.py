from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..livtypes import UNSET, Unset

T = TypeVar("T", bound="CreateSMSMessageJsonBody")


@attr.s(auto_attribs=True)
class CreateSMSMessageJsonBody:
    """
    Attributes:
        message (Union[Unset, None, str]): The message you would like to send
        phone_number_id (Union[Unset, str]): The ID of a verified phone number the SMS message should be sent to
    """

    message: Union[Unset, None, str] = UNSET
    phone_number_id: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        message = self.message
        phone_number_id = self.phone_number_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if phone_number_id is not UNSET:
            field_dict["phone_number_id"] = phone_number_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        message = d.pop("message", UNSET)

        phone_number_id = d.pop("phone_number_id", UNSET)

        create_sms_message_json_body = cls(
            message=message,
            phone_number_id=phone_number_id,
        )

        return create_sms_message_json_body
