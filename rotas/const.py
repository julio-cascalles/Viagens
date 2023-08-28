"""
Contém as constantes com
todos os endereços da API
"""

NOVO_HOTEL = '/novo/hotel'
NOVO_PASSEIO = '/novo/passeio'
RESERVA_PACOTE = '/pacote/reserva'
CONSUMIR_PACOTE = '/pacote/consumir/{hospede}'
LISTAR_HOTEIS = '/pesquisas/listar_hoteis/{cidade}'
LISTAR_PASSEIOS = '/pesquisas/listar_passeios/{cidade}'
LISTAR_PASSEIOS_POR_DATA = '/pesquisas/listar_passeios/{cidade}/{data}'

SUCESSO_HOTEL = 'Hotel gravado com sucesso!'
SUCESSO_PASSEIO = 'Passeio gravado com sucesso!'

FORMATO_RETORNO_CONSUMO = '{} > {}.'