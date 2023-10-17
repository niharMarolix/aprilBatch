from typing import Union, Dict

from fastapi import FastAPI, HTTPException

app = FastAPI()

# Example data storage (in-memory dictionary)
data = {}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/items/")
def create_item(item: Dict):
    item_id = len(data) + 1
    data[item_id] = item
    return {"item_id": item_id, "item": item}
