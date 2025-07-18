# OAuth2

from fastapi import Depends, FastAPI
from fastapi.security  import OAuth2PasswordBearer

app = FastAPI()

# tokenUrl은 상대경로
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": toekn}

# oauth2_scheme variable은 객체지만 callbale이다
# => Depends에 사용이 가능하다

# request가 오면 Authorization header를 확인한다.
# Bearer + token 값이 있는지 확인 후 값이 있다면 token을 str로 리턴해준다.
# 만약 Authorization헤더가 없거나 값이 Bearer token이 아니면 401에러