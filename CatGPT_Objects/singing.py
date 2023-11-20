from pydantic import BaseModel

class Singing(BaseModel):
    send: str
    singer: str
    file: None = None
    