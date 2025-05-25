from pydantic import BaseModel


class UserBase(BaseModel):
    user_name: str


class UserCreate(UserBase):
    pass


class UserCreateResponse(UserBase):
    user_id: int


class User(UserBase):
    user_id: int
