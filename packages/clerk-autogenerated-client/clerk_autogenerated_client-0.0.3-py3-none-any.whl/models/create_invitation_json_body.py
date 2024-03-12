from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..livtypes import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_invitation_json_body_public_metadata import CreateInvitationJsonBodyPublicMetadata


T = TypeVar("T", bound="CreateInvitationJsonBody")


@attr.s(auto_attribs=True)
class CreateInvitationJsonBody:
    """
    Attributes:
        email_address (str): The email address the invitation will be sent to
        public_metadata (Union[Unset, CreateInvitationJsonBodyPublicMetadata]): Metadata that will be attached to the
            newly created invitation.
            The value of this property should be a well-formed JSON object.
            Once the user accepts the invitation and signs up, these metadata will end up in the user's public metadata.
        redirect_url (Union[Unset, str]): Optional URL which specifies where to redirect the user once they click the
            invitation link.
            This is only required if you have implemented a [custom
            flow](https://clerk.com/docs/authentication/invitations#custom-flow) and you're not using Clerk Hosted Pages or
            Clerk Components.
    """

    email_address: str
    public_metadata: Union[Unset, "CreateInvitationJsonBodyPublicMetadata"] = UNSET
    redirect_url: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        email_address = self.email_address
        public_metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.public_metadata, Unset):
            public_metadata = self.public_metadata.to_dict()

        redirect_url = self.redirect_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "email_address": email_address,
            }
        )
        if public_metadata is not UNSET:
            field_dict["public_metadata"] = public_metadata
        if redirect_url is not UNSET:
            field_dict["redirect_url"] = redirect_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_invitation_json_body_public_metadata import CreateInvitationJsonBodyPublicMetadata

        d = src_dict.copy()
        email_address = d.pop("email_address")

        _public_metadata = d.pop("public_metadata", UNSET)
        public_metadata: Union[Unset, CreateInvitationJsonBodyPublicMetadata]
        if isinstance(_public_metadata, Unset):
            public_metadata = UNSET
        else:
            public_metadata = CreateInvitationJsonBodyPublicMetadata.from_dict(_public_metadata)

        redirect_url = d.pop("redirect_url", UNSET)

        create_invitation_json_body = cls(
            email_address=email_address,
            public_metadata=public_metadata,
            redirect_url=redirect_url,
        )

        return create_invitation_json_body
