from flask_restful import Resource
from models.store import *

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {"message": "store not found"}

    def post(self,name):
        store_name = StoreModel.find_by_name(name)
        if store_name:
            return {"message":"Store already exists"}, 400
        store = StoreModel(name)

        store.save_to_db()
        return store.json(), 201

    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {"message":"store deleted"}

class StoreList(Resource):
    def get(self):
        return {"store":[store.json() for store in StoreModel.query.all()]}

