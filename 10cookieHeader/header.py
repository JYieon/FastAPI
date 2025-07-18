from typing import Optional
from fastapi import Header, FastAPI

app = FastAPI()

@app.get("/items/")
async def read_items(user_agent: Optional[str] = Header(None)):
    return {"User-Agent": user_agent}

# Request URL
# http://127.0.0.1:8000/items/

# Curl
# curl -X 'GET' \
#   'http://127.0.0.1:8000/items/' \
#   -H 'accept: application/json' \
#   -H 'user-agent: jiyeon'

# Response body
# {
#   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
# }