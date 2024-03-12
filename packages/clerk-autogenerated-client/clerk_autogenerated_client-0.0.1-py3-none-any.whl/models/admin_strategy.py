import logging
from enum import Enum

logger = logging.getLogger(__name__)


class AdminStrategy(str, Enum):
    ADMIN = "admin"
    FROM_OAUTH_GOOGLE = "from_oauth_google"
    EMAIL_LINK = "email_link"
    OTHER = "other"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value):
        logger.warning(f"Unknown AdminStrategy: {value} in {cls.__name__}")
        return cls.OTHER
