# File
# File클래스는 Form 클래스를 상속한다. => file들은 dorm data로 업로드됨
# Query, Path, File 그리고 다른 fastapi 클래스를 임포트할 때, 이들은 사실 클래스를 리턴하는 함수임을 기억하기

from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename" : file.filename}
