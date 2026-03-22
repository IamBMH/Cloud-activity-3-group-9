from abc import ABC, abstractmethod
from typing import Optional
from app.authentication.domain.vos import UserBO

class UserRepository(ABC):
    @abstractmethod
    async def create(self, email: str, password: str) -> UserBO:
        pass

    @abstractmethod
    async def get_by_email(self, email: str) -> Optional[UserBO]:
        pass