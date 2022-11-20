from datetime import datetime
from modelos.mongo_table import MongoTable

DIAS_SEMANA = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']


class Passeio(MongoTable):
    def __init__(self, nome: str, cidade: str, dia_semana: str, **args):
        self.nome = nome
        self.cidade = cidade
        self.dia_semana = dia_semana.lower()
        self._dia = DIAS_SEMANA.index(self.dia_semana)
        self.config()

    def disponivel(self, data: str) -> bool:
        if not data:
            return True
        data = datetime.strptime(data, '%d-%m-%Y')
        print('='*50)
        print(DIAS_SEMANA[data.weekday()])
        print('-'*50)
        return self._dia == data.weekday()
