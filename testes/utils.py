class MockCollection:

    FUNC = {
        '$in': lambda c, v: c in v,
        '$gt': lambda c, v: c > v,
        '$gte' : lambda c, v: c >= v,
        '$lt': lambda c, v: c < v,
        '$lte' : lambda c, v: c <= v,
        '$eq': lambda c, v: c == v
    }  

    def __init__(self):
        self.__data = {}

    def update_one(self, filter:dict , info: dict, **args):
        key = list(filter.values())[0]
        self.__data[key] = info['$set']

    def find(self, **args):
        TO_DICT = lambda x: x if isinstance(x, dict) else {'$eq': x}
        def compare(rec):
            for field, expr in args['filter'].items():
                curr = rec[field]
                if not all(self.FUNC[k](curr, v) for k, v in TO_DICT(expr).items()):
                    return False
            return True
        return [d for d in self.__data.values() if compare(d)]


class MockDatabase:
    def __init__(self):
        self.collections = {}

    def get_collection(self, name: str):
        if name not in self.collections:
            self.collections[name] = MockCollection()
        return self.collections[name]
