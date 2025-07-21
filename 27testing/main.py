# pip install pytest
# 터미널에 pytest치면 알아서 test됨

from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

@app.get("/")
async def read_main():
    return {"msg": "Hello World"}