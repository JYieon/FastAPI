from typing import Optional, Set
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = []
    image: Optional[Image] = None

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

# 하나의 모델은 다른 모델 안에 nested 될 수 있다.

# Special Type의 Field 
# url 경로 타입 str -> HttpUrl
# "str" -> "https://example.com/"

# Model을 List 타입으로 강제화
# images: Optional[List[Image]] = None