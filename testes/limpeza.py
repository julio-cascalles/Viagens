from rotas.const import EXCLUIR_HOSPEDES_INATIVOS


def limpar_inativos(client) -> bool:
    resp = client.delete(EXCLUIR_HOSPEDES_INATIVOS)
    return resp.status_code == 200
