from abc import ABC, abstractmethod
from typing import List, Optional

from app.files.domain.vos import FileVO


class FileRepositoryInterface(ABC):
    @abstractmethod
    async def create_file(self, file_vo: FileVO) -> None:
        pass

    @abstractmethod
    async def get_files_by_user(self, owner_email: str) -> List[FileVO]:
        pass

    @abstractmethod
    async def get_file_by_id(self, file_id: str) -> Optional[FileVO]:
        pass

    @abstractmethod
    async def delete_file(self, file_id: str) -> None:
        pass