import uvicorn
import asyncio
from fastapi import FastAPI
from routing import create_routing
from src.telegram.items.modules import set_webhook

app = FastAPI()

create_routing(app)

if __name__ == "__main__":
    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(set_webhook())

    uvicorn.run(app, host="0.0.0.0", port=80)
