from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.create_user_json_body_password_hasher import CreateUserJsonBodyPasswordHasher
from ..livtypes import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_user_json_body_private_metadata import CreateUserJsonBodyPrivateMetadata
    from ..models.create_user_json_body_public_metadata import CreateUserJsonBodyPublicMetadata
    from ..models.create_user_json_body_unsafe_metadata import CreateUserJsonBodyUnsafeMetadata


T = TypeVar("T", bound="CreateUserJsonBody")


@attr.s(auto_attribs=True)
class CreateUserJsonBody:
    """
    Attributes:
        external_id (Union[Unset, None, str]): The ID of the user as used in your external systems or your previous
            authentication solution.
            Must be unique across your instance.
        first_name (Union[Unset, None, str]): The first name to assign to the user
        last_name (Union[Unset, None, str]): The last name to assign to the user
        email_address (Union[Unset, List[str]]): Email addresses to add to the user.
            Must be unique across your instance.
            The first email address will be set as the user's primary email address.
        phone_number (Union[Unset, List[str]]): Phone numbers to add to the user.
            Must be unique across your instance.
            The first phone number will be set as the user's primary phone number.
        web3_wallet (Union[Unset, List[str]]): Web3 wallets to add to the user.
            Must be unique across your instance.
            The first wallet will be set as the user's primary wallet.
        username (Union[Unset, None, str]): The username to give to the user.
            It must be unique across your instance.
        password (Union[Unset, None, str]): The plaintext password to give the user.
            Must be at least 8 characters long, and can not be in any list of hacked passwords.
        password_digest (Union[Unset, str]): In case you already have the password digests and not the passwords, you
            can use them for the newly created user via this property.
            The digests should be generated with one of the supported algorithms.
            The hashing algorithm can be specified using the `password_hasher` property.
        password_hasher (Union[Unset, CreateUserJsonBodyPasswordHasher]): The hashing algorithm that was used to
            generate the password digest.
            The algorithms we support at the moment are [bcrypt](https://en.wikipedia.org/wiki/Bcrypt),
            [bcrypt_sha256_django](https://docs.djangoproject.com/en/4.0/topics/auth/passwords/), md5, pbkdf2_sha256,
            [pbkdf2_sha256_django](https://docs.djangoproject.com/en/4.0/topics/auth/passwords/),
            [scrypt_firebase](https://firebaseopensource.com/projects/firebase/scrypt/) and 2
            [argon2](https://argon2.online/) variants, argon2i and argon2id.
            Each of the above expects the incoming digest to be of a particular format.

            More specifically:

            **bcrypt:** The digest should be of the following form:

            `$<algorithm version>$<cost>$<salt & hash>`

            **bcrypt_sha256_django:** This is the Django-specific variant of Bcrypt, using SHA256 hashing function. The
            format should be as follows (as exported from Django):

            `bcrypt_sha256$$<algorithm version>$<cost>$<salt & hash>`

            **md5:** The digest should follow the regular form e.g.:

            `5f4dcc3b5aa765d61d8327deb882cf99`

            **pbkdf2_sha256:** This is the PBKDF2 algorithm using the SHA256 hashing function. The format should be as
            follows:

            `pbkdf2_sha256$<iterations>$<salt>$<hash>`

            Note: Both the salt and the hash are expected to be base64-encoded.

            **pbkdf2_sha256_django:** This is the Django-specific variant of PBKDF2 and the digest should have the following
            format (as exported from Django):

            `pbkdf2_sha256$<iterations>$<salt>$<hash>`

            Note: The salt is expected to be un-encoded, the hash is expected base64-encoded.

            **pbkdf2_sha1:** This is similar to pkbdf2_sha256_django, but with two differences:
            1. uses sha1 instead of sha256
            2. accepts the hash as a hex-encoded string

            The format is the following:

            `pbkdf2_sha1$<iterations>$<salt>$<hash-as-hex-string>`


            **scrypt_firebase:** The Firebase-specific variant of scrypt.
            The value is expected to have 6 segments separated by the $ character and include the following information:

            _hash:_ The actual Base64 hash. This can be retrieved when exporting the user from Firebase.
            _salt:_ The salt used to generate the above hash. Again, this is given when exporting the user.
            _signer key:_ The base64 encoded signer key.
            _salt separator:_ The base64 encoded salt separator.
            _rounds:_ The number of rounds the algorithm needs to run.
            _memory cost:_ The cost of the algorithm run

            The first 2 (hash and salt) are per user and can be retrieved when exporting the user from Firebase.
            The other 4 values (signer key, salt separator, rounds and memory cost) are project-wide settings and can be
            retrieved from the project's password hash parameters.

            Once you have all these, you can combine it in the following format and send this as the digest in order for
            Clerk to accept it:

            `<hash>$<salt>$<signer key>$<salt separator>$<rounds>$<memory cost>`

            **argon2i:** Algorithms in the argon2 family generate digests that encode the following information:

            _version (v):_ The argon version, version 19 is assumed
            _memory (m):_ The memory used by the algorithm (in kibibytes)
            _iterations (t):_ The number of iterations to perform
            _parallelism (p):_ The number of threads to use

            Parts are demarcated by the `$` character, with the first part identifying the algorithm variant.
            The middle part is a comma-separated list of the encoding options (memory, iterations, parallelism).
            The final part is the actual digest.

            `$argon2i$v=19$m=4096,t=3,p=1$4t6CL3P7YiHBtwESXawI8Hm20zJj4cs7/4/G3c187e0$m7RQFczcKr5bIR0IIxbpO2P0tyrLjf3eUW3M3Q
            SwnLc`

            **argon2id:** See the previous algorithm for an explanation of the formatting.

            For the argon2id case, the value of the algorithm in the first part of the digest is `argon2id`:

            `$argon2id$v=19$m=64,t=4,p=8$Z2liZXJyaXNo$iGXEpMBTDYQ8G/71tF0qGjxRHEmR3gpGULcE93zUJVU`

            If you need support for any particular hashing algorithm, [please let us know](https://clerk.com/support).
        skip_password_checks (Union[Unset, bool]): When set to `true` all password checks are skipped.
            It is recommended to use this method only when migrating plaintext passwords to Clerk.
            Upon migration the user base should be prompted to pick stronger password.
        skip_password_requirement (Union[Unset, bool]): When set to `true`, `password` is not required anymore when
            creating the user and can be omitted.
            This is useful when you are trying to create a user that doesn't have a password, in an instance that is using
            passwords.
            Please note that you cannot use this flag if password is the only way for a user to sign into your instance.
        totp_secret (Union[Unset, str]): In case TOTP is configured on the instance, you can provide the secret to
            enable it on the newly created user without the need to reset it.
            Please note that currently the supported options are:
            * Period: 30 seconds
            * Code length: 6 digits
            * Algorithm: SHA1
        backup_codes (Union[Unset, List[str]]): If Backup Codes are configured on the instance, you can provide them to
            enable it on the newly created user without the need to reset them.
            You must provide the backup codes in plain format or the corresponding bcrypt digest.
        public_metadata (Union[Unset, CreateUserJsonBodyPublicMetadata]): Metadata saved on the user, that is visible to
            both your Frontend and Backend APIs
        private_metadata (Union[Unset, CreateUserJsonBodyPrivateMetadata]): Metadata saved on the user, that is only
            visible to your Backend API
        unsafe_metadata (Union[Unset, CreateUserJsonBodyUnsafeMetadata]): Metadata saved on the user, that can be
            updated from both the Frontend and Backend APIs.
            Note: Since this data can be modified from the frontend, it is not guaranteed to be safe.
        created_at (Union[Unset, str]): A custom date/time denoting _when_ the user signed up to the application,
            specified in RFC3339 format (e.g. `2012-10-20T07:15:20.902Z`).
    """

    external_id: Union[Unset, None, str] = UNSET
    first_name: Union[Unset, None, str] = UNSET
    last_name: Union[Unset, None, str] = UNSET
    email_address: Union[Unset, List[str]] = UNSET
    phone_number: Union[Unset, List[str]] = UNSET
    web3_wallet: Union[Unset, List[str]] = UNSET
    username: Union[Unset, None, str] = UNSET
    password: Union[Unset, None, str] = UNSET
    password_digest: Union[Unset, str] = UNSET
    password_hasher: Union[Unset, CreateUserJsonBodyPasswordHasher] = UNSET
    skip_password_checks: Union[Unset, bool] = UNSET
    skip_password_requirement: Union[Unset, bool] = UNSET
    totp_secret: Union[Unset, str] = UNSET
    backup_codes: Union[Unset, List[str]] = UNSET
    public_metadata: Union[Unset, "CreateUserJsonBodyPublicMetadata"] = UNSET
    private_metadata: Union[Unset, "CreateUserJsonBodyPrivateMetadata"] = UNSET
    unsafe_metadata: Union[Unset, "CreateUserJsonBodyUnsafeMetadata"] = UNSET
    created_at: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        external_id = self.external_id
        first_name = self.first_name
        last_name = self.last_name
        email_address: Union[Unset, List[str]] = UNSET
        if not isinstance(self.email_address, Unset):
            email_address = self.email_address

        phone_number: Union[Unset, List[str]] = UNSET
        if not isinstance(self.phone_number, Unset):
            phone_number = self.phone_number

        web3_wallet: Union[Unset, List[str]] = UNSET
        if not isinstance(self.web3_wallet, Unset):
            web3_wallet = self.web3_wallet

        username = self.username
        password = self.password
        password_digest = self.password_digest
        password_hasher: Union[Unset, str] = UNSET
        if not isinstance(self.password_hasher, Unset):
            password_hasher = self.password_hasher.value

        skip_password_checks = self.skip_password_checks
        skip_password_requirement = self.skip_password_requirement
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

        created_at = self.created_at

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if email_address is not UNSET:
            field_dict["email_address"] = email_address
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if web3_wallet is not UNSET:
            field_dict["web3_wallet"] = web3_wallet
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if password_digest is not UNSET:
            field_dict["password_digest"] = password_digest
        if password_hasher is not UNSET:
            field_dict["password_hasher"] = password_hasher
        if skip_password_checks is not UNSET:
            field_dict["skip_password_checks"] = skip_password_checks
        if skip_password_requirement is not UNSET:
            field_dict["skip_password_requirement"] = skip_password_requirement
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
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_user_json_body_private_metadata import CreateUserJsonBodyPrivateMetadata
        from ..models.create_user_json_body_public_metadata import CreateUserJsonBodyPublicMetadata
        from ..models.create_user_json_body_unsafe_metadata import CreateUserJsonBodyUnsafeMetadata

        d = src_dict.copy()
        external_id = d.pop("external_id", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        email_address = cast(List[str], d.pop("email_address", UNSET))

        phone_number = cast(List[str], d.pop("phone_number", UNSET))

        web3_wallet = cast(List[str], d.pop("web3_wallet", UNSET))

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        password_digest = d.pop("password_digest", UNSET)

        _password_hasher = d.pop("password_hasher", UNSET)
        password_hasher: Union[Unset, CreateUserJsonBodyPasswordHasher]
        if isinstance(_password_hasher, Unset):
            password_hasher = UNSET
        else:
            password_hasher = CreateUserJsonBodyPasswordHasher(_password_hasher)

        skip_password_checks = d.pop("skip_password_checks", UNSET)

        skip_password_requirement = d.pop("skip_password_requirement", UNSET)

        totp_secret = d.pop("totp_secret", UNSET)

        backup_codes = cast(List[str], d.pop("backup_codes", UNSET))

        _public_metadata = d.pop("public_metadata", UNSET)
        public_metadata: Union[Unset, CreateUserJsonBodyPublicMetadata]
        if isinstance(_public_metadata, Unset):
            public_metadata = UNSET
        else:
            public_metadata = CreateUserJsonBodyPublicMetadata.from_dict(_public_metadata)

        _private_metadata = d.pop("private_metadata", UNSET)
        private_metadata: Union[Unset, CreateUserJsonBodyPrivateMetadata]
        if isinstance(_private_metadata, Unset):
            private_metadata = UNSET
        else:
            private_metadata = CreateUserJsonBodyPrivateMetadata.from_dict(_private_metadata)

        _unsafe_metadata = d.pop("unsafe_metadata", UNSET)
        unsafe_metadata: Union[Unset, CreateUserJsonBodyUnsafeMetadata]
        if isinstance(_unsafe_metadata, Unset):
            unsafe_metadata = UNSET
        else:
            unsafe_metadata = CreateUserJsonBodyUnsafeMetadata.from_dict(_unsafe_metadata)

        created_at = d.pop("created_at", UNSET)

        create_user_json_body = cls(
            external_id=external_id,
            first_name=first_name,
            last_name=last_name,
            email_address=email_address,
            phone_number=phone_number,
            web3_wallet=web3_wallet,
            username=username,
            password=password,
            password_digest=password_digest,
            password_hasher=password_hasher,
            skip_password_checks=skip_password_checks,
            skip_password_requirement=skip_password_requirement,
            totp_secret=totp_secret,
            backup_codes=backup_codes,
            public_metadata=public_metadata,
            private_metadata=private_metadata,
            unsafe_metadata=unsafe_metadata,
            created_at=created_at,
        )

        return create_user_json_body
