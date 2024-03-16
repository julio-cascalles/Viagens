"""
Contém as constantes com
todos os endereços da API
"""

NOVO_HOTEL = '/novo/hotel'
NOVO_PASSEIO = '/novo/passeio'
RESERVA_PACOTE = '/pacote/reserva'
CONSUMIR_PACOTE = '/pacote/consumir/{hospede}'
LISTAR_HOTEIS = '/lista/hoteis/{cidade}'
LISTAR_PASSEIOS = '/lista/passeios/{cidade}'
LISTAR_PASSEIOS_POR_DATA = '/lista/passeios/{cidade}/{data}'
EXCLUIR_HOSPEDES_INATIVOS = '/hospedes/limpar_inativos'

SUCESSO_HOTEL = 'Hotel gravado com sucesso!'
SUCESSO_PASSEIO = 'Passeio gravado com sucesso!'

FORMATO_RETORNO_CONSUMO = '{} > {}.'

OP_PCT_REALIZADO = 'realizado'
OP_CANCELOU_PCT = 'cancelou'
OP_PACOTE_HOJE = 'hoje'
OPERACOES_POSSIVEIS = [OP_PCT_REALIZADO, OP_CANCELOU_PCT, OP_PACOTE_HOJE]