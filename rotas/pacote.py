from fastapi import APIRouter, HTTPException
from modelos.base import Reserva
from modelos.hotel import Hotel
from modelos.passeio import Passeio
from modelos.hospede import Hospede
from rotas.const import (
    RESERVA_PACOTE, CONSUMIR_PACOTE,
    FORMATO_RETORNO_CONSUMO, OP_PCT_REALIZADO
)


router = APIRouter()

@router.post(RESERVA_PACOTE)
def fazer_reserva(dados: Reserva):
    """
    `passeios` é uma lista (separada por vírgula)
     dos passeios desejados
     > Se for vazio, traz TODOS os passeiso da cidade!

    **Observação**
    O _hospede_ só passa a existir depois que faz a reserva.
    Então **não existe** uma rota do tipo `novo/hospede`
    """
    encontrados = Passeio.amostra(dados)
    if not encontrados:
        raise HTTPException(
            status_code=404,
            detail='Nenhum passeio encontrado com essas características.'
        )
    hotel = Hotel.find_first(
        nome=dados.hotel, cidade=dados.cidade
    )
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
def consumir_pacote(hospede: str, operacao: str=OP_PCT_REALIZADO):
    """
    Simula o hóspede consumindo seu pacote de passeios
    Valores possíveis para o campos `operacao`:
    * _realizado_ (default) = Assume que o hóspede realizou o passeio
    * _cancelou_ :  Quando ele desistiu do passeio
    * _hoje_ : Realiza o passeio na data atual
    """
    encontrado = Hospede.find(nome=hospede)
    if not encontrado:
        raise HTTPException(
            status_code=404,
            detail=f'Hóspede "{hospede}" não encontrado.'
        )
    hospede = encontrado[0]
    try:
        return FORMATO_RETORNO_CONSUMO.format(
            hospede.nome, 
            Passeio.historico_gravado(
                nome=hospede.proximo_passeio(),
                hospede=hospede, operacao=operacao
            )
        )
    except Exception as e:
        return str(e)
