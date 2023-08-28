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
# MongoTable._db = MockDatabase()  # <<<---- (*)
MongoTable.DATABASE_NAME = 'teste'
# ---------------------------------

def test_novo_hotel():
    novo_hotel(client)

def test_novos_passeios():
    novos_passeios(client)

def test_fazer_reserva():
    novo_hotel(client)
    novos_passeios(client)
    fazer_reserva(client)

def test_consumir_pacote():
    novo_hotel(client)
    novos_passeios(client)
    fazer_reserva(client)
    consumir_pacote(client)

def test_listar_hoteis():
    novo_hotel(client)
    listar_hoteis(client)

def test_listar_passeios():
    novos_passeios(client)
    listar_passeios(client)

def test_passeios_por_data():
    novos_passeios(client)
    passeios_por_data(client)
