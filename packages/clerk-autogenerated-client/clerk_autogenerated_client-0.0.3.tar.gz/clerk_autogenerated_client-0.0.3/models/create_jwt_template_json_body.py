from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..livtypes import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_jwt_template_json_body_claims import CreateJWTTemplateJsonBodyClaims


T = TypeVar("T", bound="CreateJWTTemplateJsonBody")


@attr.s(auto_attribs=True)
class CreateJWTTemplateJsonBody:
    """
    Attributes:
        name (Union[Unset, str]): JWT template name
        claims (Union[Unset, CreateJWTTemplateJsonBodyClaims]): JWT template claims in JSON format
        lifetime (Union[Unset, None, float]): JWT token lifetime
        allowed_clock_skew (Union[Unset, None, float]): JWT token allowed clock skew
        custom_signing_key (Union[Unset, bool]): Whether a custom signing key/algorithm is also provided for this
            template
        signing_algorithm (Union[Unset, None, str]): The custom signing algorithm to use when minting JWTs
        signing_key (Union[Unset, None, str]): The custom signing private key to use when minting JWTs
    """

    name: Union[Unset, str] = UNSET
    claims: Union[Unset, "CreateJWTTemplateJsonBodyClaims"] = UNSET
    lifetime: Union[Unset, None, float] = UNSET
    allowed_clock_skew: Union[Unset, None, float] = UNSET
    custom_signing_key: Union[Unset, bool] = UNSET
    signing_algorithm: Union[Unset, None, str] = UNSET
    signing_key: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        claims: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.claims, Unset):
            claims = self.claims.to_dict()

        lifetime = self.lifetime
        allowed_clock_skew = self.allowed_clock_skew
        custom_signing_key = self.custom_signing_key
        signing_algorithm = self.signing_algorithm
        signing_key = self.signing_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if claims is not UNSET:
            field_dict["claims"] = claims
        if lifetime is not UNSET:
            field_dict["lifetime"] = lifetime
        if allowed_clock_skew is not UNSET:
            field_dict["allowed_clock_skew"] = allowed_clock_skew
        if custom_signing_key is not UNSET:
            field_dict["custom_signing_key"] = custom_signing_key
        if signing_algorithm is not UNSET:
            field_dict["signing_algorithm"] = signing_algorithm
        if signing_key is not UNSET:
            field_dict["signing_key"] = signing_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_jwt_template_json_body_claims import CreateJWTTemplateJsonBodyClaims

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _claims = d.pop("claims", UNSET)
        claims: Union[Unset, CreateJWTTemplateJsonBodyClaims]
        if isinstance(_claims, Unset):
            claims = UNSET
        else:
            claims = CreateJWTTemplateJsonBodyClaims.from_dict(_claims)

        lifetime = d.pop("lifetime", UNSET)

        allowed_clock_skew = d.pop("allowed_clock_skew", UNSET)

        custom_signing_key = d.pop("custom_signing_key", UNSET)

        signing_algorithm = d.pop("signing_algorithm", UNSET)

        signing_key = d.pop("signing_key", UNSET)

        create_jwt_template_json_body = cls(
            name=name,
            claims=claims,
            lifetime=lifetime,
            allowed_clock_skew=allowed_clock_skew,
            custom_signing_key=custom_signing_key,
            signing_algorithm=signing_algorithm,
            signing_key=signing_key,
        )

        create_jwt_template_json_body.additional_properties = d
        return create_jwt_template_json_body

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
