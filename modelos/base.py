from pydantic import BaseModel, field_validator

DIAS_SEMANA = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']
STATUS_INATIVO, STATUS_RESERVA, STATUS_HOSPEDADO = 0, 1, 2


class Reserva(BaseModel):
    cidade: str
    hotel: str
    hospede: str
    passeios: str


class Hospede(BaseModel):
    nome: str
    hotel: str
    quarto: int
    passeios: list
    status: int = STATUS_RESERVA


class Hotel(BaseModel):
    nome: str
    cidade: str
    tamanho: int
    quartos: list = []


class Passeio(BaseModel):
    nome: str
    cidade: str
    dia_semana: str
    historico: dict={}

    @field_validator("dia_semana")
    @classmethod
    def valida_dia(cls, dia):
        dia = dia.lower()
        if dia not in DIAS_SEMANA:
            raise ValueError(f'{dia} não é um dia da semana válido.')
        return dia
