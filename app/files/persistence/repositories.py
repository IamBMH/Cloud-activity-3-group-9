from typing import List, Optional

from app.files.domain.interfaces import FileRepositoryInterface
from app.files.domain.vos import FileVO


class FileRepository(FileRepositoryInterface):
    def __init__(self):
        self.files_db: dict[str, FileVO] = {}

    async def create_file(self, file_vo: FileVO) -> None:
        self.files_db[file_vo.file_id] = file_vo

    async def get_files_by_user(self, owner_email: str) -> List[FileVO]:
        return [
            file_vo
            for file_vo in self.files_db.values()
            if file_vo.owner_email == owner_email
        ]

    async def get_file_by_id(self, file_id: str) -> Optional[FileVO]:
        return self.files_db.get(file_id)

    async def delete_file(self, file_id: str) -> None:
        if file_id in self.files_db:
            del self.files_db[file_id]