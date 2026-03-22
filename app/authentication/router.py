from fastapi import APIRouter, HTTPException, status, Header
from pydantic import BaseModel
from typing import Optional
from app.authentication.dependency_injection.dependencies import (
    register_controller, 
    login_controller, 
    logout_controller, 
    introspect_controller
)
from app.authentication.domain.exceptions import (
    UserAlreadyExistsException, 
    UserNotFoundException, 
    InvalidCredentialsException, 
    InvalidTokenException
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
    address: Optional[str]

@router.post("/register")
async def register(input_data: RegisterInputDTO):
    try:
        await register_controller(
            username=input_data.username,
            email=input_data.email,
            address=input_data.address,
            password=input_data.password
        )
        return {"status": "ok"}
    except UserAlreadyExistsException:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)

@router.post("/login")
async def login(input_data: LoginInputDTO):
    try:
        token = await login_controller(
            email=input_data.email,
            password=input_data.password
        )
        return {"auth": token}
    except UserNotFoundException:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    except InvalidCredentialsException:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

@router.post("/logout")
async def logout(auth: str = Header()):
    try:
        await logout_controller(token=auth)
        return {"status": "ok"}
    except InvalidTokenException:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

@router.get("/introspect", response_model=IntrospectOutputDTO)
async def introspect(auth: str = Header()):
    try:
        user_bo = await introspect_controller(token=auth)
        return IntrospectOutputDTO(
            username=user_bo.username,
            email=user_bo.email,
            address=user_bo.address
        )
    except InvalidTokenException:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    except UserNotFoundException:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)