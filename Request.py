from pydantic import BaseModel
from typing import Any

class RequestModel(BaseModel):
    uid: str
    text: str