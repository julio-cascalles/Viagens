from fastapi import APIRouter
from modelos.hotel import Hotel
from modelos.passeio import Passeio


router = APIRouter()

@router.get('/pacote/reserva/{cidade}/{hotel}/{hospede}/{passeios}')
def fazer_reserva(cidade: str, hotel: str, hospede: str, passeios: str):
    encontrados = sorted(Passeio.find(
        cidade=cidade,
        nome={'$in': passeios.split(',')}
    ), key = lambda p: p.dia_semana)
    if not encontrados:
        raise Exception('Nenhum passeio encontrado com essas características.')
    hotel = Hotel.find(nome=hotel, cidade=cidade)
    quarto = hotel.reserva(hospede) if hotel else -1
    if quarto == -1:
        raise Exception('Não foi possível fazer a reserva nesse hotel.')
    Hospede(
        nome=hospede, passeios=encontrados,
        hotel=hotel, quarto=quarto
    ).save()

@router.get('/pacote/consumir/{hospede}')
def consumir_pacote(hospede: str):
    """
    Simula o hóspede consumindo seu pacote de passeios
    """
    return '{} realizou o passeio {}.'.format(
        hospede,
        Hospede.find(nome=hospede).passeio_realizado()
    )
