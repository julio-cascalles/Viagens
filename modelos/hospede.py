from modelos.mongo_table import MongoTable
from modelos.hotel import Hotel


class Hospede(MongoTable):
    def __init__(self, nome: str, hotel: Hotel):
        self.nome = nome
        self.hotel = hotel.nome
        self.cidade = hotel.cidade
        self.passeios = []
        super().__init__()

    def passeio_realizado(self) -> str:
        """
        Retira um passeio da lista
        """
        return self.passeios.pop(0)
