# Backgroud 작업
# 클라이언트에게는 빠르게 응답을 주고, 그 뒤에 필요한 작업은 백그라운드로 처리하는 것이 유용하다.
# 경로 작동 함수에 메게뱐스러 BackgroundTasks
# ex) 작업 수행 후 전송되는 이메일알림, 데이터처리

from fastapi import BackgroundTasks, FastAPI 

app = FastAPI()

def write_notification(email: str, message=""):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)

# 경로 작동 함수
@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent in the background"}

# .add_task(작업함수, 전달 인자, 함수에 전달되어야하는 모든 키워드 인자)