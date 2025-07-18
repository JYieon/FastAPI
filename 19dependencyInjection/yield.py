#  yield

async def get_db():
    db = DBSession()
    try:    
        yield db
    finally:
        db.close()

# response를 보내기전에 yield 까지의 코드만 실행된다.
# 그리고 response가 전달되면 마지막으로 finally 이후 코드가 수행된다.