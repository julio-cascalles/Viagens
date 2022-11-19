import os
from pymongo import MongoClient


class MongoTable:
    _db = None

    def __init__(self):
        table_name = self.__class__.__name__
        if not self._db:
            conn = MongoClient('mongodb://localhost:27017/')
            self._db = conn['fome_DQ']
        self._collection = self._db.get_collection(table_name)

    def save(self):
        record  = self.__data()
        key = list(record.keys())[0] # --- O primeiro campo é a chave
        self._collection.update_one(
            {key: record[key]},
            {'$set': record},
            upsert=True
        )

    def __data(self) -> dict:
        return {
            k: str(v) for k, v in self.__dict__.items()
            if not k.startswith('_') and v
        }

    def find(self) -> list:
        return list(self._collection.find(filter=self.__data()))
