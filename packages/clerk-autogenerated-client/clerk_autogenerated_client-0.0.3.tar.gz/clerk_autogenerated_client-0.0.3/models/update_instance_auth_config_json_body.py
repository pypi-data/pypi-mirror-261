from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..livtypes import UNSET, Unset

T = TypeVar("T", bound="UpdateInstanceAuthConfigJsonBody")


@attr.s(auto_attribs=True)
class UpdateInstanceAuthConfigJsonBody:
    """
    Attributes:
        restricted_to_allowlist (Union[Unset, None, bool]): Whether sign up is restricted to email addresses, phone
            numbers and usernames that are on the allowlist.
        from_email_address (Union[Unset, None, str]): The local part of the email address from which authentication-
            related emails (e.g. OTP code, magic links) will be sent.
            Only alphanumeric values are allowed.
            Note that this value should contain only the local part of the address (e.g. `foo` for `foo@example.com`).
        progressive_sign_up (Union[Unset, None, bool]): Enable the Progressive Sign Up algorithm. Refer to the
            [docs](https://clerk.com/docs/upgrade-guides/progressive-sign-up) for more info.
        session_token_template (Union[Unset, None, str]): The name of the JWT Template used to augment your session
            tokens. To disable this, pass an empty string.
        enhanced_email_deliverability (Union[Unset, None, bool]): The "enhanced_email_deliverability" feature will send
            emails from "verifications@clerk.dev" instead of your domain.
            This can be helpful if you do not have a high domain reputation.
        test_mode (Union[Unset, None, bool]): Toggles test mode for this instance, allowing the use of test email
            addresses and phone numbers.
            Defaults to true for development instances.
    """

    restricted_to_allowlist: Union[Unset, None, bool] = False
    from_email_address: Union[Unset, None, str] = UNSET
    progressive_sign_up: Union[Unset, None, bool] = UNSET
    session_token_template: Union[Unset, None, str] = UNSET
    enhanced_email_deliverability: Union[Unset, None, bool] = UNSET
    test_mode: Union[Unset, None, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        restricted_to_allowlist = self.restricted_to_allowlist
        from_email_address = self.from_email_address
        progressive_sign_up = self.progressive_sign_up
        session_token_template = self.session_token_template
        enhanced_email_deliverability = self.enhanced_email_deliverability
        test_mode = self.test_mode

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if restricted_to_allowlist is not UNSET:
            field_dict["restricted_to_allowlist"] = restricted_to_allowlist
        if from_email_address is not UNSET:
            field_dict["from_email_address"] = from_email_address
        if progressive_sign_up is not UNSET:
            field_dict["progressive_sign_up"] = progressive_sign_up
        if session_token_template is not UNSET:
            field_dict["session_token_template"] = session_token_template
        if enhanced_email_deliverability is not UNSET:
            field_dict["enhanced_email_deliverability"] = enhanced_email_deliverability
        if test_mode is not UNSET:
            field_dict["test_mode"] = test_mode

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        restricted_to_allowlist = d.pop("restricted_to_allowlist", UNSET)

        from_email_address = d.pop("from_email_address", UNSET)

        progressive_sign_up = d.pop("progressive_sign_up", UNSET)

        session_token_template = d.pop("session_token_template", UNSET)

        enhanced_email_deliverability = d.pop("enhanced_email_deliverability", UNSET)

        test_mode = d.pop("test_mode", UNSET)

        update_instance_auth_config_json_body = cls(
            restricted_to_allowlist=restricted_to_allowlist,
            from_email_address=from_email_address,
            progressive_sign_up=progressive_sign_up,
            session_token_template=session_token_template,
            enhanced_email_deliverability=enhanced_email_deliverability,
            test_mode=test_mode,
        )

        return update_instance_auth_config_json_body
