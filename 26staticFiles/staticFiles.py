# StaticFiles
# 디렉토리에서 정적 파일을 자동으로 제공

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles 

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")