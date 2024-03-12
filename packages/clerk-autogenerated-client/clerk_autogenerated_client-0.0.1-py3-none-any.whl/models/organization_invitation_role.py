from enum import Enum


class OrganizationInvitationRole(str, Enum):
    ADMIN = "admin"
    BASIC_MEMBER = "basic_member"

    def __str__(self) -> str:
        return str(self.value)
