from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import services.discord_messager as discord_messager

class Message(BaseModel):
    url: str
    description: str
    channel: str | None = None

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/links")
def send_message(message: Message):
    return discord_messager.send_message(message)