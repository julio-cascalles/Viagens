class MockCollection:
    def __init__(self):
        self.__data = {}

    def update_one(self, filter:dict , info: dict, **args):
        key = list(filter.values())[0]
        self.__data[key] = info['$set']

    def find(self, **filter):
        filter = filter['filter']
        def compara(registro):
            for campo, expr in filter.items():
                val = registro[campo]
                if isinstance(expr, dict) and '$in' in expr:
                    if val not in expr["$in"]:
                        return False
                elif val != expr:
                    return False
            return True
        return [d for d in self.__data.values() if compara(d)]


class MockDatabase:
    def __init__(self):
        self.collections = {}

    def get_collection(self, name: str):
        if name not in self.collections:
            self.collections[name] = MockCollection()
        return self.collections[name]
