from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..livtypes import UNSET, Unset

T = TypeVar("T", bound="PreviewTemplateJsonBody")


@attr.s(auto_attribs=True)
class PreviewTemplateJsonBody:
    """
    Attributes:
        subject (Union[Unset, None, str]): The email subject.
            Applicable only to email templates.
        body (Union[Unset, str]): The template body before variable interpolation
        from_email_name (Union[Unset, str]): The local part of the From email address that will be used for emails.
            For example, in the address 'hello@example.com', the local part is 'hello'.
            Applicable only to email templates.
    """

    subject: Union[Unset, None, str] = UNSET
    body: Union[Unset, str] = UNSET
    from_email_name: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        subject = self.subject
        body = self.body
        from_email_name = self.from_email_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if subject is not UNSET:
            field_dict["subject"] = subject
        if body is not UNSET:
            field_dict["body"] = body
        if from_email_name is not UNSET:
            field_dict["from_email_name"] = from_email_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        subject = d.pop("subject", UNSET)

        body = d.pop("body", UNSET)

        from_email_name = d.pop("from_email_name", UNSET)

        preview_template_json_body = cls(
            subject=subject,
            body=body,
            from_email_name=from_email_name,
        )

        return preview_template_json_body
