from typing import Optional
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items")
# ^는 시작값 설정, $는 정규식의 끝마침. 이 뒤로 문자가 올 수 없음
# 아래 예저에서 q값은 fixedquery만 올 수 있다.
# async def read_items(q: Optional[str] = Query(None, min_length=3, max_length=50, regex="^fixedquery$")):


# default value 지정
async def read_items(q: str = Query(..., min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results