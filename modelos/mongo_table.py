class MongoTable:
    _db = None

    @classmethod
    def collection(cls):
        if MongoTable._db is None:
            from pymongo import MongoClient
            conn = MongoClient('mongodb://localhost:27017/', connect=False)
            MongoTable._db = conn['viagens']
        return MongoTable._db.get_collection(cls.__name__)

    def save(self):
        record  = {
            k: v for k, v in self.__dict__.items()
            if not k.startswith('_')
        }
        key = list(record.keys())[0] # --- O primeiro campo é a chave
        self.collection().update_one(
            {key: record[key]},
            {'$set': record},
            upsert=True
        )

    @classmethod
    def find(cls, **args) -> list:
        return [cls(**o) for o in cls.collection().find(filter=args)]
