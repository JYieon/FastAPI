# CORS(Cross Origin Resource Sharing)
# 백엔드와 프론트엔드의 Origin이 다를 때 생기는 상황

# Orgin이란 protocol + domain + prot
# http://127.0.0.1:8000/ <- 이런거
# 프론트, 백엔드가 localhost에 있어도, 포트번호가 다르면 다른 Origin이다.

# CORS를 허가하기 위해 fastapi에서는 CORSMiddleware를 사용한다.
# 사용법
# CORSMiddleware import
# allowed origins 리스트를 string list로 만든다.
# 위 사항들을 FastAPI application에 추가

# 백엔드에 추가할 수 있는 사항
# Credentials 허락여부(Authorization headers, Cookies, etc)
# HTTP methods(POST, PUT), 다 허락하려면 와일드카드 "*" 사용
# 특정 HTTP 헤더, 전부 다 허락하려면 와일드카드 "*" 사용

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 허락할 origin 리스트
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

# 미들웨어 등록, credential이랑 httpmethod, header 허락 여부 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.get("/")
async def main():
    return {"message": "Hello World"}

# CORS<iddleware에 사용되는 파라미터들
# allow_origins : CORS를 허락해줄 rogin들의 리스트
# allow_origin_regex : 정규식으로 표현된 origin들
# allow_methods : HTTP 메소드 허락 목록. default로 ['GET']
# allow_headers : 허락될 HTTP header 리스트
    #  여기서 Accept, Accept-Language, Content-Language, Content-Type 헤더들은 CORS 리퀘스트에서 항상 허락된다.
# allow_credentials : 쿠키가 CORS 지원이 되는지 나타낸다. 기본값은 False
    # False일 경우 allow_origins에 와일드카드 사용불가.
# expose_headers : 브라우저에서 액세스 가능하도록 만들어야 하는 헤더들. 기본값은 텅빈 리스트[]
# max_age : 브라우저가 CORS 응답을 caching할 최대 시간을 설정. 기본값은 600초