from typing import Optional
from fastapi import FastAPI, Query
app = FastAPI()

@app.get("/items/")
async def read_items(q: Optional[str] = Query(None, alias="item-query")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bas"}]}
    if q:
        results.update({"q": q})
    return results

# item-query는 파이썬의 변수명을 쿼리 파라미터로 사용 불가
#  fastAPI에서 alias parameter를 통해서는 가능하다