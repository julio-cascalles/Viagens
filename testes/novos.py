from rotas.const import NOVO_HOTEL, NOVO_PASSEIO
from modelos import base
from testes.const import (
    HOTEL_TESTE, CIDADE_TESTE,
    DIAS_PASSEIO, LISTA_TESTE_PASSEIOS,
)


def novo_hotel(client) -> bool:
    dados = base.Hotel(
        nome=HOTEL_TESTE,
        cidade=CIDADE_TESTE,
        estrelas=2, tamanho=10,
    )
    resp = client.put(
        NOVO_HOTEL,
        json=dados.model_dump()
    )
    return resp.status_code == 200


def novos_passeios(client) -> bool:
    for passeio, dia in zip(LISTA_TESTE_PASSEIOS, DIAS_PASSEIO):
        dados = base.Passeio(
            nome=passeio, cidade=CIDADE_TESTE,
            dia_semana=dia
        )
        resp = client.put(
            NOVO_PASSEIO,
            json=dados.model_dump()
        )
        if resp.status_code != 200:
            return False
    return True
