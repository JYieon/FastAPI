from typing import Optional
from fastapi import FastAPI, Path, Query

app = FastAPI()

# ge: greater than or equal, 크거나 같다 
# gt: greater than, 크다
# lt: less than, 작다
# le: less than or equal, 작거나 같다

@app.get("/items/{item_id}")
async def read_items(
    *, item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000), q: str, size: float = Query(..., gt=0, lt=10.5)
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

