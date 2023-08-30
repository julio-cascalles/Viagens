from fastapi import APIRouter, HTTPException
from rotas.const import EXCLUIR_HOSPEDES_INATIVOS
from modelos.hospede import Hospede
from modelos.base import STATUS_INATIVO


router = APIRouter()

@router.delete(EXCLUIR_HOSPEDES_INATIVOS)
def limpar_inativos():
    nomes = [h.nome for h in Hospede.find(status=STATUS_INATIVO)]
    total = Hospede.delete(status=STATUS_INATIVO).deleted_count
    if total != len(nomes):
        raise HTTPException(status_code=404, detail='Erro ao excluir.')
    return 'Hóspedes inativos excluídos: {}'.format(
        ', '.join(nomes)
    )
