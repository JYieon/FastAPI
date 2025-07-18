from datetime import datetime, time, timedelta
from typing import Optional
from uuid import UUID
from fastapi import Body, FastAPI

app = FastAPI()

@app.put("/items/{item_id}")
async def read_items(
    item_id: UUID,
    start_datetime: Optional[datetime] = Body(None),
    end_datetime: Optional[datetime] = Body(None),
    repeat_at: Optional[time] = Body(None),
    process_after: Optional[timedelta] = Body(None),
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }

# UUID(Universally Unique Identifier)
# 많은 DB시스템에서 id로 사용됨. request와 response는 전부 str로 표현
# 형식: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

# datetime.datetime
# str로 표현. ex) 2008-09-15T15:53:00+05:00

# datetime.date
# str로 표현. ex) 2008-09-15

# datetime.time
# str로 표현. ex) 14:23:55.003.

# datetime.timedelta
# float로 표현. Pydantic에서 "ISO 8601 time dfgg encoding"로 표현할 수 있다.

# frozenset
# set으로 취급. 
# request에서 list를 읽은 뒤에 중복된 데이터를 제거하고 set으로 convert 해준다.
# response에서 set 데이터는 list로 convert 된다.
# 생성된 스키마는 JSON Schema의 uniqueltems를 이용하여 set값들을 고유하도록 만든다.

# bytes
# float로 표현. 

# Decimal
# float로 표현.