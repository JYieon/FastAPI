from typing import List, Optional
from fastapi import FastAPI, Query 

app = FastAPI()

@app.get("/items")
# async def read_items(q: Optional[List[str]] = Query(None)):
# list 자료형 사용 가능
# async def read_items(q: list = Query([])): 
async def read_items(q: List[str] = Query(["foo", "bar"])):
    query_items = {"q": q}
    return query_items

# 'http://127.0.0.1:8000/items?q=ddd&q=dsasd&q=sdf
# 여러개의 값을 줄 수 있다.