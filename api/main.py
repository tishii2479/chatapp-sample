from fastapi import FastAPI

from api.routers import chat, user

app = FastAPI()
app.include_router(chat.router)
app.include_router(user.router)
