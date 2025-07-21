# tasting
# 테스트 분리하기
# 같은 위치에 test파일을 만들어서 테스트 코드 분리

from fastapi.testclient import TestClient 
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}