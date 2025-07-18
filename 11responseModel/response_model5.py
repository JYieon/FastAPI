# response model도 list와 dict 값을 가질 수 있다.

from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str

items = [
    {"name": "Foo", "description": "There comes my hero"},
    {"name": "Red", "description": "It's my aeroplane"},
]

@app.get("/items", response_model=List[Item])
async def read_items():
    return items

# from typing import Dict 
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/keyword-weights/", response_model=Dict[str, float])
# async def read_keyword_weights():
#     return {"foo": 2.3, "bar": 3.4}