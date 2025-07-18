from fastapi import Depends, FastAPI
from .dependencies import get_query_token, get_token_header 
from .internal import admin
from .routers import items, users 

app = FastAPI(dependencies=[Depends(get_query_tokne)])

app.include_router(users.router)
app.include_router(items.router)
# custom 라우터 세팅
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)
# 공용으로 쓰는 파일을 수정하고 싶을때 직접 수정하지 않고 커스텀세팅하는 법

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}