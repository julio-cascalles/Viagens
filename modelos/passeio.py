from datetime import datetime
from modelos.mongo_table import MongoTable


class Passeio(MongoTable):
    def __init__(self, nome: str, cidade: str, dia_semana: int):
        self.nome = nome
        self.cidade = cidade
        self.dia_semana = dia_semana
        super().__init__()

    def disponivel(self, hoje: datetime) -> bool:
        return self.dia_semana == hoje.weekday()
