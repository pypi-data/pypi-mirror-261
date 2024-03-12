from typing import TYPE_CHECKING, Any, Dict, Optional, Type, TypeVar, Union

import attr

from ..models.email_object import EmailObject
from ..livtypes import UNSET, Unset

if TYPE_CHECKING:
    from ..models.email_data import EmailData


T = TypeVar("T", bound="Email")


@attr.s(auto_attribs=True)
class Email:
    """
    Attributes:
        object_ (EmailObject):
        id (str):
        from_email_name (str):
        to_email_address (str):
        subject (str):
        body (str):
        status (str):
        delivered_by_clerk (bool):
        slug (Union[Unset, None, str]):
        email_address_id (Optional[str]):
        user_id (Union[Unset, None, str]):
        body_plain (Union[Unset, None, str]):
        data (Union[Unset, None, EmailData]):
    """

    object_: EmailObject
    id: str
    from_email_name: str
    to_email_address: str
    subject: str
    body: str
    status: str
    delivered_by_clerk: bool
    email_address_id: Optional[str]
    slug: Union[Unset, None, str] = UNSET
    user_id: Union[Unset, None, str] = UNSET
    body_plain: Union[Unset, None, str] = UNSET
    data: Union[Unset, None, "EmailData"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_.value

        id = self.id
        from_email_name = self.from_email_name
        to_email_address = self.to_email_address
        subject = self.subject
        body = self.body
        status = self.status
        delivered_by_clerk = self.delivered_by_clerk
        slug = self.slug
        email_address_id = self.email_address_id
        user_id = self.user_id
        body_plain = self.body_plain
        data: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict() if self.data else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "object": object_,
                "id": id,
                "from_email_name": from_email_name,
                "to_email_address": to_email_address,
                "subject": subject,
                "body": body,
                "status": status,
                "delivered_by_clerk": delivered_by_clerk,
                "email_address_id": email_address_id,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if body_plain is not UNSET:
            field_dict["body_plain"] = body_plain
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.email_data import EmailData

        d = src_dict.copy()
        object_ = EmailObject(d.pop("object"))

        id = d.pop("id")

        from_email_name = d.pop("from_email_name")

        to_email_address = d.pop("to_email_address")

        subject = d.pop("subject")

        body = d.pop("body")

        status = d.pop("status")

        delivered_by_clerk = d.pop("delivered_by_clerk")

        slug = d.pop("slug", UNSET)

        email_address_id = d.pop("email_address_id")

        user_id = d.pop("user_id", UNSET)

        body_plain = d.pop("body_plain", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, None, EmailData]
        if _data is None:
            data = None
        elif isinstance(_data, Unset):
            data = UNSET
        else:
            data = EmailData.from_dict(_data)

        email = cls(
            object_=object_,
            id=id,
            from_email_name=from_email_name,
            to_email_address=to_email_address,
            subject=subject,
            body=body,
            status=status,
            delivered_by_clerk=delivered_by_clerk,
            slug=slug,
            email_address_id=email_address_id,
            user_id=user_id,
            body_plain=body_plain,
            data=data,
        )

        return email
