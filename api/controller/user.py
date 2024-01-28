from flask_restful import Resource
from flask import request, json

class User(Resource):
    def post(self):
        from models.user import user

        data = json.loads(request.data)
        entity = {
            "id": data["id"],
            "gender": data["gender"],
            "age": data["age"],
            "embeddings": data["embeddings"]
        }
        user.insert(entity)
        user.flush()

        return {},200
    
    def put(self):
        return {"msg": "update user"},200
    
    def delete(self):
        return {"msg": "delete user"},200
