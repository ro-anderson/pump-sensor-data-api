from typing import Dict
from fastapi import FastAPI
import uvicorn
from src.infra.v1 import routes
import pandas as pd

app = FastAPI()

@app.get("/")
def read_root() -> Dict:
    """Root request"""
    return {"if local swagger ui at:": "http://localhost:5001/docs"}

app.include_router(routes.router, prefix="/v1")

if __name__ == '__main__':

    uvicorn.run(app, host="0.0.0.0", port=5001)
