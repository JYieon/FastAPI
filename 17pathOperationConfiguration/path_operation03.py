# path operation 세팅에 관련된 파라미터
# summary와 escription 추가

from typing import Optional, Set
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = []

@app.post(
    "/items/",
    response_model=Item,
    summary="Create an item",
    description="Create an item sith all the information, name, description, price, tax and set of unique tags",
)
async def create_item(item: Item):
    return item