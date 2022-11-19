from datetime import datetime
from fastapi import APIRouter
from modelos.hotel import Hotel
from modelos.passeio import Passeio


QUARTO_VAZIO = {}


router = APIRouter()

@router.get('/pesquisas/listar_hoteis/{cidade}')
def listar_hoteis(cidade: str):
    # [To-Do] : Gerar HTTPException caso nada seja encontrado
    return [
        hotel for hotel in Hotel.find(
            cidade=cidade
        ) if QUARTO_VAZIO in hotel
    ]

@router.get('/pesquisas/listar_passeios/{cidade}')
@router.get('/pesquisas/listar_passeios/{cidade}/{data}')
def listar_passeios(cidade: str, data: str=''):
    if not data:
        dia = datetime.today()
    else:
        dia = datetime.strptime(data, '%d/%m/%Y')
    return [
        passeio for passeio in Passeio.find(
            cidade=cidade
        ) if passeio.disponivel(dia)
    ]
