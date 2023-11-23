from pydantic import BaseModel
from typing import List

# region Constants and Variables

# endregion
# region Classes
class SimpleObject(BaseModel):
    id: int
    score: float

class NestedObject(BaseModel):
    id: int
    simples: List[SimpleObject]
    best: SimpleObject
# endregion