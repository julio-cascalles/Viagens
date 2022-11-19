from modelos.mongo_table import MongoTable


class Hotel(MongoTable):
    def __init__(self, nome: str, cidade: str, estrelas: int, tamanho: int):
        self.nome = nome
        self.cidade = cidade
        self.diaria = 50 * estrelas
        self.quartos = [{}] * tamanho
        self._status = lambda s, h: {'status': s, 'hospede': h}
        super().__init__()

    def reserva(self, hospede: str) -> bool:
        for i, ocupado in enumerate(self.quartos):
            if not ocupado:
                self.quartos[i] = self._status('reserva', hospede)
                return True
        return False
    
    def check_in(self, hospede: str, quarto: int):
        reserva = self.quartos[quarto]
        if reserva != self._status('reserva', hospede):
            raise Exception('Quarto {} não está reservado para {}.'.format(
                quarto, hospede
            ))
        self.quarto[quarto] = self._status('ocupado', hospede)

    def check_out(self, quarto: int):
        self.quartos[quarto] = ''
