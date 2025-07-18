# jsonable_encoder
# 데이터 자료형을 json compatiable한 데이터로 바꿔줌
# 다른 파이썬 라이브러리를 사용할 때 json 호환 데이터를 요구할 경우 사용

from datetime import datetime
from typing import Optional
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

fake_db = {}

class Item(BaseModel):
    title: str
    timestamp: datetime
    description: Optional[str] = None

app = FastAPI()

@app.put("/items/{id}")
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data
    print(fake_db[id])