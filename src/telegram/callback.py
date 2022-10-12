from fastapi import FastAPI, Depends
from sqlalchemy.future import select
from src.telegram.common.db.models.user import User
from src.telegram.common.db.base import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from src.telegram.schemas.messages import MessageBodyModel

telegram = FastAPI()


@telegram.post("/webhook")
async def callback(event: MessageBodyModel, db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(User))
    item = result.scalars().all()

    print(item)

