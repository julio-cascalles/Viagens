from rotas.const import (
    LISTAR_HOTEIS,
    LISTAR_PASSEIOS,
    LISTAR_PASSEIOS_POR_DATA
)
from testes.const import (
    HOTEL_TESTE, ITEM_PASSEIO_GRUTA,
    CIDADE_TESTE, LISTA_TESTE_PASSEIOS,
)


def listar_hoteis(client) -> bool:
    resp = client.get(LISTAR_HOTEIS.format(cidade=CIDADE_TESTE))
    nomes = [r['nome'] for r in resp.json()]
    return nomes == [HOTEL_TESTE]

def listar_passeios(client) -> bool:
    resp = client.get(LISTAR_PASSEIOS.format(cidade=CIDADE_TESTE))
    nomes = [r['nome'] for r in resp.json()]
    return sorted(nomes) == sorted(LISTA_TESTE_PASSEIOS)

def passeios_por_data(client):
    resp = client.get(LISTAR_PASSEIOS_POR_DATA.format(
        cidade=CIDADE_TESTE, data='01-12-2022'
    ))
    nomes = [r['nome'] for r in resp.json()]
    return nomes == [ITEM_PASSEIO_GRUTA]
