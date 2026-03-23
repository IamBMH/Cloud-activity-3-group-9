from typing import Optional

from fastapi import APIRouter, Depends, Header, HTTPException, status
from pydantic import BaseModel

from app.authentication.dependency_injection.dependencies import (
    get_register_controller,
    get_login_controller,
    get_logout_controller,
    get_introspect_controller,
)
from app.authentication.domain.exceptions import (
    UserAlreadyExistsException,
    UserNotFoundException,
    InvalidCredentialsException,
    InvalidTokenException,
)

router = APIRouter(tags=["Authentication"])


class RegisterInputDTO(BaseModel):
    username: str
    email: str
    address: Optional[str] = None
    password: str


class LoginInputDTO(BaseModel):
    email: str
    password: str


class IntrospectOutputDTO(BaseModel):
    username: str
    email: str
    address: Optional[str] = None


@router.post("/register")
async def register(
    input_data: RegisterInputDTO,
    controller=Depends(get_register_controller),
):
    try:
        user_bo = await controller(
            username=input_data.username,
            email=input_data.email,
            address=input_data.address,
            password=input_data.password,
        )
        return {
            "status": "ok",
            "id": user_bo.id,
            "username": user_bo.username,
            "email": user_bo.email,
        }
    except UserAlreadyExistsException:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exists",
        )


@router.post("/login")
async def login(
    input_data: LoginInputDTO,
    controller=Depends(get_login_controller),
):
    try:
        token = await controller(
            email=input_data.email,
            password=input_data.password,
        )
        return {"auth": token}
    except UserNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    except InvalidCredentialsException:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )


@router.post("/logout")
async def logout(
    auth: str = Header(..., alias="Auth"),
    controller=Depends(get_logout_controller),
):
    try:
        await controller(token=auth)
        return {"status": "ok"}
    except InvalidTokenException:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )


@router.get("/introspect", response_model=IntrospectOutputDTO)
async def introspect(
    auth: str = Header(..., alias="Auth"),
    controller=Depends(get_introspect_controller),
):
    try:
        user_bo = await controller(token=auth)
        return IntrospectOutputDTO(
            username=user_bo.username,
            email=user_bo.email,
            address=user_bo.address,
        )
    except InvalidTokenException:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )
    except UserNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )