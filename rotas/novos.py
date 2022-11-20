from fastapi import APIRouter
from modelos import parametros
from modelos.hotel import Hotel
from modelos.passeio import Passeio


router = APIRouter()

@router.put('/novo/hotel')
def novo_hotel(dados: parametros.Hotel):
    Hotel(**dados.__dict__).save()
    return 'Hotel gravado'

@router.put('/novo/passeio')
def novo_passeio(dados: parametros.Passeio):
    Passeio(**dados.__dict__).save()
    return 'Passeio gravado'
