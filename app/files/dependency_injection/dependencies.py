from app.files.domain.controllers import FileController
from app.files.persistence.repositories import FileRepository
from app.authentication.dependency_injection.dependencies import get_auth_service


file_repository = FileRepository()
auth_service = get_auth_service()
file_controller = FileController(file_repository, auth_service)


def get_file_controller():
    return file_controller