from fastapi import FastAPI, Request
from src.telegram.schemas.messages import MessageBodyModel

telegram = FastAPI()


@telegram.post("/webhook")
async def callback(event: MessageBodyModel):
    print(event)
