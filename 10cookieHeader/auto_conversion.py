# 대부분 헤더들은 하이픈 문자(-)로 분리되어 하이픈 문자는 변수 선언x
# 그래서 Header클래스는 undersocre(_)를 하이픈(-)으로 바꿔주고 헤더를 만든다.
# => ads_id 파라미터 <- ads-id 쿠키에서 값을 가져옴
# 만약 auto conversion을 diable 하고 싶을 경우 conver_underscorres를 false로 지정

from typing import Optional
from fastapi import Header, FastAPI

app = FastAPI()

@app.get("/items/")
async def read_items(
    strange_header: Optional[str] = Header(None, convert_underscores=False)
):
    return {"strange_header": strange_header}

