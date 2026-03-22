from abc import ABC, abstractmethod
from typing import Optional
from app.authentication.domain.vos import UserBO, TokenBO

class UserRepository(ABC):
    @abstractmethod
    async def create(self, username: str, email: str, address: Optional[str], hashed_password: str) -> UserBO:
        pass

    @abstractmethod
    async def get_by_email(self, email: str) -> Optional[UserBO]:
        pass

    @abstractmethod
    async def get_by_id(self, user_id: int) -> Optional[UserBO]:
        pass

class TokenRepository(ABC):
    @abstractmethod
    async def create(self, token: str, user_id: int) -> TokenBO:
        pass

    @abstractmethod
    async def get_by_token(self, token: str) -> Optional[TokenBO]:
        pass

    @abstractmethod
    async def delete(self, token: str) -> None:
        pass