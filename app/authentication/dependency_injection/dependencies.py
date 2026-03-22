from app.authentication.persistence.repositories import PostgresUserRepository, PostgresTokenRepository
from app.authentication.domain.services import HashingService
from app.authentication.domain.controllers import RegisterController, LoginController, LogoutController, IntrospectController

user_repository = PostgresUserRepository()
token_repository = PostgresTokenRepository()
hashing_service = HashingService()

register_controller = RegisterController(user_repository, hashing_service)
login_controller = LoginController(user_repository, token_repository, hashing_service)
logout_controller = LogoutController(token_repository)
introspect_controller = IntrospectController(user_repository, token_repository)