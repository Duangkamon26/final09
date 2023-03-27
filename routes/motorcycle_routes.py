from fastapi import APIRouter

from models.motorcycles_model import Motorcycle
from config.database import collection_name

from schemas.motorcycles_schema import motorcycles_serializers, motorcycle_serializer
from bson import ObjectId

motorcycle_api_router = APIRouter()

@motorcycle_api_router.get("/hello")
async def get_hello():
    return {"msg":"Hello World"}

# retrieve
@motorcycle_api_router.get("/")
async def get_motorcycles():
    motorcycles = motorcycles_serializers(collection_name.find())
    return motorcycles

@motorcycle_api_router.get("/{id}")
async def get_motorcycle(id: str):
    # return {"test": id}
    return motorcycle_serializer(collection_name.find_one({"_id": ObjectId(id)}))


# post
@motorcycle_api_router.post("/")
async def create_motorcycle(motorcycle: Motorcycle):
    _id = collection_name.insert_one(dict(motorcycle))
    return motorcycles_serializers(collection_name.find({"_id": _id.inserted_id}))


# update
@motorcycle_api_router.put("/{id}")
async def update_motorcycle(id: str, motorcycle: Motorcycle):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(motorcycle)
    })
    return motorcycles_serializers(collection_name.find({"_id": ObjectId(id)}))

# delete
@motorcycle_api_router.delete("/{id}")
async def delete_motorcycle(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok"}