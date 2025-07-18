# Multiple Models
# 각 케이스마다 모델을 따로 작성
# 아래 코드는 비효율적(중복된 내용 많음, 코드 관리 어려움) => reduceDuplication.py

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None

class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: Optional[str] = None

def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password

def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")
    print(user_in_db)
    return user_in_db

@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved


# **user_in.dict()

# dict()함수는 모델을 사전형으로 형변환 해주어 리턴해주는 함수
# user_in = UserIn(username="john", password="secret", email="john.doe@example.com")
# user_dict = user_in.dict()
# print(user_dict)
# {
#     'username': 'john',
#     'password': 'secret',
#     'email': 'john.doe@example.com'
#     'full_name': None,
# }

# 만약 dict를 함수에 **user_in.dict형태로 전달하면 파이썬은 이를 unwrap한 뒤 key-value argument로 전달한다.
# UserInDB(**user_dict)
# 아래와 동일
# UserInDB(
#     username="john",
#     password="secret",
#     email="john.doe@example.com",
#     full_name=None,
# )
# 좀 더 정확한 코드
# UserInDB(
#     username = user_dict["username"],
#     password = user_dict["password"],
#     email = user_dict["email"],
#     full_name = user_dict["full_name"],
# )

# extra keywords 추가 가능
# UserInDB(**user_in.dict(), hashed_password=hashed_password)