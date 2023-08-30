from datetime import datetime
from modelos.mongo_table import MongoTable
from modelos import base
from modelos.base import STATUS_INATIVO, STATUS_HOSPEDADO
from modelos.hotel import Hotel
from modelos.passeio import Passeio


class Hospede(MongoTable, base.Hospede):
    def proximo_passeio(self) -> str:
        """
        Primeiro procura o `hotel` do Hospede
        Depois retira um passeio da lista
        """
        hotel = Hotel.find_first(nome=self.hotel)
        if not hotel:
            raise ValueError('O hotel {} já não existe mais.'.format(
                self.hotel
            ))
        if len(self.passeios) == 0:
            hotel.check_out(self.quarto)
            self.status = STATUS_INATIVO
            self.save()
            return ''
        if self.status != STATUS_HOSPEDADO:
            hotel.check_in(
                hospede=self.nome,
                quarto=self.quarto
            )
            self.status = STATUS_HOSPEDADO
        passeio = self.passeios.pop(0)
        self.save()
        return passeio

    @classmethod
    def hotel_atual(cls, nome: str) -> str:
        hospede = cls.find_first(nome=nome)
        if hospede and hospede.status == STATUS_HOSPEDADO:
            return hospede.hotel
        return ''
