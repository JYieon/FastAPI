# FastAPI의 HTTP exception을 가지고 있고 이것은 Startlette's의 Exception을 상속 받는다.
# 차이점은 FastAPI's HTTPException은 response에 헤더를 추가할 수 있다는 것
# 주의할 점은 exception handler를 등록할 때 starlette의 HTTPException에다가 등록해야 한다.

from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return {"item_id": item_id}