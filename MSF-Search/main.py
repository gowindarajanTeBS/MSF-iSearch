# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/


# from fastapi import FastAPI
# app = FastAPI()
#
# @app.get("/")
# def first_example():
# 	"""
# 	GFG Example First Fast API Example
# 	"""
# 	return {"GFG Example": "FastAPI"}





from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    payload: dict

@app.post("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    if item.id != item_id:
        raise HTTPException(status_code=400, detail="Item ID mismatch")
    return {"item_id": item.id, "payload": item.payload}

class search_item(BaseModel):
    id: int
    search_term: str

@app.post("/search/")
async def search_item(item_id: int, search_ip: search_item):
    if search_ip.id != item_id:
        raise HTTPException(status_code=400, detail="Item ID mismatch")
    return {"item_id": search_ip.id, "search_payload": search_ip.search_term}

