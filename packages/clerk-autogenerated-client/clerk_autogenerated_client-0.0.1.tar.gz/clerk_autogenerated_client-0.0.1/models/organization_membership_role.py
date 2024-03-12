from enum import Enum


class OrganizationMembershipRole(str, Enum):
    ADMIN = "admin"
    BASIC_MEMBER = "basic_member"

    def __str__(self) -> str:
        return str(self.value)
