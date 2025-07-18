from typing import Optional
from fastapi import FastAPI, Query

app = FastAPI()

# deprecated
# 어떤 파라미터를 업데이트하거나 관리하기 싫지만, 사용하는 유저가 있을 때 deprecated 표시를 해준다.

@app.get("/items/")
async def read_items(
    q: Optional[str] = Query(
        None,
        alias="item-query",
        title="Query string",
        description="Query string for the items to search in the database that gave a good match",
        min_length=3,
        max_length=50,
        regex="^fixedquery$",

        deprecated=True,
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q: 
        results.update({"q": q})
        return results