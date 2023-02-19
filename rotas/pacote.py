from fastapi import APIRouter, HTTPException
from modelos.base import Reserva, DIAS_SEMANA
from modelos.hotel import Hotel
from modelos.passeio import Passeio
from modelos.hospede import Hospede
from rotas.enderecos import RESERVA_PACOTE, CONSUMIR_PACOTE


router = APIRouter()

@router.post(RESERVA_PACOTE)
def fazer_reserva(dados: Reserva):
    encontrados = sorted(Passeio.find(
        cidade=dados.cidade,
        nome={'$in': dados.passeios.split(',')}
    ), key = lambda p: DIAS_SEMANA.index(p.dia_semana))
    if not encontrados:
        raise HTTPException(
            status_code=404,
            detail='Nenhum passeio encontrado com essas características.'
        )
    hotel = next(iter(Hotel.find(nome=dados.hotel, cidade=dados.cidade)), None)
    quarto = hotel.reserva(dados.hospede) if hotel else -1
    if quarto == -1:
        raise HTTPException(
            status_code=400,
            detail='Não foi possível fazer a reserva nesse hotel.'
        )
    Hospede(
        nome=dados.hospede, quarto=quarto,
        passeios=[p.nome for p in encontrados],
        hotel=hotel.nome, 
    ).save()
    return f'Quarto {quarto} reservado com sucesso para {dados.hospede}'

@router.get(CONSUMIR_PACOTE)
def consumir_pacote(hospede: str):
    """
    Simula o hóspede consumindo seu pacote de passeios
    """
    encontrado = Hospede.find(nome=hospede)
    if not encontrado:
        raise HTTPException(
            status_code=404,
            detail=f'Hóspede "{hospede}" não encontrado.'
        )
    hospede = encontrado[0]
    return '{} > {}.'.format(
        hospede.nome, hospede.passeio_realizado()
    )
