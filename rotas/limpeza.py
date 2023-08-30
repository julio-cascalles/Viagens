from fastapi import APIRouter, HTTPException
from rotas.const import EXCLUIR_HOSPEDES_INATIVOS
from modelos.hospede import Hospede
from modelos.base import STATUS_INATIVO


router = APIRouter()

@router.delete(EXCLUIR_HOSPEDES_INATIVOS)
def limpar_inativos():
    """
    Todos os hóspedes que já deixaram seus hotéis
    e não estão mais usando os serviços da API
    são marcados com STATUS_INATIVO (0).

    A **limpeza de inativos** remove esses registros
    do banco de dados e devolve os nomes das pessoas
    que foram excluídas.
    
    > Caso não encontre todos os inativos, retorna um erro.
    """
    nomes = [h.nome for h in Hospede.find(status=STATUS_INATIVO)]
    total = Hospede.delete(status=STATUS_INATIVO).deleted_count
    if total != len(nomes):
        raise HTTPException(status_code=404, detail='Erro ao excluir.')
    return 'Hóspedes inativos excluídos: {}'.format(
        ', '.join(nomes)
    )
