from rotas.enderecos import RESERVA_PACOTE, CONSUMIR_PACOTE
from modelos.base import Reserva
from testes.const import (
    HOTEL_TESTE, CIDADE_TESTE, HOSPEDE_TESTE,
    ITEM_PASSEIO_PARQUE, PASSEIOS_TESTE, 
)


def fazer_reserva(client):
    dados = Reserva(
        cidade=CIDADE_TESTE, hospede=HOSPEDE_TESTE,
        hotel=HOTEL_TESTE, passeios=PASSEIOS_TESTE,
    )
    resp = client.post(
        RESERVA_PACOTE,
        json=dados.dict()
    )
    assert resp.status_code == 200

def consumir_pacote(client):
    resp = client.get(CONSUMIR_PACOTE.format(
        hospede=HOSPEDE_TESTE
    ))
    assert resp.status_code == 200
    esperado = '{} > {}.'.format(
        HOSPEDE_TESTE, ITEM_PASSEIO_PARQUE
    )
    assert resp.json() == esperado
