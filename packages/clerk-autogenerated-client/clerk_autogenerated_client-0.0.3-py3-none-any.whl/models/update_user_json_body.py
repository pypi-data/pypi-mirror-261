from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..livtypes import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_user_json_body_private_metadata import UpdateUserJsonBodyPrivateMetadata
    from ..models.update_user_json_body_public_metadata import UpdateUserJsonBodyPublicMetadata
    from ..models.update_user_json_body_unsafe_metadata import UpdateUserJsonBodyUnsafeMetadata


T = TypeVar("T", bound="UpdateUserJsonBody")


@attr.s(auto_attribs=True)
class UpdateUserJsonBody:
    """
    Attributes:
        external_id (Union[Unset, None, str]): The ID of the user as used in your external systems or your previous
            authentication solution.
            Must be unique across your instance.
        first_name (Union[Unset, None, str]): The first name to assign to the user
        last_name (Union[Unset, None, str]): The last name to assign to the user
        primary_email_address_id (Union[Unset, str]): The ID of the email address to set as primary.
            It must be verified, and present on the current user.
        primary_phone_number_id (Union[Unset, str]): The ID of the phone number to set as primary.
            It must be verified, and present on the current user.
        primary_web3_wallet_id (Union[Unset, str]): The ID of the web3 wallets to set as primary.
            It must be verified, and present on the current user.
        username (Union[Unset, None, str]): The username to give to the user.
            It must be unique across your instance.
        profile_image_id (Union[Unset, None, str]): The ID of the image to set as the user's profile image
        password (Union[Unset, None, str]): The plaintext password to give the user.
            Must be at least 8 characters long, and can not be in any list of hacked passwords.
        skip_password_checks (Union[Unset, None, bool]): Set it to `true` if you're updating the user's password and
            want to skip any password policy settings check. This parameter can only be used when providing a `password`.
        sign_out_of_other_sessions (Union[Unset, None, bool]): Set to `true` to sign out the user from all their active
            sessions once their password is updated. This parameter can only be used when providing a `password`.
        totp_secret (Union[Unset, str]): In case TOTP is configured on the instance, you can provide the secret to
            enable it on the specific user without the need to reset it.
            Please note that currently the supported options are:
            * Period: 30 seconds
            * Code length: 6 digits
            * Algorithm: SHA1
        backup_codes (Union[Unset, List[str]]): If Backup Codes are configured on the instance, you can provide them to
            enable it on the specific user without the need to reset them.
            You must provide the backup codes in plain format or the corresponding bcrypt digest.
        public_metadata (Union[Unset, UpdateUserJsonBodyPublicMetadata]): Metadata saved on the user, that is visible to
            both your Frontend and Backend APIs
        private_metadata (Union[Unset, UpdateUserJsonBodyPrivateMetadata]): Metadata saved on the user, that is only
            visible to your Backend API
        unsafe_metadata (Union[Unset, UpdateUserJsonBodyUnsafeMetadata]): Metadata saved on the user, that can be
            updated from both the Frontend and Backend APIs.
            Note: Since this data can be modified from the frontend, it is not guaranteed to be safe.
        delete_self_enabled (Union[Unset, None, bool]): If true, the user can delete themselves with the Frontend API.
        create_organization_enabled (Union[Unset, None, bool]): If true, the user can create organizations with the
            Frontend API.
        created_at (Union[Unset, str]): A custom date/time denoting _when_ the user signed up to the application,
            specified in RFC3339 format (e.g. `2012-10-20T07:15:20.902Z`).
    """

    external_id: Union[Unset, None, str] = UNSET
    first_name: Union[Unset, None, str] = UNSET
    last_name: Union[Unset, None, str] = UNSET
    primary_email_address_id: Union[Unset, str] = UNSET
    primary_phone_number_id: Union[Unset, str] = UNSET
    primary_web3_wallet_id: Union[Unset, str] = UNSET
    username: Union[Unset, None, str] = UNSET
    profile_image_id: Union[Unset, None, str] = UNSET
    password: Union[Unset, None, str] = UNSET
    skip_password_checks: Union[Unset, None, bool] = UNSET
    sign_out_of_other_sessions: Union[Unset, None, bool] = UNSET
    totp_secret: Union[Unset, str] = UNSET
    backup_codes: Union[Unset, List[str]] = UNSET
    public_metadata: Union[Unset, "UpdateUserJsonBodyPublicMetadata"] = UNSET
    private_metadata: Union[Unset, "UpdateUserJsonBodyPrivateMetadata"] = UNSET
    unsafe_metadata: Union[Unset, "UpdateUserJsonBodyUnsafeMetadata"] = UNSET
    delete_self_enabled: Union[Unset, None, bool] = UNSET
    create_organization_enabled: Union[Unset, None, bool] = UNSET
    created_at: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        external_id = self.external_id
        first_name = self.first_name
        last_name = self.last_name
        primary_email_address_id = self.primary_email_address_id
        primary_phone_number_id = self.primary_phone_number_id
        primary_web3_wallet_id = self.primary_web3_wallet_id
        username = self.username
        profile_image_id = self.profile_image_id
        password = self.password
        skip_password_checks = self.skip_password_checks
        sign_out_of_other_sessions = self.sign_out_of_other_sessions
        totp_secret = self.totp_secret
        backup_codes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.backup_codes, Unset):
            backup_codes = self.backup_codes

        public_metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.public_metadata, Unset):
            public_metadata = self.public_metadata.to_dict()

        private_metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.private_metadata, Unset):
            private_metadata = self.private_metadata.to_dict()

        unsafe_metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unsafe_metadata, Unset):
            unsafe_metadata = self.unsafe_metadata.to_dict()

        delete_self_enabled = self.delete_self_enabled
        create_organization_enabled = self.create_organization_enabled
        created_at = self.created_at

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if primary_email_address_id is not UNSET:
            field_dict["primary_email_address_id"] = primary_email_address_id
        if primary_phone_number_id is not UNSET:
            field_dict["primary_phone_number_id"] = primary_phone_number_id
        if primary_web3_wallet_id is not UNSET:
            field_dict["primary_web3_wallet_id"] = primary_web3_wallet_id
        if username is not UNSET:
            field_dict["username"] = username
        if profile_image_id is not UNSET:
            field_dict["profile_image_id"] = profile_image_id
        if password is not UNSET:
            field_dict["password"] = password
        if skip_password_checks is not UNSET:
            field_dict["skip_password_checks"] = skip_password_checks
        if sign_out_of_other_sessions is not UNSET:
            field_dict["sign_out_of_other_sessions"] = sign_out_of_other_sessions
        if totp_secret is not UNSET:
            field_dict["totp_secret"] = totp_secret
        if backup_codes is not UNSET:
            field_dict["backup_codes"] = backup_codes
        if public_metadata is not UNSET:
            field_dict["public_metadata"] = public_metadata
        if private_metadata is not UNSET:
            field_dict["private_metadata"] = private_metadata
        if unsafe_metadata is not UNSET:
            field_dict["unsafe_metadata"] = unsafe_metadata
        if delete_self_enabled is not UNSET:
            field_dict["delete_self_enabled"] = delete_self_enabled
        if create_organization_enabled is not UNSET:
            field_dict["create_organization_enabled"] = create_organization_enabled
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.update_user_json_body_private_metadata import UpdateUserJsonBodyPrivateMetadata
        from ..models.update_user_json_body_public_metadata import UpdateUserJsonBodyPublicMetadata
        from ..models.update_user_json_body_unsafe_metadata import UpdateUserJsonBodyUnsafeMetadata

        d = src_dict.copy()
        external_id = d.pop("external_id", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        primary_email_address_id = d.pop("primary_email_address_id", UNSET)

        primary_phone_number_id = d.pop("primary_phone_number_id", UNSET)

        primary_web3_wallet_id = d.pop("primary_web3_wallet_id", UNSET)

        username = d.pop("username", UNSET)

        profile_image_id = d.pop("profile_image_id", UNSET)

        password = d.pop("password", UNSET)

        skip_password_checks = d.pop("skip_password_checks", UNSET)

        sign_out_of_other_sessions = d.pop("sign_out_of_other_sessions", UNSET)

        totp_secret = d.pop("totp_secret", UNSET)

        backup_codes = cast(List[str], d.pop("backup_codes", UNSET))

        _public_metadata = d.pop("public_metadata", UNSET)
        public_metadata: Union[Unset, UpdateUserJsonBodyPublicMetadata]
        if isinstance(_public_metadata, Unset):
            public_metadata = UNSET
        else:
            public_metadata = UpdateUserJsonBodyPublicMetadata.from_dict(_public_metadata)

        _private_metadata = d.pop("private_metadata", UNSET)
        private_metadata: Union[Unset, UpdateUserJsonBodyPrivateMetadata]
        if isinstance(_private_metadata, Unset):
            private_metadata = UNSET
        else:
            private_metadata = UpdateUserJsonBodyPrivateMetadata.from_dict(_private_metadata)

        _unsafe_metadata = d.pop("unsafe_metadata", UNSET)
        unsafe_metadata: Union[Unset, UpdateUserJsonBodyUnsafeMetadata]
        if isinstance(_unsafe_metadata, Unset):
            unsafe_metadata = UNSET
        else:
            unsafe_metadata = UpdateUserJsonBodyUnsafeMetadata.from_dict(_unsafe_metadata)

        delete_self_enabled = d.pop("delete_self_enabled", UNSET)

        create_organization_enabled = d.pop("create_organization_enabled", UNSET)

        created_at = d.pop("created_at", UNSET)

        update_user_json_body = cls(
            external_id=external_id,
            first_name=first_name,
            last_name=last_name,
            primary_email_address_id=primary_email_address_id,
            primary_phone_number_id=primary_phone_number_id,
            primary_web3_wallet_id=primary_web3_wallet_id,
            username=username,
            profile_image_id=profile_image_id,
            password=password,
            skip_password_checks=skip_password_checks,
            sign_out_of_other_sessions=sign_out_of_other_sessions,
            totp_secret=totp_secret,
            backup_codes=backup_codes,
            public_metadata=public_metadata,
            private_metadata=private_metadata,
            unsafe_metadata=unsafe_metadata,
            delete_self_enabled=delete_self_enabled,
            create_organization_enabled=create_organization_enabled,
            created_at=created_at,
        )

        return update_user_json_body
