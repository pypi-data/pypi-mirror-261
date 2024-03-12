from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..livtypes import UNSET, Unset

T = TypeVar("T", bound="CreateEmailJsonBody")


@attr.s(auto_attribs=True)
class CreateEmailJsonBody:
    """
    Attributes:
        from_email_name (Union[Unset, str]): The email name portion of the sending email address.
            <br/>e.g.: `from_email_name=info` will send from info@example.com
        subject (Union[Unset, str]): The subject of the email.
        body (Union[Unset, str]): The body of the email.
        email_address_id (Union[Unset, None, str]): The ID of the email address to send to.
    """

    from_email_name: Union[Unset, str] = UNSET
    subject: Union[Unset, str] = UNSET
    body: Union[Unset, str] = UNSET
    email_address_id: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from_email_name = self.from_email_name
        subject = self.subject
        body = self.body
        email_address_id = self.email_address_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if from_email_name is not UNSET:
            field_dict["from_email_name"] = from_email_name
        if subject is not UNSET:
            field_dict["subject"] = subject
        if body is not UNSET:
            field_dict["body"] = body
        if email_address_id is not UNSET:
            field_dict["email_address_id"] = email_address_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        from_email_name = d.pop("from_email_name", UNSET)

        subject = d.pop("subject", UNSET)

        body = d.pop("body", UNSET)

        email_address_id = d.pop("email_address_id", UNSET)

        create_email_json_body = cls(
            from_email_name=from_email_name,
            subject=subject,
            body=body,
            email_address_id=email_address_id,
        )

        return create_email_json_body
