# path operation 세팅에 관련된 파라미터
# tags를 설정하면 swagger에서 그룹이 나뉨. 문서화를 위한 코드

from typing import Optional, Set
from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = []

@app.post("/items/", response_model=Item, tags=["items"])
async def create_item(item: Item):
    return item

@app.get("/items/", tags=["items"])
async def read_items():
    return [{"name": "Foo", "price": 42}]

@app.get("/users/", tags=["users"])
async def read_user():
    return [{"username": "johndoe"}]