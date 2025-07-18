from typing import List, Optional
from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass 

class Item(ItemBase):
    id: int
    owner_id: int
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str 

class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True

# orm_mode가 켜지면 dict 자료형이 아닌데도 dict처럼 값을 읽게 해주고 SQLAlchemy의 ORM모델처럼 사용할 수 있게 해준다.
