from dataclasses import dataclass
from typing import Optional

@dataclass
class UserBO:
    id: int
    username: str
    email: str
    address: Optional[str]
    hashed_password: str

@dataclass
class TokenBO:
    token: str
    user_id: int