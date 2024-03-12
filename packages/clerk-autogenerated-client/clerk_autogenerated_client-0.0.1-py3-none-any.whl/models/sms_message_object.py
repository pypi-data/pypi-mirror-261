from enum import Enum


class SMSMessageObject(str, Enum):
    SMS_MESSAGE = "sms_message"

    def __str__(self) -> str:
        return str(self.value)
