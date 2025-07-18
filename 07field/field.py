# Field 클래스
# RequestBody 안에 있는 Metadata를 Feild 클래스로 세세하게 다룰 수 있다.

from typing import List, Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    # tags: list = []
    tags: List[str] = []
    # list 타입 제한

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results