from modelos.mongo_table import MongoTable
from modelos import base
from modelos.base import STATUS_INATIVO, STATUS_HOSPEDADO
from modelos.hotel import Hotel


class Hospede(MongoTable, base.Hospede):
    def passeio_realizado(self) -> str:
        """
        Primeiro procura o `hotel` do Hospede
        Depois retira um passeio da lista
        """
        encontrado = Hotel.find(nome=self.hotel)
        if not encontrado:
            raise ValueError('O hotel {} já não existe mais.'.format(
                self.hotel
            ))
        hotel = encontrado[0]
        if len(self.passeios) == 0:
            hotel.check_out(self.quarto)
            self.status = STATUS_INATIVO
            self.save()
            return 'deixando o hotel ***'
        if self.status != STATUS_HOSPEDADO:
            hotel.check_in(
                hospede=self.nome,
                quarto=self.quarto
            )
            self.status = STATUS_HOSPEDADO
        proximo = self.passeios.pop(0)
        self.save()
        return proximo
