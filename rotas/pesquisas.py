from fastapi import APIRouter
from modelos.hotel import Hotel
from modelos.passeio import Passeio
from rotas.enderecos import (
    LISTAR_HOTEIS,
    LISTAR_PASSEIOS,
    LISTAR_PASSEIOS_POR_DATA
)


QUARTO_VAZIO = {}


router = APIRouter()

@router.get(LISTAR_HOTEIS)
def listar_hoteis(cidade: str):
    return [
        hotel for hotel in Hotel.find(
            cidade=cidade
        ) if QUARTO_VAZIO in hotel.quartos
    ]

@router.get(LISTAR_PASSEIOS)
@router.get(LISTAR_PASSEIOS_POR_DATA)
def listar_passeios(cidade: str, data: str=''):
    return [
        passeio for passeio in Passeio.find(
            cidade=cidade
        ) if passeio.disponivel(data)
    ]
