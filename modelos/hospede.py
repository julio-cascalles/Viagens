from modelos.mongo_table import MongoTable
from modelos.hotel import Hotel

STATUS_INATIVO = 0
STATUS_RESERVA = 1
STATUS_HOSPEDADO = 2


class Hospede(MongoTable):
    def __init__(self, nome: str, hotel: Hotel, quarto:int, passeios=[]):
        self.nome = nome
        self._hotel = hotel
        self.hotel = hotel.nome
        self.quarto = quarto
        self.cidade = hotel.cidade
        self.passeios = passeios
        self.status = STATUS_RESERVA
        super().__init__()

    def passeio_realizado(self) -> str:
        """
        Retira um passeio da lista
        """
        if len(self.passeios) == 0:
            self._hotel.check_out(self.quarto)
            self.status = STATUS_INATIVO
            self.save()
            return ''
        if self.status != STATUS_HOSPEDADO:
            self._hotel.check_in(
                hospede=self.nome,
                quarto=self.quarto
            )
        return self.passeios.pop(0)
