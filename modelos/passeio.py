from datetime import datetime
from modelos import base
from modelos.base import DIAS_SEMANA, Reserva
from modelos.mongo_table import MongoTable
from rotas.const import OP_PACOTE_HOJE


class Passeio(MongoTable, base.Passeio):
    def disponivel(self, data: str) -> bool:
        if not data:
            return True
        dia_atual = DIAS_SEMANA.index(self.dia_semana)
        if data == OP_PACOTE_HOJE:
            data = datetime.today()
        else:
            data = datetime.strptime(data, '%d-%m-%Y')
        return dia_atual == data.weekday()

    @classmethod
    def historico_gravado(cls, **args) -> str:
        hospede = args.pop('hospede').nome
        operacao = args.pop('operacao')
        passeio = cls.find_first(**args)
        if not passeio:
            return 'não existem mais passeios **'
        if operacao == OP_PACOTE_HOJE: 
            if not passeio.disponivel(OP_PACOTE_HOJE):
                raise ValueError('{} só estará disponível {}'.format(
                    passeio.nome, passeio.dia_semana
                ))
            operacao = 'realizar'
        passeio.historico[hospede] = operacao
        passeio.save()
        return passeio.nome

    @staticmethod
    def amostra(reserva: Reserva) -> list:
        def filtro(item: Passeio) -> bool:
            if not reserva.passeios:
                return True
            return item.nome in reserva.passeios
        dados = {
            p.dia_semana: p
            for p in Passeio.find(cidade=reserva.cidade)
        }
        semana_ordenada = ['dom'] + DIAS_SEMANA[:-1]
        return [
            dados[dia] for dia in semana_ordenada
            if dia in dados and filtro(dados[dia])
        ]
