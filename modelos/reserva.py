from pydantic import BaseModel

class Reserva(BaseModel):
    cidade: str
    hotel: str
    hospede: str
    passeios: str
