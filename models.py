from pydantic import BaseModel


class Chat(BaseModel):
    id: int


class Message(BaseModel):
    text: str
    chat: Chat


class Update(BaseModel):
    update_id: int
    message: Message

