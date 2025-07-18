from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}
    return results

# FastAPI는 RequestBody가 하나밖에 없으면 key값을 생략하고 RequestBody 안의 데이터만 해석하도록 되어있음
# 만약 RequestBody의 key값을 넣어주고 싶다면 embed = True를 이용