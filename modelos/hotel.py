from modelos.mongo_table import MongoTable
from modelos import parametros


class Hotel(MongoTable):
    def __init__(self, nome: str, cidade: str, estrelas: int, tamanho: int):
        self.nome = nome
        self.cidade = cidade
        self.diaria = 50.00 * estrelas
        self.quartos = [{}] * tamanho
        self._status = lambda s, h: {'status': s, 'hospede': h}
        super().__init__()

    def reserva(self, hospede: str) -> int:
        for i, ocupado in enumerate(self.quartos):
            if not ocupado:
                self.quartos[i] = self._status('reserva', hospede)
                return i
                self.save()
        return -1
    
    def check_in(self, hospede: str, quarto: int):
        reserva = self.quartos[quarto]
        if reserva != self._status('reserva', hospede):
            raise Exception('Quarto {} não está reservado para {}.'.format(
                quarto, hospede
            ))
        self.quarto[quarto] = self._status('ocupado', hospede)
        self.save()

    def check_out(self, quarto: int):
        self.quartos[quarto] = {}
        self.save()
