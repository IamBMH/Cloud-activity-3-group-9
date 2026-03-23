from app.authentication.persistence.repositories import (
    PostgresUserRepository,
    PostgresTokenRepository,
)
from app.authentication.domain.services import HashingService
from app.authentication.domain.controllers import (
    RegisterController,
    LoginController,
    LogoutController,
    IntrospectController,
)

# INSTANCIAS (singletons) 
user_repository = PostgresUserRepository()
token_repository = PostgresTokenRepository()
hashing_service = HashingService()

register_controller = RegisterController(user_repository, hashing_service)
login_controller = LoginController(user_repository, token_repository, hashing_service)
logout_controller = LogoutController(token_repository)
introspect_controller = IntrospectController(user_repository, token_repository)


# DEPENDENCIES PARA FASTAPI 
def get_register_controller():
    return register_controller


def get_login_controller():
    return login_controller


def get_logout_controller():
    return logout_controller


def get_introspect_controller():
    return introspect_controller


class AuthService:
    def __init__(self, introspect_controller):
        self.introspect_controller = introspect_controller

    async def verify_token(self, token: str) -> str:
        user = await self.introspect_controller(token)
        return user.email


auth_service = AuthService(introspect_controller)


def get_auth_service():
    return auth_service