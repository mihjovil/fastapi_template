from typing import Union
from pkg.structs import SimpleObject, NestedObject
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/new_nested")
def create_nested(nested: NestedObject):
    print(nested)

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}