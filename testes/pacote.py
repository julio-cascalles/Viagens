from modelos.base import Reserva
from testes.const import (
    CIDADE_TESTE, HOSPEDE_TESTE, HOTEL_TESTE,
    LISTA_TESTE_PASSEIOS, ITEM_PASSEIO_PARQUE
)
from rotas.const import (
    RESERVA_PACOTE, CONSUMIR_PACOTE,
    FORMATO_RETORNO_CONSUMO
)


def fazer_reserva(client) -> bool:
    dados = Reserva(
        cidade=CIDADE_TESTE, hospede=HOSPEDE_TESTE,
        hotel=HOTEL_TESTE, passeios=','.join(LISTA_TESTE_PASSEIOS),
    )
    resp = client.post(
        RESERVA_PACOTE,
        json=dados.model_dump()
    )
    return resp.status_code == 200

def consumir_pacote(client) -> bool:
    resp = client.post(CONSUMIR_PACOTE.format(
        hospede=HOSPEDE_TESTE
    ))
    if resp.status_code == 404:
        return False
    esperado = FORMATO_RETORNO_CONSUMO.format(
        HOSPEDE_TESTE, ITEM_PASSEIO_PARQUE
    )
    return resp.json() == esperado
