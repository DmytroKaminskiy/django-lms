from pydantic import BaseModel



class ZoomEventCreate(BaseModel):
    event_ts: int
    event: str
    payload: dict


# def add(x, y):
#     return x + y

# def add(x: int, y: int) -> int:
#     return x + y
