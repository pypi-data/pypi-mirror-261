from enum import Enum


class OTPStrategy(str, Enum):
    EMAIL_CODE = "email_code"
    PHONE_CODE = "phone_code"

    def __str__(self) -> str:
        return str(self.value)
