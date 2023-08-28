from rotas.const import (
    LISTAR_HOTEIS,
    LISTAR_PASSEIOS,
    LISTAR_PASSEIOS_POR_DATA
)
from testes.const import (
    HOTEL_TESTE, ITEM_PASSEIO_GRUTA,
    CIDADE_TESTE, LISTA_PASSEIOS,
)


def listar_hoteis(client):
    resp = client.get(LISTAR_HOTEIS.format(cidade=CIDADE_TESTE))
    encontrados = resp.json()
    assert resp.status_code == 200
    assert encontrados
    assert encontrados[0]['nome'] == HOTEL_TESTE

def listar_passeios(client):
    resp = client.get(LISTAR_PASSEIOS.format(cidade=CIDADE_TESTE))
    encontrados = resp.json()
    assert resp.status_code == 200
    nomes = [e['nome'] for e in encontrados]
    assert nomes == LISTA_PASSEIOS

def passeios_por_data(client):
    resp = client.get(LISTAR_PASSEIOS_POR_DATA.format(
        cidade=CIDADE_TESTE, data='01-12-2022'
    ))
    encontrados = resp.json()
    assert resp.status_code == 200
    assert encontrados
    assert encontrados[0]['nome'] == ITEM_PASSEIO_GRUTA
