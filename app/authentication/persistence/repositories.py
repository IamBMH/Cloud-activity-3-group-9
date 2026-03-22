from tortoise.exceptions import IntegrityError
from app.authentication.domain.interfaces import UserRepository
from app.authentication.domain.vos import UserBO
from app.authentication.domain.exceptions import UserAlreadyExistsException
from app.authentication.models import User

class PostgresUserRepository(UserRepository):
    async def create(self, email: str, password: str) -> UserBO:
        try:
            user_model = await User.create(email=email, password=password)
            
            return UserBO(
                id=user_model.id, 
                email=user_model.email, 
                password=user_model.password
            )
        except IntegrityError:
            raise UserAlreadyExistsException(f"A user with email {email} already exists.")

    async def get_by_email(self, email: str) -> UserBO | None:
        user_model = await User.get_or_none(email=email)
        if user_model:
            return UserBO(
                id=user_model.id, 
                email=user_model.email, 
                password=user_model.password
            )
        return None