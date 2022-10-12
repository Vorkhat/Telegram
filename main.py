import uvicorn
from fastapi import FastAPI
from routing import create_routing


app = FastAPI()

create_routing(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
