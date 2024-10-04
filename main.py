from fastapi import FastAPI
from enum import Enum
from typing import Optional

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/")
async def post():
    return {"message": "From POST root"}

@app.put("/")
async def put():
    return {"message": "From PUT root"}

@app.get("/users")
async def list_users():
    return {"message": "List of users"}

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"message": f"User {user_id}"} 

@app.get("users/me")
async def get_current_user():
    return {"message": "Current User"}


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"

@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.fruits:
        return {"Food Name": food_name,
                "Message": "Fruits are good for health"}
    elif food_name == FoodEnum.vegetables:
        return {"Food Name": food_name,
                "Message": "Vegetables are good for health"}
    else:
        return {"Food Name": food_name,
                "Message": "Dairy products are good for health"}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

@app.get("/items/{item_id}")
async def get_item(item_id: int, sample_query_param: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id, "sample_query_param": sample_query_param}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})
    return item

@app.get("users/{user_id}/items/{item_id}")
async def get_user_item(user_id: int, item_id: str, q: Optional[str] | None = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})
    return item