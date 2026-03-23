from typing import Optional

from fastapi import APIRouter, Depends, Header
from pydantic import BaseModel

from app.files.dependency_injection.dependencies import get_file_controller

router = APIRouter()


class FileInput(BaseModel):
    filename: str
    description: Optional[str] = None


@router.post("")
async def create_file(
    input: FileInput,
    auth: str = Header(..., alias="Auth"),
    controller=Depends(get_file_controller),
):
    file_id = await controller.create_file(
        token=auth,
        filename=input.filename,
        description=input.description,
    )
    return {"status": "ok", "file_id": file_id}


@router.get("")
async def get_files(
    auth: str = Header(..., alias="Auth"),
    controller=Depends(get_file_controller),
):
    files = await controller.get_files(token=auth)
    return {"files": files}


@router.get("/{file_id}")
async def get_file_by_id(file_id: str):
    return {"status": "pending phase 3"}


@router.post("/{file_id}")
async def upload_file_content(file_id: str):
    return {"status": "pending phase 3"}


@router.delete("/{file_id}")
async def delete_file(file_id: str):
    return {"status": "pending phase 3"}


@router.post("/merge")
async def merge_files():
    return {"status": "pending phase 3"}