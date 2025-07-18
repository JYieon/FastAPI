# response_model을 이용해 operation들에 관한 response model 지정

from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item

# response_model이 쓰이는 경우
# 아웃풋 데이터를 response_model에서 지정한 모델로 변환
# reponse에 JSON 스키파 추가
# doc시스템에 사용
