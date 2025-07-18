# PUT operation

from typing import List, Optional
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    tax: float = 10.5
    tags: List[str] = []

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items[item_id]

# @app.put("/items/{item_id}", response_model=Item)
# async def update_item(item_id: str, item: Item):
#     update_item_encoded = jsonable_encoder(item)
#     items[item_id] = update_item_encoded
#     return update_item_encoded

# 업데이트 시 기존 데이터가 default값으로 바뀌는 문제
# -> dict()함수에서 exclude_unset 이용
# dict 자료형을 만들어 주면서 unset된 데이터들을 제외해준다.

@app.patch("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    stored_item_data = items[item_id]
    stored_item_model = Item(**stored_item_data)
    update_data = item.dict(exclude_unset=True)
    updated_item = stored_item_model.copy(update=update_data)
    items[item_id] = jsonable_encoder(updated_item)
    return updated_item

# 데이터 업데이트 과정
# 1. PATCH나 PUT operation이용
# 2. 저장된 데이터를 가져온다
# 3. 저장된 데이터를 Pydantic Model로 바꾸어준다
# 4. request data를 dict()로 바꾼다. 바꾼때 exclude_unset 기억하기!
# 5. 저장된 데이터에서 copy()메소드를 이용하여 업데이트된 아이템을 얻는다
# 6. 업데이트된 아이템을 jsonable_encoder를 이용하여 json compatiable 데이터로 변환
# 7. db로 변환된 아이템을 저장
# 8. db 업데이트


# 기본값 적용 시점?
# => 기본값은 모델 생성 시점에 메모리에 적용되지만, exclude_unset=True는 "입력에서 직접 설정된 값만" 골라내기 때문에 기본값 필드는 빠진다.