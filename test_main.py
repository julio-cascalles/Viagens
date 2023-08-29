from fastapi.testclient import TestClient
from rotas.app import create_app
from modelos.mongo_table import MongoTable
from testes.utils import MockDatabase
from testes.novos import novo_hotel, novos_passeios
from testes.pacote import fazer_reserva, consumir_pacote
from testes.pesquisas import (
    listar_hoteis,
    listar_passeios,
    passeios_por_data
)

client = TestClient(
    create_app()
)
# ---------------------------------
# Comente a linha abaixo(*) caso queira gravar os testes no B.D.:
MongoTable._db = MockDatabase()  # <<<---- (*)
MongoTable.DATABASE_NAME = 'teste'
# ---------------------------------

rotinas = [
    novo_hotel, listar_hoteis, novos_passeios, listar_passeios,
    passeios_por_data, fazer_reserva, consumir_pacote, 
]
resultado = {func.__name__: func(client) for func in rotinas}


def test_novo_hotel():
    assert resultado['novo_hotel']

def test_listar_hoteis():
    assert resultado['listar_hoteis']

def test_novos_passeios():
    assert resultado['novos_passeios']

def test_listar_passeios():
    assert resultado['listar_passeios']

def test_passeios_por_data():
    assert resultado['passeios_por_data']

def test_fazer_reserva():
    assert resultado['fazer_reserva']

def test_consumir_pacote():
    assert resultado['consumir_pacote']
