# Sub Dependency
# 디펜던시의 디펜던시 만들기
# 원하는 만큼 deep하게 만들 수 있다.

from typing import Optional
from fastapi import Depends, FastAPI, Cookie

app = FastAPI()

# 디펜던시의 디펜던시 만들기
def query_extractor(q: Optional[str] = None):
    return q

# 디펜던시의 디펜던시가 될 함수를 디펜던시 함수에 연결
# 먼저 query_extractor에서 뭐리 파라미터 q를 가져오고
# 없으면 쿠키(last_query) 값을 대신 사용
def query_or_cookie_extractor(
    q: str = Depends(query_extractor), last_query: Optional[str] = Cookie(None)
):
    if not q:
        return last_query
    return q

# path operation 연결
@app.get("/items/")
async def read_query(query_or_default: str = Depends(query_or_cookie_extractor)):
    return {"q_or_cookie": query_or_default}