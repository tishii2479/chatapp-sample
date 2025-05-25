from fastapi import APIRouter, HTTPException

import api.schemas.user as user_schema

router = APIRouter()


@router.get("/users", response_model=list[user_schema.User])
async def list_users() -> list[user_schema.User]:
    """
    Returns list of users
    """
    return [user_schema.User(user_id=1, user_name="AA")]


@router.post("/users", response_model=user_schema.UserCreateResponse)
async def create_user(user: user_schema.UserCreate) -> user_schema.UserCreateResponse:
    """
    Create a new user.
    ダミーデータとして user_id を 1 にして返す
    """
    user = user_schema.User(user_id=1, **user.model_dump())
    return user_schema.UserCreateResponse(**user.model_dump())


@router.get("/users/{user_id}", response_model=user_schema.User)
async def get_user(user_id: int) -> user_schema.User:
    """
    Retrieve a user by ID.
    """
    if user_id == 1:
        return user_schema.User(user_id=1, user_name="AA")
    raise HTTPException(status_code=404, detail="User not found")


@router.put("/users/{user_id}", response_model=user_schema.User)
async def update_user(user_id: int, updated_user: user_schema.User) -> user_schema.User:
    """
    Update a user's information by ID.
    """
    if user_id == 1:
        updated_user.user_id = 1
        return updated_user
    raise HTTPException(status_code=404, detail="User not found")


@router.delete("/users/{user_id}", response_model=dict)
async def delete_user(user_id: int) -> dict:
    """
    Delete a user by ID.
    """
    if user_id == 1:
        return {"detail": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")
