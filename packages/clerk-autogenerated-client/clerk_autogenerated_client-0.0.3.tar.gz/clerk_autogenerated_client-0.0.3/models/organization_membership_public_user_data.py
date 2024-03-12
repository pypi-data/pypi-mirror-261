from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..livtypes import UNSET, Unset

T = TypeVar("T", bound="OrganizationMembershipPublicUserData")


@attr.s(auto_attribs=True)
class OrganizationMembershipPublicUserData:
    """
    Attributes:
        user_id (Union[Unset, str]):
        first_name (Union[Unset, None, str]):
        last_name (Union[Unset, None, str]):
        profile_image_url (Union[Unset, None, str]):
        image_url (Union[Unset, str]):
        identifier (Union[Unset, None, str]):
    """

    user_id: Union[Unset, str] = UNSET
    first_name: Union[Unset, None, str] = UNSET
    last_name: Union[Unset, None, str] = UNSET
    profile_image_url: Union[Unset, None, str] = UNSET
    image_url: Union[Unset, str] = UNSET
    identifier: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id
        first_name = self.first_name
        last_name = self.last_name
        profile_image_url = self.profile_image_url
        image_url = self.image_url
        identifier = self.identifier

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if profile_image_url is not UNSET:
            field_dict["profile_image_url"] = profile_image_url
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if identifier is not UNSET:
            field_dict["identifier"] = identifier

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("user_id", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        profile_image_url = d.pop("profile_image_url", UNSET)

        image_url = d.pop("image_url", UNSET)

        identifier = d.pop("identifier", UNSET)

        organization_membership_public_user_data = cls(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            profile_image_url=profile_image_url,
            image_url=image_url,
            identifier=identifier,
        )

        return organization_membership_public_user_data
