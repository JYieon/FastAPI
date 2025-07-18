from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str = Field(..., example="Foo")
    description: Optional[str] = Field(None, example="A very nice Item")
    price: float = Field(..., example=35.4)
    tax: Optional[float] = Field(None, example=3.2)

@app.put("/items/{item_id}")
async def update_item(item_id: int, item:Item):
    results = {"item_id": item_id, "item": item}
    return results

    # 기본값 설정

    # Field(..., ...) => 필수 항목
    # Field(None, ...) + Optional[...] => 선택 항목