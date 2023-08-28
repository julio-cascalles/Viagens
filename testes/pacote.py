from modelos.base import Reserva
from testes.const import (
    CIDADE_TESTE, HOSPEDE_TESTE, HOTEL_TESTE,
    LISTA_PASSEIOS, ITEM_PASSEIO_PARQUE
)
from rotas.const import (
    RESERVA_PACOTE, CONSUMIR_PACOTE,
    FORMATO_RETORNO_CONSUMO
)


def fazer_reserva(client):
    dados = Reserva(
        cidade=CIDADE_TESTE, hospede=HOSPEDE_TESTE,
        hotel=HOTEL_TESTE, passeios=','.join(LISTA_PASSEIOS),
    )
    resp = client.post(
        RESERVA_PACOTE,
        json=dados.model_dump()
    )
    assert resp.status_code == 200

def consumir_pacote(client):
    resp = client.post(CONSUMIR_PACOTE.format(
        hospede=HOSPEDE_TESTE
    ))
    assert resp.status_code == 200
    esperado = FORMATO_RETORNO_CONSUMO.format(
        HOSPEDE_TESTE, ITEM_PASSEIO_PARQUE
    )
    assert resp.json() == esperado
