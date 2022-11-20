import json
from pymongo import MongoClient


class MongoTable:
    _db = None
    _collection = None

    @classmethod
    def config(cls):
        if MongoTable._db is None:
            conn = MongoClient('mongodb://localhost:27017/', connect=False)
            MongoTable._db = conn['viagens']
        cls._collection = MongoTable._db.get_collection(cls.__name__)
        return cls._collection

    def save(self):
        record  = {
            k: v for k, v in self.__dict__.items()
            if not k.startswith('_')
        }
        key = list(record.keys())[0] # --- O primeiro campo é a chave
        self._collection.update_one(
            {key: record[key]},
            {'$set': record},
            upsert=True
        )

    @classmethod
    def find(cls, **args) -> list:
        return [cls(**o) for o in cls.config().find(filter=args)]
