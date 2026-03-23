import uuid

from app.files.domain.vos import FileVO


class FileController:
    def __init__(self, file_repo, auth_service):
        self.file_repo = file_repo
        self.auth_service = auth_service

    async def create_file(self, token: str, filename: str, description: str | None):
        user_email = await self.auth_service.verify_token(token)

        file_vo = FileVO(
            file_id=str(uuid.uuid4()),
            owner_email=user_email,
            filename=filename,
            description=description,
        )

        await self.file_repo.create_file(file_vo)
        return file_vo.file_id

    async def get_files(self, token: str):
        user_email = await self.auth_service.verify_token(token)
        return await self.file_repo.get_files_by_user(user_email)