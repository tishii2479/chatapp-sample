from pydantic import BaseModel


class Chat(BaseModel):
    user_name: str
    message: str
