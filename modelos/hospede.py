from modelos.mongo_table import MongoTable
from modelos.hotel import Hotel

STATUS_INATIVO = 0
STATUS_RESERVA = 1
STATUS_HOSPEDADO = 2


class Hospede(MongoTable):
    def __init__(self, nome: str, hotel: Hotel, quarto:int, passeios=[], **args):
        self.nome = nome
        if isinstance(hotel, str):
            hotel = Hotel.find(nome=hotel)[0]
        self._hotel = hotel
        self.hotel = hotel.nome
        self.quarto = quarto
        self.cidade = hotel.cidade
        self.passeios = [
            p.nome if hasattr(p, 'nome') else p
            for p in passeios
        ]
        self.status = args.get('status', STATUS_RESERVA)

    def passeio_realizado(self) -> str:
        """
        Retira um passeio da lista
        """
        if len(self.passeios) == 0:
            self._hotel.check_out(self.quarto)
            self.status = STATUS_INATIVO
            self.save()
            return 'deixando o hotel ***'
        if self.status != STATUS_HOSPEDADO:
            self._hotel.check_in(
                hospede=self.nome,
                quarto=self.quarto
            )
            self.status = STATUS_HOSPEDADO
        proximo = self.passeios.pop(0)
        self.save()
        return proximo
