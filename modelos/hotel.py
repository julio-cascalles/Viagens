from modelos.mongo_table import MongoTable

INFO_STATUS = lambda s, h: {'status': s, 'hospede': h}


class Hotel(MongoTable):
    def __init__(self, nome: str, cidade: str, estrelas: int, tamanho: int, **args):
        self.nome = nome
        self.cidade = cidade
        self.diaria = 50.00 * estrelas
        self.quartos = args.get('quartos',  [{}] * tamanho)
        self.estrelas = estrelas
        self.tamanho = tamanho

    def reserva(self, hospede: str) -> int:
        for i, ocupado in enumerate(self.quartos):
            if not ocupado:
                self.quartos[i] = INFO_STATUS('reserva', hospede)
                self.save()
                return i
        return -1
    
    def check_in(self, hospede: str, quarto: int):
        reserva = self.quartos[quarto]
        if reserva != INFO_STATUS('reserva', hospede):
            raise Exception('Quarto {} não está reservado para {}.'.format(
                quarto, hospede
            ))
        self.quartos[quarto] = INFO_STATUS('ocupado', hospede)
        self.save()

    def check_out(self, quarto: int):
        self.quartos[quarto] = {}
        self.save()
