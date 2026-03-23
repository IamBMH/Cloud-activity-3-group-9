import uuid

from app.authentication.domain.interfaces import UserRepository, TokenRepository
from app.authentication.domain.services import HashingService
from app.authentication.domain.exceptions import (
    UserAlreadyExistsException,
    UserNotFoundException,
    InvalidCredentialsException,
    InvalidTokenException,
)
from app.authentication.domain.vos import UserBO


class RegisterController:
    def __init__(self, user_repository: UserRepository, hashing_service: HashingService):
        self.user_repository = user_repository
        self.hashing_service = hashing_service

    async def __call__(self, username: str, email: str, address: str | None, password: str) -> UserBO:
        existing = await self.user_repository.get_by_email(email)
        if existing:
            raise UserAlreadyExistsException()

        hashed_password = self.hashing_service.hash_password(email, password)
        return await self.user_repository.create(
            username=username,
            email=email,
            address=address,
            hashed_password=hashed_password,
        )


class LoginController:
    def __init__(
        self,
        user_repository: UserRepository,
        token_repository: TokenRepository,
        hashing_service: HashingService,
    ):
        self.user_repository = user_repository
        self.token_repository = token_repository
        self.hashing_service = hashing_service

    async def __call__(self, email: str, password: str) -> str:
        user_bo = await self.user_repository.get_by_email(email)
        if not user_bo:
            raise UserNotFoundException()

        hashed_password = self.hashing_service.hash_password(email, password)
        if hashed_password != user_bo.hashed_password:
            raise InvalidCredentialsException()

        new_token = str(uuid.uuid4())
        await self.token_repository.create(token=new_token, user_id=user_bo.id)
        return new_token


class LogoutController:
    def __init__(self, token_repository: TokenRepository):
        self.token_repository = token_repository

    async def __call__(self, token: str) -> None:
        token_bo = await self.token_repository.get_by_token(token)
        if not token_bo:
            raise InvalidTokenException()
        await self.token_repository.delete(token)


class IntrospectController:
    def __init__(self, user_repository: UserRepository, token_repository: TokenRepository):
        self.user_repository = user_repository
        self.token_repository = token_repository

    async def __call__(self, token: str) -> UserBO:
        token_bo = await self.token_repository.get_by_token(token)
        if not token_bo:
            raise InvalidTokenException()

        user_bo = await self.user_repository.get_by_id(token_bo.user_id)
        if not user_bo:
            raise UserNotFoundException()

        return user_bo