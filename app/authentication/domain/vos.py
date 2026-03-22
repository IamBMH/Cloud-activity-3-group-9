from dataclasses import dataclass

@dataclass
class UserBO:
    id: int
    email: str
    password: str