# Middleware
# 모든 request에 대해 path operaiton이 수행되기전 실행되는 함수
# 또한 모든 response에 대해서도 reponse를 return해 주기 전에 실행되는 함수
# => 프론트엔드와 백엔드 사이에서 일하는 놈

# 미들웨어가 받는 파라미터
# request
# call_next: 함수이고 request를 파라미터로 받는다.
# 그리고 이 함수는 request를 path operation에 넘긴다
# 마지막으로 path operation에 의한 response를 리턴
# 리턴받은 response를 유저에게 넘겨주기 전에 어떠한 작업을 수행할 수 있다.

import time
from fastapi import FastAPI, Request 

app = FastAPI()

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

# 위 예제는 request의 수행시간을 측정하여 커스텀 헤더에 넣어서 유저에 전달해주는 예제