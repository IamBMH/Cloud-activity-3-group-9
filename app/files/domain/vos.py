from pydantic import BaseModel
from typing import Optional


class FileVO(BaseModel):
    file_id: str
    owner_email: str
    filename: str
    description: Optional[str] = None