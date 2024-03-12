import logging
from enum import Enum

logger = logging.getLogger(__name__)


class IdentificationLinkType(str, Enum):
    OAUTH_GOOGLE = "oauth_google"
    OATH_MICROSOFT = "oauth_microsoft"
    SAML = "saml"
    OTHER = "other"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value):
        logger.warning(f"Unknown IdentificationLinkType: {value} in {cls.__name__}")
        return cls.OTHER
