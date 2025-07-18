from typing import Annotated
from fastapi import Header, HTTPException 

async def get_token_header(x_token: Annotated[str, Header()]):
    is x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400. detail="X-Token header invlid")

async def get_query_token(token: str):
    if token != "jessica": 
        raise HTTPException(status_code=400, detail="No Jessica token provided")