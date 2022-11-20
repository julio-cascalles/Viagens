from pydantic import BaseModel, validator
from modelos.passeio import DIAS_SEMANA


class Reserva(BaseModel):
    cidade: str
    hotel: str
    hospede: str
    passeios: str


class Hotel(BaseModel):
    nome: str
    estrelas : int
    cidade: str
    tamanho: int


class Passeio(BaseModel):
    nome: str
    cidade: str
    dia_semana: str

    @validator("dia_semana")
    @classmethod
    def valida_dia(cls, dia):
        dia = dia.lower()
        if dia not in DIAS_SEMANA:
            raise ValueError(f'{dia} não é um dia da semana válido.')
        return dia
    