from fastapi import APIRouter, HTTPException
from modelos.base import Reserva, DIAS_SEMANA
from modelos.hotel import Hotel
from modelos.passeio import Passeio
from modelos.hospede import Hospede
from rotas.const import (
    RESERVA_PACOTE, CONSUMIR_PACOTE,
    FORMATO_RETORNO_CONSUMO
)


router = APIRouter()

@router.post(RESERVA_PACOTE)
def fazer_reserva(dados: Reserva):
    """
    **Observação**
    O _hospede_ só passa a existir depois que faz a reserva.
    Então **não existe** uma rota do tipo `novo/hospede`
    """
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
    if hotel:
        quarto = hotel.reserva(dados.hospede)
        if quarto == -1:
            erro = 'Não foi possível fazer a reserva nesse hotel.'
        else:
            outro_hotel = Hospede.hotel_atual(dados.hospede)
            if outro_hotel:
                erro = '{} já está hospedado em {}'.format(
                    dados.hospede, outro_hotel
                )
            else:
                Hospede(
                    nome=dados.hospede, quarto=quarto,
                    passeios=[p.nome for p in encontrados],
                    hotel=hotel.nome, 
                ).save()
                erro = ''
    else:
        erro = 'Hotel não encontrado.'
    if erro:
        raise HTTPException(status_code=400, detail=erro)
    return f'Quarto {quarto} reservado com sucesso para {dados.hospede}'

@router.post(CONSUMIR_PACOTE)
def consumir_pacote(hospede: str, realizar: int=1):
    """
    Simula o hóspede consumindo seu pacote de passeios
    > Coloque `realizar` como 0 caso queira desistir do passeio
    """
    encontrado = Hospede.find(nome=hospede)
    if not encontrado:
        raise HTTPException(
            status_code=404,
            detail=f'Hóspede "{hospede}" não encontrado.'
        )
    hospede = encontrado[0]
    return FORMATO_RETORNO_CONSUMO.format(
        hospede.nome, 
        Passeio.grava_historico(
            nome=hospede.proximo_passeio(),
            hospede=hospede, cancelado=(realizar==0)
        )
    )
