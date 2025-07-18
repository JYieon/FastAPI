# HTTPException 클래스를 이용하여 에러를 일으킬 수 있다.
# raise 이용
# exception이 일어날 경우 리퀘스트는 그 자리에서 바로 종료되며 이후 코드는 동작하지 않고 클라이언트에게 HTTP error를 전달

from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404, 
            detail="Item not found",
            # 커스텀 헤더 추가(Response Header에 추가됨)
            headers={"X-Error": "there goes my error"}, 
        )
    return {"item": items[item_id]}