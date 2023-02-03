#
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
#
# app = FastAPI()
#
# class Item(BaseModel):
#     id: int
#     payload: dict
#
# @app.post("/items/{item_id}")
# async def create_item(item_id: int, item: Item):
#     if item.id != item_id:
#         raise HTTPException(status_code=400, detail="Item ID mismatch")
#     return {"item_id": item.id, "payload": item.payload}



# from fastapi import FastAPI
# app = FastAPI()
#
# @app.get("/")
# def first_example():
# 	"""
# 	GFG Example First Fast API Example
# 	"""
# 	return {"GFG Example": "FastAPI"}
