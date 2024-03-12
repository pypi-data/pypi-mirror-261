from enum import Enum


class CreateUserJsonBodyPasswordHasher(str, Enum):
    ARGON2I = "argon2i"
    ARGON2ID = "argon2id"
    BCRYPT = "bcrypt"
    BCRYPT_SHA256_DJANGO = "bcrypt_sha256_django"
    MD5 = "md5"
    PBKDF2_SHA1 = "pbkdf2_sha1"
    PBKDF2_SHA256 = "pbkdf2_sha256"
    PBKDF2_SHA256_DJANGO = "pbkdf2_sha256_django"
    SCRYPT_FIREBASE = "scrypt_firebase"

    def __str__(self) -> str:
        return str(self.value)
