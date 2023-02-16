from datetime import datetime
from modelos import base
from modelos.base import DIAS_SEMANA
from modelos.mongo_table import MongoTable


class Passeio(MongoTable, base.Passeio):
    def disponivel(self, data: str) -> bool:
        if not data:
            return True
        dia_atual = DIAS_SEMANA.index(self.dia_semana)
        data = datetime.strptime(data, '%d-%m-%Y')
        return dia_atual == data.weekday()
