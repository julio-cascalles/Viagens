from fastapi import APIRouter
from modelos.parametros import Reserva
from modelos.hotel import Hotel
from modelos.passeio import Passeio
from modelos.hospede import Hospede


router = APIRouter()

@router.post('/pacote/reserva')
def fazer_reserva(dados: Reserva):
    encontrados = sorted(Passeio.find(
        cidade=dados.cidade,
        nome={'$in': dados.passeios.split(',')}
    ), key = lambda p: p.dia_semana)
    if not encontrados:
        raise Exception('Nenhum passeio encontrado com essas características.')
    hotel = next(iter(Hotel.find(nome=dados.hotel, cidade=dados.cidade)), None)
    quarto = hotel.reserva(dados.hospede) if hotel else -1
    if quarto == -1:
        raise Exception('Não foi possível fazer a reserva nesse hotel.')
    Hospede(
        nome=dados.hospede, quarto=quarto,
        passeios=encontrados, hotel=hotel, 
    ).save()
    return f'Quarto {quarto} reservado para o hóspede'

@router.get('/pacote/consumir/{hospede}')
def consumir_pacote(hospede: str):
    """
    Simula o hóspede consumindo seu pacote de passeios
    """
    return '{} > {}.'.format(
        hospede,
        Hospede.find(nome=hospede)[0].passeio_realizado()
    )
