# response status code 직접 지정 가능
# 역할
# response에 status code 지정
# docs에 status code 표시

from fastapi import FastAPI

app = FastAPI()

@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}

# shortcut로 status code 지정 가능
# status_code=status.HTTP_201_CREATED