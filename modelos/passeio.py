from datetime import datetime
from modelos.mongo_table import MongoTable

DIAS_SEMANA = ['dom', 'seg', 'ter', 'qua', 'qui', 'sex', 'sab']


class Passeio(MongoTable):
    def __init__(self, nome: str, cidade: str, dia_semana: str):
        self.nome = nome
        self.cidade = cidade
        self.dia_semana = dia_semana.lower()
        self._dia = DIAS_SEMANA.index(self.dia_semana)
        super().__init__()

    def disponivel(self, hoje: datetime) -> bool:
        return self._dia == hoje.weekday()
