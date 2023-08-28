from fastapi import APIRouter, HTTPException
from modelos import base
from modelos.hotel import Hotel
from modelos.passeio import Passeio
from rotas.const import (
    NOVO_HOTEL, NOVO_PASSEIO,
    SUCESSO_HOTEL, SUCESSO_PASSEIO
)


router = APIRouter()

@router.put(NOVO_HOTEL)
def novo_hotel(dados: base.Hotel):
    try:
        Hotel(**dados.model_dump()).save()
    except Exception as e:
        raise HTTPException(status_code=400, detail=e.errors())
    return SUCESSO_HOTEL

@router.put(NOVO_PASSEIO)
def novo_passeio(dados: base.Passeio):
    try:
        Passeio(**dados.model_dump()).save()
    except Exception as e:
        raise HTTPException(status_code=400, detail=e.errors())
    return SUCESSO_PASSEIO
