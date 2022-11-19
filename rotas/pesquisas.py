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

@router.get('/pesquisas/listar_passeios/{cidade}/{dia}')
def listar_passeios(cidade: str, dia: int):
    return [
        passeio for passeio in Passeio.find(
            cidade=cidade
        ) if passeio.disponivel(dia)
    ]
