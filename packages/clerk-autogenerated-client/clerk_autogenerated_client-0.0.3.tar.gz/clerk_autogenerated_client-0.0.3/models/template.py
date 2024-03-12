from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.template_object import TemplateObject
from ..livtypes import UNSET, Unset

T = TypeVar("T", bound="Template")


@attr.s(auto_attribs=True)
class Template:
    """
    Attributes:
        id (Union[Unset, str]):
        object_ (Union[Unset, TemplateObject]): String representing the object's type. Objects of the same type share
            the same value.
        instance_id (Union[Unset, None, str]): the id of the instance the template belongs to
        resource_type (Union[Unset, str]): whether this is a system (default) or user overridden) template
        template_type (Union[Unset, str]): whether this is an email or SMS template
        name (Union[Unset, str]): user-friendly name of the template
        slug (Union[Unset, str]): machine-friendly name of the template
        position (Union[Unset, int]): position with the listing of templates
        can_revert (Union[Unset, bool]): whether this template can be reverted to the corresponding system default
        can_delete (Union[Unset, bool]): whether this template can be deleted
        subject (Union[Unset, None, str]): email subject
        markup (Union[Unset, str]): the editor markup used to generate the body of the template
        body (Union[Unset, str]): the template body before variable interpolation
        available_variables (Union[Unset, List[str]]): list of variables that are available for use in the template body
        required_variables (Union[Unset, List[str]]): list of variables that must be contained in the template body
        from_email_name (Union[Unset, str]):
        delivered_by_clerk (Union[Unset, bool]):
        updated_at (Union[Unset, int]): Unix timestamp of last update.
        created_at (Union[Unset, int]): Unix timestamp of creation.
    """

    id: Union[Unset, str] = UNSET
    object_: Union[Unset, TemplateObject] = UNSET
    instance_id: Union[Unset, None, str] = UNSET
    resource_type: Union[Unset, str] = UNSET
    template_type: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    slug: Union[Unset, str] = UNSET
    position: Union[Unset, int] = UNSET
    can_revert: Union[Unset, bool] = UNSET
    can_delete: Union[Unset, bool] = UNSET
    subject: Union[Unset, None, str] = UNSET
    markup: Union[Unset, str] = UNSET
    body: Union[Unset, str] = UNSET
    available_variables: Union[Unset, List[str]] = UNSET
    required_variables: Union[Unset, List[str]] = UNSET
    from_email_name: Union[Unset, str] = UNSET
    delivered_by_clerk: Union[Unset, bool] = UNSET
    updated_at: Union[Unset, int] = UNSET
    created_at: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        object_: Union[Unset, str] = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        instance_id = self.instance_id
        resource_type = self.resource_type
        template_type = self.template_type
        name = self.name
        slug = self.slug
        position = self.position
        can_revert = self.can_revert
        can_delete = self.can_delete
        subject = self.subject
        markup = self.markup
        body = self.body
        available_variables: Union[Unset, List[str]] = UNSET
        if not isinstance(self.available_variables, Unset):
            available_variables = self.available_variables

        required_variables: Union[Unset, List[str]] = UNSET
        if not isinstance(self.required_variables, Unset):
            required_variables = self.required_variables

        from_email_name = self.from_email_name
        delivered_by_clerk = self.delivered_by_clerk
        updated_at = self.updated_at
        created_at = self.created_at

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if object_ is not UNSET:
            field_dict["object"] = object_
        if instance_id is not UNSET:
            field_dict["instance_id"] = instance_id
        if resource_type is not UNSET:
            field_dict["resource_type"] = resource_type
        if template_type is not UNSET:
            field_dict["template_type"] = template_type
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if position is not UNSET:
            field_dict["position"] = position
        if can_revert is not UNSET:
            field_dict["can_revert"] = can_revert
        if can_delete is not UNSET:
            field_dict["can_delete"] = can_delete
        if subject is not UNSET:
            field_dict["subject"] = subject
        if markup is not UNSET:
            field_dict["markup"] = markup
        if body is not UNSET:
            field_dict["body"] = body
        if available_variables is not UNSET:
            field_dict["available_variables"] = available_variables
        if required_variables is not UNSET:
            field_dict["required_variables"] = required_variables
        if from_email_name is not UNSET:
            field_dict["from_email_name"] = from_email_name
        if delivered_by_clerk is not UNSET:
            field_dict["delivered_by_clerk"] = delivered_by_clerk
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _object_ = d.pop("object", UNSET)
        object_: Union[Unset, TemplateObject]
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = TemplateObject(_object_)

        instance_id = d.pop("instance_id", UNSET)

        resource_type = d.pop("resource_type", UNSET)

        template_type = d.pop("template_type", UNSET)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        position = d.pop("position", UNSET)

        can_revert = d.pop("can_revert", UNSET)

        can_delete = d.pop("can_delete", UNSET)

        subject = d.pop("subject", UNSET)

        markup = d.pop("markup", UNSET)

        body = d.pop("body", UNSET)

        available_variables = cast(List[str], d.pop("available_variables", UNSET))

        required_variables = cast(List[str], d.pop("required_variables", UNSET))

        from_email_name = d.pop("from_email_name", UNSET)

        delivered_by_clerk = d.pop("delivered_by_clerk", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        created_at = d.pop("created_at", UNSET)

        template = cls(
            id=id,
            object_=object_,
            instance_id=instance_id,
            resource_type=resource_type,
            template_type=template_type,
            name=name,
            slug=slug,
            position=position,
            can_revert=can_revert,
            can_delete=can_delete,
            subject=subject,
            markup=markup,
            body=body,
            available_variables=available_variables,
            required_variables=required_variables,
            from_email_name=from_email_name,
            delivered_by_clerk=delivered_by_clerk,
            updated_at=updated_at,
            created_at=created_at,
        )

        return template
