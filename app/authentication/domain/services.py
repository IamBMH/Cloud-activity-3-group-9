import hashlib


class HashingService:
    def hash_password(self, email: str, password: str) -> str:
        raw_value = f"{email}:{password}"
        return hashlib.sha256(raw_value.encode("utf-8")).hexdigest()