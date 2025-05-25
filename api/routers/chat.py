from fastapi import APIRouter

import api.schemas.chat as chat_schema

router = APIRouter()


@router.get("/chats", response_model=list[chat_schema.Chat])
async def list_chats() -> list[chat_schema.Chat]:
    return [chat_schema.Chat(user_name="AA", message="Message")]
