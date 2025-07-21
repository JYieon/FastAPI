# Backgroud 작업
# 의존성 주입
# FastAPI는 각 경우에 수행할 작업과 동일한 객체를 내부적으로 재사용하기에, 모든 백그라운드 작업이 함께 병합되고 나중에 백그라운드에서 실행됩니다.

from typing import Union
from fastapi import BackgroundTasks, Depends, FastAPI

app = FastAPI()

def write_log(message: str):
    with open("log.txt", mode="a") as log:
        log.write(message)

def get_query(background_tasks: BackgroundTasks, q: Union[str, None] = None):
    if q:
        message = f"found query: {q}\n"
        background_tasks.add_task(write_log, message)
    return q 

@app.post("/send-notification/{email}")
async def send_notification(
    email: str, background_tasks: BackgroundTasks, q: str = Depends(get_query)
):
    message = f"message to {email}\n"
    background_tasks.add_task(write_log, message)
    return {"message": "Message sent"}