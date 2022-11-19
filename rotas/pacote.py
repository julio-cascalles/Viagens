from fastapi import APIRouter
from modelos.reserva import Reserva
from modelos.hotel import Hotel
from modelos.passeio import Passeio


router = APIRouter()

@router.post('/pacote/reserva')
def fazer_reserva(dados: Reserva):
    encontrados = sorted(Passeio.find(
        cidade=dados.cidade,
        nome={'$in': dados.passeios.split(',')}
    ), key = lambda p: p.dia_semana)
    if not encontrados:
        raise Exception('Nenhum passeio encontrado com essas características.')
    hotel = Hotel.find(nome=dados.hotel, cidade=dados.cidade)
    quarto = hotel.reserva(dados.hospede) if hotel else -1
    if quarto == -1:
        raise Exception('Não foi possível fazer a reserva nesse hotel.')
    Hospede(
        nome=dados.hospede, quarto=quarto
        passeios=encontrados, hotel=hotel, 
    ).save()
    return f'Quarto {quarto} reservado para o hóspede'

@router.get('/pacote/consumir/{hospede}')
def consumir_pacote(hospede: str):
    """
    Simula o hóspede consumindo seu pacote de passeios
    """
    return '{} realizou o passeio {}.'.format(
        hospede,
        Hospede.find(nome=hospede).passeio_realizado()
    )
