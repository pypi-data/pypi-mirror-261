from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.user_object import UserObject
from ..livtypes import UNSET, Unset

if TYPE_CHECKING:
    from ..models.email_address import EmailAddress
    from ..models.phone_number import PhoneNumber
    from ..models.saml_account import SAMLAccount
    from ..models.user_external_accounts_item import UserExternalAccountsItem
    from ..models.user_private_metadata import UserPrivateMetadata
    from ..models.user_public_metadata import UserPublicMetadata
    from ..models.user_unsafe_metadata import UserUnsafeMetadata
    from ..models.web_3_wallet import Web3Wallet


T = TypeVar("T", bound="User")


@attr.s(auto_attribs=True)
class User:
    """
    Attributes:
        id (Union[Unset, str]):
        object_ (Union[Unset, UserObject]): String representing the object's type. Objects of the same type share the
            same value.
        external_id (Union[Unset, None, str]):
        primary_email_address_id (Union[Unset, None, str]):
        primary_phone_number_id (Union[Unset, None, str]):
        primary_web3_wallet_id (Union[Unset, None, str]):
        username (Union[Unset, None, str]):
        first_name (Union[Unset, None, str]):
        last_name (Union[Unset, None, str]):
        profile_image_url (Union[Unset, str]):
        image_url (Union[Unset, str]):
        public_metadata (Union[Unset, UserPublicMetadata]):
        private_metadata (Union[Unset, None, UserPrivateMetadata]):
        unsafe_metadata (Union[Unset, UserUnsafeMetadata]):
        gender (Union[Unset, None, str]):
        birthday (Union[Unset, None, str]):
        email_addresses (Union[Unset, List['EmailAddress']]):
        phone_numbers (Union[Unset, List['PhoneNumber']]):
        web3_wallets (Union[Unset, List['Web3Wallet']]):
        password_enabled (Union[Unset, bool]):
        two_factor_enabled (Union[Unset, bool]):
        totp_enabled (Union[Unset, bool]):
        backup_code_enabled (Union[Unset, bool]):
        external_accounts (Union[Unset, List['UserExternalAccountsItem']]):
        saml_accounts (Union[Unset, List['SAMLAccount']]):
        last_sign_in_at (Union[Unset, None, int]): Unix timestamp of last sign-in.
        banned (Union[Unset, bool]): Flag to denote whether user is banned or not.
        updated_at (Union[Unset, int]): Unix timestamp of last update.
        created_at (Union[Unset, int]): Unix timestamp of creation.
        delete_self_enabled (Union[Unset, bool]): If enabled, user can delete themselves via FAPI.
        create_organization_enabled (Union[Unset, bool]): If enabled, user can create organizations via FAPI.
    """

    id: Union[Unset, str] = UNSET
    object_: Union[Unset, UserObject] = UNSET
    external_id: Union[Unset, None, str] = UNSET
    primary_email_address_id: Union[Unset, None, str] = UNSET
    primary_phone_number_id: Union[Unset, None, str] = UNSET
    primary_web3_wallet_id: Union[Unset, None, str] = UNSET
    username: Union[Unset, None, str] = UNSET
    first_name: Union[Unset, None, str] = UNSET
    last_name: Union[Unset, None, str] = UNSET
    profile_image_url: Union[Unset, str] = UNSET
    image_url: Union[Unset, str] = UNSET
    public_metadata: Union[Unset, "UserPublicMetadata"] = UNSET
    private_metadata: Union[Unset, None, "UserPrivateMetadata"] = UNSET
    unsafe_metadata: Union[Unset, "UserUnsafeMetadata"] = UNSET
    gender: Union[Unset, None, str] = UNSET
    birthday: Union[Unset, None, str] = UNSET
    email_addresses: Union[Unset, List["EmailAddress"]] = UNSET
    phone_numbers: Union[Unset, List["PhoneNumber"]] = UNSET
    web3_wallets: Union[Unset, List["Web3Wallet"]] = UNSET
    password_enabled: Union[Unset, bool] = UNSET
    two_factor_enabled: Union[Unset, bool] = UNSET
    totp_enabled: Union[Unset, bool] = UNSET
    backup_code_enabled: Union[Unset, bool] = UNSET
    external_accounts: Union[Unset, List["UserExternalAccountsItem"]] = UNSET
    saml_accounts: Union[Unset, List["SAMLAccount"]] = UNSET
    last_sign_in_at: Union[Unset, None, int] = UNSET
    banned: Union[Unset, bool] = UNSET
    updated_at: Union[Unset, int] = UNSET
    created_at: Union[Unset, int] = UNSET
    delete_self_enabled: Union[Unset, bool] = UNSET
    create_organization_enabled: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        object_: Union[Unset, str] = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        external_id = self.external_id
        primary_email_address_id = self.primary_email_address_id
        primary_phone_number_id = self.primary_phone_number_id
        primary_web3_wallet_id = self.primary_web3_wallet_id
        username = self.username
        first_name = self.first_name
        last_name = self.last_name
        profile_image_url = self.profile_image_url
        image_url = self.image_url
        public_metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.public_metadata, Unset):
            public_metadata = self.public_metadata.to_dict()

        private_metadata: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.private_metadata, Unset):
            private_metadata = self.private_metadata.to_dict() if self.private_metadata else None

        unsafe_metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unsafe_metadata, Unset):
            unsafe_metadata = self.unsafe_metadata.to_dict()

        gender = self.gender
        birthday = self.birthday
        email_addresses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.email_addresses, Unset):
            email_addresses = []
            for email_addresses_item_data in self.email_addresses:
                email_addresses_item = email_addresses_item_data.to_dict()

                email_addresses.append(email_addresses_item)

        phone_numbers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.phone_numbers, Unset):
            phone_numbers = []
            for phone_numbers_item_data in self.phone_numbers:
                phone_numbers_item = phone_numbers_item_data.to_dict()

                phone_numbers.append(phone_numbers_item)

        web3_wallets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.web3_wallets, Unset):
            web3_wallets = []
            for web3_wallets_item_data in self.web3_wallets:
                web3_wallets_item = web3_wallets_item_data.to_dict()

                web3_wallets.append(web3_wallets_item)

        password_enabled = self.password_enabled
        two_factor_enabled = self.two_factor_enabled
        totp_enabled = self.totp_enabled
        backup_code_enabled = self.backup_code_enabled
        external_accounts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.external_accounts, Unset):
            external_accounts = []
            for external_accounts_item_data in self.external_accounts:
                external_accounts_item = external_accounts_item_data.to_dict()

                external_accounts.append(external_accounts_item)

        saml_accounts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.saml_accounts, Unset):
            saml_accounts = []
            for saml_accounts_item_data in self.saml_accounts:
                saml_accounts_item = saml_accounts_item_data.to_dict()

                saml_accounts.append(saml_accounts_item)

        last_sign_in_at = self.last_sign_in_at
        banned = self.banned
        updated_at = self.updated_at
        created_at = self.created_at
        delete_self_enabled = self.delete_self_enabled
        create_organization_enabled = self.create_organization_enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if object_ is not UNSET:
            field_dict["object"] = object_
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if primary_email_address_id is not UNSET:
            field_dict["primary_email_address_id"] = primary_email_address_id
        if primary_phone_number_id is not UNSET:
            field_dict["primary_phone_number_id"] = primary_phone_number_id
        if primary_web3_wallet_id is not UNSET:
            field_dict["primary_web3_wallet_id"] = primary_web3_wallet_id
        if username is not UNSET:
            field_dict["username"] = username
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if profile_image_url is not UNSET:
            field_dict["profile_image_url"] = profile_image_url
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if public_metadata is not UNSET:
            field_dict["public_metadata"] = public_metadata
        if private_metadata is not UNSET:
            field_dict["private_metadata"] = private_metadata
        if unsafe_metadata is not UNSET:
            field_dict["unsafe_metadata"] = unsafe_metadata
        if gender is not UNSET:
            field_dict["gender"] = gender
        if birthday is not UNSET:
            field_dict["birthday"] = birthday
        if email_addresses is not UNSET:
            field_dict["email_addresses"] = email_addresses
        if phone_numbers is not UNSET:
            field_dict["phone_numbers"] = phone_numbers
        if web3_wallets is not UNSET:
            field_dict["web3_wallets"] = web3_wallets
        if password_enabled is not UNSET:
            field_dict["password_enabled"] = password_enabled
        if two_factor_enabled is not UNSET:
            field_dict["two_factor_enabled"] = two_factor_enabled
        if totp_enabled is not UNSET:
            field_dict["totp_enabled"] = totp_enabled
        if backup_code_enabled is not UNSET:
            field_dict["backup_code_enabled"] = backup_code_enabled
        if external_accounts is not UNSET:
            field_dict["external_accounts"] = external_accounts
        if saml_accounts is not UNSET:
            field_dict["saml_accounts"] = saml_accounts
        if last_sign_in_at is not UNSET:
            field_dict["last_sign_in_at"] = last_sign_in_at
        if banned is not UNSET:
            field_dict["banned"] = banned
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if delete_self_enabled is not UNSET:
            field_dict["delete_self_enabled"] = delete_self_enabled
        if create_organization_enabled is not UNSET:
            field_dict["create_organization_enabled"] = create_organization_enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.email_address import EmailAddress
        from ..models.phone_number import PhoneNumber
        from ..models.saml_account import SAMLAccount
        from ..models.user_external_accounts_item import UserExternalAccountsItem
        from ..models.user_private_metadata import UserPrivateMetadata
        from ..models.user_public_metadata import UserPublicMetadata
        from ..models.user_unsafe_metadata import UserUnsafeMetadata
        from ..models.web_3_wallet import Web3Wallet

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _object_ = d.pop("object", UNSET)
        object_: Union[Unset, UserObject]
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = UserObject(_object_)

        external_id = d.pop("external_id", UNSET)

        primary_email_address_id = d.pop("primary_email_address_id", UNSET)

        primary_phone_number_id = d.pop("primary_phone_number_id", UNSET)

        primary_web3_wallet_id = d.pop("primary_web3_wallet_id", UNSET)

        username = d.pop("username", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        profile_image_url = d.pop("profile_image_url", UNSET)

        image_url = d.pop("image_url", UNSET)

        _public_metadata = d.pop("public_metadata", UNSET)
        public_metadata: Union[Unset, UserPublicMetadata]
        if isinstance(_public_metadata, Unset):
            public_metadata = UNSET
        else:
            public_metadata = UserPublicMetadata.from_dict(_public_metadata)

        _private_metadata = d.pop("private_metadata", UNSET)
        private_metadata: Union[Unset, None, UserPrivateMetadata]
        if _private_metadata is None:
            private_metadata = None
        elif isinstance(_private_metadata, Unset):
            private_metadata = UNSET
        else:
            private_metadata = UserPrivateMetadata.from_dict(_private_metadata)

        _unsafe_metadata = d.pop("unsafe_metadata", UNSET)
        unsafe_metadata: Union[Unset, UserUnsafeMetadata]
        if isinstance(_unsafe_metadata, Unset):
            unsafe_metadata = UNSET
        else:
            unsafe_metadata = UserUnsafeMetadata.from_dict(_unsafe_metadata)

        gender = d.pop("gender", UNSET)

        birthday = d.pop("birthday", UNSET)

        email_addresses = []
        _email_addresses = d.pop("email_addresses", UNSET)
        for email_addresses_item_data in _email_addresses or []:
            email_addresses_item = EmailAddress.from_dict(email_addresses_item_data)

            email_addresses.append(email_addresses_item)

        phone_numbers = []
        _phone_numbers = d.pop("phone_numbers", UNSET)
        for phone_numbers_item_data in _phone_numbers or []:
            phone_numbers_item = PhoneNumber.from_dict(phone_numbers_item_data)

            phone_numbers.append(phone_numbers_item)

        web3_wallets = []
        _web3_wallets = d.pop("web3_wallets", UNSET)
        for web3_wallets_item_data in _web3_wallets or []:
            web3_wallets_item = Web3Wallet.from_dict(web3_wallets_item_data)

            web3_wallets.append(web3_wallets_item)

        password_enabled = d.pop("password_enabled", UNSET)

        two_factor_enabled = d.pop("two_factor_enabled", UNSET)

        totp_enabled = d.pop("totp_enabled", UNSET)

        backup_code_enabled = d.pop("backup_code_enabled", UNSET)

        external_accounts = []
        _external_accounts = d.pop("external_accounts", UNSET)
        for external_accounts_item_data in _external_accounts or []:
            external_accounts_item = UserExternalAccountsItem.from_dict(external_accounts_item_data)

            external_accounts.append(external_accounts_item)

        saml_accounts = []
        _saml_accounts = d.pop("saml_accounts", UNSET)
        for saml_accounts_item_data in _saml_accounts or []:
            saml_accounts_item = SAMLAccount.from_dict(saml_accounts_item_data)

            saml_accounts.append(saml_accounts_item)

        last_sign_in_at = d.pop("last_sign_in_at", UNSET)

        banned = d.pop("banned", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        created_at = d.pop("created_at", UNSET)

        delete_self_enabled = d.pop("delete_self_enabled", UNSET)

        create_organization_enabled = d.pop("create_organization_enabled", UNSET)

        user = cls(
            id=id,
            object_=object_,
            external_id=external_id,
            primary_email_address_id=primary_email_address_id,
            primary_phone_number_id=primary_phone_number_id,
            primary_web3_wallet_id=primary_web3_wallet_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            profile_image_url=profile_image_url,
            image_url=image_url,
            public_metadata=public_metadata,
            private_metadata=private_metadata,
            unsafe_metadata=unsafe_metadata,
            gender=gender,
            birthday=birthday,
            email_addresses=email_addresses,
            phone_numbers=phone_numbers,
            web3_wallets=web3_wallets,
            password_enabled=password_enabled,
            two_factor_enabled=two_factor_enabled,
            totp_enabled=totp_enabled,
            backup_code_enabled=backup_code_enabled,
            external_accounts=external_accounts,
            saml_accounts=saml_accounts,
            last_sign_in_at=last_sign_in_at,
            banned=banned,
            updated_at=updated_at,
            created_at=created_at,
            delete_self_enabled=delete_self_enabled,
            create_organization_enabled=create_organization_enabled,
        )

        return user
