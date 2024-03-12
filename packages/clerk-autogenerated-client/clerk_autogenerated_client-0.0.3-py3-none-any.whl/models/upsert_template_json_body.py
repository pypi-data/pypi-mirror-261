from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..livtypes import UNSET, Unset

T = TypeVar("T", bound="UpsertTemplateJsonBody")


@attr.s(auto_attribs=True)
class UpsertTemplateJsonBody:
    """
    Attributes:
        name (Union[Unset, str]): The user-friendly name of the template
        subject (Union[Unset, None, str]): The email subject.
            Applicable only to email templates.
        markup (Union[Unset, None, str]): The editor markup used to generate the body of the template
        body (Union[Unset, str]): The template body before variable interpolation
        delivered_by_clerk (Union[Unset, None, bool]): Whether Clerk should deliver emails or SMS messages based on the
            current template
        from_email_name (Union[Unset, str]): The local part of the From email address that will be used for emails.
            For example, in the address 'hello@example.com', the local part is 'hello'.
            Applicable only to email templates.
    """

    name: Union[Unset, str] = UNSET
    subject: Union[Unset, None, str] = UNSET
    markup: Union[Unset, None, str] = UNSET
    body: Union[Unset, str] = UNSET
    delivered_by_clerk: Union[Unset, None, bool] = UNSET
    from_email_name: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        subject = self.subject
        markup = self.markup
        body = self.body
        delivered_by_clerk = self.delivered_by_clerk
        from_email_name = self.from_email_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if subject is not UNSET:
            field_dict["subject"] = subject
        if markup is not UNSET:
            field_dict["markup"] = markup
        if body is not UNSET:
            field_dict["body"] = body
        if delivered_by_clerk is not UNSET:
            field_dict["delivered_by_clerk"] = delivered_by_clerk
        if from_email_name is not UNSET:
            field_dict["from_email_name"] = from_email_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        subject = d.pop("subject", UNSET)

        markup = d.pop("markup", UNSET)

        body = d.pop("body", UNSET)

        delivered_by_clerk = d.pop("delivered_by_clerk", UNSET)

        from_email_name = d.pop("from_email_name", UNSET)

        upsert_template_json_body = cls(
            name=name,
            subject=subject,
            markup=markup,
            body=body,
            delivered_by_clerk=delivered_by_clerk,
            from_email_name=from_email_name,
        )

        return upsert_template_json_body
