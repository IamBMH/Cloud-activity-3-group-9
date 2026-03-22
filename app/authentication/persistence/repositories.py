from tortoise.exceptions import IntegrityError
from app.authentication.domain.interfaces import UserRepository, TokenRepository
from app.authentication.domain.vos import UserBO, TokenBO
from app.authentication.domain.exceptions import UserAlreadyExistsException
from app.authentication.models import User, Token

class PostgresUserRepository(UserRepository):
    async def create(self, username: str, email: str, address: str | None, hashed_password: str) -> UserBO:
        try:
            user_model = await User.create(
                username=username, 
                email=email, 
                address=address, 
                hashed_password=hashed_password
            )
            return UserBO(
                id=user_model.id, 
                username=user_model.username,
                email=user_model.email,
                address=user_model.address,
                hashed_password=user_model.hashed_password
            )
        except IntegrityError:
            raise UserAlreadyExistsException()

    async def get_by_email(self, email: str) -> UserBO | None:
        user_model = await User.get_or_none(email=email)
        if user_model:
            return UserBO(
                id=user_model.id, 
                username=user_model.username,
                email=user_model.email,
                address=user_model.address,
                hashed_password=user_model.hashed_password
            )
        return None

    async def get_by_id(self, user_id: int) -> UserBO | None:
        user_model = await User.get_or_none(id=user_id)
        if user_model:
            return UserBO(
                id=user_model.id, 
                username=user_model.username,
                email=user_model.email,
                address=user_model.address,
                hashed_password=user_model.hashed_password
            )
        return None

class PostgresTokenRepository(TokenRepository):
    async def create(self, token: str, user_id: int) -> TokenBO:
        token_model = await Token.create(token=token, user_id=user_id)
        return TokenBO(token=token_model.token, user_id=token_model.user_id)

    async def get_by_token(self, token: str) -> TokenBO | None:
        token_model = await Token.get_or_none(token=token)
        if token_model:
            return TokenBO(token=token_model.token, user_id=token_model.user_id)
        return None

    async def delete(self, token: str) -> None:
        token_model = await Token.get_or_none(token=token)
        if token_model:
            await token_model.delete()