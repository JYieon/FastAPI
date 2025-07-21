# tasting
# TestClient를 사용하려면 httpx 먼저 설치

from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

@app.get("/")
async def read_main():
    return {"msg": "Hello World"}

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

# 테스트를 위한 함수는 async def가 아니라 def로 작성해야한다.
# 클라이언트에 대한 호출도 await를 사용하지 않는 일반 호출