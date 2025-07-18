# Dependency Injection
# 코드의 재활용을 위해 제공해주는 fastapi의 기능
# 클래스 디펜던시도 가능

from typing import Optional
from fastapi import Depends, FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

class CommonQueryParams:
    def __init__(self, q: Optional[str] = None, skip: int = 0, limit: int = 100):
        self.q = q 
        self.skip = skip
        self.limit = limit

@app.get("/items/")
# async def read_items(commons: CommonQueryParams = Depends(CommonQueryParams)):
# fastapi가 제공하는 shortcut. 알아서 Depends가 CommonQueryParams 인스턴스를 만들어 리턴해준다.
async def read_items(commons: CommonQueryParams = Depends()):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items": items})
    return response
