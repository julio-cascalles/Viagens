from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection


TEST_DATABASE = 'test'

class MongoTable:
    URL_HOST = 'mongodb://localhost:27017/'
    DATABASE_NAME = ''
    _db: Database = None

    @classmethod
    def collection(cls) -> Collection:
        if MongoTable._db is None:
            conn = MongoClient(cls.URL_HOST, connect=False)
            if cls.DATABASE_NAME == TEST_DATABASE:
                conn.drop_database(cls.DATABASE_NAME)
            MongoTable._db = conn[cls.DATABASE_NAME]
        return MongoTable._db.get_collection(cls.__name__)

    def save(self, key_field_index: int = 0):
        record  = {
            k: v for k, v in self.__dict__.items()
            if not k.startswith('_')
        }
        key = list(record.keys())[key_field_index]
        self.collection().update_one(
            {key: record[key]},
            {'$set': record},
            upsert=True
        )

    @classmethod
    def find(cls, **args) -> list:
        return [
            cls(**cursor) for cursor in cls.collection().find(filter=args)
        ]

    @classmethod
    def find_first(cls, **args):
        cursor = cls.collection().find(filter=args).limit(-1)
        return cls(**cursor)

    @classmethod
    def delete(cls, **args):
        return cls.collection().delete_many(args)
